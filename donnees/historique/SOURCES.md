# Base historique des marchés : sources, couverture et contrôles

Collecte du 31/10/2026 par `python scripts/maj_historique.py`. Interrogation : `python scripts/historique.py` (voir `scripts/README.md`).

**Usage personnel uniquement.** Les données de Yahoo Finance et des fournisseurs d'indices sont réservées à un usage personnel. Le dépôt est privé et doit le rester ; s'il devenait public, retirer `donnees/historique/` et `docs/Historique-marches.xlsx` du suivi git.

## Ce que contient la base

| Fichier | Contenu |
|---|---|
| `indices.csv` | Fiche de chaque série : nom, zone, devise, type (prix ou dividendes réinvestis), fournisseur, sources, couverture réelle, remarques |
| `niveaux-mensuels.csv` | Une ligne par mois et par indice : date de la dernière cotation du mois, clôture, variation du mois en %, source, date de collecte |
| `macro-mensuel.csv` et `macro-series.csv` | Inflation, taux, change, pétrole, récessions (FRED) |
| `evenements.csv` | 86 événements datés de 1971 à 2025, chacun avec une source dont le lien a été vérifié (`verifie_le`) |
| `marches.sqlite` | **La base de données** : les mêmes tables (`indices`, `niveaux`, `macro`, `macro_series`, `evenements`) et une vue `rendements_annuels`. Reconstruite par `historique.py sqlite`, versionnée. Elle s'ouvre avec un logiciel comme DB Browser for SQLite ; les CSV restent la source de référence |

## Couverture réelle des indices

| Indice | Type | Devise | Début | Source |
|---|---|---|---|---|
| MSCI World | prix | USD | 1972-01 | Yahoo Finance ^990100-USD-STRD |
| MSCI ACWI | prix | USD | 1988-01 | Yahoo Finance ^892400-USD-STRD |
| MSCI Emerging Markets | dividendes réinvestis, via un fonds | USD | 1994-05 | Yahoo Finance VEIEX (fonds Vanguard, cours ajusté) |
| S&P 500 | prix | USD | 1927-12 | Yahoo Finance ^GSPC |
| S&P 500 dividendes réinvestis | dividendes réinvestis | USD | 1988-01 | Yahoo Finance ^SP500TR |
| Nasdaq-100 | prix | USD | 1985-10 | Yahoo Finance ^NDX |
| Nasdaq Composite | prix | USD | 1971-02 | Yahoo Finance ^IXIC |
| Dow Jones | prix | USD | 1885-02 | Yahoo Finance ^DJI depuis 1992 ; avant, MeasuringWorth (voir plus bas) |
| STOXX Europe 600 | prix | EUR | 1986-12 | STOXX (fichier officiel hbrbcpe.txt) jusqu'en 2016-09, puis Yahoo ^STOXX |
| Euro Stoxx 50 | prix | EUR | 1986-12 | STOXX (fichier officiel) jusqu'en 2016-09, puis Yahoo ^STOXX50E |
| CAC 40 | prix | EUR | 1990-03 | Yahoo Finance ^FCHI |
| DAX | dividendes réinvestis | EUR | 1987-12 | Yahoo Finance ^GDAXI |
| FTSE 100 | prix | GBP | 1984-01 | Yahoo Finance ^FTSE |
| Nikkei 225 | prix | JPY | 1965-01 | Yahoo Finance ^N225 |
| Hang Seng | prix | HKD | 1986-12 | Yahoo Finance ^HSI |

## Le « minimum de prix » sur longue période : indices de l'OCDE

Pour les marchés dont l'indice phare n'a pas d'historique libre ancien (CAC 40 avant 1990, DAX avant 1987, émergents), la base ajoute **9 indices de cours des actions de l'OCDE**, publiés par FRED (série « Share Prices », base 2015 = 100).

| Série | Début | Série FRED |
|---|---|---|
| Actions France | 1955-01 | SPASTT01FRM661N |
| Actions Allemagne | 1960-01 | SPASTT01DEM661N |
| Actions Royaume-Uni | 1957-12 | SPASTT01GBM661N |
| Actions Japon | 1959-01 | SPASTT01JPM661N |
| Actions zone euro | 1986-12 (arrêtée en 2026-01) | SPASTT01EZM661N |
| Actions Inde | 1957-01 | SPASTT01INM661N |
| Actions Brésil | 1994-07 | SPASTT01BRM661N |
| Actions Corée du Sud | 1981-01 | SPASTT01KRM661N |
| Actions Chine | 1999-01 | SPASTT01CNM661N |

**Attention :** ce sont des **moyennes du mois**, pas des clôtures. Elles servent aux tendances longues (rendements sur 10 ou 20 ans, grandes phases), pas à comparer un mois précis avec un indice en clôture. Elles ne sont jamais raccordées aux indices phares.

Brésil : la série commence au Plan Real (juillet 1994). Avant, l'hyperinflation la rend inutilisable : les valeurs sont arrondies à quelques dix-millièmes et produisent des variations de +100 % ou +6 000 % qui ne sont que des effets d'arrondi.

## Dow Jones avant 1992 : MeasuringWorth

Samuel H. Williamson, « Daily Closing Value of the Dow Jones Average, 1885 to Present », MeasuringWorth, 2026 (measuringworth.com/datasets/DJA). La série est raccordée par MeasuringWorth avant 1914 : Dow Jones Average unique avant octobre 1896, puis premier DJIA jusqu'en juillet 1914. Conditions : usage non commercial à but éducatif, avec citation. Recoupement avec Yahoo de 1992 à 2026, sur 417 mois communs : écart moyen de 0,004 point par mois. Les mois d'août à novembre 1914 manquent parce que la Bourse de New York était fermée (Première Guerre mondiale) ; ce n'est pas un trou de données.

## Ce qui est couvert

- **Plus de 50 ans** : S&P 500 (1927), Dow Jones (1885), MSCI World (1972), Nasdaq Composite (1971), Nikkei 225 (1965), et les séries OCDE France, Allemagne, Royaume-Uni, Japon et Inde (1955 à 1960).
- **Moins de 50 ans** : les autres commencent à leur création ou au début de l'historique accessible.

**Rien n'a été comblé ni reconstruit.** Au total, 24 séries et environ 15 500 mois.

## Ce qui n'a pas pu être obtenu (tests du 31/10/2026)

- **MSCI, versions dividendes réinvestis, en euros, et MSCI EM** : l'accès historique du site MSCI renvoie une erreur ou une page anti-robot ; Yahoo ne fournit que le MSCI World et l'ACWI en prix et en dollars. Pour les émergents, on utilise le fonds Vanguard VEIEX, qui a suivi le MSCI EM puis un indice FTSE à partir de 2013. Piste : télécharger les fichiers à la main sur msci.com et les intégrer.
- **CAC 40 de 1988 à 1990, DAX avant 1987, l'indice MSCI EM lui-même** : pas de source libre accessible. Stooq propose ces historiques mais impose une vérification anti-robot, qui n'a pas été contournée. **En remplacement, un minimum de prix** : les séries OCDE France, Allemagne et pays émergents (voir plus haut).
- **Inflation France** : la série OCDE (FRACPIALLMINMEI) s'arrête en mars 2025 ; elle est prolongée avec les variations de l'indice harmonisé d'Eurostat (série `inflation_fr_long`).
- **EUR/USD avant 1999** : calculé à partir du mark allemand (1,95583 marks pour 1 euro), avec la moyenne du mois et non la fin de mois. C'est une série **synthétique**.

## Contrôles qualité (31/10/2026)

- **Trous** : aucun mois manquant, sur aucun indice.
- **Variations** : toutes recalculées à partir des niveaux, aucune incohérence.
- **Mois de repère du S&P 500** : octobre 1987 -21,8 %, octobre 2008 -16,9 %, mars 2020 -12,5 %, septembre 1974 -11,9 %, conformes à l'historique publié. Rendements annuels de 2008 (-38,5 %), 2022 (-19,4 %) et 2023 (+24,2 %), conformes eux aussi.
- **Variations de plus de 25 % en un mois** : toutes correspondent à des épisodes connus. S&P 500 de 1931 à 1938 (Grande Dépression), octobre 1987 (Nasdaq, FTSE), août 1998 et octobre 2008 (émergents), février 2001 (Nasdaq-100), septembre 2002 (DAX).
- **Recoupement STOXX officiel contre Yahoo** sur les mois communs : écart moyen de 0,06 point par mois sur le STOXX Europe 600 (149 mois) et de 0,07 point sur l'Euro Stoxx 50 (114 mois). Les plus gros écarts (jusqu'à 1,5 point, mai et juin 2011) viennent de jours de cotation manquants chez Yahoo. **C'est pour cela que la source officielle passe en priorité.**
- **Variations de plus de 25 % sur les séries ajoutées** :
  - Hang Seng en octobre 1987 (-44 %) et en 1997-98 : épisodes connus.
  - Corée en mai 2026 (+25,8 %) : recoupée avec le KOSPI de Yahoo (+28 % sur le mois).
  - Royaume-Uni en février 1975 (+43,8 %) et Inde en mars 1992 (+41,5 %) : rebonds connus.
  - **Non vérifiées**, à prendre avec prudence : France OCDE en avril 1982 (+27,7 %) et Inde OCDE en avril 1973 (-48,7 %), qui pourrait être une rupture de série.
- **Fins de mois** : les seules dernières cotations éloignées de la fin du mois correspondent à des jours fériés (Pâques, fin d'année au Japon).
- **Grandes baisses** (`docs/recherche/baisses-majeures.csv`), comparées aux calculs de la base :
  - même calendrier : 1973-74, 1987, 2000-02, 2007-09, 2020 et 2022 ;
  - baisses un peu moins fortes, parce que la base est en fins de mois et non au jour le jour : S&P 500 en 2007-09, -52,6 % contre -56,8 % ; Covid en 2020, -20 % contre -34 %.
- **Valeurs modifiées entre deux collectes** : le script les liste à chaque mise à jour, au lieu de les remplacer en silence.

## Mise à jour

Une fois par mois (après le dernier jour de bourse) :

```
python scripts/maj_historique.py
python scripts/historique.py excel
python scripts/historique.py sqlite
```

Puis, une fois par trimestre :
- ajouter les nouveaux événements marquants dans `evenements.csv`, chacun avec sa source ;
- lancer `python scripts/maj_historique.py --liens`.
