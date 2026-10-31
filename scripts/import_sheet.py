"""Reconstruit positions.csv, flux.csv et cibles.csv depuis le classeur (Google Sheets téléchargé en .xlsx, ou Excel).

Usage : python scripts/import_sheet.py <classeur.xlsx> <Prénom dans le classeur> prive/<prenom>
Google Sheets : Fichier, Télécharger, Microsoft Excel (.xlsx). Les valeurs calculées du classeur sont lues
telles quelles (onglets Positions, Actifs, Transactions et Cibles). Les anciens fichiers sont gardés en .bak.
Ainsi le classeur reste la seule saisie : l'assistant se met à jour depuis lui.
"""
import sys
from datetime import date, datetime
from pathlib import Path

from openpyxl import load_workbook

from saisie import ecrire, fmt

sys.stdout.reconfigure(encoding="utf-8")


def en_date(v):
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    try:
        return datetime.strptime(str(v), "%d/%m/%Y").date()
    except ValueError:
        return date.fromisoformat(str(v)[:10])


def nombre(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def lire_classeur(chemin, personne):
    wb = load_workbook(chemin, data_only=True, read_only=True)
    frais = {r[0]: nombre(r[10]) for r in wb["Actifs"].iter_rows(min_row=2, values_only=True) if r[0]}
    positions = []
    for r in wb["Positions"].iter_rows(min_row=2, values_only=True):
        if r[0] != personne or not r[1] or nombre(r[9]) <= 0:
            continue
        positions.append({"nom": r[2] or r[1], "poche": r[3] or "Autre", "enveloppe": r[4] or "?",
                          "investi": fmt(nombre(r[7])), "valeur": fmt(nombre(r[9])),
                          "frais_annuels_pct": fmt(frais.get(r[1], 0)), "date_valeur": date.today().isoformat()})
    flux = []
    for r in wb["Transactions"].iter_rows(min_row=2, values_only=True):
        if r[1] != personne or r[3] not in ("Versement", "Retrait") or not r[0]:
            continue
        montant = nombre(r[10]) or nombre(r[5]) * nombre(r[6])
        flux.append((en_date(r[0]), -montant if r[3] == "Versement" else montant))
    flux.sort()
    cibles = [{"poche": r[1], "cible_pct": fmt(nombre(r[2]) * 100)}
              for r in wb["Cibles"].iter_rows(min_row=2, values_only=True)
              if r[0] == personne and r[1] and nombre(r[2]) > 0]
    return positions, [{"date": d.isoformat(), "montant": fmt(m)} for d, m in flux], cibles


def main(classeur, personne, dossier):
    positions, flux, cibles = lire_classeur(classeur, personne)
    if not positions:
        raise SystemExit(f"Aucune position pour « {personne} » dans l'onglet Positions (valeurs calculées absentes ?).")
    d = Path(dossier)
    d.mkdir(parents=True, exist_ok=True)
    ecrire(d / "positions.csv", positions, list(positions[0]))
    if flux:
        ecrire(d / "flux.csv", flux, ["date", "montant"])
    if cibles:
        ecrire(d / "cibles.csv", cibles, ["poche", "cible_pct"])
    total = sum(float(p["valeur"]) for p in positions)
    print(f"{len(positions)} lignes ({total:,.2f} €) et {len(flux)} versements ou retraits importés dans {d}.")
    if not flux:
        print("Aucun versement dans Transactions : la performance (XIRR) ne pourra pas être calculée.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(0)
    main(*sys.argv[1:])
