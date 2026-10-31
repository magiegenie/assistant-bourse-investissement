"""Saisie rapide d'une opération : met à jour positions.csv et flux.csv ensemble, sans éditer de fichier.

Usage : python scripts/saisie.py prive/<prenom> <operation> [arguments] [--date AAAA-MM-JJ]
  investir <ligne> <montant>     versement d'argent frais ET achat sur la ligne (le cas le plus courant)
  versement <montant>            argent frais versé, pas encore investi
  achat <ligne> <montant>        achat avec de l'argent déjà versé
  vente <ligne> <montant> [--retrait]   vente ; avec --retrait, l'argent sort du portefeuille
  valeur <ligne> <montant>       nouvelle valeur actuelle de la ligne
  retrait <montant>              argent sorti du portefeuille
Pour une ligne nouvelle : ajouter --poche P --enveloppe E [--frais 0.20].
<ligne> : un morceau du nom suffit s'il est unique (« world » pour « ETF MSCI World »).
Chaque écriture garde l'ancienne version en .bak. Rien n'est envoyé nulle part.
"""
import argparse
import csv
import shutil
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
CHAMPS_POS = ["nom", "poche", "enveloppe", "investi", "valeur", "frais_annuels_pct", "date_valeur"]


def lire(chemin):
    if not chemin.exists():
        return [], None
    with open(chemin, encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames


def ecrire(chemin, lignes, champs):
    if chemin.exists():
        shutil.copy(chemin, chemin.with_suffix(chemin.suffix + ".bak"))
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=champs, extrasaction="ignore")
        w.writeheader()
        w.writerows(lignes)


def trouver(positions, morceau):
    m = morceau.lower()
    exacts = [p for p in positions if p["nom"].lower() == m]
    if exacts:
        return exacts[0]
    trouves = [p for p in positions if m in p["nom"].lower()]
    if len(trouves) > 1:
        raise SystemExit(f"« {morceau} » est ambigu : " + ", ".join(p["nom"] for p in trouves))
    return trouves[0] if trouves else None


def fmt(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def appliquer(dossier, op, args, quand, poche=None, enveloppe=None, frais=None, retrait=False):
    """Applique l'opération et renvoie une phrase de confirmation."""
    d = Path(dossier)
    positions, champs = lire(d / "positions.csv")
    champs = champs or CHAMPS_POS
    flux, _ = lire(d / "flux.csv")
    jour = quand.isoformat()
    montant = float(args[-1])
    if montant <= 0:
        raise SystemExit("Le montant doit être positif.")

    def ajout_flux(valeur):
        flux.append({"date": jour, "montant": fmt(valeur)})

    if op in ("versement", "retrait"):
        ajout_flux(-montant if op == "versement" else montant)
        ecrire(d / "flux.csv", flux, ["date", "montant"])
        return f"{op.capitalize()} de {montant:,.2f} € noté le {quand:%d/%m/%Y}."

    nom = args[0]
    ligne = trouver(positions, nom)
    if ligne is None:
        if op not in ("investir", "achat"):
            raise SystemExit(f"Aucune ligne ne correspond à « {nom} ».")
        if not (poche and enveloppe):
            raise SystemExit(f"Ligne nouvelle « {nom} » : préciser --poche et --enveloppe.")
        ligne = {"nom": nom, "poche": poche, "enveloppe": enveloppe, "investi": "0", "valeur": "0",
                 "frais_annuels_pct": fmt(frais or 0), "date_valeur": jour}
        positions.append(ligne)
    investi, valeur = float(ligne["investi"]), float(ligne["valeur"])

    if op in ("investir", "achat"):
        ligne["investi"], ligne["valeur"] = fmt(investi + montant), fmt(valeur + montant)
        if op == "investir":
            ajout_flux(-montant)
        phrase = f"{montant:,.2f} € ajoutés sur {ligne['nom']} ({ligne['enveloppe']})."
    elif op == "vente":
        if montant > valeur + 0.01:
            raise SystemExit(f"Vente de {montant:,.2f} € supérieure à la valeur de la ligne ({valeur:,.2f} €).")
        part = montant / valeur if valeur else 1
        ligne["investi"], ligne["valeur"] = fmt(investi * (1 - part)), fmt(valeur - montant)
        if retrait:
            ajout_flux(montant)
        phrase = f"Vente de {montant:,.2f} € sur {ligne['nom']}" + (" , argent retiré." if retrait else ", argent resté dans l'enveloppe.")
        phrase = phrase.replace(" ,", ",")
    elif op == "valeur":
        ligne["valeur"] = fmt(montant)
        phrase = f"Valeur de {ligne['nom']} mise à {montant:,.2f} €."
    else:
        raise SystemExit(f"Opération inconnue : {op}")
    ligne["date_valeur"] = jour
    ecrire(d / "positions.csv", [p for p in positions if float(p["valeur"]) > 0.005 or float(p["investi"]) > 0.005],
           champs if "date_valeur" in champs else champs + ["date_valeur"])
    if op in ("investir", "vente") and (op == "investir" or retrait):
        ecrire(d / "flux.csv", flux, ["date", "montant"])
    return phrase


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("dossier")
    p.add_argument("operation", choices=["investir", "versement", "achat", "vente", "valeur", "retrait"])
    p.add_argument("args", nargs="+")
    p.add_argument("--date", type=date.fromisoformat, default=date.today())
    p.add_argument("--poche")
    p.add_argument("--enveloppe")
    p.add_argument("--frais", type=float)
    p.add_argument("--retrait", action="store_true")
    a = p.parse_args()
    print(appliquer(a.dossier, a.operation, a.args, a.date, a.poche, a.enveloppe, a.frais, a.retrait))


if __name__ == "__main__":
    main()
