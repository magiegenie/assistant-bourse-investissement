"""Tests de la collecte hebdomadaire et du contrôle qualité, sans réseau (flux locaux)."""
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

import collecte_hebdo  # noqa: E402
import controle_depot  # noqa: E402
import verifier_sources  # noqa: E402

FLUX = RACINE / "tests" / "donnees"
SOURCES = [
    {"nom": "Flux RSS test", "famille": "banque centrale", "url_flux": "rss"},
    {"nom": "Chaîne test", "famille": "pedagogie video", "url_flux": "atom"},
    {"nom": "Flux cassé", "famille": "presse", "url_flux": "casse"},
]


def faux_telechargement(url):
    if url == "casse":
        raise OSError("réseau")
    return (FLUX / f"flux-{url}.xml").read_bytes()


class Collecte(unittest.TestCase):
    def test_rss_et_atom(self):
        self.assertEqual(len(collecte_hebdo.articles(faux_telechargement("rss"))), 3)
        d, titre, lien = collecte_hebdo.articles(faux_telechargement("atom"))[0]
        self.assertEqual((d, titre, lien), (date(2026, 10, 27), "Comprendre les ETF", "https://exemple.test/v"))

    def test_semaine_doublons_erreurs(self):
        retenus, erreurs = collecte_hebdo.collecter(SOURCES, date(2026, 10, 24), date(2026, 10, 30),
                                                    faux_telechargement)
        self.assertEqual(len(retenus["banque centrale"]), 1)  # doublon et ancien article écartés
        self.assertEqual(len(retenus["pedagogie video"]), 1)
        self.assertEqual(erreurs, [("Flux cassé", "OSError")])
        with tempfile.TemporaryDirectory() as d:
            chemin, total = collecte_hebdo.ecrire(retenus, erreurs, date(2026, 10, 24), date(2026, 10, 30), d)
            texte = chemin.read_text(encoding="utf-8")
        self.assertEqual(chemin.name, "2026-S44.md")
        self.assertEqual(total, 2)
        self.assertIn("La BCE maintient ses taux", texte)
        self.assertIn("Flux en échec", texte)

    def test_catalogue_lisible(self):
        sources = collecte_hebdo.lire_sources()
        self.assertGreater(len(sources), 5)
        for s in sources:
            self.assertTrue(s["url_flux"].startswith("https://"), s["nom"])

    def test_verification(self):
        limite = date(2026, 9, 1)
        self.assertEqual(verifier_sources.etat(SOURCES[0], limite, faux_telechargement)[0], "OK")
        self.assertEqual(verifier_sources.etat(SOURCES[2], limite, faux_telechargement)[0], "ERREUR")
        self.assertEqual(verifier_sources.etat(SOURCES[0], date(2027, 1, 1), faux_telechargement)[0], "ANCIEN")


class Depot(unittest.TestCase):
    def test_controle_qualite(self):
        self.assertEqual(controle_depot.problemes(), [])


if __name__ == "__main__":
    unittest.main()
