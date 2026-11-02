"""Tests du générateur d'email de la newsletter : numérotation des sources, contrôles de lecture."""
import copy
import json
import sys
import unittest
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

import cloture_hebdo  # noqa: E402
import newsletter_html  # noqa: E402

EXEMPLE = RACINE / "docs" / "exemples" / "newsletter-2026-11-01.json"


def exemple():
    return json.loads(EXEMPLE.read_text(encoding="utf-8"))


class Newsletter(unittest.TestCase):
    def test_exemple_se_rend_avec_toutes_les_rubriques(self):
        page = newsletter_html.Rendu(exemple()).page()
        for titre in ("Résumé express", "Bilan de la semaine", "Pourquoi ça a baissé", "Ce qu&#x27;il se passe en ce moment",
                      "La France", "Pour toi", "La semaine qui vient", "ordre de lecture"):
            self.assertIn(titre, page)

    def test_plus_de_feuille_veille(self):
        page = newsletter_html.Rendu(exemple()).page()
        self.assertNotIn("feuille Veille", page)
        self.assertNotIn("recopier", page)

    def test_temps_de_lecture_calcule_entre_8_et_12_minutes(self):
        rendu = newsletter_html.Rendu(exemple())
        rendu.page()
        self.assertTrue(8 <= rendu.minutes <= 12, rendu.minutes)

    def test_sources_numerotees_dans_l_ordre_de_lecture(self):
        rendu = newsletter_html.Rendu(exemple())
        rendu.page()
        # La première source citée est celle des clôtures, dans le résumé du haut.
        self.assertEqual(rendu.ordre[0], "yahoo")
        self.assertEqual(len(rendu.ordre), len(set(rendu.ordre)))
        self.assertEqual(set(rendu.ordre), set(exemple()["sources"]))

    def test_renvois_croissants_a_la_lecture(self):
        import re
        corps, _ = newsletter_html.Rendu(exemple()).construire()
        vus = []
        for n in map(int, re.findall(r"<sup[^>]*>\[(\d+)\]</sup>", corps)):
            if n not in vus:
                self.assertEqual(n, len(vus) + 1, f"renvoi {n} apparait avant {len(vus) + 1}")
                vus.append(n)

    def test_aucun_lien_dans_le_corps(self):
        corps, _ = newsletter_html.Rendu(exemple()).construire()
        self.assertNotIn("href=", corps)
        self.assertNotIn("http", corps)

    def test_source_non_declaree_refusee(self):
        c = exemple()
        c["resume"]["verdict"] += " [[src:inconnue]]"
        with self.assertRaises(SystemExit):
            newsletter_html.Rendu(c).page()

    def test_source_jamais_citee_refusee(self):
        c = exemple()
        c["sources"]["orpheline"] = {"nom": "x", "url": "https://exemple.org"}
        with self.assertRaises(SystemExit):
            newsletter_html.Rendu(c).page()

    def test_tiret_long_et_emoji_refuses(self):
        for texte in ("Le CAC " + chr(8212) + " en baisse", "Bonne semaine \U0001F600"):
            c = copy.deepcopy(exemple())
            c["resume"]["verdict"] = texte
            with self.assertRaises(SystemExit):
                newsletter_html.Rendu(c).page()

    def test_chiffre_manquant_affiche_non_disponible(self):
        page = newsletter_html.Rendu(exemple()).page()
        self.assertIn("non disponible", page)

    def test_cause_sans_source_refusee(self):
        c = exemple()
        c["pourquoi_baisse"]["cartes"][0]["etapes"][0]["texte"] = "Alphabet baisse car les investisseurs sont inquiets."
        with self.assertRaises(SystemExit):
            newsletter_html.Rendu(c).page()

    def test_cause_non_etablie_acceptee_sans_source(self):
        c = exemple()
        c["pourquoi_baisse"]["cartes"][0]["etapes"][0]["texte"] = "Cause non établie."
        c["sources"].pop("ssga_spy", None)
        # ssga_spy est encore cité ailleurs : le rendu doit rester valide
        c["sources"]["ssga_spy"] = exemple()["sources"]["ssga_spy"]
        newsletter_html.Rendu(c).page()


class Clotures(unittest.TestCase):
    SERIE = [(date(2026, 10, 23), 100.0), (date(2026, 10, 26), 101.0), (date(2026, 10, 29), 110.0),
             (date(2026, 10, 30), 99.0)]

    def test_variation_hebdomadaire(self):
        r = cloture_hebdo.calcul(self.SERIE, date(2026, 10, 30), "prix")
        self.assertEqual(r["variation"], -1.0)
        self.assertEqual(r["reference"]["date"], "2026-10-23")
        self.assertEqual(len(r["jours"]), 3)

    def test_taux_en_points(self):
        serie = [(date(2026, 10, 23), 4.98), (date(2026, 10, 30), 4.93)]
        self.assertEqual(cloture_hebdo.calcul(serie, date(2026, 10, 30), "taux")["variation"], -0.05)

    def test_repere_sans_donnees_reste_nul(self):
        def en_panne(_ticker):
            raise OSError("réseau")
        res = cloture_hebdo.collecter(date(2026, 10, 30), [{"cle": "x", "nom": "X", "groupe": "g", "ticker_yahoo": "X", "type": "prix"}], en_panne)
        self.assertIsNone(res["reperes"][0]["variation"])

    def test_dernier_vendredi(self):
        self.assertEqual(cloture_hebdo.dernier_vendredi(date(2026, 11, 2)), date(2026, 10, 30))
        self.assertEqual(cloture_hebdo.dernier_vendredi(date(2026, 11, 1)), date(2026, 10, 30))


if __name__ == "__main__":
    unittest.main()
