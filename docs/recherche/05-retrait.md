# Recherche 05 : liberté financière et phase de retrait

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichier de données associé : `retrait.csv` (extrait du texte, tel que fourni).

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

1. **Fiscalité : mêmes contradictions que la recherche 04.** Le point 4 utilise PS à 17,2 %, PFU à 30 %. La recherche 01 donne 18,6 % et 31,4 %. Pire : « Assurance vie de plus de 8 ans, au-delà de l'abattement, taxation maximale à 30 % (PFU) » est faux ou très simplifié par rapport à la recherche 01 (7,5 % ou 12,8 % d'impôt après 8 ans, selon le seuil de 150 000 €).
2. **Morningstar** : « taux sûr de 4 % en 2025 (À VÉRIFIER), après 3,8 % en 2022 ». L'autre IA signale elle-même le doute. À contrôler dans le rapport original.
3. **Taux de retrait européen (3,2 % à 3,5 %) et probabilités du CSV** (95, 90, 99, 90 %) : en grande partie « À VÉRIFIER », et les probabilités de succès du CSV ressemblent à des ordres de grandeur, pas à des résultats d'études précises.
4. **Âge légal « 64 ans »** : à vérifier. La réforme des retraites a pu être suspendue ou modifiée depuis, je ne peux pas le confirmer d'ici.
5. **Affirmation sans source** : « dans 90 % des scénarios, viser 100 % de succès conduit à mourir avec un capital 2 à 3 fois supérieur au capital de départ » (point 8).
6. **Capital cible (point 6)** : calculs arithmétiques justes (450 000 €, 600 000 €, 750 000 €, 1 M€, 1,2 M€, 1,6 M€ ; 450 000 / 0,90 = 500 000 €). Mais l'hypothèse « fiscalité moyenne de 10 % » n'est pas justifiée.
7. **Sources** : aucune URL précise pour les études (Bengen, Trinity, Guyton-Klinger : titres corrects, pas de lien), « Early Retirement Now » cité en bloc. Coût EHPAD (2 200 €/mois, DREES 2023) sans lien.
8. **CSV** : séparateurs avec espaces (« , »), « A VERIFIER » sans accent, colonne `taux_sur_pct` : à nettoyer avant lecture par un script.

---

## 1. Quelle est l'origine et quelles sont les limites de la règle des 4 % ?

**Réponse courte :** La règle des 4 % indique qu'un retraité peut retirer 4 % de son capital investi la première année, puis ajuster ce montant à l'inflation chaque année, sans épuiser son portefeuille sur une période de 30 ans. Elle provient de l'étude de William Bengen (1994) et a été popularisée par l'étude Trinity (1998).

**Détail :** Bengen s'est basé sur un horizon de 30 ans et une allocation de 50 % à 75 % d'actions américaines, en utilisant les données historiques américaines de 1926 à 1976. Aujourd'hui, des chercheurs comme Wade Pfau ou Karsten Jeske (Early Retirement Now) soulignent que ces rendements passés ne garantissent pas l'avenir. Morningstar a évalué le taux sûr à 4 % en 2025 (À VÉRIFIER) en raison de la remontée des rendements obligataires, après l'avoir abaissé à 3,8 % en 2022.

**Piège fréquent ou erreur courante :** Appliquer cette règle sur un horizon de 50 ans (retraite anticipée) ou avec un portefeuille non américain, ce qui augmente considérablement le risque d'épuisement du capital.

**Source(s) :** Journal of Financial Planning (William Bengen, 1994) ; Morningstar (State of Retirement Income 2025).

## 2. Quel est le taux de retrait sûr pour un investisseur en Europe sur 30, 40 ou 50 ans ?

Les données historiques américaines surestiment les rendements mondiaux (biais du survivant). Pour un portefeuille européen ou mondial, le taux de retrait sûr historique est mathématiquement inférieur.

**Détail :** Selon les bases de données financières mondiales, le taux de retrait sûr sur 30 ans pour l'Europe se situe historiquement entre 3,2 % et 3,5 % (À VÉRIFIER). Pour des horizons de 40 à 50 ans, les simulations de Karsten Jeske (ERN) recommandent de cibler un taux de retrait compris entre 3 % et 3,25 % pour absorber les pires cycles économiques.

**Piège fréquent ou erreur courante :** Ignorer que l'inflation européenne et la fiscalité française réduisent le montant net réellement disponible pour la consommation.

**Source(s) :** UBS Global Investment Returns Yearbook 2024 (publié début 2024) ; Early Retirement Now (SWR Series, 2016-2026).

## 3. Quelles sont les principales stratégies de retrait et leurs garde-fous ?

Les retraits peuvent être fixes (ajustés à l'inflation), en pourcentage constant du portefeuille, ou dynamiques. Les stratégies dynamiques ajustent les retraits à la baisse lors des krachs boursiers pour protéger le capital.

**Détail :** La méthode Guyton-Klinger (2006) utilise des « garde-fous » : on gèle l'ajustement à l'inflation si le portefeuille baisse, ce qui permet de commencer avec un taux initial plus élevé (souvent 4,5 % à 5 %). La stratégie des seaux (« bucket strategy », Harold Evensky) divise le capital : 1 à 3 ans de liquidités sans risque (Livret A, fonds euros), 3 à 7 ans en obligations, le reste en actions mondiales.

**Piège fréquent ou erreur courante :** Penser que la stratégie des seaux augmente la rentabilité mathématique. Elle sert surtout à rassurer l'investisseur pour éviter qu'il ne vende ses actions en pleine panique.

**Source(s) :** Journal of Financial Planning (Guyton et Klinger, 2006).

## 4. Comment est fiscalisée la phase de retrait en France (PEA, AV, CTO) ?

En France, l'imposition lors d'un retrait ne frappe que la quote-part de plus-value (les gains), et non le capital initialement versé. L'ordre de retrait optimal consiste à purger d'abord les enveloppes défiscalisées.

**Détail (données 2026) :**

- PEA (ouvert depuis plus de 5 ans) : exonération d'impôt sur le revenu (IR), mais les gains subissent 17,2 % de prélèvements sociaux (PS).
- Assurance vie (contrat de plus de 8 ans) : abattement annuel sur les gains de 4 600 euros (personne seule) ou 9 200 euros (couple). Au-delà, taxation maximale à 30 % (PFU).
- Compte-titres ordinaire (CTO) : les plus-values sont taxées au Prélèvement Forfaitaire Unique (PFU) de 30 % (12,8 % IR + 17,2 % PS).

**Piège fréquent ou erreur courante :** Croire qu'un retrait de 10 000 euros sur un PEA subit 17,2 % de taxe sur 10 000 euros. Si le portefeuille a fait +50 % de gain global, le retrait est composé de deux tiers de capital et d'un tiers de gain. Seul le tiers de gain est taxé.

**Source(s) :** impots.gouv.fr (fiscalité des valeurs mobilières, consulté le 30 octobre 2026) ; legifrance.gouv.fr (Code général des impôts).

## 5. Comment intégrer la retraite publique, le PER et l'épargne salariale ?

La retraite publique (régime général et complémentaire Agirc-Arrco) abaisse considérablement le capital nécessaire, transformant l'indépendance financière en une simple phase de transition jusqu'à l'âge légal (64 ans).

**Détail :** Si l'investisseur touche 1 500 euros net de pension à 64 ans, son capital n'aura plus besoin de générer ce revenu après cet âge. Le Plan Épargne Retraite (PER) permet de défiscaliser pendant la vie active, mais les retraits en capital sont taxés au barème progressif de l'IR. L'épargne salariale (PEE) débloquée pour fin de contrat de travail est exonérée d'IR (seuls les PS de 17,2 % s'appliquent sur les plus-values).

**Piège fréquent ou erreur courante :** Sortir tout son PER en capital en une seule fois lors de la première année de retraite. Cela propulse les revenus dans les tranches d'imposition les plus élevées (TMI à 30 %, 41 % ou 45 %).

**Source(s) :** service-public.fr (Retraite et PER, consulté le 30 octobre 2026).

## 6. Comment calculer le capital cible (formule et exemples) ?

Le capital cible brut se calcule en multipliant la dépense annuelle estimée par l'inverse du taux de retrait (ex : dépense mensuelle × 12 / 0,04 pour la règle des 4 %).

**Détail :**

- Pour 1 500 euros/mois (18 000 euros/an) : 450 000 euros à 4 % ; 600 000 euros à 3 %.
- Pour 2 500 euros/mois (30 000 euros/an) : 750 000 euros à 4 % ; 1 000 000 euros à 3 %.
- Pour 4 000 euros/mois (48 000 euros/an) : 1 200 000 euros à 4 % ; 1 600 000 euros à 3 %.

Pour tenir compte d'une fiscalité moyenne estimée à 10 % sur les retraits globaux, il faut diviser ce capital cible brut par 0,90. Exemple : 450 000 euros bruts deviennent 500 000 euros nécessaires nets.

**Piège fréquent ou erreur courante :** Se baser sur ses dépenses actuelles en oubliant l'inflation qui aura lieu entre aujourd'hui et le jour du départ en retraite.

**Source(s) :** Formule mathématique des rentes perpétuelles.

## 7. Quels sont les risques spécifiques à la phase de retrait ?

Le risque majeur est le « risque de séquence des rendements » (Sequence of Returns Risk). Subir un krach boursier dans les cinq premières années de retraite est dévastateur car le capital vendu au plus bas pour vivre ne profitera jamais de la remontée des marchés.

**Détail :** S'ajoutent le risque d'inflation (érosion du pouvoir d'achat) et le risque de longévité (vivre plus longtemps que prévu). Le coût de la dépendance est aussi critique : un EHPAD en France coûte en médiane environ 2 200 euros/mois (chiffre DREES 2023). Pour s'en prémunir, la flexibilité (travailler à mi-temps les premières années de baisse) est le meilleur bouclier mathématique.

**Piège fréquent ou erreur courante :** Se rassurer avec le « rendement annuel moyen » d'un ETF boursier (ex : 7 % ou 8 % par an). À la retraite, l'ordre dans lequel les rendements arrivent compte plus que la moyenne.

**Source(s) :** drees.solidarites-sante.gouv.fr (tarifs médians des EHPAD, étude de 2023).

## 8. Quelle est la fiabilité des chiffres et la probabilité de succès ?

Les études calculent le taux de succès d'un plan en testant des milliers de scénarios passés ou simulés (Monte Carlo). Un taux de 3 % frôle historiquement les 100 % de réussite.

**Détail :** Sur 30 ans avec 50 % d'actions, la règle des 4 % a un taux de succès d'environ 95 % sur les données historiques américaines. Si on allonge l'horizon à 50 ans, la probabilité de succès d'un retrait de 4 % chute brutalement (souvent estimée autour de 70 % à 80 %, À VÉRIFIER selon les modèles ERN/Morningstar). Abaisser le taux à 3,25 % sur 50 ans remonte les chances à plus de 95 %.

**Piège fréquent ou erreur courante :** Viser une probabilité de succès de 100 %. Dans 90 % des scénarios, cibler 100 % de sécurité initiale conduit le retraité à mourir avec un capital deux à trois fois supérieur à son montant de départ, signifiant qu'il s'est privé inutilement de sa propre épargne.

**Source(s) :** Early Retirement Now (Safe Withdrawal Rate Series).

---

## Ce qui a changé récemment (fin 2024 à octobre 2026)

- L'inflation post-COVID, après avoir fortement érodé le pouvoir d'achat en 2022 et 2023, s'est stabilisée. Cela a permis aux projections de taux de retrait (comme celles de Morningstar) de remonter légèrement (vers 4 %), aidées par des rendements obligataires de nouveau positifs et des taux directeurs assagis.
- Les fonds en euros de l'assurance vie française ont retrouvé des rendements nets plus attractifs, redevenant des outils pertinents pour constituer la « poche de sécurité » liquide dans une stratégie des seaux.
- La fiscalité française des investissements (PEA, PFU à 30 %) a été l'objet de très nombreux débats budgétaires à l'Assemblée nationale, mais le cadre de base pour les petits et moyens patrimoines est resté en place.

## Ce que je n'ai pas pu trancher

- Les réformes futures de la fiscalité française : le Prélèvement Forfaitaire Unique (PFU à 30 %) est un dispositif qui dépend des majorités politiques. Sa suppression éventuelle et un retour au barème progressif de l'impôt sur le revenu pour les dividendes et plus-values changeraient radicalement le calcul du capital cible net pour un retraité en CTO.
- L'évolution du système de répartition : la loi reportant l'âge de départ (actuellement 64 ans) pourrait évoluer d'ici à ce qu'un jeune investisseur atteigne cet âge, ce qui modifie la durée exacte de la phase de « transition » financée par l'épargne privée pour les pratiquants du mouvement FIRE.

## Sources utilisées

- impots.gouv.fr (Direction générale des Finances publiques) : imposition des revenus de capitaux mobiliers, PFU, PEA, assurance vie.
- service-public.fr : règles générales sur l'épargne retraite (PER) et l'épargne salariale.
- legifrance.gouv.fr : textes de lois en vigueur en octobre 2026 (Code général des impôts).
- drees.solidarites-sante.gouv.fr : statistiques sur le coût de la dépendance et tarifs médians des EHPAD (édition 2023).
- Journal of Financial Planning :
  - « Determining Withdrawal Rates Using Historical Data » (William Bengen, 1994).
  - « Retirement Savings: Choosing a Withdrawal Rate That Is Sustainable » (Cooley, Hubbard, Walz, Trinity Study, 1998).
  - « Decision Rules and Maximum Initial Withdrawal Rates » (Jonathan Guyton et William Klinger, 2006).
- Morningstar : « State of Retirement Income 2025 » (rapport annuel sur les taux de retrait sûrs).
- UBS : « Global Investment Returns Yearbook 2024 » (continuité des travaux de Dimson, Marsh, Staunton sur les rendements mondiaux historiques).
- Early Retirement Now (Karsten Jeske) : « The Safe Withdrawal Rate Series » (analyses approfondies pour le mouvement FIRE).
