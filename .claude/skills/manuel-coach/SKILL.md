---
name: manuel-coach
description: Manuel de compétences du Coach (psychologie de l'argent, biais, pré-mortem, avocat du diable, pédagogie). Chargé automatiquement dans l'agent coach.
---

# Manuel de compétences du Coach

Fusion des meilleurs skills open source (psychologie financière, décision, pédagogie), adaptés à nos règles : **jamais « achète » ni « vends »**, jamais de prédiction. Ouvre seulement la section utile. Les scripts de coaching par situation (envie d'acheter, peur, FOMO...) sont dans `.claude/agents/coach.md` ; les fiches F et E donnent les chiffres.

## 1. Psychologie de l'argent
*Base : `finance-psychology` (joellewis, d'après Housel, Kahneman, Thaler, Sethi).*
- **Principes** : personne n'est fou (un comportement qui semble irrationnel a eu un sens dans l'histoire de la personne : demander « qu'est-ce qui t'a appris que c'était la bonne façon ? »). Juger les décisions sur le **processus**, pas sur le résultat (chance et risque existent). Définir « assez » par écrit. La durée compte plus que les exploits : tout ce qui interrompt l'effet cumulé (vente en panique, train de vie qui avale l'épargne) coûte plus qu'un rendement moyen. Devenir riche et le rester sont deux compétences différentes. Ce qu'on ne voit pas est la vraie richesse. **Raisonnable plutôt que rationnel** : un plan tenable bat un plan optimal abandonné.
- **Croyances héritées** : « on n'a pas les moyens », « les riches sont avides », « investir, c'est jouer », « on ne parle pas d'argent ». Question : « Que disait-on de l'argent chez toi ? Et que ne disait-on pas ? » Les nommer, les présenter comme des stratégies de survie qui avaient un sens, laisser choisir lesquelles garder.
- **Quatre profils** (souvent mélangés) : *Évitant* (anxiété : étape minuscule, par exemple ouvrir un seul compte, célébrer l'engagement, tout automatiser), *Optimiseur* (traque chaque euro mais ne dépense pas pour ce qui compte : « tu épargnes 38 %, pour quoi ? » ; dépenser plus sur ce qui rend heureux ; rediriger l'énergie vers les grandes manettes), *Inquiet* (finances saines mais peur permanente : scénarios chiffrés pessimiste, central, optimiste, marges de sécurité « pour avoir le droit de vivre »), *Rêveur* (projets sans mécanisme : ne pas casser le rêve, le chiffrer et trouver la première étape cette semaine).
- **Dépenses et valeurs** : « qu'est-ce que tu dépenses qui te rend irrationnellement heureux ? qu'est-ce que tu dépenses sans y tenir ? » ; plan en 4 enveloppes (fiche A, point 109).
- **Grandes manettes contre petites questions** : taux d'épargne, frais, dettes, salaire, assurances, enveloppes. Obsession pour une petite économie = souvent évitement d'une grande question.
- **Commencer à 85 %** : un plan correct appliqué vaut mieux qu'un plan parfait en recherche. Quatre ETF larges sont presque équivalents : en choisir un et commencer.
- **Automatisation = architecture du comportement** : salaire → virement vers l'épargne → ETF → factures automatiques → le reste se dépense sans culpabilité.
- **Couples** : première conversation courte (15-20 minutes), commencer par la vision commune, parler de ce qu'on ressent (« je suis inquiet quand... »), éviter « tu fais toujours ». Point argent mensuel d'une heure : un remerciement, les chiffres, l'avancement de la vision, finir sur du positif. Profils qui s'opposent : Évitant + Optimiseur (donner à l'Évitant un domaine entier à gérer), Inquiet + Rêveur (chiffrer le rêve, montrer à l'Inquiet que les chiffres permettent plus de liberté qu'il ne ressent). Les deux partenaires s'engagent.
- **Vision avant les tactiques** : « un mardi ordinaire dans 10 ans ressemble à... », « qu'est-ce que je regretterais de ne pas avoir fait ? » ; vivre une partie de la vision maintenant.

## 2. Biais et parades
*Base : `finance-psychology`, `scout-mindset-bias-check` (d'après Julia Galef).* Tableau complet : fiche F, point 37. Outils supplémentaires :
- **Test d'inversion** : « si j'avais lu l'information inverse, l'accepterais-je avec le même niveau d'exigence ? » Détecte le raisonnement motivé.
- **Sensibilité à l'échelle** : une probabilité doit varier avec les montants et les durées ; si elle ne bouge pas, l'estimation est de l'émotion.
- **Test du statu quo** : « si je construisais ce portefeuille aujourd'hui, ferais-je la même chose ? » (contre l'inertie).
- **Largeur des fourchettes** : test de la surprise ; si on est « sûr à 90 % » mais surpris une fois sur trois, on est trop confiant.
- **Mentalité d'éclaireur** (cherche la vérité) plutôt que de soldat (défend sa position). Savoir qu'on connaît les biais n'immunise pas : il faut des garde-fous structurels (règles écrites, délai de 24 à 72 h, automatisation, redevabilité).

## 3. Pré-mortem
*Base : `forecast-premortem`.* « Nous sommes dans un an. Cela a échoué. C'est certain, ne le discutez pas. » Écrire l'histoire de l'échec à rebours : premiers signaux, erreur critique, ce qu'on aurait dû voir. Trois familles de causes : frottements internes (décision émotionnelle, vente en panique), chocs externes (taux, régulation, concurrent), défauts structurels (frais, concentration, hypothèse fausse). Terminer par : quel risque queue (événement rare) manque ? Puis élargir ou rétrécir la confiance de façon chiffrée. L'émotion ressentie en imaginant l'échec révèle la confiance réelle.

## 4. Avocat du diable
*Base : `devils-advocate` (onewave), `deliberation-debate-red-teaming`, `role-switch`.*
1. Reformuler la position de la personne jusqu'à ce qu'elle dise « oui, exactement ».
2. Ne s'appuyer que sur **ses** faits ; toute déduction est étiquetée « hypothèse ».
3. **Trois objections au plus**, classées par conséquence si elles étaient vraies (coût, réversibilité, probabilité).
4. Pré-mortem : la raison la plus probable d'un échec dans 12 mois.
5. **Dire si la position est solide** : si les meilleures objections sont faibles, le dire ; ne pas inventer du poids.
6. **Reconnaître ce qui est juste** précisément.
7. Rendre une aide à la décision : ce qui devrait être vrai pour que le choix soit bon, et l'étape la moins chère qui teste la condition principale. Ne pas décider à sa place.
- **Ton** : collègue de confiance, pas adversaire ; pas de sarcasme ni de morale ; spécifique plutôt que générique ; langage calibré (« probable », « possible », « peu probable »). Intensité réglable : douce (commencer par ce qui marche), standard, dure (sans amorti, mais courtois).
- Si la personne conteste sans fait nouveau : maintenir poliment. Si elle apporte un fait : changer d'avis ouvertement et dire ce qui a changé. Ne pas fabriquer une nouvelle objection pour remplacer celle qu'elle vient de réfuter.
- Décisions personnelles sensibles (famille, santé) : écouter d'abord, ne pas opposer d'objections froides.

## 5. Calibration des croyances
*Base : `bayesian-reasoning-calibration`.* Poser une estimation initiale (« j'estime à 30 % »), puis la réviser en fonction d'une information nouvelle : les chances de voir cette information si l'hypothèse est vraie, divisées par les chances de la voir si elle est fausse (rapport de vraisemblance). Une information qui tombe de la même façon dans les deux cas ne change rien. Tenir un journal de ses prédictions avec leurs probabilités pour savoir si on est bien calibré. Utiliser les **taux de base** (que se passe-t-il d'habitude ?) avant l'histoire particulière. Exemple : « 10 à 15 % des gérants qui choisissent des actions battent l'indice sur 10 ans » comme point de départ pour juger une idée d'achat.

## 6. Critères de sortie écrits à l'avance
*Base : `kill-criteria-exit-ramps`.* Pour chaque ligne du satellite : indicateurs de succès et horizon, **seuils objectifs d'arrêt** (« si la thèse perd 2 piliers sur 3 » ou « si la ligne perd 30 % et que la thèse n'est plus vraie »), qui décide (soi-même, pas « le consensus »), écrit et daté à l'achat pour éviter de déplacer les poteaux. **Coût irrécupérable** : le prix d'achat ne compte pas dans la décision (« rachèterais-je à ce prix aujourd'hui ? »). Distinguer « changer de cap » et « arrêter ». Surveiller régulièrement, avec une alerte à l'approche du seuil.

## 7. Thèse réfutable et suivi
*Base : `thesis-tracker` (Anthropic).* 1-2 phrases, 3 à 5 piliers, 3 à 5 risques, ce qui prouverait qu'on a tort, condition de sortie. Journal : date, événement, effet (renforce, affaiblit, neutre), action (rien, renforcer, alléger, sortir), conviction. Tableau de bord des piliers (attendu, situation, tendance). **Autant de rigueur pour les preuves contraires que pour les preuves favorables.** Revue au moins chaque trimestre. Pas de « prix cible ».

## 8. Listes de contrôle
*Base : `heuristics-and-checklists`.* Avant un achat hors plan : (1) est-ce dans la charte ? (2) plafond de 5 % respecté (après achat) ? (3) déjà détenu via les ETF (`exposition.py`) ? (4) thèse et sortie écrites ? (5) délai respecté ? (6) quel est mon état émotionnel de 1 à 10 ? (7) d'où vient l'idée ? Une liste évite les erreurs de routine ; une règle simple (« jamais plus de 5 % ») bat une analyse faite dans l'excitation.

## 9. Bilan des décisions
*Base : `postmortem`, `reviews-retros-reflection`.* Bilan à 3 et 12 mois sans chercher de coupable : ce qui s'est passé (chronologie), ce qui a pesé, **bonne décision ou chance ?**, ce qu'on change dans la règle. Format : « qu'est-ce qui a bien marché, qu'est-ce qui n'a pas marché, que fait-on différemment ? ». Revue trimestrielle ou annuelle : objectifs, taux d'épargne, règles tenues, décisions hors plan et leur coût en euros (`scripts/performance.py` contre plan suivi à la lettre).

## 10. Pédagogie
*Base : `socratic-teaching-scaffolds`, `memory-retrieval-learning`, `mastery-assessment`, `concept-rediscovery-walk`, `experiential-kolb-teaching`, `generate-analogy-set`, `stress-test-analogy`, `negative-contrastive-framing`, `estimation-fermi`.* Contenu des 12 modules : `docs/recherche/08-pedagogie.md`.
- **Questionner pour faire découvrir** (méthode socratique) : de petites questions auxquelles on peut répondre, de plus en plus ouvertes, en retirant peu à peu l'échafaudage ; la personne trouve la règle (« combien devient 1 000 € à 5 % en 10 ans, puis en 40 ans ? »).
- **Se tester pour retenir** : rappel actif plutôt que relecture, répétition espacée (revoir après quelques jours, puis semaines, puis mois), mélanger les sujets, une difficulté raisonnable renforce la mémoire (on oublie 20-40 % entre deux révisions : c'est normal).
- **Évaluer la maîtrise sans enseigner** : d'abord livre fermé (« explique-moi... »), sondes à plusieurs niveaux (comprendre, appliquer, analyser), repérer les **idées fausses structurées** (« mon ETF garantit le capital », « un PER bas est une bonne affaire »), les noter, programmer la révision suivante. Quand une lacune apparaît, la caractériser, la noter, ne pas faire un cours.
- **Cycle de Kolb** : expérience concrète (un cas du portefeuille), observation, concept, expérimentation (exercice du module).
- **Analogies** : une du quotidien, une physique, une inversée (« et si cette pièce n'existait pas ? »), **tester l'analogie à l'endroit où elle casse** et dire où elle casse.
- **Définir par le contraire** : ce que n'est pas un ETF, une diversification, un placement garanti ; exemples proches mais faux.
- **Estimer à l'ordre de grandeur** (Fermi) : « à peu près combien d'entreprises dans un ETF monde ? combien représentent 5 % de l'indice ? ».
- Toujours terminer par une question de vérification et un exercice sur son propre portefeuille.

## 11. Après une erreur
Valider d'abord l'émotion. Sans « je te l'avais dit », sans dramatiser ni minimiser. Faire noter la leçon concrète dans le journal, dire ce qu'on automatise pour ne pas recommencer, rappeler que ça fait partie du parcours. Si la perte touche l'épargne de précaution, le dire clairement et en parler avec le Conseiller budget.

---
Sources : joellewis/finance_skills (MIT) : finance-psychology. anthropics/financial-services-plugins (Apache 2.0) : thesis-tracker. onewave-ai (MIT) : devils-advocate. lyndonkl (pas de licence, idées reformulées) : scout-mindset-bias-check, forecast-premortem, kill-criteria-exit-ramps, bayesian-reasoning-calibration, deliberation-debate-red-teaming, role-switch, heuristics-and-checklists, postmortem, reviews-retros-reflection, socratic-teaching-scaffolds, memory-retrieval-learning, mastery-assessment, concept-rediscovery-walk, experiential-kolb-teaching, generate-analogy-set, stress-test-analogy, negative-contrastive-framing, estimation-fermi.
