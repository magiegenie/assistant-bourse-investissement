"""Coût des frais dans le temps : combien un écart de frais annuels coûte sur 10, 20 et 30 ans.

Usage : python scripts/frais.py <capital> <mensuel> <rendement_brut_%> <frais_A_%> [frais_B_%] [--annees 10,20,30]
Exemple : python scripts/frais.py 5000 300 6 0.20 1.80   (ETF à 0,20 % contre fonds à 1,80 %)

Les frais sont retirés du rendement chaque mois (rendement net = brut - frais). Hypothèses, pas des prévisions :
le rendement brut n'est pas garanti, mais l'écart de frais, lui, est certain (fiche D).
"""
import sys

from projection import projeter

sys.stdout.reconfigure(encoding="utf-8")


def capital_final(capital, mensuel, brut, frais, annees):
    return projeter(capital, mensuel, brut - frais, annees)


def main(args):
    annees = [10, 20, 30]
    if "--annees" in args:
        i = args.index("--annees")
        annees = [int(x) for x in args[i + 1].split(",")]
        del args[i:i + 2]
    capital, mensuel, brut, frais_a = map(float, args[:4])
    frais_b = float(args[4]) if len(args) > 4 else None
    print(f"Capital {capital:,.0f} €, versement {mensuel:,.0f} €/mois, rendement brut supposé {brut:.1f} %/an\n")
    entete = f"{'Durée':>6}{'Versé':>12}{f'Frais {frais_a:.2f} %':>18}"
    if frais_b is not None:
        entete += f"{f'Frais {frais_b:.2f} %':>18}{'Écart':>14}"
    print(entete)
    for a in annees:
        verse = capital + mensuel * 12 * a
        va = capital_final(capital, mensuel, brut, frais_a, a)
        ligne = f"{a:>4} a{verse:>12,.0f}{va:>16,.0f} €"
        if frais_b is not None:
            vb = capital_final(capital, mensuel, brut, frais_b, a)
            ligne += f"{vb:>16,.0f} €{va - vb:>12,.0f} €"
        print(ligne)
    sans = capital_final(capital, mensuel, brut, 0, max(annees))
    avec = capital_final(capital, mensuel, brut, frais_a, max(annees))
    print(f"\nSur {max(annees)} ans, des frais de {frais_a:.2f} % coûtent {sans - avec:,.0f} € "
          f"({(sans - avec) / sans * 100:.1f} % du capital final).")
    print("Hypothèses illustratives, avant impôts. Le rendement n'est pas garanti ; l'écart de frais l'est.")


if __name__ == "__main__":
    if len(sys.argv) < 5 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    main(sys.argv[1:])
