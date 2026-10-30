"""Exposition réelle du portefeuille par pays, par devise et par grande entreprise (transparisation des ETF).

Usage : python scripts/exposition.py prive/<prenom>

Données : donnees/indices-pays.csv et donnees/indices-entreprises.csv (fiches officielles MSCI, Nasdaq,
positions de l'ETF SPY de State Street ; date et source sur chaque ligne). À mettre à jour chaque trimestre.
Chaque ligne de positions.csv est rattachée à un indice par la colonne facultative `indice`, sinon d'après
son nom et sa poche (Monde/World, ACWI/All-World, S&P/500, Nasdaq, Émergents/EM, Europe/Stoxx).
Seules les 10 premières entreprises de chaque indice sont connues : l'exposition par entreprise est donc
un minimum (une entreprise hors top 10 n'apparaît pas).
"""
import csv
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from allocation import lire

RACINE = Path(__file__).resolve().parent.parent / "donnees"

REGLES = [  # (mots-clés, indice) ; l'ordre compte : le plus précis d'abord
    (("acwi", "all-world", "all world", "tous pays"), "MSCI ACWI"),
    (("nasdaq",), "Nasdaq-100"),
    (("s&p", "sp500", "sp 500", " 500"), "S&P 500"),
    (("émergent", "emergent", "emerging", " em "), "MSCI Emerging Markets"),
    (("europe", "stoxx"), "MSCI Europe"),
    (("monde", "world"), "MSCI World"),
]
HORS_ACTIONS = ("oblig", "bond", "fonds euro", "monétaire", "liquid", "crypto", "bitcoin", "or ", "gold")


def charger(nom):
    with open(RACINE / nom, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def indice_de(ligne):
    if ligne.get("indice"):
        return ligne["indice"].strip()
    texte = f" {ligne['nom']} {ligne['poche']} ".lower()
    if any(k in texte for k in HORS_ACTIONS):
        return None
    for cles, indice in REGLES:
        if any(k in texte for k in cles):
            return indice
    return "?"


def main(dossier):
    positions = lire(Path(dossier) / "positions.csv")
    pays_idx, ent_idx, dates = {}, {}, {}
    for r in charger("indices-pays.csv"):
        pays_idx.setdefault(r["indice"], []).append((r["pays"], float(r["poids_pct"])))
        dates[r["indice"]] = r["date"]
    for r in charger("indices-entreprises.csv"):
        ent_idx.setdefault(r["indice"], []).append((r["entreprise"], float(r["poids_pct"])))
    connues = {e.lower() for lst in ent_idx.values() for e, _ in lst}

    total = sum(float(r["valeur"]) for r in positions)
    pays, entreprises, hors, inconnus, directes = {}, {}, 0.0, [], []
    for r in positions:
        v = float(r["valeur"])
        nom = r["nom"].strip()
        if nom.lower() in connues:  # action détenue en direct
            entreprises[nom] = entreprises.get(nom, 0) + v
            directes.append(nom)
            continue
        idx = indice_de(r)
        if idx is None:
            hors += v
            continue
        if idx not in pays_idx:
            inconnus.append(nom)
            continue
        for p, w in pays_idx[idx]:
            pays[p] = pays.get(p, 0) + v * w / 100
        for e, w in ent_idx.get(idx, []):
            entreprises[e] = entreprises.get(e, 0) + v * w / 100

    print(f"Portefeuille : {total:,.0f} €   (hors actions : {hors:,.0f} €, soit {hors / total * 100:.1f} %)\n")
    print("Exposition par pays (part du portefeuille total) :")
    for p, v in sorted(pays.items(), key=lambda x: -x[1]):
        print(f"  {p:<28}{v:>11,.0f} €{v / total * 100:>7.1f} %")
    usd = pays.get("États-Unis", 0)
    print(f"\nPart en dollars, approchée par la part des États-Unis : {usd / total * 100:.0f} % du portefeuille.")
    print("\nPlus grosses entreprises, à travers tous les ETF (minimum, top 10 des indices seulement) :")
    for e, v in sorted(entreprises.items(), key=lambda x: -x[1])[:12]:
        alerte = "  <- plus de 5 % du portefeuille via les ETF : à savoir avant d'acheter cette action en direct" if v / total * 100 > 5 else ""
        print(f"  {e:<28}{v:>11,.0f} €{v / total * 100:>7.2f} %{alerte}")
    if directes:
        print("\nDéjà détenu dans les ETF en plus de la ligne en direct : " + ", ".join(sorted(set(directes))))
    if inconnus:
        print("\nLignes non rattachées à un indice (ajouter une colonne `indice` dans positions.csv) : " + ", ".join(inconnus))
    print("\nDonnées des indices au : " + ", ".join(f"{i} {d}" for i, d in sorted(dates.items())))
    print("Sources : fiches officielles MSCI et Nasdaq, positions de l'ETF SPY (donnees/indices-*.csv). Ordres de grandeur : "
          "un ETF suit son indice à quelques écarts près.")


if __name__ == "__main__":
    main(sys.argv[1])
