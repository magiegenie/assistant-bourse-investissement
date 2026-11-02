"""Clôtures de la semaine pour la newsletter : python scripts/cloture_hebdo.py [--fin AAAA-MM-JJ] [--sortie fichier.json]

Lit donnees/reperes.csv (ou donnees/actions-fr.csv), interroge l'API publique de graphiques de Yahoo Finance (sans clé) et calcule, pour
chaque repère, la variation entre la clôture du vendredi précédent et celle du vendredi demandé, plus les
clôtures de chaque jour de la semaine (pour le récit jour par jour).

  --fin     : dernier jour de la semaine couverte (défaut : le dernier vendredi passé)
  --sortie  : écrit le résultat en JSON ; sinon affiche un tableau

Bibliothèque standard uniquement. Données Yahoo indicatives : toujours citer la source et la date. Un repère
qui ne répond pas reste dans le résultat avec une valeur nulle : la newsletter écrit alors « non disponible ».
Pour les taux, la variation est donnée en points de pourcentage (0,10 = 10 points de base), pas en pourcentage.
"""
import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=1mo&interval=1d"
ENTETE = {"User-Agent": "Mozilla/5.0 (assistant-bourse-investissement)"}


def dernier_vendredi(aujourdhui=None):
    d = aujourdhui or date.today()
    return d - timedelta(days=(d.weekday() - 4) % 7)


def lire_reperes(chemin=RACINE / "donnees" / "reperes.csv"):
    with open(chemin, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def telecharger(ticker, essais=2):
    url = URL.format(ticker=urllib.parse.quote(ticker, safe=""))
    derniere = None
    for i in range(essais):
        try:
            req = urllib.request.Request(url, headers=ENTETE)
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.load(r)
        except Exception as e:  # réseau, quota, ticker inconnu
            derniere = e
            time.sleep(1 + i)
    raise OSError(str(derniere))


def clotures(donnees):
    """Liste triée [(date, clôture)] sans les jours sans cours."""
    r = donnees["chart"]["result"][0]
    fuseau = timezone(timedelta(seconds=r["meta"].get("gmtoffset", 0)))
    sortie = []
    for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]):
        if c is not None:
            sortie.append((datetime.fromtimestamp(t, fuseau).date(), float(c)))
    return sortie


def calcul(serie, fin, type_repere):
    """Variation de la semaine finissant à `fin` (inclus) et clôtures du lundi au vendredi."""
    avant = [x for x in serie if x[0] <= fin]
    if not avant:
        return None
    debut_semaine = fin - timedelta(days=4)
    precedente = [x for x in avant if x[0] < debut_semaine]
    semaine = [x for x in avant if x[0] >= debut_semaine]
    if not precedente or not semaine:
        return None
    ref, dern = precedente[-1], semaine[-1]
    if type_repere == "taux":
        variation = round(dern[1] - ref[1], 3)
    else:
        variation = round((dern[1] / ref[1] - 1) * 100, 2)
    return {
        "reference": {"date": ref[0].isoformat(), "valeur": round(ref[1], 4)},
        "derniere": {"date": dern[0].isoformat(), "valeur": round(dern[1], 4)},
        "variation": variation,
        "unite_variation": "points" if type_repere == "taux" else "%",
        "jours": [{"date": d.isoformat(), "valeur": round(v, 4)} for d, v in semaine],
    }


def collecter(fin, reperes=None, telecharger_fn=telecharger):
    resultat = {"fin": fin.isoformat(), "source": "Yahoo Finance (donnees indicatives)", "reperes": []}
    for r in reperes or lire_reperes():
        ligne = {"cle": r["cle"], "nom": r["nom"], "groupe": r["groupe"], "ticker": r["ticker_yahoo"]}
        try:
            calc = calcul(clotures(telecharger_fn(r["ticker_yahoo"])), fin, r["type"])
        except Exception as e:
            calc, ligne["erreur"] = None, str(e)[:120]
        ligne.update(calc or {"variation": None})
        resultat["reperes"].append(ligne)
    return resultat


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fin", help="dernier jour de la semaine (AAAA-MM-JJ), défaut : dernier vendredi")
    ap.add_argument("--sortie", help="fichier JSON à écrire")
    ap.add_argument("--liste", default="reperes", help="reperes (indices, devises, matières) ou actions-fr (valeurs du CAC 40)")
    args = ap.parse_args()
    fin = date.fromisoformat(args.fin) if args.fin else dernier_vendredi()
    res = collecter(fin, lire_reperes(RACINE / "donnees" / f"{args.liste}.csv"))
    if args.sortie:
        Path(args.sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        ok = sum(1 for r in res["reperes"] if r.get("variation") is not None)
        print(f"{args.sortie} écrit : {ok} repères sur {len(res['reperes'])}.")
        return
    print(f"Semaine finissant le {fin.isoformat()} ({res['source']})")
    for r in res["reperes"]:
        v = r.get("variation")
        txt = "non disponible" if v is None else f"{v:+.2f} {r['unite_variation']} (clôture {r['derniere']['valeur']} le {r['derniere']['date']})"
        print(f"{r['nom']:<42} {txt}")


if __name__ == "__main__":
    main()
