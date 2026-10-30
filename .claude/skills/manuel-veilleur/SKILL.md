---
name: manuel-veilleur
description: Manuel de compétences du Veilleur (brief du jour, news, macro, secteurs, calendrier). Chargé automatiquement dans l'agent veilleur.
---

# Manuel de compétences du Veilleur

Fusion des meilleurs skills open source, adaptés à un particulier français et à nos règles (pas de prédiction, pas d'avis d'achat ou de vente). Sources par compétence en fin de fichier ; tri complet dans `docs/externe/tri-des-skills.csv`. Ouvre la section dont tu as besoin, pas tout le fichier.

## 1. Brief du jour
*Base : `morning-note` (Anthropic). Retiré : « idées de trades », objectifs de cours, « soyez tranchant ».*
- Lisible en 2 minutes, une page maximum. **Le plus important d'abord**, jamais enterré au milieu.
- Plan : (1) **le titre du jour** en 2-3 phrases, « pourquoi ça compte pour toi » ; (2) ce qui a bougé sur ses ETF ou ses indices de référence, chiffre de clôture et source ; (3) l'agenda du jour avec l'heure ; (4) le verdict, le plus souvent « rien à faire » ; (5) une notion en 3 lignes.
- « **Rien d'important** » est un brief valable : le dire franchement plutôt que remplir.
- Séparer ce qui touche le plan (fiscalité, frais d'un ETF, changement d'indice) du bruit (note d'un analyste, rumeur).
- Horodater : « écrit à 8 h, avant l'ouverture, les chiffres peuvent changer ».
- Si un brief précédent s'est trompé, le dire dans le suivant : la crédibilité compte plus que d'avoir raison.
- Résultats d'une entreprise présente dans ses ETF : petit tableau attendu / publié (chiffre d'affaires, bénéfice par action, prévisions), puis « est-ce que ça change quelque chose pour un ETF monde ? » (presque toujours non : poids de la société, `scripts/exposition.py`).

## 2. Agenda des événements
*Base : `catalyst-calendar` (Anthropic), `earnings-calendar` (staskh).*
- Univers suivi : les plus grosses entreprises de ses ETF (top 10 dans `donnees/indices-entreprises.csv`) et la macro (BCE, Fed, inflation zone euro et France, emploi américain), plus les échéances qui le concernent personnellement (déclaration d'impôts, révision du Livret A le 1er février et le 1er août, revue annuelle de la charte).
- Tableau : date, événement, ce qui est concerné, impact attendu (fort, moyen, routine). Vue de la semaine, et aperçu de la suivante.
- Les dates de résultats bougent : les vérifier sur le site de l'entreprise à l'approche. Le serveur `financial-data` donne des dates (à recouper).
- Garder les événements passés avec ce qui s'est réellement passé : on apprend à relativiser.

## 3. Tableau de bord macro et taux
*Base : `macro-rates-monitor` (Anthropic).*
- Quatre questions, dans l'ordre : où en est le cycle (croissance, emploi, activité) ? Que fait la banque centrale (taux directeur) ? Que dit le marché obligataire (pente de la courbe 2 ans-10 ans, taux réels = taux nominal moins inflation) ? Les conditions financières se durcissent-elles ou s'assouplissent-elles ?
- Données : `financial-data` (`get_macro_series`, `get_yield_curve`, `get_inflation_snapshot`), BCE, INSEE. Situer chaque chiffre par rapport à son historique récent.
- Conclusion toujours ramenée au portefeuille : « ce qui change pour toi », le plus souvent rien pour un investisseur long terme.

## 4. Comprendre un secteur
*Base : `sector-overview` (Anthropic).*
- Taille et croissance du marché (avec la source), concentration (les 5 premiers), où se crée la valeur, barrières à l'entrée, tendances de fond et vents contraires, principaux acteurs avec leurs marges, comment ils se font concurrence, valorisation du secteur par rapport au marché.
- Distinguer le marché réellement accessible du discours « marché potentiel immense ». Dater les chiffres, ils vieillissent vite.
- Pas de « meilleures opportunités » : présenter le débat (arguments pour et contre), pas une conclusion d'achat.

## 5. Vérifier une information
*Base : `research-claim-map` (lyndonkl).*
1. Reformuler l'affirmation en version précise et vérifiable (chiffres, dates).
2. Rassembler les éléments pour et contre.
3. Noter la qualité : **primaire** (donnée brute, texte officiel, publication de l'entreprise) > **secondaire** (presse sérieuse qui cite ses sources) > **tertiaire** (résumé, communiqué marketing) > **non recevable** (réseau social, « des experts disent », source anonyme).
4. Ce qu'on ne sait pas. « Pas trouvé de preuve » n'est pas « preuve que c'est faux ».
5. Conclusion avec un niveau de confiance chiffré (par exemple 70 %), pas « probablement ».

## 6. Ne pas inventer de récit
*Base : `narrative-fallacy-guard`, `causal-inference-root-cause` (lyndonkl).*
- Une cause n'est donnée que si une source datée la fournit : « selon Reuters... ». Sinon : « cause non établie ».
- Pièges : « après, donc à cause de » ; corrélation prise pour une cause ; retour à la moyenne présenté comme un événement ; explication choisie après coup parce qu'on connaît la fin.
- Toujours au moins une autre explication possible. Dire qui a intérêt à la version racontée.
- Ne pas tomber dans l'excès inverse : si une cause est solidement établie, l'affirmer clairement, une seule fois.

## 7. Veille structurée (revue trimestrielle)
*Base : `environmental-scanning-foresight` (lyndonkl).*
- Balayer politique, économie, société, technologie, droit, environnement, pour repérer ce qui pourrait changer le plan à 3-5 ans (fiscalité de l'épargne, réforme des retraites, taux, démographie).
- Distinguer un signal faible crédible du bruit (source, preuves, plausibilité).
- Scénarios : 3 au plus, plausibles et non souhaités ou redoutés, **sans probabilité ni prédiction**. Pour chacun, les indicateurs à surveiller et le seuil qui justifierait de revoir la charte.

## 8. Lire vite un document
*Base : `inspectional-reading` (lyndonkl).*
- Avant de tout lire (rapport, prospectus, document d'informations clés) : titre, auteur, date, sommaire, introduction, conclusion. Classer le document, juger s'il mérite une lecture complète pour la question posée, résumer en une ligne. Ne pas inventer une date ou un auteur non visibles.

## 9. Données de marché fiables
*Base : `market-data` (joellewis), `stock-quote`, `price-history` (staskh), serveur `financial-data`.*
- Données Yahoo Finance indicatives (API non officielle, parfois en retard) : citer « Yahoo Finance via financial-data », l'heure, la devise. Signaler un écart supérieur à 2 % sur une journée sans le dramatiser.
- Méfiance : données périmées, trous, historiques sans les sociétés disparues (biais du survivant). Jamais de décision sur un seul chiffre.

## 10. Actualité (sources)
Voir `connaissances/H-information.md` (points 74 à 81) pour la hiérarchie des sources et la grille « ignorer, surveiller, agir ». Outils : `financial-data` (`get_stock_news` pour une entreprise), `actualite-flux` (flux RSS BCE, Le Monde économie, BBC Business) et `lecture-web` (lire un article ou un communiqué précis).

---
Sources : anthropics/financial-services-plugins (Apache 2.0) : morning-note, catalyst-calendar, macro-rates-monitor, sector-overview. joellewis/finance_skills (MIT) : market-data. staskh/trading_skills (MIT) : earnings-calendar, stock-quote, price-history. lyndonkl/claude (pas de licence, idées reformulées) : research-claim-map, narrative-fallacy-guard, causal-inference-root-cause, environmental-scanning-foresight, inspectional-reading.
