# Idées pour le cahier des charges

Document de travail. Chaque idée a une priorité (P1 = socle, P2 = fort impact, P3 = plus tard) et une difficulté (facile, moyen, dur). On trie ensemble, puis on en tire le vrai cahier des charges.

---

## 0. Principes de base (à valider avant tout)

1. **Aide à la décision, pas exécution.** L'assistant analyse, alerte, challenge. Il ne passe jamais d'ordre tout seul. Les clés de broker, si on en branche un jour, sont en lecture seule.
2. **Les chiffres viennent du code, jamais de la mémoire du modèle.** Prix, performances, ratios, fiscalité : calculés par des scripts à partir de données sourcées. Le modèle explique et interprète, il ne "devine" aucun chiffre. C'est la règle qui évite les hallucinations dangereuses.
3. **Toute affirmation est sourcée** (lien, date, niveau de confiance). Pas de source, pas d'affirmation.
4. **Le levier principal de performance est le comportement**, pas la prédiction : frais, diversification, régularité, éviter le FOMO et la vente panique. L'assistant doit surtout nous protéger de nous-mêmes.
5. **Un profil par utilisateur** : l'assistant sait toujours qui lui parle (horizon, risque, enveloppes, objectifs, règles perso) et adapte tout en conséquence.
6. **Cadre légal** : tant que l'outil reste pour nous deux, c'est un outil perso. Dès qu'on le donne à d'autres personnes avec des recommandations personnalisées, on entre dans le territoire du conseil en investissement (statut CIF, AMF). À trancher avant d'ouvrir à des tiers.

---

## 1. Profils et personnalisation (P1)

- **Onboarding conversationnel** (15 questions) : horizon, objectifs chiffrés, tolérance au risque réelle (via scénarios "ton portefeuille perd 25 %, tu fais quoi ?"), niveau de connaissance, temps disponible, enveloppes (PEA, CTO, assurance vie, PER, crypto), contraintes (éthique, secteurs exclus).
- **Fichier profil par personne** (`prive/<prenom>/profil.md`) : l'assistant le charge au début de chaque session.
- **Règles personnelles** que l'assistant fait respecter : "max 8 % par ligne", "jamais d'achat sur un titre sans thèse écrite", "pas d'achat dans les 24 h après une hausse de plus de 10 %".
- **Style de communication réglable** : concis ou détaillé, niveau débutant ou avancé, ton direct.
- **Portefeuilles multiples** : perso de chacun + portefeuille commun éventuel, avec droits de visibilité (je vois le tien ou pas).
- **Mise à jour du profil** : l'assistant détecte quand la situation change (nouveau salaire, objectif, enfant, achat immobilier) et propose de mettre à jour.

## 2. Connexions de données (P1)

- **Google Sheets** (P1, facile) : lecture de la compta des investissements (lignes, quantités, prix de revient, dates, frais). Écriture possible pour les journaux et rapports.
- **Imports de relevés broker** (P1, moyen) : CSV/PDF Trade Republic, Boursorama, Degiro, IBKR, Bitpanda, etc. Normalisés dans un format unique.
- **Prix de marché** (P1, facile) : yfinance pour démarrer (gratuit, non officiel, fragile), puis Twelve Data, Finnhub, Alpha Vantage ou EODHD pour la fiabilité. Cours, historiques, dividendes, splits, taux de change.
- **Fondamentaux** (P2, moyen) : bilans, résultats, ratios via Financial Modeling Prep ou EODHD.
- **Documents officiels** (P2, moyen) : SEC EDGAR (10-K, 10-Q, 8-K, Form 4 insiders), documents d'enregistrement universels français, communiqués de résultats.
- **Macro** (P2, facile) : FRED (taux, inflation, emploi US), BCE, INSEE, calendrier des banques centrales.
- **News et RSS** (P1, facile) : flux de presse financière, GDELT pour la géopolitique, NewsAPI.
- **Calendrier** (P2, facile) : dates de résultats, dividendes, détachements, réunions Fed/BCE, publications macro.
- **Crypto** (P3) : CoinGecko, wallets en lecture seule.
- **Open banking** (P3, dur) : pour voir la capacité d'épargne mensuelle et alimenter le plan d'investissement.

## 3. Suivi et analyse du portefeuille (P1)

- **Tableau de bord** : valeur totale, performance jour/semaine/mois/an/depuis l'origine, plus-values latentes et réalisées.
- **Vraie performance** (P1, moyen) : performance pondérée par le temps (TWR) et par les flux (MWR/XIRR), après frais et devises. C'est ce qui permet de savoir si on bat vraiment le marché.
- **Comparaison à un benchmark** : MSCI World, S&P 500, CAC 40, ou un portefeuille "bête" 100 % ETF monde. La question centrale : *est-ce qu'on fait mieux qu'un simple ETF ?*
- **Répartition** : par classe d'actifs, secteur, zone géographique, devise, taille de capitalisation, enveloppe.
- **Risque de concentration** : poids des lignes, exposition cachée (3 ETF qui contiennent tous Apple et Nvidia), dépendance à un secteur ou une devise.
- **Métriques de risque** : volatilité, drawdown max, Sharpe, Sortino, bêta, corrélations entre lignes, value at risk.
- **Contribution à la performance** : quelle ligne a fait gagner ou perdre, en points de pourcentage.
- **Revenus** : calendrier des dividendes à venir, rendement du portefeuille, projection des revenus passifs.
- **Frais** : total des frais de courtage, de gestion (TER des ETF), de change, par an. Impact cumulé sur 10 ans.
- **Détecteur d'écarts** : "ton portefeuille s'est éloigné de l'allocation cible de plus de 5 %".
- **Suggestions de rééquilibrage** (P2) : combien acheter ou vendre pour revenir à la cible, en tenant compte des frais et de la fiscalité.

## 4. Veille et newsletter quotidienne (P1)

**Newsletter de 8 h, personnalisée par utilisateur :**
- Ce qui a bougé sur *tes* lignes (hier à la clôture, pré-marché, futures).
- Pourquoi (la news ou l'événement qui explique le mouvement, avec source).
- Les événements du jour qui touchent le portefeuille : résultats, dividendes, publications macro, discours de banquiers centraux.
- Politique et géopolitique filtrées par impact : on ne résume pas "toute l'actualité", seulement ce qui touche les positions (tarifs douaniers, élections, sanctions, régulation d'un secteur).
- **Score d'importance** de chaque info (à ignorer / à surveiller / à agir) pour éviter le bruit.
- Les 3 points d'attention de la journée, et un rappel de nos propres règles.
- Format : email (Resend ou Gmail), Telegram ou Discord. Lisible en 3 minutes.
- Variantes : **résumé de clôture** (18 h), **revue hebdomadaire** du dimanche, **revue mensuelle** avec bilan de performance.
- **Mode "ne rien faire"** : si rien d'important, l'assistant le dit explicitement. Une bonne journée d'investisseur est souvent une journée sans action.

## 5. Alertes (P2)

- Seuils de prix, d'écart au cours moyen d'achat, de baisse depuis un plus haut.
- Résultats publiés sur une ligne détenue ou en watchlist, avec résumé immédiat et écart aux attentes.
- Dirigeants qui achètent ou vendent (Form 4, déclarations AMF).
- Changement de recommandation d'analystes, changement de dividende, augmentation de capital.
- Rupture de nos propres règles (ligne qui dépasse 10 % du portefeuille).
- Événement macro majeur (surprise d'inflation, décision de taux).
- **Anti-spam** : plafond d'alertes par jour, regroupement, niveau d'urgence.

## 6. Aide à la décision (P1/P2)

- **Fiche d'analyse d'une entreprise** (P1, moyen) : activité, chiffres clés sur 10 ans, marges, dette, flux de trésorerie, valorisation vs historique et vs concurrents, risques, catalyseurs.
- **Thèse d'investissement écrite avant tout achat** (P1) : pourquoi j'achète, ce que j'attends, horizon, **conditions qui invalident la thèse**, prix où je revends. Stockée dans le journal.
- **Checklist pré-achat** : taille de position, impact sur la diversification, frais, enveloppe fiscale adaptée, liquidité.
- **Avocat du diable** (P1) : l'assistant doit argumenter contre notre idée avant de la valider. Contre-arguments, pré-mortem ("on est dans 1 an, c'est un échec, pourquoi ?").
- **Scénarios bull / base / bear** avec probabilités et rendement attendu de chaque cas.
- **Dimensionnement de position** : combien investir selon la conviction, le risque et le portefeuille actuel.
- **Comparateur** de deux titres ou ETF (frais, composition, performance, chevauchement).
- **Screener personnalisé** : filtres à nous (qualité, croissance, valorisation), résultats rafraîchis chaque semaine.
- **Watchlist avec déclencheurs** : "j'achète si le titre passe sous X ou si le P/E repasse sous Y".
- **Lecture de documents** (P2) : résumé d'un rapport annuel, d'un call de résultats, d'un prospectus d'ETF, avec les passages clés cités.
- **Analyse d'impact d'une news** sur le portefeuille : "cette décision de la Fed touche quelles lignes, de quelle façon ?"
- **Mode "second avis"** : on colle une idée vue sur YouTube, Reddit ou X, l'assistant vérifie les faits, cherche qui a intérêt à la pousser, et la teste contre nos règles.

## 7. Journal et amélioration de la performance (P1)

C'est le module qui améliore vraiment la performance annuelle.

- **Journal de décisions** : chaque achat, vente ou "non-décision" avec la raison, l'état d'esprit (confiant, stressé, euphorique), la source de l'idée.
- **Post-mortem automatique** à 1, 3, 6, 12 mois : la thèse s'est-elle vérifiée ? Résultat dû à la bonne analyse ou à la chance ?
- **Détection de biais** : FOMO (achats après de fortes hausses), vente trop précoce des gagnants, conservation des perdants, sur-trading, ancrage sur le prix d'achat, concentration sur ce qu'on aime.
- **Statistiques de décision** : taux de réussite, gain moyen vs perte moyenne, durée de détention, performance par type de décision.
- **Attribution de performance** : quelle part vient de l'allocation, de la sélection de titres, du timing, des frais.
- **Comparaison contrefactuelle** : "si tu n'avais rien touché depuis janvier, tu aurais fait X %". Chiffre qui fait souvent réfléchir.
- **Objectifs annuels** et suivi : rendement visé, taux d'épargne, nombre de lignes, frais maximum.
- **Bilan annuel** automatique : ce qui a marché, ce qui a échoué, 3 règles à ajouter pour l'année suivante.
- **Cooling-off** : avant une grosse décision émotionnelle, l'assistant impose un délai et pose 5 questions.

## 8. Simulation et backtest (P2)

- **Backtest de règles** : "que donne une stratégie de DCA mensuel vs investissement en une fois ?" Avec frais et fiscalité.
- **Simulation Monte Carlo** : probabilité d'atteindre un objectif (capital X à telle date) selon l'épargne et l'allocation.
- **Stress tests** : le portefeuille actuel en 2008, mars 2020, 2022.
- **Scénarios "et si"** : -20 % sur la tech, dollar -10 %, taux +1 point.
- **Planificateur d'objectifs** : combien épargner par mois pour atteindre un objectif.
- Garde-fou : un backtest n'est pas une promesse, l'assistant rappelle les limites (biais du survivant, sur-optimisation).

## 9. Fiscalité française (P2)

- Suivi de l'ancienneté du PEA (seuil des 5 ans), plafonds de versement, répartition PEA/CTO/assurance vie.
- **Simulateur de vente** : impôt estimé (flat tax ou barème, prélèvements sociaux) avant de vendre.
- Moins-values reportables, compensation, optimisation de la date de vente.
- Retenues à la source sur dividendes étrangers, crédit d'impôt.
- Préparation de la déclaration (IFU, cases 2042, 2074), crypto (2086).
- Garde-fou : informations à vérifier avec un expert-comptable ou le site des impôts, les règles changent.

## 10. Apprentissage (P2)

- **Parcours personnalisé** selon le niveau et les lacunes détectées dans le journal.
- **Mode mentor** : l'assistant pose des questions plutôt que de donner la réponse.
- **Glossaire contextuel** : on clique sur un terme dans la newsletter, explication simple avec un exemple tiré du portefeuille.
- **"Explique-moi cette news"** à trois niveaux (débutant, intermédiaire, expert).
- **Études de cas** basées sur *nos propres* décisions passées.
- **Quiz et flashcards** à répétition espacée sur les notions vues.
- **Lecture guidée d'un bilan** : on le fait ensemble, ligne par ligne.
- **Résumés de livres de référence** (Graham, Lynch, Marks, Munger) reliés à nos situations réelles.
- **Défi mensuel** : analyser une entreprise inconnue de A à Z.

## 11. Collaboration à deux (P2)

- **Portefeuille et watchlist communs**, avec historique des décisions partagées.
- **Débat structuré** : chacun écrit sa thèse, l'assistant compare, trouve les vrais points de désaccord et les données qui permettraient de trancher.
- **Journal de décisions partagé** avec commentaires.
- **Tableau de bord comparatif** perso vs perso vs benchmark (amical).
- **Notes partagées** et base de connaissances commune (analyses déjà faites, entreprises écartées et pourquoi).
- **Notifications croisées** : "ton associé vient d'ajouter X à sa watchlist".

## 12. Interfaces et automatisation (P1/P2)

- **Commandes** : `/point` (état du portefeuille), `/analyse TICKER`, `/news`, `/rebalance`, `/fiscal`, `/journal`, `/revue-mensuelle`.
- **Tâches planifiées** : newsletter 8 h, clôture 18 h, revue du dimanche, rappels de post-mortem.
- **Canaux** : email, Telegram ou Discord (conversation avec l'assistant depuis le téléphone), Google Sheets.
- **Dashboard web** (P3) : graphiques interactifs, vue allocation, performance.
- **Workflows n8n** (déjà utilisé en local) pour les enchaînements simples.
- **Mode vocal** (P3) : brief audio du matin.

## 13. Architecture possible

| Option | Principe | Pour | Contre |
|---|---|---|---|
| A. Workspace Claude Code | Skills + commandes + tâches planifiées, fichiers de profil | Zéro infra, très rapide, déjà notre façon de travailler | Dépend d'un PC allumé ou de tâches cloud, pas d'interface pour des tiers |
| B. Scripts Python + automatisation | Scripts de calcul, GitHub Actions ou serveur pour les tâches, API Claude pour la rédaction, bot Telegram | Fiable, tourne tout seul, calculs vérifiables | Plus de code à maintenir |
| C. Application web complète | Next.js + base (Supabase) + API Claude, comptes utilisateurs | Multi-utilisateurs propre, vraie interface | Le plus long, obligations RGPD et réglementaires |

**Recommandation :** démarrer avec A + B (Python pour les calculs et les données, Claude pour l'analyse et la rédaction, Google Sheets comme base), architecture modulaire et profils par utilisateur dès le départ. Passer à C seulement si l'usage le justifie.

Modules à séparer proprement : `data/` (connecteurs), `analytics/` (calculs), `agents/` (analyse IA), `reports/` (newsletter, bilans), `profiles/` (utilisateurs), `journal/`.

## 14. Sécurité et conformité

- Clés API dans `.env`, jamais dans le code ni dans le dépôt.
- Aucune clé de broker avec droit d'ordre. Lecture seule uniquement.
- Données financières perso : dépôt privé, accès limité, pas de partage de relevés bruts à des services tiers inutiles.
- RGPD si on ouvre à d'autres utilisateurs.
- Avertissement systématique : outil d'information et d'aide à la réflexion, pas un conseil personnalisé en investissement.
- Journal des sources utilisées pour chaque analyse (traçabilité).
- Tests automatiques sur les calculs (performance, fiscalité) avec cas connus.

## 15. Roadmap proposée

**MVP (2 semaines)**
1. Profils utilisateurs + onboarding
2. Connexion Google Sheet + prix de marché
3. Rapport de portefeuille (allocation, concentration, performance vs benchmark)
4. Newsletter de 8 h personnalisée
5. Journal de décisions + thèse avant achat

**V1 (1 à 2 mois)**
Alertes, fiche d'analyse d'entreprise, avocat du diable, revue hebdomadaire et mensuelle, détection de biais, import des relevés de broker.

**V2**
Backtests et simulations, fiscalité française, parcours d'apprentissage, module de collaboration (débat des thèses), bot Telegram conversationnel.

**V3**
Dashboard web, lecture de documents officiels, ouverture à d'autres utilisateurs (après analyse réglementaire).

## 16. Questions ouvertes pour cadrer

1. Quels brokers et enveloppes utilisez-vous (PEA, CTO, assurance vie, crypto) ?
2. Combien de lignes, quels types d'actifs (actions en direct, ETF, crypto) ?
3. Horizon et objectif chiffré de chacun ?
4. Le Google Sheet existe déjà ? Quelles colonnes ?
5. Canal préféré pour la newsletter (email, Telegram, Discord) ?
6. Budget mensuel acceptable pour les données et l'API (gratuit, 20 euros, 50 euros) ?
7. Portefeuille commun ou deux portefeuilles séparés ?
8. L'outil restera-t-il entre vous deux, ou une ouverture à d'autres est-elle envisagée ?
9. Quel niveau de détail pour l'analyse (investisseur long terme ou trading actif) ?
10. Qui maintient quoi entre vous deux (répartition des modules) ?
