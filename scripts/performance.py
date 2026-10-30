"""Rendement annualisé réel (XIRR) comparé aux mêmes versements placés à un taux de référence."""
import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
from datetime import date
from pathlib import Path

def xirr(flux):
    """flux : liste de (date, montant). Méthode de Newton puis bissection en secours."""
    t0 = flux[0][0]
    def vna(r):
        return sum(m / (1 + r) ** ((d - t0).days / 365) for d, m in flux)
    bas, haut = -0.99, 10.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if vna(bas) * vna(mil) <= 0:
            haut = mil
        else:
            bas = mil
    return (bas + haut) / 2

def main(dossier, taux_ref):
    d = Path(dossier)
    with open(d / "flux.csv", encoding="utf-8") as f:
        flux = [(date.fromisoformat(r["date"]), float(r["montant"])) for r in csv.DictReader(f)]
    with open(d / "positions.csv", encoding="utf-8") as f:
        valeur = sum(float(r["valeur"]) for r in csv.DictReader(f))
    flux.sort()
    aujourdhui = date.today()
    verse = -sum(m for _, m in flux)
    r = xirr(flux + [(aujourdhui, valeur)])
    ref = sum(-m * (1 + taux_ref / 100) ** ((aujourdhui - d0).days / 365) for d0, m in flux)
    print(f"Versé net : {verse:,.2f} €   Valeur : {valeur:,.2f} €   Gain : {valeur - verse:+,.2f} €")
    print(f"Rendement annualisé réel (XIRR) : {r * 100:.2f} %")
    print(f"Mêmes versements placés à {taux_ref:.1f} %/an : {ref:,.2f} €  (écart {valeur - ref:+,.2f} €)")
    if (aujourdhui - flux[0][0]).days < 365:
        print("Attention : moins d'un an d'historique, le rendement annualisé est peu significatif.")

if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 7.0)
