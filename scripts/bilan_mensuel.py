"""Bilan mensuel en une commande : enchaîne répartition, performance, exposition, stress et budget.

Usage : python scripts/bilan_mensuel.py prive/<prenom> [versement] [taux_reference]
Chaque bloc est la sortie brute du script correspondant ; un bloc absent signale le fichier manquant.
L'Analyste lit ce bilan, puis explique et propose la prochaine action (routine mensuelle).
"""
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
SCRIPTS = Path(__file__).resolve().parent

BLOCS = [
    ("Répartition et versement du mois", "allocation.py", ("positions.csv", "cibles.csv"), lambda v, t: [v]),
    ("Performance réelle", "performance.py", ("positions.csv", "flux.csv"), lambda v, t: [t]),
    ("Exposition réelle", "exposition.py", ("positions.csv",), lambda v, t: []),
    ("Tests de résistance", "stress.py", ("positions.csv",), lambda v, t: []),
    ("Budget", "budget.py", ("budget.md",), lambda v, t: []),
]


def main(dossier, versement="0", taux="7"):
    d = Path(dossier)
    for titre, script, requis, extra in BLOCS:
        print(f"\n## {titre}\n")
        manquants = [f for f in requis if not (d / f).exists()]
        if manquants:
            print(f"Non calculé : fichier manquant ({', '.join(manquants)}).")
            continue
        r = subprocess.run([sys.executable, str(SCRIPTS / script), str(d), *extra(versement, taux)],
                           capture_output=True, text=True, encoding="utf-8")
        print(r.stdout.strip() if r.returncode == 0 else f"Erreur du script {script} : {r.stderr.strip()[-300:]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    main(*sys.argv[1:4])
