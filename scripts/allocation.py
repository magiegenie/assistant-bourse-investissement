"""Poids, écarts à la cible et répartition d'un versement sans rien vendre."""
import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def repartir(valeurs, cibles, versement):
    """Répartit le versement pour rapprocher chaque poche de sa cible, sans vente."""
    total_final = sum(valeurs.values()) + versement
    manques = {p: max(0.0, cibles.get(p, 0) / 100 * total_final - valeurs.get(p, 0)) for p in cibles}
    somme = sum(manques.values())
    if somme == 0:
        return {p: versement * c / 100 for p, c in cibles.items()}
    facteur = min(1.0, versement / somme)
    alloc = {p: m * facteur for p, m in manques.items()}
    reste = versement - sum(alloc.values())
    for p, c in cibles.items():
        alloc[p] += reste * c / 100
    return alloc

def main(dossier, versement):
    d = Path(dossier)
    positions = lire(d / "positions.csv")
    cibles = {r["poche"]: float(r["cible_pct"]) for r in lire(d / "cibles.csv")}
    valeurs = {}
    for r in positions:
        valeurs[r["poche"]] = valeurs.get(r["poche"], 0) + float(r["valeur"])
    total = sum(valeurs.values())
    print(f"Total : {total:,.2f} €\n")
    print(f"{'Poche':<18}{'Valeur':>12}{'Actuel':>9}{'Cible':>8}{'Écart':>8}")
    for p in sorted(set(valeurs) | set(cibles)):
        v = valeurs.get(p, 0); a = v / total * 100 if total else 0; c = cibles.get(p, 0)
        alerte = "  <- écart > 5 pts" if abs(a - c) > 5 else ""
        print(f"{p:<18}{v:>11,.0f}€{a:>8.1f}%{c:>7.0f}%{a - c:>+7.1f}{alerte}")
    if versement:
        print(f"\nRépartition du versement de {versement:,.0f} € :")
        for p, m in repartir(valeurs, cibles, versement).items():
            if m >= 1:
                print(f"  {p:<18}{m:>10,.0f} €")
    frais = sum(float(r["valeur"]) * float(r.get("frais_annuels_pct") or 0) / 100 for r in positions)
    print(f"\nFrais annuels estimés : {frais:,.2f} € ({frais / total * 100 if total else 0:.2f} %)")
    print("\nLignes :")
    for r in sorted(positions, key=lambda r: -float(r["valeur"])):
        print(f"  {r['nom']:<35}{float(r['valeur']) / total * 100:>6.1f}%")

if __name__ == "__main__":
    a = sys.argv[1:]
    if "--ajout" in a:
        # Simulation d'une décision, sans rien écrire : --ajout <nom> <poche> <montant>
        i = a.index("--ajout"); nom, poche, montant = a[i + 1], a[i + 2], float(a[i + 3]); del a[i:i + 4]
        _lire = lire
        def lire(chemin, _l=_lire):
            lignes = _l(chemin)
            if Path(chemin).name == "positions.csv":
                lignes.append({"nom": nom, "poche": poche, "enveloppe": "?", "investi": montant, "valeur": montant, "frais_annuels_pct": 0})
            return lignes
        print(f"SIMULATION : ajout de {montant:,.0f} € sur {nom} (poche {poche}), rien n'est enregistré.\n")
    main(a[0], float(a[1]) if len(a) > 1 else 0)
