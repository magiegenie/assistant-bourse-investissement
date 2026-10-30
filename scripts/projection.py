"""Projection du capital avec versements mensuels, délai pour atteindre un objectif et versement nécessaire.

Usage : python scripts/projection.py <capital> <mensuel> <taux_nominal_%> <années> [objectif] [--inflation 2]
Montants nominaux (euros courants), avant frais et impôts. Avec --inflation, affiche aussi l'équivalent en euros d'aujourd'hui.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

def projeter(capital, mensuel, taux, annees):
    r = (1 + taux / 100) ** (1 / 12) - 1
    for _ in range(int(annees * 12)):
        capital = capital * (1 + r) + mensuel
    return capital

def versement_requis(capital, taux, annees, objectif):
    """Versement mensuel constant qui atteint l'objectif en `annees` (recherche par dichotomie)."""
    bas, haut = 0.0, max(objectif, 1.0)
    if projeter(capital, 0, taux, annees) >= objectif:
        return 0.0
    for _ in range(100):
        m = (bas + haut) / 2
        bas, haut = (m, haut) if projeter(capital, m, taux, annees) < objectif else (bas, m)
    return haut

def main(capital, mensuel, taux, annees, objectif=None, inflation=None):
    for a in sorted({5, 10, 15, 20, 30, int(annees)}):
        v = projeter(capital, mensuel, taux, a)
        reel = f"  soit {v / (1 + inflation / 100) ** a:,.0f} € d'aujourd'hui" if inflation is not None else ""
        print(f"Dans {a:>2} ans : {v:>14,.0f} €  (versé {capital + mensuel * 12 * a:,.0f} €){reel}")
    if objectif:
        mois, c, r = 0, capital, (1 + taux / 100) ** (1 / 12) - 1
        while c < objectif and mois < 1200:
            c = c * (1 + r) + mensuel; mois += 1
        print(f"\nObjectif {objectif:,.0f} € atteint en {mois // 12} ans et {mois % 12} mois" if mois < 1200 else "\nObjectif non atteint en 100 ans")
        print(f"Versement mensuel nécessaire pour l'atteindre en {annees:g} ans : {versement_requis(capital, taux, annees, objectif):,.0f} €")
    print(f"Hypothèse : {taux:.1f} %/an nominal, avant frais et impôts, rendement non garanti.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    inflation = None
    if "--inflation" in args:
        i = args.index("--inflation"); inflation = float(args[i + 1]); del args[i:i + 2]
    main(*[float(x) for x in args], inflation=inflation)
