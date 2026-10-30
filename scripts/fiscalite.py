"""Estimation de l'impôt d'un retrait ou d'une vente (CTO, PEA, assurance vie), taux 2026.

Usage : python scripts/fiscalite.py <cto|pea|av> <retrait> <valeur_totale> <total_verse> [options]
Options : --anciennete ANNEES (défaut 6) ; --couple (assurance vie, abattement de 9 200 €) ;
          --primes MONTANT (assurance vie : total des primes versées, défaut = total_verse) ;
          --moins-values MONTANT (CTO : moins-values reportables à imputer)

L'impôt ne porte que sur la part de gain contenue dans le retrait : retrait x (valeur - versé) / valeur.
Les taux sont dans le dictionnaire TAUX ci-dessous : à revérifier chaque année (fiche C).
"""
import argparse
import sys
sys.stdout.reconfigure(encoding="utf-8")

# Taux 2026. Vérifiés sur service-public.fr (fiches F2329, F2613, F22449) sauf mention contraire.
TAUX = {
    "ir_pfu": 12.8,
    "ps_general": 18.6,       # CTO, plus-values mobilières, PEA (cas général, à vérifier pour le PEA)
    "ps_assurance_vie": 17.2,
    "av_taux_reduit": 7.5,    # après 8 ans, primes <= seuil (à vérifier)
    "av_seuil_primes": 150000,
    "av_abattement_seul": 4600,
    "av_abattement_couple": 9200,
}


def part_de_gain(retrait, valeur, verse):
    if valeur <= 0:
        raise SystemExit("La valeur totale doit être positive.")
    return max(0.0, (valeur - verse) / valeur)


def cto(retrait, valeur, verse, moins_values):
    gain = retrait * part_de_gain(retrait, valeur, verse)
    imposable = max(0.0, gain - moins_values)
    ir = imposable * TAUX["ir_pfu"] / 100
    ps = imposable * TAUX["ps_general"] / 100
    return gain, imposable, ir, ps, []


def pea(retrait, valeur, verse, anciennete):
    gain = retrait * part_de_gain(retrait, valeur, verse)
    notes = []
    if anciennete >= 5:
        ir = 0.0
        notes.append("PEA de plus de 5 ans : 0 % d'impôt sur le revenu, prélèvements sociaux seuls "
                     "(taux 18,6 % par application du cas général, à vérifier pour les gains anciens).")
    else:
        ir = gain * TAUX["ir_pfu"] / 100
        notes.append("ATTENTION : un retrait avant 5 ans clôture le plan (sauf cas légaux).")
    ps = gain * TAUX["ps_general"] / 100
    return gain, gain, ir, ps, notes


def assurance_vie(retrait, valeur, verse, anciennete, couple, primes):
    gain = retrait * part_de_gain(retrait, valeur, verse)
    notes = ["Simplification : les prélèvements sociaux des fonds en euros sont en réalité prélevés chaque année."]
    ps = gain * TAUX["ps_assurance_vie"] / 100
    if anciennete < 8:
        ir = gain * TAUX["ir_pfu"] / 100
        notes.append("Contrat de moins de 8 ans : 12,8 % sans abattement.")
        return gain, gain, ir, ps, notes
    abattement = TAUX["av_abattement_couple"] if couple else TAUX["av_abattement_seul"]
    imposable = max(0.0, gain - abattement)
    seuil = TAUX["av_seuil_primes"]
    if primes <= seuil:
        taux_ir = TAUX["av_taux_reduit"]
    else:
        part_haute = (primes - seuil) / primes
        taux_ir = TAUX["av_taux_reduit"] * (1 - part_haute) + TAUX["ir_pfu"] * part_haute
        notes.append("Primes supérieures à 150 000 € : taux d'impôt pondéré (estimation).")
    ir = imposable * taux_ir / 100
    notes.append(f"Abattement annuel appliqué : {abattement:,.0f} €.".replace(",", " "))
    return gain, imposable, ir, ps, notes


def main():
    p = argparse.ArgumentParser(description="Estimation de l'impôt d'un retrait (taux 2026).")
    p.add_argument("enveloppe", choices=["cto", "pea", "av"])
    p.add_argument("retrait", type=float)
    p.add_argument("valeur_totale", type=float)
    p.add_argument("total_verse", type=float)
    p.add_argument("--anciennete", type=float, default=6)
    p.add_argument("--couple", action="store_true")
    p.add_argument("--primes", type=float, default=None)
    p.add_argument("--moins-values", type=float, default=0.0)
    a = p.parse_args()

    if a.enveloppe == "cto":
        gain, imposable, ir, ps, notes = cto(a.retrait, a.valeur_totale, a.total_verse, a.moins_values)
    elif a.enveloppe == "pea":
        gain, imposable, ir, ps, notes = pea(a.retrait, a.valeur_totale, a.total_verse, a.anciennete)
    else:
        primes = a.primes if a.primes is not None else a.total_verse
        gain, imposable, ir, ps, notes = assurance_vie(
            a.retrait, a.valeur_totale, a.total_verse, a.anciennete, a.couple, primes)

    total = ir + ps
    print(f"Retrait brut                    : {a.retrait:>12,.2f} €")
    print(f"Part de gain dans le retrait    : {gain:>12,.2f} €")
    print(f"Base imposable à l'IR           : {imposable:>12,.2f} €")
    print(f"Impôt sur le revenu             : {ir:>12,.2f} €")
    print(f"Prélèvements sociaux            : {ps:>12,.2f} €")
    print(f"Total des impôts                : {total:>12,.2f} €")
    print(f"Net perçu                       : {a.retrait - total:>12,.2f} €")
    if gain > 0:
        print(f"Taux effectif sur le gain       : {total / gain * 100:>11.1f} %")
    for n in notes:
        print("Note :", n)
    print("Estimation à vérifier avec un professionnel pour les cas complexes. Taux 2026, à revérifier (fiche C).")


if __name__ == "__main__":
    main()
