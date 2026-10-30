"""Synthèse du budget depuis prive/<prenom>/budget.md : taux d'épargne, répartition, épargne de précaution.

Usage : python scripts/budget.py prive/<prenom> [--precaution MONTANT]
Lit le tableau mensuel de budget.md (format de templates/budget-modele.md). Montants en euros, sans symbole
obligatoire (« 1 850 », « 1850 € » et « 1850,50 » sont acceptés). Repères : fiche A.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
COLONNES = ("mois", "revenu", "besoins", "envies", "epargne")


def nombre(texte):
    t = re.sub(r"[^\d,.-]", "", texte.replace(" ", "").replace(" ", "")).replace(",", ".")
    try:
        return float(t)
    except ValueError:
        return None


def lire_mois(chemin):
    """Renvoie [{mois, revenu, besoins, envies, epargne}] pour chaque ligne complète du tableau mensuel."""
    lignes = []
    for l in Path(chemin).read_text(encoding="utf-8").splitlines():
        if not l.startswith("|") or "---" in l or "Revenu net" in l:
            continue
        cellules = [c.strip() for c in l.strip("|").split("|")]
        if len(cellules) < 5 or not cellules[0]:
            continue
        valeurs = [nombre(c) for c in cellules[1:5]]
        if None in valeurs:
            continue
        lignes.append(dict(zip(COLONNES, [cellules[0]] + valeurs)))
    return lignes


def synthese(mois, precaution=None):
    r = {}
    if not mois:
        return r
    rev = sum(m["revenu"] for m in mois)
    r["mois"] = len(mois)
    r["taux_epargne"] = sum(m["epargne"] for m in mois) / rev if rev else 0
    r["besoins"] = sum(m["besoins"] for m in mois) / rev if rev else 0
    r["envies"] = sum(m["envies"] for m in mois) / rev if rev else 0
    r["depenses_moy"] = sum(m["besoins"] + m["envies"] for m in mois) / len(mois)
    r["ecart_moy"] = sum(m["revenu"] - m["besoins"] - m["envies"] - m["epargne"] for m in mois) / len(mois)
    if precaution is not None and r["depenses_moy"]:
        r["precaution_mois"] = precaution / r["depenses_moy"]
    return r


def main(args):
    precaution = None
    if "--precaution" in args:
        i = args.index("--precaution")
        precaution = float(args[i + 1])
        del args[i:i + 2]
    mois = lire_mois(Path(args[0]) / "budget.md")
    if not mois:
        print("Aucun mois complet dans budget.md : remplir au moins une ligne du tableau.")
        return
    s = synthese(mois, precaution)
    print(f"Mois analysés : {s['mois']} (de {mois[0]['mois']} à {mois[-1]['mois']})")
    print(f"Besoins : {s['besoins'] * 100:.0f} %   Envies : {s['envies'] * 100:.0f} %   "
          f"Épargne + investissement : {s['taux_epargne'] * 100:.0f} %   (repère 50 / 30 / 20, fiche A)")
    print(f"Dépenses mensuelles moyennes : {s['depenses_moy']:,.0f} €")
    if abs(s["ecart_moy"]) >= 1:
        print(f"Écart non expliqué moyen : {s['ecart_moy']:+,.0f} €/mois (argent qui n'apparaît dans aucune case)")
    if "precaution_mois" in s:
        alerte = "  <- sous les 3 mois conseillés" if s["precaution_mois"] < 3 else ""
        print(f"Épargne de précaution : {s['precaution_mois']:.1f} mois de dépenses{alerte}")
    if s["taux_epargne"] < 0.2:
        print("Taux d'épargne sous 20 % : premier levier à travailler avant le choix des placements (fiche A).")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    main(sys.argv[1:])
