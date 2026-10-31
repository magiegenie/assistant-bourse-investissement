"""Importe un relevé d'opérations exporté du courtier ou de la banque (CSV) :
python scripts/importer_releve.py prive/<prenom> <releve.csv> [--enveloppe PEA] [--simulation]

- Détecte l'encodage, le séparateur, les décimales à la française et les colonnes (table templates/courtiers.csv,
  à enrichir quand un courtier utilise d'autres noms de colonnes).
- Reconnaît le type d'opération (achat, vente, versement, retrait, dividende, frais, intérêts) en français, anglais, allemand.
- Écarte les opérations déjà importées ou déjà présentes dans transactions.csv (date, ISIN, quantité, montant).
- Écrit prive/<prenom>/import-<date>.xlsx (complété si plusieurs relevés le même jour), au format des colonnes A à J
  de la feuille Transactions du Google Sheet, à coller tel quel, et liste les actifs à ajouter dans la feuille Actifs.
Ne demande et ne lit jamais d'identifiants bancaires : on part d'un fichier exporté par la personne.
"""
import csv
import io
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from fichiers_profil import TEMPLATES, ecrire_csv, lire_csv, lire_parametres, nombre

TYPES = [  # (mots reconnus, type du Sheet) : le premier qui correspond l'emporte
    (("dividend", "coupon", "ausschuttung", "distribution"), "Dividende"),
    (("interet", "interest", "zins"), "Intérêts"),
    (("retrait", "withdraw", "auszahlung", "virement sortant", "payout"), "Retrait"),
    (("versement", "depot", "deposit", "einzahlung", "virement entrant", "apport", "alimentation", "top up"), "Versement"),
    (("frais", "fee", "gebuhr", "commission", "droits de garde"), "Frais"),
    (("vente", "sell", "verkauf", "cession", "sale"), "Vente"),
    (("achat", "buy", "kauf", "purchase", "souscription", "savings plan", "sparplan", "plan d'investissement"), "Achat"),
]
ENTETES_SHEET = ["Date", "Utilisateur", "Enveloppe", "Type d'opération", "ID actif", "Quantité",
                 "Prix unitaire (ou montant)", "Frais de courtage", "Devise", "Taux de change (1 si EUR)"]


def simple(t):
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode().lower()
    return " ".join(t.replace("_", " ").split())


def lire_fichier(chemin):
    brut = Path(chemin).read_bytes()
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            texte = brut.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    lignes = [l for l in texte.splitlines() if l.strip()]
    sep = max((";", ",", "\t", "|"), key=lambda s: lignes[0].count(s))
    # Certains relevés ont des lignes d'en-tête avant le tableau : on prend la première ligne qui contient une date et un montant
    synonymes = {r["champ"]: r["synonymes"].split("|") for r in lire_csv(TEMPLATES / "courtiers.csv")}
    debut = 0
    for i, l in enumerate(lignes[:20]):
        cols = [simple(c) for c in l.split(sep)]
        if any(c in synonymes["date"] for c in cols):
            debut = i
            break
    lecteur = csv.reader(io.StringIO("\n".join(lignes[debut:])), delimiter=sep)
    entete = [simple(c) for c in next(lecteur)]
    correspondance = {}
    for champ, syn in synonymes.items():
        for j, c in enumerate(entete):
            if c in syn and champ not in correspondance:
                correspondance[champ] = j
    return [r for r in lecteur if any(x.strip() for x in r)], correspondance, entete


def date_iso(t):
    t = str(t).strip()[:19]
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d.%m.%Y", "%d-%m-%Y", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%d/%m/%y", "%m/%d/%Y"):
        try:
            return datetime.strptime(t if "T" in fmt or " %H" in fmt else t[:10], fmt).date().isoformat()
        except ValueError:
            pass
    return ""


def type_operation(texte, quantite, montant):
    s = simple(texte)
    for mots, typ in TYPES:
        if any(m in s for m in mots):
            return typ
    if quantite:
        return "Achat" if montant < 0 or not montant else "Vente"
    return "Versement" if montant > 0 else "Retrait" if montant < 0 else ""


def cle(d, isin, q, m):
    return f"{d}|{isin}|{round(abs(q), 4)}|{round(abs(m), 2)}"


def main(dossier, fichier, enveloppe=None, simulation=False):
    d = Path(dossier)
    params = lire_parametres(d)
    lignes, corr, entete = lire_fichier(fichier)
    manquants = [c for c in ("date", "montant") if c not in corr]
    if manquants:
        sys.exit(f"Colonnes introuvables : {', '.join(manquants)}. En-têtes lus : {entete}. "
                 "Ajouter le nom de ces colonnes dans templates/courtiers.csv.")
    deja = {r["cle"] for r in lire_csv(d / "imports-faits.csv")}
    connus = {}
    for t in lire_csv(d / "transactions.csv"):
        deja.add(cle(t["date"], t.get("isin", ""), nombre(t["quantite"]), nombre(t["montant_eur"])))
        if t.get("isin"):
            connus[t["isin"]] = t["id_actif"]
    val = lambda r, champ: r[corr[champ]].strip() if champ in corr and corr[champ] < len(r) else ""
    nouvelles, doublons, a_ajouter, ignorees = [], 0, {}, 0
    for r in lignes:
        jour = date_iso(val(r, "date"))
        montant = nombre(val(r, "montant"))
        if not jour or (not montant and not val(r, "quantite")):
            ignorees += 1
            continue
        q = abs(nombre(val(r, "quantite")))
        isin = val(r, "isin").upper()
        typ = type_operation(" ".join([val(r, "type"), val(r, "libelle")]), q, montant)
        k = cle(jour, isin, q, montant)
        if k in deja:
            doublons += 1
            continue
        deja.add(k)
        frais = abs(nombre(val(r, "frais")))
        nom = val(r, "nom") or val(r, "libelle")
        ident = connus.get(isin) or ("".join(c for c in simple(nom).upper() if c.isalnum())[:8] if isin else "")
        if isin and isin not in connus:
            a_ajouter[isin] = (ident, nom)
        if q:
            prix = nombre(val(r, "prix")) or max(0.0, (abs(montant) - frais) / q)
        else:
            q, prix = 1, abs(montant)
        nouvelles.append({"Date": datetime.fromisoformat(jour).strftime("%d/%m/%Y"), "Utilisateur": params.get("prenom", ""),
                          "Enveloppe": enveloppe or "", "Type d'opération": typ, "ID actif": ident if isin else "",
                          "Quantité": round(q, 6), "Prix unitaire (ou montant)": round(prix, 4),
                          "Frais de courtage": round(frais, 2), "Devise": val(r, "devise") or "EUR",
                          "Taux de change (1 si EUR)": 1, "_cle": k})
    print(f"Relevé {Path(fichier).name} : {len(lignes)} lignes lues, colonnes reconnues : "
          f"{', '.join(f'{c} = « {entete[j]} »' for c, j in corr.items())}")
    print(f"- {len(nouvelles)} opérations nouvelles, {doublons} déjà importées, {ignorees} ignorées (sans date ni montant)")
    if any(n["Type d'opération"] == "" for n in nouvelles):
        print("- Attention : certaines opérations n'ont pas de type reconnu, à compléter avant de coller.")
    if not enveloppe:
        print("- Enveloppe non précisée (option --enveloppe PEA, CTO...) : colonne à remplir avant de coller.")
    if simulation or not nouvelles:
        print("Simulation : rien n'est écrit." if simulation else "Rien à importer.")
        return
    # Fichier .xlsx (dates et nombres typés : rien à reconvertir dans un Google Sheet en français), complété s'il existe déjà
    from openpyxl import Workbook, load_workbook
    sortie = d / f"import-{date.today().isoformat()}.xlsx"
    if sortie.exists():
        wb = load_workbook(sortie)
        ws = wb.active
    else:
        wb = Workbook()
        ws = wb.active
        ws.title = "A coller dans Transactions"
        ws.append(ENTETES_SHEET)
    for n in nouvelles:
        ligne = [n[c] for c in ENTETES_SHEET]
        ligne[0] = datetime.strptime(ligne[0], "%d/%m/%Y").date()
        ws.append(ligne)
        ws.cell(ws.max_row, 1).number_format = "DD/MM/YYYY"
    wb.save(sortie)
    faits = lire_csv(d / "imports-faits.csv") + [{"cle": n["_cle"], "date_import": date.today().isoformat(),
                                                   "fichier": Path(fichier).name} for n in nouvelles]
    ecrire_csv(d / "imports-faits.csv", ["cle", "date_import", "fichier"], faits)
    print(f"Écrit : {sortie.name} (à coller dans la feuille Transactions, à partir de la colonne A d'une ligne vide)")
    if a_ajouter:
        print("Actifs à ajouter dans la feuille Actifs (ID, nom, ISIN) :")
        for isin, (ident, nom) in a_ajouter.items():
            print(f"  {ident}  {nom}  {isin}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2 or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    env = args[args.index("--enveloppe") + 1] if "--enveloppe" in args else None
    main(args[0], args[1], env, "--simulation" in args)
