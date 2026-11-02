"""Fabrique l'email HTML de la newsletter du dimanche à partir d'un fichier JSON de contenu.

Usage : python scripts/newsletter_html.py edition.json [--sortie edition.html]

Le JSON décrit le contenu (voir templates/newsletter-modele.md). Ce script s'occupe de la mise en forme et
garantit les règles de lecture :
  - aucun lien dans le corps : les textes citent une source avec [[src:cle]] et le script la transforme
    en [1], [2]... numérotés dans l'ordre où la lecture les rencontre ;
  - tous les liens sont réunis dans le bloc « Sources » en bas, dans cet ordre ;
  - dans « Pourquoi ça a baissé », chaque étape de cause cite une source ou dit « cause non établie » ;
  - le temps de lecture est calculé d'après le nombre de mots ;
  - le contrôle final refuse les tirets longs, les emojis, les adresses web dans le corps et toute source
    citée sans être déclarée (ou déclarée sans être citée).

Bibliothèque standard uniquement. Données publiques seulement : aucun montant réel ne doit être écrit dans le dépôt.
"""
import argparse
import html
import json
import math
import re
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

NIVEAUX = {
    "ignorer": ("À ignorer", "#5b6673", "#e9edf1"),
    "surveiller": ("À surveiller", "#7a4f00", "#fcefcf"),
    "agir": ("À agir", "#9b1c1c", "#fde3e3"),
}
MOTS_PAR_MINUTE = 230
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre",
        "novembre", "décembre"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
MARQUEUR = re.compile(r"\[\[src:([a-z0-9_\-]+)\]\]")
GRAS = re.compile(r"\*\*(.+?)\*\*")

# Styles en ligne (les clients mail ignorent souvent les feuilles de style), doublés d'une petite feuille de style pour le mobile.
# Design clair uniquement : pas de mode sombre.
S = {
    "page": "margin:0;padding:0;background-color:#eef1f5;",
    "cadre": "max-width:640px;width:100%;margin:0 auto;table-layout:fixed;font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;",
    "texte": "font-family:Georgia,'Times New Roman',serif;font-size:17px;line-height:1.65;color:#1d2733;",
    "ui": "",
    "carte": "background-color:#ffffff;border-radius:16px;padding:26px 26px 22px 26px;",
    "fond_doux": "background-color:#f3f6fa;border-radius:12px;padding:20px 22px;",
    "fond_bleu": "background-color:#dbe9f9;border-radius:16px;padding:26px 26px 22px 26px;",
    "h2": "margin:0 0 16px 0;font-size:22px;line-height:1.25;font-weight:700;color:#12304a;",
    "petit": "font-size:14px;line-height:1.55;color:#5b6673;",
    "pos": "color:#17794a;",
    "neg": "color:#b3261e;",
}


UI_FONT = "font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;"


def a(cls, extra=""):
    """Attributs class + style en ligne pour les clés de S (plusieurs clés séparées par des espaces)."""
    style = "".join(S[c] for c in cls.split()) + extra
    return f'style="{style}"'


def liste(x):
    """Un texte seul ou une liste de paragraphes, toujours rendu comme une liste."""
    if x is None:
        return []
    return [x] if isinstance(x, str) else list(x)


class Rendu:
    def __init__(self, contenu):
        self.c = contenu
        self.sources = contenu.get("sources", {})
        self.ordre = []  # clés de sources dans l'ordre de lecture

    # ---- texte ----
    def num(self, cle):
        if cle not in self.sources:
            raise SystemExit(f"Source citée mais non déclarée : {cle}")
        if cle not in self.ordre:
            self.ordre.append(cle)
        return self.ordre.index(cle) + 1

    def t(self, texte):
        """Texte brut -> HTML : échappe, met le **gras**, remplace [[src:x]] par [n]."""
        out = html.escape(str(texte), quote=False)
        out = GRAS.sub(r"<strong>\1</strong>", out)

        def renvoi(m):
            n = self.num(m.group(1))
            return f'<sup style="{S["ui"]}font-size:11px;color:#12304a;">[{n}]</sup>'

        return MARQUEUR.sub(renvoi, out)

    def paragraphes(self, x, taille="16px", marge="0 0 10px 0"):
        return "".join(f'<p {a("texte", f"margin:{marge};font-size:{taille};")}>{self.t(p)}</p>' for p in liste(x))

    def pastille(self, niveau):
        nom, couleur, fond = NIVEAUX[niveau]
        return (f'<span style="{S["ui"]}display:inline-block;padding:3px 10px;border-radius:999px;font-size:12px;'
                f'font-weight:600;color:{couleur};background-color:{fond};">{nom}</span>')

    def variation(self, v, neutre=False):
        """Variation en vert ou rouge ; en gris si le sens n'est ni bon ni mauvais (VIX, taux, pétrole)."""
        if v in (None, ""):
            return f'<span style="{S["ui"]}color:#8a94a0;">non disponible</span>'
        texte = str(v)
        if neutre:
            return f'<span style="{S["ui"]}font-weight:600;color:#5b6673;">{html.escape(texte)}</span>'
        cls = "neg" if texte.strip().startswith(("-", chr(8722))) else "pos"
        return f'<span style="{S["ui"]}font-weight:600;{S[cls]}">{html.escape(texte)}</span>'

    # ---- briques ----
    def titre_section(self, texte):
        return f'<h2 {a("h2 ui")}>{html.escape(texte)}</h2>'

    def sous_titre(self, texte, marge="18px 0 6px 0"):
        return (f'<div {a("ui", f"font-size:16px;font-weight:700;color:#1d2733;margin:{marge};")}>'
                f'{self.t(texte)}</div>')

    def boite(self, cle, interieur, marge="0", padding=None, fond=None):
        """Boîte colorée : un tableau avec bgcolor et background-color, que Gmail respecte (il ignore le fond des div)."""
        bg = fond or re.search(r"background(?:-color)?:(#[0-9a-fA-F]{6})", S[cle]).group(1)
        rayon = re.search(r"border-radius:(\d+px)", S[cle]).group(1)
        pad = padding or re.search(r"padding:([^;]+);", S[cle]).group(1)
        return (f'<table width="100%" cellpadding="0" cellspacing="0" bgcolor="{bg}" '
                f'style="background-color:{bg};border-radius:{rayon};margin:{marge};">'
                f'<tr><td class="{cle}" style="padding:{pad};{UI_FONT}">{interieur}</td></tr></table>')

    def bloc(self, cle_fond, interieur):
        return f'<tr><td style="padding:0 16px 14px 16px;">{self.boite(cle_fond, interieur)}</td></tr>'

    def lignes_nom_valeur(self, lignes):
        """Liste « nom, variation, note » (gagnants, perdants, repères)."""
        rows = ""
        for r in lignes:
            note = f'<div {a("ui petit")}>{self.t(r["note"])}</div>' if r.get("note") else ""
            rows += (f'<tr><td {a("ui", "padding:6px 8px 6px 0;font-size:15px;color:#1d2733;vertical-align:top;")}>'
                     f'{html.escape(r["nom"])}{note}</td>'
                     f'<td {a("ui", "padding:6px 0;font-size:15px;text-align:right;white-space:nowrap;vertical-align:top;")}>'
                     f'{self.variation(r.get("variation"), r.get("neutre", False))}</td></tr>')
        return f'<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;">{rows}</table>'

    def puces(self, items, classe="texte", taille="15px"):
        li = "".join(f'<li style="margin:4px 0;">{self.t(x)}</li>' for x in liste(items))
        couleur = "color:#1d2733;" if classe == "ui" else ""
        return f'<ul {a(classe, f"margin:0 0 10px 0;padding-left:20px;font-size:{taille};{couleur}")}>{li}</ul>'

    # ---- sections ----
    def entete(self, minutes, sommaire):
        p = self.c["periode"]
        debut, fin = date.fromisoformat(p["debut"]), date.fromisoformat(p["fin"])
        du = f"{debut.day} {MOIS[debut.month - 1]}"
        au = f"{fin.day} {MOIS[fin.month - 1]} {fin.year}"
        som = " · ".join(html.escape(s) for s in sommaire)
        bandeau = (f'<div {a("ui", "font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#a9c4e4;")}>Ta semaine bourse</div>'
                   f'<div {a("ui", "font-size:28px;line-height:1.2;font-weight:700;color:#ffffff;margin:6px 0 8px 0;")}>'
                   f'Du {du} au {au}</div>'
                   f'<div {a("ui", "font-size:14px;line-height:1.55;color:#d3e2f4;")}>Lecture : environ {minutes} minutes. '
                   f'Outil d&#x27;aide à la réflexion, pas un conseil en investissement réglementé.</div>'
                   f'<div {a("ui", "font-size:13px;line-height:1.55;color:#a9c4e4;margin-top:10px;")}>{som}</div>')
        return (f'<tr><td style="padding:16px 16px 14px 16px;">'
                f'{self.boite("carte", bandeau, "0", "26px 26px 22px 26px", "#12304a")}</td></tr>')

    def resume(self):
        r = self.c["resume"]
        # Chaque morceau est construit dans l'ordre d'affichage : c'est ce qui fixe la numérotation des sources.
        inner = self.titre_section("Résumé express, 30 secondes")
        inner += f'<p {a("texte", "margin:0 0 14px 0;font-size:20px;line-height:1.4;color:#12304a;")}>{self.t(r["verdict"])}</p>'
        if r.get("points"):
            inner += self.puces(r["points"], "ui", "15px")
        pastilles = ""
        for p in r.get("pastilles", []):
            pastilles += (f'<tr><td style="padding:5px 12px 5px 0;white-space:nowrap;vertical-align:top;">'
                          f'{self.pastille(p["niveau"])}</td>'
                          f'<td {a("ui", "padding:5px 0;font-size:15px;line-height:1.45;color:#1d2733;")}>'
                          f'<strong>{html.escape(p["theme"])}.</strong> {self.t(p["texte"])}</td></tr>')
        if pastilles:
            inner += f'<table cellpadding="0" cellspacing="0" style="width:100%;">{pastilles}</table>'
        cle = r.get("chiffre_cle")
        if cle:
            inner += (f'<div {a("ui", "margin:16px 0 4px 0;")}>'
                      f'<span style="font-size:34px;font-weight:700;color:#12304a;">{html.escape(cle["valeur"])}</span> '
                      f'<span {a("ui petit")}>{self.t(cle["legende"])}</span></div>')
        rdv = ""
        for x in r.get("rdv", []):
            rdv += (f'<tr><td {a("ui", "padding:4px 14px 4px 0;font-size:14px;font-weight:700;color:#1d2733;white-space:nowrap;vertical-align:top;")}>'
                    f'{html.escape(x["quand"])}</td>'
                    f'<td {a("ui", "padding:4px 0;font-size:14px;color:#1d2733;")}>{self.t(x["quoi"])}</td></tr>')
        if rdv:
            inner += (f'<div {a("ui", "margin:14px 0 6px 0;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#5b6673;")}>'
                      f'À ne pas rater</div>'
                      f'<table cellpadding="0" cellspacing="0" style="width:100%;">{rdv}</table>')
        return self.bloc("fond_bleu", inner)

    def bilan(self):
        b = self.c["bilan"]
        inner = self.titre_section("Bilan de la semaine") + self.paragraphes(b.get("intro"))
        groupes = {}
        for r in b.get("reperes", []):
            groupes.setdefault(r.get("groupe", "Autres"), []).append(r)
        for nom, lignes in groupes.items():
            inner += self.sous_titre(nom, "14px 0 2px 0") + self.lignes_nom_valeur(lignes)
        if b.get("reperes_note"):
            inner += f'<p {a("ui petit", "margin:10px 0 0 0;")}>{self.t(b["reperes_note"])}</p>'
        if b.get("jours"):
            inner += self.sous_titre("Jour par jour", "24px 0 8px 0")
            for j in b["jours"]:
                tete = (f'<div {a("ui", "font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:#5b6673;")}>{html.escape(j["jour"])}</div>'
                        f'<div {a("ui", "font-size:16px;font-weight:700;color:#1d2733;margin:2px 0 8px 0;")}>{self.t(j["titre"])}</div>')
                chips = "".join(
                    f'<span style="display:inline-block;margin:0 16px 4px 0;color:#5b6673;">{html.escape(c["nom"])} '
                    f'{self.variation(c.get("variation"), c.get("neutre", False))}</span>' for c in j.get("chiffres", []))
                if chips:
                    tete += f'<div {a("ui", "font-size:14px;line-height:1.7;margin:0 0 8px 0;")}>{chips}</div>'
                corps = self.paragraphes(j["texte"], "15px", "0 0 6px 0")
                if j.get("faits"):
                    corps += self.puces(j["faits"], "texte", "15px")
                inner += self.boite("fond_doux", tete + corps, "0 0 10px 0", "14px 16px")
        gp = b.get("gagnants_perdants")
        if gp:
            inner += self.sous_titre("Les plus fortes hausses et baisses", "20px 0 2px 0")
            if gp.get("intro"):
                inner += self.paragraphes(gp["intro"], "14px")
            inner += (f'<div {a("ui", "font-size:12px;font-weight:700;color:#17794a;margin:10px 0 0 0;")}>HAUSSES</div>'
                      + self.lignes_nom_valeur(gp.get("gagnants", []))
                      + f'<div {a("ui", "font-size:12px;font-weight:700;color:#b3261e;margin:10px 0 0 0;")}>BAISSES</div>'
                      + self.lignes_nom_valeur(gp.get("perdants", [])))
        return self.bloc("carte", inner)

    def pourquoi_baisse(self):
        p = self.c["pourquoi_baisse"]
        inner = self.titre_section("Pourquoi ça a baissé") + self.paragraphes(p.get("intro"))
        for carte in p.get("cartes", []):
            # Ordre d'affichage : titre, sous-titre, résumé, puis les étapes.
            tete = (f'<div {a("ui", "font-size:17px;font-weight:700;color:#1d2733;")}>{html.escape(carte["titre"])} '
                    f'{self.variation(carte.get("variation"))}</div>'
                    + (f'<div {a("ui petit", "margin:2px 0 8px 0;")}>{self.t(carte["sous_titre"])}</div>' if carte.get("sous_titre") else "")
                    + self.paragraphes(carte.get("resume"), "15px"))
            etapes = ""
            for i, e in enumerate(carte.get("etapes", []), 1):
                texte = " ".join(liste(e["texte"]))
                if not MARQUEUR.search(texte) and "non établie" not in texte:
                    raise SystemExit(f"Étape de cause sans source ni « cause non établie » : {e['titre']}")
                etapes += (f'<tr><td {a("ui", "padding:8px 12px 8px 0;vertical-align:top;font-size:20px;font-weight:700;color:#1d2733;width:28px;")}>{i}</td>'
                           f'<td {a("ui", "padding:8px 0;vertical-align:top;font-size:15px;color:#1d2733;")}>'
                           f'<strong>{self.t(e["titre"])}</strong><div {a("texte", "font-size:15px;margin-top:2px;")}>{self.t(texte)}</div></td></tr>')
            corps = tete + (self.sous_titre("La chaîne de causes", "10px 0 2px 0")
                            + f'<table cellpadding="0" cellspacing="0" style="width:100%;">{etapes}</table>' if etapes else "")
            for titre, cle in (("Ce qui est établi", "etabli"), ("Ce qui reste non établi", "non_etabli"),
                               ("Les précédents", "precedent")):
                if carte.get(cle):
                    corps += self.sous_titre(titre, "10px 0 2px 0") + self.puces(carte[cle])
            if carte.get("ce_que_ca_change"):
                corps += (self.sous_titre("Ce que ça change pour toi", "10px 0 2px 0")
                          + self.paragraphes(carte["ce_que_ca_change"], "15px"))
            inner += self.boite("fond_doux", corps, "0 0 14px 0", "18px 18px")
        return self.bloc("carte", inner)

    def contexte(self):
        c = self.c["contexte"]
        inner = self.titre_section("Ce qu'il se passe en ce moment") + self.paragraphes(c.get("intro"))
        for th in c.get("themes", []):
            pastille = f'<div style="margin:0 0 6px 0;">{self.pastille(th["niveau"])}</div>' if th.get("niveau") else ""
            inner += self.boite("fond_doux",
                      f'{pastille}<div {a("ui", "font-size:16px;font-weight:700;color:#1d2733;margin:0 0 6px 0;")}>{self.t(th["titre"])}</div>'
                      f'{self.paragraphes(th["paragraphes"], "15px", "0 0 8px 0")}', "0 0 12px 0", "16px 18px")
        return self.bloc("carte", inner)

    def france(self):
        f = self.c["france"]
        inner = self.titre_section("La France")
        act = f.get("actions")
        if act:
            inner += self.sous_titre("Les actions françaises", "4px 0 6px 0") + self.paragraphes(act.get("paragraphes"), "15px")
            if act.get("hausses") or act.get("baisses"):
                inner += (f'<div {a("ui", "font-size:12px;font-weight:700;color:#17794a;margin:8px 0 0 0;")}>HAUSSES</div>'
                          + self.lignes_nom_valeur(act.get("hausses", []))
                          + f'<div {a("ui", "font-size:12px;font-weight:700;color:#b3261e;margin:10px 0 0 0;")}>BAISSES</div>'
                          + self.lignes_nom_valeur(act.get("baisses", [])))
        for cle, titre in (("politique", "La politique"), ("infos", "Les informations qui comptent")):
            bloc = f.get(cle)
            if not bloc:
                continue
            inner += self.sous_titre(titre, "22px 0 6px 0") + self.paragraphes(bloc.get("paragraphes"), "15px")
            for pt in bloc.get("points", []):
                pastille = f'<div style="margin:0 0 6px 0;">{self.pastille(pt["niveau"])}</div>' if pt.get("niveau") else ""
                inner += self.boite("fond_doux",
                          f'{pastille}<div {a("ui", "font-size:15px;font-weight:700;color:#1d2733;margin:0 0 4px 0;")}>{self.t(pt["titre"])}</div>'
                          f'{self.paragraphes(pt["texte"], "15px", "0 0 6px 0")}', "0 0 10px 0", "14px 16px")
        return self.bloc("carte", inner)

    def pour_toi(self):
        p = self.c.get("pour_toi", {})
        morceaux = []
        if p.get("statut") == "indisponible":
            morceaux.append(f'<p {a("ui petit", "margin:0 0 12px 0;")}>{self.t(p.get("diagnostic", "Ton portefeuille n\'a pas pu être lu cette semaine."))}</p>')
        else:
            if p.get("portefeuille"):
                pf = p["portefeuille"]
                morceaux.append(f'<p {a("texte", "margin:0 0 10px 0;")}>Valeur approximative : <strong>{html.escape(pf["valeur"])}</strong> '
                                f'({self.variation(pf.get("variation"))} sur la semaine).</p>')
            for titre, cle in (("Écarts à ta cible", "ecarts"), ("Alertes", "alertes")):
                if p.get(cle):
                    morceaux.append(self.sous_titre(titre, "10px 0 2px 0") + self.puces(p[cle]))
        lignes = ""
        for l in p.get("lecture", []):
            lignes += (f'<tr><td {a("ui", "padding:6px 12px 6px 0;font-size:14px;font-weight:700;color:#1d2733;vertical-align:top;width:34%;")}>{self.t(l["fait"])}</td>'
                       f'<td {a("ui", "padding:6px 0;font-size:14px;color:#1d2733;vertical-align:top;")}>{self.t(l["effet"])}</td></tr>')
        if lignes:
            morceaux.append(self.sous_titre("Ce que chaque fait change pour tes placements", "14px 0 4px 0")
                            + f'<table cellpadding="0" cellspacing="0" style="width:100%;">{lignes}</table>')
        return self.bloc("carte", self.titre_section("Pour toi") + "".join(morceaux))

    def _liste_agenda(self, titre, lignes, colonnes, vide):
        if not lignes:
            return self.sous_titre(titre, "16px 0 4px 0") + f'<p {a("ui petit", "margin:0;")}>{self.t(vide)}</p>'
        rows = ""
        for l in lignes:
            cases = "".join(
                f'<td {a("ui", "padding:6px 12px 6px 0;font-size:14px;vertical-align:top;" + st)}>{self.t(l.get(k, ""))}</td>'
                for k, st in colonnes)
            rows += f"<tr>{cases}</tr>"
        return (self.sous_titre(titre, "16px 0 4px 0")
                + f'<table cellpadding="0" cellspacing="0" style="width:100%;">{rows}</table>')

    def agenda(self):
        ag = self.c.get("agenda", {})
        fort = "font-weight:700;color:#1d2733;width:26%;"
        inner = self.titre_section("La semaine qui vient")
        inner += self._liste_agenda("Banques centrales, inflation, emploi, politique", ag.get("macro", []),
                                    [("quand", fort), ("quoi", "color:#1d2733;")], "Rien de majeur au calendrier.")
        inner += self._liste_agenda("Résultats d'entreprises : tes ETF", ag.get("resultats_etf", []),
                                    [("quand", fort), ("entreprise", "font-weight:700;color:#1d2733;"), ("a_regarder", "color:#1d2733;")],
                                    ag.get("resultats_etf_vide", "Aucune grosse ligne de tes ETF ne publie cette semaine."))
        inner += self._liste_agenda("Résultats d'entreprises : les plus suivis du marché", ag.get("resultats_marche", []),
                                    [("quand", fort), ("entreprise", "font-weight:700;color:#1d2733;"), ("a_regarder", "color:#1d2733;")],
                                    "Pas de publication majeure repérée.")
        if ag.get("note"):
            inner += f'<p {a("ui petit", "margin:12px 0 0 0;")}>{self.t(ag["note"])}</p>'
        return self.bloc("carte", inner)

    def notion(self):
        n = self.c.get("notion")
        if not n:
            return ""
        inner = (self.titre_section("Une notion en 3 lignes")
                 + f'<div {a("ui", "font-size:16px;font-weight:700;color:#1d2733;margin:0 0 6px 0;")}>{self.t(n["titre"])}</div>'
                 + f'<div {a("texte", "font-size:15px;")}>{self.t(n["texte"])}</div>')
        return self.bloc("fond_doux", inner)

    def limites(self):
        lim = self.c.get("limites", [])
        if not lim:
            return ""
        inner = self.titre_section("Limites de cette édition") + self.puces(lim, "ui petit", "13px")
        return self.bloc("fond_doux", inner)

    def pied(self):
        return (f'<tr><td {a("ui petit", "padding:6px 24px 28px 24px;")}>'
                f'Outil d\'aide à la réflexion, pas un conseil en investissement réglementé.</td></tr>')

    # ---- assemblage ----
    def construire(self):
        sections = [("Résumé", "resume", self.resume), ("Bilan", "bilan", self.bilan),
                    ("Pourquoi ça a baissé", "pourquoi_baisse", self.pourquoi_baisse),
                    ("En ce moment", "contexte", self.contexte), ("France", "france", self.france),
                    ("Pour toi", "pour_toi", self.pour_toi), ("Semaine qui vient", "agenda", self.agenda),
                    ("Notion", "notion", self.notion), ("Limites", "limites", self.limites)]
        # Rendu dans l'ordre de lecture : c'est lui qui fixe la numérotation des sources.
        rendus = [(nom, f()) for nom, cle, f in sections if cle in self.c]
        corps = "".join(r for _, r in rendus)
        mots = len(re.sub(r"<[^>]+>", " ", corps).split())
        minutes = max(1, math.ceil(mots / MOTS_PAR_MINUTE))
        corps = self.entete(minutes, [n for n, r in rendus if r]) + corps
        for cle in self.sources:
            if cle not in self.ordre:
                raise SystemExit(f"Source déclarée mais jamais citée : {cle}")
        items = ""
        for cle in self.ordre:
            s = self.sources[cle]
            d = f" ({html.escape(s['date'])})" if s.get("date") else ""
            items += (f'<li style="margin:4px 0;"><a href="{html.escape(s["url"], quote=True)}" '
                      f'style="color:#12304a;">{html.escape(s["nom"])}</a>{d}</li>')
        sources = self.bloc("carte", self.titre_section("Sources, dans l'ordre de lecture")
                            + f'<ol {a("ui petit", "margin:0;padding-left:22px;")}>{items}</ol>')
        self.minutes, self.mots = minutes, mots
        return corps, sources + self.pied()

    def page(self):
        corps, bas = self.construire()
        controler(corps)
        return (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<meta name="color-scheme" content="only light"><meta name="supported-color-schemes" content="light">'
                f'<title>Ta semaine bourse</title><style>@media (max-width:480px){{.carte,.fond_bleu{{padding:20px 16px !important;}}}}</style></head>'
                f'<body class="page" bgcolor="#eef1f5" style="{S["page"]}">'
                f'<table width="100%" cellpadding="0" cellspacing="0" bgcolor="#eef1f5" style="{S["page"]}"><tr><td align="center">'
                f'<table width="100%" cellpadding="0" cellspacing="0" style="{S["cadre"]}">'
                f'{corps}{bas}</table></td></tr></table></body></html>')


def controler(corps):
    """Refuse un corps qui contient un tiret long, un emoji ou une adresse web."""
    texte = re.sub(r"<[^>]+>", " ", corps)
    problemes = []
    if chr(8212) in texte or chr(8211) in texte:
        problemes.append("tiret long")
    if EMOJI.search(texte):
        problemes.append("emoji")
    if re.search(r"https?://|www\.", texte):
        problemes.append("adresse web dans le corps (mets-la dans sources)")
    if "href=" in corps:
        problemes.append("lien dans le corps")
    if problemes:
        raise SystemExit("Contrôle refusé : " + ", ".join(problemes))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("contenu", help="fichier JSON de l'édition")
    ap.add_argument("--sortie", help="fichier HTML à écrire (défaut : même nom en .html)")
    args = ap.parse_args()
    contenu = json.loads(Path(args.contenu).read_text(encoding="utf-8"))
    rendu = Rendu(contenu)
    page = rendu.page()
    sortie = Path(args.sortie) if args.sortie else Path(args.contenu).with_suffix(".html")
    sortie.write_text(page, encoding="utf-8")
    print(f"{sortie} écrit : {len(rendu.ordre)} sources, {rendu.mots} mots, lecture {rendu.minutes} minutes, "
          f"{len(page) // 1024} Ko.")


if __name__ == "__main__":
    main()
