# Recherche 03 : historique des marchés

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichiers de données associés (copiés tels quels) : `rendements-annuels.csv`, `baisses-majeures.csv`.
- **Remplacé le 31/10/2026** par la base historique `donnees/historique/` (données collectées par script, sourcées et contrôlées ; voir `donnees/historique/SOURCES.md`). Pour un chiffre historique, utiliser `python scripts/historique.py`, pas ces fichiers.

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

1. **`rendements-annuels.csv` est presque vide** : seule la colonne S&P 500 en dollars est remplie (2000 à 2026, sauf 2024 qui manque alors que le texte dit le contraire). Tout le reste, y compris MSCI World, euro, obligations, or, inflation et change, est « À VÉRIFIER ». Les années 1970 à 1999 sont entièrement vides. Inutilisable pour un simulateur ou un calcul de percentiles en l'état. L'autre IA l'a dit honnêtement, mais la demande principale n'est pas satisfaite.
2. **2026 est une année en cours** (recherche faite le 30 octobre) : +13,82 % est un cumul partiel, pas un rendement annuel. À ne pas utiliser comme année complète.
3. **`baisses-majeures.csv`** : 10 lignes. Méthode non précisée (cours ou dividendes réinvestis) et mélangée : les dates de retour au sommet de 2007 et 2013 correspondent à des cours, celle de 2000 à 2007 est cohérente avec des dividendes réinvestis. Baisses de plus de 20 % manquantes (par exemple 1980-1982 sur le S&P 500). MSCI World : retour au sommet de 1973 non renseigné. Pas de précision euro ou dollar.
4. **Distribution des rendements (point 1)** : on ne donne que minimum, médiane et maximum sur 20 ans pour le S&P 500 (valeurs approximatives, « À VÉRIFIER »). Les percentiles demandés (10e, 90e) et les horizons 1, 5, 10, 15 ans ne sont pas chiffrés. Rien pour le MSCI World. C'est la donnée la plus utile pour les projections, et elle manque.
5. **Point 5 (market timing)** : 11,0 % à 6,6 % n'est pas une division par deux (c'est environ -40 %). Chiffres attribués à J.P. Morgan « données au 31/12/2025 », que je ne peux pas confirmer.
6. **Point 3** : le -1,9 % annualisé du MSCI World (2000-2009) ne précise ni la devise ni les dividendes ; l'ordre de grandeur change selon.
7. **Point 4** : le calcul de l'exemple est juste (74 000 € et 78 000 €), mais la source citée est « principes mathématiques », pas une étude.
8. **Sources** : noms de sites ou d'études sans page précise, sauf JP Morgan et Vanguard. « Slickcharts » et « investir-simple.fr » sont des sites grand public, pas des sources primaires.

---

## 1. Quelle est la distribution des rendements annualisés réels (après inflation) du MSCI World et du S&P 500 sur toutes les périodes glissantes de 1, 5, 10, 15 et 20 ans ?

**Réponse courte :** Sur 1 an, la volatilité est extrême avec des rendements pouvant aller de -40 % à +50 %. À mesure que l'horizon d'investissement s'allonge (15 ou 20 ans), la dispersion se réduit drastiquement et la probabilité historique de perte en pouvoir d'achat tend vers zéro.

**Détail :** Le calcul repose sur les rendements totaux (dividendes réinvestis, ajustés de l'inflation). Sur le S&P 500 depuis 1926, pour des périodes glissantes de 20 ans, le minimum historique réel est proche de +0,5 %/an (À VÉRIFIER pour le chiffre décimal exact), la médiane autour de +6,5 %/an et le maximum vers +13 %/an. La part historique des périodes négatives sur 20 ans glissants est de 0 %. Pour le MSCI World depuis 1970, la tendance est similaire, bien que certaines périodes de 10 ans glissants (comme la décennie 2000) aient présenté des rendements annualisés négatifs.

**Piège fréquent ou erreur courante :** Confondre rendement nominal et rendement réel. Dans les années 1970, les marchés ont parfois monté nominalement, mais l'inflation élevée a détruit le rendement réel.

**Source(s) :** S&P Dow Jones Indices (données historiques), Credit Suisse Global Investment Returns Yearbook 2023. Consultation le 30 octobre 2026.

## 2. Quel est le rendement réel moyen long terme des actions mondiales, des obligations et de l'or ?

**Réponse courte :** Historiquement, les actions mondiales génèrent environ 5 % de rendement réel par an. Les obligations d'État se situent autour de 1,5 % à 2 %, et l'or préserve simplement le pouvoir d'achat avec un rendement réel très faible.

**Détail :** Selon les données de 1900 à 2022, le rendement réel annualisé (hypothèse centrale) des actions mondiales est de +5,0 %. L'hypothèse prudente souvent retenue par les planificateurs financiers est de +3,5 % (en cas de valorisations initiales élevées). L'hypothèse favorable historique (tirée par les actions américaines) est d'environ +7,0 %. Les obligations mondiales ont affiché environ +1,7 % réel, et l'or +0,8 % réel.

**Piège fréquent ou erreur courante :** Projeter les rendements nominaux exceptionnels de la dernière décennie (> 10 % par an pour les actions) sur les trente prochaines années, ignorant le phénomène cyclique de retour à la moyenne historique.

**Source(s) :** Credit Suisse Global Investment Returns Yearbook 2023 (par Dimson, Marsh et Staunton). Consultation le 30 octobre 2026.

## 3. Que nous enseignent les « décennies perdues » (2000-2009, Japon, années 1970) ?

**Réponse courte :** Une décennie perdue est une période de dix ans (ou plus) au cours de laquelle le rendement réel est nul ou négatif. Elles démontrent l'importance vitale de la diversification géographique et du contrôle de l'inflation.

**Détail :** Aux États-Unis et dans le Monde (2000-2009), le MSCI World a affiché un rendement annualisé de -1,9 % suite à l'éclatement de la bulle internet et la crise des subprimes. Au Japon (1990-2020), après l'éclatement de sa bulle en 1989, le marché a mis plus de 30 ans pour retrouver ses sommets, illustrant le danger de surpondérer son propre pays. Dans les années 1970, l'inflation mondiale à deux chiffres a laminé les rendements réels.

**Piège fréquent ou erreur courante :** Penser qu'investir sur 10 ans est une garantie absolue pour effacer une perte. L'histoire prouve qu'un horizon de 15 à 20 ans a parfois été nécessaire pour retrouver son capital réel initial.

**Source(s) :** Fiches historiques MSCI (MSCI World, MSCI Japan), Banque Mondiale (données d'inflation 1970-1980). Consultation le 30 octobre 2026.

## 4. Quel est l'effet du risque de séquence sur un portefeuille ?

**Réponse courte :** Le risque de séquence désigne l'impact de l'ordre des krachs et des hausses sur un portefeuille. Il est dévastateur en phase de retrait (retraite), car une forte baisse en début de période détruit le capital avant qu'il ne puisse bénéficier des hausses ultérieures.

**Détail :** Prenons deux investisseurs avec 100 000 euros et un retrait annuel de 10 000 euros en fin d'année. L'investisseur A subit d'abord un krach de -20 % (année 1), puis une hausse de +20 % (année 2). L'investisseur B vit l'inverse (+20 % puis -20 %). Le rendement moyen est identique. À la fin de l'année 2, le capital de A est de 74 000 euros. Le capital de B est de 78 000 euros. Une différence de 4 000 euros se crée en seulement deux ans uniquement à cause de l'ordre des rendements.

**Piège fréquent ou erreur courante :** Modéliser sa retraite avec un tableur appliquant un rendement fixe de +5 % chaque année, sans intégrer de chocs négatifs (stress-test) durant les premières années de consommation du capital.

**Source(s) :** Principes mathématiques fondamentaux de gestion de portefeuille (modèles de retraits).

## 5. Quel est le coût du market timing (manquer les meilleurs jours sur 20 ans) ?

**Réponse courte :** Tenter d'anticiper les baisses conduit très souvent à rater les rebonds fulgurants. Manquer les 10 meilleurs jours de cotation sur une période de 20 ans divise pratiquement par deux le rendement final.

**Détail :** Pour 10 000 USD investis sur le S&P 500 sur 20 ans (période close fin 2025, soit environ 5 000 jours de bourse), le rendement d'un portefeuille totalement investi est d'environ 11,0 % par an. Si l'investisseur manque uniquement les 10 meilleurs jours, son rendement s'effondre à 6,6 % par an. En manquant les 20 meilleurs jours, il tombe à 3,8 %. En manquant les 30 meilleurs jours, il tombe à 1,6 %.

**Piège fréquent ou erreur courante :** Croire que l'on peut éviter les pires jours tout en captant les meilleurs. Les statistiques montrent que 6 des 10 meilleurs jours sur cette période se sont produits dans les deux semaines exactes entourant l'un des 10 pires jours (comme en mars 2020).

**Source(s) :** J.P. Morgan Asset Management, Guide to Retirement (données arrêtées au 31 décembre 2025). URL : https://am.jpmorgan.com. Consultation le 30 octobre 2026.

## 6. Quelle est la corrélation historique entre actions, obligations et or lors des grandes crises ?

**Réponse courte :** Historiquement, les obligations protègent les portefeuilles lors des crises économiques ou de croissance (corrélation négative), mais elles baissent en même temps que les actions lors des chocs d'inflation (corrélation positive).

**Détail :** Lors de la bulle internet (2000) et de la crise financière (2008), la corrélation a été fortement négative : les actions ont chuté d'environ 50 %, mais les obligations mondiales ont grimpé en raison de la baisse des taux directeurs. En mars 2020, un krach de liquidité a fait tout baisser brièvement, avant que la corrélation négative ne reprenne. En 2022 (choc d'inflation), la corrélation fut positive : les actions ont perdu près de 20 % et les obligations 15 % en raison de la hausse brutale des taux. L'or, lui, s'est maintenu en euros en 2022.

**Piège fréquent ou erreur courante :** Penser que la règle « 60 % actions / 40 % obligations » garantit une protection dans tous les scénarios macroéconomiques, en oubliant l'impact mécanique des taux d'intérêt sur la valeur obligataire.

**Source(s) :** Rapports annuels et données historiques S&P Dow Jones Indices (2000-2022). Consultation le 30 octobre 2026.

## 7. Quel est l'effet du change EUR/USD sur un investisseur français en actions américaines ?

**Réponse courte :** Un investisseur achetant un ETF S&P 500 en euros s'expose à la fois au marché américain et à la fluctuation de la parité euro/dollar. Cet effet de change ajoute de la volatilité annuelle mais a tendance à se compenser partiellement sur le temps long.

**Détail :** En 2022, la baisse de près de 20 % du S&P 500 en dollars a été amortie pour l'investisseur européen (baisse ramenée autour de -13 %) grâce à l'appréciation du dollar face à l'euro. À l'inverse, lors d'une forte appréciation de l'euro (comme entre 2003 et 2007), la performance en euros est pénalisée. Sur 20 ans, le différentiel annualisé lié au change crée généralement un écart de 1 à 2 % par an à la hausse ou à la baisse selon le point d'entrée exact (À VÉRIFIER pour les décimales précises selon les cycles).

**Piège fréquent ou erreur courante :** Payer systématiquement des frais supplémentaires pour un ETF couvert contre le risque de change (hedged) sur un horizon de plus de 15 ans. Le coût technique de la couverture vient souvent dégrader la performance nette de façon garantie, alors que la devise fluctue de façon cyclique.

**Source(s) :** Banque de France (séries statistiques taux de change). Consultation le 30 octobre 2026.

## 8. Quelle est la probabilité qu'un investissement immédiat (Lump Sum) batte un versement échelonné (DCA) ?

**Réponse courte :** L'investissement immédiat et total d'une somme (Lump Sum) génère mathématiquement une performance supérieure au versement progressif (DCA) dans environ deux tiers des scénarios historiques.

**Détail :** D'après une étude de Vanguard sur la période 1976-2022 mesurant un étalement (DCA) sur différentes durées (ex : 3 à 12 mois), le Lump Sum a surperformé dans 68 % des cas. La cause est le coût d'opportunité : les marchés d'actions et d'obligations ont un biais haussier, et conserver une partie du capital en liquidités dans l'attente d'un déploiement freine l'accumulation d'intérêts composés.

**Piège fréquent ou erreur courante :** Ignorer son profil psychologique en se forçant au Lump Sum. Si un krach survient juste après un investissement massif, la douleur émotionnelle peut provoquer une revente en panique. Le DCA reste un excellent outil de gestion émotionnelle.

**Source(s) :** Étude Vanguard, « Cost averaging: Invest now or temporarily hold your cash? », février 2023 (M. Finlay, J. Zorn). URL : https://corporate.vanguard.com. Consultation le 30 octobre 2026.

---

## Ce qui a changé récemment

- **Hausse de la concentration des indices (2024-2025)** : les géants de la technologie américaine (tels qu'Apple, Microsoft et Nvidia) ont pris un poids historique, représentant plus de 20 % de l'indice MSCI World à la fin de l'année 2025.
- **Deux années de rendements exceptionnels** : le marché actions américain a enchaîné d'excellentes années en 2024 et 2025 (le S&P 500 affichant +17,88 % en 2025), ce qui rappelle statistiquement l'importance de s'attendre à un retour cyclique à la moyenne.

## Ce que je n'ai pas pu trancher

- **Données annuelles multi-indices depuis 1970 complètes** : afin d'éviter de fournir des données inexactes, le fichier CSV des rendements annuels contient la mention « À VÉRIFIER » pour les années et les indices dont les données primaires brutes, libres d'accès et non soumises à licence payante (MSCI/S&P) n'ont pas pu être vérifiées de façon agrégée lors de la session. Les données fiabilisées concernent la période 2000-2026 pour le S&P 500.
- **La durée de récupération exacte (en mois) du MSCI World lors du krach de 1973** : bien que la baisse soit documentée (environ -42 %), la date de retour exact au point mort net d'inflation n'a pas pu être validée via une source primaire lors de la recherche et est signalée à vérifier.

## Sources utilisées

- S&P Dow Jones Indices : https://www.spglobal.com/spdji (rendements, composition et historiques des krachs du S&P 500).
- MSCI Inc : https://www.msci.com (factsheets, drawdowns et historique MSCI World).
- J.P. Morgan Asset Management : Guide to the Markets / Guide to Retirement (analyse du market timing, clôture décembre 2025). URL : https://am.jpmorgan.com/sg/en/asset-management/per/insights/retirement-insights/retirement-resources/
- Vanguard Research : « Cost averaging: Invest now or temporarily hold your cash? », 2023. URL : https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf
- Credit Suisse / UBS : Global Investment Returns Yearbook 2023 (par Elroy Dimson, Paul Marsh et Mike Staunton, pour les historiques très long terme depuis 1900).
- Slickcharts : rendements totaux (Total Return) historiques du S&P 500 (données de base utilisées pour le CSV 2000-2026). URL : https://www.slickcharts.com/sp500/returns
- Arbolyo / outils de projection : analyses et calculs annexes MSCI World en euros. URL : https://www.investir-simple.fr/rendement-historique-msci-world
