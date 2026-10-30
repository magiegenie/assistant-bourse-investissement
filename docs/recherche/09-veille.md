# Recherche 09 : veille et information

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichier de données associé : `sources-veille.csv` (14 lignes, copié tel quel).

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

1. **Conflit avec l'agent Veilleur** : le point 6 recommande un brief sans explication narrative (variations de clôture, statistique du jour, calendrier). `.claude/agents/veilleur.md` demande au contraire de dire pourquoi ça a bougé, de classer 3 infos (à ignorer, à surveiller, à agir) et de donner un verdict. Il faudra choisir une ligne à l'intégration. Le risque d'une explication narrative (souvent inventée a posteriori) est réel, mais un brief sans contexte aide moins à rester calme.
2. **Fiscalité** : le point 3 cite un « plafond de versements légal du PEA de 150 000 € » et un « changement de la flat tax » comme déclencheurs. Cohérent avec la recherche 01, mais la valeur de la flat tax à surveiller dépend de la question 31,4 % contre 30 % à trancher.
3. **Seuils de la grille de tri** : « TER > 0,40 % » est un exemple arbitraire, pas une norme.
4. **Poids maximal d'une entreprise (4 à 6 % du MSCI World)** : « À VÉRIFIER » selon l'autre IA. L'ordre de grandeur me paraît plausible pour les plus grosses lignes, mais il bouge.
5. **Calendrier** : fréquences correctes à ma connaissance (8 réunions par an pour la BCE et la Fed, publication de l'inflation américaine en milieu de mois, emploi américain le premier vendredi). Pas de dates précises ni de lien vers les calendriers officiels, alors que le prompt les demandait.
6. **`sources-veille.csv`** : notes de fiabilité de 1 à 5 données par l'autre IA, subjectives. Pas de flux RSS réel indiqué (« RSS », « API » sans adresse). Trois lignes « sans URL » (influenceurs, newsletters, forums) servent de contre-exemples.
7. **Manques** : fiches « comment lire une factsheet » détaillées, exemples d'appels API (BCE, FRED), liste de 15 types d'actualité avec impact chiffré.

---

## 1. Quelles sont les sources fiables pour s'informer sans stresser ?

Privilégiez les données brutes des banques centrales, des instituts statistiques officiels et la presse économique factuelle. Évitez les contenus basés sur l'opinion, la prédiction ou l'urgence.

Les agences de presse (Reuters, Bloomberg) et les institutions (BCE, Fed) fournissent les faits bruts. Les émetteurs (Amundi, BlackRock, Vanguard) et fournisseurs d'indices (MSCI) délivrent les données techniques exactes de vos produits. L'INSEE publie l'inflation française.

Le piège est de consommer des vidéos d'influenceurs financiers ou des newsletters payantes qui dramatisent la volatilité normale des marchés pour capter l'attention.

Sources : Autorité des Marchés Financiers (mises en garde de l'Espace Épargnants, consulté en octobre 2026, amf-france.org).

## 2. Quel est le calendrier macroéconomique à connaître ?

L'actualité économique bat au rythme des publications mensuelles sur l'inflation et l'emploi, et des réunions monétaires toutes les six semaines.

La Réserve fédérale américaine (FOMC) et la Banque centrale européenne (BCE) se réunissent 8 fois par an pour fixer les taux. L'inflation (IPC/CPI) tombe vers le 10 ou 15 de chaque mois. Les créations d'emplois américains (NFP) sortent le premier vendredi du mois. Les grandes entreprises publient leurs résultats trimestriels principalement en janvier, avril, juillet et octobre.

Croire qu'il faut modifier son portefeuille la veille d'une annonce de la Fed. Les marchés financiers intègrent en réalité ces probabilités de hausse ou baisse de taux des semaines à l'avance.

Sources : calendrier officiel de la BCE (bce.europa.eu, 2026), calendrier du FOMC (federalreserve.gov, 2026), INSEE (insee.fr).

## 3. Comment trier l'actualité avec une grille de lecture efficace ?

Un investisseur de long terme en ETF Monde doit ignorer 95 % du flux d'actualité quotidienne. Il faut surveiller les tendances macroéconomiques lourdes, mais n'agir que sur les changements réglementaires ou les modifications des caractéristiques de ses fonds.

Grille de tri (15 exemples) :

- **À ignorer** : 1. Baisse ponctuelle de 3 % du CAC 40. 2. Résultats trimestriels décevants d'une seule entreprise technologique. 3. Scandale ou changement de PDG dans une multinationale. 4. Record mensuel du chiffre de l'inflation américaine. 5. Prédiction de krach imminent par un économiste dans les médias. 6. Chute brutale du cours du Bitcoin. 7. Faillite d'une banque régionale étrangère. 8. Tensions géopolitiques localisées sans impact énergétique mondial majeur.
- **À surveiller** : 9. Cycle de baisse ou hausse des taux directeurs de la BCE. 10. Élection présidentielle dans une grande puissance économique. 11. Rachat ou fusion de la société qui gère votre ETF.
- **À agir** : 12. Hausse des prélèvements sociaux ou modification du taux de la flat tax. 13. Hausse des frais de gestion annuels (TER) de votre ETF au-delà de votre seuil d'acceptation (ex : > 0,40 %). 14. Changement brutal de l'indice de référence par l'émetteur de l'ETF (passage d'un indice Monde classique à un indice excluant des secteurs). 15. Atteinte imminente du plafond de versements légal du PEA (150 000 euros en 2026).

Le piège classique est d'appliquer à un ETF diversifié mondialement les réflexes d'un boursicoteur qui achète des actions individuelles.

Sources : méthodologie des études SPIVA (S&P Global, 2026, spglobal.com).

## 4. Quel est l'impact type des événements sur un portefeuille ETF Monde ?

La diversification d'un ETF répliquant le MSCI World dilue rapidement l'impact d'une mauvaise nouvelle isolée. Les chocs globaux entraînent des baisses à court terme, mais la persistance historique de cet impact est faible.

Une hausse surprise des taux d'intérêt ou de l'inflation provoque souvent une baisse mécanique des valorisations des actions (car le risque coûte plus cher). Cependant, la littérature académique (event studies) montre que l'effet d'une crise géopolitique isolée est généralement lissé et absorbé par un indice mondial en quelques semaines ou mois.

Penser que la chute massive d'une des plus grandes entreprises de l'indice va ruiner l'ETF. Le poids maximal d'une seule entreprise (même colossale comme Apple ou Microsoft) oscille généralement entre 4 % et 6 % [À VÉRIFIER : valeurs exactes des pondérations à l'instant T en 2026] de l'indice MSCI World.

Sources : études fondatrices de MacKinlay sur les « Event Studies in Economics and Finance » (1997).

## 5. Comment repérer les fake news financières et les manipulations ?

Les manipulations financières s'appuient systématiquement sur le sentiment d'urgence, le jargon faussement complexe, et des sources anonymes ou invérifiables.

Les signaux d'alerte incluent des promesses de rendements supérieurs au taux sans risque sans mentionner de risque de perte en capital. Méfiez-vous des rumeurs de faillites bancaires lancées sur les réseaux sociaux pour créer des mouvements de panique (bank run).

Confondre une publicité (publirédactionnel) pour un produit financier toxique avec un article d'analyse objectif d'un média reconnu.

Sources : AMF, listes noires et alertes (amf-france.org, 2026).

## 6. Que doit contenir un brief quotidien de 2 minutes ?

Un brief pertinent pour un épargnant se contente des variations de clôture, de la statistique du jour et du calendrier du lendemain, en excluant toute tentative d'explication narrative (ex : « les marchés baissent à cause des craintes sur... »).

Modèle et longueur : 3 phrases maximum.

- Jour 1 (calme) : Le MSCI World a clôturé à +0,2 %. Aucune statistique macroéconomique majeure aujourd'hui. Demain, publication des inscriptions au chômage US.
- Jour 2 (forte baisse) : Le S&P 500 a reculé de -2,1 % en clôture. L'inflation américaine (CPI) publiée à 14h30 est ressortie au-dessus du consensus du marché.
- Jour 3 (banque centrale) : Les indices européens terminent stables. La BCE a annoncé le maintien de son taux de dépôt à son niveau actuel, comme anticipé par les analystes.

Piège : lire son brief et décider, sous le coup de l'émotion d'une séance rouge, d'annuler son plan d'investissement mensuel automatisé.

Sources : modèles issus des « Morning Briefs » d'agences factuelles (Reuters, 2026).

## 7. Où et comment vérifier la composition exacte de mes ETF ?

Les courtiers et les sites comparateurs peuvent afficher des données périmées. Seule la documentation de l'émetteur du fonds (le gestionnaire) fait autorité légalement.

Cherchez le code ISIN de l'ETF sur le site officiel de l'émetteur (Amundi, BlackRock/iShares, Vanguard, etc.). Lisez la « factsheet » (fiche mensuelle) pour voir le top 10 des positions, la répartition sectorielle, et l'encours total. Lisez le Document d'informations clés (DIC/KID) pour vérifier les frais courants (TER) et la politique de distribution (capitalisation ou distribution).

Piège : choisir un ETF uniquement sur son nom sans vérifier sa méthode de réplication (physique, où le fonds détient les actions, ou synthétique, souvent utilisée pour rendre un ETF Monde éligible au PEA français).

Sources : base de données GECO de l'AMF (geco.amf-france.org), sites officiels des émetteurs.

## 8. Où trouver des données de marché gratuites et légales pour un script informatique ?

Il est possible d'automatiser sa veille ou le suivi de son portefeuille sans recourir à des API payantes onéreuses, grâce aux portails open-data des institutions.

Le « Data Portal » de la BCE (API RESTful) et la plateforme FRED de la Réserve fédérale de Saint-Louis (API avec clé gratuite) offrent toutes les séries temporelles macroéconomiques. Stooq permet de télécharger manuellement ou par script des fichiers CSV des historiques de cours. La bibliothèque Python `yfinance` interroge l'API non officielle de Yahoo Finance pour les cours boursiers.

Piège : lancer des scripts qui bombardent Yahoo Finance ou d'autres plateformes gratuites de milliers de requêtes par heure. Cela aboutit systématiquement à un bannissement temporaire ou définitif de votre adresse IP.

Sources : portail Data de la BCE (data.ecb.europa.eu), FRED API (fred.stlouisfed.org), documentation de la librairie Python yfinance (pypi.org, 2026).

---

## Ce qui a changé récemment

Sur les 24 derniers mois (2024-2026), les investisseurs européens ont vu l'essor des ETF obligataires à échéance fixe (Maturity ETFs), complexifiant un peu la lecture des taux par rapport aux fonds en euros classiques de l'assurance vie. Par ailleurs, la réglementation européenne (MiCA / DORA) a poussé l'AMF à multiplier les mises en garde contre les plateformes non régulées et les « finfluenceurs », imposant de nouvelles règles de transparence aux créateurs de contenu financier. L'offre d'ETF Monde synthétiques pour le PEA a également connu des fusions et absorptions chez les grands émetteurs européens, imposant aux épargnants de suivre de près les avis de changement d'indice ou de code ISIN (notamment lors de l'intégration de Lyxor par Amundi, dont les effets se sont prolongés).

## Ce que je n'ai pas pu trancher

- Le taux d'échec exact des tentatives d'hameçonnage (phishing) par SMS ciblant spécifiquement les détenteurs de PEA français en 2026. L'AMF alerte sur la hausse de ces pratiques, mais les statistiques isolées pour ce produit précis ne sont pas publiées de façon centralisée par les pouvoirs publics.
- La limite de requêtes (rate limit) de l'API masquée de Yahoo Finance exploitée par les outils comme `yfinance`. Cette limite évolue sans préavis et n'est documentée officiellement nulle part, empêchant de donner un chiffre d'appels garantis par minute.

## Sources utilisées

- Autorité des Marchés Financiers (Espace Épargnants et base GECO) : https://www.amf-france.org/fr et https://geco.amf-france.org/
- Banque centrale européenne (calendrier et Data Portal) : https://www.ecb.europa.eu/ et https://data.ecb.europa.eu/
- Réserve fédérale américaine (calendrier FOMC et FRED) : https://www.federalreserve.gov/ et https://fred.stlouisfed.org/
- Institut national de la statistique et des études économiques (INSEE) : https://www.insee.fr/
- Reuters (briefs financiers) : https://www.reuters.com/finance
- S&P Global (études SPIVA sur la gestion active et passive) : https://www.spglobal.com/spdji/en/research-insights/spiva/
- MacKinlay, A. C. (1997). « Event Studies in Economics and Finance ». Journal of Economic Literature.
- Amundi (informations réglementaires des ETF) : https://www.amundietf.fr/
- BlackRock / iShares (fiches produits et factsheets) : https://www.ishares.com/fr/
- Stooq (historiques de cotations) : https://stooq.com/
