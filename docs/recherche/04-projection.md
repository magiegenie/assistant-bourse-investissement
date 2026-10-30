# Recherche 04 : hypothèses de projection

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié. Le texte reçu n'avait pas de numérotation ni de date de recherche en tête.
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichier de données associé : `hypotheses-projection.csv` (extrait du texte, tel que fourni).

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

J'ai recalculé les chiffres avec `scripts/projection.py` :

1. **Tableau des frais (100 000 € + 1 000 €/mois, 7 % brut)** : plusieurs résultats du rapport sont faux.

   | Durée | Frais | Rapport | Recalculé |
   |---|---|---|---|
   | 10 ans | 0,1 % | 365 300 € | 365 056 € |
   | 10 ans | 1 % | 348 200 € | 341 558 € |
   | 10 ans | 2 % | 330 300 € | 317 253 € |
   | 20 ans | 0,1 % | 878 900 € | 881 610 € |
   | 20 ans | 1 % | 768 700 € | 774 152 € |
   | 20 ans | 2 % | 662 100 € | 671 134 € |
   | 30 ans | 0,1 % | 1 983 000 € | 1 888 293 € |
   | 30 ans | 2 % | 1 279 000 € | 1 247 570 € |

   La conclusion (« plus du tiers du capital perdu à 2 % sur 30 ans ») reste vraie : environ 34 % avec mes chiffres. Ne pas reprendre les montants du rapport.
2. **Cas chiffré 100 000 € + 2 000 €/mois sur 10 ans** (frais de 0,3 %) : montants nominaux légèrement trop hauts. Recalculés : 447 286 € (bas), 510 794 € (central), 583 925 € (haut), contre 452 700 €, 517 000 € et 591 900 € dans le rapport (environ +1 %).
3. **Valeurs « réelles » du même cas** : le rapport donne 392 300 €, 449 800 € et 517 000 €. Ce sont, à peu près, les résultats obtenus en supposant que les versements de 2 000 € augmentent avec l'inflation, ce qui n'est pas dit. Avec 2 000 € fixes (cas le plus courant), le pouvoir d'achat réel est de 366 930 €, 419 029 € et 479 022 €.
4. **Contradiction avec la recherche 01** : la section fiscalité reprend le PFU à 30 %, les prélèvements sociaux à 17,2 % et une assurance vie à 24,7 %. La recherche 01 donne 31,4 %, 18,6 % et 7,5 % + prélèvements sociaux. À réconcilier.
5. **Monte Carlo** : le rapport met en garde contre la loi normale qui sous-estime les krachs, puis recommande une loi log-normale, qui a aussi des queues fines. Ce n'est pas cohérent. Il faudrait un tirage historique (bootstrap) ou une loi à queues épaisses. La conversion des paramètres est aussi simplifiée (écart-type arithmétique utilisé comme écart-type logarithmique).
6. **Sources** : noms de sites (am.jpmorgan.com, vanguard.com) sans lien vers la publication, aucune date de publication, aucune valeur par publication comme demandé. Les attributions du tableau (« BlackRock », « AQR / Research Affiliates ») sont invérifiables en l'état.
7. **Valeurs du CSV** : écrites avec le signe « % » dans les cellules (« 5.0% »), donc pas directement lisibles par un script.
8. **Manques** : corrélations entre classes d'actifs non chiffrées, effet de la fiscalité sur l'objectif non calculé, rendements attendus des grands gérants non détaillés par publication.

---

## Quels sont les rendements attendus à long terme par les professionnels ?

Les grandes institutions projettent pour les 10 à 15 prochaines années des rendements nominaux annualisés compris entre 5 % et 8,5 % pour les actions mondiales. Les rendements réels, nets d'inflation, se situent généralement entre 3 % et 6 %.

| Classe d'actifs | Nominal (fourchette) | Réel (central) | Volatilité attendue | Source principale (2026) |
|---|---|---|---|---|
| Actions mondiales | 5,0 % à 8,0 % | 4,5 % | 15,0 % | BlackRock (LTCMA) |
| Actions US | 4,5 % à 7,5 % | 4,0 % | 16,0 % | Vanguard (CMM) |
| Actions européennes | 5,5 % à 8,5 % | 5,0 % | 17,0 % | J.P. Morgan |
| Actions émergentes | 6,5 % à 9,5 % | 6,0 % | 22,0 % | AQR / Research Affiliates |
| Obligations d'État | 3,0 % à 5,0 % | 2,0 % | 6,0 % | Vanguard |
| Liquidités | 2,0 % à 3,0 % | 0,5 % | 0,5 % | BCE / Banque de France |

Ces chiffres s'entendent en rendement total (dividendes et coupons réinvestis) sur un horizon de placement long terme. Les marchés américains, ayant connu une valorisation exceptionnelle ces dix dernières années, affichent des espérances de rendement futur souvent révisées à la baisse par rapport à l'Europe ou aux émergents.

Un piège très courant consiste à utiliser la performance passée du S&P 500 sur les 10 dernières années (souvent supérieure à 12 % annualisés) comme hypothèse de base pour les 30 prochaines années, ce qui surestime massivement la projection de capital final.

Sources : J.P. Morgan Long-Term Capital Market Assumptions 2026 (am.jpmorgan.com), Vanguard Capital Markets Model Q1 2026 (vanguard.com).

## Quelle est la volatilité historique et attendue des classes d'actifs ?

La volatilité, mesurée par l'écart-type annuel, quantifie le risque de fluctuation d'un actif autour de sa moyenne. Historiquement, un portefeuille d'actions mondiales fluctue d'environ 15 % par an, tandis que les obligations d'État se limitent à 5 ou 7 %.

Les corrélations entre actions et obligations jouent un rôle central dans l'amortissement de cette volatilité. Dans les simulations Monte Carlo, la corrélation actions-obligations est souvent paramétrée autour de 0,1 à 0,2 pour refléter des régimes d'inflation normalisés. Les actions des pays émergents affichent la volatilité la plus élevée (au-delà de 20 %), mais apportent un léger gain de décorrélation par rapport aux marchés développés.

L'erreur fréquente est d'assumer que les corrélations sont statiques. En période de forte inflation (comme en 2022), la corrélation actions-obligations devient fortement positive, détruisant temporairement la diversification classique des portefeuilles 60/40.

Sources : MSCI World Index Factsheet (msci.com, 2026), rapports de volatilité historique de l'AMF (amf-france.org).

## Quelles sont les méthodes de projection et leurs limites ?

Il existe trois méthodes principales pour projeter un capital : le rendement constant, le tirage historique (bootstrap) et la simulation Monte Carlo paramétrique.

Le rendement constant applique simplement la formule des intérêts composés, ce qui est pédagogique mais occulte totalement le risque de séquence des rendements. Le bootstrap pioche aléatoirement des mois réels du passé, préservant la réalité des chocs mais limitant la projection aux événements déjà connus. La méthode Monte Carlo génère des milliers de trajectoires aléatoires basées sur une distribution statistique, permettant d'observer les scénarios extrêmes et de donner une probabilité de réussite.

Le piège absolu du modèle Monte Carlo paramétrique est d'utiliser une loi normale classique (courbe en cloche) qui sous-estime les queues de distribution (les « fat tails »). Les marchés financiers subissent des krachs extrêmes bien plus souvent que ne le prévoit une loi normale stricte.

Sources : Recommandations de l'AMF sur les simulateurs d'épargne (amf-france.org, 2026).

## Comment intégrer correctement l'inflation dans la projection ?

L'inflation érode silencieusement le pouvoir d'achat du capital, il est donc impératif d'exprimer les objectifs de très long terme en euros constants (réels) plutôt qu'en euros courants (nominaux).

La cible structurelle de la Banque Centrale Européenne est fixée à 2,0 % à moyen terme. En France, selon l'INSEE, l'inflation moyenne de 1990 à 2025 s'établit autour de 1,8 % par an. Pour obtenir le rendement réel, la méthode mathématique exacte consiste à diviser le facteur nominal par le facteur d'inflation : (1 + rendement nominal) / (1 + inflation) - 1. Dans les simulateurs, on retranche souvent simplement le taux d'inflation du taux nominal pour faciliter le calcul.

Une erreur courante est de projeter un million d'euros à 30 ans avec un rendement nominal de 7 %, et de penser que l'on pourra acheter l'équivalent d'un million d'euros de biens d'aujourd'hui. À 2 % d'inflation, un million d'euros dans 30 ans correspond à environ 552 000 € de pouvoir d'achat actuel.

Sources : INSEE - Indice des prix à la consommation (insee.fr), Banque Centrale Européenne (ecb.europa.eu).

## Quel est l'effet des frais de gestion sur le capital à long terme ?

Les frais annuels agissent comme un rendement négatif composé qui confisque une part exponentielle de la richesse finale au fil des décennies.

Pour un capital de départ de 100 000 € et un versement de 1 000 € par mois, en supposant un rendement brut des marchés de 7 % (calculé ici en capitalisation mensuelle pour plus de précision) sur différentes durées, voici l'impact net de frais :

- Sur 10 ans : 0,1 % de frais génère 365 300 € / 1,0 % donne 348 200 € / 2,0 % donne 330 300 €.
- Sur 20 ans : 0,1 % de frais génère 878 900 € / 1,0 % donne 768 700 € / 2,0 % donne 662 100 €.
- Sur 30 ans : 0,1 % de frais (net 6,9 %) génère environ 1 983 000 €. Des frais de 2 % (net 5,0 %, typiques d'une assurance-vie en gestion pilotée avec fonds actifs) aboutissent à 1 279 000 €.

Le piège mental est de juger qu'une différence de 2 % de frais ne représente que « 2 % de perte ». Sur 30 ans, ces 2 % de frottement détruisent plus du tiers du capital final par rapport à une solution indicielle low-cost (ETF).

Sources : calculs financiers purs (formule de capitalisation), Observatoire de l'épargne de l'AMF.

## Comment intégrer la fiscalité à la sortie dans les enveloppes françaises ?

La fiscalité ne s'applique jamais sur l'encours total, mais exclusivement sur la part de plus-value contenue dans le retrait (l'assiette de taxation).

Sur un Plan d'Épargne en Actions (PEA) de plus de 5 ans, les gains sont exonérés d'impôt sur le revenu mais supportent les prélèvements sociaux (17,2 %). Sur une assurance vie de plus de 8 ans, après l'abattement annuel de 4 600 € (célibataire) ou 9 200 € (couple), les plus-values sont taxées à 24,7 % (7,5 % d'impôt + 17,2 % de prélèvements sociaux) pour les versements inférieurs à 150 000 €. Sur un Compte-Titres Ordinaire (CTO), la flat tax s'applique à hauteur de 30 % sur les plus-values.

L'erreur de modélisation classique est de retrancher 30 % au capital total à la fin de la simulation. La taxation fiscale doit être pondérée par la proportion exacte de gains générés par rapport aux versements totaux cumulés.

Sources : Code Général des Impôts (legifrance.gouv.fr), service-public.fr (octobre 2026).

## Quels paramètres utiliser pour un simulateur Monte Carlo en Python ?

Pour un outil robuste destiné aux épargnants français, la modélisation doit reposer sur une distribution log-normale et utiliser des paramètres de rendement net d'inflation ou à inflation déterministe.

Paramètres recommandés : utiliser un rendement nominal moyen (μ) de 6,5 % (ou 4,5 % en réel) et un écart-type (σ) de 16 % pour un portefeuille 100 % actions mondiales. Le modèle Python (`numpy.random.lognormal`) nécessite de convertir ces taux : l'espérance de la loi normale sous-jacente s'écrit ln(1+μ) - σ²/2. Un minimum de 10 000 trajectoires (tirages) est indispensable pour stabiliser statistiquement les centiles extrêmes (le 1er et le 99e).

Le piège technique est de modéliser avec un simple mouvement brownien arithmétique (distribution normale pure). Sur des horizons de 30 ans, ce modèle peut générer des prix d'actifs négatifs lors des pires tirages, ce qui est financièrement impossible pour des actions non endettées.

Sources : mathématiques quantitatives de base (Paul Wilmott), documentations numpy / scipy.stats.

## Comment expliquer la probabilité de réussite d'une projection à un débutant ?

Une projection financière ne doit jamais fournir un chiffre final unique, mais exprimer la réalité du risque par des paliers de probabilité facilement tangibles.

Plutôt que d'afficher la moyenne mathématique, il faut vulgariser les centiles. Exemple : « Dans le scénario médian (50 % de chances), vous obtiendrez 500 000 €. Dans un scénario très défavorable (historiquement, 9 chances sur 10 de faire mieux), votre capital de sécurité s'élèvera à 350 000 €. » Cette approche ancre les attentes de l'investisseur sur le pire scénario probable (le 10e centile) plutôt que sur le scénario idéal.

L'erreur fréquente est de mettre en avant la moyenne des trajectoires. En raison de la composition des intérêts et de l'asymétrie des rendements positifs, la moyenne (l'espérance) est tirée vers le haut par quelques trajectoires exceptionnelles, dépassant largement la médiane que la majorité des épargnants connaîtront.

Sources : Recommandations de l'ACPR sur les bonnes pratiques de commercialisation et d'information (acpr.banque-france.fr).

## Cas chiffré complet sur 10 ans : départ 100 000 € et 2 000 € / mois ?

En utilisant une capitalisation mensuelle rigoureuse, avec 0,3 % de frais d'ETF déduits des rendements bruts des institutions. Capital initial investi : 100 000 €. Somme totale placée au bout de 10 ans : 340 000 €.

- **Scénario bas** (rendement brut 4,5 % / net nominal 4,2 % / net réel 2,2 %) : le capital atteint environ 452 700 € en valeur nominale. Corrigé de l'inflation à 2 %, le pouvoir d'achat équivaut à 392 300 €.
- **Scénario central** (rendement brut 6,5 % / net nominal 6,2 % / net réel 4,2 %) : le capital nominal est de 517 000 €. Le pouvoir d'achat réel s'établit à environ 449 800 €.
- **Scénario haut** (rendement brut 8,5 % / net nominal 8,2 % / net réel 6,2 %) : le capital nominal bondit à 591 900 €. Le pouvoir d'achat réel atteint 517 000 €.

Le piège ici est d'oublier qu'un horizon de 10 ans pour 100 % d'actions est en réalité assez court. Le « scénario bas » présenté correspond à une moyenne long terme pessimiste, et non à un véritable krach de fin de période (séquence des rendements négative).

Sources : calculs financiers (formule mathématique de valeur future avec paiements mensuels constants).

---

## Ce qui a changé récemment

Depuis la normalisation des taux directeurs de la BCE intervenue courant 2024-2025, les rendements de la classe obligataire et du monétaire ont retrouvé des niveaux durablement positifs après une décennie de taux zéro ou négatifs. Parallèlement, l'inflation française a convergé vers la cible des 2 % post-crise énergétique. Les grands gestionnaires d'actifs ont en conséquence rehaussé la valeur défensive des obligations dans l'allocation d'actifs des simulations de long terme.

## Ce que je n'ai pas pu trancher

La survie juridique et fiscale du PFU (flat tax de 30 %) sur un horizon de 30 ans. La législation fiscale française (loi de finances) étant débattue et amendée annuellement, intégrer un taux fixe de 30 % dans un simulateur jusqu'en 2056 relève d'une convention statistique, non d'une garantie juridique. De même, l'impact macroéconomique du réchauffement climatique sur les rendements actions à horizon 2050 divise encore profondément les modèles des instituts de recherche.

## Sources utilisées

- J.P. Morgan Asset Management (LTCMA) : am.jpmorgan.com (consulté le 30 octobre 2026)
- Vanguard (Capital Markets Model) : vanguard.com (consulté le 30 octobre 2026)
- BlackRock Investment Institute : blackrock.com (consulté le 30 octobre 2026)
- Autorité des Marchés Financiers (AMF) : amf-france.org (consulté le 30 octobre 2026)
- Institut National de la Statistique et des Études Économiques (INSEE) : insee.fr (consulté le 30 octobre 2026)
- Banque Centrale Européenne (BCE) : ecb.europa.eu (consulté le 30 octobre 2026)
- Fiscalité française et Code Général des Impôts : service-public.fr et impots.gouv.fr (consulté le 30 octobre 2026)
