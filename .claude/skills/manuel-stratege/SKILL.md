---
name: manuel-stratege
description: Manuel de compétences du Stratège (charte, objectifs, enveloppes, fiscalité, retrait). Chargé automatiquement dans l'agent stratege.
---

# Manuel de compétences du Stratège

Fusion des meilleurs skills open source adaptés à la France (PEA, assurance vie, CTO, PER) et à nos règles. Fiscalité : toujours `connaissances/C-fiscalite.md` et `scripts/fiscalite.py`, jamais les règles américaines des skills d'origine (401k, IRA, 529, « wash sale »). Ouvre seulement la section utile.

## 1. Charte d'investissement
*Base : `investment-policy`, `investment-proposal` (Anthropic), `proposal-generation`.* Modèle : `templates/charte-modele.md`.
- **Objectif de rendement** : le taux qui finance les besoins futurs, pas celui qu'on espère. Rendement nominal nécessaire ≈ besoin de rendement réel + inflation + frais. Un objectif de rendement supérieur à ce que le risque toléré permet est un défaut de la charte.
- **Capacité** (revenus stables, patrimoine par rapport aux besoins, horizon, liquidités) et **volonté** (réaction aux pertes) : évaluées séparément ; **la plus basse décide**. Éduquer pour relever la volonté, jamais forcer.
- **Contraintes**, cinq familles : liquidité (besoins sous 3 ans, épargne de précaution), droit et fiscalité (enveloppes), horizon (une ou plusieurs phases), fiscalité, particularités (valeurs éthiques, actions de l'employeur, crédit en cours).
- **Allocation cible avec fourchettes** (par exemple actions 70-90 %), pas un chiffre unique : la fourchette laisse des marges avant de rééquilibrer.
- **Politique de rééquilibrage** (calendrier, seuil ou les deux), **indice de référence** : investable (un ETF existe), mesurable, **fixé à l'avance**, adapté à l'allocation.
- **Revue** : annuelle, plus immédiate après un événement de vie (naissance, séparation, perte d'emploi, héritage, achat immobilier).
- Piège : rigide au point d'être inapplicable, ou si lâche qu'il n'impose rien ; changer d'indice après coup pour embellir.
- Proposition à un particulier : approche, allocation proposée, résultats possibles **en fourchette**, frais, risques ; jamais « voici ce que vous gagnerez ».

## 2. Allocation stratégique
*Base : `asset-allocation`.* Part d'actions selon capacité et volonté (fiche D, points 22 et 56) ; l'allocation explique l'essentiel du risque, plus que le choix des lignes. Test de crise obligatoire avant validation (`scripts/stress.py`). Documenter pourquoi on détient chaque poche (inflation, longévité, croissance), pas seulement le pourcentage.

## 3. Objectifs et épargne nécessaire
*Base : `savings-goals`, `time-value-of-money`, `financial-goal-planner`, `roadmap-backcast`, `reference-class-forecasting`.*
- Épargne mensuelle nécessaire pour un objectif à une date : `scripts/projection.py` (donne le versement requis). Exprimer l'objectif en **euros d'aujourd'hui** (`--inflation 2`).
- **Planifier à rebours** : fixer la date et le montant, remonter à aujourd'hui : jalons, dépendances, montant à épargner par an, ce qu'il faut pour que ce soit faisable.
- **Classe de référence** : situer l'objectif par rapport à ce qui s'est vraiment passé pour des gens dans la même situation (rendements historiques réalistes, durées) plutôt que d'ancrer sur l'enthousiasme. Un objectif irréaliste appelle un jalon intermédiaire daté.
- **Ordre des priorités** (version française, fiche A, point 111) : épargne de précaution, abondement de l'employeur, dettes à plus de 5-6 %, PEA, assurance vie, puis autres projets (achat immobilier, études, voyage). Plusieurs objectifs : une poche par objectif, les plus proches d'abord, jamais en actions sous 3 ans.
- Retraite : capital cible et taux de retrait (fiche B, points 90 à 95).

## 4. Retraite et retraits
*Base : `retirement-decumulation`.*
- **Risque de séquence** : une baisse en début de retraite pèse bien plus qu'une baisse tardive ; deux investisseurs de même rendement moyen finissent très différemment.
- **Règle des 4 %** : repère, pas garantie (fiche B, point 90). Plus l'horizon est long, plus le taux sûr baisse (3 à 3,25 % sur 40-50 ans).
- **Garde-fous** : taux de départ (par exemple 5 %), retraits relevés de l'inflation chaque année, bornes à ±20 % du taux de départ ; si le taux réel monte de plus de 20 % au-dessus (soit 6 % pour 5 %), **réduire de 10 %** ; s'il descend de plus de 20 % en dessous (4 %), **augmenter de 10 %** ; sauter l'indexation après une année de baisse. Contrepartie : un revenu de départ plus élevé, payé par une variabilité que la personne doit accepter d'avance.
- **Seaux** (1 à 3 ans de dépenses en liquidités, le reste en actions) contre rendement total : le seau rassure, il n'augmente pas le rendement attendu.
- **Rente viagère** (PER, assurance vie) : assurance contre la longévité, prix de la perte de capital transmissible ; à envisager pour couvrir les dépenses incompressibles.
- Ordre de retrait en France : arbitrer entre enveloppes selon leur fiscalité (fiche C, points 16 et 53). Pension publique à l'âge légal (à vérifier).

## 5. Optimisation fiscale des enveloppes (France)
*Base : `tax-efficiency`, `tax-loss-harvesting`, `tax-strategy-optimizer`, `tax-loss-harvest-scanner`.*
- **Localisation d'actifs** : mettre où la fiscalité est la plus douce ce qui rapporte le plus (actions de croissance dans le PEA après 5 ans) ; fonds en euros et obligations dans l'assurance vie ; CTO pour ce qui ne rentre pas ailleurs (actions américaines, ETF non éligibles PEA).
- **Moins-values** : imputables sur les plus-values de même nature, reportables 10 ans sur CTO (fiche C, point 17). Réaliser une moins-value pour compenser une plus-value n'est utile que si l'impôt économisé justifie les frais et le changement de ligne. Remplacer par un ETF **différent mais similaire** ; la France n'a pas de règle « wash sale » aussi explicite que les États-Unis, mais l'administration peut contester un montage purement fiscal : prudence, à faire valider par un professionnel pour les gros montants.
- **Calendrier** : étaler une grosse vente sur plusieurs années peut utiliser plusieurs fois les abattements (assurance vie) ; une vente en CTO déclenche l'impôt de l'année.
- **Éviter l'impôt qu'on peut éviter** : diriger les versements vers le PEA plutôt que vendre le CTO pour le transférer (fiche C, point 117).
- **Préparer sa déclaration** *(base : `cowork-tax-prep-organizer`)* : rassembler les justificatifs par formulaire (IFU des courtiers français, relevés des courtiers étrangers, 2042 et 2042-C, 2047 revenus étrangers, 2074 plus-values, 2086 crypto, 3916 comptes à l'étranger), vérifier les montants préremplis, garder les justificatifs. En avril : rappel au Directeur.
- Simulations : `scripts/fiscalite.py`. Toujours « à vérifier avec un professionnel pour les cas complexes ».

## 6. Transmission
*Base : `estate-gifting`.* Clause bénéficiaire précise et à jour, assurance vie hors succession dans les limites (fiche C, point 53), donations (abattements en ligne directe, à vérifier), testament, accès des proches (fiche I, point 108). Dire la limite : ce n'est pas un conseil notarial.

## 7. Épargne salariale et actions gratuites
*Base : `equity-compensation`.* Intéressement et participation sur PEE ou PER collectif (abondement de l'employeur = argent gratuit, fiche A, point 86). Actions de son employeur : **risque de concentration** (emploi et patrimoine dépendent de la même société) : vendre régulièrement et plafonner (par exemple 5 à 10 % du patrimoine). Connaître la date de blocage et l'imposition à la livraison.

## 8. Décider sous incertitude
*Base : `expected-value`, `decision-matrix`, `hypotheticals-counterfactuals`, `chain-estimation-decision-storytelling`.*
- **Valeur espérée** : issues possibles × probabilités × montants ; attention, une espérance positive ne protège pas d'une ruine : regarder aussi le pire cas et sa réversibilité.
- **Matrice de décision** : critères pondérés (coût, risque, liquidité, fiscalité, souplesse), notes, puis tester la sensibilité aux pondérations.
- **Et si ?** : tester les hypothèses (si le rendement est 2 points plus bas, si je perds mon emploi, si la fiscalité change) et noter ce qui ne casse dans aucun scénario (« sans regret »).
- Exemples typiques : acheter ou louer, rembourser un crédit ou investir, PEA ou assurance vie, vendre un CTO.
- **Projections en probabilités** *(base : `monte-carlo-valuation`)* : exprimer en « 8 chances sur 10 d'avoir au moins X » ; hypothèses de rendement et de volatilité dans `docs/recherche/04-projection.md` ; distribution log-normale en première approximation (sous-estime les krachs) ; script Monte Carlo à créer.

## 9. Adéquation au profil
*Base : `investment-suitability`.* Avant de proposer un produit : objectif, horizon, connaissance, capacité à perdre, situation fiscale, produits déjà détenus. Un produit n'est « adapté » que s'il résiste à la question « et si ça baisse de 40 % ? ». Garder trace de la raison du choix.

## 10. Démarche de plan financier
*Base : `financial-planning-workflow`, `financial-planning-integration`.* Six étapes : (1) recueillir la situation (revenus, dépenses, patrimoine, dettes, protections) ; (2) objectifs et priorités ; (3) analyser (capacité d'épargne, projections, risques) ; (4) proposer (allocation, enveloppes, protections) ; (5) mettre en œuvre (ordres, virements automatiques) ; (6) suivre (revue annuelle, événements de vie). Le plan s'inscrit dans la charte.

## 11. Mémo de décision important
*Base : `ic-memo` (adapté).* Pour une grosse décision (achat immobilier, vente d'un gros CTO, arrêt de travail) : question, options, chiffres de chaque option (scénarios bas, central, haut), risques et réversibilité, ce qu'on ignore, décision proposée, **ce qui la ferait changer**, date de revue. Une page.

---
Sources : anthropics/financial-services-plugins (Apache 2.0) : investment-proposal, ic-memo. joellewis/finance_skills (MIT) : investment-policy, asset-allocation, savings-goals, time-value-of-money, retirement-decumulation, tax-efficiency, tax-loss-harvesting, estate-gifting, equity-compensation, investment-suitability, financial-planning-workflow, financial-planning-integration, proposal-generation. onewave-ai (MIT) : financial-goal-planner, tax-strategy-optimizer, cowork-tax-prep-organizer. lyndonkl (pas de licence, idées reformulées) : roadmap-backcast, reference-class-forecasting, expected-value, decision-matrix, hypotheticals-counterfactuals, chain-estimation-decision-storytelling, monte-carlo-valuation, tax-loss-harvest-scanner.
