"""Relit le Google Sheet (exporté en .xlsx) d'une personne et met à jour ses fichiers : python scripts/synchro_sheet.py prive/<prenom> <fichier.xlsx>

L'assistant obtient le fichier avec le connecteur Google Drive (download_file_content, export
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet), ou la personne l'exporte elle-même.
Tout est recalculé à partir des transactions brutes (les valeurs en cache ne servent qu'au prix).
Prix d'une ligne, dans l'ordre : « Prix saisi à la main », prix GOOGLEFINANCE en cache, cours Yahoo Finance (ticker Yahoo).

Écrit : transactions.csv, positions.csv, flux.csv, budget.csv, objectifs.csv.
Ne remplace pas cibles.csv ni parametres.csv : signale les écarts (option --cibles-du-sheet pour reprendre les cibles du Sheet),
et complète seulement les paramètres vides.
"""
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from openpyxl import load_workbook

sys.stdout.reconfigure(encoding="utf-8")
from fichiers_profil import CSV, ecrire_csv, ecrire_parametres, lire_csv, lire_parametres, nombre

ACHATS = ("Achat", "Reprise")


def jour(v):
    if isinstance(v, datetime):
        return v.date().isoformat()
    if isinstance(v, date):
        return v.isoformat()
    t = str(v or "").strip()
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m/%Y"):
        try:
            return datetime.strptime(t, fmt).date().isoformat()
        except ValueError:
            pass
    return ""


def lignes(ws, colonnes):
    """Lignes non vides d'une feuille, en dictionnaires {nom de colonne: valeur} (lettres -> noms)."""
    out = []
    for r in range(2, ws.max_row + 1):
        d = {nom: ws[f"{col}{r}"].value for col, nom in colonnes.items()}
        cle = next(iter(colonnes.values()))
        if d[cle] not in (None, ""):
            out.append(d)
    return out


def prix_yahoo(ticker):
    try:
        from maj_historique import yahoo
        mois = yahoo(ticker, "close")[0]
        dernier = max(mois)
        return mois[dernier][1], mois[dernier][0]
    except Exception as e:
        print(f"  prix Yahoo indisponible pour {ticker} : {e}")
        return None, None


def main(dossier, fichier, cibles_du_sheet=False):
    d = Path(dossier)
    wb = load_workbook(fichier, data_only=True)
    actifs = {a["id"]: a for a in lignes(wb["Actifs"], {
        "A": "id", "B": "nom", "C": "isin", "D": "ticker_google", "E": "type", "F": "poche", "J": "enveloppe",
        "K": "ter", "N": "prix_cache", "O": "date_prix", "P": "ticker_yahoo", "Q": "prix_main"})}
    ops = lignes(wb["Transactions"], {
        "A": "date", "B": "utilisateur", "C": "enveloppe", "D": "type", "E": "id_actif", "F": "quantite", "G": "prix",
        "H": "frais", "I": "devise", "J": "taux_change", "L": "prevu", "M": "source", "N": "note"})
    alertes = []

    # transactions.csv : copie fidèle, montant en euros recalculé
    trans = []
    for o in sorted(ops, key=lambda o: jour(o["date"])):
        q, p, fx = nombre(o["quantite"]), nombre(o["prix"]), nombre(o["taux_change"], 1) or 1
        frais = nombre(o["frais"])
        montant = q * p * fx + (frais if o["type"] in ACHATS else -frais if o["type"] == "Vente" else 0)
        a = actifs.get(o["id_actif"] or "", {})
        if o["id_actif"] and not a:
            alertes.append(f"Transaction du {jour(o['date'])} : actif « {o['id_actif']} » absent de la feuille Actifs.")
        trans.append({"date": jour(o["date"]), "enveloppe": o["enveloppe"] or a.get("enveloppe", ""), "type": o["type"],
                      "id_actif": o["id_actif"] or "", "nom": a.get("nom", ""), "isin": a.get("isin", "") or "",
                      "quantite": q, "prix": p, "frais": frais, "devise": o["devise"] or "EUR", "taux_change": fx,
                      "montant_eur": round(montant, 2), "prevu": o["prevu"] or "", "source": o["source"] or "",
                      "note": o["note"] or ""})
    ecrire_csv(d / "transactions.csv", CSV["transactions.csv"], trans)

    # positions.csv : quantité, coût moyen pondéré (frais inclus), valeur au dernier prix
    qte, cout = defaultdict(float), defaultdict(float)
    for t in trans:
        i = t["id_actif"]
        if t["type"] in ACHATS:
            qte[i] += t["quantite"]
            cout[i] += t["montant_eur"]
        elif t["type"] == "Vente" and qte[i] > 0:
            part = min(1, t["quantite"] / qte[i])
            cout[i] -= cout[i] * part
            qte[i] -= t["quantite"]
    positions = []
    for i, q in qte.items():
        if q <= 1e-9 or i not in actifs:
            continue
        a = actifs[i]
        prix, date_prix = None, ""
        if a["prix_main"] not in (None, ""):
            prix, date_prix = nombre(a["prix_main"]), jour(a["date_prix"])
        elif isinstance(a["prix_cache"], (int, float)):
            prix, date_prix = float(a["prix_cache"]), date.today().isoformat()
        elif a["ticker_yahoo"]:
            prix, date_prix = prix_yahoo(a["ticker_yahoo"])
        if prix is None:
            alertes.append(f"{a['nom']} : aucun prix (ni saisi, ni GOOGLEFINANCE, ni ticker Yahoo). Valeur = prix de revient.")
            prix, date_prix = cout[i] / q, ""
        positions.append({"nom": a["nom"], "poche": a["poche"] or "Autre", "enveloppe": a["enveloppe"] or "",
                          "investi": round(cout[i], 2), "valeur": round(q * prix, 2),
                          "frais_annuels_pct": nombre(a["ter"]), "date_valeur": date_prix or date.today().isoformat(),
                          "quantite": round(q, 6), "isin": a["isin"] or "", "ticker_yahoo": a["ticker_yahoo"] or ""})
    ecrire_csv(d / "positions.csv", CSV["positions.csv"], positions)

    # flux.csv : versements et retraits ; à défaut, achats et ventes (versements négatifs, retraits positifs)
    versements = [t for t in trans if t["type"] in ("Versement", "Retrait")]
    if versements:
        flux = [{"date": t["date"], "montant": round(-t["montant_eur"] if t["type"] == "Versement" else t["montant_eur"], 2)}
                for t in versements]
    else:
        flux = [{"date": t["date"], "montant": round(-t["montant_eur"] if t["type"] in ACHATS else t["montant_eur"], 2)}
                for t in trans if t["type"] in ACHATS + ("Vente",)]
        if flux:
            alertes.append("Aucun « Versement » saisi : la performance est calculée avec les achats et ventes comme apports.")
    ecrire_csv(d / "flux.csv", CSV["flux.csv"], flux)

    # budget.csv et objectifs.csv
    budget = [{"mois": jour(b["mois"])[:7], "revenu_net": b["revenu"], "besoins": b["besoins"], "envies": b["envies"],
               "epargne_investissement": b["epargne"], "abonnements": b["abos"] or "", "note": b["note"] or ""}
              for b in lignes(wb["Budget"], {"A": "mois", "C": "revenu", "D": "besoins", "E": "envies", "F": "epargne",
                                             "H": "abos", "J": "note"})]
    ecrire_csv(d / "budget.csv", CSV["budget.csv"], budget)
    anciens = {o["nom"]: o for o in lire_csv(d / "objectifs.csv")}
    objectifs = [{"nom": o["nom"], "montant": o["montant"], "date_debut": jour(o["debut"]), "date_cible": jour(o["cible"]),
                  "montant_actuel": o["actuel"] or "", "poche": anciens.get(o["nom"], {}).get("poche", ""),
                  "priorite": anciens.get(o["nom"], {}).get("priorite", "")}
                 for o in lignes(wb["Objectifs"], {"A": "nom", "B": "montant", "C": "debut", "D": "cible", "E": "actuel"})]
    ecrire_csv(d / "objectifs.csv", CSV["objectifs.csv"], objectifs)

    # cibles : comparaison, pas d'écrasement par défaut
    ws = wb["Cibles"]
    poches_pa = [wb["Paramètres"][f"N{r}"].value for r in range(2, 12)]
    cibles_sheet = {p: round(nombre(ws[f"B{2 + i}"].value) * 100, 2) for i, p in enumerate(poches_pa)
                    if p and ws[f"B{2 + i}"].value not in (None, "")}
    cibles_ass = {c["poche"]: nombre(c["cible_pct"]) for c in lire_csv(d / "cibles.csv")}
    if not cibles_ass or cibles_du_sheet:
        ecrire_csv(d / "cibles.csv", CSV["cibles.csv"], [{"poche": p, "cible_pct": v} for p, v in cibles_sheet.items()])
    elif cibles_sheet and cibles_sheet != cibles_ass:
        alertes.append(f"Cibles différentes entre le Sheet {cibles_sheet} et cibles.csv {cibles_ass} : à trancher "
                       "(la charte fait foi ; --cibles-du-sheet pour reprendre celles du Sheet).")

    # paramètres : on complète seulement les champs vides
    p = lire_parametres(d)
    pa = wb["Paramètres"]
    valeurs = {"versement_mensuel": pa["C2"].value, "jour_versement": pa["D2"].value, "date_ouverture_pea": jour(pa["E2"].value),
               "indice_reference": pa["F2"].value, "plafond_crypto_pct": pa["G2"].value, "plafond_ligne_pct": pa["H2"].value,
               "courtier_principal": pa["I2"].value}
    for cle, v in valeurs.items():
        if v not in (None, "") and not p.get(cle):
            p[cle] = v
        elif v not in (None, "") and str(p.get(cle)) != str(v) and cle in ("versement_mensuel", "jour_versement"):
            alertes.append(f"Paramètre « {cle} » : {p.get(cle)} dans parametres.csv, {v} dans le Sheet.")
    ecrire_parametres(d, p)

    total = sum(x["valeur"] for x in positions)
    print(f"Synchronisation de {d.name} depuis {Path(fichier).name}")
    total_fr = f"{total:,.2f}".replace(",", " ").replace(".", ",")
    print(f"- {len(trans)} transactions ; {len(positions)} lignes détenues ; valeur totale {total_fr} €")
    print(f"- {len(flux)} flux, {len(budget)} mois de budget, {len(objectifs)} objectifs")
    print("Alertes :" if alertes else "Aucune alerte.")
    for a in alertes:
        print(f"- {a}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2 or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    main(args[0], args[1], "--cibles-du-sheet" in args)
