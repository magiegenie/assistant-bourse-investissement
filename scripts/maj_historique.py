"""Collecte et met à jour la base historique des marchés (mensuelle) dans donnees/historique/.

Usage :
  python scripts/maj_historique.py              collecte tout (indices et macro), puis lance les contrôles
  python scripts/maj_historique.py --controles  contrôles qualité seulement, sur les CSV existants
  python scripts/maj_historique.py --liens      vérifie les sources de la frise d'événements (evenements.csv)

Sources (testées le 31/10/2026, détail dans donnees/historique/SOURCES.md) :
  - Yahoo Finance, API « chart » quotidienne, clôture du dernier jour de bourse de chaque mois ;
  - STOXX, fichier officiel hbrbcpe.txt (STOXX Europe 600 et Euro Stoxx 50, de 1986 à 2016) ;
  - FRED (Réserve fédérale de Saint-Louis), CSV publics sans clé, pour la macro.
Bibliothèque standard uniquement. Une valeur déjà présente qui change est signalée, jamais remplacée en silence.
Usage personnel : ces données ne doivent pas être publiées (dépôt privé).
"""
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
DOSSIER = RACINE / "donnees" / "historique"
AGENT = {"User-Agent": "Mozilla/5.0 (assistant-bourse-investissement, usage personnel)"}
AUJOURDHUI = date.today().isoformat()

# Chaque indice : sources dans l'ordre de priorité. Une source plus prioritaire l'emporte sur les mois communs.
INDICES = [
    {"id": "MSCI_WORLD", "nom": "MSCI World", "zone": "Monde développé", "devise": "USD", "type": "prix",
     "fournisseur": "MSCI", "sources": [("yahoo", "^990100-USD-STRD", "close")],
     "remarques": "Prix seul, en dollars. Les versions dividendes réinvestis et en euros ne sont pas accessibles librement (site MSCI protégé contre les robots)."},
    {"id": "MSCI_ACWI", "nom": "MSCI ACWI (monde entier)", "zone": "Monde", "devise": "USD", "type": "prix",
     "fournisseur": "MSCI", "sources": [("yahoo", "^892400-USD-STRD", "close")],
     "remarques": "Pays développés et émergents. Prix seul, en dollars."},
    {"id": "MSCI_EM", "nom": "MSCI Emerging Markets (via fonds Vanguard)", "zone": "Émergents", "devise": "USD", "type": "dividendes réinvestis (fonds)",
     "fournisseur": "Vanguard (fonds VEIEX)", "sources": [("yahoo", "VEIEX", "adjclose")],
     "remarques": "Approximation : fonds indiciel Vanguard Emerging Markets, cours ajusté des dividendes, frais déduits. Il suivait le MSCI EM, puis un indice FTSE Emerging à partir de 2013. L'indice MSCI EM lui-même n'est pas accessible librement."},
    {"id": "SP500", "nom": "S&P 500", "zone": "États-Unis", "devise": "USD", "type": "prix",
     "fournisseur": "S&P Dow Jones Indices", "sources": [("yahoo", "^GSPC", "close")], "remarques": "Prix seul."},
    {"id": "SP500_TR", "nom": "S&P 500 dividendes réinvestis", "zone": "États-Unis", "devise": "USD", "type": "dividendes réinvestis",
     "fournisseur": "S&P Dow Jones Indices", "sources": [("yahoo", "^SP500TR", "close")], "remarques": "Version « total return »."},
    {"id": "NASDAQ100", "nom": "Nasdaq-100", "zone": "États-Unis", "devise": "USD", "type": "prix",
     "fournisseur": "Nasdaq", "sources": [("yahoo", "^NDX", "close")], "remarques": "Les 100 plus grosses valeurs non financières du Nasdaq. Prix seul."},
    {"id": "NASDAQ_COMP", "nom": "Nasdaq Composite", "zone": "États-Unis", "devise": "USD", "type": "prix",
     "fournisseur": "Nasdaq", "sources": [("yahoo", "^IXIC", "close")], "remarques": "Toutes les valeurs du Nasdaq, plus long historique que le Nasdaq-100. Prix seul."},
    {"id": "DOW_JONES", "nom": "Dow Jones Industrial Average", "zone": "États-Unis", "devise": "USD", "type": "prix",
     "fournisseur": "S&P Dow Jones Indices", "sources": [("yahoo", "^DJI", "close"), ("measuringworth", "DJA")],
     "remarques": "30 valeurs, pondéré par le prix. Yahoo Finance depuis 1992 ; avant, série MeasuringWorth (Samuel H. Williamson, « Daily Closing Value of the Dow Jones Average, 1885 to Present »), raccordée par MeasuringWorth avant 1914."},
    {"id": "STOXX600", "nom": "STOXX Europe 600", "zone": "Europe", "devise": "EUR", "type": "prix",
     "fournisseur": "STOXX", "sources": [("stoxx", "SXXP"), ("yahoo", "^STOXX", "close")],
     "remarques": "Fichier officiel STOXX de 1986 à 2016, puis Yahoo Finance. Prix seul."},
    {"id": "EUROSTOXX50", "nom": "Euro Stoxx 50", "zone": "Zone euro", "devise": "EUR", "type": "prix",
     "fournisseur": "STOXX", "sources": [("stoxx", "SX5E"), ("yahoo", "^STOXX50E", "close")],
     "remarques": "Fichier officiel STOXX de 1986 à 2016, puis Yahoo Finance. Prix seul."},
    {"id": "CAC40", "nom": "CAC 40", "zone": "France", "devise": "EUR", "type": "prix",
     "fournisseur": "Euronext", "sources": [("yahoo", "^FCHI", "close")],
     "remarques": "Base 1 000 au 31/12/1987 ; historique libre depuis mars 1990. Prix seul (francs avant 1999, niveau d'indice inchangé)."},
    {"id": "DAX", "nom": "DAX", "zone": "Allemagne", "devise": "EUR", "type": "dividendes réinvestis",
     "fournisseur": "Deutsche Börse", "sources": [("yahoo", "^GDAXI", "close")],
     "remarques": "Attention : le DAX est un indice de performance, dividendes réinvestis, contrairement au CAC 40."},
    {"id": "FTSE100", "nom": "FTSE 100", "zone": "Royaume-Uni", "devise": "GBP", "type": "prix",
     "fournisseur": "FTSE Russell", "sources": [("yahoo", "^FTSE", "close")], "remarques": "Prix seul, en livres sterling."},
    {"id": "NIKKEI225", "nom": "Nikkei 225", "zone": "Japon", "devise": "JPY", "type": "prix",
     "fournisseur": "Nikkei", "sources": [("yahoo", "^N225", "close")], "remarques": "Prix seul, en yens. Pondéré par le prix."},
    {"id": "HANG_SENG", "nom": "Hang Seng", "zone": "Hong Kong", "devise": "HKD", "type": "prix",
     "fournisseur": "Hang Seng Indexes", "sources": [("yahoo", "^HSI", "close")], "remarques": "Prix seul, en dollars de Hong Kong."},
]

# Indices de cours des actions de l'OCDE (via FRED) : un « minimum » de prix sur longue période pour les marchés
# dont l'indice phare n'a pas d'historique libre ancien. Base 2015 = 100, MOYENNE du mois (pas une clôture) :
# à ne pas raccorder aux indices ci-dessus, à utiliser pour les tendances longues.
OCDE = [
    ("OCDE_FRANCE", "Actions France (OCDE)", "France", "SPASTT01FRM661N"),
    ("OCDE_ALLEMAGNE", "Actions Allemagne (OCDE)", "Allemagne", "SPASTT01DEM661N"),
    ("OCDE_ROYAUME_UNI", "Actions Royaume-Uni (OCDE)", "Royaume-Uni", "SPASTT01GBM661N"),
    ("OCDE_JAPON", "Actions Japon (OCDE)", "Japon", "SPASTT01JPM661N"),
    ("OCDE_ZONE_EURO", "Actions zone euro (OCDE)", "Zone euro", "SPASTT01EZM661N"),
    ("OCDE_INDE", "Actions Inde (OCDE)", "Inde", "SPASTT01INM661N"),
    ("OCDE_BRESIL", "Actions Brésil (OCDE)", "Brésil", "SPASTT01BRM661N"),  # gardé à partir de 1994-07, voir DEBUT_OCDE
    ("OCDE_COREE", "Actions Corée du Sud (OCDE)", "Corée du Sud", "SPASTT01KRM661N"),
    ("OCDE_CHINE", "Actions Chine (OCDE)", "Chine", "SPASTT01CNM661N"),
]
# Avant le Plan Real (juillet 1994), l'hyperinflation rend la série brésilienne inutilisable : valeurs arrondies à
# quelques dix-millièmes, variations de +100 % ou +6 000 % qui sont des effets d'arrondi, pas des mouvements de marché.
DEBUT_OCDE = {"SPASTT01BRM661N": "1994-07"}
for _id, _nom, _zone, _serie in OCDE:
    INDICES.append({"id": _id, "nom": _nom, "zone": _zone, "devise": "monnaie locale", "type": "prix (moyenne du mois)",
                    "fournisseur": "OCDE (via FRED)", "sources": [("fred", _serie)],
                    "remarques": "Indice de cours des actions de l'OCDE, base 2015 = 100, moyenne mensuelle et non clôture. "
                                 "Pour les tendances longues seulement : ne pas comparer mois par mois avec un indice en clôture."})

# Séries macro FRED : (id dans la base, id FRED, description, agrégation des données quotidiennes)
MACRO = [
    ("inflation_us_indice", "CPIAUCSL", "Indice des prix à la consommation, États-Unis (1982-84 = 100)", None),
    ("inflation_fr_indice_ocde", "FRACPIALLMINMEI", "Indice des prix à la consommation, France (OCDE, 2015 = 100)", None),
    ("inflation_fr_ipch", "CP0000FRM086NEST", "Indice des prix harmonisé, France (Eurostat, 2015 = 100)", None),
    ("taux_fed", "FEDFUNDS", "Taux directeur effectif de la Fed, %", None),
    ("taux_10ans_us", "GS10", "Taux de l'emprunt d'État américain à 10 ans, %", None),
    ("taux_10ans_fr", "IRLTLT01FRM156N", "Taux de l'emprunt d'État français à 10 ans, %", None),
    ("taux_bce_depot", "ECBDFR", "Taux de la facilité de dépôt de la BCE, % (fin de mois)", "dernier"),
    ("usd_par_eur", "DEXUSEU", "Dollars pour 1 euro (fin de mois)", "dernier"),
    ("dem_par_usd", "EXGEUS", "Marks allemands pour 1 dollar (moyenne du mois, 1971-2001)", None),
    ("petrole_wti", "WTISPLC", "Pétrole WTI, dollars le baril (moyenne du mois)", None),
    ("recession_us", "USREC", "Récession américaine selon le NBER (1 = oui)", None),
    ("recession_zone_euro", "EUROREC", "Récession zone euro selon l'OCDE (1 = oui)", None),
]


def telecharger(url, essais=3):
    for i in range(essais):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=AGENT), timeout=90) as r:
                return r.read()
        except Exception as e:
            if i == essais - 1:
                raise
            print(f"  nouvel essai après erreur : {e}")
            time.sleep(3 * (i + 1))


def fin_de_mois(points):
    """{date: valeur} quotidien -> {AAAA-MM: (dernière date, valeur)}. Le dernier mois de la série n'est gardé
    que s'il est terminé (dernière cotation après le 25) : mois en cours, ou série qui s'arrête en cours de mois."""
    mois = {}
    for d, v in sorted(points.items()):
        if v is not None:
            mois[d[:7]] = (d, v)
    if mois:
        dernier = max(mois)
        if int(mois[dernier][0][8:10]) < 26:
            del mois[dernier]
    return mois


def yahoo(ticker, champ):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(ticker)}"
           f"?interval=1d&period1=-2208988800&period2=9999999999")
    r = json.loads(telecharger(url))["chart"]["result"][0]
    decalage = r["meta"].get("gmtoffset", 0)
    if champ == "adjclose":
        valeurs = r["indicators"]["adjclose"][0]["adjclose"]
    else:
        valeurs = r["indicators"]["quote"][0]["close"]
    points = {}
    for ts, v in zip(r["timestamp"], valeurs):
        d = (datetime(1970, 1, 1) + timedelta(seconds=ts + decalage)).date().isoformat()
        points[d] = v
    return fin_de_mois(points), f"Yahoo Finance {ticker}"


_STOXX = {}


def stoxx(colonne):
    if not _STOXX:
        texte = telecharger("https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt").decode("latin-1")
        lignes = texte.splitlines()
        entete = [c.strip() for c in lignes[3].split(";")]
        for l in lignes[4:]:
            c = [x.strip() for x in l.split(";")]
            if len(c) < 3 or len(c[0]) != 10:
                continue
            j, m, a = c[0].split(".")
            for nom, v in zip(entete[1:], c[1:]):
                if nom and v:
                    _STOXX.setdefault(nom, {})[f"{a}-{m}-{j}"] = float(v)
    return fin_de_mois(_STOXX[colonne]), f"STOXX hbrbcpe.txt ({colonne})"


def fred(serie, agregation):
    texte = telecharger(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={serie}").decode("utf-8")
    points = {}
    for r in list(csv.reader(texte.splitlines()))[1:]:
        if len(r) == 2 and r[1] not in ("", "."):
            points[r[0]] = float(r[1])
    if agregation == "dernier":
        return {m: v for m, (d, v) in fin_de_mois(points).items()}
    return {d[:7]: v for d, v in points.items()}


def measuringworth(serie):
    """Clôtures quotidiennes du Dow Jones depuis 1885 (MeasuringWorth, usage non commercial avec citation)."""
    url = (f"https://www.measuringworth.com/datasets/{serie}/export.php?monthStartD=1&dayStartD=1&yearStartD=1885"
           f"&monthEndD=12&dayEndD=31&yearEndD={date.today().year}")
    points = {}
    for r in csv.reader(telecharger(url).decode("utf-8", "replace").splitlines()):
        if len(r) == 2 and r[0].count("/") == 2:
            mo, j, a = r[0].split("/")
            try:
                points[f"{a}-{int(mo):02d}-{int(j):02d}"] = float(r[1])
            except ValueError:
                pass
    return fin_de_mois(points), f"MeasuringWorth {serie}"


_CACHE = {}


def charger(src):
    """Une source d'indice -> ({AAAA-MM: (date de clôture, valeur)}, libellé). Mise en cache pour la séance."""
    if src not in _CACHE:
        if src[0] == "yahoo":
            _CACHE[src] = yahoo(src[1], src[2])
        elif src[0] == "stoxx":
            _CACHE[src] = stoxx(src[1])
        elif src[0] == "measuringworth":
            _CACHE[src] = measuringworth(src[1])
        else:
            # Les tout premiers points de certains pays valent 0 une fois arrondis (Brésil, hyperinflation) : écartés
            debut = DEBUT_OCDE.get(src[1], "")
            _CACHE[src] = ({m: ("", v) for m, v in fred(src[1], None).items() if v > 0 and m >= debut},
                           f"FRED {src[1]} (OCDE, moyenne du mois)")
        time.sleep(1)
    return _CACHE[src]


def lire_csv(nom):
    f = DOSSIER / nom
    if not f.exists():
        return []
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def ecrire_csv(nom, colonnes, lignes):
    DOSSIER.mkdir(parents=True, exist_ok=True)
    with open(DOSSIER / nom, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=colonnes, lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)


def collecter_indices():
    anciens = {(r["mois"], r["indice"]): r for r in lire_csv("niveaux-mensuels.csv")}
    lignes, fiches, modifies = [], [], []
    for ind in INDICES:
        print(f"{ind['nom']}...")
        serie = {}
        for src in reversed(ind["sources"]):  # la source prioritaire est écrite en dernier et l'emporte
            mois, libelle = charger(src)
            for m, (d, v) in mois.items():
                serie[m] = (v, libelle, d)
        precedent = None
        for m in sorted(serie):
            v, libelle, d = serie[m]
            var = "" if precedent is None else f"{(v / precedent - 1) * 100:.2f}"
            ancien = anciens.get((m, ind["id"]))
            date_recup = AUJOURDHUI
            if ancien:
                if abs(float(ancien["cloture"]) / v - 1) > 0.0001:
                    modifies.append(f"{ind['id']} {m} : {ancien['cloture']} -> {v:.4f}")
                else:
                    date_recup = ancien["recupere_le"]
            lignes.append({"mois": m, "indice": ind["id"], "date_cloture": d, "cloture": f"{v:.10g}", "variation_pct": var,
                           "source": libelle, "recupere_le": date_recup})
            precedent = v
        mois_tries = sorted(serie)
        fiches.append({"id": ind["id"], "nom": ind["nom"], "zone": ind["zone"], "devise": ind["devise"],
                       "type": ind["type"], "fournisseur": ind["fournisseur"],
                       "sources": " ; ".join(s[1] for s in ind["sources"]),
                       "debut": mois_tries[0], "fin": mois_tries[-1], "nb_mois": len(mois_tries),
                       "remarques": ind["remarques"]})
        print(f"  {mois_tries[0]} -> {mois_tries[-1]} ({len(mois_tries)} mois)")
    ecrire_csv("niveaux-mensuels.csv", ["mois", "indice", "date_cloture", "cloture", "variation_pct", "source", "recupere_le"], lignes)
    ecrire_csv("indices.csv", ["id", "nom", "zone", "devise", "type", "fournisseur", "sources", "debut", "fin", "nb_mois", "remarques"], fiches)
    return modifies


def collecter_macro():
    lignes = []
    series = {}
    for cle, serie, desc, agreg in MACRO:
        print(f"FRED {serie}...")
        series[cle] = fred(serie, agreg)
        for m, v in sorted(series[cle].items()):
            lignes.append({"mois": m, "serie": cle, "valeur": f"{v:.4f}", "source": f"FRED {serie}"})
        time.sleep(1)
    # Série dérivée : dollars pour 1 euro, depuis 1971 (avant 1999 : mark converti au taux fixe 1,95583,
    # synthétique, et moyenne du mois au lieu de la fin de mois)
    for m, dem in sorted(series["dem_par_usd"].items()):
        if m < "1999-01":
            lignes.append({"mois": m, "serie": "usd_par_eur_long", "valeur": f"{1.95583 / dem:.4f}",
                           "source": "Calcul : 1,95583 / FRED EXGEUS (synthétique avant l'euro, moyenne du mois)"})
    for m, v in sorted(series["usd_par_eur"].items()):
        lignes.append({"mois": m, "serie": "usd_par_eur_long", "valeur": f"{v:.4f}", "source": "FRED DEXUSEU"})
    # Inflation France longue : série OCDE, prolongée par les variations de l'indice harmonisé après sa fin
    ocde, ipch = series["inflation_fr_indice_ocde"], series["inflation_fr_ipch"]
    dernier = max(ocde)
    for m, v in sorted(ocde.items()):
        lignes.append({"mois": m, "serie": "inflation_fr_long", "valeur": f"{v:.4f}", "source": "FRED FRACPIALLMINMEI"})
    niveau = ocde[dernier]
    for m in sorted(k for k in ipch if k > dernier):
        prec = max(k for k in ipch if k < m)
        niveau *= ipch[m] / ipch[prec]
        lignes.append({"mois": m, "serie": "inflation_fr_long", "valeur": f"{niveau:.4f}",
                       "source": "Prolongé avec les variations de FRED CP0000FRM086NEST"})
    lignes.sort(key=lambda r: (r["serie"], r["mois"]))
    ecrire_csv("macro-mensuel.csv", ["mois", "serie", "valeur", "source"], lignes)
    desc = [{"serie": c, "fred": s, "description": d} for c, s, d, _ in MACRO]
    desc += [{"serie": "usd_par_eur_long", "fred": "EXGEUS + DEXUSEU", "description": "Dollars pour 1 euro depuis 1971 (synthétique avant 1999)"},
             {"serie": "inflation_fr_long", "fred": "FRACPIALLMINMEI + CP0000FRM086NEST", "description": "Indice des prix France depuis 1955, prolongé"}]
    ecrire_csv("macro-series.csv", ["serie", "fred", "description"], desc)


# Mois sans cotation connus, qui ne sont pas des trous de données
FERMETURES = {"DOW_JONES": {"1914-08": "Bourse de New York fermée (Première Guerre mondiale)", "1914-09": "idem",
                            "1914-10": "idem", "1914-11": "idem"}}


def suivant(m):
    a, mo = int(m[:4]), int(m[5:])
    return f"{a + (mo == 12)}-{1 if mo == 12 else mo + 1:02d}"


def controler():
    lignes = lire_csv("niveaux-mensuels.csv")
    par_indice = {}
    for r in lignes:
        par_indice.setdefault(r["indice"], {})[r["mois"]] = r
    ok = True
    print("\nCONTRÔLES QUALITÉ")
    for ind, s in par_indice.items():
        mois = sorted(s)
        trous, m = [], mois[0]
        while m < mois[-1]:
            m = suivant(m)
            if m not in s and m not in FERMETURES.get(ind, {}):
                trous.append(m)
        erreurs = 0
        precedent = None
        for mm in mois:
            v = float(s[mm]["cloture"])
            if precedent is not None and s[mm]["variation_pct"]:
                if abs((v / precedent - 1) * 100 - float(s[mm]["variation_pct"])) > 0.01:
                    erreurs += 1
            precedent = v
        extremes = [f"{mm} {float(s[mm]['variation_pct']):+.1f} %" for mm in mois
                    if s[mm]["variation_pct"] and abs(float(s[mm]["variation_pct"])) > 25]
        # Fin de mois douteuse : dernière cotation plus de 4 jours ouvrés avant la fin du mois (trou de la source)
        douteux = []
        for mm in mois:
            if not s[mm]["date_cloture"]:  # moyenne du mois (OCDE) : pas de date de clôture
                continue
            d = date.fromisoformat(s[mm]["date_cloture"])
            fin = date(d.year + (d.month == 12), 1 if d.month == 12 else d.month + 1, 1) - timedelta(days=1)
            ouvres = sum(1 for k in range(1, (fin - d).days + 1) if (d + timedelta(days=k)).weekday() < 5)
            if ouvres > 4:
                douteux.append(f"{mm} ({s[mm]['date_cloture']})")
        etat = "OK" if not trous and not erreurs else "À VOIR"
        ok &= etat == "OK"
        print(f"- {ind:<12} {mois[0]} -> {mois[-1]}  trous : {len(trous)}{' ' + ', '.join(trous[:5]) if trous else ''}"
              f"  variations fausses : {erreurs}  {etat}" + (f"  | plus de 25 % : {', '.join(extremes)}" if extremes else "")
              + (f"  | fins de mois douteuses : {len(douteux)} ({', '.join(douteux[:4])}{'...' if len(douteux) > 4 else ''})" if douteux else ""))
    print("\nMois de repère (S&P 500, attendu d'après l'historique publié) :")
    for m, attendu in [("1987-10", -21.8), ("2008-10", -16.9), ("2020-03", -12.5), ("1974-09", -11.9)]:
        r = par_indice.get("SP500", {}).get(m)
        if r:
            ecart = float(r["variation_pct"]) - attendu
            print(f"- {m} : {float(r['variation_pct']):+.1f} % (attendu environ {attendu:+.1f} %, écart {ecart:+.1f})")
    print("\nRecoupement des sources sur les mois communs (variation mensuelle, écart moyen absolu) :")
    for ind in INDICES:
        if len(ind["sources"]) < 2:
            continue
        a = charger(ind["sources"][1])[0]
        b = charger(ind["sources"][0])[0]
        communs = sorted(set(a) & set(b))
        ecarts = []
        for m in communs[1:]:
            p = max(k for k in communs if k < m)
            ecarts.append(abs((a[m][1] / a[p][1]) - (b[m][1] / b[p][1])) * 100)
        if ecarts:
            print(f"- {ind['id']} : {len(ecarts)} mois communs ({communs[0]} -> {communs[-1]}), écart moyen {sum(ecarts) / len(ecarts):.3f} point, maximum {max(ecarts):.3f}")
    return ok


def verifier_liens():
    """Vérifie que chaque source de evenements.csv répond, affiche le titre de la page pour relecture, date verifie_le."""
    import html
    import re
    lignes = lire_csv("evenements.csv")
    ko = 0
    for r in lignes:
        try:
            page = telecharger(r["source_url"], essais=2)[:200000].decode("utf-8", "replace")
            m = re.search(r"<title[^>]*>(.*?)</title>", page, re.S | re.I)
            titre = html.unescape(m.group(1)).strip()[:80] if m else "(sans titre)"
            r["verifie_le"] = AUJOURDHUI
            print(f"OK  {r['date_debut']} {r['titre'][:40]:<41} | {titre}")
        except Exception as e:
            ko += 1
            print(f"KO  {r['date_debut']} {r['titre'][:40]:<41} | {r['source_url']} | {e}")
        time.sleep(0.5)
    ecrire_csv("evenements.csv", list(lignes[0]), lignes)
    print(f"\n{len(lignes) - ko} liens OK, {ko} en échec. Relire les titres : une page « introuvable » peut répondre sans erreur.")


def main():
    if "--liens" in sys.argv:
        verifier_liens()
        return
    if "--controles" not in sys.argv:
        modifies = collecter_indices()
        collecter_macro()
        print(f"\nValeurs déjà présentes qui ont changé : {len(modifies)}")
        for m in modifies[:30]:
            print(f"  {m}")
    controler()


if __name__ == "__main__":
    main()
