# Recherche 06 : allocation d'actifs (version A)

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Une deuxième version, produite par une autre session, est dans `06b-allocation-bis.md`. Les deux se contredisent sur plusieurs points (voir ci-dessous).
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichier de données associé : `allocations-types.csv` (extrait du texte, tel que fourni).

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

1. **Fiscalité** : PFU à 30 % et PS à 17,2 % partout (rééquilibrage, crypto), en contradiction avec la recherche 01 (31,4 % et 18,6 %). Le 17,2 % sur les SCPI en direct est en revanche cohérent avec la recherche 01.
2. **Bessembinder « mise à jour de juillet 2026 »** : la version B parle de mars 2026, avec un autre jeu de chiffres. Je ne peux pas confirmer qu'une telle mise à jour existe. Les chiffres de 46 entreprises, 59 % des actions qui détruisent de la valeur et 41,2 % qui battent les bons du Trésor sont à vérifier dans l'article.
3. **Barber et Odean** : « 11,4 % contre 17,9 % avec 75 % de rotation ». 11,4 % est le rendement du groupe de ménages les plus actifs, 75 % est la rotation moyenne de l'ensemble des ménages, pas celle de ce groupe. Mélange à corriger.
4. **Poids des États-Unis dans le MSCI World** : 70,3 % ici, 72 % et 72,x % dans la version B, 73 % dans la recherche 02. Trois valeurs pour la même donnée à la même date.
5. **CSV `allocations-types.csv`** : le texte dit « dynamique : 80 % d'actions », le CSV 90 % (80 + 10). Les rendements (4,5 / 6,5 / 8,5 %) sont attribués à des « simulations Portfolio Visualizer » non reproductibles. Un rendement annualisé de 8,5 % pour 90 % d'actions sur 2000-2026 me paraît élevé par rapport à ce que je connais de l'indice monde sur la période. À vérifier avant tout usage.
6. **Questions non traitées ou superficielles** : questionnaire de tolérance au risque (pas de grille détaillée), études de rééquilibrage (Vanguard cité sans chiffres).
7. **Sources** : la plupart sans lien précis.

---

## 1. Comment adapter la part d'actions selon l'âge et l'horizon d'investissement ?

**Réponse courte :** L'horizon d'investissement prime sur l'âge biologique, et un horizon très long justifie une exposition maximale aux actions. La vieille règle empirique « 100 moins son âge » pour définir la part d'actions est aujourd'hui jugée trop conservatrice.

**Détail :** Les gérants de fonds à date cible (comme Vanguard) maintiennent souvent 90 % d'actions jusqu'à 20 ans avant le retrait prévu. Pour un investisseur de 30 ans avec un horizon de 10 ans, une part de 60 à 80 % est classique ; pour un horizon de 20 ou 30 ans, une exposition de 90 à 100 % est mathématiquement défendable pour contrer l'inflation. La désensibilisation (glide path) ne s'accélère souvent que dans les 10 dernières années.

**Piège fréquent ou erreur courante :** Confondre l'âge de la retraite avec la fin de l'horizon d'investissement, alors que le capital devra continuer à générer du rendement pendant 20 ou 30 ans de décaissement.

**Source(s) :** Vanguard, méthodologie des « Target Retirement Funds », consulté en 2026.

## 2. Comment évaluer sa tolérance au risque boursier ?

**Réponse courte :** Le profil de risque se définit au carrefour de la capacité financière à absorber des pertes (mesurable) et de la tolérance psychologique à la volatilité (subjective). Les autorités de marché imposent l'évaluation séparée de ces deux dimensions.

**Détail :** La capacité financière s'évalue par la stabilité des revenus, l'endettement et l'existence d'une épargne de précaution (3 à 6 mois de dépenses). La tolérance psychologique est évaluée par des questions de mise en situation (« Quelle est votre réaction face à une baisse de 20 % en un mois : vendre, attendre, acheter plus ? »). Si la capacité financière est faible, le profil final sera prudent même si la tolérance psychologique est élevée.

**Piège fréquent ou erreur courante :** Surestimer sa tolérance psychologique lors des phases de marché haussier (FOMO), pour paniquer et vendre à perte au premier krach.

**Source(s) :** Autorité des Marchés Financiers (AMF), doctrine sur l'évaluation du profil de risque des clients, amf-france.org.

## 3. Faut-il rééquilibrer son portefeuille et à quelle fréquence ?

**Réponse courte :** Le rééquilibrage sert avant tout à contrôler le niveau de risque initial du portefeuille, et non à maximiser la performance. Une fréquence annuelle ou par seuils d'écart est le meilleur compromis.

**Détail :** Les études montrent qu'un rééquilibrage annuel ou déclenché par un écart de 5 % par rapport à l'allocation cible offre un contrôle du risque similaire à un rééquilibrage mensuel, mais avec beaucoup moins de frais. En France, un rééquilibrage par les flux (orienter les nouveaux versements vers l'actif sous-pondéré) est optimal. La vente d'actifs déclenche une imposition au Prélèvement Forfaitaire Unique (PFU, 30 %) sur un compte-titres, un coût fiscal purgé au sein d'un PEA ou d'une assurance vie.

**Piège fréquent ou erreur courante :** Rééquilibrer de manière trop fréquente (mensuelle), générant des frais de transaction et d'imposition inutiles.

**Source(s) :** Étude Vanguard « Best practices for portfolio rebalancing », impots.gouv.fr (fiscalité PFU 2026).

## 4. Quelle part consacrer aux actions individuelles (satellite) ?

**Réponse courte :** La part allouée à la sélection de titres vifs ne devrait pas dépasser 5 à 10 % de l'allocation globale, car cette pratique détruit statistiquement de la valeur. Il est recommandé de ne pas excéder 2 à 5 % du capital par ligne individuelle.

**Détail :** Barber et Odean ont démontré que les investisseurs particuliers actifs sous-performent lourdement le marché (11,4 % contre 17,9 % de rendement brut annuel entre 1991 et 1996, avec 75 % de rotation). Plus récemment, l'étude de Bessembinder (mise à jour en juillet 2026) sur un siècle (1926-2025) a révélé que seules 46 entreprises américaines ont généré la moitié de la richesse boursière totale. Près de 59 % des actions ont détruit de la richesse, et à peine 41,2 % ont battu des bons du Trésor à un mois.

**Piège fréquent ou erreur courante :** Pratiquer le biais de familiarité en achetant quelques actions connues, et passer à côté de l'infime minorité de « superstars » qui portent la performance des grands indices.

**Source(s) :** Barber & Odean, « Trading Is Hazardous to Your Wealth », Journal of Finance (2000) ; H. Bessembinder, « One Hundred Years in the U.S. Stock Markets » (SSRN, 2026).

## 5. Quel est le rôle des obligations et des fonds euros dans l'allocation ?

**Réponse courte :** Les poches obligataires servent de ballast pour amortir la volatilité des actions et offrir de la liquidité lors des baisses de marché. Le fonds en euros français ajoute une garantie en capital absente des obligations cotées.

**Détail :** Les obligations subissent le risque de taux d'intérêt et le risque de crédit. Les rendements attendus des fonds en euros en 2026 gravitent autour de 2,5 % à 3,0 % net de frais (À VÉRIFIER), tandis qu'un ETF obligataire diversifié verse un rendement à l'échéance dicté par le marché. L'ETF obligataire peut perdre de la valeur (baisse des prix si les taux montent), ce qui est impossible pour le capital garanti du fonds en euros.

**Piège fréquent ou erreur courante :** Penser qu'un ETF obligataire est « sans risque » en capital sur le court terme, ou à l'inverse conserver trop de fonds euros et subir l'érosion monétaire due à l'inflation.

**Source(s) :** Banque de France (taux directeurs), documentation DICI des assureurs.

## 6. Faut-il inclure de l'or, de l'immobilier coté (SCPI) ou des matières premières ?

**Réponse courte :** Ces classes d'actifs sont strictement optionnelles. Elles offrent des vertus de diversification mais impliquent des frictions importantes (frais, fiscalité) ou des rendements réels historiques faibles.

**Détail :** L'or physique ou papier, qui ne génère aucun rendement, sert d'assurance contre les crises systémiques (0 à 5 % de l'allocation). Les SCPI (rendement cible 4 à 6 %) supportent des frais de souscription très élevés (8 à 12 %) et une fiscalité confiscatoire hors enveloppe (tranche marginale d'imposition plus 17,2 % de prélèvements sociaux). Les matières premières ont historiquement un rendement réel proche de zéro.

**Piège fréquent ou erreur courante :** Investir en SCPI sur un horizon court de moins de 10 ans, ce qui empêche d'amortir les frais d'entrée.

**Source(s) :** Association Française des Sociétés de Placement Immobilier (ASPIM), legifrance.gouv.fr.

## 7. Les crypto-actifs ont-ils leur place dans une allocation long terme ?

**Réponse courte :** Ils peuvent justifier une part marginale (1 à 5 % maximum) pour les investisseurs très dynamiques, agissant comme un pari asymétrique. Cette poche reste purement spéculative et extrêmement volatile.

**Détail :** Le Bitcoin a enregistré des baisses maximales d'environ 84 % en 2018 et 77 % en 2022. La corrélation entre les cryptomonnaies et les marchés actions s'est intensifiée ces dernières années, réduisant leur bénéfice de diversification lors des krachs. En France, la conversion en monnaie fiat est imposée au taux unique de 30 % (PFU).

**Piège fréquent ou erreur courante :** Concentrer ce patrimoine sur une plateforme centralisée sans posséder ses clés privées (risque de contrepartie et de faillite).

**Source(s) :** Impots.gouv.fr (fiscalité des actifs numériques 2026).

## 8. Faut-il se couvrir contre le risque de change (dollar) ?

**Réponse courte :** Sur un horizon long terme en actions, la couverture de change (hedging) n'est généralement pas recommandée en raison de son coût structurel et du rôle protecteur de la devise américaine.

**Détail :** Un ETF MSCI World expose l'investisseur européen à environ 70 % de dollar américain (fin 2026). Se couvrir coûte cher si les taux d'intérêt en Europe sont inférieurs aux États-Unis (coût de portage). Par ailleurs, le dollar s'apprécie souvent lors des crises mondiales, offrant un effet stabilisateur aux portefeuilles européens. Sur des horizons de 20 ou 30 ans, les fluctuations de devises ont tendance à s'annuler.

**Piège fréquent ou erreur courante :** Acheter systématiquement des ETF « EUR Hedged » et payer des frais de gestion supérieurs pendant 20 ans pour gommer un risque qui s'érode avec le temps.

**Source(s) :** Factsheet MSCI World (octobre 2026), publications de recherche iShares et Vanguard.

## 9. Quels sont les risques de concentration des grands indices ?

**Réponse courte :** La concentration des indices est actuellement historique, exposant massivement l'investisseur au seul marché américain et à son secteur technologique.

**Détail :** En octobre 2026, les États-Unis représentent plus de 70,3 % de l'indice MSCI World (ils pesaient environ 30 % au plus bas dans les années 80, et plus de 60 % en 1970). Les 10 plus grandes entreprises du S&P 500 pèsent aujourd'hui 37,7 % de l'indice. Les 10 plus grandes capitalisations du MSCI World représentent 26,6 % du poids global. Le Nasdaq 100 est encore plus polarisé avec un top 10 avoisinant les 45 % (À VÉRIFIER).

**Piège fréquent ou erreur courante :** Superposer un ETF S&P 500 et un ETF MSCI World dans l'espoir de se diversifier, alors que l'overlap (chevauchement) est immense.

**Source(s) :** JustETF (comparatif MSCI World vs S&P 500, octobre 2026), Club Patrimoine.

## 10. À quoi ressemblent des allocations types chiffrées ?

**Réponse courte :** Des portefeuilles stylisés (prudent, équilibré, dynamique) illustrent le compromis classique entre le couple rendement attendu et baisse maximale subie. Ce ne sont que des illustrations.

**Détail :** Un portefeuille prudent (30 % actions, 70 % sécuritaire) cible historiquement 4 à 5 % de rendement avec des baisses maximales contenues sous les 15 %. Un profil équilibré (50 à 60 % actions) offre 6 à 7 % moyennant des baisses pouvant frôler les 30 %. Un profil dynamique (80 % actions) vise 8 à 9 % mais s'expose à des chutes transitoires de près de la moitié de sa valeur.

**Piège fréquent ou erreur courante :** Extrapoler aveuglément les rendements des 15 dernières années pour construire son plan financier futur, sans tenir compte des frais de son enveloppe fiscale.

**Source(s) :** Données historiques extraites de moteurs de backtest (simulations Portfolio Visualizer, période 2000-2026).

---

## Ce qui a changé récemment

La mise à jour en juillet 2026 de l'étude centenaire de Hendrik Bessembinder vient conforter l'extrême rareté de la création de valeur en actions individuelles (3,7 % des actions créent l'intégralité de la richesse). La concentration de l'indice mondial s'est encore accentuée, franchissant ponctuellement le seuil des 75 % pour les États-Unis, tirée par le bloc des valeurs technologiques. L'institutionnalisation des cryptomonnaies s'est actée avec l'approbation d'ETF spot (Bitcoin et Ethereum), renforçant paradoxalement leur corrélation aux marchés traditionnels et actant une fiscalité stabilisée.

## Ce que je n'ai pas pu trancher

Le taux de rendement moyen servi par les fonds en euros pour l'année 2026 n'est pas encore consolidé (les assureurs l'annoncent début d'année suivante). Le niveau exact de concentration du Nasdaq 100 fin octobre 2026 dépend du rééquilibrage de l'indice et fluctue au quotidien. De même, la performance exacte des trois allocations types dans le CSV dépend strictement du choix des indices sous-jacents, de la date précise de rééquilibrage et des frais des ETF spécifiques retenus dans les simulations.

## Sources utilisées

- Vanguard Research : Methodology on Target Retirement Funds & Best practices for portfolio rebalancing.
- JustETF : comparatifs de composition et de pondération MSCI World / S&P 500 (octobre 2026), justetf.com.
- AMF : doctrine sur l'évaluation des clients, amf-france.org.
- Barber, B., & Odean, T. (2000). Trading Is Hazardous to Your Wealth. The Journal of Finance (faculty.haas.berkeley.edu).
- Bessembinder, H. (2026). One Hundred Years in the U.S. Stock Markets, SSRN.
- Club Patrimoine : Les États-Unis dominent le MSCI World, clubpatrimoine.com.
- Impots.gouv : fiscalité du PFU et des actifs numériques, impots.gouv.fr.
- Banque de France & INSEE : séries macroéconomiques et taux de l'argent.
- ASPIM : rendements immobiliers et SCPI.
