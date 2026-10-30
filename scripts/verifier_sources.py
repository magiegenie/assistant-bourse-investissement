"""Vérifie que chaque flux de donnees/sources.csv répond et contient des articles récents.

Usage : python scripts/verifier_sources.py [--jours 60]
Sortie : une ligne par source (OK, VIDE, ANCIEN ou ERREUR) et un code de retour 1 si un flux est mort.
Lancé chaque semaine par .github/workflows/veille-hebdo.yml (le réseau y est ouvert).
"""
import argparse
import sys
from datetime import date, timedelta

from collecte_hebdo import articles, lire_sources, telecharger

sys.stdout.reconfigure(encoding="utf-8")


def etat(source, limite, telecharge=telecharger):
    try:
        liste = articles(telecharge(source["url_flux"]))
    except Exception as e:
        return "ERREUR", type(e).__name__
    if not liste:
        return "VIDE", "aucun article"
    dates = [d for d, _, _ in liste if d]
    if dates and max(dates) < limite:
        return "ANCIEN", f"dernier article le {max(dates):%d/%m/%Y}"
    return "OK", f"{len(liste)} articles"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--jours", type=int, default=60)
    a = p.parse_args()
    limite = date.today() - timedelta(days=a.jours)
    morts = 0
    for s in lire_sources():
        code, detail = etat(s, limite)
        morts += code in ("ERREUR", "VIDE")
        print(f"{code:<7} {s['nom']:<45} {detail}")
    print(f"\n{morts} flux mort(s).")
    sys.exit(1 if morts else 0)


if __name__ == "__main__":
    main()
