"""Fabrique le PDF du guide à partir de docs/GUIDE.md : python scripts/generer_guide.py

Aucune dépendance à installer : le texte est converti en HTML par ce script, puis imprimé en PDF
par Microsoft Edge ou Google Chrome (déjà présents sur l'ordinateur) en mode sans fenêtre.
Le HTML intermédiaire est écrit à côté du PDF puis supprimé (option --garder-html pour le conserver).
"""
import html
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / "docs" / "GUIDE.md"
SORTIE = RACINE / "docs" / "Guide-assistant-bourse-investissement.pdf"

NAVIGATEURS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]

CSS = """
@page { size: A4; margin: 20mm 18mm 22mm 18mm;
        @bottom-center { content: counter(page); font: 9pt 'Segoe UI', Arial, sans-serif; color: #7a8590; } }
@page cover { margin: 0; @bottom-center { content: none; } }
:root { --encre: #16212b; --bleu: #1f3a5f; --gris: #5b6770; --fond: #f3f6fa; --accent: #d9822b; --clair: #e7edf4; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.55 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; color: var(--encre); margin: 0; }
.couverture { page: cover; height: 296mm; overflow: hidden; padding: 38mm 24mm 24mm; background: var(--bleu); color: #fff; page-break-after: always;
              display: flex; flex-direction: column; justify-content: space-between; }
.couverture .etiquette { font-size: 11pt; letter-spacing: .18em; text-transform: uppercase; color: #f2b36d; }
.couverture h1 { font-size: 40pt; line-height: 1.08; margin: 10mm 0 6mm; font-weight: 700; border: 0; padding: 0; color: #fff; }
.couverture .sous { font-size: 16pt; color: #cfdced; max-width: 125mm; }
.couverture .pied { font-size: 10.5pt; color: #cfdced; }
.couverture .pied b { color: #fff; }
.sommaire { page-break-after: always; }
.sommaire h2 { font-size: 22pt; color: var(--bleu); margin: 0 0 8mm; }
.sommaire ol { list-style: none; margin: 0; padding: 0; }
.sommaire li { padding: 2.6mm 4mm; margin-bottom: 1.4mm; background: var(--fond); border-radius: 3px; }
.sommaire a { color: var(--encre); text-decoration: none; font-weight: 600; }
.sommaire .num { display: inline-block; width: 9mm; color: var(--accent); font-weight: 700; }
h1 { font-size: 24pt; color: var(--bleu); margin: 0 0 6mm; padding: 0; page-break-before: always; line-height: 1.15; }
h1 .n { color: var(--accent); }
h2 { font-size: 14.5pt; color: var(--bleu); margin: 8mm 0 3mm; page-break-after: avoid; }
h3 { font-size: 11.5pt; color: var(--encre); margin: 5mm 0 2mm; page-break-after: avoid; }
p { margin: 0 0 3mm; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; }
li { margin-bottom: 1.2mm; }
strong { color: var(--encre); }
code { font: 9pt Consolas, 'Courier New', monospace; background: var(--clair); padding: .3mm 1.2mm; border-radius: 2px; color: #1b3556; }
pre { font: 9pt/1.45 Consolas, 'Courier New', monospace; background: #17212c; color: #e8eef5; padding: 4mm; border-radius: 4px;
      margin: 0 0 4mm; white-space: pre-wrap; page-break-inside: avoid; }
pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
table { width: 100%; border-collapse: collapse; margin: 0 0 4mm; font-size: 9.5pt; page-break-inside: auto; }
thead th { background: var(--bleu); color: #fff; text-align: left; padding: 2mm 2.6mm; font-weight: 600; }
tbody td { padding: 2mm 2.6mm; vertical-align: top; }
tbody tr:nth-child(even) td { background: var(--fond); }
tr { page-break-inside: avoid; }
blockquote { margin: 0 0 4mm; padding: 3.5mm 5mm; background: #fdf3e6; border-left: 3mm solid var(--accent); border-radius: 3px; page-break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }
"""


def lire_source():
    texte = SOURCE.read_text(encoding="utf-8")
    meta = {}
    m = re.match(r"---\n(.*?)\n---\n", texte, re.S)
    if m:
        for ligne in m.group(1).splitlines():
            cle, _, val = ligne.partition(":")
            meta[cle.strip()] = val.strip()
        texte = texte[m.end():]
    return meta, texte


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", t)
    return t


def cellules(ligne):
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def convertir(texte):
    lignes = texte.splitlines()
    out, titres = [], []
    i = 0
    while i < len(lignes):
        l = lignes[i]
        if l.startswith("```"):
            bloc = []
            i += 1
            while i < len(lignes) and not lignes[i].startswith("```"):
                bloc.append(lignes[i])
                i += 1
            i += 1
            out.append("<pre><code>" + html.escape("\n".join(bloc)) + "</code></pre>")
            continue
        if l.startswith("# "):
            titre = l[2:].strip()
            m = re.match(r"(\d+)\.\s+(.*)", titre)
            num, nom = (m.group(1), m.group(2)) if m else ("", titre)
            ancre = f"ch{num or len(titres) + 1}"
            titres.append((num, nom, ancre))
            n = f'<span class="n">{num}.</span> ' if num else ""
            out.append(f'<h1 id="{ancre}">{n}{inline(nom)}</h1>')
            i += 1
            continue
        if l.startswith("## "):
            out.append(f"<h2>{inline(l[3:].strip())}</h2>")
            i += 1
            continue
        if l.startswith("### "):
            out.append(f"<h3>{inline(l[4:].strip())}</h3>")
            i += 1
            continue
        if l.startswith("|") and i + 1 < len(lignes) and re.match(r"^\|[\s:\-|]+\|$", lignes[i + 1].strip()):
            tete = cellules(l)
            i += 2
            corps = []
            while i < len(lignes) and lignes[i].startswith("|"):
                corps.append(cellules(lignes[i]))
                i += 1
            h = "".join(f"<th>{inline(c)}</th>" for c in tete)
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in corps)
            out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")
            continue
        if l.startswith(">"):
            paras, cur = [], []
            while i < len(lignes) and lignes[i].startswith(">"):
                contenu = lignes[i][1:].strip()
                if contenu:
                    cur.append(contenu)
                elif cur:
                    paras.append(" ".join(cur))
                    cur = []
                i += 1
            if cur:
                paras.append(" ".join(cur))
            out.append("<blockquote>" + "".join(f"<p>{inline(p)}</p>" for p in paras) + "</blockquote>")
            continue
        m = re.match(r"^(\s*)(-|\d+\.)\s+(.*)", l)
        if m:
            ordonnee = m.group(2) != "-"
            items = []
            debut = int(m.group(2)[:-1]) if ordonnee else 1
            while i < len(lignes):
                mm = re.match(r"^(\s*)(-|\d+\.)\s+(.*)", lignes[i])
                if mm and (mm.group(2) != "-") == ordonnee:
                    items.append(mm.group(3))
                    i += 1
                    continue
                if lignes[i].startswith("   ") and items and lignes[i].strip() == "":
                    i += 1
                    continue
                break
            tag = "ol" if ordonnee else "ul"
            attr = f' start="{debut}"' if ordonnee and debut != 1 else ""
            out.append(f"<{tag}{attr}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        if not l.strip():
            i += 1
            continue
        para = [l.strip()]
        i += 1
        while i < len(lignes) and lignes[i].strip() and not re.match(r"^(#|\||>|```|\s*(-|\d+\.)\s)", lignes[i]):
            para.append(lignes[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out), titres


def date_fr(iso):
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
            "septembre", "octobre", "novembre", "décembre"]
    try:
        d = date.fromisoformat(iso)
    except ValueError:
        return iso
    return f"{d.day}{'er' if d.day == 1 else ''} {mois[d.month - 1]} {d.year}"


def construire_html(meta, corps, titres):
    sommaire = "".join(
        f'<li><a href="#{a}"><span class="num">{n}</span>{html.escape(t)}</a></li>' for n, t, a in titres
    )
    couv = f"""
<section class="couverture">
  <div class="etiquette">Assistant Bourse Investissement</div>
  <div>
    <h1>{html.escape(meta.get('titre', 'Guide'))}</h1>
    <div class="sous">Comment utiliser et bien utiliser ton assistant : l'équipe, la veille, l'analyse, le budget, la stratégie, le coach.</div>
  </div>
  <div class="pied">Version <b>{html.escape(meta.get('version', '?'))}</b> &nbsp;·&nbsp; mis à jour le <b>{date_fr(meta.get('date', ''))}</b><br>
  Outil d'aide à la réflexion, pas un conseil en investissement réglementé.</div>
</section>"""
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>{html.escape(meta.get('titre', 'Guide'))} : {html.escape(meta.get('sous_titre', ''))}</title>
<style>{CSS}</style></head><body>
{couv}
<section class="sommaire"><h2>Sommaire</h2><ol>{sommaire}</ol></section>
{corps}
</body></html>"""


def trouver_navigateur():
    for chemin in NAVIGATEURS:
        if Path(chemin).exists():
            return chemin
    for nom in ("msedge", "chrome", "google-chrome", "chromium"):
        trouve = shutil.which(nom)
        if trouve:
            return trouve
    return None


def main():
    garder = "--garder-html" in sys.argv
    meta, texte = lire_source()
    corps, titres = convertir(texte)
    page = construire_html(meta, corps, titres)
    nav = trouver_navigateur()
    if not nav:
        sys.exit("Aucun navigateur (Edge ou Chrome) trouvé : impossible de fabriquer le PDF.")
    with tempfile.TemporaryDirectory() as tmp:
        fichier_html = Path(tmp) / "guide.html"
        fichier_html.write_text(page, encoding="utf-8")
        if garder:
            shutil.copy(fichier_html, SORTIE.with_suffix(".html"))
        SORTIE.parent.mkdir(exist_ok=True)
        cmd = [nav, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
               f"--user-data-dir={Path(tmp) / 'profil'}", f"--print-to-pdf={SORTIE}", fichier_html.as_uri()]
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
    if not SORTIE.exists() or SORTIE.stat().st_size < 1000:
        sys.exit("Le PDF n'a pas été créé.")
    print(f"PDF créé : {SORTIE.relative_to(RACINE)} ({SORTIE.stat().st_size // 1024} Ko), version {meta.get('version')}")


if __name__ == "__main__":
    main()
