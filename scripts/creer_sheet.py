"""Génère le classeur du portefeuille (modèle vide, anonyme) : python scripts/creer_sheet.py [sortie.xlsx] [--exemple]"""
import sys
from datetime import date
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, PieChart, Reference
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

BLEU, GRIS, JAUNE = "1F3A5F", "5B6770", "FFF4CC"
H_IN = PatternFill("solid", fgColor=BLEU)
H_CALC = PatternFill("solid", fgColor=GRIS)
CALC = PatternFill("solid", fgColor="F1F3F5")
IN = PatternFill("solid", fgColor=JAUNE)
ROUGE = Font(color="C00000")
VERT = Font(color="2E7D32")
EUR, PCT, DATE = '#,##0.00 "€"', "0.0%", "DD/MM/YYYY"

POCHES = ["USA", "Europe", "Asie émergente", "Monde", "Crypto", "Cash", "Autre"]
ENVELOPPES = ["PEA", "CTO", "Assurance vie", "PER", "Crypto", "Livret"]
LISTES = {
    "K": ("Types d'opération", ["Versement", "Achat", "Vente", "Dividende", "Frais", "Retrait", "Intérêts"]),
    "L": ("Enveloppes", ENVELOPPES),
    "M": ("Types d'actif", ["ETF", "Action", "Crypto", "Obligation", "Fonds euro", "Cash"]),
    "N": ("Poches", POCHES),
    "O": ("Cœur / satellite", ["Cœur", "Satellite"]),
    "P": ("Cap / dist", ["Capitalisant", "Distribuant"]),
    "Q": ("Devises", ["EUR", "USD", "GBP", "CHF"]),
    "R": ("Verdicts du Coach", ["Conforme au plan", "Attendre 24-72 h", "Contraire aux règles"]),
    "S": ("Prévu / hors plan", ["Prévu", "Hors plan"]),
    "T": ("Statut", ["En avance", "Dans les temps", "En retard", "Atteint"]),
}
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


def grise(ws, col, debut, fin, fmt=None):
    for r in range(debut, fin + 1):
        c = ws[f"{col}{r}"]
        c.fill = CALC
        if fmt:
            c.number_format = fmt


def construire(chemin, exemple=False):
    wb = Workbook()

    # ---------- Lisez-moi
    ws = wb.active
    ws.title = "Lisez-moi"
    ws.sheet_properties.tabColor = "999999"
    lignes = [
        "PORTEFEUILLE : mode d'emploi",
        "",
        "Cases JAUNES ou en-têtes BLEUS = tu saisis. En-têtes GRIS et cases grisées = calculé, ne rien écrire dedans.",
        "",
        "1. Paramètres : remplace Prénom 1 et Prénom 2, règle le versement mensuel (une seule fois).",
        "2. Actifs : une ligne par ETF, action ou crypto (ID court unique, ticker, poche, enveloppe, frais).",
        "3. Transactions : à chaque opération, une ligne. On ajoute, on n'efface jamais.",
        "   Pour Versement, Dividende, Frais, Retrait, Intérêts : mets Quantité = 1 et le montant dans Prix unitaire.",
        "4. Positions : une ligne par (personne, actif) que tu détiens. Choisis la personne et l'ID, tout le reste se calcule.",
        "5. Historique : une ligne par mois et par personne (valeur du portefeuille, total versé, valeur de l'indice). 5 minutes par mois.",
        "6. Cibles : saisis ta cible en % par poche. Le tableau te dit combien mettre où au prochain versement.",
        "7. Budget : une ligne par mois. Le taux d'épargne se calcule.",
        "8. Objectifs : tes objectifs chiffrés et datés. La progression se calcule.",
        "9. Journal : les décisions d'achat ou de vente (rempli avec le Coach ou à la main).",
        "10. Revenus et frais, Fiscalité : calculés depuis Transactions et Positions (dividendes, frais, impôt estimé d'une sortie).",
        "11. Idées : toute envie d'achat hors plan attend 30 jours ici avant décision (fiche H).",
        "12. Veille : les infos retenues chaque semaine par la newsletter du dimanche.",
        "13. Dashboard : choisis ton prénom en haut, tout s'affiche (chiffres clés, alertes, à-faire, graphiques).",
        "",
        "Prix : GOOGLEFINANCE fonctionne pour la plupart des ETF cotés. Pour la crypto et les ETF non reconnus, tape le prix à la main dans Actifs, colonne Prix actuel.",
        "Confidentialité : ce fichier est vide. Ne le mets jamais dans un dépôt public.",
    ]
    for l in lignes:
        ws.append([l])
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 130

    # ---------- Dashboard (rempli plus bas, créé ici pour l'ordre)
    db = wb.create_sheet("Dashboard")
    db.sheet_properties.tabColor = "2E7D32"

    # ---------- Paramètres
    pa = wb.create_sheet("Paramètres")
    pa.sheet_properties.tabColor = "F2B01E"
    tete(pa, [("Utilisateur", 16), ("Devise de référence", 12), ("Versement mensuel prévu (€)", 14),
              ("Jour du versement", 10), ("Date d'ouverture du PEA", 14), ("Indice de référence", 18),
              ("Plafond crypto %", 10), ("Plafond par action %", 10)])
    for i, nom in enumerate(["Prénom 1", "Prénom 2"], start=2):
        pa.append([nom, "EUR", 1000, 5, None, "MSCI World", 10, 5])
        for c in "ABCDEFGH":
            pa[f"{c}{i}"].fill = IN
        pa[f"E{i}"].number_format = DATE
        pa[f"C{i}"].number_format = EUR
    for col, (titre, valeurs) in LISTES.items():
        c = pa[f"{col}1"]
        c.value = titre
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = H_CALC
        c.alignment = Alignment(wrap_text=True, horizontal="center")
        pa.column_dimensions[col].width = 18
        for i, v in enumerate(valeurs, start=2):
            pa[f"{col}{i}"] = v
    pa["A6"] = "Les colonnes K à T sont les listes déroulantes du classeur : tu peux les modifier."
    pa["A6"].font = Font(italic=True)

    def L(col, n):
        return f"={PS}!${col}$2:${col}${n + 1}"

    UTIL = f"={PS}!$A$2:$A$3"
    LP, LE, LT, LO = L("N", 7), L("L", 6), L("K", 7), L("S", 2)

    # ---------- Actifs
    ac = wb.create_sheet("Actifs")
    ac.sheet_properties.tabColor = "F2B01E"
    tete(ac, [("ID (code court)", 14), ("Nom", 34), ("ISIN", 16), ("Ticker (GOOGLEFINANCE)", 16), ("Type", 12),
              ("Poche", 16), ("Secteur", 14), ("Devise de cotation", 10), ("Exposition devise", 12),
              ("Enveloppe", 14), ("Frais annuels (TER) %", 11), ("Cap / dist", 14), ("Cœur / satellite", 12),
              ("Prix actuel", 12), ("Date du prix", 12)])
    for r in range(2, 62):
        ac[f"N{r}"] = f'=IF(D{r}="","",IFERROR(GOOGLEFINANCE(D{r}),""))'
        ac[f"N{r}"].number_format = EUR
        ac[f"O{r}"].number_format = DATE
    liste(ac, "E2:E61", L("M", 6))
    liste(ac, "F2:F61", LP)
    liste(ac, "H2:H61", L("Q", 4))
    liste(ac, "I2:I61", "=" + PS + "!$Q$2:$Q$5")
    liste(ac, "J2:J61", LE)
    liste(ac, "L2:L61", L("P", 2))
    liste(ac, "M2:M61", L("O", 2))

    # ---------- Transactions
    tr = wb.create_sheet("Transactions")
    tr.sheet_properties.tabColor = "F2B01E"
    tete(tr, [("Date", 12), ("Utilisateur", 14), ("Enveloppe", 14), ("Type d'opération", 14), ("ID actif", 14),
              ("Quantité", 10), ("Prix unitaire (ou montant)", 13), ("Frais de courtage", 10), ("Devise", 8),
              ("Taux de change (1 si EUR)", 11), ("Montant en €", 14), ("Prévu / hors plan", 12),
              ("Source de l'idée", 18), ("Note", 30)], calc=(11,))
    for r in range(2, 1002):
        tr[f"K{r}"] = (f'=IF(OR(D{r}="",F{r}="",G{r}=""),"",F{r}*G{r}*IF(J{r}="",1,J{r})'
                       f'+IF(D{r}="Achat",N(H{r}),IF(D{r}="Vente",-N(H{r}),0)))')
        tr[f"K{r}"].number_format = EUR
        tr[f"K{r}"].fill = CALC
        tr[f"A{r}"].number_format = DATE
    liste(tr, "B2:B1001", UTIL)
    liste(tr, "C2:C1001", LE)
    liste(tr, "D2:D1001", LT)
    liste(tr, "E2:E1001", "=Actifs!$A$2:$A$61")
    liste(tr, "I2:I1001", L("Q", 4))
    liste(tr, "L2:L1001", LO)

    # ---------- Positions
    po = wb.create_sheet("Positions")
    po.sheet_properties.tabColor = "5B6770"
    tete(po, [("Utilisateur", 14), ("ID actif", 14), ("Nom", 30), ("Poche", 15), ("Enveloppe", 13),
              ("Quantité détenue", 11), ("Prix de revient moyen", 12), ("Montant investi (net)", 13),
              ("Prix actuel", 11), ("Valeur actuelle", 13), ("Plus ou moins-value €", 13),
              ("Plus ou moins-value %", 11), ("Poids %", 9), ("Dividendes reçus", 12),
              ("Frais annuels estimés €", 12)], calc=tuple(range(3, 16)))
    T = "Transactions!"
    for r in range(2, 42):
        crit = f"{T}$B:$B,$A{r},{T}$E:$E,$B{r}"
        ach = f'SUMIFS({T}$F:$F,{crit},{T}$D:$D,"Achat")'
        ven = f'SUMIFS({T}$F:$F,{crit},{T}$D:$D,"Vente")'
        mont_a = f'SUMIFS({T}$K:$K,{crit},{T}$D:$D,"Achat")'
        mont_v = f'SUMIFS({T}$K:$K,{crit},{T}$D:$D,"Vente")'
        idx = lambda col: f'IFERROR(INDEX(Actifs!${col}:${col},MATCH($B{r},Actifs!$A:$A,0)),"")'
        po[f"C{r}"] = f'=IF($B{r}="","",{idx("B")})'
        po[f"D{r}"] = f'=IF($B{r}="","",{idx("F")})'
        po[f"E{r}"] = f'=IF($B{r}="","",{idx("J")})'
        po[f"F{r}"] = f'=IF($B{r}="","",{ach}-{ven})'
        po[f"G{r}"] = f'=IF($B{r}="","",IFERROR({mont_a}/{ach},""))'
        po[f"H{r}"] = f'=IF($B{r}="","",{mont_a}-{mont_v})'
        po[f"I{r}"] = f'=IF($B{r}="","",{idx("N")})'
        po[f"J{r}"] = f'=IF(OR($B{r}="",I{r}=""),"",F{r}*I{r})'
        po[f"K{r}"] = f'=IF(J{r}="","",J{r}-H{r})'
        po[f"L{r}"] = f'=IF(J{r}="","",IFERROR(K{r}/H{r},""))'
        po[f"M{r}"] = f'=IF(J{r}="","",IFERROR(J{r}/SUMIFS($J:$J,$A:$A,$A{r}),""))'
        po[f"N{r}"] = f'=IF($B{r}="","",SUMIFS({T}$K:$K,{crit},{T}$D:$D,"Dividende"))'
        po[f"O{r}"] = f'=IF(J{r}="","",J{r}*N({idx("K")})/100)'
        for c in "GHIJKNO":
            po[f"{c}{r}"].number_format = EUR
        for c in "LM":
            po[f"{c}{r}"].number_format = PCT
        for c in "CDEFGHIJKLMNO":
            po[f"{c}{r}"].fill = CALC
    liste(po, "A2:A41", UTIL)
    liste(po, "B2:B41", "=Actifs!$A$2:$A$61")
    po.conditional_formatting.add("K2:L41", CellIsRule(operator="lessThan", formula=["0"], font=ROUGE))
    po.conditional_formatting.add("K2:L41", CellIsRule(operator="greaterThan", formula=["0"], font=VERT))

    # ---------- Historique
    hi = wb.create_sheet("Historique")
    hi.sheet_properties.tabColor = "F2B01E"
    cols = [("Mois (1er du mois)", 13), ("Utilisateur", 14), ("Valeur totale du portefeuille", 14),
            ("Total versé cumulé", 13), ("Versement du mois", 12), ("Plus-value latente", 13),
            ("Performance du mois %", 12), ("Valeur de l'indice (mêmes versements)", 15)]
    cols += [(f"Valeur {p}", 12) for p in POCHES]
    cols += [("Cash disponible", 12), ("Épargne de précaution", 13)]
    tete(hi, cols, calc=(6, 7))
    for r in range(2, 122):
        hi[f"F{r}"] = f'=IF(OR(C{r}="",D{r}=""),"",C{r}-D{r})'
        hi[f"G{r}"] = (f'=IF(OR(C{r}="",A{r}=""),"",IFERROR((C{r}-N(E{r})-SUMIFS($C:$C,$A:$A,EDATE(A{r},-1),$B:$B,B{r}))'
                       f'/SUMIFS($C:$C,$A:$A,EDATE(A{r},-1),$B:$B,B{r}),""))')
        hi[f"A{r}"].number_format = "MM/YYYY"
        for c in "CDEFH" + "IJKLMNO" + "PQ":
            hi[f"{c}{r}"].number_format = EUR
        hi[f"G{r}"].number_format = PCT
        grise(hi, "F", r, r)
        grise(hi, "G", r, r)
    liste(hi, "B2:B121", UTIL)

    # ---------- Cibles
    ci = wb.create_sheet("Cibles")
    ci.sheet_properties.tabColor = "5B6770"
    tete(ci, [("Utilisateur", 14), ("Poche", 16), ("Cible %", 10), ("Valeur actuelle €", 14), ("Actuel %", 10),
              ("Écart (points)", 11), ("Besoin pour la cible €", 14), ("À verser ce mois €", 14)], calc=(1, 2, 4, 5, 6, 7, 8))
    r = 2
    for u in (2, 3):
        for p in POCHES:
            ci[f"A{r}"] = f"={PS}!$A${u}"
            ci[f"B{r}"] = p
            ci[f"C{r}"].fill = IN
            ci[f"C{r}"].number_format = PCT
            ci[f"D{r}"] = f"=SUMIFS(Positions!$J:$J,Positions!$A:$A,$A{r},Positions!$D:$D,$B{r})"
            ci[f"E{r}"] = f'=IFERROR(D{r}/SUMIFS($D:$D,$A:$A,$A{r}),0)'
            ci[f"F{r}"] = f'=IF(C{r}="","",(E{r}-C{r})*100)'
            ci[f"G{r}"] = (f'=IF(C{r}="",0,MAX(0,C{r}*(SUMIFS($D:$D,$A:$A,$A{r})'
                           f"+INDEX({PS}!$C:$C,MATCH($A{r},{PS}!$A:$A,0)))-D{r}))")
            ci[f"H{r}"] = (f'=IFERROR(G{r}/SUMIFS($G:$G,$A:$A,$A{r})*INDEX({PS}!$C:$C,MATCH($A{r},{PS}!$A:$A,0)),0)')
            for c in "DGH":
                ci[f"{c}{r}"].number_format = EUR
            ci[f"E{r}"].number_format = PCT
            ci[f"F{r}"].number_format = "+0.0;-0.0;0.0"
            r += 1
    ci.conditional_formatting.add("F2:F15", FormulaRule(formula=['AND(ISNUMBER(F2),ABS(F2)>5)'],
                                                        fill=PatternFill("solid", fgColor="F8D7DA")))
    ci["J1"] = "Total des cibles par personne (doit faire 100 %)"
    ci["J1"].font = Font(bold=True)
    ci.column_dimensions["J"].width = 40
    for i, u in enumerate((2, 3), start=2):
        ci[f"J{i}"] = f'={PS}!$A${u}&" : "&TEXT(SUMIFS($C:$C,$A:$A,{PS}!$A${u}),"0.0%")'

    # ---------- Budget
    bu = wb.create_sheet("Budget")
    bu.sheet_properties.tabColor = "F2B01E"
    tete(bu, [("Mois (1er du mois)", 13), ("Utilisateur", 14), ("Revenu net", 13), ("Besoins", 12), ("Envies", 12),
              ("Épargne + investissement", 14), ("Taux d'épargne %", 11), ("Dont abonnements", 12),
              ("Contrôle (reste)", 12), ("Note", 30)], calc=(7, 9))
    for r in range(2, 122):
        bu[f"G{r}"] = f'=IF(OR(C{r}="",F{r}=""),"",IFERROR(F{r}/C{r},""))'
        bu[f"I{r}"] = f'=IF(C{r}="","",C{r}-N(D{r})-N(E{r})-N(F{r}))'
        bu[f"A{r}"].number_format = "MM/YYYY"
        for c in "CDEFHI":
            bu[f"{c}{r}"].number_format = EUR
        bu[f"G{r}"].number_format = PCT
        grise(bu, "G", r, r)
        grise(bu, "I", r, r)
    liste(bu, "B2:B121", UTIL)
    bu.conditional_formatting.add("G2:G121", CellIsRule(operator="greaterThanOrEqual", formula=["0.3"], font=VERT))
    bu.conditional_formatting.add("G2:G121", FormulaRule(formula=['AND(ISNUMBER(G2),G2<0.2)'], font=ROUGE))
    bu.conditional_formatting.add("I2:I121", FormulaRule(formula=['AND(ISNUMBER(I2),ABS(I2)>1)'], font=ROUGE))

    # ---------- Objectifs
    ob = wb.create_sheet("Objectifs")
    ob.sheet_properties.tabColor = "F2B01E"
    tete(ob, [("Utilisateur", 14), ("Objectif", 28), ("Montant cible", 14), ("Date de début", 12), ("Date cible", 12),
              ("Montant actuel", 14), ("Progression %", 11), ("Mois restants", 10),
              ("Versement mensuel nécessaire (sans rendement)", 18), ("Statut", 14)], calc=(7, 8, 9, 10))
    for r in range(2, 22):
        ob[f"G{r}"] = f'=IF(OR(C{r}="",F{r}=""),"",MIN(1,F{r}/C{r}))'
        ob[f"H{r}"] = f'=IF(E{r}="","",MAX(0,ROUND((E{r}-TODAY())/30.44,0)))'
        ob[f"I{r}"] = f'=IF(OR(C{r}="",H{r}="",H{r}=0),"",MAX(0,(C{r}-N(F{r}))/H{r}))'
        ob[f"J{r}"] = (f'=IF(OR(G{r}="",D{r}="",E{r}=""),"",IF(G{r}>=1,"Atteint",'
                       f'IF(G{r}>=(TODAY()-D{r})/(E{r}-D{r})+0.1,"En avance",IF(G{r}>=(TODAY()-D{r})/(E{r}-D{r})-0.05,"Dans les temps","En retard"))))')
        for c in "CFI":
            ob[f"{c}{r}"].number_format = EUR
        ob[f"G{r}"].number_format = PCT
        for c in "DE":
            ob[f"{c}{r}"].number_format = DATE
        for c in "GHIJ":
            ob[f"{c}{r}"].fill = CALC
    liste(ob, "A2:A21", UTIL)
    liste(ob, "J2:J21", L("T", 4))
    for txt, coul in (("En retard", ROUGE), ("Atteint", VERT), ("En avance", VERT)):
        ob.conditional_formatting.add("J2:J21", CellIsRule(operator="equal", formula=[f'"{txt}"'], font=coul))

    # ---------- Journal
    jo = wb.create_sheet("Journal")
    jo.sheet_properties.tabColor = "F2B01E"
    tete(jo, [("Date", 12), ("Utilisateur", 14), ("Action (achat / vente)", 12), ("ID actif", 14), ("Montant €", 12),
              ("Pourquoi", 34), ("Pourquoi maintenant", 26), ("Ce qui invaliderait l'idée", 30), ("Source de l'idée", 18),
              ("Émotion (1 à 10)", 10), ("Verdict du Coach", 18), ("Décision finale", 14),
              ("Date du bilan à 3 mois", 13), ("Résultat à 3 mois", 22), ("Leçon", 34)], calc=(13,))
    for r in range(2, 302):
        jo[f"M{r}"] = f'=IF(A{r}="","",A{r}+91)'
        jo[f"M{r}"].number_format = DATE
        jo[f"M{r}"].fill = CALC
        jo[f"A{r}"].number_format = DATE
        jo[f"E{r}"].number_format = EUR
    liste(jo, "B2:B301", UTIL)
    liste(jo, "C2:C301", '"Achat,Vente,Autre"')
    liste(jo, "D2:D301", "=Actifs!$A$2:$A$61")
    liste(jo, "J2:J301", '"1,2,3,4,5,6,7,8,9,10"')
    liste(jo, "K2:K301", L("R", 3))
    liste(jo, "L2:L301", '"Acheté,Vendu,Reporté,Abandonné"')


    # ---------- Revenus et frais (par année et par enveloppe)
    rf = wb.create_sheet("Revenus et frais")
    rf.sheet_properties.tabColor = "5B6770"
    tete(rf, [("Utilisateur", 14), ("Année", 8), ("Enveloppe", 14), ("Versements €", 13), ("Retraits €", 12),
              ("Dividendes €", 12), ("Intérêts €", 12), ("Frais prélevés €", 12), ("Courtage payé €", 12),
              ("Revenus nets de frais €", 14)], calc=tuple(range(1, 11)))
    r = 2
    for u in (2, 3):
        for an in range(2025, 2031):
            for env in ENVELOPPES:
                rf[f"A{r}"], rf[f"B{r}"], rf[f"C{r}"] = f"={PS}!$A${u}", an, env
                crit = (f'{T}$B:$B,$A{r},{T}$C:$C,$C{r},{T}$A:$A,">="&DATE($B{r},1,1),'
                        f'{T}$A:$A,"<="&DATE($B{r},12,31)')
                for col, typ in (("D", "Versement"), ("E", "Retrait"), ("F", "Dividende"), ("G", "Intérêts"), ("H", "Frais")):
                    rf[f"{col}{r}"] = f'=SUMIFS({T}$K:$K,{crit},{T}$D:$D,"{typ}")'
                rf[f"I{r}"] = f"=SUMIFS({T}$H:$H,{crit})"
                rf[f"J{r}"] = f"=F{r}+G{r}-H{r}-I{r}"
                for c in "DEFGHIJ":
                    rf[f"{c}{r}"].number_format = EUR
                r += 1
    rf.auto_filter.ref = f"A1:J{r - 1}"
    rf["L1"] = "Filtre sur Utilisateur et Année. Les montants viennent de Transactions (rien à saisir ici)."
    rf["L1"].font = Font(italic=True)

    # ---------- Fiscalité (estimation si tout était vendu aujourd'hui)
    fi = wb.create_sheet("Fiscalité")
    fi.sheet_properties.tabColor = "5B6770"
    tete(fi, [("Utilisateur", 14), ("Enveloppe", 14), ("Valeur actuelle €", 14), ("Investi net €", 13),
              ("Plus-value latente €", 14), ("Taux estimé sur le gain %", 12), ("Impôt estimé si vente totale €", 15),
              ("Note", 60)], calc=(1, 2, 3, 4, 5, 7, 8))
    TAUX_ENV = {
        "PEA": ('=IF(IFERROR(DATEDIF(INDEX({ps}!$E:$E,MATCH($A{r},{ps}!$A:$A,0)),TODAY(),"Y"),0)>=5,0.186,0.314)',
                "Après 5 ans : prélèvements sociaux seuls (18,6 %). Avant : 31,4 % et clôture du plan. Saisir la date d'ouverture dans Paramètres."),
        "CTO": ("0.314", "Prélèvement forfaitaire unique 2026 : 12,8 % + 18,6 %. Moins-values imputables non comptées."),
        "Assurance vie": ("0.172", "Minimum : prélèvements sociaux 17,2 %. Après 8 ans, abattement 4 600 € (9 200 € en couple) puis 7,5 %. Calcul exact : scripts/fiscalite.py."),
        "PER": ("", "Dépend de la tranche d'imposition et des déductions passées : à voir avec le Stratège."),
        "Crypto": ("0.314", "Flat tax sur les cessions contre euros, à vérifier chaque année (fiche C)."),
        "Livret": ("0", "Livrets réglementés : exonérés."),
    }
    r = 2
    for u in (2, 3):
        for env in ENVELOPPES:
            taux, note = TAUX_ENV[env]
            fi[f"A{r}"], fi[f"B{r}"] = f"={PS}!$A${u}", env
            fi[f"C{r}"] = f"=SUMIFS(Positions!$J:$J,Positions!$A:$A,$A{r},Positions!$E:$E,$B{r})"
            fi[f"D{r}"] = f"=SUMIFS(Positions!$H:$H,Positions!$A:$A,$A{r},Positions!$E:$E,$B{r})"
            fi[f"E{r}"] = f"=C{r}-D{r}"
            fi[f"F{r}"] = taux.format(ps=PS, r=r) if taux.startswith("=") else (float(taux) if taux else None)
            fi[f"F{r}"].fill = IN
            fi[f"G{r}"] = f'=IF(F{r}="","",MAX(0,E{r})*F{r})'
            fi[f"H{r}"] = note
            for c in "CDEG":
                fi[f"{c}{r}"].number_format = EUR
            fi[f"F{r}"].number_format = PCT
            r += 1
    fi[f"A{r + 1}"] = ("Estimation indicative, taux 2026 à revérifier chaque année (fiche C). "
                       "Aucune vente n'est recommandée ici : c'est le coût d'une sortie, pas un conseil.")
    fi[f"A{r + 1}"].font = Font(italic=True)
    fi.conditional_formatting.add("E2:E13", CellIsRule(operator="lessThan", formula=["0"], font=ROUGE))

    # ---------- Idées (liste d'attente avant tout achat hors plan, fiche H)
    idx_ = wb.create_sheet("Idées")
    idx_.sheet_properties.tabColor = "F2B01E"
    tete(idx_, [("Date", 12), ("Utilisateur", 14), ("Idée (actif ou thème)", 26), ("Ticker", 12),
                ("Source de l'idée", 22), ("Type de source", 16), ("Thèse en une phrase", 40),
                ("Ce qui invaliderait l'idée", 30), ("Émotion (1 à 10)", 10), ("Verdict du Coach", 18),
                ("Date de revue (J+30)", 13), ("Décision après revue", 16), ("Note", 30)], calc=(11,))
    for r in range(2, 202):
        idx_[f"A{r}"].number_format = DATE
        idx_[f"K{r}"] = f'=IF(A{r}="","",A{r}+30)'
        idx_[f"K{r}"].number_format = DATE
        idx_[f"K{r}"].fill = CALC
    liste(idx_, "B2:B201", UTIL)
    liste(idx_, "F2:F201", '"Source fiable (presse, AMF),Réseau social,Ami ou famille,Newsletter,Forum,Autre"')
    liste(idx_, "I2:I201", '"1,2,3,4,5,6,7,8,9,10"')
    liste(idx_, "J2:J201", L("R", 3))
    liste(idx_, "L2:L201", '"Acheter (dans le plan),Abandonner,Reporter"')
    idx_.conditional_formatting.add("K2:K201", FormulaRule(formula=['AND(ISNUMBER(K2),K2<=TODAY(),L2="")'],
                                                           fill=PatternFill("solid", fgColor="F8D7DA")))

    # ---------- Veille (une ligne par info retenue, remplie par la newsletter du dimanche)
    ve = wb.create_sheet("Veille")
    ve.sheet_properties.tabColor = "F2B01E"
    tete(ve, [("Semaine (dimanche)", 13), ("Thème", 18), ("Importance", 13), ("Fait (chiffré)", 50),
              ("Source et date", 30), ("Positions concernées", 22), ("Impact estimé", 30), ("Action", 30)])
    for r in range(2, 502):
        ve[f"A{r}"].number_format = DATE
    liste(ve, "B2:B501", '"Marchés,Taux et banques centrales,Inflation et emploi,Change,Entreprises,Crypto,Fiscalité et réglementation,Autre"')
    liste(ve, "C2:C501", '"À ignorer,À surveiller,À agir"')
    ve.conditional_formatting.add("C2:C501", CellIsRule(operator="equal", formula=['"À agir"'], font=ROUGE))

    # ---------- Dashboard
    db["A1"] = "TABLEAU DE BORD"
    db["A1"].font = Font(bold=True, size=16, color=BLEU)
    db["A2"] = "Personne :"
    db["A2"].font = Font(bold=True)
    db["B2"] = f"={PS}!A2"
    db["B2"].fill = IN
    db["B2"].font = Font(bold=True, size=12)
    liste(db, "B2", UTIL)
    U = "$B$2"

    def DERNIER(feuille):
        return f"_xlfn.MAXIFS({feuille}!$A:$A,{feuille}!$B:$B,{U})"
    kpis = [
        ("Patrimoine (positions)", f"=SUMIFS(Positions!$J:$J,Positions!$A:$A,{U})", EUR),
        ("Montant investi net", f"=SUMIFS(Positions!$H:$H,Positions!$A:$A,{U})", EUR),
        ("Plus-value latente", f"=SUMIFS(Positions!$K:$K,Positions!$A:$A,{U})", EUR),
        ("Performance", f'=IFERROR(C5/B5,0)', PCT),
        ("Taux d'épargne (dernier mois)",
         f'=IFERROR(SUMIFS(Budget!$G:$G,Budget!$B:$B,{U},Budget!$A:$A,{DERNIER("Budget")}),"")', PCT),
        ("Frais annuels estimés", f"=SUMIFS(Positions!$O:$O,Positions!$A:$A,{U})", EUR),
        ("Décisions hors plan", f'=COUNTIFS(Transactions!$B:$B,{U},Transactions!$L:$L,"Hors plan")', "0"),
        ("Écart avec l'indice (dernier mois)",
         f'=IFERROR(SUMIFS(Historique!$C:$C,Historique!$B:$B,{U},Historique!$A:$A,{DERNIER("Historique")})'
         f'-SUMIFS(Historique!$H:$H,Historique!$B:$B,{U},Historique!$A:$A,{DERNIER("Historique")}),"")', EUR),
        ("Épargne de précaution (mois de besoins)",
         f'=IFERROR(SUMIFS(Historique!$Q:$Q,Historique!$B:$B,{U},Historique!$A:$A,{DERNIER("Historique")})'
         f'/AVERAGEIFS(Budget!$D:$D,Budget!$B:$B,{U},Budget!$D:$D,">0"),"")', "0.0"),
        ("Versé sur le PEA",
         f'=SUMIFS(Transactions!$K:$K,Transactions!$B:$B,{U},Transactions!$C:$C,"PEA",Transactions!$D:$D,"Versement")', EUR),
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
    for i in range(1, 11):
        db.column_dimensions[get_column_letter(i)].width = 17
    db.column_dimensions["A"].width = 20

    db["A7"] = "À FAIRE CE MOIS"
    db["A7"].font = Font(bold=True, size=12, color=BLEU)
    db["A8"] = (f'="Versement prévu : "&TEXT(IFERROR(INDEX({PS}!$C:$C,MATCH({U},{PS}!$A:$A,0)),0),"#,##0")'
                f'&" € : à répartir selon la colonne « À verser » ci-dessous."')
    db["A9"] = '=IFERROR("Poche la plus sous-pondérée : "&INDEX($A$18:$A$24,MATCH(MIN($E$18:$E$24),$E$18:$E$24,0))&" ("&TEXT(MIN($E$18:$E$24),"+0.0;-0.0")&" pts)","")'
    db["A10"] = '=IFERROR("Poche la plus sur-pondérée : "&INDEX($A$18:$A$24,MATCH(MAX($E$18:$E$24),$E$18:$E$24,0))&" ("&TEXT(MAX($E$18:$E$24),"+0.0;-0.0")&" pts)","")'
    db["A11"] = (f'=IF(SUMIFS(Positions!$J:$J,Positions!$A:$A,{U},Positions!$D:$D,"Crypto")'
                 f'/MAX(1,SUMIFS(Positions!$J:$J,Positions!$A:$A,{U}))'
                 f'>IFERROR(INDEX({PS}!$G:$G,MATCH({U},{PS}!$A:$A,0)),10)/100,'
                 f'"ALERTE : la crypto dépasse le plafond fixé.","Crypto dans la limite fixée.")')
    db["A12"] = (f'=COUNTIFS(Journal!$B:$B,{U},Journal!$M:$M,"<="&TODAY(),Journal!$N:$N,"")'
                 f'&" bilan(s) de décision à faire (3 mois écoulés)."')
    db["A13"] = (f'=IF(COUNTIFS(Historique!$A:$A,DATE(YEAR(TODAY()),MONTH(TODAY()),1),Historique!$B:$B,{U})=0,'
                 f'"Historique du mois à saisir (feuille Historique).","Historique du mois saisi.")')
    db["A14"] = (f'=IF(COUNTIFS(Budget!$A:$A,DATE(YEAR(TODAY()),MONTH(TODAY()),1),Budget!$B:$B,{U})=0,'
                 f'"Budget du mois à saisir (feuille Budget).","Budget du mois saisi.")')
    db["H8"] = ('=IF(I5="","Épargne de précaution : saisir le cash de côté dans Historique (colonne Q).",'
                'IF(I5<3,"ALERTE : moins de 3 mois de besoins de côté (fiche A).",'
                '"Épargne de précaution : "&TEXT(I5,"0.0")&" mois de besoins."))')
    db["H9"] = ('=IF(J5>=150000,"PEA : plafond de 150 000 € de versements atteint.",'
                '"PEA : "&TEXT(150000-J5,"#,##0")&" € de versements encore possibles.")')
    db["H10"] = f'=COUNTIFS(Idées!$B:$B,{U},Idées!$K:$K,"<="&TODAY(),Idées!$L:$L,"")&" idée(s) de la liste à revoir (feuille Idées)."'
    db["H11"] = f'=COUNTIFS(Veille!$C:$C,"À agir",Veille!$A:$A,">="&(TODAY()-7))&" point(s) « à agir » dans la veille de la semaine."'
    db["A15"] = f'=IF(ABS(SUMIFS(Cibles!$C:$C,Cibles!$A:$A,{U})-1)>0.001,"Tes cibles ne font pas 100 % (feuille Cibles).","Cibles OK.")'

    # tables
    def entete(row, titres):
        for i, t in enumerate(titres, start=1):
            c = db.cell(row, i, t)
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = H_CALC
            c.alignment = Alignment(horizontal="center", wrap_text=True)

    db["A16"] = "Répartition par poche"
    db["A16"].font = Font(bold=True, size=12, color=BLEU)
    entete(17, ["Poche", "Valeur €", "Actuel %", "Cible %", "Écart (pts)", "À verser €"])
    for i in range(7):
        r = 18 + i
        db[f"A{r}"] = f"={PS}!$N${2 + i}"
        db[f"B{r}"] = f"=SUMIFS(Cibles!$D:$D,Cibles!$A:$A,{U},Cibles!$B:$B,$A{r})"
        db[f"C{r}"] = f"=SUMIFS(Cibles!$E:$E,Cibles!$A:$A,{U},Cibles!$B:$B,$A{r})"
        db[f"D{r}"] = f"=SUMIFS(Cibles!$C:$C,Cibles!$A:$A,{U},Cibles!$B:$B,$A{r})"
        db[f"E{r}"] = f"=(C{r}-D{r})*100"
        db[f"F{r}"] = f"=SUMIFS(Cibles!$H:$H,Cibles!$A:$A,{U},Cibles!$B:$B,$A{r})"
        db[f"B{r}"].number_format = EUR
        db[f"F{r}"].number_format = EUR
        db[f"C{r}"].number_format = PCT
        db[f"D{r}"].number_format = PCT
        db[f"E{r}"].number_format = "+0.0;-0.0;0.0"
    db.conditional_formatting.add("E18:E24", FormulaRule(formula=["ABS(E18)>5"], fill=PatternFill("solid", fgColor="F8D7DA")))

    db["A26"] = "Répartition par enveloppe"
    db["A26"].font = Font(bold=True, size=12, color=BLEU)
    entete(27, ["Enveloppe", "Valeur €", "Poids %"])
    for i in range(6):
        r = 28 + i
        db[f"A{r}"] = f"={PS}!$L${2 + i}"
        db[f"B{r}"] = f"=SUMIFS(Positions!$J:$J,Positions!$A:$A,{U},Positions!$E:$E,$A{r})"
        db[f"C{r}"] = f"=IFERROR(B{r}/SUM($B$28:$B$33),0)"
        db[f"B{r}"].number_format = EUR
        db[f"C{r}"].number_format = PCT

    db["A35"] = "Historique (24 derniers mois)"
    db["A35"].font = Font(bold=True, size=12, color=BLEU)
    entete(36, ["Mois", "Valeur portefeuille", "Total versé", "Valeur indice", "Perf du mois"])
    for i in range(24):
        r = 37 + i
        db[f"A{r}"] = f"=EDATE(DATE(YEAR(TODAY()),MONTH(TODAY()),1),{i - 23})"
        db[f"A{r}"].number_format = "MM/YYYY"
        for col, src in (("B", "C"), ("C", "D"), ("D", "H"), ("E", "G")):
            db[f"{col}{r}"] = f"=IF(COUNTIFS(Historique!$A:$A,$A{r},Historique!$B:$B,{U})=0,NA(),SUMIFS(Historique!${src}:${src},Historique!$A:$A,$A{r},Historique!$B:$B,{U}))"
            db[f"{col}{r}"].number_format = PCT if col == "E" else EUR

    db["A62"] = "Budget (12 derniers mois)"
    db["A62"].font = Font(bold=True, size=12, color=BLEU)
    entete(63, ["Mois", "Besoins", "Envies", "Épargne + invest."])
    for i in range(12):
        r = 64 + i
        db[f"A{r}"] = f"=EDATE(DATE(YEAR(TODAY()),MONTH(TODAY()),1),{i - 11})"
        db[f"A{r}"].number_format = "MM/YYYY"
        for col, src in (("B", "D"), ("C", "E"), ("D", "F")):
            db[f"{col}{r}"] = f"=SUMIFS(Budget!${src}:${src},Budget!$A:$A,$A{r},Budget!$B:$B,{U})"
            db[f"{col}{r}"].number_format = EUR

    # graphiques
    def ligne(titre, cols, ancre, debut=36, fin=60):
        ch = LineChart()
        ch.title, ch.height, ch.width = titre, 7.5, 15
        for c in cols:
            ch.add_data(Reference(db, min_col=c, min_row=debut, max_row=fin), titles_from_data=True)
        ch.set_categories(Reference(db, min_col=1, min_row=debut + 1, max_row=fin))
        db.add_chart(ch, ancre)

    ligne("Valeur du portefeuille et total versé", [2, 3], "L3")
    ligne("Portefeuille et indice de référence", [2, 4], "V3")

    pie = PieChart()
    pie.title, pie.height, pie.width = "Répartition par poche", 7.5, 15
    pie.add_data(Reference(db, min_col=2, min_row=17, max_row=24), titles_from_data=True)
    pie.set_categories(Reference(db, min_col=1, min_row=18, max_row=24))
    db.add_chart(pie, "L19")

    bar = BarChart()
    bar.type, bar.title, bar.height, bar.width = "col", "Actuel et cible par poche", 7.5, 15
    for c in (3, 4):
        bar.add_data(Reference(db, min_col=c, min_row=17, max_row=24), titles_from_data=True)
    bar.set_categories(Reference(db, min_col=1, min_row=18, max_row=24))
    db.add_chart(bar, "V19")

    pie2 = PieChart()
    pie2.title, pie2.height, pie2.width = "Répartition par enveloppe", 7.5, 15
    pie2.add_data(Reference(db, min_col=2, min_row=27, max_row=33), titles_from_data=True)
    pie2.set_categories(Reference(db, min_col=1, min_row=28, max_row=33))
    db.add_chart(pie2, "L35")

    bud = BarChart()
    bud.type, bud.grouping, bud.overlap = "col", "stacked", 100
    bud.title, bud.height, bud.width = "Budget mensuel", 7.5, 15
    for c in (2, 3, 4):
        bud.add_data(Reference(db, min_col=c, min_row=63, max_row=75), titles_from_data=True)
    bud.set_categories(Reference(db, min_col=1, min_row=64, max_row=75))
    db.add_chart(bud, "V35")

    obj = BarChart()
    obj.type, obj.title, obj.height, obj.width = "bar", "Progression des objectifs", 7.5, 15
    obj.add_data(Reference(ob, min_col=7, min_row=1, max_row=11), titles_from_data=True)
    obj.set_categories(Reference(ob, min_col=2, min_row=2, max_row=11))
    db.add_chart(obj, "L51")

    if exemple:
        donnees_exemple(wb)
    wb.save(chemin)


def donnees_exemple(wb):
    """Données FICTIVES pour tester les formules (jamais dans le modèle livré)."""
    wb["Paramètres"]["A2"], wb["Paramètres"]["A3"] = "Alice", "Bruno"
    ac = wb["Actifs"]
    for i, (a, nom, poche, env, ter, prix) in enumerate([
        ("ETFUSA", "ETF USA test", "USA", "PEA", 0.1, 100), ("ETFEU", "ETF Europe test", "Europe", "PEA", 0.2, 50),
        ("BTC", "Bitcoin", "Crypto", "Crypto", 0, 60000)], start=2):
        ac[f"A{i}"], ac[f"B{i}"], ac[f"F{i}"], ac[f"J{i}"], ac[f"K{i}"], ac[f"N{i}"] = a, nom, poche, env, ter, prix
    tr = wb["Transactions"]
    for i, (d, u, e, t, a, q, p, f) in enumerate([
        (date(2026, 8, 5), "Alice", "PEA", "Achat", "ETFUSA", 10, 90, 1),
        (date(2026, 9, 5), "Alice", "PEA", "Achat", "ETFUSA", 5, 95, 1),
        (date(2026, 9, 5), "Alice", "PEA", "Achat", "ETFEU", 20, 48, 1),
        (date(2026, 9, 20), "Alice", "Crypto", "Achat", "BTC", 0.01, 55000, 0),
        (date(2026, 10, 1), "Alice", "PEA", "Dividende", "ETFUSA", 1, 12, 0),
        (date(2026, 9, 6), "Bruno", "PEA", "Achat", "ETFUSA", 3, 97, 0)], start=2):
        tr[f"A{i}"], tr[f"B{i}"], tr[f"C{i}"], tr[f"D{i}"], tr[f"E{i}"] = d, u, e, t, a
        tr[f"F{i}"], tr[f"G{i}"], tr[f"H{i}"], tr[f"J{i}"], tr[f"L{i}"] = q, p, f, 1, "Prévu"
    po = wb["Positions"]
    for i, (u, a) in enumerate([("Alice", "ETFUSA"), ("Alice", "ETFEU"), ("Alice", "BTC"), ("Bruno", "ETFUSA")], start=2):
        po[f"A{i}"], po[f"B{i}"] = u, a
    ci = wb["Cibles"]
    for r, v in zip(range(2, 9), [0.4, 0.3, 0.1, 0.1, 0.1, 0, 0]):
        ci[f"C{r}"] = v
    hi = wb["Historique"]
    for i, (m, v, ve) in enumerate([(date(2026, 9, 1), 1500, 1450), (date(2026, 10, 1), 1800, 1750)], start=2):
        hi[f"A{i}"], hi[f"B{i}"], hi[f"C{i}"], hi[f"D{i}"], hi[f"E{i}"], hi[f"H{i}"] = m, "Alice", v, ve - 100, 100, v - 20
    bu = wb["Budget"]
    bu["A2"], bu["B2"], bu["C2"], bu["D2"], bu["E2"], bu["F2"] = date(2026, 10, 1), "Alice", 2000, 1000, 500, 500
    ob = wb["Objectifs"]
    ob["A2"], ob["B2"], ob["C2"], ob["D2"], ob["E2"], ob["F2"] = "Alice", "Apport", 20000, date(2026, 1, 1), date(2028, 1, 1), 3000
    jo = wb["Journal"]
    jo["A2"], jo["B2"] = date(2026, 6, 1), "Alice"
    tr["A8"], tr["B8"], tr["C8"], tr["D8"], tr["E8"], tr["F8"], tr["G8"], tr["J8"] = (
        date(2026, 8, 1), "Alice", "PEA", "Versement", "", 1, 1200, 1)
    hi["P2"], hi["Q2"], hi["P3"], hi["Q3"] = 300, 4500, 250, 4600
    idees = wb["Idées"]
    idees["A2"], idees["B2"], idees["C2"], idees["F2"], idees["I2"] = date(2026, 9, 15), "Alice", "Action test", "Réseau social", 8
    ve = wb["Veille"]
    ve["A2"], ve["B2"], ve["C2"], ve["D2"] = date(2026, 10, 25), "Marchés", "À surveiller", "Ligne fictive de test"
    wb["Paramètres"]["E2"] = date(2019, 5, 1)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sortie = args[0] if args else "templates/Portefeuille-complet.xlsx"
    construire(sortie, exemple="--exemple" in sys.argv)
    print("Créé :", sortie)
