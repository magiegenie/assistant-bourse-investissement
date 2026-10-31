"""Tests des scripts de calcul, sur le jeu fictif de templates/exemple/.

Lancer : python -m unittest discover tests
"""
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SCRIPTS = RACINE / "scripts"
EXEMPLE = RACINE / "templates" / "exemple"
sys.path.insert(0, str(SCRIPTS))

import allocation  # noqa: E402
import fiscalite  # noqa: E402
import performance  # noqa: E402
import projection  # noqa: E402
import stress  # noqa: E402


def lancer(*args):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise AssertionError(r.stderr)
    return r.stdout


class Allocation(unittest.TestCase):
    def test_versement_entierement_reparti(self):
        valeurs = {"Monde": 7000, "USA": 3000, "Cash": 0}
        cibles = {"Monde": 60, "USA": 20, "Cash": 20}
        alloc = allocation.repartir(valeurs, cibles, 1000)
        self.assertAlmostEqual(sum(alloc.values()), 1000, places=6)
        self.assertTrue(all(m >= 0 for m in alloc.values()))
        self.assertGreater(alloc["Cash"], alloc["USA"])

    def test_versement_qui_comble_tout(self):
        valeurs = {"Monde": 500, "USA": 500}
        cibles = {"Monde": 50, "USA": 50}
        alloc = allocation.repartir(valeurs, cibles, 1000)
        self.assertAlmostEqual(alloc["Monde"], 500)
        self.assertAlmostEqual(alloc["USA"], 500)

    def test_cli_exemple(self):
        sortie = lancer(SCRIPTS / "allocation.py", EXEMPLE, 1000)
        self.assertIn("Total : 15,802.00 €", sortie)
        self.assertIn("Frais annuels estimés", sortie)


class Performance(unittest.TestCase):
    def test_xirr_un_an(self):
        flux = [(date(2025, 1, 1), -1000), (date(2026, 1, 1), 1070)]
        self.assertAlmostEqual(performance.xirr(flux), 0.07, places=4)

    def test_xirr_signes_incoherents(self):
        with self.assertRaises(ValueError):
            performance.xirr([(date(2025, 1, 1), 1000), (date(2026, 1, 1), 1070)])

    def test_cli_exemple(self):
        self.assertIn("XIRR", lancer(SCRIPTS / "performance.py", EXEMPLE, 7))


class Projection(unittest.TestCase):
    def test_sans_rendement(self):
        self.assertAlmostEqual(projection.projeter(1000, 100, 0, 1), 2200)

    def test_versement_requis_atteint_objectif(self):
        m = projection.versement_requis(5000, 6, 10, 100000)
        self.assertGreaterEqual(projection.projeter(5000, m, 6, 10), 100000 - 1)
        self.assertLess(projection.projeter(5000, m - 5, 6, 10), 100000)


class Fiscalite(unittest.TestCase):
    def test_cto_pfu(self):
        gain, imposable, ir, ps, _ = fiscalite.cto(10000, 20000, 10000, 0)
        self.assertAlmostEqual(gain, 5000)
        self.assertAlmostEqual(ir + ps, 5000 * 0.314)

    def test_pea_plus_de_5_ans(self):
        _, _, ir, ps, _ = fiscalite.pea(8000, 24000, 15000, 6)
        self.assertEqual(ir, 0)
        self.assertAlmostEqual(ps, 3000 * 0.186)

    def test_av_abattement(self):
        _, imposable, _, _, _ = fiscalite.assurance_vie(10000, 20000, 15000, 9, False, 15000)
        self.assertEqual(imposable, 0)  # gain de 2 500 € sous l abattement de 4 600 €

    def test_aucun_gain(self):
        gain, *_ = fiscalite.cto(1000, 900, 1000, 0)
        self.assertEqual(gain, 0)


class Stress(unittest.TestCase):
    def test_classes(self):
        self.assertEqual(stress.classe("Crypto"), "crypto")
        self.assertEqual(stress.classe("Obligations"), "oblig")
        self.assertEqual(stress.classe("Monde"), "actions")
        self.assertEqual(stress.part_dollar("USA"), 1.0)

    def test_cli_exemple(self):
        self.assertIn("Krach type 2008", lancer(SCRIPTS / "stress.py", EXEMPLE))


class AutresCli(unittest.TestCase):
    def test_reequilibrage_controle(self):
        sortie = lancer(SCRIPTS / "reequilibrage.py", EXEMPLE, 0, 3)
        self.assertNotIn("ERREUR", sortie)

    def test_exposition(self):
        self.assertIn("États-Unis", lancer(SCRIPTS / "exposition.py", EXEMPLE))

    def test_fiscalite_cli(self):
        self.assertIn("Net perçu", lancer(SCRIPTS / "fiscalite.py", "pea", 8000, 24000, 15000))

    def test_projection_cli(self):
        self.assertIn("Objectif", lancer(SCRIPTS / "projection.py", 6000, 300, 5, 15, 100000))


class NouveauxCalculs(unittest.TestCase):
    def test_frais_ecart_positif(self):
        import frais
        a = frais.capital_final(5000, 300, 6, 0.2, 20)
        b = frais.capital_final(5000, 300, 6, 1.8, 20)
        self.assertGreater(a, b)
        self.assertAlmostEqual(frais.capital_final(1000, 0, 5, 5, 10), 1000)

    def test_budget(self):
        import budget
        mois = budget.lire_mois(EXEMPLE / "budget.md")
        self.assertEqual(len(mois), 3)
        self.assertEqual(mois[1]["revenu"], 2340)
        s = budget.synthese(mois, 6200)
        self.assertAlmostEqual(s["taux_epargne"], 1500 / 7095)
        self.assertGreater(s["precaution_mois"], 3)

    def test_bilan_mensuel(self):
        sortie = lancer(SCRIPTS / "bilan_mensuel.py", EXEMPLE, 500)
        for bloc in ("Répartition", "Performance réelle", "Exposition", "Tests de résistance", "Budget"):
            self.assertIn(bloc, sortie)
        self.assertNotIn("Erreur du script", sortie)


class Saisie(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        self.dossier = Path(tempfile.mkdtemp())
        for f in ("positions.csv", "flux.csv", "cibles.csv"):
            shutil.copy(EXEMPLE / f, self.dossier / f)

    def lignes(self, nom):
        return allocation.lire(self.dossier / nom)

    def test_investir_ligne_existante(self):
        import saisie
        saisie.appliquer(self.dossier, "investir", ["world", "500"], date(2026, 11, 5))
        world = [p for p in self.lignes("positions.csv") if "World" in p["nom"]][0]
        self.assertEqual((float(world["investi"]), float(world["valeur"])), (6700, 7635))
        self.assertEqual(self.lignes("flux.csv")[-1], {"date": "2026-11-05", "montant": "-500"})
        self.assertTrue((self.dossier / "positions.csv.bak").exists())

    def test_nouvelle_ligne_et_ambiguite(self):
        import saisie
        with self.assertRaises(SystemExit):
            saisie.appliquer(self.dossier, "achat", ["ETF", "100"], date(2026, 11, 5))
        with self.assertRaises(SystemExit):
            saisie.appliquer(self.dossier, "achat", ["ETF Nasdaq 100", "100"], date(2026, 11, 5))
        saisie.appliquer(self.dossier, "achat", ["ETF Nasdaq 100", "100"], date(2026, 11, 5), "USA", "PEA", 0.3)
        self.assertEqual(len(self.lignes("positions.csv")), 7)
        self.assertEqual(len(self.lignes("flux.csv")), 5)  # achat seul : pas de flux

    def test_vente_et_retrait(self):
        import saisie
        saisie.appliquer(self.dossier, "vente", ["bitcoin", "620"], date(2026, 11, 5), retrait=True)
        btc = [p for p in self.lignes("positions.csv") if p["nom"] == "Bitcoin"][0]
        self.assertEqual((float(btc["investi"]), float(btc["valeur"])), (250, 620))
        self.assertEqual(self.lignes("flux.csv")[-1]["montant"], "620")
        with self.assertRaises(SystemExit):
            saisie.appliquer(self.dossier, "vente", ["bitcoin", "5000"], date(2026, 11, 5))

    def test_scripts_relisent_apres_saisie(self):
        import saisie
        saisie.appliquer(self.dossier, "investir", ["world", "500"], date(2026, 11, 5))
        self.assertIn("XIRR", lancer(SCRIPTS / "performance.py", self.dossier, 7))


class ImportClasseur(unittest.TestCase):
    def test_import_depuis_classeur_recalcule(self):
        import shutil
        import tempfile
        if not shutil.which("soffice"):
            self.skipTest("LibreOffice absent : recalcul impossible")
        import creer_sheet
        import import_sheet
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            creer_sheet.construire(d / "ex.xlsx", exemple=True)
            subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", "--outdir", str(d / "calc"),
                            str(d / "ex.xlsx")], capture_output=True, timeout=120)
            positions, flux, cibles = import_sheet.lire_classeur(d / "calc" / "ex.xlsx", "Alice")
        self.assertEqual(len(positions), 3)
        self.assertAlmostEqual(sum(float(p["valeur"]) for p in positions), 3100)
        self.assertEqual(flux, [{"date": "2026-08-01", "montant": "-1200"}])
        self.assertAlmostEqual(sum(float(c["cible_pct"]) for c in cibles), 100)


class Classeur(unittest.TestCase):
    def test_feuilles(self):
        import tempfile
        from openpyxl import load_workbook
        import creer_sheet
        with tempfile.TemporaryDirectory() as d:
            chemin = Path(d) / "x.xlsx"
            creer_sheet.construire(chemin, exemple=True)
            noms = load_workbook(chemin).sheetnames
        for f in ("Dashboard", "Transactions", "Positions", "Fiscalité", "Idées", "Veille", "Revenus et frais"):
            self.assertIn(f, noms)


if __name__ == "__main__":
    unittest.main()
