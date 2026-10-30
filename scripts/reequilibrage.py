"""Plan de rééquilibrage par ventes, avec coût fiscal estimé. Ne passe aucun ordre.

Usage : python scripts/reequilibrage.py prive/<prenom> [versement] [seuil_pts]
  versement : nouvel argent à placer d'abord sur les poches en retard (défaut 0)
  seuil_pts : écart en points au-delà duquel on vend (défaut 10, fiche E point 31 et routine de l'Analyste)

Logique (idée reprise du skill « portfolio-drift-rebalancer », recodée pour les enveloppes françaises) :
1. Le versement va d'abord aux poches en retard (comme allocation.py).
2. Si une poche reste au-dessus de sa cible de plus de `seuil_pts`, on propose de vendre l'excédent.
3. Ordre des ventes, du moins coûteux au plus coûteux : PEA et assurance vie (un arbitrage interne
   n'est pas imposé), puis CTO en moins-value, puis CTO avec la plus petite plus-value.
4. Le produit d'une vente se réinvestit dans la MÊME enveloppe (on ne sort pas l'argent d'un PEA).
5. Vérification : total des achats = total des ventes + versement.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from allocation import lire, repartir

PFU = 31.4  # CTO, 2026 (fiche C, point 16)


def main(dossier, versement=0.0, seuil=10.0):
    d = Path(dossier)
    positions = lire(d / "positions.csv")
    cibles = {r["poche"]: float(r["cible_pct"]) for r in lire(d / "cibles.csv")}
    valeurs = {}
    for r in positions:
        valeurs[r["poche"]] = valeurs.get(r["poche"], 0) + float(r["valeur"])
    for p, m in repartir(valeurs, cibles, versement).items():
        valeurs[p] = valeurs.get(p, 0) + m
    total = sum(valeurs.values())

    exces = {p: valeurs.get(p, 0) - c / 100 * total for p, c in cibles.items()}
    a_vendre = {p: e for p, e in exces.items() if e / total * 100 > seuil}
    print(f"Total après versement : {total:,.0f} €   Seuil de vente : {seuil:.0f} points\n")
    print(f"{'Poche':<18}{'Actuel':>8}{'Cible':>8}{'Écart':>8}")
    for p in sorted(cibles):
        a = valeurs.get(p, 0) / total * 100
        print(f"{p:<18}{a:>7.1f}%{cibles[p]:>7.0f}%{a - cibles[p]:>+7.1f}")
    if not a_vendre:
        print("\nAucune poche ne dépasse le seuil : pas de vente. Le versement suffit (rééquilibrage par les flux).")
        return

    def cout(r):
        env = r["enveloppe"].strip().upper()
        if env in ("PEA", "AV", "ASSURANCE VIE", "PER"):
            return (0, 0.0)
        v, i = float(r["valeur"]), float(r["investi"])
        return (1 if v < i else 2, (v - i) / v if v else 0)

    print("\nVentes proposées (à faire valider, rien n'est exécuté) :")
    total_ventes, total_impot = 0.0, 0.0
    par_enveloppe = {}
    for p, montant in a_vendre.items():
        reste = montant
        for r in sorted([r for r in positions if r["poche"] == p], key=cout):
            if reste <= 0:
                break
            v = float(r["valeur"])
            vente = min(v, reste)
            env = r["enveloppe"].strip().upper()
            impot = 0.0
            if cout(r)[0] > 0:
                impot = max(0.0, vente * (v - float(r["investi"])) / v) * PFU / 100
            print(f"  Vendre {vente:>10,.0f} € de {r['nom']} ({env})  impôt estimé : {impot:,.0f} €")
            par_enveloppe[env] = par_enveloppe.get(env, 0) + vente
            total_ventes += vente
            total_impot += impot
            reste -= vente
    manques = {p: c / 100 * total - valeurs.get(p, 0) for p, c in cibles.items()}
    manques = {p: m for p, m in manques.items() if m > 0}
    somme = sum(manques.values())
    print("\nRéinvestissement (dans la même enveloppe que la vente) :")
    achats = 0.0
    for env, produit in par_enveloppe.items():
        for p, m in manques.items():
            a = produit * m / somme if somme else 0
            achats += a
            if a >= 1:
                print(f"  Acheter {a:>10,.0f} € en {p} (enveloppe {env})")
    print(f"\nVentes par enveloppe : " + ", ".join(f"{e} {m:,.0f} €" for e, m in par_enveloppe.items()))
    print(f"Impôt total estimé : {total_impot:,.0f} € (PFU {PFU} % sur les gains en CTO ; calcul détaillé : scripts/fiscalite.py)")
    ok = abs(achats - total_ventes) < 1
    print("Contrôle achats = ventes :", "OK" if ok else "ERREUR, ne pas utiliser ce plan")
    print("Vérifier qu'un ETF de la poche à renforcer existe dans chaque enveloppe concernée (éligibilité PEA).")


if __name__ == "__main__":
    a = sys.argv[1:]
    main(a[0], float(a[1]) if len(a) > 1 else 0.0, float(a[2]) if len(a) > 2 else 10.0)
