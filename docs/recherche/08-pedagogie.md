# Recherche 08 : parcours pédagogique en 12 modules

- Origine : **rédigé par Claude à partir de ses propres connaissances**, sans recherche externe (l'autre IA n'a pas traité ce sujet). Date : 30/10/2026.
- Statut : brouillon à relire. Les exemples chiffrés simples ont été recalculés avec `scripts/projection.py` ou par calcul direct. Les chiffres de marché cités viennent des recherches 03 et 04 (non vérifiées) ou de mémoire : ils sont signalés par « À VÉRIFIER ».
- Les lectures sont des titres et des sites connus, sans lien précis, pour ne pas inventer d'adresse. Les fiscalités citées dépendent de la question 31,4 % contre 30 % (recherche 01) : tant qu'elle n'est pas tranchée, elles sont données en renvoi à la fiche C.
- Chaque module respecte le plan : objectifs, 3 niveaux, 2 exemples chiffrés, 3 erreurs courantes, 5 questions de quiz, 3 lectures, 1 exercice sur son propre portefeuille.

---

## Module 1. Bases et intérêts composés

**Objectifs :** comprendre les intérêts composés ; distinguer rendement nominal et réel ; utiliser la règle des 72 ; mesurer l'effet des frais et du temps ; savoir pourquoi commencer tôt compte.

- **En 30 secondes :** un euro placé rapporte des intérêts, qui rapportent eux-mêmes des intérêts. Plus c'est long, plus la courbe s'accélère. L'inflation grignote en parallèle ce que l'argent permet d'acheter.
- **En 5 minutes :** le capital final = capital × (1 + rendement)^années. La règle des 72 donne le temps de doublement : 72 divisé par le taux en pourcent. Le rendement réel = rendement nominal moins l'inflation (formule exacte : (1 + nominal) / (1 + inflation) - 1). Les frais agissent comme un rendement négatif qui se compose aussi.
- **Pour aller plus loin :** les rendements ne sont jamais réguliers : un rendement moyen de 7 % ne donne pas 7 % chaque année. L'ordre des rendements compte quand on retire de l'argent (module 5). Le temps de placement pèse plus que le rendement les 10 premières années : le taux d'épargne domine (fiche A, point 2).

**Exemples chiffrés :**
1. 10 000 € à 7 % par an : 19 672 € après 10 ans, 38 697 € après 20 ans, 76 123 € après 30 ans (hypothèse, non garantie). Règle des 72 : 72 / 7, soit environ 10,3 ans pour doubler.
2. 500 €/mois à 5 % par an : 202 902 € après 20 ans pour 120 000 € versés, 407 688 € après 30 ans pour 180 000 € versés. Les intérêts dépassent les versements après environ 20 ans.

**Erreurs courantes :** confondre rendement moyen et rendement chaque année ; oublier l'inflation (à 2 %, 100 € ne valent plus que 67 € de pouvoir d'achat actuel dans 20 ans) ; croire qu'un gain de 50 % compense une perte de 50 % (il faut +100 %).

**Quiz :**
1. 1 000 € à 5 % pendant 40 ans donnent environ combien ? *7 040 €.*
2. Combien de temps pour doubler un capital à 6 % ? *Environ 12 ans (72 / 6).*
3. Un fonds euro à 2,5 % et une inflation à 2 % : rendement réel ? *Environ 0,5 %.*
4. Une perte de 50 % demande quel gain pour revenir à l'équilibre ? *+100 %.*
5. Pourquoi les frais pèsent-ils plus qu'on ne croit ? *Ils se composent chaque année, comme un rendement négatif.*

**Lectures :** Banque de France, portail *Mes questions d'argent* (mesquestionsdargent.fr) ; Morgan Housel, *La psychologie de l'argent* ; wiki Bogleheads (bogleheads.org), page sur les intérêts composés.

**Exercice :** relève le rendement et les frais de chacune de tes lignes. Calcule, avec `scripts/projection.py`, ce que donneraient tes versements actuels à 4, 5 et 7 % sur 10 et 20 ans.

---

## Module 2. Les ETF

**Objectifs :** expliquer ce qu'est un ETF ; lire un TER ; distinguer réplication physique et synthétique ; comprendre l'écart de suivi et la liquidité ; connaître les risques.

- **En 30 secondes :** un ETF est un panier d'actions ou d'obligations qui copie un indice, coté en bourse comme une action, à frais très bas.
- **En 5 minutes :** le TER est le frais annuel affiché. L'écart de suivi (tracking difference) est la différence réelle entre la performance du fonds et celle de l'indice : c'est le vrai coût. Réplication physique : le fonds détient les titres. Synthétique : un contrat d'échange (swap) avec une banque reproduit l'indice, ce qui rend certains ETF monde éligibles au PEA (fiche C, recherche 02). Capitalisant : dividendes réinvestis. Distribuant : dividendes versés.
- **Pour aller plus loin :** critères de choix (fiche D, point 27) : frais, encours, réplication, éligibilité, écart de suivi, jamais la performance passée. Risques : de marché (l'ETF baisse avec l'indice), de contrepartie (swap), de change, de liquidité (écart achat-vente).

**Exemples chiffrés :**
1. 100 000 € investis 20 ans à 6 % brut : avec 0,2 % de frais, environ 308 826 € ; avec 1,5 % de frais, environ 241 171 €. Écart : environ 67 600 € dus aux seuls frais.
2. Un ETF à 0,20 % de TER sur 50 000 € coûte 100 € par an ; un fonds actif à 2 % coûte 1 000 € par an.

**Erreurs courantes :** choisir un ETF sur sa performance passée ; en cumuler plusieurs sur le même indice ; ignorer la devise et la domiciliation.

**Quiz :**
1. Que mesure le TER ? *Les frais de gestion annuels affichés.*
2. Que mesure l'écart de suivi ? *L'écart réel de performance avec l'indice, frais compris.*
3. Qu'est-ce qu'un ETF capitalisant ? *Il réinvestit les dividendes dans le fonds.*
4. Quel risque spécifique pour un ETF synthétique ? *Celui de la banque qui fournit le swap.*
5. Pourquoi viser un encours de plus de 100 M€ ? *Pour limiter le risque de fermeture du fonds.*

**Lectures :** justETF (justetf.com), comparateur et fiches ETF ; John Bogle, *Un petit livre pour investir avec bon sens* ; le DIC (KID) de ton propre ETF, sur le site de l'émetteur.

**Exercice :** ouvre le DIC de chacun de tes ETF. Note le TER, la réplication, l'indice, le caractère capitalisant ou distribuant. Repère un éventuel doublon (fiche D, point 25).

---

## Module 3. Enveloppes et fiscalité en France

**Objectifs :** distinguer PEA, assurance vie, CTO, PER ; connaître l'ordre de remplissage ; comprendre la règle des 5 ans et des 8 ans ; simuler l'impôt d'une vente.

- **En 30 secondes :** l'enveloppe est le « contenant » fiscal. Les mêmes ETF sont taxés différemment selon qu'ils sont dans un PEA, une assurance vie ou un CTO.
- **En 5 minutes :** ordre habituel (fiche C, point 14) : épargne de précaution, PEA, assurance vie, CTO, PER si la tranche d'imposition est élevée. PEA : exonération d'impôt sur le revenu après 5 ans, plafond de versements de 150 000 €. Assurance vie : abattement annuel après 8 ans, avantage successoral. CTO : aucun avantage, flat tax. PER : déduction à l'entrée, imposition à la sortie.
- **Pour aller plus loin :** l'impôt ne porte que sur la part de gain contenue dans le retrait. Les taux (PFU, prélèvements sociaux) ont changé ou vont changer : se reporter à la recherche 01 et à la fiche C, à vérifier avant chaque simulation.

**Exemples chiffrés :**
1. Retrait de 8 000 € sur un PEA de plus de 5 ans valant 24 000 € dont 9 000 € de gains : la part de gain est 37,5 %, soit 3 000 € de gain dans le retrait, sur lesquels s'appliquent seulement les prélèvements sociaux. (Taux à vérifier.)
2. Vente sur CTO : plus-value de 3 000 € ; avec un PFU de 31,4 % (recherche 01), impôt de 942 € ; avec 30 %, 900 €. L'écart de taux change l'impôt de 42 € sur cette vente.

**Erreurs courantes :** retirer de l'argent du PEA dans les 5 premières années (clôture du plan) ; oublier de déclarer un compte-titres étranger (formulaire 3916) ; imposer mentalement l'encours entier au lieu des gains.

**Quiz :**
1. Que se passe-t-il si on retire de l'argent d'un PEA avant 5 ans ? *Le plan est clôturé, avec exceptions légales.*
2. Quel est le plafond de versements du PEA ? *150 000 € (hors PEA-PME).*
3. À partir de quand l'abattement annuel de l'assurance vie s'applique-t-il ? *Après 8 ans.*
4. Qu'est-ce qui est taxé lors d'un retrait ? *La part de gain, pas le capital versé.*
5. Quel formulaire déclare un compte-titres à l'étranger ? *Le 3916.*

**Lectures :** service-public.fr, fiches PEA, assurance vie, PER ; impots.gouv.fr, rubrique valeurs mobilières ; AMF, rubrique Épargnants.

**Exercice :** liste tes enveloppes, leur date d'ouverture et leur montant. Pour chaque ligne, note si l'enveloppe est la plus adaptée selon la fiche C, point 14. Demande au Stratège une simulation d'impôt pour une vente de ton choix.

---

## Module 4. Allocation et diversification

**Objectifs :** définir l'allocation d'actifs ; comprendre la corrélation ; utiliser le cœur-satellite ; rééquilibrer ; voir la concentration cachée.

- **En 30 secondes :** répartir son argent entre classes d'actifs qui ne bougent pas toutes pareil (actions, obligations, or...) réduit les mauvaises surprises.
- **En 5 minutes :** l'allocation entre actions et obligations explique l'essentiel du risque d'un portefeuille. Cœur-satellite : 80-90 % en cœur passif (indice monde), 10-20 % en convictions (fiche D, point 21). Rééquilibrer ramène l'allocation à la cible, de préférence avec les nouveaux versements (fiche E, point 31).
- **Pour aller plus loin :** « diversifier » n'est pas « multiplier les lignes ». Un ETF monde et un ETF S&P 500 se recoupent (poids des États-Unis dans l'indice monde proche de 70 %, À VÉRIFIER, recherches 02 et 06). La corrélation entre actions et obligations n'est pas stable : elle est devenue positive en 2022 (recherche 03).

**Exemples chiffrés :**
1. Portefeuille 60 % actions, 40 % obligations. Si les actions gagnent 20 % et les obligations 0 %, le portefeuille passe à 64,3 % d'actions et 35,7 % d'obligations. Pour revenir à 60/40, il faut orienter les versements vers les obligations.
2. 100 € répartis sur MSCI World, S&P 500 et Nasdaq 100 : une large part des trois suit les mêmes grandes valeurs américaines. Le gain de diversification est faible.

**Erreurs courantes :** empiler des ETF qui se recoupent ; confondre diversification et complexité ; changer d'allocation à chaque actualité.

**Quiz :**
1. Que signifie « cœur-satellite » ? *Un noyau passif et une petite part de convictions.*
2. Comment rééquilibrer sans vendre ? *Avec les nouveaux versements.*
3. Pourquoi un ETF monde et un S&P 500 se recoupent-ils ? *Le S&P 500 pèse très lourd dans l'indice monde.*
4. Qu'est-ce que la corrélation ? *Le degré auquel deux actifs bougent ensemble.*
5. Combien de lignes suffisent souvent ? *1 à 5 ETF (fiche D, point 28).*

**Lectures :** Burton Malkiel, *A Random Walk Down Wall Street* ; factsheets MSCI et S&P (msci.com, spglobal.com) ; Vanguard Research, notes sur le rééquilibrage.

**Exercice :** passe tes lignes à l'Analyste pour estimer le poids réel des États-Unis et des 10 premières entreprises. Compare à ta cible.

---

## Module 5. Risque et volatilité

**Objectifs :** mesurer la volatilité ; comprendre le drawdown ; connaître le risque de séquence ; relier horizon et risque ; définir sa capacité à supporter une baisse.

- **En 30 secondes :** le risque en bourse, c'est la possibilité de voir son portefeuille baisser, parfois beaucoup, parfois longtemps.
- **En 5 minutes :** la volatilité est l'écart-type des rendements annuels (environ 15 % pour les actions mondiales selon la recherche 04, À VÉRIFIER). Le drawdown est la baisse maximale depuis un sommet. Le risque de séquence : un krach au moment des retraits pèse plus qu'un krach pendant la phase de versements.
- **Pour aller plus loin :** capacité (financière) et tolérance (psychologique) sont deux choses différentes. La dimension la plus prudente doit guider l'allocation (recherche 06). Le bon niveau de risque est celui qu'on tient dans la tempête (fiche D, point 23).

**Exemples chiffrés :**
1. Volatilité de 15 % : une année « normale » peut se situer entre -15 % et +15 % autour de la moyenne. Sur 10 000 €, cela représente entre 8 500 € et 11 500 € environ (ordre de grandeur, non garanti).
2. Baisse de 56,8 % (S&P 500, 2007-2009, recherche 03) : 10 000 € deviennent 4 320 €. Il faut +131,5 % pour revenir à 10 000 €.

**Erreurs courantes :** juger le risque par sa tolérance en période haussière ; regarder son portefeuille tous les jours ; oublier que l'argent nécessaire dans moins de 3 ans n'a pas sa place en actions (fiche B, point 10).

**Quiz :**
1. Qu'est-ce que le drawdown ? *La baisse maximale depuis un sommet.*
2. Qu'est-ce que la volatilité ? *L'ampleur des variations de rendement.*
3. Pourquoi le risque de séquence est-il plus grave à la retraite ? *On vend pendant la baisse, donc on fige les pertes.*
4. Après -50 %, combien faut-il pour revenir ? *+100 %.*
5. Pourquoi ne pas mettre en actions l'argent dont on a besoin dans 2 ans ? *Une baisse peut durer plus longtemps que l'horizon.*

**Lectures :** recherche 03 du dépôt (baisses majeures) ; AMF, page sur le risque et le rendement ; Howard Marks, notes d'investissement (oaktreecapital.com).

**Exercice :** note la plus forte baisse de ton portefeuille depuis que tu investis. Demande-toi ce que tu aurais fait à -30 %, puis compare à ta réponse initiale (accueil).

---

## Module 6. Psychologie de l'investisseur

**Objectifs :** reconnaître les principaux biais ; comprendre l'écart de comportement ; écrire une règle de décision ; utiliser le journal et le pré-mortem.

- **En 30 secondes :** le principal ennemi de l'investisseur, c'est souvent lui-même : peur, euphorie, envie de bouger.
- **En 5 minutes :** biais courants (fiche F, point 37) : aversion aux pertes, ancrage, excès de confiance, biais de récence, effet de disposition, biais de confirmation, FOMO. Les outils : plan écrit, règle des 24 à 72 h, journal de décision, pré-mortem, versements automatiques (recherche 07).
- **Pour aller plus loin :** l'écart de comportement mesuré par Morningstar serait de l'ordre de 1 point par an pour les fonds américains (recherche 07, À VÉRIFIER). Les études sur le sur-trading (Barber et Odean) montrent que les plus actifs gagnent moins.

**Exemples chiffrés :**
1. Écart de comportement de 1,1 point par an sur 20 ans pour un capital de 100 000 € à 6 % : 100 000 × 1,06^20 = 320 714 € contre 100 000 × 1,049^20 = 260 321 € environ. L'écart représente plus de 60 000 €.
2. Frais de courtage de 1,95 € sur un ordre de 100 € : 1,95 % de frais. Multiplier les petits ordres coûte vite cher.

**Erreurs courantes :** penser que connaître les biais protège d'eux ; rédiger sa charte pendant une tempête ; juger une décision au résultat plutôt qu'au processus.

**Quiz :**
1. Qu'est-ce que le FOMO ? *La peur de manquer une opportunité qui monte.*
2. À quoi sert le pré-mortem ? *Imaginer l'échec à l'avance pour en repérer les causes.*
3. Que note-t-on dans un journal de décision ? *Date, décision, raison, source de l'idée, émotion, bilan.*
4. Qu'est-ce que l'effet de disposition ? *Vendre trop tôt les gagnants et garder trop longtemps les perdants.*
5. Pourquoi automatiser les versements ? *Pour supprimer la décision émotionnelle du mois.*

**Lectures :** Daniel Kahneman, *Thinking, Fast and Slow* (*Système 1, Système 2* en français) ; Morgan Housel, *La psychologie de l'argent* ; Barber et Odean, *Trading Is Hazardous to Your Wealth* (SSRN).

**Exercice :** ouvre `prive/<prénom>/journal.md` et note ta dernière décision hors plan : raison, émotion, résultat. Repère le biais principal.

---

## Module 7. Lire une actualité financière

**Objectifs :** distinguer faits et opinions ; identifier la source ; évaluer l'impact sur un portefeuille ETF monde ; classer « ignorer, surveiller, agir ».

- **En 30 secondes :** une actualité est utile si elle change ton plan. Sinon, c'est du bruit.
- **En 5 minutes :** un fait est vérifiable (« l'inflation est de X % »), une opinion est une interprétation (« le marché va chuter »). Pour chaque information : qui parle, quelle source primaire, quelle date, quel impact sur mes lignes, à quel horizon (recherche 09).
- **Pour aller plus loin :** la plupart des événements sont déjà intégrés dans les prix quand on les lit. Pour un ETF monde, la diversification dilue l'effet d'une nouvelle isolée.

**Exemples chiffrés :**
1. Une entreprise qui pèse 5 % de ton ETF monde perd 20 % en un jour : l'impact sur l'ETF est d'environ -1 % (5 % × -20 %), toutes choses égales par ailleurs.
2. Titre : « Les marchés s'effondrent de 3 % ». Sur un portefeuille de 50 000 €, c'est environ -1 500 € en une séance, soit moins que l'écart habituel d'une année (voir module 5).

**Erreurs courantes :** réagir au titre sans lire l'article ; suivre les sources qui promettent ; confondre publicité et analyse.

**Quiz :**
1. Fait ou opinion : « le CAC 40 a clôturé en baisse de 1 % » ? *Un fait.*
2. Fait ou opinion : « la bourse va corriger cet automne » ? *Une opinion.*
3. Où trouver la composition exacte d'un ETF ? *Sur le site de l'émetteur, dans la factsheet.*
4. Quel est le premier réflexe face à une grosse baisse ? *Relire son plan et son horizon.*
5. Combien de sources suffisent pour un brief quotidien ? *Quelques sources fiables, pas davantage.*

**Lectures :** Reuters ; Les Echos ; BCE (ecb.europa.eu) pour les décisions de taux et INSEE (insee.fr) pour l'inflation.

**Exercice :** prends une actualité de la semaine. Classe-la en « ignorer, surveiller, agir » et justifie par écrit en trois lignes.

---

## Module 8. Lire le bilan d'une entreprise

**Objectifs :** distinguer compte de résultat, bilan et flux de trésorerie ; lire quelques ratios (marge, dette nette, retour sur capitaux) ; repérer les signaux d'alerte.

- **En 30 secondes :** le compte de résultat dit si l'entreprise gagne de l'argent, le bilan ce qu'elle possède et doit, les flux de trésorerie d'où vient l'argent réellement.
- **En 5 minutes :** chiffre d'affaires, résultat net, marge nette (résultat net / chiffre d'affaires). Dette nette = dettes moins trésorerie. Flux de trésorerie disponible = trésorerie générée après investissements. Un bénéfice sans trésorerie est suspect.
- **Pour aller plus loin :** comparer des ratios au sein d'un même secteur ; regarder l'évolution sur 5 ans, pas une année ; vérifier les notes aux comptes. Pour un satellite d'actions en direct, l'idée doit s'écrire en une page avec ce qui l'invaliderait (fiche E, point 33).

**Exemples chiffrés :**
1. Chiffre d'affaires de 1 000 M€, résultat net de 80 M€ : marge nette de 8 %.
2. Dette de 600 M€, trésorerie de 200 M€, résultat d'exploitation avant amortissements de 200 M€ : dette nette de 400 M€, soit 2 fois le résultat. Au-delà de 3 à 4 fois, la prudence s'impose (ordre de grandeur courant, varie selon le secteur).

**Erreurs courantes :** juger sur une seule année ; ignorer la dette ; confondre bénéfice comptable et trésorerie.

**Quiz :**
1. Quel document montre ce que l'entreprise possède et doit ? *Le bilan.*
2. Comment calcule-t-on la marge nette ? *Résultat net divisé par chiffre d'affaires.*
3. Qu'est-ce que la dette nette ? *Dettes moins trésorerie.*
4. Pourquoi regarder les flux de trésorerie ? *Ils montrent l'argent réellement généré.*
5. Pourquoi comparer à un même secteur ? *Les ratios normaux varient d'un secteur à l'autre.*

**Lectures :** rapports annuels (documents d'enregistrement universel) sur les sites des sociétés ; AMF, rubrique sur l'information financière des sociétés ; Aswath Damodaran (pages.stern.nyu.edu/~adamodar), cours gratuits et données.

**Exercice :** si tu as une action en direct, retrouve son dernier rapport annuel. Note chiffre d'affaires, résultat net, dette nette. Écris ce qui invaliderait ton idée.

---

## Module 9. Valorisation

**Objectifs :** calculer un PER et un rendement du bénéfice ; comprendre l'actualisation ; connaître les limites de la valorisation ; ne pas confondre bonne entreprise et bon prix.

- **En 30 secondes :** une bonne entreprise peut être un mauvais investissement si on la paie trop cher.
- **En 5 minutes :** PER = cours / bénéfice par action. Le rendement du bénéfice est l'inverse (1 / PER). Actualiser : un euro dans le futur vaut moins qu'un euro aujourd'hui, car on aurait pu le placer.
- **Pour aller plus loin :** les valorisations élevées sont corrélées à des rendements futurs plus faibles sur 10 ans, mais ne permettent pas de prévoir le moment du retournement (fiche E, point 30). Pour un ETF monde, la valorisation d'ensemble est un contexte, pas un signal d'action.

**Exemples chiffrés :**
1. Action à 100 €, bénéfice par action de 5 € : PER de 20, rendement du bénéfice de 5 %.
2. Valeur actuelle de 1 000 € reçus dans 10 ans avec un taux d'actualisation de 5 % : 1 000 / 1,05^10 = 614 € environ.

**Erreurs courantes :** utiliser le PER seul ; comparer des PER de secteurs différents ; croire qu'un PER bas signifie « bon marché ».

**Quiz :**
1. Que mesure le PER ? *Le nombre d'années de bénéfices contenues dans le prix.*
2. Que vaut l'inverse du PER ? *Le rendement du bénéfice.*
3. Qu'est-ce que l'actualisation ? *Ramener une somme future à sa valeur d'aujourd'hui.*
4. Un PER bas garantit-il une bonne affaire ? *Non, l'entreprise peut être en difficulté.*
5. Peut-on prévoir un krach avec le PER ? *Non, il indique un contexte, pas un moment.*

**Lectures :** Benjamin Graham, *L'investisseur intelligent* ; Aswath Damodaran, pages de valorisation ; recherche 03 du dépôt, section sur le coût du market timing.

**Exercice :** calcule le PER et le rendement du bénéfice d'une entreprise de ton portefeuille. Compare au secteur.

---

## Module 10. Macro et taux

**Objectifs :** comprendre inflation, taux directeurs, courbe des taux ; relier taux, obligations et actions ; situer les cycles.

- **En 30 secondes :** quand les taux montent, les obligations existantes perdent de la valeur et les actions sont souvent revues à la baisse.
- **En 5 minutes :** la banque centrale (BCE) fixe les taux directeurs pour viser une inflation autour de 2 %. La courbe des taux compare les taux courts et longs. Le prix d'une obligation baisse quand les taux montent, d'autant plus que sa duration est longue.
- **Pour aller plus loin :** en 2022, actions et obligations ont baissé ensemble (recherche 03). Les cycles économiques ne se prévoient pas ; on s'y prépare avec une allocation tenable.

**Exemples chiffrés :**
1. Duration de 7 ans, taux en hausse de 1 point : le prix de l'obligation baisse d'environ 7 %.
2. Inflation de 3,4 % (chiffre cité en recherche 10, À VÉRIFIER) et Livret A à 1,70 % : rendement réel d'environ -1,6 %.

**Erreurs courantes :** croire que les obligations sont sans risque ; anticiper les décisions de la banque centrale ; regarder l'inflation sans regarder son rendement réel.

**Quiz :**
1. Que fixe la banque centrale ? *Les taux directeurs.*
2. Que fait le prix d'une obligation quand les taux montent ? *Il baisse.*
3. Qu'est-ce que la duration ? *La sensibilité du prix d'une obligation aux taux.*
4. Quelle est la cible d'inflation de la BCE ? *Environ 2 %.*
5. Pourquoi le rendement réel compte-t-il ? *Il mesure ce que l'on peut vraiment acheter.*

**Lectures :** BCE (ecb.europa.eu), pages pédagogiques sur la politique monétaire ; INSEE (insee.fr), indice des prix ; Banque de France, *Mes questions d'argent*.

**Exercice :** note les taux actuels de ton fonds euro et de ton Livret A. Calcule le rendement réel avec l'inflation du moment (à vérifier sur l'INSEE).

---

## Module 11. Crypto-actifs

**Objectifs :** comprendre ce que sont les crypto-actifs ; mesurer leur risque ; connaître la fiscalité de base ; sécuriser son accès.

- **En 30 secondes :** les crypto-actifs sont des actifs numériques très volatils, sans flux de revenus propre.
- **En 5 minutes :** le bitcoin a perdu plus de 75 % de sa valeur à plusieurs reprises (-84 % en 2018, -77 % en 2022, recherche 06, À VÉRIFIER). Part prudente : 5 à 10 % au plus, en acceptant de tout perdre (fiche D, point 24). Jamais à crédit.
- **Pour aller plus loin :** fiscalité des cessions (recherche 01, point 8) : l'impôt se déclenche à la conversion en euros, pas à l'échange entre crypto-actifs. Risque de plateforme : vérifier l'enregistrement PSAN ou l'agrément MiCA (recherche 11).

**Exemples chiffrés :**
1. 5 % d'un portefeuille de 100 000 €, soit 5 000 €, qui perdent 80 % : perte de 4 000 €, soit 4 % du portefeuille total.
2. Même portefeuille avec 30 % en crypto (30 000 €) : une baisse de 80 % coûte 24 000 €, soit 24 % du portefeuille.

**Erreurs courantes :** acheter par peur de manquer (FOMO) ; laisser ses actifs sur une plateforme non vérifiée ; oublier de déclarer les comptes étrangers (3916-bis).

**Quiz :**
1. Quand l'impôt sur les crypto-actifs se déclenche-t-il ? *À la cession contre euros ou à l'achat d'un bien.*
2. Peut-on emprunter pour investir en crypto ? *Ce n'est pas recommandé (fiche D, point 24).*
3. Quel est le risque d'une plateforme non régulée ? *Sa faillite ou une fraude.*
4. Quelle baisse a connu le bitcoin en 2022 ? *Environ 77 %.*
5. Quel formulaire déclare un compte crypto étranger ? *Le 3916-bis.*

**Lectures :** AMF, rubrique crypto-actifs ; recherche 11 du dépôt ; impots.gouv.fr, fiscalité des actifs numériques.

**Exercice :** calcule la part de crypto dans ton portefeuille total. Compare à ta règle personnelle (profil, 10 % maximum).

---

## Module 12. Construire sa charte d'investissement

**Objectifs :** écrire une charte d'une page ; relier objectifs, allocation et règles ; prévoir les comportements en cas de crise ; planifier la revue annuelle.

- **En 30 secondes :** la charte est le contrat que tu passes avec toi-même, écrit à froid, pour tenir quand ça secoue.
- **En 5 minutes :** contenu minimal : 1) objectifs nommés, datés, chiffrés ; 2) allocation cible ; 3) règles d'achat (versement mensuel, jour fixe) ; 4) règles de vente (quand, pourquoi) ; 5) limites (une ligne hors ETF large : 5 %, crypto : 10 %) ; 6) conduite en cas de baisse de 20, 30, 40 % ; 7) rythme de revue.
- **Pour aller plus loin :** relire la charte une fois par an, jamais en pleine crise. Toute décision hors charte passe par le Coach, avec 24 à 72 h d'attente (fiche F, point 36).

**Exemple de charte rempli (fictif) :**

> **Objectif :** 300 000 € dans 15 ans (hypothèse 5 %, non garantie). **Allocation :** 80 % ETF monde, 10 % ETF émergents, 10 % obligations. **Versement :** 1 000 € le 5 de chaque mois, quoi qu'il arrive. **Achat hors plan :** 24 à 72 h et passage par le Coach. **Vente :** uniquement pour un besoin d'argent prévu ou un changement d'objectif, jamais sur une actualité. **Limites :** une action en direct, 5 % maximum ; crypto, 5 % maximum. **En cas de baisse de 30 % :** je relis cette charte, je ne vends rien, je continue de verser. **Revue :** chaque année en janvier.

**Exemples chiffrés :**
1. Avec 1 000 €/mois à 5 % pendant 15 ans : environ 264 825 € (`scripts/projection.py 0 1000 5 15 300000`). Pour atteindre 300 000 €, il faudrait 16 ans et 5 mois, ou un peu plus de versements.
2. Une règle « 5 % maximum par ligne » sur un portefeuille de 100 000 € limite le pari à 5 000 €.

**Erreurs courantes :** charte trop longue et illisible ; règles de vente absentes ; écrire la charte en période de stress.

**Quiz :**
1. Que doit contenir une charte ? *Objectifs, allocation, règles d'achat et de vente, limites, revue.*
2. Quand l'écrire ? *À froid, hors période de stress.*
3. Que faire en cas de baisse de 30 % si la charte est respectée ? *Rien changer et continuer les versements.*
4. À quelle fréquence la réviser ? *Une fois par an.*
5. Qui valide une décision hors charte ? *Soi-même, après 24 à 72 h et passage par le Coach.*

**Lectures :** recherche 07 du dépôt (outils anti-émotion) ; modèle de charte (fiche B, point 13) ; Bogleheads (bogleheads.org), page sur l'*Investment Policy Statement*.

**Exercice :** écris ta charte en une page avec le Stratège. Elle sera enregistrée dans `prive/<prénom>/charte.md`.

---

## Glossaire : 100 termes essentiels

**A.** *Action* : part du capital d'une entreprise. *Actualisation* : conversion d'une somme future en valeur d'aujourd'hui. *Allocation d'actifs* : répartition entre classes d'actifs. *AMF* : Autorité des marchés financiers, régulateur. *Assurance vie* : enveloppe d'épargne et de transmission. *Aversion aux pertes* : une perte pèse plus qu'un gain équivalent.
**B.** *Bear market* : marché baissier, baisse de plus de 20 %. *Biais* : raccourci mental qui fausse la décision. *Bilan* : état de ce que l'entreprise possède et doit. *Bid-ask (écart)* : différence entre prix d'achat et de vente. *Bull market* : marché haussier.
**C.** *Capitalisation boursière* : cours × nombre d'actions. *Capitalisant* : réinvestit les dividendes. *Cœur-satellite* : noyau passif et petite part de convictions. *Corrélation* : degré de mouvement commun entre deux actifs. *Cours* : prix d'un titre. *CTO* : compte-titres ordinaire. *Courtier* : intermédiaire qui passe les ordres.
**D.** *DCA* : investir une somme fixe à intervalle régulier. *Dette nette* : dettes moins trésorerie. *Diversification* : répartir pour réduire les risques propres à un titre. *Dividende* : part du bénéfice versée aux actionnaires. *DIC / KID* : document d'informations clés. *Distribuant* : verse les dividendes. *Drawdown* : baisse depuis un sommet. *Duration* : sensibilité d'une obligation aux taux.
**E.** *Effet de disposition* : vendre trop tôt les gagnants. *Encours* : total des actifs d'un fonds. *EONIA / €STR* : taux au jour le jour de la zone euro. *Épargne de précaution* : réserve pour imprévus. *ETF* : fonds indiciel coté. *Euro Stoxx 50* : indice de 50 grandes valeurs de la zone euro.
**F.** *Flat tax* : prélèvement forfaitaire unique. *Fonds euro* : support à capital garanti de l'assurance vie. *FOMO* : peur de rater une hausse. *Frais de gestion* : coût annuel d'un fonds. *FGDR* : fonds de garantie des dépôts et de résolution.
**G.** *Glide path* : baisse programmée de la part d'actions avec l'âge. *GAFAM* : géants américains de la technologie.
**H.** *Hedging* : couverture contre un risque (change, par exemple). *Horizon de placement* : durée prévue avant d'avoir besoin de l'argent.
**I.** *Indice* : panier de titres qui mesure un marché. *Inflation* : hausse générale des prix. *Intérêts composés* : intérêts qui produisent à leur tour des intérêts. *ISIN* : code international d'identification d'un titre.
**L.** *Levier* : emprunt pour investir plus. *Liquidité* : facilité à vendre sans perdre sur le prix. *Livret A* : livret réglementé défiscalisé. *Lump sum* : investissement d'une somme en une fois.
**M.** *Marge nette* : résultat net divisé par chiffre d'affaires. *Market timing* : tenter d'anticiper les hausses et baisses. *MSCI World* : indice des grandes valeurs des pays développés. *Moins-value* : perte réalisée à la vente.
**N.** *Nasdaq 100* : indice des 100 plus grandes valeurs non financières du Nasdaq. *Nominal* : avant inflation.
**O.** *Obligation* : prêt à une entreprise ou un État, contre intérêts. *OAT* : obligation d'État française. *Option* : contrat donnant un droit d'achat ou de vente.
**P.** *PEA* : plan d'épargne en actions. *PER (ratio)* : cours sur bénéfice. *PER (plan)* : plan d'épargne retraite. *PFU* : prélèvement forfaitaire unique. *Plus-value* : gain réalisé à la vente. *Pré-mortem* : imaginer l'échec avant d'agir. *Prélèvements sociaux* : CSG, CRDS et autres.
**R.** *Rééquilibrage* : retour à l'allocation cible. *Réel* : après inflation. *Réplication* : manière dont l'ETF copie l'indice. *Rendement* : gain rapporté au capital. *Risque de change* : variation de la valeur due à la devise. *Risque de séquence* : risque lié à l'ordre des rendements.
**S.** *S&P 500* : indice des 500 grandes entreprises américaines. *Satellite* : part de convictions hors cœur. *SCPI* : société civile de placement immobilier. *Spread* : écart de prix. *Swap* : contrat d'échange de flux. *Synthétique* : réplication par swap.
**T.** *Taux directeur* : taux fixé par la banque centrale. *Taux d'épargne* : part du revenu épargnée. *TER* : frais courants annuels. *TMI* : tranche marginale d'imposition. *Tracking difference* : écart réel entre l'ETF et son indice. *Tracking error* : variabilité de cet écart.
**U.** *UCITS* : cadre européen des fonds grand public. *Unité de compte* : support d'assurance vie sans garantie en capital.
**V.** *Valeur liquidative* : prix d'une part d'un fonds. *Valorisation* : niveau de prix par rapport aux fondamentaux. *Volatilité* : ampleur des variations de rendement. *Versement programmé* : prélèvement automatique régulier.
**X-Z.** *XIRR* : taux de rendement interne avec dates de flux. *Yield* : rendement courant d'un titre. *Zone euro* : pays utilisant l'euro.

*(Environ 95 termes : à compléter lors de la relecture.)*

---

## Études de cas historiques

*Les chiffres S&P 500 viennent de `baisses-majeures.csv` (recherche 03, non vérifiée). Les autres sont de mémoire, à vérifier.*

### 1. Bulle internet (2000-2002)
- **Chronologie :** sommet du S&P 500 en mars 2000, creux en octobre 2002 (-49,1 %), retour au sommet en 2007 d'après le fichier de la recherche 03 (selon la méthode, jusqu'en 2013). Le Nasdaq a perdu environ 78 % et n'a retrouvé son sommet qu'en 2015 (À VÉRIFIER).
- **Investisseur patient :** continue de verser. Il achète à des prix bas pendant trois ans.
- **Investisseur paniqué :** vend en 2002, fige la perte, manque le rebond de 2003 (+28,68 %, recherche 03).
- **Leçon :** la concentration sur un thème à la mode est le vrai risque. Un indice monde diversifié a été moins touché.

### 2. Crise de 2008
- **Chronologie :** sommet en octobre 2007, creux en mars 2009 (-56,8 %), retour au sommet en mars 2013 (recherche 03).
- **Patient :** 10 000 € deviennent 4 320 € au creux ; il lui faut +131,5 % pour revenir au départ. En continuant de verser, il rachète à bas prix.
- **Paniqué :** vend en mars 2009. Le S&P 500 gagne +26,46 % en 2009 (recherche 03).
- **Leçon :** une baisse de plus de 50 % arrive. La question n'est pas « si » mais « le supporterai-je ? ».

### 3. Covid (2020)
- **Chronologie :** baisse de 33,9 % en environ un mois (février à mars 2020), retour au sommet en août 2020 (recherche 03).
- **Patient :** ne fait rien, ou continue de verser.
- **Paniqué :** vend à la fin mars, manque un rebond d'environ cinq mois.
- **Leçon :** les baisses les plus rapides se corrigent parfois vite, mais on ne peut pas le savoir à l'avance.

### 4. Hausse des taux (2022)
- **Chronologie :** sommet de janvier 2022, creux d'octobre 2022 (-25,4 % pour le S&P 500), retour au sommet en janvier 2024 (recherche 03). Les obligations ont aussi baissé : un portefeuille 60/40 n'a pas été protégé.
- **Patient :** conserve son allocation et ses versements.
- **Paniqué :** passe en liquidités au pire moment, manque la remontée.
- **Leçon :** la diversification actions-obligations n'est pas une garantie ; le plan écrit et l'horizon restent la meilleure protection. Pour un investisseur en euros, la baisse en euros a été plus faible qu'en dollars (recherche 03).

---

## Grille de progression

| Niveau | Il sait | Il fait |
|---|---|---|
| **Débutant** | Expliquer intérêts composés, ETF, PEA/AV/CTO. | Épargne de précaution constituée, 1 à 3 ETF, versement automatique. |
| **Intermédiaire** | Lire un DIC, calculer le XIRR, simuler l'impôt d'une vente, repérer un chevauchement. | Charte écrite, journal de décisions, rééquilibrage par les flux, revue annuelle. |
| **Avancé** | Lire un bilan, calculer une valorisation, expliquer l'impact des taux. | Satellite documenté (une thèse par ligne), mesure du coût de ses propres décisions, comparaison systématique à un ETF monde. |

**Passage de débutant à intermédiaire :** modules 1 à 6 validés (quiz ≥ 4/5), charte rédigée, aucune décision hors plan sans journal pendant 6 mois.
**Passage à avancé :** modules 7 à 12 validés, bilan annuel complet, écart entre performance réelle et « plan suivi à la lettre » connu.

---

## 5 notions du jour (modèle de 3 lignes réutilisable)

Modèle : **Notion** (une phrase) / **Pourquoi aujourd'hui** (lien avec l'actualité ou le portefeuille) / **À retenir** (une idée actionnable ou rassurante).

1. **Tracking difference.** L'écart réel entre ton ETF et son indice. Utile quand tu compares deux ETF sur le même indice. À retenir : regarde-la avant le TER.
2. **Risque de séquence.** L'ordre des rendements compte quand on retire de l'argent. Utile si une baisse arrive et que tu penses à ta retraite. À retenir : plus l'horizon est long, moins ça te concerne.
3. **Rendement réel.** Le rendement après inflation. Utile quand on compare Livret A et inflation. À retenir : calcule (1 + nominal) / (1 + inflation) - 1.
4. **Rééquilibrage par les flux.** Orienter les nouveaux versements vers la ligne en retard. Utile quand une ligne a beaucoup monté. À retenir : pas de vente, donc pas d'impôt.
5. **Pré-mortem.** Imaginer dans un an que ton achat a échoué, et lister pourquoi. Utile quand une idée t'enthousiasme. À retenir : si la liste est longue ou floue, attends 72 h.
