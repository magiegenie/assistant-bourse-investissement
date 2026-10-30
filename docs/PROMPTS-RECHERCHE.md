# Besoins en données et prompts de recherche

Objectif : enrichir `connaissances/` (aujourd'hui 4 à 11 lignes par fiche) avec des données à jour, chiffrées et sourcées, issues d'une recherche approfondie faite avec une autre IA.

Mode d'emploi :
1. Colle le **prompt maître** (partie 2) dans l'autre IA, puis un **prompt spécifique** à la suite. Un prompt par conversation.
2. Récupère la réponse Markdown et les éventuels CSV.
3. Ramène-les ici : je les fusionne dans `connaissances/`, remplis `00-SOURCES.md`, et adapte agents et scripts.

---

## Partie 1. Ce dont j'ai besoin

| # | Domaine | Alimente | Pourquoi | Priorité |
|---|---|---|---|---|
| 1 | Fiscalité française à jour (PFU, prélèvements sociaux, PEA, assurance vie, CTO, PER, plafonds, tranches IR, abattements, formulaires) | fiche C, stratège | Les taux de la fiche C (30 %, 17,2 %) sont peut-être périmés. Un chiffre fiscal faux rend une simulation de vente fausse. | Haute |
| 2 | Catalogue produits : ETF éligibles PEA et CTO, courtiers français, contrats d'assurance vie | fiche D, analyste | Aucune donnée produit aujourd'hui : impossible de comparer avec des critères réels (frais, encours, réplication). | Haute |
| 3 | Historique des marchés : rendements, inflation, baisses majeures, distributions sur 10/15/20 ans | fiches B, E, F, G, projection, coach | Les taux 4/5/7 % des projections n'ont aucune base. Le coach a besoin de chiffres réels pour mettre une baisse en perspective. | Haute |
| 4 | Hypothèses de projection : rendements attendus, volatilité, risque de séquence, paramètres Monte Carlo | fiche B, `projection.py` | Passer d'un chiffre unique à des fourchettes de probabilité. | Haute |
| 5 | Liberté financière : taux de retrait sûr version Europe/France, fiscalité du retrait | fiche B, stratège | La règle des 4 % vient des États-Unis. Il faut la version européenne et fiscalisée. | Moyenne |
| 6 | Allocation : part actions selon âge et risque, rééquilibrage, crypto, or, SCPI, fonds euro, devises | fiche D, analyste | Les fiches D donnent des règles sans leur base chiffrée. | Moyenne |
| 7 | Comportement : études chiffrées, protocoles anti-biais, scripts de coaching par situation | fiche F, coach | Le coach s'appuie sur des références citées par leur nom, sans les chiffres. | Moyenne |
| 8 | Contenu pédagogique : 12 modules détaillés, glossaire, quiz, études de cas historiques | fiche H, coach | Le parcours n'existe qu'en titres. | Moyenne |
| 9 | Veille : sources fiables classées, calendrier macro récurrent, grille de tri des news | fiche H, veilleur | Le brief du jour a besoin d'une liste de sources et d'un agenda structuré. | Moyenne |
| 10 | Budget et prévoyance France : benchmarks de dépenses, livrets, dettes, assurances | fiches A, I, conseiller | Comparer un budget à une norme réelle, pas à une règle générale. | Moyenne |
| 11 | Arnaques : listes AMF/ACPR, typologie, signaux d'alerte, cas réels | fiche I, conseiller | Aider à repérer une arnaque avec des exemples concrets. | Basse |
| 12 | Bibliographie sourcée | `00-SOURCES.md`, toutes les fiches | Le fichier est vide alors que toute recommandation doit être citée. | Basse |

**Ce que je ferai de mon côté, sans recherche externe** : simulateur fiscal de vente, Monte Carlo, XIRR plus robuste, génération du fichier Excel à partir des CSV.

Ordre conseillé : 1, 3, 4, 2, puis le reste.

---

## Partie 2. Prompts

### Prompt maître (à coller en premier, avant chaque prompt spécifique)

```
Tu es un chercheur en finance personnelle et en investissement, spécialisé dans le contexte français. Tu travailles pour un projet d'assistant qui accompagne des investisseurs particuliers débutants à intermédiaires (France, investissement en ETF, enveloppes PEA, assurance vie, CTO, PER). Ta recherche va alimenter des fiches de connaissances utilisées par des agents IA, donc elle doit être précise, vérifiable et directement exploitable.

Date du jour : indique la date à laquelle tu fais la recherche, et n'utilise que des informations en vigueur à cette date.

Règles à respecter dans toute ta réponse :
1. Langue : français, direct, sans jargon non expliqué. Pas de tirets longs.
2. Format : Markdown, en points numérotés. Chaque point suit ce modèle :
   - **N. Question posée par un investisseur ?**
   - Réponse courte (2 à 3 phrases).
   - Détail : chiffres, conditions, exceptions.
   - Piège fréquent ou erreur courante.
   - Source(s) : nom, URL, date de publication ou de consultation.
3. Chaque chiffre est donné avec sa valeur, sa date de validité (année ou période) et sa source. Privilégie les sources primaires : impots.gouv.fr, service-public.fr, legifrance.gouv.fr, amf-france.org, banque-france.fr, insee.fr, sites des émetteurs d'ETF, fournisseurs d'indices (MSCI, S&P), publications d'origine des études citées.
4. Tout chiffre que tu ne trouves pas dans une source primaire est marqué « À VÉRIFIER ». Si deux sources se contredisent, présente les deux et explique l'écart. N'invente jamais un chiffre ni une URL : si tu ne sais pas, dis-le.
5. Aucune prédiction de marché, aucun conseil personnalisé, aucune recommandation d'un produit précis. Tu fournis des critères, des données et des faits.
6. Les données volumineuses (listes de produits, séries historiques) sont fournies dans un tableau CSV séparé, avec une ligne d'en-tête, des colonnes clairement nommées, la date des données et la source de chaque ligne ou de chaque colonne.
7. À la fin de ta réponse, ajoute trois sections : « Ce qui a changé récemment » (évolutions des 24 derniers mois), « Ce que je n'ai pas pu trancher » (questions ouvertes) et « Sources utilisées » (liste complète avec URL).

Voici maintenant le sujet de recherche précis.
```

### Prompt 1. Fiscalité française à jour

```
SUJET : fiscalité de l'investisseur particulier en France, en vigueur aujourd'hui.

Couvre au minimum, en points numérotés :
- Prélèvement forfaitaire unique (PFU) : taux total, répartition impôt sur le revenu et prélèvements sociaux, évolutions récentes (loi de finances et loi de financement de la sécurité sociale), produits concernés et produits exemptés d'une hausse éventuelle de CSG. Précise explicitement si les taux de 30 % (PFU) et 17,2 % (prélèvements sociaux) sont toujours exacts, et pour quels produits.
- Option pour le barème progressif de l'impôt sur le revenu : quand elle est avantageuse, comment elle s'applique, exemple chiffré.
- PEA et PEA-PME : plafonds de versement, règle des 5 ans, ce qui se passe en cas de retrait avant 5 ans, après 5 ans, rente viagère, transfert, clôture, prélèvements sociaux selon la date d'ouverture, titres éligibles, ETF éligibles (règle des 75 % d'actions européennes), dividendes et plus-values dans l'enveloppe.
- Assurance vie : fiscalité avant et après 8 ans, abattements annuels (célibataire et couple), taux de 7,5 % et 12,8 %, seuil de 150 000 € de primes, fiscalité en cas de décès (articles 990 I et 757 B), unités de compte et fonds euro.
- CTO : fiscalité des plus-values et dividendes, imputation des moins-values sur 10 ans, comptes détenus à l'étranger (formulaire 3916), ETF américains non accessibles (réglementation PRIIPs/KID), retenue à la source sur dividendes étrangers.
- PER : déductibilité des versements, plafonds de déduction, sortie en capital ou en rente, fiscalité à la sortie, déblocage anticipé, cas où il est pertinent (tranche marginale d'imposition).
- Barème de l'impôt sur le revenu : tranches en vigueur, quotient familial de base, contribution exceptionnelle sur les hauts revenus.
- Crypto-actifs : fiscalité des cessions, formulaire 2086, déclaration des comptes d'échanges étrangers.
- Calendrier déclaratif annuel : dates limites, formulaires (2042, 2042-C, 2086, 3916-bis, IFU).
- Un tableau comparatif PEA / AV / CTO / PER : plafond, fiscalité à la sortie, durée minimale, liquidité, succession.
- Trois exemples chiffrés de simulation de vente (CTO, PEA de plus de 5 ans, assurance vie de plus de 8 ans) avec le calcul détaillé.

Fournis aussi un CSV « fiscalite-parametres.csv » avec les colonnes : parametre, valeur, unite, date_effet, source_url. Il doit contenir tous les taux, plafonds et seuils cités.
```

### Prompt 2. Catalogue produits (ETF, courtiers, assurance vie)

```
SUJET : données sur les produits d'investissement accessibles à un particulier en France.

Livre trois CSV et un texte de synthèse.

CSV 1, « etf.csv » : environ 60 ETF courants, couvrant au minimum ces expositions : monde développé, monde tous pays, S&P 500, Nasdaq 100, Europe, zone euro, marchés émergents, petites capitalisations, obligations (monde, euro), or physique, immobilier coté. Colonnes : nom, isin, emetteur, indice, ter_pct, encours_meur, date_encours, replication (physique complète, échantillonnée ou synthétique), capitalisant_ou_distribuant, devise_de_cotation, domicile_fonds, eligible_pea (oui/non/à vérifier), nombre_de_lignes_approx, ecart_de_suivi_pct (tracking difference sur 1 an et 5 ans si disponible), date_creation, source_url. Ne choisis pas sur la performance passée : sélectionne par catégorie les ETF les plus gros et les moins chers.

CSV 2, « courtiers.csv » : environ 15 courtiers et banques en ligne accessibles en France. Colonnes : nom, type (courtier, banque en ligne, banque traditionnelle), enveloppes_proposees, frais_de_courtage_par_ordre (grille détaillée par montant), frais_de_garde, frais_de_tenue_de_compte, frais_de_change, frais_de_transfert_sortant, versement_programme_possible (oui/non), parts_fractionnees (oui/non), garantie_des_depots, regulateur, date_du_releve, source_url.

CSV 3, « assurance-vie.csv » : environ 15 contrats d'assurance vie en ligne. Colonnes : nom, assureur, frais_sur_versement_pct, frais_de_gestion_uc_pct, frais_de_gestion_fonds_euro_pct, nombre_ou_liste_d_etf_disponibles, fonds_euro (rendement des 3 dernières années avec bonus éventuels), versement_minimum, versements_programmes (oui/non), gestion_pilotee, source_url, date.

Texte de synthèse, en points numérotés au format du prompt maître :
- Comment comparer deux ETF sur le même indice (TER, tracking difference, encours, réplication, domiciliation, fiscalité des dividendes).
- Réplication physique ou synthétique : avantages, risques, impact fiscal (notamment PEA).
- ETF capitalisant ou distribuant : fiscalité française pour chaque cas.
- Chevauchement entre indices : tableau des 10 premières lignes et de la part USA pour MSCI World, S&P 500, Nasdaq 100, MSCI ACWI, MSCI EM, Euro Stoxx 50, MSCI Europe, avec date des données (fiches des fournisseurs d'indices).
- Les frais cachés : écart bid-ask, frais de change, droits de garde.
- Quels critères d'un courtier comptent vraiment pour un versement mensuel de 500 à 2 500 €.
- Comment vérifier qu'un courtier est régulé (ACPR, AMF), garantie des titres et des espèces.

Rappel : aucune recommandation d'un produit en particulier, uniquement des données et des critères. Si une donnée n'est pas disponible pour une ligne, laisse la cellule vide et marque « À VÉRIFIER » dans une colonne « remarques ».
```

### Prompt 3. Historique des marchés

```
SUJET : données historiques de marchés pour calibrer des projections réalistes et des mises en perspective.

Livre deux CSV et un texte.

CSV 1, « rendements-annuels.csv », une ligne par année, depuis la plus ancienne année disponible de façon fiable (idéalement 1970, sinon l'année la plus ancienne que tu peux sourcer). Colonnes : annee, msci_world_total_return_eur_pct, msci_world_total_return_usd_pct, sp500_total_return_usd_pct, sp500_total_return_eur_pct, msci_europe_pct, euro_stoxx_50_pct, msci_emerging_pct, obligations_monde_couvert_pct, obligations_euro_pct, or_eur_pct, inflation_france_pct, inflation_usa_pct, eur_usd_fin_annee, source_url. Précise si chaque rendement est dividendes réinvestis, en euros ou en dollars, et ce qui est reconstitué plutôt que mesuré. Si tu ne disposes pas d'une série fiable, dis-le plutôt que d'estimer.

CSV 2, « baisses-majeures.csv » : toutes les baisses de plus de 20 % sur le MSCI World et le S&P 500 depuis 1970. Colonnes : indice, date_sommet, date_creux, baisse_pct, duree_de_la_baisse_en_mois, date_de_retour_au_sommet, duree_de_recuperation_en_mois (en euros et en dollars si possible), evenement_declencheur, source_url.

Texte, en points numérotés au format du prompt maître :
- Distribution des rendements annualisés réels (après inflation) du MSCI World et du S&P 500 sur toutes les périodes glissantes de 1, 5, 10, 15 et 20 ans : minimum, 10e percentile, médiane, 90e percentile, maximum, part des périodes négatives. Donne la méthode de calcul.
- Rendement réel moyen long terme des actions mondiales, des obligations et de l'or. Ce que l'on peut raisonnablement retenir comme hypothèse prudente, centrale et favorable, et pourquoi.
- Comparaison avec des « décennies perdues » connues (2000-2009, Japon, 1970s) et ce qu'elles enseignent.
- Effet du risque de séquence : exemple chiffré de deux investisseurs avec le même rendement moyen mais des séquences différentes.
- Coût du market timing : manquer les meilleurs jours (10, 20, 30 meilleurs jours) sur 20 ans, chiffres d'origine et auteurs, avec les réserves méthodologiques connues.
- Corrélation entre actions, obligations et or lors des grandes crises (2000, 2008, 2020, 2022).
- Effet du change EUR/USD sur un investisseur français en actions américaines : écarts de performance sur 10 et 20 ans.
- Probabilité empirique que l'investissement d'une somme en une fois batte un versement échelonné sur 12 mois (étude Vanguard et autres, avec chiffres et limites).

Pour chaque série, indique la source exacte, l'indice précis (price, net total return, gross total return) et ses limites.
```

### Prompt 4. Hypothèses de projection

```
SUJET : hypothèses prudentes et défendables pour projeter la valeur d'un portefeuille d'actions sur 5 à 30 ans.

Couvre, en points numérotés au format du prompt maître :
- Rendements attendus à long terme publiés par les grands gérants et instituts (Vanguard, BlackRock, JP Morgan, Research Affiliates, GMO, Morningstar, AQR, Schroders...) pour : actions mondiales, actions américaines, actions européennes, émergents, obligations, liquidités. Pour chaque publication : nom, date, horizon, valeur nominale ou réelle, lien. Présente un tableau de synthèse, puis les fourchettes basse, centrale, haute.
- Volatilité annuelle historique et attendue de chaque classe d'actifs, corrélations entre elles, et hypothèses souvent retenues dans des simulations (Monte Carlo).
- Méthodes de projection : rendement constant, tirage historique (bootstrap), Monte Carlo paramétrique. Avantages, limites, erreurs fréquentes (sous-estimer les queues de distribution).
- Inflation : cible BCE, inflation française moyenne depuis 1990, et manière correcte d'exprimer un objectif en euros constants ou courants.
- Frais : effet chiffré de 0,1 %, 0,5 %, 1 % et 2 % de frais annuels sur 10, 20 et 30 ans pour un capital initial de 100 000 € et un versement mensuel de 1 000 €.
- Fiscalité dans la projection : comment intégrer l'impôt à la sortie (PEA, AV, CTO) dans un objectif net.
- Paramètres recommandés pour un simulateur Monte Carlo à implémenter en Python : rendement moyen, écart-type, distribution, nombre de tirages, corrélation, traitement de l'inflation. Justifie chaque valeur et cite la source.
- Probabilité d'atteindre un objectif : comment l'exprimer à un débutant (par exemple « 8 chances sur 10 d'avoir au moins X »), et pourquoi une projection à un seul taux est trompeuse.
- Un cas chiffré complet : 100 000 € de départ, 2 000 € par mois, 10 ans, avec le résultat selon les hypothèses basse, centrale, haute, nominal et réel, brut et net de frais. Détaille les calculs.

Fournis un CSV « hypotheses-projection.csv » : classe_d_actifs, rendement_nominal_bas, rendement_nominal_central, rendement_nominal_haut, rendement_reel_central, volatilite_annuelle, source_url, date_source.
```

### Prompt 5. Liberté financière et retrait

```
SUJET : indépendance financière et phase de retrait, adaptées à la France.

Couvre, en points numérotés au format du prompt maître :
- Origine de la règle des 4 % (étude Trinity, Bengen), hypothèses, durée de retraite supposée, limites. Critiques et mises à jour (Pfau, Kitces, Morningstar « safe withdrawal rate » avec valeurs par année, Early Retirement Now).
- Taux de retrait sûr pour des horizons de 30, 40 et 50 ans, et pour un investisseur européen : résultats d'études spécifiques à l'Europe, valeurs chiffrées.
- Stratégies de retrait : règle fixe, règle de pourcentage, garde-fous dynamiques (Guyton-Klinger), « bucket strategy ». Avantages, risques, exemples chiffrés.
- Fiscalité de la phase de retrait en France : retraits programmés depuis une assurance vie (part de capital et d'intérêts, abattement), retraits d'un PEA de plus de 5 ans, ventes d'un CTO, ordre de retrait optimal, exemples chiffrés.
- Intégration de la retraite publique (régime général, complémentaires), PER, et de l'épargne salariale.
- Calcul du capital cible : formule, exemples pour 1 500, 2 500 et 4 000 € de dépenses mensuelles, avec et sans prise en compte de la fiscalité et de l'inflation.
- Risques spécifiques : risque de séquence au début de la retraite, inflation, santé, longévité. Réponses possibles.
- Fiabilité des chiffres : ce que les études disent sur la probabilité d'échec selon le taux de retrait choisi.

Fournis un CSV « retrait.csv » : source, annee, horizon_ans, taux_sur_pct, probabilite_de_succes_pct, hypotheses_actions_obligations, zone_geographique, remarque.
```

### Prompt 6. Allocation d'actifs

```
SUJET : construction de l'allocation d'actifs d'un investisseur particulier long terme.

Couvre, en points numérotés au format du prompt maître :
- Allocation selon l'âge et l'horizon : glide path (fonds à date cible, règles comme « 100 moins l'âge »), études et pratiques des gérants, avec chiffres. Part d'actions défendable pour un investisseur de 30 ans à horizon 10, 20 et 30 ans.
- Évaluer sa tolérance au risque : questionnaires validés, capacité (financière) versus tolérance (psychologique), questions types et grille d'interprétation.
- Rééquilibrage : fréquence (annuelle, par seuil), études comparatives (Vanguard et autres), rééquilibrage par les flux, coût fiscal.
- Cœur et satellite : part raisonnable du satellite, résultats observés des investisseurs particuliers sur des actions individuelles (études Barber et Odean, Bessembinder sur la concentration des gains), pourcentage maximum par ligne.
- Obligations et fonds euro : rôle, risques (taux, crédit), rendement attendu, hypothèses actuelles, fonds euro versus ETF obligataire.
- Or, immobilier coté, SCPI, matières premières : rôle éventuel, risques, frais, fiscalité en France, chiffres historiques.
- Crypto-actifs : volatilité historique, baisses maximales (2018, 2022), corrélation avec les actions, débat sur la part maximale raisonnable, fiscalité française, risques de plateforme.
- Devises : exposition au dollar d'un portefeuille monde, couverture ou non, coût de la couverture, études sur le long terme.
- Concentration cachée : part des 10 premières entreprises dans MSCI World, S&P 500, Nasdaq 100 (chiffres datés), part des États-Unis dans l'indice mondial depuis 1970 (évolution), et risque de concentration actuel.
- Exemples d'allocations types chiffrées pour trois profils (prudent, équilibré, dynamique), avec les rendements historiques annualisés, la volatilité et la pire baisse simulée sur la période disponible, en précisant clairement qu'il s'agit d'illustrations et non de recommandations.

Fournis un CSV « allocations-types.csv » : profil, pct_actions_monde, pct_actions_emergents, pct_obligations, pct_or, pct_autres, rendement_annualise_historique, volatilite, pire_baisse_pct, periode, source_url.
```

### Prompt 7. Comportement et psychologie

```
SUJET : psychologie de l'investisseur particulier et outils pour limiter les erreurs coûteuses.

Couvre, en points numérotés au format du prompt maître :
- L'écart de comportement (« behavior gap ») : études Morningstar « Mind the Gap » (chiffres par année), DALBAR (QAIB), Vanguard « Advisor's Alpha », avec les réserves méthodologiques. Quel est l'ordre de grandeur crédible de la perte moyenne due au comportement.
- Sur-trading : études de Barber et Odean (chiffres, périodes, populations), études plus récentes sur les investisseurs français (AMF, universités), effet des frais.
- Biais cognitifs : pour chacun (aversion aux pertes, ancrage, excès de confiance, biais de récence, effet de disposition, biais de confirmation, FOMO, effet de troupeau, comptabilité mentale, illusion de contrôle) : définition, étude d'origine chiffrée, exemple d'investisseur, signal d'alerte dans le langage (« phrase typique »), contre-mesure concrète.
- Comportement en cas de krach : données sur les ventes de particuliers en mars 2020, fin 2008, 2022 (chiffres des courtiers, de l'AMF, de fonds), et conséquences chiffrées sur la performance.
- Fréquence de consultation du portefeuille : étude sur la myopie face aux pertes (Benartzi et Thaler), effet de la fréquence de consultation sur la prise de risque.
- Outils anti-émotion : charte d'investissement (contenu type d'une page), règle des 24-72 h, pré-mortem, journal de décision (modèle de champs), « ordre à l'avance », automatisation des versements. Preuves de leur efficacité s'il y en a.
- Finance comportementale et réseaux sociaux : études sur l'influence des influenceurs, forums et applications sur les décisions, arnaques et manipulations (pump and dump, signaux payants).
- Stress financier : liens entre consultation, stress et décisions, recommandations de santé financière (indicateurs, seuils d'alerte).
- Scripts de coaching : pour chacune de ces situations, propose 5 questions que le coach doit poser, 3 pièges à éviter dans sa réponse et une formulation bienveillante mais ferme : envie d'acheter un titre qui monte fort, envie de vendre après -20 %, FOMO sur une crypto, certitude après une « bonne affaire » entendue, envie d'arrêter les versements, euphorie après un gain, culpabilité après une erreur.

Fournis un CSV « etudes-comportement.csv » : etude, auteurs, annee, population, resultat_chiffre, limite, source_url.
```

### Prompt 8. Contenu pédagogique

```
SUJET : parcours pédagogique de 12 modules pour des investisseurs débutants à intermédiaires en France.

Pour chaque module, fournis : objectifs d'apprentissage (3 à 5), contenu structuré en 3 niveaux (« en 30 secondes », « en 5 minutes », « pour aller plus loin »), 2 exemples chiffrés, 3 erreurs courantes, 5 questions de quiz avec réponses commentées, 3 lectures de référence gratuites ou accessibles (avec URL), et un exercice pratique à faire sur son propre portefeuille.

Les 12 modules :
1. Bases et intérêts composés (inflation, rendement réel, règle des 72, effet du temps et des frais)
2. Les ETF (fonctionnement, réplication, TER, tracking difference, liquidité, risques)
3. Enveloppes et fiscalité en France (PEA, AV, CTO, PER, comparaison)
4. Allocation et diversification (cœur-satellite, corrélation, rééquilibrage)
5. Risque et volatilité (écart-type, drawdown, risque de séquence, horizon)
6. Psychologie de l'investisseur (biais, discipline, plan écrit)
7. Lire une actualité financière (faits contre opinions, sources, ce qui compte pour un portefeuille)
8. Lire le bilan d'une entreprise (compte de résultat, bilan, flux de trésorerie, ratios de base)
9. Valorisation (PER, rendement du bénéfice, actualisation, limites)
10. Macro et taux (inflation, taux directeurs, courbe des taux, cycles, impact sur les actions et obligations)
11. Crypto-actifs (principe, risques, fiscalité, sécurité)
12. Construire sa charte d'investissement (modèle complet avec exemple rempli)

Ajoute :
- Un glossaire de 100 termes essentiels (définition en une phrase, exemple).
- 4 études de cas historiques (bulle internet 2000, crise de 2008, Covid 2020, hausse des taux 2022) : chronologie, chiffres, ce qu'un investisseur patient et un investisseur paniqué ont obtenu, leçons.
- Une grille de progression : critères pour passer de débutant à intermédiaire, puis avancé.
- 5 notions « du jour » liées à l'actualité, avec un modèle de texte de 3 lignes réutilisable.

Les exemples chiffrés doivent être vérifiables. Marque « À VÉRIFIER » ceux que tu ne peux pas sourcer.
```

### Prompt 9. Veille et information

```
SUJET : organiser une veille financière fiable, courte et peu anxiogène pour un investisseur ETF français.

Couvre, en points numérotés au format du prompt maître :
- Sources fiables classées par catégorie (agences de presse, presse économique francophone et anglophone, banques centrales, régulateurs, instituts de statistiques, émetteurs d'ETF, fournisseurs d'indices) : nom, URL, type de contenu, gratuit ou payant, fréquence, flux RSS ou API gratuite quand ils existent. Signale les sources à éviter ou à manier avec prudence (influenceurs, forums, newsletters payantes promettant des rendements) avec le raisonnement.
- Calendrier macro récurrent : dates types et fréquence des réunions de la BCE, de la Fed, publications d'inflation (zone euro, France, États-Unis), emploi américain, PIB, résultats trimestriels des grandes entreprises (périodes types). Donne les URL officielles des calendriers.
- Grille de tri d'une news : critères pour dire « à ignorer », « à surveiller », « à agir », avec 15 exemples réels de types d'actualités et leur classement argumenté pour un investisseur en ETF monde à horizon long.
- Impact type de chaque événement sur un portefeuille ETF monde : hausse ou baisse de taux, surprise d'inflation, tensions géopolitiques, résultats des géants technologiques, baisse du dollar, chute d'une grande banque. Ce que disent les études d'événements (« event studies ») sur la persistance de l'impact.
- Fake news financières et manipulations : signaux d'alerte, exemples réels.
- Contenu d'un brief quotidien de 2 minutes : modèle structuré, longueur cible, exemples complets sur 3 jours fictifs (calme, forte baisse, annonce de banque centrale).
- Sources d'information pour comprendre la composition des ETF : fiches de produits, factsheets, composition de l'indice, et comment lire une factsheet.
- Données de marché gratuites et légales exploitables par un script (Banque de France, BCE Data Portal, FRED, Yahoo Finance, Stooq, Eurostat, INSEE) : accès, format, limites de licence, exemples d'appel.

Fournis un CSV « sources-veille.csv » : nom, categorie, url, gratuit_payant, frequence, flux_rss_ou_api, fiabilite_1_a_5, remarque.
```

### Prompt 10. Budget et prévoyance en France

```
SUJET : finances personnelles d'un salarié français, du budget à la prévoyance.

Couvre, en points numérotés au format du prompt maître :
- Dépenses moyennes des ménages français par poste et par niveau de revenu (INSEE, enquête Budget de famille), avec les chiffres les plus récents et la date. Repères pour un célibataire de 30 ans, salarié, avec un revenu net de 2 000, 3 000 et 5 000 € par mois.
- Règles de budget (50/30/20 et variantes) : origine, limites, adaptation au coût de la vie en France selon la région (logement), taux d'épargne moyen des Français (Banque de France, INSEE) et par niveau de revenu.
- Épargne de précaution : durée recommandée selon la situation (CDI, CDD, indépendant, famille), livrets réglementés (Livret A, LDDS, LEP, LEL) : taux en vigueur, plafonds, conditions, fiscalité, éligibilité, autres placements de précaution.
- Dettes : crédit à la consommation, crédit renouvelable, prêt immobilier. Taux moyens actuels (Banque de France, taux d'usure), méthodes de remboursement (avalanche, boule de neige), arbitrage entre rembourser et investir avec un exemple chiffré.
- Logement : acheter ou louer, règles des 33 % d'endettement, effet du prêt sur la capacité d'investissement (sans prendre position), frais d'achat.
- Abonnements et dépenses récurrentes : moyenne par foyer, méthode d'audit, leviers d'économies chiffrés.
- Prime, augmentation, héritage : règles pratiques d'affectation, fiscalité des primes, intéressement et participation, PEE et PERCO/PER collectif, abondement, avantages fiscaux.
- Assurances et prévoyance : mutuelle, prévoyance (décès, invalidité, incapacité), assurance emprunteur, responsabilité civile, protection juridique. Ordres de grandeur de tarifs, ce qui est obligatoire, ce qui est utile, pièges.
- Succession et transmission : assurance vie et clause bénéficiaire, abattements (en ligne directe, entre époux, pacsés), testament, accès des proches aux comptes, documents à tenir à jour.
- Augmenter ses revenus : leviers (négociation, mobilité, compétences, activité complémentaire), statuts d'activité annexe en France (auto-entrepreneur), seuils fiscaux et sociaux, chiffres.
- Indicateurs de santé financière : ratios utiles (taux d'épargne, taux d'endettement, mois de précaution, patrimoine net), seuils d'alerte et d'excellence.

Fournis un CSV « budget-reperes.csv » : poste, profil_revenu, montant_moyen_mensuel, part_du_revenu_pct, annee, source_url.
```

### Prompt 11. Arnaques et fraudes financières

```
SUJET : repérer et éviter les arnaques financières visant les investisseurs particuliers en France.

Couvre, en points numérotés au format du prompt maître :
- Les listes noires et registres officiels : AMF (liste noire des sites non autorisés), ACPR, ORIAS, Banque de France (listes de sites douteux), registre des PSAN pour les crypto-actifs, registre des intermédiaires. Pour chacun : URL, ce qu'il contient, comment faire une vérification en moins de 3 minutes, limites.
- Typologie des arnaques les plus courantes en France (faux brokers et Forex, binaires, crypto, faux conseillers en placement, usurpation d'identité de conseillers et de sites officiels, arnaques sentimentales avec investissement, « signaux » de trading payants, faux placements « diamants », vins, terres rares, SCPI frauduleuses, arnaques au CPF, recouvrement de pertes, pump and dump sur réseaux sociaux). Pour chacune : fonctionnement pas à pas, signaux d'alerte, chiffres de victimes ou de montants (AMF, Banque de France, ACPR, Cybermalveillance, Gendarmerie), exemples réels documentés.
- Signaux d'alerte universels : rendement promis, urgence, paiement en crypto, pression, absence d'agrément, demande de prise en main à distance, promesse de remboursement.
- Que faire si on a été victime : démarches, délais, interlocuteurs (plainte, signalement, opposition bancaire, chargeback, médiateur de l'AMF), cas des virements, des cartes, de la crypto.
- Sécurité de ses comptes : double authentification, hameçonnage (faux mails de courtier), téléphonie (vishing), SIM swapping, gestion des mots de passe, protection des données et de l'accès des proches en cas de décès.
- Garanties : garantie des dépôts (100 000 €), garantie des titres (70 000 €), garantie de l'assurance vie (Fonds de garantie des assurances de personnes), ce qu'elles couvrent et ne couvrent pas, avec montants en vigueur.
- Dix exemples de messages ou d'annonces d'arnaque réalistes (textes anonymisés), avec l'analyse des signaux d'alerte.
- Un « arbre de décision » en 10 questions pour juger une offre.

Fournis un CSV « arnaques-signaux.csv » : type_d_arnaque, signal_d_alerte, verification_a_faire, source_url, date.
```

### Prompt 12. Bibliographie et sources

```
SUJET : bibliographie de référence pour un assistant d'investissement français destiné à des investisseurs particuliers.

Livre un fichier Markdown « 00-SOURCES.md » avec :
1. Les sources officielles françaises et européennes par thème (fiscalité, régulation, statistiques, épargne, retraite, assurance), avec URL et description en une ligne.
2. Les sources académiques et institutionnelles (articles fondateurs et références) sur : diversification et portefeuille (Markowitz, Fama et French, Sharpe), investissement passif, coûts et frais, comportement (Kahneman et Tversky, Barber et Odean, Thaler), retrait (Bengen, Trinity), performance des fonds actifs (SPIVA, Morningstar Active/Passive Barometer). Pour chacun : auteurs, année, titre exact, éditeur ou revue, lien (accès libre si possible), conclusion principale en une phrase.
3. Les livres de référence accessibles à des débutants et intermédiaires, en français quand c'est possible (titre, auteur, année, éditeur, niveau, à retenir en 2 phrases, avis de pertinence pour le contexte français).
4. Les sites éducatifs et outils gratuits utiles (simulateurs, comparateurs, bases de données ETF), avec leurs limites et leur éventuel conflit d'intérêts (affiliation, publicité).
5. Les sources de données de marché gratuites et leur licence.
6. Une section « sources à éviter ou à relativiser » avec le raisonnement (conflits d'intérêts, promesses de rendement, biais de survie).

Pour chaque entrée : indique l'année de dernière mise à jour connue et marque « À VÉRIFIER » si tu n'es pas certain que l'URL ou la référence soit exacte. N'invente aucune référence : mieux vaut une liste plus courte et exacte qu'une liste longue et approximative.
```

---

## Après la recherche

Quand tu ramènes les résultats, je :
1. fusionne les réponses dans `connaissances/` (fiches développées, même numérotation A à I, points enrichis ou ajoutés) ;
2. remplis `00-SOURCES.md` ;
3. remplace les taux figés 4/5/7 % des projections par des fourchettes sourcées, et ajoute un simulateur fiscal et un Monte Carlo aux scripts ;
4. mets à jour les agents pour qu'ils citent les nouvelles fiches.
