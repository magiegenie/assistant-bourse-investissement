---
name: manuel-analyste
description: Manuel de compétences de l'Analyste : bilan de portefeuille, rééquilibrage, performance, frais, chevauchements d'ETF, graphiques. Réservé à l'agent analyste.
---

# Manuel de compétences de l'Analyste

Fusion des meilleurs skills open source (Anthropic en priorité, puis joellewis, lyndonkl, onewave, staskh), adaptés à un particulier français, à ses ETF et à nos règles : **aucun avis d'achat ou de vente, aucun objectif de cours, aucune prédiction**. Les calculs passent par `scripts/`. Ouvre seulement la section utile. Sources et tri complet : fin de fichier et `docs/externe/tri-des-skills.csv`.

## 1. Bilan et rapport de portefeuille
*Base : `client-report`, `client-review` (Anthropic), `performance-reporting`, `portfolio-analyzer`.*
- Structure : (1) résumé en une page ; (2) performance du portefeuille contre l'indice de référence **choisi dans la charte, pas celui qui flatte** (`scripts/performance.py`) ; (3) allocation actuelle contre cible, écart par poche, alerte au-delà du seuil (`scripts/allocation.py`) ; (4) lignes détaillées avec poids et frais ; (5) commentaire de marché en 2-3 phrases sans jargon ; (6) activité de la période : versements, retraits, dividendes, frais, rééquilibrages ; (7) avancement vers chaque objectif ; (8) points d'attention et prochaine date de revue.
- **Net de frais** par défaut. Dire « sur moins d'un an, ce n'est pas significatif ».
- Si la performance est mauvaise : le dire directement, avec le contexte (marché, concentration), sans l'enjoliver.
- Ordre de la revue périodique : où on en est, pourquoi, que décider, et **des actions datées** pour la prochaine fois. Partir de ce qui compte pour la personne, pas de ce qu'on veut présenter.
- Contributeurs : les 3 lignes qui ont le plus contribué et les 3 qui ont le plus pesé ; repérer toute ligne dont l'effet est démesuré.
- Format : tableau de bord d'une page, tableur (section 18) ; garder les bilans datés dans `bilans.md` sans effacer les précédents.

## 2. Rééquilibrage
*Base : `rebalancing`, `portfolio-drift-rebalancer`.*
- **Par les flux d'abord** : diriger 100 % du versement vers la poche la plus en retard (`allocation.py`). C'est le moins cher, sans impôt.
- Deux déclencheurs : **calendrier** (annuel suffit) ou **seuil** (écart absolu de 3 à 5 points, ou 20-25 % relatif). Une règle combinée : regarder une fois par an, ne vendre que si le seuil est franchi.
- Bandes **plus larges** si les frais ou l'impôt sont élevés (CTO), **plus étroites** si l'actif est volatil ou si la personne est très prudente (intuition de Leland : coût de transaction fort, bande large).
- Une prime de rééquilibrage existe (acheter bas, vendre haut) mais **n'est pas un repas gratuit** : elle disparaît quand un actif monte durablement.
- Si vente : `scripts/reequilibrage.py`. Ordre : PEA et assurance vie (arbitrage non imposé), CTO en moins-value, CTO avec la plus petite plus-value ; réinvestir dans la **même enveloppe** ; montrer le coût fiscal ; vérifier achats = ventes ; ne jamais exécuter.
- Piège : rééquilibrer trop souvent ; ignorer la fiscalité du CTO ; croire qu'un écart de 2 points est un problème.

## 3. Diversification
*Base : `diversification`.*
- Le gain de diversification dépend de la **corrélation**, pas du nombre de lignes. Deux ETF sur les mêmes grandes valeurs diversifient peu (`scripts/exposition.py`).
- Les corrélations ne sont pas stables : en crise, elles montent ; en 2022, actions et obligations ont baissé ensemble.
- Mesures : ratio de diversification (risque moyen des lignes / risque du portefeuille), contribution de chaque ligne au risque total. Une ligne à 5 % du poids qui fait 15 % du risque est un signal.
- Rendements décroissants : au-delà de quelques lignes bien choisies, la diversification supplémentaire est marginale (fiche D, point 28).

## 4. Mesure de performance
*Base : `performance-metrics`, `performance-attribution`, `return-calculations`, `statistics-fundamentals`, `returns-analysis`.*
- Rendement réel : taux de rendement interne (XIRR) après frais et versements ; ne pas confondre avec un rendement annuel moyen.
- Ratios, à n'utiliser que pour **comparer** deux portefeuilles sur la même période : **Sharpe** (rendement excédentaire / volatilité), **Sortino** (ne compte que la baisse), **Calmar** (rendement / pire baisse), part de hausse et de baisse capturée contre l'indice.
- Attribution : ce qui vient de l'allocation, de la sélection et des frais.
- Statistiques : médiane plutôt que moyenne quand les rendements sont asymétriques, percentiles pour les scénarios ; ne pas tirer de conclusion de peu de données.
- Dire toujours la période et si c'est avant ou après impôt.

## 5. Risque historique
*Base : `historical-risk`, `volatility-modeling`.*
- Volatilité annualisée, **pire baisse** (drawdown), perte historique à 95 % (« 1 mois sur 20 fait pire que... »), écart à la baisse, erreur de suivi.
- La volatilité du passé sous-estime les crises : compléter par `scripts/stress.py`.
- Une baisse de 50 % demande +100 % pour revenir : toujours le dire avec un chiffre en euros.

## 6. Choisir un fonds ou un ETF
*Base : `fund-vehicles`.* Critères dans l'ordre (fiche D, points 27 et 58 à 60) : écart de suivi, frais, encours, réplication, domiciliation, devise, capitalisant ou distribuant, éligibilité PEA. Fonds actif : jamais sans comparer à l'indice et aux frais ; la grande majorité des fonds actifs fait moins bien que son indice à 10 ans. Fonds à échéance et fonds obligataires : lire la duration.

## 7. Fiche entreprise (fondamentaux)
*Base : `equity-research`, `tear-sheet`, `equities`, `fundamentals`, `sec-filing-puller`, `company-classification-routing`. Retiré : recommandation, objectif de cours, « idées de trades ».*
Pour une action en direct (satellite) ou pour comprendre un titre présent dans ses ETF :
1. **Qui est-ce** : activité, secteur, taille, stade de vie (croissance, maturité, déclin), pays.
2. **Consensus** des analystes (nombre, dispersion) : à lire comme « ce que le marché attend déjà », pas comme une recommandation.
3. **Chiffres sur 3 à 5 ans** : croissance du chiffre d'affaires, marge brute, marge opérationnelle, rendement des capitaux (ROE, ROIC), dette nette / résultat d'exploitation.
4. **Valorisation** : PER prospectif, valeur d'entreprise / résultat d'exploitation, rendement du dividende, **comparés au secteur et à son propre historique**.
5. **Parcours en bourse** : rendement depuis le début d'année et sur 1 an, position dans la fourchette sur 52 semaines, volatilité.
6. **Contexte macro** du pays et du secteur : vent favorable ou contraire.
7. **Ce qu'elle pèse déjà dans le portefeuille** via les ETF (`exposition.py`) et le plafond de 5 % par ligne.
- Chaque chiffre : source, date. Sources de données : `financial-data` (fondamentaux, cours), sites officiels des sociétés et AMF ; données SEC pour les sociétés américaines.
- Conclusion autorisée : « voici les faits et ce qui les rend chers ou bon marché par rapport à leur histoire ». Interdite : « achète », « objectif de cours », « sous-évalué ».
- Remettre la fiche au Coach pour le garde-fou si la personne veut acheter.

## 8. Lire les résultats d'une entreprise
*Base : `earnings-analysis`, `earnings-preview`.*
- **Vérifier la date du jour** et que la publication est bien la plus récente ; vérifier que le compte rendu d'appel correspond à la bonne période. Les connaissances de mémoire sont périmées : tout chiffre vient d'une source datée.
- Tableau : indicateur, attendu, publié, écart (chiffre d'affaires, bénéfice par action, indicateur clé, prévisions de l'entreprise). Puis : les prévisions ont-elles changé ? la qualité du bénéfice est-elle bonne (flux de trésorerie) ?
- Avant une publication : ce qui est attendu, scénarios et seuils à surveiller ; après : ce qui a surpris. Toujours terminer par « est-ce que ça change quelque chose pour mon plan ? » (presque jamais pour un ETF monde).
- Sources cités avec lien précis. Pas de « thèse d'investissement » ni de note à publier.

## 9. Lire les états financiers
*Base : `financial-statements`, `3-statement-model`, `financial-statement-normalization`, `spreadsheet-model-auditor`.*
- **Compte de résultat** (la société gagne-t-elle de l'argent ?), **bilan** (que possède-t-elle et que doit-elle ?), **flux de trésorerie** (d'où vient l'argent, que devient-il ?). Les trois doivent « se parler » : le bilan équilibre, la trésorerie finale du tableau de flux égale celle du bilan, le résultat net alimente les capitaux propres.
- Ratios utiles : marge nette, croissance, dette nette / résultat d'exploitation (prudence au-delà de 3-4, selon le secteur), couverture des intérêts, rendement des capitaux, flux de trésorerie disponible, conversion du résultat en trésorerie.
- Retraitements utiles (niveau avancé) : traiter la R&D et les loyers comme des investissements pour comparer des sociétés ; ne pas se fier à un résultat « ajusté » sans le rapprocher du résultat publié.
- Alertes : bénéfice sans trésorerie, dette croissante plus vite que l'activité, créances qui gonflent, changement de méthode comptable.

## 10. Valorisation par comparaison
*Base : `comps-analysis`, `relative-valuation-toolkit`.*
- Choisir 5 à 10 sociétés vraiment comparables (même activité, taille, croissance, pays).
- Multiples : PER, PEG, valeur d'entreprise / résultat d'exploitation, / chiffre d'affaires, prix / valeur comptable. Pour chacun : **médiane et quartiles** du groupe, pas seulement la moyenne.
- Hiérarchie des données : sources officielles et bases de données financières d'abord, recherche web en dernier recours, avec date.
- **Formules plutôt que valeurs collées** dans un tableur, et chaque ratio calculé à partir des cellules sources (jamais saisi deux fois). Montrer et vérifier les marges avant de passer à la valorisation.
- Un multiple bas n'est pas « bon marché » : l'expliquer (croissance, risque, qualité).

## 11. Valorisation par les flux (DCF), pour comprendre, pas pour prévoir
*Base : `dcf-model`, `dcf-valuation-engine`, `cost-of-capital-toolkit`, `valuation-red-team`, `valuation-consistency-checks`, `monte-carlo-valuation`.*
- Principe : valeur = flux futurs ramenés à aujourd'hui. Très sensible à deux hypothèses : taux d'actualisation (coût du capital) et croissance à l'infini (jamais supérieure à celle de l'économie).
- Faire une **table de sensibilité** dont la case centrale est le cas de base ; une variation d'un point change fortement le résultat, ce qui montre la fragilité de tout « prix juste ».
- Contrôles : devise cohérente entre flux et taux d'actualisation ; nombre d'actions dilué ; cohérence croissance, marges, réinvestissement ; part de la valeur finale dans le total (si elle dépasse 75-80 %, méfiance).
- **Contre-expertise** : chercher activement ce qui rend la valorisation fausse, vérifier que chaque risque est chiffré, que la conclusion n'était pas décidée avant le calcul.
- Mieux qu'un chiffre : une **fourchette** (loi de probabilité des hypothèses les plus incertaines). Ne jamais présenter un résultat comme objectif de cours.

## 12. Avantage concurrentiel, gouvernance, dividendes
*Base : `competitive-analysis`, `qualitative-valuation`, `corporate-governance-analysis`, `payout-policy-analysis`, `narrative-to-numbers`.*
- Avantage durable : coûts de changement, effet de réseau, marque, coûts, échelle, brevets. Se mesure à des marges et un rendement des capitaux supérieurs sur 10 ans.
- Gouvernance : qui contrôle (actions à droit de vote multiple, famille, État), indépendance du conseil, rémunération des dirigeants, transactions avec des proches.
- Dividendes et rachats : la société rend-elle la bonne somme (flux de trésorerie après investissements) ? Un dividende payé par de la dette est un signal d'alerte.
- Relier l'histoire de l'entreprise aux chiffres (marché, croissance, marge, réinvestissement) : une belle histoire sans chiffres n'est pas une analyse.

## 13. Poche obligataire
*Base : `fixed-income-portfolio`, `fixed-income-corporate`, `fixed-income-sovereign`.*
- Risques : taux (le prix baisse quand les taux montent, d'autant plus que la **duration** est longue ; duration 7, taux +1 point : environ -7 %), crédit (défaut, écart de rendement), inflation, change.
- Fonds en euros (capital garanti, rendement servi par l'assureur) contre ETF obligataire (valeur qui bouge, rendement marché) : fiche D, point 23.
- À regarder : duration, notation moyenne, devise (version couverte ou non), frais.

## 14. Or, matières premières, immobilier, crypto-actifs
*Base : `commodities`, `real-assets`, `alternatives`, `digital-assets`.* Optionnels, rôle d'assurance ou de diversification limité, frais ou fiscalité lourds : fiche D, points 24 et 63. L'or n'a pas de rendement propre ; les matières premières ont un rendement réel historique proche de zéro ; l'immobilier coté (SCPI, foncières) a des frais d'entrée élevés et une fiscalité au barème ; les crypto-actifs peuvent perdre 80 %.

## 15. Facteurs
*Base : `factor-investing`.* Primes historiques (valeur, petites capitalisations, qualité, momentum) : réelles sur le long terme mais capricieuses, parfois absentes pendant 10 ans. Pour un particulier : un ETF monde large capte déjà l'essentiel ; un ETF de facteur est un pari assumé, au plus dans le satellite.

## 16. Exposition aux devises
*Base : `currencies-and-fx`.* Part en dollars via `exposition.py` ; couverture coûteuse (différentiel de taux) et rarement utile à long terme (fiche D, point 26).

## 17. Taille maximale d'une ligne
*Base : `bet-sizing`.* Règle simple : 5 % du total au maximum par action en direct, calculé **après** achat (fiche E, point 32). Le critère de Kelly est réservé aux paris à probabilités connues : il ne s'applique pas à la bourse, on n'utilise que son idée de prudence (fraction, jamais le plein montant). Budget de risque : une ligne ne doit pas apporter plus de risque que sa part dans la charte.

## 18. Livrables tableur fiables
*Base : `audit-xls`, `xlsx-author`, `clean-data-xls`, `spreadsheet-model-auditor`, `csv-excel-merger`.*
- Générer le classeur avec `scripts/creer_sheet.py` (modèle `templates/`), sans manipuler un tableur ouvert.
- Contrôles avant de rendre : formules sans erreur (#REF, #DIV/0), pas de valeur collée à la place d'une formule, totaux qui se recoupent (somme des lignes = total, poids = 100 %), unités et devises cohérentes, dates au bon format, nombres stockés comme du texte corrigés, doublons supprimés.
- Gravité : **critique** (le résultat est faux), **avertissement**, **information**. Un classeur jugé propre doit avoir 0 critique.

## 19. Lire un relevé de courtier
*Base : `pdf-statement-parser`, `statement-extract-and-prove`.* Extraire lignes, quantités, valeurs et dates d'un relevé (PDF, export du courtier) vers `positions.csv`, puis **prouver** : somme des lignes = total du relevé, flux = variation du solde. Si un écart subsiste, le signaler au lieu de le masquer.

## 20. Graphiques honnêtes
*Base : `cognitive-fallacies-guard`, `visualization-choice-reporting`.* Axe qui part de zéro pour les barres, même échelle pour comparer, pas de double axe trompeur, indiquer période et devise, un message par graphique, annoter l'événement qui explique une cassure. Barres pour comparer des montants, lignes pour une évolution, camembert seulement pour 2 à 4 parts.

## Données de marché
Voir le manuel du Veilleur, section 9 : citer source, heure, devise ; jamais de décision sur un seul chiffre.

---
Sources : anthropics/financial-services-plugins (Apache 2.0) : client-report, client-review, equity-research, tear-sheet, earnings-analysis, earnings-preview, comps-analysis, dcf-model, 3-statement-model, audit-xls, xlsx-author, clean-data-xls, fixed-income-portfolio, returns-analysis. joellewis/finance_skills (MIT) : rebalancing, diversification, performance-metrics, performance-attribution, performance-reporting, return-calculations, statistics-fundamentals, historical-risk, volatility-modeling, fund-vehicles, equities, factor-investing, financial-statements, quantitative-valuation, qualitative-valuation, fixed-income-*, commodities, real-assets, alternatives, digital-assets, currencies-and-fx, bet-sizing, data-quality. onewave-ai (MIT) : portfolio-analyzer, spreadsheet-model-auditor, statement-extract-and-prove, csv-excel-merger, sec-filing-puller, executive-dashboard-generator. staskh (MIT) : fundamentals, report-stock. lyndonkl (pas de licence, idées reformulées) : portfolio-drift-rebalancer, relative-valuation-toolkit, dcf-valuation-engine, cost-of-capital-toolkit, valuation-red-team, valuation-consistency-checks, monte-carlo-valuation, financial-statement-normalization, company-classification-routing, corporate-governance-analysis, payout-policy-analysis, narrative-to-numbers, pdf-statement-parser, cognitive-fallacies-guard, visualization-choice-reporting.
