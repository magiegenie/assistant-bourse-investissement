# Synthèse des recherches déposées (30/10/2026)

Ce fichier résume l'état des 12 domaines et liste les contradictions à trancher avant d'intégrer quoi que ce soit dans `connaissances/`. Aucune donnée n'est encore intégrée.

## 1. État des fichiers

| # | Fichier | Contenu | Qualité | Données (CSV) |
|---|---|---|---|---|
| 1 | `01-fiscalite.md` | Fiscalité complète, simulations | Bonne base, à corriger sur l'assurance vie (voir §2) | `fiscalite-parametres.csv`, `enveloppes-fiscales-france.csv` |
| 2 | `02-produits.md` | ETF, courtiers, assurance vie | Moyenne : lignes factices, ISIN en double, écart de suivi vide | `etf.csv`, `courtiers.csv`, `assurance-vie.csv` |
| 3 | `03-historique.md` | Rendements, baisses | Faible : le CSV de rendements est quasi vide. **Remplacé** par `donnees/historique/` (31/10/2026) | `rendements-annuels.csv`, `baisses-majeures.csv` |
| 4 | `04-projection.md` | Hypothèses, Monte Carlo | Moyenne : plusieurs montants faux (recalculés) | `hypotheses-projection.csv` |
| 5 | `05-retrait.md` | Règle des 4 %, retrait | Moyenne : fiscalité périmée | `retrait.csv` |
| 6 | `06-allocation.md` et `06b-allocation-bis.md` | Allocation (deux versions) | Moyenne : chiffres différents d'une version à l'autre | `allocations-types.csv`, `allocations-types-b.csv` |
| 7 | `07-comportement.md` | Biais, scripts de coaching | Bonne base, quelques chiffres douteux | `etudes-comportement.csv` |
| 8 | `08-pedagogie.md` | 12 modules, glossaire, cas | **Rédigé par Claude**, sans recherche externe | aucun |
| 9 | `09-veille.md` | Sources, calendrier, brief | Moyenne, conflit avec l'agent Veilleur | `sources-veille.csv` |
| 10 | `10-budget.md` | Budget, livrets, prévoyance | Faible : CSV manquant, taux à vérifier | **absent** (`budget-reperes.csv`) |
| 11 | `11-arnaques.md` | Arnaques, garanties | Bonne base, règle de l'arbre de décision inversée | `arnaques-signaux.csv` |
| 12 | `12-sources.md` | Bibliographie | Moyenne | `enveloppes-fiscales-france.csv` |

## 2. Contradiction majeure : prélèvements sociaux et PFU

- **Recherche 01** : prélèvements sociaux à 18,6 % et PFU à 31,4 % depuis le 1er janvier 2026, partout (CTO, PEA, assurance vie, crypto).
- **Recherches 02 (point 3), 04, 05, 06, 06b, 12 et `enveloppes-fiscales-france.csv`** : 17,2 % et PFU à 30 %.
- **Vérification par recherche web (sites d'information, pas le Journal officiel)** : la loi de financement de la sécurité sociale pour 2026 relève la CSG de 9,2 % à 10,6 % sur une partie des revenus du capital, soit 18,6 % de prélèvements sociaux et un PFU de 31,4 %. **La recherche 01 a raison sur le principe, les autres sont périmées.** En revanche :
  - **assurance vie** : les sources indiquent que les contrats d'assurance vie et de capitalisation sont **exclus** de la hausse (prélèvements sociaux maintenus à 17,2 %). La recherche 01 se trompe sur ce point (simulation 3 notamment) ;
  - **PEA** : plusieurs sources le disent concerné, mais le traitement des gains acquis avant 2026 n'est pas clair (taux selon la date de formation du gain). À vérifier ;
  - **PEL, CEL** : exclus ou à 9,2 % selon la date d'ouverture, sources divergentes. Peu important ici.
- **Confirmation officielle (service-public.fr, fiche F2329 vérifiée le 30/06/2026)** : cas général 18,6 % en 2026 ; assurance vie, PEL, CEL et immobilier 17,2 % ; PFU de 31,4 % (12,8 % + 18,6 %). Pour le PEA, la fiche ne donne pas de taux explicite : 18,6 % par application du cas général, à vérifier pour les gains anciens. **La fiche C a été corrigée en conséquence.**
- **Reste à faire** : relire le texte de la LFSS 2026 sur Légifrance (article sur la CSG) ou la fiche service-public.fr « prélèvements sociaux ». Sources web consultées (secondaires) : [Meilleurtaux, CSG 10,6 % et assurance vie épargnée](https://placement.meilleurtaux.com/assurance-vie/actualites/2025-decembre/csg-10-6-certains-placements-assurance-vie-epargnee.html), [Auguste Patrimoine, PEA et hausse de la CSG](https://www.auguste-patrimoine.fr/blog/pea-et-hausse-de-la-csg-en-2026-impact-calcul-et-strategies-de-retrait), [La Finance pour tous](https://www.lafinancepourtous.com/2025/12/17/csg-un-taux-a-double-vitesse-pour-2026/).

## 3. Autres contradictions et points à trancher

1. **Poids des États-Unis dans le MSCI World** : 73 % (02), 70,3 % (06), 72 % (06b). **Tranché** : 72,94 % au 30/09/2026 (fiche officielle MSCI).
2. **Inflation** : « converge vers 2 % » (04) contre 3,4 % en octobre 2026 (10), avec un Livret A à 1,70 % (10) et un « taux sans risque de 2,5 à 3 % » (11). À aligner sur l'INSEE et la Banque de France.
3. **Bessembinder** : « mise à jour de juillet 2026 » (06) contre « 15 mars 2026 » (06b). Existence non confirmée.
4. **AMF et mars 2020** : 150 000 nouveaux comptes (07, texte) contre 1,5 million de nouveaux investisseurs (07, CSV).
5. **Fréquence de consultation du portefeuille** : une à deux fois par an (07) contre une fois par semaine maximum (fiche F, point 35).
6. **Brief du Veilleur** : sans explication (09) contre avec explication et verdict (`veilleur.md`).
7. **Allocation dynamique** : 80 % d'actions (06, texte) contre 90 % (06, CSV).
8. **Arbre de décision arnaques** : règle d'interprétation inversée pour les questions 4 et 8 (11).
9. **Plafond légal de 0,5 % sur les frais d'ordre PEA** : affirmé en 02 et 07, non vérifié.
10. **Âge légal de départ à la retraite (64 ans)** : à vérifier (05).

## 4. Données manquantes, à redemander

- `budget-reperes.csv` (recherche 10).
- Série complète des rendements annuels (recherche 03) : c'est la plus utile pour remplacer les taux 4/5/7 % des projections.
- Distribution des rendements sur 10, 15 et 20 ans (percentiles).
- Écart de suivi des ETF (recherche 02).
- Liens précis vers les sources officielles (presque toutes les recherches).

## 4 bis. Avancement de l'intégration

- **Fiche C** : corrigée et vérifiée sur service-public.fr.
- **Fiches D et E** : enrichies (points 56 à 66) à partir des recherches 02, 03, 06 et 06b. Les contradictions de chiffres (poids des États-Unis, concentration) sont remplacées par des fourchettes marquées « à vérifier ». Rien n'a été vérifié à la source.
- **Fiches F et H** : enrichies (points 67 à 73 et 74 à 81). Décisions prises : consultation du portefeuille « au plus une fois par semaine, plutôt une fois par mois » (la recherche 07 disait une à deux fois par an, jugé peu réaliste avec un versement mensuel) ; brief du Veilleur avec cause attribuée à une source ou « cause non établie ». `coach.md` (scripts par situation, reformulés sans prédiction ni recommandation) et `veilleur.md` ajustés.
- **Fiches A, B, G, I** : enrichies (points 82 à 89, 90 à 95, 96 à 98, 100 à 108). Vérifié par recherche web : Livret A et LDDS à 1,7 % et LEP à 2,5 % depuis le 1er août 2026 (la recherche 10 disait à tort qu'ils baissaient de 3,00 %, ils montaient de 1,5 %) ; inflation de 3,1 % en septembre 2026 (la recherche 04 disait qu'elle était revenue à 2 %). Décision prise : scénarios de projection par défaut 4 / 6 / 8 % nominaux (environ 2 / 4 / 6 % réels), au lieu de 4 / 5 / 7 %. `stratege.md` mis à jour. L'arbre de décision anti-arnaque est corrigé (arrêter dès un OUI).
- **Script `scripts/fiscalite.py`** créé (CTO, PEA, assurance vie, taux 2026) et testé sur les trois exemples de la fiche C.
- Restent à faire : simulateur Monte Carlo, données manquantes (rendements annuels complets, `budget-reperes.csv`, écart de suivi des ETF), vérification à la source des chiffres marqués « à vérifier ».

## 5. Ordre d'intégration conseillé

1. Trancher la fiscalité (§2) et produire la fiche C corrigée.
2. Fiches D et E (allocation, méthode) en réconciliant 02, 06, 06b.
3. Fiches F et H (comportement, info) à partir de 07 et 09, puis ajustement de `coach.md` et `veilleur.md`.
4. Fiche G et scripts : simulateur fiscal, Monte Carlo, hypothèses de projection (04), quand les données de 03 seront complètes.
5. `00-SOURCES.md` à partir de 12, sans y mettre ce qui n'est pas vérifié.
