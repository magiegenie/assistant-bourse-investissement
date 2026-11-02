"""Contrôle qualité du dépôt : tirets longs, chemins cités qui n'existent pas, fiches citées inconnues.

Usage : python scripts/controle_depot.py
Code de retour 1 si un problème est trouvé. Lancé par les tests.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
IGNORES = {".git", "externe", "prive", "node_modules", "__pycache__", ".venv"}
EXCLUS = ("docs/externe/", "docs/recherche/", "docs/veille/")  # textes importés ou générés
TEXTES = {".md", ".py", ".csv", ".yml", ".json"}
TIRETS = (chr(0x2014), chr(0x2013))
# Chemins relatifs cités entre accents graves, à partir des dossiers connus du dépôt.
CHEMIN = re.compile(r"`((?:scripts|connaissances|templates|docs|donnees|mcp|tests|\.claude)/[^`\s<>*]+?)`")


def fichiers():
    for p in RACINE.rglob("*"):
        rel = p.relative_to(RACINE).as_posix()
        if p.is_file() and p.suffix in TEXTES and not set(p.relative_to(RACINE).parts) & IGNORES \
                and not rel.startswith(EXCLUS):
            yield p, rel


def problemes():
    sortie = []
    for p, rel in fichiers():
        texte = p.read_text(encoding="utf-8", errors="replace")
        for n, ligne in enumerate(texte.splitlines(), start=1):
            if any(t in ligne for t in TIRETS):
                sortie.append(f"{rel}:{n} tiret long ou demi-cadratin")
            for c in CHEMIN.findall(ligne):
                c = c.rstrip(".,;:)")
                if "<" in c or "*" in c or "AAAA" in c:
                    continue
                if not (RACINE / c).exists():
                    sortie.append(f"{rel}:{n} chemin introuvable : {c}")
    return sortie


def main():
    liste = problemes()
    for l in liste:
        print(l)
    print(f"{len(liste)} problème(s).")
    sys.exit(1 if liste else 0)


if __name__ == "__main__":
    main()
