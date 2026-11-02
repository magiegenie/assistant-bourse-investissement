"""Fabrique l'email HTML de la newsletter du dimanche à partir d'un fichier JSON de contenu.

Usage : python scripts/newsletter_html.py edition.json [--sortie edition.html]

Le JSON décrit le contenu (voir templates/newsletter-modele.md). Ce script s'occupe de la mise en forme et
garantit trois règles de lecture :
  - aucun lien dans le corps : les textes citent une source avec [[src:cle]] et le script la transforme
    en [1], [2]... numérotés dans l'ordre où la lecture les rencontre ;
  - tous les liens sont réunis dans le bloc « Sources » en bas, dans cet ordre ;
  - le contrôle final refuse les tirets longs, les emojis, les adresses web dans le corps et toute source
    citée sans être déclarée (ou déclarée sans être citée).

Bibliothèque standard uniquement. Données publiques seulement : aucun montant réel ne doit être écrit dans le dépôt.
"""
import argparse
import html
import json
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
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre",
        "novembre", "décembre"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
MARQUEUR = re.compile(r"\[\[src:([a-z0-9_\-]+)\]\]")
GRAS = re.compile(r"\*\*(.+?)\*\*")

# Styles en ligne (les clients mail ignorent souvent les feuilles de style), doublés d'une feuille de style
# pour le mode sombre.
S = {
    "page": "margin:0;padding:0;background:#f1f3f5;",
    "cadre": "max-width:640px;width:100%;margin:0 auto;table-layout:fixed;",
    "texte": "font-family:Georgia,'Times New Roman',serif;font-size:16px;line-height:1.55;color:#1d2733;",
    "ui": "font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;",
    "carte": "background:#ffffff;border-radius:14px;padding:22px 24px;",
    "fond_doux": "background:#eef2f6;border-radius:14px;padding:22px 24px;",
    "h2": "margin:0 0 14px 0;font-size:13px;letter-spacing:.09em;text-transform:uppercase;color:#12304a;",
    "petit": "font-size:13px;line-height:1.5;color:#5b6673;",
    "pos": "color:#17794a;",
    "neg": "color:#b3261e;",
}


def a(cls, extra=""):
    """Attributs class + style en ligne pour les clés de S (plusieurs clés séparées par des espaces)."""
    style = "".join(S[c] for c in cls.split()) + extra
    return f'class="{cls}" style="{style}"'


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

    def pastille(self, niveau):
        nom, couleur, fond = NIVEAUX[niveau]
        return (f'<span style="{S["ui"]}display:inline-block;padding:3px 10px;border-radius:999px;font-size:12px;'
                f'font-weight:600;color:{couleur};background:{fond};">{nom}</span>')

    def variation(self, v):
        if v in (None, ""):
            return f'<span style="{S["ui"]}color:#8a94a0;">non disponible</span>'
        cls = "neg" if str(v).strip().startswith(("-", "−")) else "pos"
        return f'<span style="{S["ui"]}font-weight:600;{S[cls]}">{html.escape(str(v))}</span>'

    # ---- sections ----
    def titre_section(self, texte):
        return f'<h2 {a("h2 ui")}>{html.escape(texte)}</h2>'

    def bloc(self, cle_fond, interieur):
        return (f'<tr><td style="padding:0 16px 14px 16px;"><div {a(cle_fond)}>{interieur}</div></td></tr>')

    def entete(self):
        c = self.c
        p = c["periode"]
        debut, fin = date.fromisoformat(p["debut"]), date.fromisoformat(p["fin"])
        du = f"{debut.day} {MOIS[debut.month - 1]}"
        au = f"{fin.day} {MOIS[fin.month - 1]} {fin.year}"
        return (f'<tr><td style="padding:26px 24px 16px 24px;">'
                f'<div {a("ui", "font-size:13px;color:#5b6673;")}>Ta semaine bourse</div>'
                f'<div {a("ui", "font-size:26px;line-height:1.2;font-weight:700;color:#12304a;margin:4px 0 6px 0;")}>'
                f'Du {du} au {au}</div>'
                f'<div {a("ui petit")}>Lecture : {int(c.get("lecture_min", 4))} minutes. '
                f'Outil d\'aide à la réflexion, pas un conseil en investissement réglementé.</div>'
                f'</td></tr>')

    def vue_ensemble(self):
        c = self.c
        pastilles = ""
        for p in c.get("pastilles", []):
            pastilles += (f'<tr><td style="padding:5px 12px 5px 0;white-space:nowrap;vertical-align:top;">'
                          f'{self.pastille(p["niveau"])}</td>'
                          f'<td {a("ui", "padding:5px 0;font-size:15px;line-height:1.45;color:#1d2733;")}>'
                          f'<strong>{html.escape(p["theme"])}.</strong> {self.t(p["texte"])}</td></tr>')
        cle = c.get("chiffre_cle")
        bloc_cle = ""
        if cle:
            bloc_cle = (f'<div {a("ui", "margin:16px 0 4px 0;")}>'
                        f'<span style="font-size:34px;font-weight:700;color:#12304a;">{html.escape(cle["valeur"])}</span> '
                        f'<span {a("ui petit")}>{self.t(cle["legende"])}</span></div>')
        rdv = ""
        for r in c.get("rdv", []):
            rdv += (f'<tr><td {a("ui", "padding:4px 14px 4px 0;font-size:14px;font-weight:700;color:#12304a;white-space:nowrap;vertical-align:top;")}>'
                    f'{html.escape(r["quand"])}</td>'
                    f'<td {a("ui", "padding:4px 0;font-size:14px;color:#1d2733;")}>{self.t(r["quoi"])}</td></tr>')
        inner = (self.titre_section("Vue d'ensemble")
                 + f'<p {a("texte", "margin:0 0 14px 0;font-size:20px;line-height:1.4;color:#12304a;")}>'
                   f'{self.t(c["verdict"])}</p>'
                 + (f'<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;">{pastilles}</table>' if pastilles else "")
                 + bloc_cle
                 + (f'<div {a("ui", "margin:14px 0 6px 0;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#5b6673;")}>'
                    f'À ne pas rater</div>'
                    f'<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;">{rdv}</table>' if rdv else ""))
        return self.bloc("fond_doux", inner)

    def marches(self):
        lignes = ""
        for r in self.c.get("reperes", []):
            note = f' <span {a("ui petit")}>{self.t(r["note"])}</span>' if r.get("note") else ""
            lignes += (f'<tr><td {a("ui", "padding:7px 8px 7px 0;font-size:15px;color:#1d2733;")}>{html.escape(r["nom"])}{note}</td>'
                       f'<td {a("ui", "padding:7px 8px;font-size:15px;text-align:right;color:#1d2733;")}>{html.escape(str(r.get("valeur") or ""))}</td>'
                       f'<td {a("ui", "padding:7px 0 7px 8px;font-size:15px;text-align:right;white-space:nowrap;")}>'
                       f'{self.variation(r.get("variation"))}</td></tr>')
        pied = ""
        if self.c.get("reperes_note"):
            pied = f'<p {a("ui petit", "margin:10px 0 0 0;")}>{self.t(self.c["reperes_note"])}</p>'
        inner = (self.titre_section("Les marchés cette semaine")
                 + f'<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;">{lignes}</table>'
                 + pied)
        return self.bloc("carte", inner)

    def faits(self):
        cartes = ""
        for f in self.c.get("faits", []):
            cartes += (f'<div {a("fond_doux", "margin:0 0 12px 0;padding:16px 18px;")}>'
                       f'<div style="margin:0 0 8px 0;">{self.pastille(f["niveau"])}</div>'
                       f'<div {a("ui", "font-size:16px;font-weight:700;color:#12304a;margin:0 0 6px 0;")}>{self.t(f["titre"])}</div>'
                       f'<div {a("texte", "font-size:15px;")}>{self.t(f["texte"])}</div>'
                       f'<div {a("texte", "font-size:15px;margin-top:6px;")}><strong>Pourquoi ça compte.</strong> {self.t(f["pourquoi"])}</div>'
                       f'</div>')
        return self.bloc("carte", self.titre_section("Ce qui s'est passé") + cartes)

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
                    li = "".join(f'<li style="margin:3px 0;">{self.t(x)}</li>' for x in p[cle])
                    morceaux.append(f'<div {a("ui", "font-size:13px;font-weight:700;color:#12304a;margin:10px 0 2px 0;")}>{titre}</div>'
                                    f'<ul {a("texte", "margin:0;padding-left:20px;font-size:15px;")}>{li}</ul>')
        lignes = ""
        for l in p.get("lecture", []):
            lignes += (f'<tr><td {a("ui", "padding:6px 12px 6px 0;font-size:14px;font-weight:700;color:#12304a;vertical-align:top;width:34%;")}>{self.t(l["fait"])}</td>'
                       f'<td {a("ui", "padding:6px 0;font-size:14px;color:#1d2733;vertical-align:top;")}>{self.t(l["effet"])}</td></tr>')
        if lignes:
            morceaux.append(f'<div {a("ui", "font-size:13px;font-weight:700;color:#12304a;margin:14px 0 4px 0;")}>Ce que chaque fait change pour tes placements</div>'
                            f'<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;">{lignes}</table>')
        return self.bloc("carte", self.titre_section("Pour toi") + "".join(morceaux))

    def _liste_agenda(self, titre, lignes, colonnes, vide):
        if not lignes:
            return (f'<div {a("ui", "font-size:13px;font-weight:700;color:#12304a;margin:16px 0 4px 0;")}>{titre}</div>'
                    f'<p {a("ui petit", "margin:0;")}>{self.t(vide)}</p>')
        rows = ""
        for l in lignes:
            cases = "".join(
                f'<td {a("ui", "padding:6px 12px 6px 0;font-size:14px;vertical-align:top;" + st)}>{self.t(l.get(k, ""))}</td>'
                for k, st in colonnes)
            rows += f"<tr>{cases}</tr>"
        return (f'<div {a("ui", "font-size:13px;font-weight:700;color:#12304a;margin:16px 0 4px 0;")}>{titre}</div>'
                f'<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;">{rows}</table>')

    def agenda(self):
        ag = self.c.get("agenda", {})
        fort = "font-weight:700;color:#12304a;width:26%;"
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
                 + f'<div {a("ui", "font-size:16px;font-weight:700;color:#12304a;margin:0 0 6px 0;")}>{self.t(n["titre"])}</div>'
                 + f'<div {a("texte", "font-size:15px;")}>{self.t(n["texte"])}</div>')
        return self.bloc("fond_doux", inner)

    def veille(self):
        lignes = self.c.get("veille", [])
        if not lignes:
            return ""
        entetes = ["Semaine", "Thème", "Importance", "Fait", "Source et date", "Positions concernées", "Impact estimé", "Action"]
        th = "".join(f'<th {a("ui", "text-align:left;padding:6px 8px 6px 0;font-size:11px;color:#5b6673;white-space:nowrap;")}>{e}</th>' for e in entetes)
        trs = ""
        for l in lignes:
            tds = "".join(f'<td {a("ui", "padding:6px 8px 6px 0;font-size:12px;vertical-align:top;color:#1d2733;")}>{self.t(x)}</td>' for x in l)
            trs += f"<tr>{tds}</tr>"
        inner = (self.titre_section("À recopier dans la feuille Veille")
                 + f'<div style="overflow-x:auto;"><table cellpadding="0" cellspacing="0" style="border-collapse:collapse;min-width:100%;">'
                   f'<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
        return self.bloc("carte", inner)

    def limites(self):
        lim = self.c.get("limites", [])
        if not lim:
            return ""
        li = "".join(f'<li style="margin:3px 0;">{self.t(x)}</li>' for x in lim)
        inner = (self.titre_section("Limites de cette édition")
                 + f'<ul {a("ui petit", "margin:0;padding-left:20px;")}>{li}</ul>')
        return self.bloc("fond_doux", inner)

    def pied(self):
        return (f'<tr><td {a("ui petit", "padding:6px 24px 28px 24px;")}>'
                f'Outil d\'aide à la réflexion, pas un conseil en investissement réglementé.</td></tr>')

    # ---- assemblage ----
    def construire(self):
        corps = "".join([self.entete(), self.vue_ensemble(), self.marches(), self.faits(), self.pour_toi(),
                         self.agenda(), self.notion(), self.veille(), self.limites()])
        # Les sources sont numérotées d'après ce qui a été lu, donc rendues en dernier.
        for cle in self.sources:
            if cle not in self.ordre:
                raise SystemExit(f"Source déclarée mais jamais citée : {cle}")
        items = ""
        for i, cle in enumerate(self.ordre, 1):
            s = self.sources[cle]
            d = f" ({html.escape(s['date'])})" if s.get("date") else ""
            items += (f'<li style="margin:4px 0;"><a href="{html.escape(s["url"], quote=True)}" '
                      f'style="color:#12304a;">{html.escape(s["nom"])}</a>{d}</li>')
        sources = self.bloc("carte",
                            self.titre_section("Sources, dans l'ordre de lecture")
                            + f'<ol {a("ui petit", "margin:0;padding-left:22px;")}>{items}</ol>')
        return corps, sources + self.pied()

    def page(self):
        corps, bas = self.construire()
        controler(corps)
        sombre = """
@media (prefers-color-scheme: dark) {
  body, .page { background:#10161d !important; }
  .carte { background:#18212b !important; }
  .fond_doux { background:#1f2a36 !important; }
  .texte, .ui { color:#e6ebf0 !important; }
  .h2 { color:#9cc3e6 !important; }
  .petit { color:#a3afbb !important; }
  strong { color:#ffffff; }
  [style*="#12304a"] { color:#9cc3e6 !important; }
  [style*="#1d2733"] { color:#e6ebf0 !important; }
  [style*="#5b6673"] { color:#a3afbb !important; }
}
@media (max-width: 480px) { .carte, .fond_doux { padding:18px 16px !important; } }
"""
        return (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<meta name="color-scheme" content="light dark"><meta name="supported-color-schemes" content="light dark">'
                f'<title>Ta semaine bourse</title><style>{sombre}</style></head>'
                f'<body class="page" style="{S["page"]}">'
                f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="{S["page"]}"><tr><td align="center">'
                f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="{S["cadre"]}">'
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
    print(f"{sortie} écrit : {len(rendu.ordre)} sources, {len(page) // 1024} Ko.")


if __name__ == "__main__":
    main()
