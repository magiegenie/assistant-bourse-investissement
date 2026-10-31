"""Formats des fichiers d'un profil (prive/<prenom>/), partagés par tous les scripts. Source unique : ne pas dupliquer."""
import csv
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TEMPLATES = RACINE / "templates"

# Fichiers CSV : nom -> colonnes (les scripts de calcul ignorent les colonnes en plus)
CSV = {
    "positions.csv": ["nom", "poche", "enveloppe", "investi", "valeur", "frais_annuels_pct", "date_valeur",
                      "quantite", "isin", "ticker_yahoo"],
    "cibles.csv": ["poche", "cible_pct"],
    "flux.csv": ["date", "montant"],
    "transactions.csv": ["date", "enveloppe", "type", "id_actif", "nom", "isin", "quantite", "prix", "frais",
                         "devise", "taux_change", "montant_eur", "prevu", "source", "note"],
    "objectifs.csv": ["nom", "montant", "date_debut", "date_cible", "montant_actuel", "poche", "priorite"],
    "budget.csv": ["mois", "revenu_net", "besoins", "envies", "epargne_investissement", "abonnements", "note"],
    "reponses-risque.csv": ["id", "reponse"],
}

# Paramètres d'un profil : clé -> (valeur par défaut, description). Rempli à l'accueil, lu par les scripts.
PARAMETRES = {
    "prenom": ("", "Prénom"),
    "date_creation": ("", "Date de création du profil (AAAA-MM-JJ)"),
    "courtier_principal": ("", "Courtier ou banque principal"),
    "autres_comptes": ("", "Autres comptes (assurance vie, livrets, épargne salariale...)"),
    "versement_mensuel": ("", "Versement mensuel prévu, en euros"),
    "jour_versement": ("", "Jour du mois du versement"),
    "date_ouverture_pea": ("", "Date d'ouverture du PEA (AAAA-MM-JJ), vide si pas de PEA"),
    "total_verse_pea": ("", "Total versé sur le PEA (plafond 150 000 €)"),
    "plafond_crypto_pct": ("10", "Part maximale de crypto-actifs, en %"),
    "plafond_ligne_pct": ("5", "Poids maximal d'une ligne hors ETF large, en %"),
    "seuil_reequilibrage_pts": ("10", "Écart à la cible qui déclenche un rééquilibrage par ventes, en points"),
    "indice_reference": ("MSCI_WORLD", "Indice de comparaison choisi à l'avance (id de donnees/historique/indices.csv)"),
    "sheet_drive_id": ("", "Identifiant du Google Sheet dans le Drive"),
    "sheet_drive_url": ("", "Lien du Google Sheet"),
    "app_url": ("", "Lien de l'application mobile"),
    "partage_associe": ("non", "L'associé peut voir ce portefeuille : oui / non"),
}

# Poches proposées par défaut (les cibles de la personne font foi dès qu'elles existent)
POCHES_DEFAUT = ["Monde", "USA", "Europe", "Émergents", "Obligations", "Fonds euro", "Crypto", "Liquidités"]


def lire_csv(chemin):
    chemin = Path(chemin)
    if not chemin.exists():
        return []
    with open(chemin, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ecrire_csv(chemin, colonnes, lignes):
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=colonnes, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)


def lire_parametres(dossier):
    p = {cle: defaut for cle, (defaut, _) in PARAMETRES.items()}
    for r in lire_csv(Path(dossier) / "parametres.csv"):
        p[r["cle"]] = r["valeur"]
    return p


def ecrire_parametres(dossier, valeurs):
    lignes = [{"cle": c, "valeur": valeurs.get(c, d), "description": desc} for c, (d, desc) in PARAMETRES.items()]
    ecrire_csv(Path(dossier) / "parametres.csv", ["cle", "valeur", "description"], lignes)


def nombre(x, defaut=0.0):
    """'1 234,50 €' -> 1234.5 ; vide ou illisible -> defaut."""
    if x is None:
        return defaut
    if isinstance(x, (int, float)):
        return float(x)
    t = str(x).replace(" ", "").replace("\xa0", "").replace(" ", "").replace("€", "").replace("%", "")
    if t.count(",") == 1 and t.count(".") <= 1 and t.rfind(",") > t.rfind("."):
        t = t.replace(".", "").replace(",", ".")
    else:
        t = t.replace(",", "")
    try:
        return float(t)
    except ValueError:
        return defaut
