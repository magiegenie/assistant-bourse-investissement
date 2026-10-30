# Recherche 06b : allocation d'actifs (version B)

- Origine : recherche externe (autre IA ou autre session), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié. Même sujet que `06-allocation.md`.
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichier de données associé : `allocations-types-b.csv` (extrait du texte, tel que fourni).

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

Différences avec la version A, à trancher :

| Point | Version A | Version B |
|---|---|---|
| Date de la mise à jour Bessembinder | juillet 2026 | 15 mars 2026 |
| Part des États-Unis dans le MSCI World | 70,3 % | 72 % (septembre 2026) |
| Top 10 du S&P 500 | 37,7 % | plus de 39 % (sommet de 40,7 % fin 2025) |
| Top 10 du MSCI World | 26,6 % | près de 28 % |
| Sous-performance Barber et Odean | 11,4 % contre 17,9 % | « environ 6,5 % par an » (c'est la différence des deux chiffres) |
| Rendement 100 % actions monde 2000-2026 | 8-9 % pour le profil dynamique | 9 % (« en euros »), pire baisse de -53,6 % |

1. **Mêmes limites que la version A** sur la fiscalité (PFU à 30 %, PS à 17,2 %, en contradiction avec la recherche 01) et sur la mise à jour de Bessembinder. La source de l'étude est un site tiers (theideafarm.com), pas l'auteur ni SSRN. Je ne peux pas confirmer l'existence ni les chiffres de cette mise à jour (91 000 milliards de dollars, 46 entreprises).
2. **Rendement de 9 %** annualisé pour un indice 100 % actions mondiales en euros sur 2000-2026 : plus haut que ce que je connais de cet indice sur la période. À vérifier avec les données de MSCI.
3. **CSV** : « Dynamique (100 %) » est étiqueté 100 % mais la répartition est 90 % monde + 10 % émergents (donc 100 % d'actions, cohérent). Rendement, volatilité et pire baisse restent non sourcés.
4. **Bitcoin** : -93,8 % en 2011, -84 % en 2018, -77 % en 2022 (la version A ne cite pas 2011). Cohérent avec ce que je connais, source citée : CoinMarketCap / Binance, peu fiable.
5. **Coût de la couverture de change** : justifié par le différentiel de taux (à vérifier selon l'époque, il peut s'inverser).

---

## 1. Quelle part d'actions dois-je détenir selon mon âge et mon horizon d'investissement ?

La part des actions doit décroître à l'approche du besoin de consommer le capital (retraite, achat immobilier) pour sécuriser le portefeuille. Sur un horizon de plus de 10 ans, une allocation très majoritairement en actions est recommandée car le temps lisse le risque historique de perte.

**Détail :** La règle mathématique de « 100 moins l'âge » (ex. : 70 % d'actions à 30 ans) est aujourd'hui obsolète face à l'allongement de l'espérance de vie. Les gérants de fonds à date cible institutionnels ciblent désormais des allocations de type « 110 ou 120 moins l'âge ». Pour un investisseur de 30 ans : à 10 ans d'horizon, une part de 60 à 80 % d'actions est défendable ; à 20 ou 30 ans d'horizon, une part de 80 à 100 % en actions est rationnelle.

**Piège fréquent ou erreur courante :** Appliquer une allocation 100 % actions uniquement basée sur son jeune âge, sans évaluer sa tolérance psychologique face à un krach.

**Source(s) :** Vanguard, « Vanguard's approach to target-date funds », consulté en 2026 (https://investor.vanguard.com/investor-resources-education).

## 2. Comment évaluer ma véritable tolérance au risque ?

Le risque se définit sous deux dimensions : la « capacité » financière à encaisser une perte (patrimoine, revenus stables, horizon) et la « tolérance » psychologique (capacité à ne pas paniquer). La dimension la plus conservatrice des deux doit dicter l'allocation finale.

**Détail :** Les questionnaires réglementaires imposent des mises en situation quantifiées. Une question type demande : « Si votre portefeuille perd 20 % en un mois, quelle est votre réaction ? » (acheter, ne rien faire, tout vendre). Selon la grille d'interprétation de l'AMF (2026), un investisseur ayant une capacité financière de 100 % en actions mais répondant vouloir « tout vendre » lors d'une baisse de 10 % sera orienté vers un profil prudent.

**Piège fréquent ou erreur courante :** Remplir un questionnaire de risque au milieu d'un marché haussier (bull market), surestimer son courage, et capituler en vendant au point le plus bas lors d'une crise.

**Source(s) :** AMF, doctrine sur l'évaluation de l'adéquation, consulté le 30 octobre 2026 (https://www.amf-france.org).

## 3. À quelle fréquence dois-je rééquilibrer mon portefeuille ?

Le rééquilibrage sert à contrôler l'exposition au risque du portefeuille lorsque les marchés modifient le poids initial des actifs, et non à booster la performance. Il s'opère en vendant ce qui a monté pour racheter ce qui a baissé.

**Détail :** Selon une étude de Vanguard (2026), il n'existe pas de fréquence parfaite : les rendements ajustés au risque sont similaires, que le rééquilibrage soit mensuel, trimestriel ou annuel. La norme institutionnelle recommande un rééquilibrage annuel ou dès qu'un actif dévie de son seuil cible de 5 points de pourcentage. En France (PEA, CTO), le moyen le moins coûteux (fiscalité et frais) est de rééquilibrer par l'allocation des flux d'épargne mensuels entrants vers l'actif en retard.

**Piège fréquent ou erreur courante :** Rééquilibrer son CTO mensuellement par des ventes, ce qui déclenche un frottement fiscal immédiat (flat tax) et détruit le rendement composé.

**Source(s) :** Vanguard, « Best practices for portfolio rebalancing », 2026 (https://investor.vanguard.com/investor-resources-education/portfolio-management/rebalancing-your-portfolio).

## 4. Faut-il construire un portefeuille « satellite » d'actions individuelles ?

L'approche « cœur-satellite » consiste à placer la majorité (80-90 %) dans des indices mondiaux et le reste dans des convictions personnelles. Bien que ludique, cette approche détruit statistiquement de la valeur pour le particulier.

**Détail :** La dernière mise à jour de l'étude Bessembinder (mars 2026) sur la période 1926-2025 révèle que seulement 46 entreprises sont responsables de la moitié de toute la création de richesse boursière américaine (91 billions de dollars). Dénicher ces entreprises à l'avance est quasi impossible. Les études de Barber et Odean (2000) chiffrent la sous-performance des investisseurs particuliers très actifs à environ 6,5 % par an par rapport au marché. Une ligne individuelle ne devrait jamais dépasser 5 % du total.

**Piège fréquent ou erreur courante :** Renforcer aveuglément son « satellite » avec ses économies après un gain chanceux initial, transformant un pari mineur en un risque de concentration majeur.

**Source(s) :** H. Bessembinder, « One Hundred Years in the U.S. Stock Markets », 15 mars 2026 (https://theideafarm.com/markets/one-hundred-years-in-the-u-s-stock-markets/) ; Barber & Odean, « Trading Is Hazardous to Your Wealth » (Journal of Finance).

## 5. Quel est le rôle des obligations et des fonds en euros en France ?

Ces supports servent de stabilisateurs face aux tempêtes boursières. En France, le fonds en euros logé en assurance vie offre un double avantage d'amortisseur et de garantie en capital.

**Détail :** Le fonds en euros protège du risque de remontée des taux d'intérêt, l'assureur absorbant la perte en capital. Son rendement, net de frais de gestion, gravite entre 2,5 % et 3,0 % (chiffres France Assureurs 2025-2026, À VÉRIFIER en clôture d'année). Un ETF obligataire comporte un risque de taux (la valeur de la part baisse quand les taux montent, mesuré par la duration) et un risque de crédit, avec un rendement espéré long terme de 2 à 4 % nominal.

**Piège fréquent ou erreur courante :** Croire qu'un ETF obligataire garantit le capital à tout instant comme un Livret A, et vendre à perte lors d'une hausse brutale des taux directeurs.

**Source(s) :** France Assureurs (estimations annuelles) ; impots.gouv.fr (fiscalité assurance vie).

## 6. Dois-je inclure de l'or, de l'immobilier ou des matières premières ?

Ces actifs peuvent agir comme agents décorrélants mais ne sont pas obligatoires pour la constitution d'un patrimoine boursier performant. Ils impliquent de fortes contraintes fiscales et tarifaires en France.

**Détail :** L'or (0 % de rendement endogène) est une assurance de portefeuille. L'immobilier papier (SCPI) supporte des frais d'entrée lourds de l'ordre de 8 à 12 %. Hors enveloppe fiscale protectrice, les revenus des SCPI supportent la TMI de l'investisseur majorée des prélèvements sociaux de 17,2 %, érodant fortement le rendement net (jusqu'à plus de 60 % de ponction).

**Piège fréquent ou erreur courante :** Sur-pondérer l'or par peur de l'inflation au détriment des actions (qui, elles, s'ajustent à l'inflation via leurs prix de vente), ou souscrire à crédit à des SCPI sans simuler l'impôt net.

**Source(s) :** Code général des impôts (barème IR), AMF (frais des SCPI), 2026.

## 7. Les crypto-actifs ont-ils leur place dans une allocation long terme ?

En raison de leur volatilité extrême, s'ils sont ajoutés au portefeuille, les crypto-actifs ne devraient représenter qu'une proportion marginale (1 à 5 % maximum) assumée à 100 % en perte potentielle.

**Détail :** Historiquement, le Bitcoin a connu des baisses maximales dévastatrices : -93,8 % en 2011, -84 % en 2018, et -77 % lors du krach de 2022. La corrélation du Bitcoin avec les indices boursiers technologiques s'est renforcée, limitant son pouvoir de décorrélation. La fiscalité applicable en France sur la cession vers une devise fiat est le Prélèvement Forfaitaire Unique de 30 %.

**Piège fréquent ou erreur courante :** Laisser un montant significatif de cryptomonnaies sur une plateforme d'échange non réglementée au lieu d'un portefeuille froid (cold wallet), s'exposant au risque de faillite de la plateforme.

**Source(s) :** CoinMarketCap / Binance, historiques de « drawdown » Bitcoin (consulté en octobre 2026) ; impots.gouv.fr pour le PFU.

## 8. Dois-je couvrir le risque de change (hedging) sur un portefeuille mondial ?

Pour un portefeuille en actions de long terme (au-delà de 15-20 ans), la couverture au risque de change n'est pas nécessaire et s'avère coûteuse.

**Détail :** Le MSCI World expose l'investisseur de la zone euro à environ 72 % d'actifs cotés en dollars (chiffre septembre 2026). La couverture (hedged) coûte à l'investisseur la différence des taux d'intérêt entre la BCE et la Fed, grevant la performance de long terme. Lors d'un krach, le dollar agit presque toujours comme une valeur refuge qui s'apprécie face à l'euro, l'exposition « non couverte » amortissant alors la chute de l'actif en bourse.

**Piège fréquent ou erreur courante :** Acheter systématiquement la version « EUR Hedged » d'un ETF Monde par peur des fluctuations monétaires quotidiennes.

**Source(s) :** MSCI, méthodologie des indices et études sur l'impact des devises.

## 9. Quel risque de concentration se cache dans un indice « diversifié » ?

La diversification d'un portefeuille mondial est aujourd'hui trompeuse en raison du poids exceptionnellement élevé du secteur technologique américain lié à l'intelligence artificielle.

**Détail :** Les États-Unis représentent aujourd'hui 72 % de l'indice MSCI World (septembre 2026), contre à peine 30 % vers la fin des années 1980. Le top 10 des entreprises de l'indice MSCI World pèse près de 28 %, et le top 10 de l'indice S&P 500 dépasse 39 % (fin septembre 2026, avec un sommet récent de 40,7 % fin 2025).

**Piège fréquent ou erreur courante :** Croire diversifier son portefeuille en cumulant un ETF Nasdaq 100, un ETF S&P 500 et un ETF MSCI World, alors que leurs performances sont dominées par les 7 mêmes entreprises gigantesques (Apple, Microsoft, Nvidia, etc.).

**Source(s) :** Factsheets MSCI World (30 septembre 2026, https://www.msci.com) et State Street SPDR S&P 500 (septembre 2026, https://www.ssga.com).

## 10. Quelles seraient des allocations types illustratives et leurs risques historiques ?

Une allocation « prudente » cherche la préservation face aux chocs (majorité d'obligataire), une « équilibrée » cherche un compromis, et une « dynamique » sacrifie la stabilité court terme pour faire travailler l'intégralité du capital.

**Détail :** Sur la période de l'an 2000 à août 2026, un indice 100 % actions mondiales en euros a subi une pire chute (« drawdown ») de -53,60 % (entre mai 2001 et mars 2009) avec une volatilité proche de 13-15 %, mais délivre environ 9 % de rendement annualisé. Un portefeuille 60/40 divise généralement ce risque par deux (max drawdown proche de -30 %) pour un rendement d'environ 6,5 % annualisé (ces chiffres sont conditionnels aux périodes étudiées).

**Piège fréquent ou erreur courante :** Fixer son regard uniquement sur le « rendement annualisé » dans le tableau, en minimisant la sévérité psychologique d'une colonne « pire baisse de -53,6 % ».

**Source(s) :** MSCI World Factsheet EUR, estimations des backtests de portefeuilles classiques européens (données de rendement et volatilité agrégées 2000-2026, À VÉRIFIER pour les calculs croisés exacts).

---

## Ce qui a changé récemment

- **Mise à jour 2026 de l'hyper-concentration des gains :** la dernière mise à jour de l'étude Bessembinder en mars 2026 (sur 100 ans de bourse) montre un renforcement drastique de la concentration ; 46 entreprises seulement justifient la moitié des gains boursiers d'un siècle entier.
- **Concentration indicielle historique :** sous l'impulsion de l'intelligence artificielle (notamment Nvidia), le poids du top 10 du MSCI World (28 %) et des États-Unis (72 %) atteint en 2026 un sommet de domination inégalé depuis des décennies.
- **Cycles de taux d'intérêt :** l'inversion et la politique monétaire plus souple des banques centrales en 2024-2025 ont légèrement restabilisé le compartiment obligataire tout en maintenant des rendements honorables sur les fonds en euros avant ajustement.
- **Acceptation réglementaire des cryptos :** l'approbation d'ETF Bitcoin spot début 2024 aux États-Unis a modifié la liquidité et la structure des participants de marché pour les crypto-actifs, catalysant les nouveaux sommets du cycle.

## Ce que je n'ai pas pu trancher

- Le rendement moyen officiel net définitif des fonds en euros de l'assurance vie française pour l'année 2026 complète (les assureurs annoncent généralement leurs résultats en janvier ou février de l'année suivante).
- L'impact exact à long terme de l'hyper-concentration de l'indice S&P 500 : le débat académique n'est pas encore clos pour affirmer si une correction des grandes capitalisations technologiques s'étalera sur une « décennie perdue » ou sera comblée par des gains rapides d'autres valeurs mid-cap.

## Sources utilisées

- **MSCI** : MSCI World Index Factsheet USD & EUR, données de septembre 2026 (https://www.msci.com/documents/10199/255599/msci-world-index.pdf).
- **State Street Global Advisors** : factsheet SPDR S&P 500 ETF, données de fin septembre 2026 (https://www.ssga.com).
- **Vanguard** : « Best practices for portfolio rebalancing », 2026 (https://investor.vanguard.com/investor-resources-education).
- **Bessembinder, Hendrik** : « One Hundred Years in the U.S. Stock Markets », mars 2026 (https://theideafarm.com).
- **Barber, Brad M., & Odean, Terrance** : « Trading Is Hazardous to Your Wealth », The Journal of Finance, 2000.
- **AMF** : doctrines sur le questionnaire de risque et données tarifaires SCPI, 2026 (https://www.amf-france.org).
- **Impots.gouv.fr** : documentation sur la fiscalité des comptes (PFU, assurance vie), 2026.
- **Historiques crypto** : Bitcoin Drawdown Analyzer et données Binance, 2026.
