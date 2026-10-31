# Scripts de calcul

Utilisés par les agents, jamais besoin de les lancer à la main. Les données lues sont dans `prive/<prenom>/`.

## Formats
`positions.csv` (une ligne par placement) :
```
nom,poche,enveloppe,investi,valeur,frais_annuels_pct,date_valeur
ETF S&P 500,USA,PEA,1000,1100,0.07,2026-10-30
```
`cibles.csv` :
```
poche,cible_pct
USA,40
```
`flux.csv` (versements négatifs, retraits positifs) :
```
date,montant
2026-01-15,-500
```

Les formats de tous les fichiers d'un profil (colonnes des CSV, paramètres) sont définis une seule fois dans `scripts/fichiers_profil.py`.

## Mise en place et données d'un profil
- `python scripts/nouveau_profil.py <prenom>` : crée `prive/<prenom>/` avec tous les documents (profil, profil de risque, budget, charte, plan d'investissement, checklist, journal, bilans, accueil) et les CSV vides au bon format. N'écrase jamais rien.
- `python scripts/creer_sheet.py prive/<prenom>/Portefeuille-<prenom>.xlsx --profil prive/<prenom>` : classeur de la personne, pré-rempli (paramètres, cibles, lignes déjà détenues en « Reprise », objectifs, budget), à importer dans Google Drive. Sans `--profil` : modèle vide ; `--exemple` : données fictives.
- `python scripts/synchro_sheet.py prive/<prenom> <Sheet exporté.xlsx>` : relit le Google Sheet et réécrit `transactions.csv`, `positions.csv`, `flux.csv`, `budget.csv`, `objectifs.csv` (prix : saisi, GOOGLEFINANCE ou Yahoo). Signale les écarts de cibles et de paramètres sans les écraser.
- `python scripts/importer_releve.py prive/<prenom> <releve.csv> --enveloppe PEA` : import d'un relevé exporté du courtier (colonnes reconnues via `templates/courtiers.csv`), sans doublons, vers `import-<date>.xlsx` à coller dans le Sheet. Voir `docs/CONNECTER-BANQUE-COURTIER.md`.

## Commandes
- `python scripts/allocation.py prive/<prenom> 1000` : poids, écarts, répartition d'un versement de 1 000 €, frais
- `python scripts/performance.py prive/<prenom> 7` : rendement réel (XIRR) comparé aux mêmes versements placés à 7 %/an
- `python scripts/projection.py 6000 1000 5 15 300000 --inflation 2` : capital, versement mensuel, rendement nominal %, années, objectif ; affiche le délai et le versement mensuel nécessaire, et avec `--inflation` l'équivalent en euros d'aujourd'hui
- `python scripts/allocation.py prive/<prenom> 0 --ajout Nvidia USA 6000` : simule l'ajout d'une ligne sans rien enregistrer
- `investi` = prix de revient de la ligne ; le plafond PEA se suit avec le total versé sur le PEA, à noter dans le profil
- `python scripts/reequilibrage.py prive/<prenom> 2000 10` : plan de ventes si une poche dépasse la cible de plus de 10 points après le versement de 2 000 € (PEA et assurance vie d'abord, CTO ensuite), impôt estimé, contrôle achats = ventes. Ne passe aucun ordre.
- `python scripts/exposition.py prive/<prenom>` : exposition réelle par pays, part en dollars et grandes entreprises à travers les ETF (données datées dans `donnees/indices-pays.csv` et `indices-entreprises.csv`, à mettre à jour chaque trimestre). Colonne facultative `indice` dans positions.csv pour forcer le rattachement.
- `python scripts/stress.py prive/<prenom>` : impact en euros de 6 scénarios de crise (hypothèses, pas des prévisions)
- `python scripts/profil_risque.py questions --montant 10000` : affiche le test de profil de risque, chiffré en euros sur le montant (questions dans `connaissances/questionnaire-risque.json`)
- `python scripts/profil_risque.py prive/<prenom>` : note `reponses-risque.csv` (colonnes `id,reponse` ; lettre de l'option, montant en euros pour T10, V, F ou ? pour le quiz ; infos `montant`, `capital`, `mensuel`, `objectif`, `annees`, `contexte_marche`) et donne capacité, tolérance, besoin de risque, connaissances, profil retenu (le plus prudent des deux), perte maximale acceptable et alertes. N'écrit rien.
- `stress.py` compare aussi le pire scénario à la ligne `perte_max_eur:` de `profil-risque.md` si elle existe
- `python scripts/historique.py resume | mois 2008-10 | periode SP500 2000-01 2012-12 | annees CAC40 | baisses MSCI_WORLD --seuil 20 | glissant SP500 --annees 10 | evenement covid` : base historique des marchés (24 séries mensuelles : 15 indices, dont le Dow Jones depuis 1885, et 9 séries de cours OCDE depuis 1955 à 1999, macro FRED, 86 événements). Options `--eur` et `--reel`. Aussi `excel` (régénère `docs/Historique-marches.xlsx`) et `sqlite` (reconstruit `donnees/historique/marches.sqlite`)
- `python scripts/maj_historique.py` : collecte mensuelle (Yahoo Finance, STOXX, FRED dont les indices de cours OCDE, MeasuringWorth pour le Dow Jones avant 1992) puis contrôles qualité ; `--controles` contrôles seuls ; `--liens` vérifie les sources des événements. Détail dans `donnees/historique/SOURCES.md`
- `python scripts/fiscalite.py pea 8000 24000 15000 --anciennete 6` : impôt estimé d'un retrait (enveloppe `cto`, `pea` ou `av`, retrait, valeur totale, total versé). Options : `--anciennete ANS`, `--couple` et `--primes MONTANT` (assurance vie), `--moins-values MONTANT` (CTO). Taux 2026 dans le dictionnaire `TAUX` du script, à revérifier chaque année (fiche C).
