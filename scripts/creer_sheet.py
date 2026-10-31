"""Génère le classeur du portefeuille d'une personne, à importer dans Google Sheets (ou à ouvrir dans Excel).

Usage :
  python scripts/creer_sheet.py [sortie.xlsx]                                 modèle vide et anonyme
  python scripts/creer_sheet.py sortie.xlsx --profil prive/<prenom>           pré-rempli depuis le dossier de la personne
  python scripts/creer_sheet.py sortie.xlsx --exemple                         données FICTIVES pour tester les formules

Pré-remplissage : parametres.csv (versement, jour, PEA, plafonds, courtier), cibles.csv (poches et cibles),
positions.csv (une ligne d'actif et une transaction « Reprise » par ligne déjà détenue), objectifs.csv, budget.csv.
Formules compatibles Google Sheets et Excel (GOOGLEFINANCE ne fonctionne que dans Google Sheets).
"""
import sys
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, PieChart, Reference
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

sys.stdout.reconfigure(encoding="utf-8")
from fichiers_profil import POCHES_DEFAUT, lire_csv, lire_parametres, nombre

BLEU, GRIS, JAUNE = "1F3A5F", "5B6770", "FFF4CC"
H_IN = PatternFill("solid", fgColor=BLEU)
H_CALC = PatternFill("solid", fgColor=GRIS)
CALC = PatternFill("solid", fgColor="F1F3F5")
IN = PatternFill("solid", fgColor=JAUNE)
ROUGE = Font(color="C00000")
VERT = Font(color="2E7D32")
EUR, PCT, DATE = '#,##0.00 "€"', "0.0%", "DD/MM/YYYY"
NB_POCHES = 10  # lignes réservées aux poches (les vides restent vides)
NB_ACTIFS = 60
NB_TRANSACTIONS = 1000
NB_MOIS = 120  # lignes de Historique et Budget
NB_JOURNAL = 300
ENVELOPPES = ["PEA", "CTO", "Assurance vie", "PER", "Crypto", "Livret", "Épargne salariale"]
TYPES_OP = ["Versement", "Reprise", "Achat", "Vente", "Dividende", "Frais", "Retrait", "Intérêts"]
PS = "'Paramètres'"


def tete(ws, cols, calc=()):
    ws.append([c[0] for c in cols])
    for i, (nom, larg) in enumerate(cols, start=1):
        c = ws.cell(1, i)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = H_CALC if i in calc else H_IN
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(i)].width = larg
    ws.row_dimensions[1].height = 42
    ws.freeze_panes = "A2"


def liste(ws, plage, source):
    dv = DataValidation(type="list", formula1=source, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(plage)


def ticker_google(yahoo):
    """CW8.PA -> EPA:CW8 ; ticker sans suffixe (bourse américaine) inchangé."""
    if not yahoo:
        return ""
    bourses = {"PA": "EPA", "DE": "ETR", "AS": "AMS", "L": "LON", "MI": "BIT", "SW": "SWX", "BR": "EBR"}
    if "." in yahoo:
        code, suffixe = yahoo.rsplit(".", 1)
        return f"{bourses.get(suffixe.upper(), suffixe.upper())}:{code}"
    return yahoo


def construire(chemin, profil=None, exemple=False):
    params = lire_parametres(profil) if profil else {}
    prenom = params.get("prenom") or ("Alice" if exemple else "Prénom")
    cibles = {r["poche"]: nombre(r["cible_pct"]) for r in lire_csv(Path(profil) / "cibles.csv")} if profil else {}
    poches = list(cibles) or list(POCHES_DEFAUT)
    if "Autre" not in poches:
        poches.append("Autre")
    poches = poches[:NB_POCHES]
    listes = {
        "K": ("Types d'opération", TYPES_OP),
        "L": ("Enveloppes", ENVELOPPES),
        "M": ("Types d'actif", ["ETF", "Action", "Crypto", "Obligation", "Fonds euro", "Cash"]),
        "N": ("Poches", poches),
        "O": ("Cœur / satellite", ["Cœur", "Satellite"]),
        "P": ("Cap / dist", ["Capitalisant", "Distribuant"]),
        "Q": ("Devises", ["EUR", "USD", "GBP", "CHF"]),
        "R": ("Verdicts du Coach", ["Conforme au plan", "Attendre 24-72 h", "Contraire aux règles"]),
        "S": ("Prévu / hors plan", ["Prévu", "Hors plan"]),
        "T": ("Statut", ["En avance", "Dans les temps", "En retard", "Atteint"]),
    }

    def L(col):
        return f"={PS}!${col}$2:${col}${len(listes[col][1]) + 1}"

    UTIL = f"={PS}!$A$2:$A$3"
    wb = Workbook()

    # ---------- Lisez-moi
    ws = wb.active
    ws.title = "Lisez-moi"
    ws.sheet_properties.tabColor = "999999"
    lignes = [
        f"PORTEFEUILLE DE {prenom.upper()} : mode d'emploi",
        "",
        "Cases et en-têtes BLEUS = tu saisis. En-têtes GRIS et cases grisées = calculé automatiquement, n'écris rien dedans.",
        "",
        "AU QUOTIDIEN (2 minutes, depuis ton téléphone avec l'app Google Sheets) :",
        "  Transactions : une ligne à chaque opération (versement, achat, vente, dividende). On ajoute, on n'efface jamais.",
        "  Pour Versement, Dividende, Frais, Retrait, Intérêts : Quantité = 1 et le montant dans Prix unitaire.",
        "",
        "UNE FOIS PAR MOIS (5 minutes) :",
        "  Historique : une ligne (valeur du portefeuille, total versé, versement du mois).",
        "  Budget : une ligne (revenu, besoins, envies, épargne).",
        "  Puis dis à l'assistant « synchronise mon Sheet » : il relit tout et met à jour ses calculs et ton app.",
        "",
        "AU DÉPART (fait avec l'assistant à l'accueil) :",
        "  Paramètres : versement mensuel, jour, date du PEA, plafonds.",
        "  Actifs : une ligne par ETF, action ou crypto. Ticker Google (ex. EPA:CW8) pour le prix automatique, sinon Prix saisi à la main.",
        "  Transactions de type « Reprise » : les lignes que tu possédais déjà, avec la quantité et le prix de revient.",
        "  Cibles et Objectifs : repris de ton plan d'investissement.",
        "",
        "Positions et Tableau de bord se calculent seuls. Le Tableau de bord te dit quoi faire ce mois-ci.",
        "Prix : GOOGLEFINANCE marche dans Google Sheets pour la plupart des ETF. Sinon, colonne « Prix saisi à la main » dans Actifs.",
        "Confidentialité : ce fichier contient tes données. Ne le partage qu'avec l'assistant (connecteur Google Drive).",
    ]
    for l in lignes:
        ws.append([l])
    ws["A1"].font = Font(bold=True, size=14, color=BLEU)
    for r in (5, 9, 14):
        ws[f"A{r}"].font = Font(bold=True)
    ws.column_dimensions["A"].width = 120

    db = wb.create_sheet("Tableau de bord")
    db.sheet_properties.tabColor = "2E7D32"

    # ---------- Paramètres
    pa = wb.create_sheet("Paramètres")
    pa.sheet_properties.tabColor = "F2B01E"
    tete(pa, [("Utilisateur", 16), ("Devise de référence", 12), ("Versement mensuel prévu (€)", 14),
              ("Jour du versement", 10), ("Date d'ouverture du PEA", 14), ("Indice de référence", 18),
              ("Plafond crypto %", 10), ("Plafond par ligne %", 10), ("Courtier principal", 18)])
    pea = params.get("date_ouverture_pea", "")
    pa.append([prenom, "EUR", nombre(params.get("versement_mensuel"), 500) or 500,
               int(nombre(params.get("jour_versement"), 5)) or 5,
               date.fromisoformat(pea) if pea else None, params.get("indice_reference") or "MSCI_WORLD",
               nombre(params.get("plafond_crypto_pct"), 10), nombre(params.get("plafond_ligne_pct"), 5),
               params.get("courtier_principal", "")])
    for c in "ABCDEFGHI":
        pa[f"{c}2"].fill = IN
    pa["E2"].number_format = DATE
    pa["C2"].number_format = EUR
    for col, (titre, valeurs) in listes.items():
        c = pa[f"{col}1"]
        c.value = titre
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = H_CALC
        c.alignment = Alignment(wrap_text=True, horizontal="center")
        pa.column_dimensions[col].width = 18
        for i, v in enumerate(valeurs, start=2):
            pa[f"{col}{i}"] = v
    pa["A5"] = "Ligne 3 : laisse vide, ou ajoute une 2e personne si vous partagez ce classeur."
    pa["A6"] = "Les colonnes K à T sont les listes déroulantes du classeur : tu peux ajouter une poche en colonne N (10 au maximum)."
    for c in ("A5", "A6"):
        pa[c].font = Font(italic=True)

    # ---------- Actifs
    ac = wb.create_sheet("Actifs")
    ac.sheet_properties.tabColor = "F2B01E"
    tete(ac, [("ID (code court)", 14), ("Nom", 34), ("ISIN", 16), ("Ticker Google (ex. EPA:CW8)", 16), ("Type", 12),
              ("Poche", 16), ("Secteur", 14), ("Devise de cotation", 10), ("Exposition devise", 12),
              ("Enveloppe", 14), ("Frais annuels (TER) %", 11), ("Cap / dist", 14), ("Cœur / satellite", 12),
              ("Prix actuel", 12), ("Date du prix", 12), ("Ticker Yahoo (ex. CW8.PA)", 16), ("Prix saisi à la main", 12)],
         calc=(14,))
    fin_ac = NB_ACTIFS + 1
    for r in range(2, fin_ac + 1):
        ac[f"N{r}"] = f'=IF(Q{r}<>"",Q{r},IF(D{r}="","",IFERROR(GOOGLEFINANCE(D{r}),"")))'
        ac[f"N{r}"].number_format = EUR
        ac[f"N{r}"].fill = CALC
        ac[f"O{r}"].number_format = DATE
        ac[f"Q{r}"].number_format = EUR
    liste(ac, f"E2:E{fin_ac}", L("M"))
    liste(ac, f"F2:F{fin_ac}", f"={PS}!$N$2:$N${NB_POCHES + 1}")
    liste(ac, f"H2:H{fin_ac}", L("Q"))
    liste(ac, f"I2:I{fin_ac}", L("Q"))
    liste(ac, f"J2:J{fin_ac}", L("L"))
    liste(ac, f"L2:L{fin_ac}", L("P"))
    liste(ac, f"M2:M{fin_ac}", L("O"))

    # ---------- Transactions
    tr = wb.create_sheet("Transactions")
    tr.sheet_properties.tabColor = "F2B01E"
    tete(tr, [("Date", 12), ("Utilisateur", 14), ("Enveloppe", 14), ("Type d'opération", 14), ("ID actif", 14),
              ("Quantité", 10), ("Prix unitaire (ou montant)", 13), ("Frais de courtage", 10), ("Devise", 8),
              ("Taux de change (1 si EUR)", 11), ("Montant en €", 14), ("Prévu / hors plan", 12),
              ("Source de l'idée", 18), ("Note", 30)], calc=(11,))
    for r in range(2, NB_TRANSACTIONS + 2):
        tr[f"K{r}"] = (f'=IF(OR(D{r}="",F{r}="",G{r}=""),"",F{r}*G{r}*IF(J{r}="",1,J{r})'
                       f'+IF(OR(D{r}="Achat",D{r}="Reprise"),N(H{r}),IF(D{r}="Vente",-N(H{r}),0)))')
        tr[f"K{r}"].number_format = EUR
        tr[f"K{r}"].fill = CALC
        tr[f"A{r}"].number_format = DATE
    liste(tr, f"B2:B{NB_TRANSACTIONS + 1}", UTIL)
    liste(tr, f"C2:C{NB_TRANSACTIONS + 1}", L("L"))
    liste(tr, f"D2:D{NB_TRANSACTIONS + 1}", L("K"))
    liste(tr, f"E2:E{NB_TRANSACTIONS + 1}", f"=Actifs!$A$2:$A${fin_ac}")
    liste(tr, f"I2:I{NB_TRANSACTIONS + 1}", L("Q"))
    liste(tr, f"L2:L{NB_TRANSACTIONS + 1}", L("S"))

    # ---------- Positions : une ligne par actif, automatiquement
    po = wb.create_sheet("Positions")
    po.sheet_properties.tabColor = "5B6770"
    tete(po, [("Utilisateur", 14), ("ID actif", 14), ("Nom", 30), ("Poche", 15), ("Enveloppe", 13),
              ("Quantité détenue", 11), ("Prix de revient moyen", 12), ("Montant investi (net)", 13),
              ("Prix actuel", 11), ("Valeur actuelle", 13), ("Plus ou moins-value €", 13),
              ("Plus ou moins-value %", 11), ("Poids %", 9), ("Dividendes reçus", 12),
              ("Frais annuels estimés €", 12)], calc=tuple(range(1, 16)))
    T = "Transactions!"
    for r in range(2, fin_ac + 1):
        crit = f"{T}$E:$E,$B{r}"
        somme = lambda col, typ: f'SUMIFS({T}${col}:${col},{crit},{T}$D:$D,"{typ}")'
        ach = f'({somme("F", "Achat")}+{somme("F", "Reprise")})'
        mont_a = f'({somme("K", "Achat")}+{somme("K", "Reprise")})'
        idx = lambda col: f'IFERROR(INDEX(Actifs!${col}:${col},MATCH($B{r},Actifs!$A:$A,0)),"")'
        po[f"A{r}"] = f'=IF(Actifs!A{r}="","",{PS}!$A$2)'
        po[f"B{r}"] = f'=IF(Actifs!A{r}="","",Actifs!A{r})'
        po[f"C{r}"] = f'=IF($B{r}="","",{idx("B")})'
        po[f"D{r}"] = f'=IF($B{r}="","",{idx("F")})'
        po[f"E{r}"] = f'=IF($B{r}="","",{idx("J")})'
        po[f"F{r}"] = f'=IF($B{r}="","",{ach}-{somme("F", "Vente")})'
        po[f"G{r}"] = f'=IF($B{r}="","",IFERROR({mont_a}/{ach},""))'
        po[f"H{r}"] = f'=IF($B{r}="","",IFERROR(G{r}*F{r},0))'
        po[f"I{r}"] = f'=IF($B{r}="","",{idx("N")})'
        po[f"J{r}"] = f'=IF(OR($B{r}="",I{r}=""),"",F{r}*I{r})'
        po[f"K{r}"] = f'=IF(J{r}="","",J{r}-H{r})'
        po[f"L{r}"] = f'=IF(J{r}="","",IFERROR(K{r}/H{r},""))'
        po[f"M{r}"] = f'=IF(J{r}="","",IFERROR(J{r}/SUM($J$2:$J${fin_ac}),""))'
        po[f"N{r}"] = f'=IF($B{r}="","",{somme("K", "Dividende")})'
        po[f"O{r}"] = f'=IF(J{r}="","",J{r}*N({idx("K")})/100)'
        for c in "GHIJKNO":
            po[f"{c}{r}"].number_format = EUR
        for c in "LM":
            po[f"{c}{r}"].number_format = PCT
        for c in "ABCDEFGHIJKLMNO":
            po[f"{c}{r}"].fill = CALC
    po.conditional_formatting.add(f"K2:L{fin_ac}", CellIsRule(operator="lessThan", formula=["0"], font=ROUGE))
    po.conditional_formatting.add(f"K2:L{fin_ac}", CellIsRule(operator="greaterThan", formula=["0"], font=VERT))

    # ---------- Historique
    hi = wb.create_sheet("Historique")
    hi.sheet_properties.tabColor = "F2B01E"
    tete(hi, [("Mois (1er du mois)", 13), ("Utilisateur", 14), ("Valeur totale du portefeuille", 14),
              ("Total versé cumulé", 13), ("Versement du mois", 12), ("Plus-value latente", 13),
              ("Performance du mois %", 12), ("Valeur de l'indice (mêmes versements)", 15),
              ("Cash disponible", 12), ("Épargne de précaution", 13)], calc=(6, 7))
    for r in range(2, NB_MOIS + 2):
        hi[f"F{r}"] = f'=IF(OR(C{r}="",D{r}=""),"",C{r}-D{r})'
        hi[f"G{r}"] = (f'=IF(OR(C{r}="",A{r}=""),"",IFERROR((C{r}-N(E{r})-SUMIFS($C:$C,$A:$A,EDATE(A{r},-1),$B:$B,B{r}))'
                       f'/SUMIFS($C:$C,$A:$A,EDATE(A{r},-1),$B:$B,B{r}),""))')
        hi[f"A{r}"].number_format = "MM/YYYY"
        for c in "CDEFHIJ":
            hi[f"{c}{r}"].number_format = EUR
        hi[f"G{r}"].number_format = PCT
        hi[f"F{r}"].fill = CALC
        hi[f"G{r}"].fill = CALC
    liste(hi, f"B2:B{NB_MOIS + 1}", UTIL)

    # ---------- Cibles
    ci = wb.create_sheet("Cibles")
    ci.sheet_properties.tabColor = "5B6770"
    tete(ci, [("Poche", 16), ("Cible %", 10), ("Valeur actuelle €", 14), ("Actuel %", 10),
              ("Écart (points)", 11), ("Besoin pour la cible €", 14), ("À verser ce mois €", 14)], calc=(1, 3, 4, 5, 6, 7))
    fin_ci = NB_POCHES + 1
    for i in range(NB_POCHES):
        r = 2 + i
        ci[f"A{r}"] = f'=IF({PS}!$N${2 + i}="","",{PS}!$N${2 + i})'
        ci[f"B{r}"].fill = IN
        ci[f"B{r}"].number_format = PCT
        ci[f"C{r}"] = f'=IF(A{r}="","",SUMIFS(Positions!$J:$J,Positions!$D:$D,$A{r}))'
        ci[f"D{r}"] = f'=IF(A{r}="","",IFERROR(C{r}/SUM($C$2:$C${fin_ci}),0))'
        ci[f"E{r}"] = f'=IF(OR(A{r}="",B{r}=""),"",(D{r}-B{r})*100)'
        ci[f"F{r}"] = f'=IF(OR(A{r}="",B{r}=""),0,MAX(0,B{r}*(SUM($C$2:$C${fin_ci})+{PS}!$C$2)-C{r}))'
        ci[f"G{r}"] = f'=IF(A{r}="","",IFERROR(F{r}/SUM($F$2:$F${fin_ci})*{PS}!$C$2,0))'
        for c in "CFG":
            ci[f"{c}{r}"].number_format = EUR
        ci[f"D{r}"].number_format = PCT
        ci[f"E{r}"].number_format = "+0.0;-0.0;0.0"
        if poches[i:i + 1] and poches[i] in cibles:
            ci[f"B{r}"] = cibles[poches[i]] / 100
    ci.conditional_formatting.add(f"E2:E{fin_ci}", FormulaRule(formula=['AND(ISNUMBER(E2),ABS(E2)>5)'],
                                                                fill=PatternFill("solid", fgColor="F8D7DA")))
    ci["I1"] = "Total des cibles (doit faire 100 %)"
    ci["I1"].font = Font(bold=True)
    ci["I2"] = f"=SUM(B2:B{fin_ci})"
    ci["I2"].number_format = PCT
    ci.column_dimensions["I"].width = 34

    # ---------- Budget
    bu = wb.create_sheet("Budget")
    bu.sheet_properties.tabColor = "F2B01E"
    tete(bu, [("Mois (1er du mois)", 13), ("Utilisateur", 14), ("Revenu net", 13), ("Besoins", 12), ("Envies", 12),
              ("Épargne + investissement", 14), ("Taux d'épargne %", 11), ("Dont abonnements", 12),
              ("Contrôle (reste)", 12), ("Note", 30)], calc=(7, 9))
    for r in range(2, NB_MOIS + 2):
        bu[f"G{r}"] = f'=IF(OR(C{r}="",F{r}=""),"",IFERROR(F{r}/C{r},""))'
        bu[f"I{r}"] = f'=IF(C{r}="","",C{r}-N(D{r})-N(E{r})-N(F{r}))'
        bu[f"A{r}"].number_format = "MM/YYYY"
        for c in "CDEFHI":
            bu[f"{c}{r}"].number_format = EUR
        bu[f"G{r}"].number_format = PCT
        bu[f"G{r}"].fill = CALC
        bu[f"I{r}"].fill = CALC
    liste(bu, f"B2:B{NB_MOIS + 1}", UTIL)
    bu.conditional_formatting.add(f"G2:G{NB_MOIS + 1}", CellIsRule(operator="greaterThanOrEqual", formula=["0.3"], font=VERT))
    bu.conditional_formatting.add(f"G2:G{NB_MOIS + 1}", FormulaRule(formula=['AND(ISNUMBER(G2),G2<0.2)'], font=ROUGE))
    bu.conditional_formatting.add(f"I2:I{NB_MOIS + 1}", FormulaRule(formula=['AND(ISNUMBER(I2),ABS(I2)>1)'], font=ROUGE))

    # ---------- Objectifs
    ob = wb.create_sheet("Objectifs")
    ob.sheet_properties.tabColor = "F2B01E"
    tete(ob, [("Objectif", 28), ("Montant cible", 14), ("Date de début", 12), ("Date cible", 12),
              ("Montant actuel", 14), ("Progression %", 11), ("Mois restants", 10),
              ("Versement mensuel nécessaire (sans rendement)", 18), ("Statut", 14)], calc=(6, 7, 8, 9))
    for r in range(2, 22):
        ob[f"F{r}"] = f'=IF(OR(B{r}="",E{r}=""),"",MIN(1,E{r}/B{r}))'
        ob[f"G{r}"] = f'=IF(D{r}="","",MAX(0,ROUND((D{r}-TODAY())/30.44,0)))'
        ob[f"H{r}"] = f'=IF(OR(B{r}="",G{r}="",G{r}=0),"",MAX(0,(B{r}-N(E{r}))/G{r}))'
        ob[f"I{r}"] = (f'=IF(OR(F{r}="",C{r}="",D{r}=""),"",IF(F{r}>=1,"Atteint",'
                       f'IF(F{r}>=(TODAY()-C{r})/(D{r}-C{r})+0.1,"En avance",IF(F{r}>=(TODAY()-C{r})/(D{r}-C{r})-0.05,"Dans les temps","En retard"))))')
        for c in "BEH":
            ob[f"{c}{r}"].number_format = EUR
        ob[f"F{r}"].number_format = PCT
        for c in "CD":
            ob[f"{c}{r}"].number_format = DATE
        for c in "FGHI":
            ob[f"{c}{r}"].fill = CALC
    for txt, coul in (("En retard", ROUGE), ("Atteint", VERT), ("En avance", VERT)):
        ob.conditional_formatting.add("I2:I21", CellIsRule(operator="equal", formula=[f'"{txt}"'], font=coul))

    # ---------- Journal
    jo = wb.create_sheet("Journal")
    jo.sheet_properties.tabColor = "F2B01E"
    tete(jo, [("Date", 12), ("Action (achat / vente)", 12), ("ID actif", 14), ("Montant €", 12),
              ("Pourquoi", 34), ("Pourquoi maintenant", 26), ("Ce qui invaliderait l'idée", 30), ("Source de l'idée", 18),
              ("Émotion (1 à 10)", 10), ("Verdict du Coach", 18), ("Décision finale", 14),
              ("Date du bilan à 3 mois", 13), ("Résultat à 3 mois", 22), ("Leçon", 34)], calc=(12,))
    for r in range(2, NB_JOURNAL + 2):
        jo[f"L{r}"] = f'=IF(A{r}="","",A{r}+91)'
        jo[f"L{r}"].number_format = DATE
        jo[f"L{r}"].fill = CALC
        jo[f"A{r}"].number_format = DATE
        jo[f"D{r}"].number_format = EUR
    liste(jo, f"B2:B{NB_JOURNAL + 1}", '"Achat,Vente,Autre"')
    liste(jo, f"C2:C{NB_JOURNAL + 1}", f"=Actifs!$A$2:$A${fin_ac}")
    liste(jo, f"I2:I{NB_JOURNAL + 1}", '"1,2,3,4,5,6,7,8,9,10"')
    liste(jo, f"J2:J{NB_JOURNAL + 1}", L("R"))
    liste(jo, f"K2:K{NB_JOURNAL + 1}", '"Acheté,Vendu,Reporté,Abandonné"')

    tableau_de_bord(db, fin_ac, fin_ci, len(ENVELOPPES), ob)

    if profil:
        pre_remplir(wb, profil, prenom, poches)
    if exemple:
        donnees_exemple(wb)
    wb.save(chemin)


def tableau_de_bord(db, fin_ac, fin_ci, nb_env, ob):
    U = f"{PS}!$A$2"
    db["A1"] = "TABLEAU DE BORD"
    db["A1"].font = Font(bold=True, size=16, color=BLEU)
    db["A2"] = f'="Portefeuille de "&{U}&", situation au :"'
    db["A2"].font = Font(italic=True)
    db["B2"] = "=TODAY()"
    db["B2"].number_format = DATE
    db["B2"].font = Font(italic=True)
    kpis = [
        ("Patrimoine (positions)", f"=SUM(Positions!$J$2:$J${fin_ac})", EUR),
        ("Montant investi net", f"=SUM(Positions!$H$2:$H${fin_ac})", EUR),
        ("Plus-value latente", f"=SUM(Positions!$K$2:$K${fin_ac})", EUR),
        ("Plus-value en %", "=IFERROR(C5/B5,0)", PCT),
        ("Taux d'épargne (dernier mois)",
         f'=IFERROR(INDEX(Budget!$G$2:$G${NB_MOIS + 1},MATCH(MAX(Budget!$A$2:$A${NB_MOIS + 1}),Budget!$A$2:$A${NB_MOIS + 1},0)),"")', PCT),
        ("Frais annuels estimés", f"=SUM(Positions!$O$2:$O${fin_ac})", EUR),
        ("Décisions hors plan", '=COUNTIFS(Transactions!$L:$L,"Hors plan")', "0"),
    ]
    for i, (nom, f, fmt) in enumerate(kpis, start=1):
        c = db.cell(4, i, nom)
        c.font = Font(bold=True, color="FFFFFF", size=9)
        c.fill = H_IN
        c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")
        v = db.cell(5, i, f)
        v.number_format = fmt
        v.font = Font(bold=True, size=13)
        v.alignment = Alignment(horizontal="center")
    db.row_dimensions[4].height = 32
    for i in range(1, 8):
        db.column_dimensions[get_column_letter(i)].width = 17
    db.column_dimensions["A"].width = 22

    # Lignes du tableau des poches (référencées par les messages « à faire »)
    p0, p1 = 19, 19 + NB_POCHES - 1
    db["A7"] = "À FAIRE CE MOIS"
    db["A7"].font = Font(bold=True, size=12, color=BLEU)
    db["A8"] = f'="Versement prévu : "&ROUND({PS}!$C$2,0)&" € le "&{PS}!$D$2&" du mois, à répartir selon « À verser » ci-dessous."'
    db["A9"] = f'=IFERROR("Poche la plus en retard sur sa cible : "&INDEX($A${p0}:$A${p1},MATCH(MIN($E${p0}:$E${p1}),$E${p0}:$E${p1},0))&" ("&ROUND(MIN($E${p0}:$E${p1}),1)&" pts)","")'
    db["A10"] = f'=IFERROR("Poche la plus en avance sur sa cible : "&INDEX($A${p0}:$A${p1},MATCH(MAX($E${p0}:$E${p1}),$E${p0}:$E${p1},0))&" ("&ROUND(MAX($E${p0}:$E${p1}),1)&" pts)","")'
    db["A11"] = (f'=IF(SUMIFS(Positions!$J:$J,Positions!$D:$D,"Crypto")/MAX(1,SUM(Positions!$J$2:$J${fin_ac}))'
                 f'>{PS}!$G$2/100,"ALERTE : la crypto dépasse le plafond fixé.","Crypto dans la limite fixée.")')
    db["A12"] = (f'=IF(MAX(Positions!$M$2:$M${fin_ac})>{PS}!$H$2/100,'
                 f'"À vérifier : une ligne dépasse "&{PS}!$H$2&" % (normal pour un ETF monde, pas pour une action).",'
                 f'"Aucune ligne au-dessus du plafond par ligne.")')
    db["A13"] = ('=COUNTIFS(Journal!$L:$L,"<="&TODAY(),Journal!$M:$M,"",Journal!$A:$A,"<>")'
                 '&" bilan(s) de décision à faire (3 mois écoulés)."')
    db["A14"] = ('=IF(COUNTIFS(Historique!$A:$A,DATE(YEAR(TODAY()),MONTH(TODAY()),1))=0,'
                 '"Historique du mois à saisir (feuille Historique).","Historique du mois saisi.")')
    db["A15"] = ('=IF(COUNTIFS(Budget!$A:$A,DATE(YEAR(TODAY()),MONTH(TODAY()),1))=0,'
                 '"Budget du mois à saisir (feuille Budget).","Budget du mois saisi.")')
    db["A16"] = f'=IF(ABS(SUM(Cibles!$B$2:$B${fin_ci})-1)>0.001,"Tes cibles ne font pas 100 % (feuille Cibles).","Cibles OK.")'

    def entete(row, titres):
        for i, t in enumerate(titres, start=1):
            c = db.cell(row, i, t)
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = H_CALC
            c.alignment = Alignment(horizontal="center", wrap_text=True)

    db[f"A{p0 - 2}"] = "Répartition par poche"
    db[f"A{p0 - 2}"].font = Font(bold=True, size=12, color=BLEU)
    entete(p0 - 1, ["Poche", "Valeur €", "Actuel %", "Cible %", "Écart (pts)", "À verser €"])
    for i in range(NB_POCHES):
        r, s = p0 + i, 2 + i
        db[f"A{r}"] = f'=IF(Cibles!$A${s}="","",Cibles!$A${s})'
        db[f"B{r}"] = f'=IF(A{r}="","",Cibles!$C${s})'
        db[f"C{r}"] = f'=IF(A{r}="","",Cibles!$D${s})'
        db[f"D{r}"] = f'=IF(A{r}="","",Cibles!$B${s})'
        db[f"E{r}"] = f'=IF(OR(A{r}="",D{r}=""),"",(C{r}-D{r})*100)'
        db[f"F{r}"] = f'=IF(A{r}="","",Cibles!$G${s})'
        for c in "BF":
            db[f"{c}{r}"].number_format = EUR
        for c in "CD":
            db[f"{c}{r}"].number_format = PCT
        db[f"E{r}"].number_format = "+0.0;-0.0;0.0"
    db.conditional_formatting.add(f"E{p0}:E{p1}", FormulaRule(formula=[f"AND(ISNUMBER(E{p0}),ABS(E{p0})>5)"],
                                                              fill=PatternFill("solid", fgColor="F8D7DA")))

    e0 = p1 + 4
    db[f"A{e0 - 2}"] = "Répartition par enveloppe"
    db[f"A{e0 - 2}"].font = Font(bold=True, size=12, color=BLEU)
    entete(e0 - 1, ["Enveloppe", "Valeur €", "Poids %"])
    e1 = e0 + nb_env - 1
    for i in range(nb_env):
        r = e0 + i
        db[f"A{r}"] = f"={PS}!$L${2 + i}"
        db[f"B{r}"] = f"=SUMIFS(Positions!$J:$J,Positions!$E:$E,$A{r})"
        db[f"C{r}"] = f"=IFERROR(B{r}/SUM($B${e0}:$B${e1}),0)"
        db[f"B{r}"].number_format = EUR
        db[f"C{r}"].number_format = PCT

    h0 = e1 + 4
    db[f"A{h0 - 2}"] = "Historique (24 derniers mois)"
    db[f"A{h0 - 2}"].font = Font(bold=True, size=12, color=BLEU)
    entete(h0 - 1, ["Mois", "Valeur portefeuille", "Total versé", "Valeur indice", "Perf du mois"])
    for i in range(24):
        r = h0 + i
        db[f"A{r}"] = f"=EDATE(DATE(YEAR(TODAY()),MONTH(TODAY()),1),{i - 23})"
        db[f"A{r}"].number_format = "MM/YYYY"
        for col, src in (("B", "C"), ("C", "D"), ("D", "H"), ("E", "G")):
            db[f"{col}{r}"] = f"=IF(COUNTIFS(Historique!$A:$A,$A{r})=0,NA(),SUMIFS(Historique!${src}:${src},Historique!$A:$A,$A{r}))"
            db[f"{col}{r}"].number_format = PCT if col == "E" else EUR
    h1 = h0 + 23

    b0 = h1 + 4
    db[f"A{b0 - 2}"] = "Budget (12 derniers mois)"
    db[f"A{b0 - 2}"].font = Font(bold=True, size=12, color=BLEU)
    entete(b0 - 1, ["Mois", "Besoins", "Envies", "Épargne + invest."])
    for i in range(12):
        r = b0 + i
        db[f"A{r}"] = f"=EDATE(DATE(YEAR(TODAY()),MONTH(TODAY()),1),{i - 11})"
        db[f"A{r}"].number_format = "MM/YYYY"
        for col, src in (("B", "D"), ("C", "E"), ("D", "F")):
            db[f"{col}{r}"] = f"=SUMIFS(Budget!${src}:${src},Budget!$A:$A,$A{r})"
            db[f"{col}{r}"].number_format = EUR
    b1 = b0 + 11

    def ligne(titre, cols, ancre):
        ch = LineChart()
        ch.title, ch.height, ch.width = titre, 7.5, 15
        for c in cols:
            ch.add_data(Reference(db, min_col=c, min_row=h0 - 1, max_row=h1), titles_from_data=True)
        ch.set_categories(Reference(db, min_col=1, min_row=h0, max_row=h1))
        db.add_chart(ch, ancre)

    ligne("Valeur du portefeuille et total versé", [2, 3], "I3")
    ligne("Portefeuille et indice de référence", [2, 4], "S3")
    pie = PieChart()
    pie.title, pie.height, pie.width = "Répartition par poche", 7.5, 15
    pie.add_data(Reference(db, min_col=2, min_row=p0 - 1, max_row=p1), titles_from_data=True)
    pie.set_categories(Reference(db, min_col=1, min_row=p0, max_row=p1))
    db.add_chart(pie, "I19")
    bar = BarChart()
    bar.type, bar.title, bar.height, bar.width = "col", "Actuel et cible par poche", 7.5, 15
    for c in (3, 4):
        bar.add_data(Reference(db, min_col=c, min_row=p0 - 1, max_row=p1), titles_from_data=True)
    bar.set_categories(Reference(db, min_col=1, min_row=p0, max_row=p1))
    db.add_chart(bar, "S19")
    pie2 = PieChart()
    pie2.title, pie2.height, pie2.width = "Répartition par enveloppe", 7.5, 15
    pie2.add_data(Reference(db, min_col=2, min_row=e0 - 1, max_row=e1), titles_from_data=True)
    pie2.set_categories(Reference(db, min_col=1, min_row=e0, max_row=e1))
    db.add_chart(pie2, "I35")
    bud = BarChart()
    bud.type, bud.grouping, bud.overlap = "col", "stacked", 100
    bud.title, bud.height, bud.width = "Budget mensuel", 7.5, 15
    for c in (2, 3, 4):
        bud.add_data(Reference(db, min_col=c, min_row=b0 - 1, max_row=b1), titles_from_data=True)
    bud.set_categories(Reference(db, min_col=1, min_row=b0, max_row=b1))
    db.add_chart(bud, "S35")
    obj = BarChart()
    obj.type, obj.title, obj.height, obj.width = "bar", "Progression des objectifs", 7.5, 15
    obj.add_data(Reference(ob, min_col=6, min_row=1, max_row=11), titles_from_data=True)
    obj.set_categories(Reference(ob, min_col=1, min_row=2, max_row=11))
    db.add_chart(obj, "I51")


def id_court(nom, pris):
    base = "".join(c for c in nom.upper() if c.isalnum())[:8] or "LIGNE"
    i, ident = 1, base
    while ident in pris:
        i += 1
        ident = f"{base[:6]}{i}"
    pris.add(ident)
    return ident


def pre_remplir(wb, profil, prenom, poches):
    """Lignes déjà détenues (Actifs + Reprise), objectifs et budget depuis prive/<prenom>/."""
    ac, tr = wb["Actifs"], wb["Transactions"]
    pris = set()
    for i, p in enumerate(lire_csv(Path(profil) / "positions.csv")[:NB_ACTIFS], start=2):
        ident = id_court(p["nom"], pris)
        qte = nombre(p.get("quantite"), 0) or 1
        investi, valeur = nombre(p.get("investi")), nombre(p.get("valeur"))
        yahoo = p.get("ticker_yahoo", "")
        ac[f"A{i}"], ac[f"B{i}"], ac[f"C{i}"] = ident, p["nom"], p.get("isin", "")
        ac[f"D{i}"], ac[f"P{i}"] = ticker_google(yahoo), yahoo
        ac[f"F{i}"] = p["poche"] if p["poche"] in poches else "Autre"
        ac[f"J{i}"], ac[f"K{i}"] = p.get("enveloppe", ""), nombre(p.get("frais_annuels_pct"))
        if not yahoo:  # sans ticker, prix tiré de la dernière valeur connue
            ac[f"Q{i}"] = round(valeur / qte, 4)
            ac[f"O{i}"] = date.fromisoformat(p["date_valeur"]) if p.get("date_valeur") else None
        dv = p.get("date_valeur") or date.today().isoformat()
        tr[f"A{i}"], tr[f"B{i}"], tr[f"C{i}"], tr[f"D{i}"], tr[f"E{i}"] = date.fromisoformat(dv), prenom, p.get("enveloppe", ""), "Reprise", ident
        tr[f"F{i}"], tr[f"G{i}"], tr[f"J{i}"], tr[f"L{i}"] = qte, round(investi / qte, 4), 1, "Prévu"
        tr[f"N{i}"] = "Ligne déjà détenue à l'accueil (prix de revient)"
    ob = wb["Objectifs"]
    for i, o in enumerate(lire_csv(Path(profil) / "objectifs.csv")[:20], start=2):
        ob[f"A{i}"], ob[f"B{i}"] = o["nom"], nombre(o.get("montant"))
        for col, cle in (("C", "date_debut"), ("D", "date_cible")):
            if o.get(cle):
                ob[f"{col}{i}"] = date.fromisoformat(o[cle])
        if o.get("montant_actuel"):
            ob[f"E{i}"] = nombre(o["montant_actuel"])
    bu = wb["Budget"]
    for i, b in enumerate(lire_csv(Path(profil) / "budget.csv")[:120], start=2):
        bu[f"A{i}"], bu[f"B{i}"] = date.fromisoformat(b["mois"][:7] + "-01"), prenom
        for col, cle in (("C", "revenu_net"), ("D", "besoins"), ("E", "envies"), ("F", "epargne_investissement"), ("H", "abonnements")):
            if b.get(cle):
                bu[f"{col}{i}"] = nombre(b[cle])
        bu[f"J{i}"] = b.get("note", "")


def donnees_exemple(wb):
    """Données FICTIVES pour tester les formules (jamais dans le modèle livré)."""
    ac = wb["Actifs"]
    for i, (a, nom, poche, env, ter, prix) in enumerate([
        ("ETFMONDE", "ETF Monde test", "Monde", "PEA", 0.2, 100), ("ETFEU", "ETF Europe test", "Europe", "PEA", 0.2, 50),
        ("BTC", "Bitcoin", "Crypto", "Crypto", 0, 60000)], start=2):
        ac[f"A{i}"], ac[f"B{i}"], ac[f"F{i}"], ac[f"J{i}"], ac[f"K{i}"], ac[f"Q{i}"] = a, nom, poche, env, ter, prix
    tr = wb["Transactions"]
    for i, (d, e, t, a, q, p, f) in enumerate([
        (date(2026, 7, 1), "PEA", "Reprise", "ETFMONDE", 10, 85, 0),
        (date(2026, 8, 5), "PEA", "Versement", "", 1, 600, 0),
        (date(2026, 8, 5), "PEA", "Achat", "ETFMONDE", 5, 95, 1),
        (date(2026, 9, 5), "PEA", "Achat", "ETFEU", 20, 48, 1),
        (date(2026, 9, 20), "Crypto", "Achat", "BTC", 0.01, 55000, 0),
        (date(2026, 10, 1), "PEA", "Dividende", "ETFMONDE", 1, 12, 0)], start=2):
        tr[f"A{i}"], tr[f"B{i}"], tr[f"C{i}"], tr[f"D{i}"], tr[f"E{i}"] = d, "Alice", e, t, a
        tr[f"F{i}"], tr[f"G{i}"], tr[f"H{i}"], tr[f"J{i}"], tr[f"L{i}"] = q, p, f, 1, "Prévu"
    ci = wb["Cibles"]
    for r, v in zip(range(2, 10), [0.6, 0.1, 0.1, 0.1, 0, 0, 0.1, 0]):
        ci[f"B{r}"] = v
    hi = wb["Historique"]
    for i, (m, v, ve) in enumerate([(date(2026, 9, 1), 2500, 2450), (date(2026, 10, 1), 2800, 2750)], start=2):
        hi[f"A{i}"], hi[f"B{i}"], hi[f"C{i}"], hi[f"D{i}"], hi[f"E{i}"], hi[f"H{i}"] = m, "Alice", v, ve - 100, 100, v - 20
    bu = wb["Budget"]
    bu["A2"], bu["B2"], bu["C2"], bu["D2"], bu["E2"], bu["F2"] = date(2026, 10, 1), "Alice", 2000, 1000, 500, 500
    ob = wb["Objectifs"]
    ob["A2"], ob["B2"], ob["C2"], ob["D2"], ob["E2"] = "Apport", 20000, date(2026, 1, 1), date(2028, 1, 1), 3000
    wb["Journal"]["A2"] = date(2026, 6, 1)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    profil = args[args.index("--profil") + 1] if "--profil" in args else None
    libres = [a for a in args if not a.startswith("--") and a != profil]
    sortie = libres[0] if libres else "templates/Portefeuille-complet.xlsx"
    construire(sortie, profil=profil, exemple="--exemple" in args)
    print("Créé :", sortie)
