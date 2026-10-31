"""Interroge la base historique des marchés (donnees/historique/, mise à jour par maj_historique.py).

Usage :
  python scripts/historique.py resume                          indices disponibles et couverture réelle
  python scripts/historique.py mois 2008-10                    tous les indices ce mois-là, la macro, les événements
  python scripts/historique.py periode SP500 2000-01 2012-12   rendement cumulé et annualisé (du début du 1er mois à la fin du 2e)
  python scripts/historique.py annees CAC40                    grille années x mois
  python scripts/historique.py baisses MSCI_WORLD [--seuil 20] sommet, creux, baisse, durées, retour au sommet
  python scripts/historique.py glissant SP500 [--annees 10]    pire, médian et meilleur rendement annualisé sur N ans glissants
  python scripts/historique.py evenement covid                 événements trouvés et réaction des grands indices à 1, 3 et 12 mois
  python scripts/historique.py excel                           régénère docs/Historique-marches.xlsx
  python scripts/historique.py sqlite                          reconstruit donnees/historique/marches.sqlite

Options : --eur (indices en dollars convertis en euros), --reel (après inflation : France pour l'euro, États-Unis
pour le dollar). Les noms d'indice acceptent des variantes (« s&p 500 », « cac », « world »...).
Les indices « prix » ne comptent pas les dividendes (environ 2 à 4 % par an en moins). Le passé n'annonce pas l'avenir.
"""
import csv
import sqlite3
import statistics
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
DOSSIER = RACINE / "donnees" / "historique"
EXCEL = RACINE / "docs" / "Historique-marches.xlsx"
PRINCIPAUX = ["MSCI_WORLD", "SP500", "STOXX600", "CAC40", "NIKKEI225"]
ALIAS = {"sp500": "SP500", "s&p500": "SP500", "s&p": "SP500", "world": "MSCI_WORLD", "msciworld": "MSCI_WORLD",
         "monde": "MSCI_WORLD", "acwi": "MSCI_ACWI", "emergents": "MSCI_EM", "em": "MSCI_EM", "nasdaq": "NASDAQ100",
         "dow": "DOW_JONES", "dowjones": "DOW_JONES", "cac": "CAC40", "stoxx": "STOXX600", "eurostoxx": "EUROSTOXX50",
         "ftse": "FTSE100", "nikkei": "NIKKEI225", "dax": "DAX"}


def lire(nom):
    f = DOSSIER / nom
    if not f.exists():
        return []
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


FICHES = {r["id"]: r for r in lire("indices.csv")}
NIVEAUX = {}
for _r in lire("niveaux-mensuels.csv"):
    NIVEAUX.setdefault(_r["indice"], {})[_r["mois"]] = float(_r["cloture"])
MACRO = {}
for _r in lire("macro-mensuel.csv"):
    MACRO.setdefault(_r["serie"], {})[_r["mois"]] = float(_r["valeur"])
EVENEMENTS = lire("evenements.csv")


def normaliser(t):
    return "".join(c for c in t.lower() if c.isalnum() or c == "&").replace("_", "")


def indice(nom):
    n = normaliser(nom)
    for i, f in FICHES.items():
        if n in (normaliser(i), normaliser(f["nom"])):
            return i
    if n in ALIAS:
        return ALIAS[n]
    sys.exit(f"Indice inconnu : {nom}. Disponibles : {', '.join(FICHES)}")


def decaler(m, k):
    a, mo = int(m[:4]), int(m[5:]) - 1 + k
    return f"{a + mo // 12}-{mo % 12 + 1:02d}"


def serie(ind, eur=False, reel=False):
    """{mois: niveau}, converti en euros et/ou corrigé de l'inflation si demandé (mois sans donnée retirés)."""
    s = dict(NIVEAUX[ind])
    devise = FICHES[ind]["devise"]
    if eur and devise == "USD":
        fx = MACRO.get("usd_par_eur_long", {})
        s = {m: v / fx[m] for m, v in s.items() if m in fx}
        devise = "EUR"
    elif eur and devise not in ("EUR", "USD"):
        print(f"(Conversion en euros non disponible pour {devise} : valeurs en {devise}.)")
    if reel:
        prix = MACRO.get("inflation_fr_long" if devise == "EUR" else "inflation_us_indice", {})
        s = {m: v / prix[m] for m, v in s.items() if m in prix}
    return s


def libelle(ind, eur, reel):
    f = FICHES[ind]
    dev = "EUR" if eur and f["devise"] == "USD" else f["devise"]
    return f"{f['nom']} ({f['type']}, {dev}{', après inflation' if reel else ''})"


def pct(a, b):
    return (b / a - 1) * 100


def variations(s):
    mois = sorted(s)
    return {m: pct(s[p], s[m]) for p, m in zip(mois, mois[1:]) if decaler(p, 1) == m}


def baisses(s, seuil):
    """Épisodes où l'indice a perdu au moins `seuil` % depuis son plus haut, avec le retour au sommet."""
    mois = sorted(s)
    res, sommet, m_sommet, creux, m_creux = [], s[mois[0]], mois[0], None, None
    for m in mois[1:]:
        v = s[m]
        if v >= sommet:
            if creux is not None and pct(sommet, creux) <= -seuil:
                res.append((m_sommet, m_creux, pct(sommet, creux), m))
            sommet, m_sommet, creux, m_creux = v, m, None, None
        elif creux is None or v < creux:
            creux, m_creux = v, m
    if creux is not None and pct(sommet, creux) <= -seuil:
        res.append((m_sommet, m_creux, pct(sommet, creux), None))
    return res


def ecart_mois(a, b):
    return (int(b[:4]) - int(a[:4])) * 12 + int(b[5:]) - int(a[5:])


def annualise(cumul, nb_mois):
    return ((1 + cumul / 100) ** (12 / nb_mois) - 1) * 100 if nb_mois else 0


def cmd_resume():
    print(f"{'Indice':<13}{'Nom':<45}{'Type':<32}{'Devise':<7}{'Début':<9}{'Fin':<9}")
    for i, f in FICHES.items():
        print(f"{i:<13}{f['nom'][:44]:<45}{f['type'][:31]:<32}{f['devise']:<7}{f['debut']:<9}{f['fin']:<9}")
    print(f"\nMacro : {', '.join(sorted(MACRO))}\nÉvénements : {len(EVENEMENTS)}")


def evenements_du_mois(m):
    return [e for e in EVENEMENTS if e["date_debut"][:7] <= m <= (e["date_fin"] or e["date_debut"])[:7]]


def cmd_mois(m):
    print(f"MARCHÉS EN {m}\n")
    print(f"{'Indice':<46}{'Mois':>9}{'Sur 12 mois':>13}")
    for i in FICHES:
        s = NIVEAUX[i]
        p, a = decaler(m, -1), decaler(m, -12)
        if m in s and p in s:
            sur12 = f"{pct(s[a], s[m]):+.1f} %" if a in s else ""
            print(f"{FICHES[i]['nom'][:45]:<46}{pct(s[p], s[m]):>+8.1f} %{sur12:>13}")
    lignes = []
    for cle, nom in [("taux_fed", "Taux de la Fed"), ("taux_bce_depot", "Taux de dépôt BCE"), ("taux_10ans_us", "10 ans américain"),
                     ("taux_10ans_fr", "10 ans français"), ("usd_par_eur_long", "Dollars pour 1 euro"), ("petrole_wti", "Pétrole WTI ($)")]:
        if m in MACRO.get(cle, {}):
            lignes.append(f"{nom} : {MACRO[cle][m]:.2f}")
    for cle, nom in [("inflation_us_indice", "Inflation États-Unis sur 12 mois"), ("inflation_fr_long", "Inflation France sur 12 mois")]:
        s = MACRO.get(cle, {})
        if m in s and decaler(m, -12) in s:
            lignes.append(f"{nom} : {pct(s[decaler(m, -12)], s[m]):.1f} %")
    if MACRO.get("recession_us", {}).get(m) == 1:
        lignes.append("Les États-Unis sont en récession (NBER)")
    if lignes:
        print("\nMACRO\n- " + "\n- ".join(lignes))
    ev = evenements_du_mois(m)
    if ev:
        print("\nÉVÉNEMENTS")
        for e in ev:
            print(f"- {e['date_debut']} {e['titre']} ({e['categorie']}, {e['zone']}) : {e['resume']} [source : {e['source_url']}]")
    print("\nSources : Yahoo Finance, STOXX, FRED. Indices dans leur devise, prix seul sauf mention.")


def cmd_periode(ind, debut, fin, eur, reel):
    s = serie(ind, eur, reel)
    base = decaler(debut, -1)
    if base not in s or fin not in s:
        sys.exit(f"Période hors des données : il faut la fin du mois précédant le début ({base}) et la fin de {fin}. "
                 f"Données disponibles : {min(s)} -> {max(s)}.")
    n = ecart_mois(base, fin)
    cumul = pct(s[base], s[fin])
    v = {m: x for m, x in variations(s).items() if debut <= m <= fin}
    sous = {m: x for m, x in s.items() if base <= m <= fin}
    pire = min(baisses(sous, 0.01), key=lambda b: b[2], default=None)
    print(libelle(ind, eur, reel))
    print(f"Du début de {debut} à la fin de {fin} ({n} mois) : {cumul:+.1f} % au total, soit {annualise(cumul, n):+.1f} % par an")
    print(f"Meilleur mois : {max(v, key=v.get)} ({max(v.values()):+.1f} %), pire mois : {min(v, key=v.get)} ({min(v.values()):+.1f} %)")
    print(f"Mois en hausse : {sum(1 for x in v.values() if x > 0)} sur {len(v)}")
    if pire:
        print(f"Plus forte baisse dans la période : {pire[2]:.1f} % (sommet {pire[0]}, creux {pire[1]})")


def cmd_annees(ind, eur, reel):
    s = serie(ind, eur, reel)
    v = variations(s)
    print(libelle(ind, eur, reel))
    print("Année " + "".join(f"{m:>7}" for m in ["janv", "févr", "mars", "avr", "mai", "juin", "juil", "août", "sept", "oct", "nov", "déc"]) + "   Année")
    for a in range(int(min(s)[:4]), int(max(s)[:4]) + 1):
        cases = "".join(f"{v[f'{a}-{k:02d}']:>+7.1f}" if f"{a}-{k:02d}" in v else " " * 7 for k in range(1, 13))
        dec, prec = f"{a}-12", f"{a - 1}-12"
        an = f"{pct(s[prec], s[dec]):>+8.1f}" if dec in s and prec in s else "        "
        print(f"{a} {cases}{an}")


def cmd_baisses(ind, seuil, eur, reel):
    s = serie(ind, eur, reel)
    print(f"{libelle(ind, eur, reel)} : baisses d'au moins {seuil:g} %\n")
    print(f"{'Sommet':<9}{'Creux':<9}{'Baisse':>8}{'Durée':>8}  {'Retour au sommet':<17}{'Récupération':>13}")
    for som, cre, b, ret in baisses(s, seuil):
        r = f"{ret:<17}{ecart_mois(cre, ret):>9} mois" if ret else f"{'pas encore':<17}{'':>13}"
        print(f"{som:<9}{cre:<9}{b:>7.1f}%{ecart_mois(som, cre):>5} mois  {r}")
    print("\nDurée : du sommet au creux. Récupération : du creux au retour au sommet précédent. Calcul sur les fins de mois :"
          "\nau jour le jour, les baisses sont plus fortes (Covid, S&P 500 : environ -34 % en séance, -20 % en fin de mois).")


def cmd_glissant(ind, annees, eur, reel):
    s = serie(ind, eur, reel)
    n = annees * 12
    res = [(annualise(pct(s[m], s[decaler(m, n)]), n), m) for m in sorted(s) if decaler(m, n) in s]
    if not res:
        sys.exit("Historique trop court pour cette durée.")
    valeurs = sorted(r[0] for r in res)
    pire, meilleur = min(res), max(res)
    print(f"{libelle(ind, eur, reel)} : rendement annualisé sur {annees} ans glissants ({len(res)} périodes)")
    print(f"Pire : {pire[0]:+.1f} %/an (de {pire[1]} à {decaler(pire[1], n)})")
    print(f"Médian : {statistics.median(valeurs):+.1f} %/an")
    print(f"Meilleur : {meilleur[0]:+.1f} %/an (de {meilleur[1]} à {decaler(meilleur[1], n)})")
    print(f"Périodes positives : {sum(1 for x in valeurs if x > 0) / len(valeurs) * 100:.0f} %")


def reactions(m):
    """Variation des grands indices depuis la fin du mois précédant l'événement, à 1, 3 et 12 mois."""
    out = []
    for i in PRINCIPAUX:
        s = NIVEAUX[i]
        base = decaler(m, -1)
        if base in s:
            out.append((i, [pct(s[base], s[decaler(m, k - 1)]) if decaler(m, k - 1) in s else None for k in (1, 3, 12)]))
    return out


def cmd_evenement(mot):
    if not EVENEMENTS:
        sys.exit("La frise d'événements (evenements.csv) est vide.")
    t = mot.lower()
    trouves = [e for e in EVENEMENTS if t in (e["titre"] + " " + e["resume"] + " " + e["categorie"]).lower()]
    if not trouves:
        sys.exit(f"Aucun événement pour « {mot} ».")
    for e in trouves:
        print(f"\n{e['date_debut']} : {e['titre']} ({e['categorie']}, {e['zone']})\n{e['resume']}\nSource : {e['source_url']}")
        for i, r in reactions(e["date_debut"][:7]):
            print(f"  {FICHES[i]['nom'][:30]:<31}" + "".join(f"{lab} {x:+6.1f} %   " if x is not None else f"{lab}    n.d.   "
                                                          for lab, x in zip(("1 mois", "3 mois", "12 mois"), r)))
    print("\nRéaction mesurée depuis la fin du mois précédant l'événement. Ce n'est pas une preuve de cause à effet.")


def annuels(s):
    return {int(m[:4]): pct(s[f"{int(m[:4]) - 1}-12"], s[m]) for m in s if m.endswith("-12") and f"{int(m[:4]) - 1}-12" in s}


def cmd_sqlite():
    f = DOSSIER / "marches.sqlite"
    f.unlink(missing_ok=True)
    con = sqlite3.connect(f)
    for nom, table in [("indices.csv", "indices"), ("niveaux-mensuels.csv", "niveaux"), ("macro-mensuel.csv", "macro"),
                       ("macro-series.csv", "macro_series"), ("evenements.csv", "evenements")]:
        lignes = lire(nom)
        if not lignes:
            continue
        cols = list(lignes[0])
        con.execute(f"CREATE TABLE {table} ({', '.join(cols)})")
        con.executemany(f"INSERT INTO {table} VALUES ({', '.join('?' * len(cols))})", [list(r.values()) for r in lignes])
    con.execute("""CREATE VIEW rendements_annuels AS
        SELECT substr(a.mois, 1, 4) AS annee, a.indice, ROUND((CAST(a.cloture AS REAL) / CAST(b.cloture AS REAL) - 1) * 100, 2) AS rendement_pct
        FROM niveaux a JOIN niveaux b ON b.indice = a.indice
        AND b.mois = (CAST(substr(a.mois, 1, 4) AS INTEGER) - 1) || '-12' WHERE a.mois LIKE '%-12'""")
    con.commit()
    con.close()
    print(f"Base reconstruite : {f.relative_to(RACINE)} (tables indices, niveaux, macro, macro_series, evenements ; vue rendements_annuels)")


def cmd_excel():
    from openpyxl import Workbook
    from openpyxl.formatting.rule import ColorScaleRule
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    bleu, blanc = PatternFill("solid", fgColor="1F3A5F"), Font(color="FFFFFF", bold=True)
    echelle = ColorScaleRule(start_type="num", start_value=-10, start_color="E06666", mid_type="num", mid_value=0,
                             mid_color="FFFFFF", end_type="num", end_value=10, end_color="6AA84F")
    echelle_an = ColorScaleRule(start_type="num", start_value=-30, start_color="E06666", mid_type="num", mid_value=0,
                                mid_color="FFFFFF", end_type="num", end_value=30, end_color="6AA84F")

    def entete(ws, valeurs, ligne=1):
        for j, v in enumerate(valeurs, 1):
            c = ws.cell(ligne, j, v)
            c.fill, c.font, c.alignment = bleu, blanc, Alignment(horizontal="center", wrap_text=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Lisez-moi"
    texte = ["HISTORIQUE DES MARCHÉS : mode d'emploi",
             "Un onglet par indice : chaque ligne est une année, chaque case la variation du mois en %, la dernière colonne l'année entière.",
             "Vert = hausse, rouge = baisse, plus la couleur est forte plus le mouvement est grand.",
             "Synthèse annuelle : tous les indices côte à côte, année par année. Grandes baisses : chaque baisse d'au moins 20 % et son temps de récupération.",
             "Événements : la frise datée et sourcée, avec la variation des grands indices 1, 3 et 12 mois après. Macro : inflation, taux, change, pétrole par année.",
             "Sources : Yahoo Finance, STOXX, FRED. Détail, couverture et limites : donnees/historique/SOURCES.md.",
             "Attention : la plupart des indices sont en prix seul (sans dividendes) et dans leur devise d'origine. Le passé n'annonce pas l'avenir.",
             "Fichier régénéré par : python scripts/historique.py excel. Usage personnel, ne pas publier.", ""]
    for i, t in enumerate(texte, 1):
        ws.cell(i, 1, t).font = Font(bold=(i == 1), size=13 if i == 1 else 11)
    entete(ws, ["Indice", "Nom", "Type", "Devise", "Début", "Fin", "Remarques"], len(texte) + 1)
    for k, f in enumerate(FICHES.values(), len(texte) + 2):
        for j, cle in enumerate(["id", "nom", "type", "devise", "debut", "fin", "remarques"], 1):
            ws.cell(k, j, f[cle])
    for col, w in zip("ABCDEFG", [14, 40, 28, 8, 9, 9, 90]):
        ws.column_dimensions[col].width = w

    mois_noms = ["Janv", "Févr", "Mars", "Avr", "Mai", "Juin", "Juil", "Août", "Sept", "Oct", "Nov", "Déc"]
    for i, f in FICHES.items():
        s = NIVEAUX[i]
        v = variations(s)
        an = annuels(s)
        ws = wb.create_sheet(i[:31])
        ws.cell(1, 1, f"{f['nom']} : variation mensuelle en % ({f['type']}, {f['devise']})").font = Font(bold=True, size=12)
        entete(ws, ["Année"] + mois_noms + ["Année %"], 2)
        a0, a1 = int(min(s)[:4]), int(max(s)[:4])
        for k, a in enumerate(range(a1, a0 - 1, -1), 3):
            ws.cell(k, 1, a).font = Font(bold=True)
            for mo in range(1, 13):
                x = v.get(f"{a}-{mo:02d}")
                if x is not None:
                    ws.cell(k, mo + 1, round(x, 2)).number_format = "+0.0;-0.0;0.0"
            if a in an:
                c = ws.cell(k, 14, round(an[a], 2))
                c.number_format, c.font = "+0.0;-0.0;0.0", Font(bold=True)
        fin = 2 + a1 - a0 + 1
        ws.conditional_formatting.add(f"B3:M{fin}", echelle)
        ws.conditional_formatting.add(f"N3:N{fin}", echelle_an)
        ws.freeze_panes = "B3"
        ws.column_dimensions["A"].width = 8
        for j in range(2, 15):
            ws.column_dimensions[get_column_letter(j)].width = 7.5

    ws = wb.create_sheet("Synthèse annuelle")
    ids = list(FICHES)
    entete(ws, ["Année"] + [FICHES[i]["nom"] for i in ids])
    ans = {i: annuels(NIVEAUX[i]) for i in ids}
    toutes = sorted({a for d in ans.values() for a in d}, reverse=True)
    for k, a in enumerate(toutes, 2):
        ws.cell(k, 1, a).font = Font(bold=True)
        for j, i in enumerate(ids, 2):
            if a in ans[i]:
                ws.cell(k, j, round(ans[i][a], 2)).number_format = "+0.0;-0.0;0.0"
    ws.conditional_formatting.add(f"B2:{get_column_letter(len(ids) + 1)}{len(toutes) + 1}", echelle_an)
    ws.freeze_panes = "B2"
    ws.row_dimensions[1].height = 45
    for j in range(2, len(ids) + 2):
        ws.column_dimensions[get_column_letter(j)].width = 12

    ws = wb.create_sheet("Grandes baisses")
    entete(ws, ["Indice", "Sommet", "Creux", "Baisse %", "Durée (mois)", "Retour au sommet", "Récupération (mois)", "Événements autour du creux"])
    k = 2
    for i in ids:
        for som, cre, b, ret in baisses(NIVEAUX[i], 20):
            ev = "; ".join(e["titre"] for e in EVENEMENTS if som <= e["date_debut"][:7] <= cre)
            for j, val in enumerate([FICHES[i]["nom"], som, cre, round(b, 1), ecart_mois(som, cre), ret or "pas encore",
                                     ecart_mois(cre, ret) if ret else "", ev], 1):
                ws.cell(k, j, val)
            k += 1
    for col, w in zip("ABCDEFGH", [30, 10, 10, 10, 12, 16, 18, 90]):
        ws.column_dimensions[col].width = w

    ws = wb.create_sheet("Événements")
    entete(ws, ["Date", "Fin", "Titre", "Catégorie", "Zone", "Résumé", "Source"] +
           [f"{FICHES[i]['nom'][:18]} {h}" for i in PRINCIPAUX for h in ("1 m", "3 m", "12 m")])
    for k, e in enumerate(sorted(EVENEMENTS, key=lambda e: e["date_debut"]), 2):
        for j, cle in enumerate(["date_debut", "date_fin", "titre", "categorie", "zone", "resume", "source_url"], 1):
            ws.cell(k, j, e[cle])
        j = 8
        r = dict(reactions(e["date_debut"][:7]))
        for i in PRINCIPAUX:
            for x in r.get(i, [None, None, None]):
                if x is not None:
                    ws.cell(k, j, round(x, 1)).number_format = "+0.0;-0.0;0.0"
                j += 1
    if EVENEMENTS:
        ws.conditional_formatting.add(f"H2:{get_column_letter(7 + 3 * len(PRINCIPAUX))}{len(EVENEMENTS) + 1}", echelle_an)
    for col, w in zip("ABCDEFG", [11, 11, 40, 16, 14, 70, 40]):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "D2"

    ws = wb.create_sheet("Macro par année")
    entete(ws, ["Année", "Inflation États-Unis %", "Inflation France %", "Taux Fed fin d'année %", "Taux dépôt BCE fin d'année %",
                "10 ans US fin d'année %", "10 ans France fin d'année %", "Dollars pour 1 euro fin d'année", "Pétrole WTI déc. ($)", "Récession US (mois)"])
    a_max = max(int(m[:4]) for m in MACRO["taux_fed"])
    for k, a in enumerate(range(a_max, 1955, -1), 2):
        dec, prec = f"{a}-12", f"{a - 1}-12"
        vals = [a]
        for cle in ("inflation_us_indice", "inflation_fr_long"):
            s = MACRO.get(cle, {})
            vals.append(round(pct(s[prec], s[dec]), 1) if dec in s and prec in s else None)
        for cle in ("taux_fed", "taux_bce_depot", "taux_10ans_us", "taux_10ans_fr", "usd_par_eur_long", "petrole_wti"):
            x = MACRO.get(cle, {}).get(dec)
            vals.append(round(x, 2) if x is not None else None)
        vals.append(sum(1 for mo in range(1, 13) if MACRO.get("recession_us", {}).get(f"{a}-{mo:02d}") == 1))
        for j, x in enumerate(vals, 1):
            ws.cell(k, j, x)
    ws.row_dimensions[1].height = 45
    for j in range(1, 11):
        ws.column_dimensions[get_column_letter(j)].width = 14
    ws.freeze_panes = "B2"

    wb.save(EXCEL)
    print(f"Classeur créé : {EXCEL.relative_to(RACINE)} ({len(wb.sheetnames)} onglets)")


def main():
    args = [a for a in sys.argv[1:]]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return
    eur, reel = "--eur" in args, "--reel" in args
    args = [a for a in args if a not in ("--eur", "--reel")]
    opt = lambda nom, defaut: float(args[args.index(nom) + 1]) if nom in args else defaut
    c = args[0]
    if c == "resume":
        cmd_resume()
    elif c == "mois":
        cmd_mois(args[1])
    elif c == "periode":
        cmd_periode(indice(args[1]), args[2], args[3], eur, reel)
    elif c == "annees":
        cmd_annees(indice(args[1]), eur, reel)
    elif c == "baisses":
        cmd_baisses(indice(args[1]), opt("--seuil", 20), eur, reel)
    elif c == "glissant":
        cmd_glissant(indice(args[1]), int(opt("--annees", 10)), eur, reel)
    elif c == "evenement":
        cmd_evenement(" ".join(args[1:]))
    elif c == "excel":
        cmd_excel()
    elif c == "sqlite":
        cmd_sqlite()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
