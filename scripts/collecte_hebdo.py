"""Collecte hebdomadaire de l'actualité publique : lit les flux de donnees/sources.csv et écrit un digest.

Usage : python scripts/collecte_hebdo.py [--fin AAAA-MM-JJ] [--jours 7] [--sortie docs/veille]
  --fin   : dernier jour couvert (défaut : aujourd'hui)
  --jours : nombre de jours couverts (défaut 7)

Bibliothèque standard uniquement. Données publiques seulement : aucun profil, aucune position.
Le digest liste les titres, la date et le lien, regroupés par famille de source. Il ne résume pas et ne
commente pas : c'est la matière première du Veilleur et de la newsletter du dimanche (fiche H).
"""
import argparse
import csv
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
ATOM = "{http://www.w3.org/2005/Atom}"
ORDRE = ["banque centrale", "statistique", "regulateur", "presse", "emetteur ETF", "calendrier",
         "pedagogie video", "podcast"]


def lire_sources(chemin=RACINE / "donnees" / "sources.csv"):
    with open(chemin, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("url_flux")]


def telecharger(url, delai=20):
    req = urllib.request.Request(url, headers={"User-Agent": "assistant-bourse-investissement/1.0"})
    with urllib.request.urlopen(req, timeout=delai) as r:
        return r.read()


def date_de(texte):
    if not texte:
        return None
    texte = texte.strip()
    try:
        d = parsedate_to_datetime(texte)
    except (TypeError, ValueError):
        try:
            d = datetime.fromisoformat(texte.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc).date()


def propre(texte):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", texte or "")).strip()


def articles(contenu):
    """Renvoie [(date, titre, lien)] depuis un flux RSS 2.0 ou Atom."""
    racine = ET.fromstring(contenu)
    sortie = []
    for it in racine.iter("item"):
        sortie.append((date_de(it.findtext("pubDate") or it.findtext("{http://purl.org/dc/elements/1.1/}date")),
                       propre(it.findtext("title")), (it.findtext("link") or "").strip()))
    for e in racine.iter(f"{ATOM}entry"):
        lien = e.find(f"{ATOM}link")
        sortie.append((date_de(e.findtext(f"{ATOM}published") or e.findtext(f"{ATOM}updated")),
                       propre(e.findtext(f"{ATOM}title")), lien.get("href", "") if lien is not None else ""))
    return sortie


def collecter(sources, debut, fin, telecharge=telecharger):
    retenus, erreurs, vus = {}, [], set()
    for s in sources:
        try:
            liste = articles(telecharge(s["url_flux"]))
        except Exception as e:  # réseau, XML invalide : on note et on continue
            erreurs.append((s["nom"], type(e).__name__))
            continue
        for d, titre, lien in liste:
            cle = titre.lower()
            if not titre or d is None or not (debut <= d <= fin) or cle in vus:
                continue
            vus.add(cle)
            retenus.setdefault(s["famille"], []).append((d, s["nom"], titre, lien))
    return retenus, erreurs


def ecrire(retenus, erreurs, debut, fin, dossier):
    annee, semaine, _ = fin.isocalendar()
    chemin = Path(dossier) / f"{annee}-S{semaine:02d}.md"
    chemin.parent.mkdir(parents=True, exist_ok=True)
    total = sum(len(v) for v in retenus.values())
    l = [f"# Veille brute : {debut:%d/%m/%Y} au {fin:%d/%m/%Y}", "",
         f"{total} titres collectés automatiquement depuis `donnees/sources.csv`. Matière brute, non vérifiée "
         "ni commentée : le Veilleur trie, vérifie et explique (fiche H).", ""]
    for fam in sorted(retenus, key=lambda f: ORDRE.index(f) if f in ORDRE else 99):
        l += [f"## {fam.capitalize()}", ""]
        for d, nom, titre, lien in sorted(retenus[fam], reverse=True)[:25]:
            l.append(f"- {d:%d/%m} | {nom} | [{titre}]({lien})" if lien else f"- {d:%d/%m} | {nom} | {titre}")
        l.append("")
    if erreurs:
        l += ["## Flux en échec cette semaine", ""] + [f"- {n} ({e})" for n, e in erreurs] + [""]
    chemin.write_text("\n".join(l), encoding="utf-8")
    return chemin, total


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fin", type=date.fromisoformat, default=date.today())
    p.add_argument("--jours", type=int, default=7)
    p.add_argument("--sortie", default=str(RACINE / "docs" / "veille"))
    a = p.parse_args()
    debut = a.fin - timedelta(days=a.jours - 1)
    retenus, erreurs = collecter(lire_sources(), debut, a.fin)
    chemin, total = ecrire(retenus, erreurs, debut, a.fin, a.sortie)
    print(f"{total} titres, {len(erreurs)} flux en échec : {chemin}")


if __name__ == "__main__":
    main()
