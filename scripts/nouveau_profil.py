"""Crée le dossier privé complet d'un nouveau profil : python scripts/nouveau_profil.py <prenom> [--dossier prive]

Copie les modèles de templates/ (profil, profil de risque, budget, charte, plan d'investissement, checklist),
crée les CSV vides au bon format (scripts/fichiers_profil.py), parametres.csv, journal, bilans et accueil.
Ne touche jamais à un fichier existant : relancer le script complète un dossier sans rien écraser.
"""
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from fichiers_profil import CSV, RACINE, TEMPLATES, ecrire_csv, ecrire_parametres

MODELES = {
    "profil.md": "profil-modele.md",
    "profil-risque.md": "profil-risque-modele.md",
    "budget.md": "budget-modele.md",
    "charte.md": "charte-modele.md",
    "plan-investissement.md": "plan-investissement-modele.md",
    "checklist.md": "checklist-mise-en-place.md",
}
TEXTES = {
    "journal.md": "# Journal des décisions de {p}\n\n_Une entrée par décision hors plan : date, décision, raisons, source de l'idée, "
                  "émotion (1 à 10), verdict du Coach, décision finale, date du bilan à 3 mois. Les plus récentes en haut._\n",
    "bilans.md": "# Bilans de {p}\n\n_Bilans mensuels et annuels, le plus récent en haut. Rien n'est effacé._\n",
    "accueil.md": "# Accueil de {p}\n\n_Statut : en cours. Commencé le {d}._\n\n"
                  "| Étape | Statut | Notes |\n|---|---|---|\n| 1. Toi | à faire | |\n| 2. Ton argent | à faire | |\n"
                  "| 3. Tes objectifs | à faire | |\n| 4. Tes connaissances | à faire | |\n| 5. Ton rapport au risque | à faire | |\n"
                  "| 6. Ton rapport à l'argent et tes préférences | à faire | |\n| Restitution du profil de risque | à faire | |\n"
                  "| Documents remplis (profil, plan, charte) | à faire | |\n| Google Sheet créé | à faire | |\n"
                  "| Application créée | à faire | |\n",
}


def creer(prenom, base):
    p = prenom.strip()
    dossier = Path(base) / p.lower()
    dossier.mkdir(parents=True, exist_ok=True)
    crees, gardes = [], []
    aujourdhui = date.today().isoformat()
    for cible, modele in MODELES.items():
        f = dossier / cible
        if f.exists():
            gardes.append(cible)
            continue
        f.write_text((TEMPLATES / modele).read_text(encoding="utf-8").replace("<Prénom>", p), encoding="utf-8")
        crees.append(cible)
    for cible, texte in TEXTES.items():
        f = dossier / cible
        if f.exists():
            gardes.append(cible)
            continue
        f.write_text(texte.format(p=p, d=aujourdhui), encoding="utf-8")
        crees.append(cible)
    for nom, colonnes in CSV.items():
        f = dossier / nom
        if f.exists():
            gardes.append(nom)
            continue
        ecrire_csv(f, colonnes, [])
        crees.append(nom)
    if (dossier / "parametres.csv").exists():
        gardes.append("parametres.csv")
    else:
        ecrire_parametres(dossier, {"prenom": p, "date_creation": aujourdhui})
        crees.append("parametres.csv")
    return dossier, crees, gardes


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    base = args[args.index("--dossier") + 1] if "--dossier" in args else RACINE / "prive"
    dossier, crees, gardes = creer(args[0], base)
    print(f"Dossier : {dossier}")
    print(f"Créés ({len(crees)}) : {', '.join(crees) or 'aucun'}")
    if gardes:
        print(f"Déjà présents, non modifiés ({len(gardes)}) : {', '.join(gardes)}")
