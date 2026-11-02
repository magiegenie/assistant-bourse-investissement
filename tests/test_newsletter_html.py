"""Tests du générateur d'email de la newsletter : numérotation des sources, contrôles de lecture."""
import copy
import json
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

import newsletter_html  # noqa: E402

EXEMPLE = RACINE / "docs" / "exemples" / "newsletter-2026-11-01.json"


def exemple():
    return json.loads(EXEMPLE.read_text(encoding="utf-8"))


class Newsletter(unittest.TestCase):
    def test_exemple_se_rend(self):
        page = newsletter_html.Rendu(exemple()).page()
        self.assertIn("ordre de lecture", page)

    def test_sources_numerotees_dans_l_ordre_de_lecture(self):
        rendu = newsletter_html.Rendu(exemple())
        rendu.page()
        # La première source citée dans le texte est le récapitulatif de marché de la vue d'ensemble.
        self.assertEqual(rendu.ordre[0], "recap_ifyouspent")
        self.assertEqual(len(rendu.ordre), len(set(rendu.ordre)))
        self.assertEqual(set(rendu.ordre), set(exemple()["sources"]))

    def test_aucun_lien_dans_le_corps(self):
        corps, _ = newsletter_html.Rendu(exemple()).construire()
        self.assertNotIn("href=", corps)
        self.assertNotIn("http", corps)

    def test_source_non_declaree_refusee(self):
        c = exemple()
        c["verdict"] += " [[src:inconnue]]"
        with self.assertRaises(SystemExit):
            newsletter_html.Rendu(c).page()

    def test_source_jamais_citee_refusee(self):
        c = exemple()
        c["sources"]["orpheline"] = {"nom": "x", "url": "https://exemple.org"}
        with self.assertRaises(SystemExit):
            newsletter_html.Rendu(c).page()

    def test_tiret_long_et_emoji_refuses(self):
        for texte in ("Le CAC " + chr(8212) + " en baisse","Bonne semaine \U0001F600"):
            c = copy.deepcopy(exemple())
            c["verdict"] = texte
            with self.assertRaises(SystemExit):
                newsletter_html.Rendu(c).page()

    def test_chiffre_manquant_affiche_non_disponible(self):
        page = newsletter_html.Rendu(exemple()).page()
        self.assertIn("non disponible", page)


if __name__ == "__main__":
    unittest.main()
