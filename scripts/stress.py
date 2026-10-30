"""Tests de résistance : impact en euros de scénarios de crise sur le portefeuille.

Usage : python scripts/stress.py prive/<prenom>

Les chocs sont des HYPOTHÈSES illustratives, inspirées des grandes baisses passées (fiche D, recherche 03),
pas des prévisions. Idée reprise du skill « portfolio-cio » (stress tests par position), recodée et
limitée à un portefeuille d'ETF de particulier.

Chaque poche est classée d'après son nom : obligations, or, crypto, liquidités, sinon actions.
Part en dollars estimée : 100 % pour USA / S&P / Nasdaq, 70 % pour Monde / World / ACWI, 0 % sinon.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from allocation import lire

# Scénario : (description, choc actions, choc obligations, choc or, choc crypto, choc du dollar contre l'euro)
SCENARIOS = [
    ("Correction des actions (-20 %)", -20, 0, 0, -30, 0),
    ("Krach type 2008 (-50 % actions)", -50, 5, 5, -60, 10),
    ("Krach type Covid 2020 (-34 % en un mois)", -34, 0, 0, -40, 3),
    ("Hausse des taux type 2022", -18, -15, 0, -60, 10),
    ("Effondrement des crypto-actifs (-80 %)", 0, 0, 0, -80, 0),
    ("Baisse du dollar de 15 %", 0, 0, 0, 0, -15),
]


def classe(poche):
    p = poche.lower()
    if "oblig" in p or "bond" in p:
        return "oblig"
    if p in ("or", "gold") or p.startswith("or "):
        return "or"
    if "crypto" in p or "bitcoin" in p:
        return "crypto"
    if "liquid" in p or "monétaire" in p or "fonds euro" in p or "livret" in p:
        return "cash"
    return "actions"


def part_dollar(poche):
    p = poche.lower()
    if any(k in p for k in ("usa", "us ", "s&p", "nasdaq", "amérique")) or p == "us":
        return 1.0
    if any(k in p for k in ("monde", "world", "acwi")):
        return 0.7
    return 0.0


def main(dossier):
    positions = lire(Path(dossier) / "positions.csv")
    # Un fonds euro a un capital garanti : on le traite comme des liquidités, même s'il est rangé
    # dans une poche « Obligations ». On classe donc chaque ligne d'après son nom ET sa poche.
    poches = {}
    for r in positions:
        cle = r["poche"]
        if "fonds euro" in r["nom"].lower() or "fonds en euro" in r["nom"].lower():
            cle = "Fonds euro (capital garanti)"
        poches[cle] = poches.get(cle, 0) + float(r["valeur"])
    total = sum(poches.values())
    print(f"Portefeuille : {total:,.0f} €\n")
    for nom, act, obl, gold, cry, usd in SCENARIOS:
        impact = 0.0
        for p, v in poches.items():
            c = classe(p)
            choc = {"actions": act, "oblig": obl, "or": gold, "crypto": cry, "cash": 0}[c]
            if c == "actions":
                choc += usd * part_dollar(p)
            impact += v * choc / 100
        print(f"{nom:<44}{impact:>+12,.0f} €  ({impact / total * 100:+.1f} %)")
    print("Une seule action en direct : compter -50 % sur la ligne (cela arrive), soit la valeur de la ligne divisée par deux.")
    print("\nHypothèses illustratives, pas des prévisions. Le dollar qui monte amortit souvent les krachs pour un "
          "investisseur en euros. La question utile : « si ça arrivait le mois prochain, changerais-tu quelque chose ? »")


if __name__ == "__main__":
    main(sys.argv[1])
