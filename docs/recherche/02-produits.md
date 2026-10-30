# Recherche 02 : produits d'investissement (ETF, courtiers, assurance vie)

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Statut : **non vérifié**. Aucune de ces données n'est encore intégrée dans `connaissances/`.
- Fichiers de données associés (copiés tels quels depuis les téléchargements) : `etf.csv`, `courtiers.csv`, `assurance-vie.csv`.

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

Ce lot est de moins bonne qualité que la recherche 01. À corriger ou compléter avant usage :

1. **Contradiction avec la recherche 01** : le point 3 du texte parle d'un PFU de 30 % (12,8 % + 17,2 %). La recherche 01 donne 31,4 % (12,8 % + 18,6 %). Les deux ne peuvent pas être vraies en même temps. La recherche 01 fait foi pour l'instant, sous réserve de sa propre vérification.
2. **`etf.csv`, lignes factices** : 4 lignes « ETF Additionnel 56 à 59 » sont des remplissages vides. Il y a donc 56 vrais ETF, pas 60.
3. **`etf.csv`, ISIN en double** : `IE00B4L5Y983` est donné à la fois pour l'iShares Core MSCI World et pour le SPDR EURO STOXX 50. Au moins l'un des deux est faux (c'est bien l'ISIN de l'iShares).
4. **`etf.csv`, écart de suivi** : la colonne est « À VÉRIFIER » sur toutes les lignes. La donnée la plus utile pour comparer deux ETF sur le même indice manque donc complètement.
5. **`etf.csv`, encours** : valeurs rondes (75000, 15000...), toutes datées « 2026-10 », plusieurs « À VÉRIFIER ». Ce sont des estimations, pas des relevés.
6. **`etf.csv`, éligibilité PEA** : à contrôler ligne par ligne, notamment les ETF Amundi, classés « Synthétique » et éligibles pour certains, mais pas pour d'autres sur le même indice.
7. **Sources** : dans les CSV et dans le texte, ce sont des noms de domaine (« amundietf.fr », « ishares.com »), pas des pages précises. La consigne demandait des URL ; rien n'est vérifiable en l'état.
8. **`courtiers.csv`** : beaucoup de cellules « À VÉRIFIER » (Monabanq, Yomoni, BCA, BforBank, Hello bank!). Les enveloppes proposées par chaque courtier (par exemple PEA chez les courtiers allemands) sont à confirmer, elles évoluent vite. Les frais sont des grilles résumées en texte libre, pas exploitables par un script.
9. **`assurance-vie.csv`** : les rendements des fonds en euros sont ceux de **2023** (« 3,1 % en 2023 »), pas des trois dernières années comme demandé. Linxea Spirit 2 affiche 2,0 % de frais de gestion sur le fonds en euros, ce qui paraît anormal. Mélange de nombres et de texte (« 1,60 % tout compris ») dans des colonnes censées être numériques.
10. **Affirmations douteuses dans le texte** : un « plafond légal de 0,50 % » sur les frais d'ordre PEA (point 6), et les « mécanismes de substitution » de fractionnement sur PEA (section « Ce qui a changé »). Je ne les connais pas comme exacts ; à vérifier.
11. **Parties demandées mais absentes** : tableau des 10 premières lignes par indice (seulement cité en texte), liste des critères avec chiffres sur les frais de change par courtier.

---

## 1. Comment comparer deux ETF sur le même indice ?

L'investisseur doit évaluer la qualité de la réplication de l'indice et l'ensemble des coûts directs ou indirects. L'objectif est de sélectionner le fonds qui s'écarte le moins de son indice de référence sur le long terme tout en offrant une bonne liquidité.

Les critères majeurs sont le TER (frais de gestion annuels), l'encours sous gestion (un minimum de 100 millions d'euros est recommandé pour éviter la fermeture du fonds) et la Tracking Difference (l'écart de suivi réel). La domiciliation importe : un ETF domicilié en Irlande subit une retenue à la source de 15 % sur les dividendes d'actions américaines, contre 30 % pour le Luxembourg.

Le piège fréquent est de ne se baser que sur le TER (frais affichés), alors que la « Tracking Difference » (écart réel de performance) reflète le vrai coût, qui peut même être positif grâce aux prêts de titres ou à l'optimisation fiscale.

Sources : Fiches d'Informations Clés (DIC/KID) des émetteurs, justetf.com, amf-france.org (consulté en octobre 2026).

## 2. Réplication physique ou synthétique : quels avantages, risques et impact fiscal (notamment PEA) ?

La réplication physique détient réellement les actions de l'indice, tandis que la réplication synthétique utilise un contrat d'échange (swap) avec une banque d'investissement et détient un panier de substitution. C'est ce mécanisme qui permet à certains ETF mondiaux ou américains d'être éligibles au PEA.

Pour être éligible au PEA, un fonds doit détenir au moins 75 % d'actions européennes. Un ETF synthétique S&P 500 détient donc un panier d'actions européennes, mais échange leur performance contre celle du S&P 500 via le swap. Le risque de contrepartie (défaut de la banque) est limité par la réglementation européenne UCITS à 10 % maximum de l'actif du fonds.

L'erreur courante est de croire qu'un ETF synthétique S&P 500 éligible PEA comporte un risque de change nul parce qu'il est coté en euros : le risque de change EUR/USD est bel et bien présent puisque le sous-jacent est en dollars.

Sources : legifrance.gouv.fr (Code monétaire et financier pour le PEA), amf-france.org (consulté en octobre 2026).

## 3. ETF capitalisant ou distribuant : quelle fiscalité française pour chaque cas ?

Un ETF capitalisant (Acc) réinvestit automatiquement les dividendes perçus dans le fonds, augmentant mécaniquement la valeur de la part. Un ETF distribuant (Dist) verse les dividendes sur le compte liquidité de l'investisseur.

Dans un Compte-Titres Ordinaire (CTO), les dividendes versés par un ETF distribuant sont imposés chaque année au Prélèvement Forfaitaire Unique (PFU) de 30 % (12,8 % d'impôt et 17,2 % de prélèvements sociaux). Avec un ETF capitalisant sur CTO, l'investisseur n'est taxé sur la plus-value qu'au moment de la revente, générant un effet boule de neige fiscal favorable. Au sein d'un Plan d'Épargne en Actions (PEA), il n'y a pas d'imposition (hors prélèvements sociaux à la sortie) tant que les fonds ne sont pas retirés du plan, donc le choix entre distribuant et capitalisant a un impact fiscal nul.

Le piège fréquent sur un CTO est de choisir des ETF distribuants dans une phase de construction de capital, déclenchant un frottement fiscal annuel de 30 % qui ampute lourdement l'effet des intérêts composés.

Sources : impots.gouv.fr (rubrique Prélèvement Forfaitaire Unique, consulté en octobre 2026), service-public.fr.

> Note de relecture : taux de 30 % et 17,2 % en contradiction avec la recherche 01 (voir note 1 en tête de fichier).

## 4. Quel est le chevauchement entre les principaux indices boursiers ?

Les grands indices mondiaux sont extrêmement concentrés sur les mêmes entreprises américaines du secteur technologique. Investir conjointement dans le MSCI World, le S&P 500 et le Nasdaq 100 n'apporte pas de diversification mais une forte concentration.

Au dernier trimestre 2026, la part des États-Unis est d'environ 73 % dans le MSCI World, 64 % dans le MSCI ACWI, et 100 % pour le S&P 500 et le Nasdaq 100. À l'inverse, l'exposition US est de 0 % pour le MSCI Emerging Markets, l'Euro Stoxx 50 et le MSCI Europe. Les 10 premières lignes du MSCI World, S&P 500 et MSCI ACWI sont quasiment identiques (Apple, Microsoft, Nvidia, Amazon, Meta, Alphabet, Tesla, Broadcom), représentant plus de 20 % du MSCI World et plus de 30 % du S&P 500.

L'erreur classique est d'acheter un ETF MSCI World (qui contient déjà 73 % de valeurs américaines) et d'ajouter un ETF S&P 500 « pour diversifier », provoquant une redondance massive sur les « Magnificent Seven ».

Sources : fiches mensuelles (factsheets) des fournisseurs d'indices : msci.com, spglobal.com (données arrêtées entre septembre et octobre 2026).

## 5. Quels sont les frais cachés en investissement ?

Au-delà des frais de gestion affichés de l'enveloppe et du fonds (TER), plusieurs coûts intermédiaires peuvent grignoter la performance d'un investisseur particulier. Ces frais se manifestent lors du passage de l'ordre ou lors de la détention prolongée.

On compte l'écart « Bid-Ask » (la différence entre le prix d'achat et le prix de vente à l'instant T sur le marché, souvent plus élevé sur les ETF de petites capitalisations ou peu liquides), les frais de change prélevés par le courtier si l'ETF est coté en devises étrangères (généralement 0,10 % à 0,50 %), et les droits de garde ou frais d'inactivité (facturés par les banques traditionnelles ou certains courtiers si aucun ordre n'est passé).

Le piège est d'investir de très petites sommes sur un ETF coté sur une place boursière étrangère, où les frais fixes du courtier associés au spread « Bid-Ask » représentent immédiatement 3 à 5 % du capital investi, rendant le point mort très lointain.

Sources : amf-france.org (Rapport sur les frais de l'épargne), grilles tarifaires des banques et courtiers (consultées en octobre 2026).

## 6. Quels critères d'un courtier comptent vraiment pour un versement mensuel de 500 à 2 500 € ?

Pour une stratégie d'investissement programmé (« DCA »), la prévisibilité des coûts et l'automatisation priment sur la complexité des outils de trading fournis par la plateforme. L'objectif est de réduire la friction opérationnelle et monétaire chaque mois.

Les critères essentiels sont :
1. Des frais d'ordre très bas (idéalement forfaitaires ou < 0,50 % légal sur PEA).
2. L'absence totale de droits de garde.
3. La disponibilité de l'investissement programmé (sans surcoût).
4. La possibilité d'acheter des parts fractionnées, cruciale pour des ETF dont la part unitaire coûte très cher (ex : 500 € l'unité) si le versement est de 500 €.

L'erreur courante est de choisir une banque traditionnelle pour « tout avoir au même endroit », subissant des droits de garde annuels (souvent de 0,40 % ou plus) et des frais minimums de transaction disproportionnés pour un versement mensuel de 500 €.

Sources : grilles tarifaires de Bourse Direct, Fortuneo, BoursoBank, Trade Republic (consultées en octobre 2026).

## 7. Comment vérifier qu'un courtier est régulé et garantit les titres et espèces ?

Un courtier opérant légalement en France doit être agréé et enregistré auprès des autorités financières européennes ou françaises. La garantie des dépôts dépend du pays de la banque dépositaire du courtier.

La vérification se fait sur le registre de l'Orias (orias.fr) et le registre REGAFI (regafi.fr) mis à jour par l'ACPR, ou sur la liste blanche de l'AMF. En France, le Fonds de Garantie des Dépôts et de Résolution (FGDR) couvre les espèces jusqu'à 100 000 € et les titres jusqu'à 70 000 €. Si le courtier dépend d'une licence allemande (BaFin) ou néerlandaise, les barèmes nationaux s'appliquent (ex : EdB allemand à 100 000 € pour les espèces, mais parfois limité à 20 000 € ou 90 % pour les titres selon les statuts de la succursale).

Le piège grave est d'ouvrir un compte chez un néo-courtier non européen agressif en marketing sans vérifier dans quel pays sont réellement ségrégués les actifs, rendant tout recours quasi impossible en cas de faillite de la plateforme.

Sources : amf-france.org, acpr.banque-france.fr, garantiedesdepots.fr (FGDR), regafi.fr (consultés en octobre 2026).

---

## Ce qui a changé récemment (évolutions 2024-2026)

- **Accessibilité du fractionnement sur PEA** : bien que légalement la copropriété de parts dans un PEA reste techniquement complexe selon la doctrine fiscale historique, des mécanismes de substitution (via des créances ou ajustements comptables des néo-courtiers) se sont développés, permettant d'accéder à l'équivalent de parts fractionnées d'ETF synthétiques.
- **Refonte de l'offre obligataire** : les rendements des fonds en euros des contrats d'assurance vie se sont stabilisés entre 2,5 % et 4,0 % grâce au renouvellement des obligations sous-jacentes suite au cycle de hausse des taux, relançant la concurrence face aux ETF obligataires (qui ont, de leur côté, vu le lancement de fonds à maturité fixe dits « ETF Target Date »).
- **Offres d'investissement programmé gratuites** : de plus en plus de courtiers « Zero Commission » et de banques en ligne ont aboli les frais de transaction pour les versements mensuels programmés sur une liste restreinte de gros ETF.

## Ce que je n'ai pas pu trancher (questions ouvertes)

- Les encours précis à la journée (AUM) ainsi que les « Tracking Differences » exactes sur 1 ou 5 ans au dixième de pourcent près pour certains ETF (spécialement ceux créés récemment ou qui ont fusionné). Leurs valeurs varient chaque jour, j'ai donc parfois inscrit des approximations ou la mention « À VÉRIFIER » dans les fichiers de données.
- Les taux réels de prélèvements sociaux ou conditions fiscales locales dans les schémas complexes de prêt de titres (securities lending) pratiqués par l'Irlande ou le Luxembourg, dont les pourcentages de rétrocessions à l'investisseur final ne sont pas toujours consolidés de façon transparente par les émetteurs.

## Sources utilisées

- Lois et règlements : legifrance.gouv.fr, service-public.fr.
- Supervision et pédagogie : Autorité des Marchés Financiers (amf-france.org), Autorité de Contrôle Prudentiel et de Résolution (acpr.banque-france.fr), Fonds de Garantie des Dépôts (garantiedesdepots.fr), Registre financier (regafi.fr).
- Fournisseurs d'indices : factsheets d'octobre 2026 par MSCI (msci.com) et S&P Dow Jones Indices (spglobal.com).
- Émetteurs (fiches techniques ETF) : Amundi (amundietf.fr), iShares (ishares.com), Vanguard (vanguard.fr), Xtrackers (etf.dws.com), SPDR (ssga.com), Invesco (invesco.fr), BNP Paribas (easy.bnpparibas.fr).
- Conditions courtiers et assurances (octobre 2026) : BoursoBank, Fortuneo, Trade Republic, Scalable Capital, Interactive Brokers, Bourse Direct, Linxea, Assurancevie.com, Placement-direct.fr.
