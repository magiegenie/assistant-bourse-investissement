"""Test de profil de risque : affiche les questions, puis note les réponses.

Usage :
  python scripts/profil_risque.py questions [--montant 10000]   questions à poser, chiffrées en euros sur le montant
  python scripts/profil_risque.py prive/<prenom>                note prive/<prenom>/reponses-risque.csv

Format de reponses-risque.csv (une ligne par question, plus les infos facultatives) :
  id,reponse
  C1,C            lettre de l'option choisie
  T10,2000        perte en euros à partir de laquelle on dort mal
  K1,V            quiz : V (vrai), F (faux) ou ? (je ne sais pas)
  montant,10000   infos : montant, capital, mensuel, objectif (euros d'aujourd'hui), annees, contexte_marche

Quatre dimensions : capacité, tolérance, besoin de risque, connaissances. Profil = le plus prudent de
la capacité et de la tolérance (fiche D, point 56). Les questions et les points sont dans
connaissances/questionnaire-risque.json. Le script n'écrit rien. Outil d'aide, non validé scientifiquement.
"""
import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
from pathlib import Path
from allocation import lire
from projection import rendement_requis

RACINE = Path(__file__).resolve().parent.parent
QUESTIONNAIRE = RACINE / "connaissances" / "questionnaire-risque.json"
ORDRE_BLOCS = ["Toi", "Ton argent", "Tes objectifs", "Tes connaissances", "Ton rapport au risque"]


def euros(x):
    return f"{x:,.0f}".replace(",", " ")


def montants(montant):
    """Valeurs des repères {B}, {P20}, {M+8}... utilisés dans les textes des questions."""
    b = max(100, round((montant or 10000) * 0.10, -2))
    m = montant or 10000
    v = {"B": b, "B15": b * 1.5, "B2": b * 2, "B25": b * 2.5, "B3": b * 3, "B5": b * 5, "B6": b * 6,
         "P20": m * 0.20, "P35": m * 0.35}
    for pct in (2, 5, 8, 15, 25, 30, 35, 45):
        v[f"M+{pct}"] = m * pct / 100
        v[f"M-{pct}"] = -m * pct / 100
    return {k: (f"+{euros(x)}" if k.startswith("M+") else euros(x)) for k, x in v.items()}


def remplir(texte, valeurs):
    for k, x in valeurs.items():
        texte = texte.replace("{" + k + "}", x)
    return texte


def afficher_questions(q, montant):
    valeurs = montants(montant)
    base = f"{euros(montant)} €" if montant else "10 000 € (montant d'exemple, donne le tien pour personnaliser)"
    print(f"Test de profil de risque, chiffré sur {base}\n")
    for bloc in ORDRE_BLOCS:
        qs = [x for x in q["questions"] if x["bloc"] == bloc]
        if not qs:
            continue
        print(f"## {bloc}\n")
        for x in qs:
            print(f"**{x['id']}**. {remplir(x['texte'], valeurs)}")
            if x.get("type") == "quiz":
                print("   V (vrai) / F (faux) / ? (je ne sais pas)")
            for o in x.get("options", []):
                print(f"   {o['code']}) {remplir(o['texte'], valeurs)}")
            print()
    print("Infos à demander aussi : " + "; ".join(f"{k} ({v})" for k, v in q["infos"].items()))


def niveau(score):
    return min(5, int(score // 20) + 1)


def noter(q, rep):
    infos = {k: rep[k] for k in q["infos"] if k in rep}
    montant = float(infos["montant"]) if "montant" in infos else None
    dims = {"capacite": [0.0, 0.0], "tolerance": [0.0, 0.0], "connaissances": [0.0, 0.0]}
    plafonds, alertes, choix, quiz_faux, corrections = [], [], {}, 0, []
    perte_max = None
    for x in q["questions"]:
        r = rep.get(x["id"], "").strip()
        if not r:
            continue
        d, poids = x["dimension"], x.get("poids", 1)
        if x.get("type") == "quiz":
            r = r.upper()[:1]
            dims[d][1] += 1
            if r == x["bonne"]:
                dims[d][0] += 1
            else:
                if r in ("V", "F"):
                    quiz_faux += 1
                corrections.append(f"{x['id']} : {q['corrections_quiz'][x['id']]}")
            continue
        if x.get("type") == "montant":
            perte_max = float(r.replace(" ", "").replace("€", ""))
            if montant:
                pct = perte_max / montant * 100
                pts = next(p for seuil, p in x["grille_pct"] if pct < seuil)
                dims[d][0] += pts * poids
                dims[d][1] += 4 * poids
                cap = next((p for seuil, p in x["plafonds_pct"] if pct < seuil), None)
                if cap:
                    plafonds.append((cap, x["id"], d))
            continue
        opt = next((o for o in x["options"] if o["code"] == r.upper()), None)
        if opt is None:
            print(f"Réponse inconnue pour {x['id']} : {r} (ignorée)")
            continue
        choix[x["id"]] = opt["code"]
        if opt["points"] is None:
            continue
        maxi = max(o["points"] for o in x["options"] if o["points"] is not None)
        dims[d][0] += opt["points"] * poids
        dims[d][1] += maxi * poids
        if "plafond" in opt:
            plafonds.append((opt["plafond"], x["id"], d))
        if "alerte" in opt:
            alertes.append(opt["alerte"])
    scores = {d: (s / m * 100 if m else None) for d, (s, m) in dims.items()}
    return scores, plafonds, alertes, choix, quiz_faux, corrections, perte_max, montant, infos


def besoin(infos):
    try:
        cap, men = float(infos.get("capital", 0)), float(infos.get("mensuel", 0))
        obj, ans = float(infos["objectif"]), float(infos["annees"])
    except (KeyError, ValueError):
        return None, None
    r = rendement_requis(cap, men, ans, obj)
    if r is None:
        return None, "irréaliste"
    for seuil, nom in ((2, "faible"), (4, "moyen"), (6, "élevé")):
        if r <= seuil:
            return r, nom
    return r, "irréaliste"


def main(dossier):
    q = json.loads(QUESTIONNAIRE.read_text(encoding="utf-8"))
    noms = {n["niveau"]: n for n in q["niveaux"]}
    rep = {r["id"].strip(): r["reponse"].strip() for r in lire(Path(dossier) / "reponses-risque.csv")}
    scores, plafonds, alertes, choix, quiz_faux, corrections, perte_max, montant, infos = noter(q, rep)
    if scores["capacite"] is None or scores["tolerance"] is None:
        sys.exit("Il manque les réponses de capacité (C1 à C7) ou de tolérance (T1 à T10).")

    n_cap, n_tol = niveau(scores["capacite"]), niveau(scores["tolerance"])
    ecart = abs(n_cap - n_tol)
    for p, qid, d in plafonds:
        if d == "capacite" and p < n_cap:
            n_cap = p
            alertes.append(f"Capacité plafonnée au niveau {p} par la réponse {qid}.")
        if d == "tolerance" and p < n_tol:
            n_tol = p
            alertes.append(f"Tolérance plafonnée au niveau {p} par ta perte maximale acceptable : "
                           f"un profil plus offensif peut perdre davantage dans un krach type 2008.")
    final = min(n_cap, n_tol)
    r_req, n_besoin = besoin(infos)

    print("PROFIL DE RISQUE\n")
    print(f"{'Dimension':<24}{'Score':>7}{'Niveau':>8}")
    print(f"{'Capacité (finances)':<24}{scores['capacite']:>6.0f}/100{n_cap:>4}  {noms[n_cap]['nom']}")
    print(f"{'Tolérance (émotions)':<24}{scores['tolerance']:>6.0f}/100{n_tol:>4}  {noms[n_tol]['nom']}")
    if scores["connaissances"] is not None:
        sk = scores["connaissances"]
        nk = "faible" if sk < 40 else "moyen" if sk < 70 else "bon"
        print(f"{'Connaissances':<24}{sk:>6.0f}/100      {nk}")
    if r_req is not None:
        print(f"{'Besoin de risque':<24}  rendement réel nécessaire {r_req:.1f} %/an : {n_besoin}")
    elif n_besoin:
        print(f"{'Besoin de risque':<24}  objectif hors d'atteinte même à 30 %/an : irréaliste")
    else:
        print(f"{'Besoin de risque':<24}  non calculé (objectif, annees, capital, mensuel manquants)")

    print(f"\nPROFIL RETENU : {final}. {noms[final]['nom']} (actions : {noms[final]['actions']}, repère fiche D point 22)")
    print("Règle : le plus prudent de la capacité et de la tolérance décide.")
    if perte_max is not None:
        pct = f" soit {perte_max / montant * 100:.0f} % du montant" if montant else ""
        print(f"Perte maximale acceptable : {euros(perte_max)} €{pct}")

    if n_besoin == "faible" and final >= 4:
        alertes.append(f"Besoin de risque faible ({r_req:.1f} % réel suffit) : un cran plus prudent "
                       f"({final - 1}. {noms[final - 1]['nom']}) atteint l'objectif avec moins de stress. À la personne de choisir.")
    if n_besoin == "irréaliste" or (n_besoin == "élevé" and final <= 3):
        alertes.append("Objectif exigeant pour ce profil : revoir le montant, le délai ou le versement, pas le risque.")
    if ecart >= 2:
        alertes.append(f"Écart de {ecart} niveaux entre capacité et tolérance (avant plafonds) : en parler avant de fixer l'allocation.")
    if choix.get("T9") in ("A", "B") and (choix.get("T6") in ("C", "D") or choix.get("T7") in ("C", "D")):
        alertes.append("Tu as vendu lors d'une vraie baisse mais tu déclares tenir : le comportement réel compte plus que le déclaratif.")
    if choix.get("T9") == "E" and n_tol >= 4:
        alertes.append("Tolérance élevée jamais testée en vrai : commencer un cran en dessous et réévaluer après la première grosse baisse.")
    if montant and perte_max is not None and perte_max / montant < 0.20 and choix.get("T6") in ("C", "D"):
        alertes.append("Tu dis ne pas vendre à -20 % mais mal dormir avant : à clarifier, c'est souvent le sommeil qui gagne.")
    if perte_max is not None and not montant:
        alertes.append("Montant manquant (ligne montant) : la perte maximale acceptable n'a pas pu plafonner le profil. Ajouter le montant et relancer.")
    if infos.get("contexte_marche", "").lower() == "haut":
        alertes.append("Test passé avec des marchés proches de leurs plus hauts : on surestime souvent son courage (fiche D, point 56). Refaire le test après une baisse.")
    if scores["connaissances"] is not None and scores["connaissances"] < 40:
        alertes.append("Connaissances encore faibles : s'en tenir aux ETF larges et commencer par le module 1 du Coach.")
    if quiz_faux >= 2:
        alertes.append(f"{quiz_faux} réponses fausses données avec assurance au quiz : attention à l'excès de confiance (fiche F, point 37).")

    print("\nALERTES" if alertes else "\nAucune alerte.")
    for a in alertes:
        print(f"- {a}")
    if corrections:
        print("\nCORRECTIONS DU QUIZ")
        for c in corrections:
            print(f"- {c}")
    print("\nDonnées pour les scripts (à recopier dans profil-risque.md) :")
    print(f"profil_niveau: {final}\ncapacite_niveau: {n_cap}\ntolerance_niveau: {n_tol}")
    if perte_max is not None:
        print(f"perte_max_eur: {perte_max:.0f}")
    print("\nOutil d'aide à la réflexion, non validé scientifiquement : pas un conseil en investissement réglementé.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if args[0] == "questions":
        m = float(args[args.index("--montant") + 1]) if "--montant" in args else None
        afficher_questions(json.loads(QUESTIONNAIRE.read_text(encoding="utf-8")), m)
    else:
        main(args[0])
