"""Installe les serveurs MCP des agents et génère .mcp.json pour cet ordinateur.

Usage : python scripts/installer_mcp.py [--ecrire-seulement]
  (sans option)        crée les environnements Python manquants dans externe/, installe les paquets, écrit .mcp.json
  --ecrire-seulement   ne touche pas aux installations, régénère seulement .mcp.json

Les serveurs sont décrits dans mcp/serveurs.json. Rien n'est lancé : on installe et on déclare.
Idempotent : un environnement déjà présent n'est pas recréé. Redémarrer Claude Code ensuite.
Le dossier externe/ et .mcp.json ne sont pas versionnés (chemins propres à l'ordinateur).
"""
import json
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BIN = "Scripts" if sys.platform.startswith("win") else "bin"
EXT = ".exe" if sys.platform.startswith("win") else ""


def lancer(cmd, **kw):
    print("  >", " ".join(str(c) for c in cmd))
    subprocess.run([str(c) for c in cmd], check=True, **kw)


def installer(nom, s):
    venv = RACINE / s["venv"]
    exe = venv / BIN / (s["executable"] + EXT)
    if exe.exists():
        print(f"[{nom}] déjà installé")
        return
    print(f"[{nom}] installation")
    if "source_git" in s:
        dossier = RACINE / s["dossier"]
        if not dossier.exists():
            lancer(["git", "clone", s["source_git"], dossier])
        lancer(["git", "-C", dossier, "checkout", s["commit"]])
    venv.parent.mkdir(parents=True, exist_ok=True)
    lancer([sys.executable, "-m", "venv", venv])
    py = venv / BIN / ("python" + EXT)
    if "source_git" in s:
        lancer([py, "-m", "pip", "install", "-q", "-e", RACINE / s["dossier"]])
        lancer([py, "-m", "pip", "install", "-q", "mcp<2"])
    else:
        lancer([py, "-m", "pip", "install", "-q", s["paquet_pypi"]])
        if nom == "actualite-flux":
            lancer([py, "-m", "pip", "install", "-q", "mcp<2"])


def ecrire_mcp_json(serveurs):
    conf = {"mcpServers": {}}
    for nom, s in serveurs.items():
        exe = RACINE / s["venv"] / BIN / (s["executable"] + EXT)
        if not exe.exists():
            print(f"[{nom}] absent, non déclaré (relancer sans --ecrire-seulement)")
            continue
        conf["mcpServers"][nom] = {"command": exe.as_posix(), "args": s["args"]}
    (RACINE / ".mcp.json").write_text(json.dumps(conf, indent=2), encoding="utf-8")
    print(f".mcp.json écrit : {', '.join(conf['mcpServers']) or 'aucun serveur'}")


if __name__ == "__main__":
    serveurs = json.loads((RACINE / "mcp" / "serveurs.json").read_text(encoding="utf-8"))["serveurs"]
    if "--ecrire-seulement" not in sys.argv:
        for nom, s in serveurs.items():
            installer(nom, s)
    ecrire_mcp_json(serveurs)
    print("Redémarre Claude Code pour que les serveurs apparaissent.")
