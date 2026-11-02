---
titre: Guide d'utilisation
sous_titre: Assistant Bourse Investissement
version: 1.4
date: 2026-11-02
---

# 1. Bienvenue

## À quoi sert l'assistant

L'assistant t'aide à **investir mieux, gérer ton budget et progresser, sans stress**. Il a deux objectifs mesurables :

1. **Améliorer ta performance nette**, avec les leviers qui marchent vraiment : frais bas, bonne diversification, régularité, rester investi, bonnes enveloppes fiscales.
2. **Réduire ton stress** : moins de décisions impulsives, une information triée (seulement ce qui touche tes placements).

Il fonctionne dans **Claude Code**, en langage normal. **Tu n'as aucune commande à retenir** : tu parles comme à un conseiller, le Directeur comprend ce que tu veux et appelle le bon spécialiste.

## Ce qu'il ne fait pas

- Il ne prédit jamais les marchés et ne donne aucun « bon plan ».
- Il ne dit jamais « achète » ou « vends » : il éclaire, **tu décides**.
- Il ne passe aucun ordre en bourse. Tu les passes toi-même chez ton courtier.
- Il n'est pas un conseil en investissement réglementé : c'est un outil d'aide à la réflexion.

## Les 4 règles d'or

> **1. Les chiffres viennent des scripts, jamais de sa tête.** Total du portefeuille, performance, impôt, projection : tout est calculé par un programme à partir de tes fichiers.
>
> **2. Chaque recommandation s'appuie sur une fiche** de la base de connaissances (il la cite, par exemple « fiche D, point 31 »).
>
> **3. Pas de source, pas d'information.** Une actualité est toujours citée avec sa source et sa date.
>
> **4. Ce qui te concerne reste chez toi.** Tes données sont dans `prive/<ton prénom>/`, un dossier jamais envoyé sur GitHub.

## L'équipe en un coup d'œil

| Qui | Ce qu'il fait | Chapitre |
|---|---|---|
| **Le Directeur** | Comprend ta demande, appelle le bon agent, fait la synthèse | 5 |
| **Le Veilleur** | Actualités filtrées sur tes placements, brief du jour, explication d'une chute | 6 |
| **L'Analyste** | Portefeuille, versement du mois, performance, frais, chevauchements d'ETF | 7 |
| **Le Conseiller budget** | Budget, épargne de précaution, dettes, primes, arnaques, prévoyance | 8 |
| **Le Stratège** | Objectifs, enveloppes (PEA, assurance vie...), impôts, charte d'investissement | 9 |
| **Le Coach** | Décisions d'achat et de vente, émotions, journal, apprentissage | 10 |

# 2. Démarrer en 5 minutes

## Ce qu'il te faut

- **Claude Code** (l'application ou le terminal).
- Le dossier du projet sur ton ordinateur (`git clone https://github.com/magiegenie/assistant-bourse-investissement.git`).
- Facultatif mais recommandé : les serveurs de données de marché et d'actualité (chapitre 12), installés par une seule commande.

## Première séance

1. Ouvre le dossier du projet dans Claude Code.
2. Écris simplement : **« Salut, c'est Melvin »** (avec ton prénom).
3. L'assistant ne te connaît pas encore : il lance tout seul l'**accueil**, une conversation détendue d'environ 20 minutes, en 6 étapes, une ou deux questions à la fois. Le **test de profil de risque** (chapitre 3) est réparti dans ces étapes.

| Étape | Les questions |
|---|---|
| **1. Toi** | Prénom, âge, famille et personnes à charge, métier et stabilité du revenu, logement, projets de vie, protection en cas de coup dur |
| **2. Ton argent** | Revenu, dépenses essentielles, épargne de précaution, dettes et taux, ce qui est déjà investi, épargne salariale, versement mensuel possible, et « si cette somme perdait la moitié pendant deux ans, ta vie changerait ? » |
| **3. Tes objectifs** | 1 à 3 objectifs nommés, datés et chiffrés, leur horizon, ce qui serait « assez », la priorité |
| **4. Tes connaissances** | Un petit quiz de 6 questions (« je ne sais pas » est une bonne réponse), ton expérience, le temps que tu as, tes sources d'information |
| **5. Ton rapport au risque** | 10 mises en situation chiffrées en euros sur ton propre montant |
| **6. Ton rapport à l'argent et tes préférences** | Ce qu'on disait de l'argent chez toi, ton profil (Évitant, Optimiseur, Inquiet, Rêveur), tes valeurs et exclusions, le niveau d'explication que tu veux, le partage avec l'associé |

4. **Pause possible à tout moment** : l'avancement est noté, et l'assistant te propose de reprendre là où tu t'es arrêté à la séance suivante. Pressé ? Une version courte fait les étapes 1, 2, 3 et 5, et garde les autres pour plus tard.
5. À la fin, il calcule ton **profil de risque**, te l'explique en langage simple et te demande si ça te ressemble. Puis il crée ton espace privé `prive/<prénom>/` (profil, profil de risque, budget, positions, cibles), et te propose une **première radiographie** et un **test de résistance** par l'Analyste, puis l'écriture de ta charte avec le Stratège.

## Les séances suivantes

Dis qui tu es, c'est tout. L'assistant recharge ton profil, ton profil de risque, ta charte et ton journal, et te rappelle en une ligne ce qui est en attente (un accueil à terminer, un bilan de décision à 3 mois, un délai de réflexion en cours, une revue de charte à venir, un test de risque de plus d'un an).

# 3. Ton profil de risque

## Pourquoi un test

Tout le reste en dépend : la part d'actions, la charte, la façon dont le Coach te parle quand ça baisse. Une seule question du type « tu fais quoi à -30 % ? » ne suffit pas : on surestime facilement son courage, surtout quand les marchés montent. Le test mesure donc **quatre choses**, séparément.

| Dimension | La question qu'elle pose | Exemples |
|---|---|---|
| **Capacité** (tes finances) | Peux-tu encaisser une perte sans que ta vie change ? | Épargne de précaution, stabilité du revenu, dettes, horizon, personnes à charge |
| **Tolérance** (tes émotions) | Supportes-tu de voir la perte sans vendre ? | Choix entre gains sûrs et paris, baisse de 20 % puis de 35 %, ce que tu as **réellement** fait lors d'une vraie baisse |
| **Besoin de risque** | Quel rendement te faut-il vraiment pour ton objectif ? | Calculé par l'assistant à partir de ton objectif, de ton capital et de ton versement |
| **Connaissances** | Sais-tu ce que tu achètes ? | Un quiz de 6 questions et ton expérience |

Les questions de tolérance sont **chiffrées en euros sur ton propre montant** : « ton portefeuille perd 20 %, soit 4 000 € » parle plus que « -20 % ». La dernière te demande à partir de quelle perte, en euros, tu dormirais mal : c'est ta **perte maximale acceptable**.

## Comment lire ton résultat

Un profil sur 5 niveaux, avec un repère de part d'actions :

| Niveau | Profil | Part d'actions (repère) |
|---|---|---|
| 1 | Très prudent | 0 à 20 % |
| 2 | Prudent | 20 à 40 % |
| 3 | Équilibré | 40 à 60 % |
| 4 | Dynamique | 60 à 85 % |
| 5 | Offensif | 85 à 100 % |

Les règles, appliquées par un script (jamais de tête) :

- **Le plus prudent de la capacité et de la tolérance décide.** Avoir les nerfs solides ne sert à rien si tu n'as pas d'épargne de précaution, et inversement.
- **Plafonds** : l'argent dont tu as besoin dans moins de 3 ans ne va pas en actions ; ta perte maximale acceptable limite la part d'actions (dans un krach type 2008, une allocation perd environ la moitié de sa part en actions).
- **Besoin de risque faible** : si un placement prudent suffit pour ton objectif, l'assistant te propose un cran plus prudent. C'est toi qui choisis.
- **Objectif trop exigeant** pour ton profil : on revoit le montant, le délai ou le versement, pas le risque.

## Les alertes

Le test signale aussi ce qui mérite une discussion :

- pas d'épargne de précaution, ou une dette chère : à régler avant d'investir plus (Conseiller budget) ;
- un écart important entre ce que tes finances permettent et ce que tes émotions supportent ;
- tu as vendu lors d'une vraie baisse, mais tu déclares que tu tiendrais : **le réel compte plus que le déclaré** ;
- une tolérance élevée jamais testée en vrai : commencer un cran en dessous ;
- un test passé quand les marchés sont au plus haut : à refaire après une baisse ;
- des connaissances encore fragiles, ou des réponses fausses données avec assurance (excès de confiance). Le quiz est corrigé, sans jugement.

## Ce que ça change ensuite

- Le **Stratège** garde ton allocation dans la fourchette de ton profil et pré-remplit ta charte.
- L'**Analyste** compare le pire scénario du test de résistance à ta perte maximale acceptable, et te prévient si elle est dépassée.
- Le **Coach** te rappelle ta perte maximale acceptable quand tu as peur ou que tu t'emballes, et choisit par où commencer ton apprentissage d'après le quiz.

## Quand le refaire

Une fois par an, après un événement de vie (naissance, perte d'emploi, héritage, achat immobilier), et **après une grosse baisse** : on compare alors ce que tu as vraiment fait à ce que tu avais déclaré. Dis simplement « refais mon test de risque » ou « quel est mon profil ? ». Chaque résultat est gardé dans l'historique de `profil-risque.md`.

## Te comparer à un test externe (facultatif)

L'AMF propose un autodiagnostic pédagogique gratuit, en français : « Vous souhaitez mieux vous connaître en tant qu'épargnant ? », sur amf-france.org, rubrique Espace épargnants, Conseils pratiques. Si son résultat diffère beaucoup du nôtre, parles-en à l'assistant. Pour les curieux, la référence académique la plus connue est l'échelle de Grable et Lytton (1999, 13 questions, en anglais).

> **Limites** : ce test est un outil d'aide à la réflexion, rédigé par nous à partir de travaux reconnus, **non validé scientifiquement**. Ce n'est pas le profil réglementaire qu'une banque ou un conseiller doit établir avant de te conseiller (questionnaire MIF 2).

## À deux sur le même ordinateur

Chaque personne a son dossier. L'assistant ne mélange jamais les données de deux personnes et ne parle jamais du portefeuille de l'un à l'autre, sauf si les deux l'ont autorisé dans leur profil (champ « Partage avec l'associé »).

# 4. Comment lui parler

## Parle normalement

Pas de syntaxe, pas de commande. Voici comment l'assistant interprète ce que tu dis.

| Si tu dis quelque chose comme... | Qui répond |
|---|---|
| « Je viens d'être payé », « mes dépenses dérapent », « j'ai une prime », « combien garder de côté ? », « c'est une arnaque ? », « j'ai un crédit » | Conseiller budget |
| « Mes objectifs », « PEA ou assurance vie ? », « combien d'impôt si je vends ? », « serai-je libre à 40 ans ? », « écrivons ma charte » | Stratège |
| « Où j'en suis ? », « je mets combien où ce mois-ci ? », « ma performance », « mes frais », « mes ETF se chevauchent ? », « bilan du mois » | Analyste |
| « J'ai envie d'acheter X », « je veux vendre », « j'ai peur », « ça monte fort », « je veux progresser », « apprends-moi » | Coach |
| « Quoi de neuf ? », « c'est quoi cette chute ? », « cette news me touche ? », « le brief » | Veilleur |

## Appeler quelqu'un par son nom

Tu peux désigner l'agent : **« coach, j'ai peur avec la baisse »**, **« analyste, où en est mon portefeuille ? »**. L'assistant appelle directement celui-là.

## Quand ta demande a besoin de plusieurs agents

Il les enchaîne et te donne **une seule réponse**, structurée ainsi : la conclusion en une phrase, les 2 ou 3 chiffres qui la justifient (avec leur source), ce que ça change pour toi, ce qui reste incertain, la suite.

## Quand ta demande est floue

Il pose **une seule question** (objectif ? horizon ? montant ?), jamais un questionnaire, et ne redemande rien qui soit déjà dans ton dossier.

## Les « suites possibles »

Chaque réponse se termine par une ou deux suites en phrases simples, par exemple « Tu veux que je regarde où mettre ton versement de ce mois ? ». Tu n'as jamais à te demander quoi demander : réponds « oui » ou choisis une suite.

## Régler le niveau d'explication

Dis-le simplement : « explique-moi comme à un débutant » ou « donne-moi les hypothèses et les limites ». Le fond reste identique (mêmes chiffres, mêmes limites), seuls le ton et la profondeur changent. Un terme technique est toujours défini à sa première apparition.

# 5. Le Directeur

Le Directeur est le **chef d'orchestre**. Il ne calcule pas et ne conseille pas lui-même : il comprend, route et synthétise. Il est défini dans `CLAUDE.md`, qui est chargé automatiquement à chaque séance.

## Ce qu'il fait à chaque séance

1. **Il sait qui parle** : si tu ne te présentes pas, il demande « Salut, c'est qui ? ».
2. **Il charge ton dossier** : `profil.md`, `charte.md`, `journal.md` s'ils existent.
3. **Il lance l'accueil** si ton dossier n'existe pas.
4. **Il route** ta demande vers le bon agent, en lui transmettant ton prénom, le chemin de ton dossier et ta demande telle quelle.
5. **Il fait la synthèse** quand plusieurs agents ont travaillé.
6. **Il se relit avant de répondre** (contrôle qualité en 7 points : chiffres sourcés ou calculés, aucune prédiction, aucun « achète » ou « vends », une fiche citée, taux fiscaux cohérents, nominal ou réel précisé, rappel du cadre quand c'est pertinent, une ou deux suites).

## Ses règles de réponse

- En français, direct, sans jargon non expliqué, sans tirets longs.
- Toujours une ou deux suites possibles.
- Un rappel discret « outil d'aide à la réflexion, pas un conseil réglementé » quand c'est pertinent.

# 6. La veille (le Veilleur)

**Sa mission : moins d'informations, mais les bonnes.** Seulement ce qui touche tes placements et tes objectifs. Moins de bruit, c'est moins de stress.

## Quand l'appeler

- « Quoi de neuf ce matin ? » ou « fais-moi le brief »
- « C'est quoi cette chute sur les marchés ? »
- « Cette news me concerne-t-elle ? »
- « Que se passe-t-il cette semaine (BCE, inflation, résultats) ? »

## Le brief du jour (2 minutes de lecture)

Un brief contient toujours, dans cet ordre :

1. **Ce qui a bougé** sur les marchés liés à tes placements, avec le chiffre de clôture. Une cause n'est donnée que si une source la fournit (« selon Reuters... »). Sinon : « cause non établie ». Aucun récit inventé après coup.
2. **3 infos maximum**, chacune avec sa source, sa date et son importance : **à ignorer**, **à surveiller** ou **à agir**.
3. **L'agenda du jour** : banques centrales, inflation, emploi, résultats des grosses entreprises présentes dans tes ETF.
4. **Le verdict**, le plus souvent **« rien à faire aujourd'hui »**, avec la raison.
5. **Une notion expliquée en 3 lignes.**

« Rien d'important » est un brief valable. Le Veilleur le dit franchement plutôt que de remplir.

> **Exemple (fictif)** : « Brief de 8 h, avant l'ouverture, les chiffres peuvent changer. Ton ETF monde a gagné 0,4 % hier à la clôture (Yahoo Finance via financial-data). Une seule info à surveiller : la BCE publie ses taux jeudi (source : communiqué BCE). Verdict : rien à faire aujourd'hui, ton plan ne dépend pas de cette décision. Notion du jour : un taux directeur, c'est le prix auquel les banques empruntent à la banque centrale. »

## Expliquer une actualité

Colle un titre ou décris une news. Le Veilleur répond : ce qui s'est passé, pourquoi ça compte (ou pas), quels placements sont concernés, sur quel horizon, en séparant les **faits** des **opinions**. Il ouvre l'article ou le communiqué avant de le citer : **un titre n'est pas une information**.

## Quand le marché chute

Il chiffre la baisse, la replace dans l'historique (baisses passées et temps de récupération), te rappelle ton plan, puis **passe la main au Coach** si tu es stressé.

## Ses compétences avancées

Elles sont dans `connaissances/agents/veilleur.md`. Demande-les simplement :

| Compétence | Ce que ça donne |
|---|---|
| **Agenda des événements** | Tableau de la semaine : date, événement, ce qui est concerné, impact attendu. Inclut tes échéances perso (déclaration d'impôts, révision du Livret A les 1er février et 1er août) |
| **Tableau de bord macro** | Cycle économique, taux directeur, courbe des taux, conditions financières, toujours ramenés à « ce qui change pour toi » |
| **Comprendre un secteur** | Taille, concentration, acteurs, tendances, valorisation |
| **Vérifier une information** | Remonter à la source, croiser, repérer ce qui est sponsorisé ou recyclé |
| **Veille structurée** | Revue trimestrielle de tes sources et de tes thèmes |
| **Lire vite un document** | Les points clés d'un rapport ou d'un communiqué |

## Ses sources

- **Actualité en continu** (serveur `actualite-flux`) : communiqués de la BCE, Le Monde économie, BBC Business. Il peut chercher un sujet, résumer, vérifier qu'un flux répond, ou ajouter un flux le temps de la séance.
- **Lecture d'une page précise** (serveur `lecture-web`) : article, communiqué officiel, fiche d'un indice.
- **Données de marché** (serveur `financial-data`) : cours, historiques, séries macro, change.
- **Sources fiables uniquement** : Reuters, Les Échos, Financial Times, Bloomberg, banques centrales, AMF. Certains sites (AMF, Les Échos, INSEE) bloquent les robots : il passe alors par la recherche web.

## La newsletter du dimanche

Chaque dimanche à 18 h 47, une routine t'envoie par email « **Ta semaine bourse** ». Elle se lit en 4 minutes, dans cet ordre :

1. **Vue d'ensemble** : le verdict en deux phrases, trois pastilles (marchés, taux et banques centrales, politique), le chiffre clé et les trois rendez-vous à ne pas rater.
2. **Les marchés** : tableau des repères de la semaine (MSCI World, S&P 500, Stoxx 600, CAC 40, émergents, euro/dollar, taux 10 ans, bitcoin). Un chiffre introuvable s'affiche « non disponible », il n'est jamais inventé.
3. **Ce qui s'est passé** : 3 à 5 faits, chacun classé à ignorer, à surveiller ou à agir, avec « pourquoi ça compte ».
4. **Pour toi** : ton portefeuille lu dans ton Google Sheet (valeur, écarts aux cibles, alertes) et ce que chaque fait change pour tes placements.
5. **La semaine qui vient** : agenda macro, puis les résultats d'entreprises en deux listes, celles de **tes ETF** (poids dans l'indice) et **les plus suivies du marché**.
6. **Une notion** en 3 lignes, puis les **lignes à recopier** dans la feuille Veille.
7. **Limites de cette édition** (ce qui n'a pas pu être trouvé) et **Sources**.

Les sources ne sont jamais au milieu du texte : on trouve [1], [2]... dans les phrases, et la liste des liens est en bas, dans l'ordre de lecture. Le mode d'emploi de la routine et ce dont elle a besoin (dépôt, Gmail, Google Drive) sont dans `docs/NEWSLETTER.md` ; le format exact de l'édition dans `templates/newsletter-modele.md`.

## Ce qu'il ne fait pas

Aucune prédiction, aucun objectif de cours, aucune « opportunité ». **Le brief du jour n'est pas automatique** : tu le demandes quand tu en as envie. Seule la newsletter du dimanche part toute seule.

# 7. L'analyse du portefeuille (l'Analyste)

**Sa mission : des chiffres justes et compréhensibles, toujours suivis de la prochaine action concrète.** Tous les chiffres viennent des scripts.

## Ce qu'il lit

Ton profil, tes **positions** (`positions.csv`), tes **cibles** (`cibles.csv`) et tes **flux** (`flux.csv`, tes versements). Si tes valeurs datent de plus d'un mois, il te demande les valeurs actuelles.

## Ses 10 routines

| # | Tu dis | Il fait |
|---|---|---|
| 1 | « Voilà mes nouveaux montants » | Met à jour `positions.csv`, et `flux.csv` pour chaque versement, mais **seulement une fois que tu confirmes l'avoir passé** |
| 2 | « Où j'en suis ? » | **Radiographie** : répartition, écarts à la cible, concentration, frais, point principal, en 5 lignes maximum |
| 3 | « Je mets combien où ce mois-ci ? » | **Répartition du versement** en ordres concrets par ligne (« 300 € sur tel ETF »). Il rééquilibre **par les versements**, jamais en vendant, sauf écart supérieur à 10 points |
| 4 | « Ma performance ? » | **Performance réelle (XIRR)**, comparée aux mêmes versements placés à 7 % par an. Avec moins d'un an d'historique, il le dit et relativise |
| 5 | « Mes ETF se chevauchent ? » | **Exposition réelle** : pays, part en dollars, grandes entreprises à travers tous tes ETF (« tu as 5 % de Nvidia sans le savoir ») |
| 6 | « Quel ETF choisir ? » | Compare **frais, encours, réplication, éligibilité PEA, écart de suivi**. Jamais sur la performance passée |
| 7 | « Bilan du mois » (ou de l'année) | Performance, versements faits contre prévus, frais, écarts, décisions hors plan. Archivé en tête de `bilans.md` |
| 8 | « Faut-il rééquilibrer en vendant ? » | Plan de ventes seulement si une poche dépasse le seuil de ta charte (10 points par défaut), avec le **coût fiscal** de chaque vente |
| 9 | « Et si ça chutait ? » | **Test de résistance** : l'impact en euros de 6 scénarios de crise |
| 10 | (spontané) | Signale **l'argent laissé sur la table** : abondement employeur non utilisé, LEP non ouvert, épargne de précaution trop dormante, PEA pas encore ouvert, liquidités qui attendent chez le courtier |

## Le test de résistance, à ne pas sauter

Il traduit le pire scénario en euros puis pose la question : **« si ça arrivait le mois prochain, changerais-tu quelque chose ? »**. Si ta réponse est « je vendrais », c'est le signe que l'allocation est trop risquée pour toi : le Stratège ajuste.

## Le rééquilibrage par ventes

C'est une **proposition** : un tableau avant / cible / après, avec l'impôt estimé. Rappel important : vendre dans un PEA ou une assurance vie n'est pas imposé tout de suite, contrairement au compte-titres (CTO). Tu passes toi-même les ordres.

## Ses compétences avancées

Dans `connaissances/agents/analyste.md` : bilan et rapport de portefeuille, rééquilibrage, diversification, mesure de performance, risque historique, choix d'un fonds, fiche entreprise, lecture des résultats et des états financiers, valorisation (comparaison et flux), avantage concurrentiel, poche obligataire, or et crypto-actifs, facteurs, devises, taille maximale d'une ligne, tableurs fiables, lecture d'un relevé de courtier, graphiques honnêtes.

> **Exemple (fictif)** : « Ton portefeuille vaut 12 400 €. Tu es à 52 % en actions USA pour une cible de 40 % (écart de 12 points). Frais moyens : 0,12 % par an. Pour ton versement de 500 € : 0 € sur les USA, 350 € sur l'Europe, 150 € sur les émergents. Point à retenir : ne vends rien, le versement suffit à rééquilibrer en 4 mois. »

# 8. Le budget (le Conseiller budget)

**Sa mission : que tu dépenses mieux, épargnes plus et investisses plus, sans stress.** Au début, le **taux d'épargne** est le premier levier de richesse.

## Quand l'appeler

« Je viens d'être payé », « mes dépenses dérapent », « j'ai une prime », « combien garder de côté ? », « c'est une arnaque ? », « j'ai un crédit », « mes abonnements ».

## Ses 12 routines

| Routine | Ce qu'elle apporte |
|---|---|
| **Point budget du mois** | Revenus, besoins, envies, épargne. Calcule ton taux d'épargne, le compare à la règle **50 / 30 / 20**, puis à l'objectif de **30 %** |
| **Je viens d'être payé** | Vérifie que le virement automatique « se payer en premier » est fait, puis passe la main à l'Analyste pour répartir |
| **Épargne de précaution** | Cible de **3 à 6 mois de dépenses essentielles** (6 à 12 mois pour un revenu variable), en paliers : 1 mois sur le compte courant, le reste en Livret A, LDDS ou LEP. Quand y puiser, comment la reconstituer |
| **Dettes** | Liste les taux. **Au-dessus de 5 à 6 %**, on rembourse en priorité |
| **Prime ou augmentation** | **Au moins 50 %** de la hausse vers l'investissement, le reste pour te faire plaisir sans culpabilité |
| **Audit des abonnements** | Tous les trimestres : liste, coût sur un an, coupes proposées |
| **Augmenter ses revenus** | Pistes concrètes adaptées à ton profil |
| **Arnaque ?** | Vérifie la plateforme sur les **listes noires de l'AMF** et repère les signaux d'alerte (rendement promis, urgence, paiement en crypto) |
| **Revue annuelle de protection** | Bénéficiaires de l'assurance vie, mutuelle, prévoyance, accès aux comptes en cas de problème |
| **4 enveloppes de dépenses** | Alternative au mot « budget » : charges fixes 50 à 60 %, investissement 10 % ou plus, projets 5 à 10 %, plaisir 20 à 35 % |
| **Ordre des priorités** | Précaution, abondement employeur (argent gratuit), dettes à plus de 5 à 6 %, PEA, assurance vie, projets |
| **Couple** | Un point argent mensuel d'une heure, chacun garde un domaine qu'il gère |

## L'ordre des priorités, à retenir

1. Épargne de précaution
2. Abondement de l'employeur, s'il existe
3. Dettes à plus de 5 à 6 %
4. PEA
5. Assurance vie
6. Projets

Le Conseiller se concentre sur les **grandes manettes** (taux d'épargne, frais, dettes, salaire, enveloppes), pas sur un abonnement à 12 €.

## Ses compétences avancées

Dans `connaissances/agents/conseiller-budget.md` : épargne de précaution, plan de dépenses, trésorerie du foyer, dettes et crédit, revenus et négociation, assurances et prévoyance, lire un contrat, détection d'anomalies et de fraudes, priorités.

## Son ton

Bienveillant, **jamais moralisateur** sur les dépenses « envies ». L'argent plaisir est fait pour être dépensé, puisque l'essentiel est déjà financé.

# 9. La stratégie (le Stratège)

**Sa mission : que tu saches où tu vas, dans quelles enveloppes, et avec quelles règles écrites.**

## Quand l'appeler

« Mes objectifs », « PEA ou assurance vie ? », « combien d'impôt si je vends ? », « serai-je libre à 40 ans ? », « écrivons ma charte », « comment préparer ma retraite ? ».

## Ses 7 routines

| Routine | Ce qu'elle apporte |
|---|---|
| **Objectifs** | Transforme des envies floues en **1 à 3 objectifs nommés, datés, chiffrés**, une poche par objectif. L'argent nécessaire **dans moins de 3 ans ne va pas en actions** |
| **Projection** | Trois scénarios, jamais un chiffre unique : **prudent (4 %), central (6 %), favorable (8 %)** en nominal, soit environ 2, 4 et 6 % en réel. Il précise toujours nominal ou réel. Repère de liberté financière : 25 à 28 fois tes dépenses annuelles |
| **Ordre des enveloppes** | Précaution, puis **PEA** (à ouvrir tôt pour lancer le compteur des 5 ans), assurance vie, CTO, et PER si ta tranche d'imposition est d'au moins 30 % |
| **Simulation fiscale d'une vente** | Enveloppe, ancienneté, plus-value, puis impôt estimé par script |
| **Charte d'investissement** | Une page co-écrite avec toi, à froid (détail ci-dessous) |
| **Rappels déclaratifs** | En avril : formulaire 3916 (comptes à l'étranger), 2086 (crypto), IFU |
| **Retraite et retraits** | Règle des 4 % comme repère, puis version à garde-fous (détail ci-dessous) |

## Les repères fiscaux 2026

| Enveloppe | Ce qui s'applique |
|---|---|
| **CTO** | PFU de 31,4 % (12,8 % d'impôt plus 18,6 % de prélèvements sociaux) |
| **PEA de plus de 5 ans** | Prélèvements sociaux de 18,6 % seulement sur les gains |
| **Assurance vie** | Prélèvements sociaux de 17,2 %, avec un régime spécifique selon l'ancienneté |
| **Livrets réglementés** | Exonérés |

Ces taux changent avec les lois de finances : l'assistant les revérifie sur service-public.fr quand sa fiche date de plus de 6 mois. **Pour les cas complexes, fais valider par un professionnel.** Un transfert de titres du CTO vers le PEA est impossible.

## La charte d'investissement

C'est **ton règlement intérieur d'investisseur**, écrit à froid, en une page, dans `prive/<prénom>/charte.md`. Elle sert à une chose : quand la peur ou l'euphorie arrive, tu n'as pas à décider, tu appliques ce que tu as écrit. Elle contient 8 parties :

1. **Pourquoi j'investis** : objectifs, et ce qui serait « assez »
2. **Mon rapport au risque** : capacité et volonté. **La plus prudente des deux décide**
3. **Mes contraintes** : liquidité, horizon, enveloppes, particularités
4. **Allocation cible** avec fourchettes tolérées
5. **Règles d'achat** : versement mensuel quoi qu'il arrive, délai de 24 à 72 h hors plan
6. **Règles de vente et de rééquilibrage**
7. **En cas de baisse** : ce que tu fais à -20 % et à -35 %
8. **Mesure et revue** : indice de référence choisi **maintenant**, revue annuelle et après un événement de vie

La partie 2 est pré-remplie avec ton profil de risque (chapitre 3), et l'allocation cible reste dans la fourchette d'actions de ton profil. Le Stratège teste ton allocation avec le test de résistance avant de la valider. Le modèle est dans `templates/charte-modele.md`.

## La retraite et les retraits

La règle des 4 % est un repère. La version à garde-fous : on part d'un taux, on augmente les retraits de l'inflation chaque année, on les **réduit de 10 %** si le taux de retrait réel dépasse de 20 % le taux de départ, on les **augmente de 10 %** s'il passe 20 % en dessous. Il faut accepter de vraiment réduire quand c'est nécessaire.

## Ses compétences avancées

Dans `connaissances/agents/stratege.md` : charte, allocation stratégique, objectifs et épargne nécessaire, retraite et retraits, optimisation fiscale des enveloppes, transmission, épargne salariale et actions gratuites, décider sous incertitude, adéquation au profil, démarche de plan financier, mémo de décision important.

## Ses règles

Il précise toujours « à vérifier avec un professionnel pour les cas complexes » sur la fiscalité, et ne recommande **aucun produit précis sans critères explicites** (frais, éligibilité, encours).

# 10. Le coach

**Sa mission : te protéger de tes émotions et te faire progresser.** Le comportement pèse plus que le choix des placements.

## Quand l'appeler

« J'ai envie d'acheter X », « je veux vendre », « j'ai peur », « ça monte fort », « je veux progresser », « apprends-moi ».

## Le garde-fou de décision

C'est la fonction la plus précieuse. Dès que tu veux acheter ou vendre **en dehors du versement prévu**, le Coach te guide :

1. **Il pose au maximum 5 questions** : quoi, combien, pourquoi, pourquoi maintenant, qu'est-ce qui invaliderait l'idée ? Plus : d'où vient l'idée, et comment tu te sens de 1 à 10.
2. **Avocat du diable** : les 3 meilleurs arguments contre, et un **pré-mortem** (« dans un an, c'est un échec : pourquoi ? »).
3. **Il vérifie** tes règles, le **plafond d'une ligne (5 % du total après achat)** et si tu détiens déjà la valeur à travers tes ETF.
4. **Verdict clair** :
   - **conforme au plan** ;
   - **attendre 24 à 72 h** ;
   - **contraire à tes règles**.
5. **Il écrit l'entrée dans ton journal** : date, décision, raisons, source de l'idée, émotion, verdict, date du bilan à 3 mois.

Tu restes libre de décider. Le but est que ce soit une décision, pas une réaction.

## Quand tu as peur ou que tu paniques

Mise en perspective historique (baisses passées, temps de récupération), rappel de ton plan et de ton horizon. **Si ton plan est respecté, il n'y a rien à faire.** S'il faut absolument agir, mieux vaut réduire de 5 à 10 points que tout vendre.

## Les situations qu'il sait accompagner

Pour chacune, il valide d'abord l'émotion, pose 3 à 5 questions, évite les pièges, puis te dit une phrase ferme et bienveillante.

| Situation | Son approche |
|---|---|
| **Envie d'acheter un titre qui monte fort** | Depuis quand le suis-tu ? Que fais-tu s'il perd 30 % demain ? Respecte-t-il ta charte ? On prend 72 h pour poser les chiffres |
| **Envie de vendre après -20 %** | As-tu besoin de cet argent ce mois-ci ? Les raisons de ton achat ont-elles changé ? On relit la charte écrite à froid |
| **FOMO sur une crypto** | Quelle part de ton patrimoine ? Es-tu prêt à tout perdre ? Voyons ce que ta charte autorise |
| **Certitude après un « bon tuyau »** | Qui t'a informé, a-t-il un intérêt ? Pré-mortem d'abord |
| **Envie d'arrêter les versements** | Vraie baisse de revenu ou peur de l'actualité ? Adapter le montant ou relire le plan |
| **Euphorie après un gros gain** | Compétence ou chance ? Vérifions que ton allocation est toujours celle de ta charte |
| **Culpabilité après une erreur** | Quelle leçon précise ? Qu'automatiser pour ne plus la refaire ? On la note dans le journal |

## Comprendre ton rapport à l'argent

Le Coach repère ton profil dominant et s'adapte. Il le note dans ton `profil.md`.

| Profil | Ce qui t'aide |
|---|---|
| **L'Évitant** | Petits pas concrets, automatisation |
| **L'Optimiseur** | Recentrer sur les grandes manettes, « tu épargnes 38 %, pour quoi faire ? » |
| **L'Inquiet** | Scénarios chiffrés prudents, marges de sécurité |
| **Le Rêveur** | Relier le rêve à un montant mensuel et à une première étape |

## Le journal et les bilans

Chaque décision hors plan est écrite dans `prive/<prénom>/journal.md`. À **3 mois et à 12 mois**, le Coach te refait le point : bonne analyse ou chance ? Il repère tes biais récurrents et les sources d'idées qui rapportent ou qui coûtent. Il calcule aussi **le coût des émotions** : l'écart en euros entre tes décisions hors plan et le simple respect du plan.

## Les actions en direct ou les thèmes (lignes « satellites »)

Avant l'achat, il écrit dans ton journal : la thèse en 1 ou 2 phrases, 3 à 5 arguments, 3 à 5 risques, **ce qui l'invaliderait** (une thèse impossible à contredire n'en est pas une) et la condition de sortie. Revue au moins tous les trimestres.

## Apprendre

Un parcours en **12 modules** : 1 bases et intérêts composés, 2 ETF, 3 enveloppes et fiscalité, 4 allocation, 5 risque et volatilité, 6 psychologie, 7 lire une news, 8 lire le bilan d'une entreprise, 9 valorisation, 10 macro et taux, 11 crypto, 12 construire sa charte. Dis « apprends-moi les ETF » : il explique à 3 niveaux avec des exemples tirés de **ton** portefeuille, puis pose une question de vérification. Ton avancement est suivi dans `profil.md`. Le contenu détaillé est un brouillon à relire (`docs/recherche/08-pedagogie.md`).

## Ses compétences avancées

Dans `connaissances/agents/coach.md` : psychologie de l'argent, biais et parades, pré-mortem, avocat du diable, calibration des croyances, critères de sortie écrits à l'avance, thèse réfutable, listes de contrôle, bilan des décisions, pédagogie, après une erreur.

## Son état d'esprit

Empathique mais ferme, jamais culpabilisant. **Raisonnable plutôt que rationnel** : un plan un peu moins optimal que tu tiendras pendant une baisse de 35 % vaut mieux qu'un plan parfait que tu abandonneras. Il ne dit jamais « achète » ou « vends ».

# 11. Les calculs (les scripts)

Tu n'as **jamais besoin de les lancer à la main** : les agents le font. Ils sont dans le dossier `scripts/` et lisent tes fichiers privés. Voici ce qui existe, pour comprendre d'où viennent les chiffres.

| Script | Ce qu'il calcule | Utilisé par |
|---|---|---|
| `allocation.py` | Poids, écarts à la cible, répartition d'un versement sans vendre, frais, simulation d'ajout d'une ligne | Analyste, Coach |
| `performance.py` | Rendement réel (XIRR) comparé aux mêmes versements placés à un taux de référence | Analyste |
| `projection.py` | Capital futur, délai ou versement nécessaire pour un objectif, équivalent en euros d'aujourd'hui avec l'inflation | Stratège |
| `reequilibrage.py` | Plan de ventes si une poche dépasse le seuil, impôt estimé, contrôle achats = ventes. Ne passe aucun ordre | Analyste |
| `exposition.py` | Exposition réelle par pays, part en dollars et grandes entreprises à travers tes ETF | Analyste, Coach |
| `stress.py` | Impact en euros de 6 scénarios de crise (hypothèses, pas des prévisions), comparé à ta perte maximale acceptable | Analyste, Stratège |
| `fiscalite.py` | Impôt estimé d'un retrait en CTO, PEA ou assurance vie | Stratège |
| `historique.py` | Interroge la base historique des marchés : un mois, une période, les grandes baisses, les rendements glissants, un événement ; régénère le classeur Excel et la base SQLite | Veilleur, Coach, Stratège, Analyste |
| `maj_historique.py` | Met à jour la base historique (Yahoo Finance, STOXX, FRED), contrôle sa qualité et vérifie les liens des événements | Toi ou l'assistant, une fois par mois |
| `profil_risque.py` | Affiche le test de profil de risque chiffré sur ton montant, puis note tes réponses : capacité, tolérance, besoin de risque, connaissances, profil retenu, perte maximale acceptable, alertes | Directeur (accueil), Stratège |
| `creer_sheet.py` | Génère le classeur Excel du portefeuille (modèle vide) | Toi, à la demande |
| `installer_mcp.py` | Installe les serveurs de données et d'actualité sur un ordinateur | Toi, une fois |

## Le format de tes fichiers

L'assistant les crée et les met à jour pour toi, mais voici à quoi ils ressemblent.

**`positions.csv`** : une ligne par placement.
```
nom,poche,enveloppe,investi,valeur,frais_annuels_pct,date_valeur
ETF S&P 500,USA,PEA,1000,1100,0.07,2026-10-30
```

**`cibles.csv`** : ton allocation cible par poche.
```
poche,cible_pct
USA,40
```

**`flux.csv`** : tes versements (en négatif) et retraits (en positif).
```
date,montant
2026-01-15,-500
```

`investi` est le prix de revient de la ligne. Le plafond du PEA se suit avec le total versé sur le PEA, noté dans ton profil.

## Pourquoi des scripts

Un modèle de langage peut se tromper sur un calcul ou « deviner » un chiffre. Ici, **tout chiffre qui compte est produit par un programme vérifiable**, et l'assistant se contente de l'expliquer. C'est la règle n° 1.

# 12. Marché et actualité en direct (serveurs MCP)

Trois petits serveurs donnent aux agents un accès aux données en direct. Ils sont **gratuits** et tournent **sur ton ordinateur**.

| Serveur | Rôle | Agents | Remarques |
|---|---|---|---|
| `financial-data` | Cours, historiques, fondamentaux, séries macro, change, matières premières, crypto, actualité d'une entreprise | Analyste, Veilleur | Données Yahoo Finance **indicatives** (API non officielle). Clé FRED facultative pour les séries macro |
| `actualite-flux` | Flux RSS : derniers articles, recherche, synthèse | Veilleur | Flux par défaut : BCE, Le Monde économie, BBC Business |
| `lecture-web` | Lire une page web précise | Veilleur | Pour vérifier à la source au lieu de se fier à un titre |

## Comment ça se passe

- Les cours s'obtiennent avec un **ticker Yahoo**, par exemple `CW8.PA`. L'assistant cite toujours la source et l'heure.
- **Jamais de décision sur un seul chiffre** : ces données sont un repère.
- **Si un serveur ne répond pas**, l'assistant continue sans lui et te le dit.

## Installer (une seule fois par ordinateur)

```bash
python scripts/installer_mcp.py
```

L'installeur lit `mcp/serveurs.json`, installe les trois serveurs dans `externe/`, puis écrit `.mcp.json` avec les chemins de **ton** ordinateur. Ensuite : **redémarre Claude Code** et accepte les serveurs quand il le propose. Il faut Python 3.10 ou plus, et git.

Pour régénérer seulement `.mcp.json` sans réinstaller : `python scripts/installer_mcp.py --ecrire-seulement`.

## Ajouter ou changer un serveur

La liste vit dans `mcp/serveurs.json` (versionnée, avec version et licence de chaque serveur). Une clé API éventuelle va dans un fichier `.env`, **jamais dans le code**.

# 13. La base de connaissances

## Les fiches

Le socle de toutes les recommandations. Chaque point est numéroté, et l'assistant cite la fiche quand il s'en sert.

| Fiche | Thème |
|---|---|
| **A** | Budget et fondations financières |
| **B** | Objectifs et plan |
| **C** | Enveloppes et fiscalité (France) |
| **D** | Allocation et diversification |
| **E** | Méthode d'investissement |
| **F** | Comportement et émotions |
| **G** | Mesure de la performance |
| **H** | Information et apprentissage |
| **I** | Protection (arnaques, prévoyance) |

Le test de profil de risque a son propre fichier, `connaissances/questionnaire-risque.json` : toutes les questions, leurs points et les plafonds y sont réunis, et le script ne lit que lui. Sa méthode est résumée dans la fiche D, point 118.

## Les manuels de compétences

Chaque agent a son **manuel**, fusion des meilleurs skills open source (Anthropic en priorité), adaptés à un particulier français et aux règles de l'assistant (pas de prédiction, pas d'avis d'achat ou de vente). Ils sont dans `connaissances/agents/`. L'agent ouvre seulement la section qui correspond à ta demande.

| Manuel | Nombre de compétences |
|---|---|
| Directeur | 6 |
| Veilleur | 10 |
| Analyste | 20 |
| Conseiller budget | 9 |
| Stratège | 11 |
| Coach | 11 |

## Le degré de confiance des fiches

Toutes les fiches ne sont pas vérifiées au même niveau, et c'est écrit dans `connaissances/00-SOURCES.md`.

- **Vérifié à la source** : fiscalité (fiche C, service-public.fr), composition des grands indices (fiches officielles MSCI, Nasdaq, State Street), taux des livrets au 1er août 2026.
- **À vérifier** : une partie des fiches D, E, F, H, I, B et G vient de recherches externes non encore confirmées. L'assistant les marque « à vérifier » et te le dit avant de s'en servir pour un chiffre.

## Les recherches

Le dossier `docs/recherche/` contient les 12 recherches de départ (fiscalité, produits, historique, projection, retrait, allocation, comportement, pédagogie, veille, budget, arnaques, sources) et leurs tableaux (`etf.csv`, `courtiers.csv`, `baisses-majeures.csv`, `arnaques-signaux.csv`...). Le dossier `docs/externe/` garde la trace des dépôts open source dont les compétences ont été reprises (version et licence).

## Les données des indices

Dans `donnees/` : la composition par pays et par grandes entreprises des principaux indices, **datée**. `exposition.py` s'en sert. **À mettre à jour chaque trimestre** : l'assistant te prévient quand elles ont plus de 3 mois.

# 14. L'historique des marchés

## Ce que c'est

Une **base de données des marchés financiers, mois par mois**, pour relativiser, comparer et apprendre avec de vrais chiffres plutôt qu'avec des souvenirs. Elle est dans `donnees/historique/`.

- **24 séries**, environ 15 500 mois. Pour chaque mois : le niveau, la variation en %, la source.
  - **15 indices de référence** : MSCI World, MSCI ACWI, émergents, S&P 500 (prix et dividendes réinvestis), Nasdaq-100, Nasdaq Composite, Dow Jones, STOXX Europe 600, Euro Stoxx 50, CAC 40, DAX, FTSE 100, Nikkei 225, Hang Seng.
  - **9 séries OCDE**, le minimum de prix sur longue période : France, Allemagne, Royaume-Uni, Japon, zone euro, Inde, Brésil, Corée du Sud, Chine.
- **La macro** : inflation aux États-Unis et en France, taux de la Fed et de la BCE, taux à 10 ans, euro contre dollar, pétrole, périodes de récession.
- **Une frise de 86 événements** de 1971 à 2025 : chocs pétroliers, Lundi noir, bulle internet, Lehman, crise de l'euro, Brexit, Covid, guerre en Ukraine, élections, décisions des banques centrales. Chacun a sa date et **sa source, dont le lien a été vérifié**.

## Jusqu'où ça remonte

| Depuis | Séries |
|---|---|
| 1885 | Dow Jones (MeasuringWorth avant 1992) |
| 1927 | S&P 500 |
| 1955-1960 | Actions France, Royaume-Uni, Japon, Inde et Allemagne (OCDE) |
| 1965 | Nikkei 225 |
| 1971-1972 | Nasdaq Composite, MSCI World |
| 1981 | Actions Corée du Sud (OCDE) |
| 1984-1988 | FTSE 100, Nasdaq-100, STOXX Europe 600, Euro Stoxx 50, Hang Seng, DAX, MSCI ACWI, S&P 500 dividendes réinvestis, actions zone euro (OCDE) |
| 1990-1999 | CAC 40, émergents, actions Brésil et Chine (OCDE) |

Une série commence à sa création ou au début de l'historique librement accessible. **Rien n'est inventé pour combler un trou.**

## Le minimum de prix : les séries OCDE

Quand l'indice phare n'a pas d'historique libre ancien, la base ajoute l'**indice de cours des actions de l'OCDE** du pays. C'est le cas du CAC 40 avant 1990, du DAX avant 1987 et des pays émergents.

- **Ce que c'est** : une **moyenne du mois**, pas une clôture.
- **À quoi ça sert** : aux tendances longues. Par exemple, sur 20 ans glissants, le marché français a été positif dans 97 % des cas depuis 1955 (prix seul).
- **À quoi ça ne sert pas** : comparer un mois précis avec un indice en clôture. Les séries OCDE ne sont jamais raccordées aux indices phares.

## La base de données

Tout est réuni dans **`donnees/historique/marches.sqlite`**, une vraie base de données. Elle est versionnée sur GitHub.

| Table | Contenu |
|---|---|
| `indices` | La fiche de chaque série : nom, zone, devise, type, sources, début, fin |
| `niveaux` | Une ligne par mois et par série (environ 15 500) |
| `macro` | Les séries macroéconomiques mois par mois |
| `evenements` | La frise d'événements avec leurs sources |
| `rendements_annuels` (vue) | Le rendement de chaque année, par série |

- **Pour l'ouvrir et l'explorer** : un logiciel gratuit comme DB Browser for SQLite.
- **Pour la lire sans outil** : le classeur Excel.
- **Pour l'interroger en langage normal** : demande à l'assistant.

Les fichiers CSV du même dossier restent la source de référence. La base est reconstruite à partir d'eux à chaque mise à jour.

## Ce que tu peux demander

| Tu dis | Tu obtiens |
|---|---|
| « Que s'est-il passé en octobre 2008 ? » | La variation de chaque indice ce mois-là et sur 12 mois, la macro, les événements |
| « Montre-moi les grandes baisses du MSCI World » | Chaque baisse de plus de 20 % : sommet, creux, durée, temps pour revenir au sommet |
| « Sur 20 ans, un ETF monde a-t-il déjà perdu de l'argent ? » | Le pire, le médian et le meilleur rendement sur 20 ans glissants, en euros et après inflation |
| « Combien a fait le CAC 40 depuis 2000 ? » | Le rendement cumulé et annualisé, le meilleur et le pire mois, la plus forte baisse |
| « Comment les marchés ont réagi au Covid ? » | L'événement, sa source, et la variation des grands indices 1, 3 et 12 mois après |

Les agents s'en servent d'eux-mêmes :
- le **Veilleur** et le **Coach** quand ça chute, pour remettre la baisse en perspective ;
- le **Stratège** pour montrer ce que l'histoire a réellement donné sur la durée de tes projections ;
- l'**Analyste** pour comparer ta performance à un indice.

## Le classeur Excel

`docs/Historique-marches.xlsx` contient :
- **un onglet par série** : une ligne par année, une case par mois, en vert quand ça monte et en rouge quand ça baisse, et le total de l'année ;
- **une synthèse annuelle** de tous les indices ;
- **les grandes baisses** avec les événements autour du creux ;
- **la frise d'événements** avec la réaction des marchés ;
- **la macro année par année**.

## Quelques repères tirés de la base

Ces chiffres sont **en prix seul**, sans les dividendes :

- **Le MSCI World en dollars** a fait environ **+7,1 % par an** de 1972 à 2026. **Sur 20 ans glissants, il n'a jamais perdu** : la pire période (2000-2020) a encore fait +1,3 % par an.
- **En euros et après inflation**, 91 % des périodes de 20 ans sont positives. La pire (1972-1992) a perdu 4,1 % par an.
- **Le Nikkei** a mis **34 ans** à retrouver son sommet de 1989 : c'est la meilleure leçon de diversification mondiale.

## Les limites

- **Prix seul pour la plupart des indices** : sans les dividendes, le rendement est sous-estimé d'environ 2 à 4 % par an. Exceptions : S&P 500 dividendes réinvestis, DAX, et la série émergents.
- **Devises** : chaque indice est dans sa devise d'origine. L'option « en euros » existe pour les indices en dollars ; avant 1999, elle passe par le mark allemand (série reconstituée).
- **Fins de mois** : les baisses mesurées au jour le jour sont plus fortes. Pour le Covid, le S&P 500 a perdu environ 34 % en séance, mais 20 % en fin de mois.
- **Émergents** : l'indice MSCI n'étant pas accessible, on utilise un fonds Vanguard qui le suit (dividendes réinvestis, frais déduits).
- **Le passé n'annonce pas l'avenir.** La base sert à relativiser et à calibrer des hypothèses, jamais à prédire.
- **Usage personnel** : ces données ne doivent pas être publiées. Le dépôt GitHub est privé et doit le rester.

Le détail des sources, de la couverture et des contrôles qualité est dans `donnees/historique/SOURCES.md`.

# 15. Le classeur Excel

Le fichier `templates/Portefeuille-complet.xlsx` est un classeur **vide et anonyme** pour suivre ton portefeuille à la main ou en parallèle de l'assistant. Il peut être régénéré avec `python scripts/creer_sheet.py` (option `--exemple` pour une version remplie d'exemples).

## Les onglets

| Onglet | Rôle |
|---|---|
| **Lisez-moi** | Le mode d'emploi, dans le fichier |
| **Dashboard** | Choisis ton prénom en haut : chiffres clés, à-faire et graphiques s'affichent |
| **Paramètres** | Les prénoms et le versement mensuel (une seule fois) |
| **Actifs** | Une ligne par ETF, action ou crypto |
| **Transactions** | Une ligne à chaque opération. On ajoute, on n'efface jamais |
| **Positions** | Ce que tu détiens, tout le reste se calcule |
| **Historique** | Une ligne par mois et par personne (5 minutes par mois) |
| **Cibles** | Ta cible en % par poche, et combien mettre où au prochain versement |
| **Budget** | Une ligne par mois, le taux d'épargne se calcule |
| **Objectifs** | Tes objectifs chiffrés et datés, la progression se calcule |
| **Journal** | Les décisions d'achat ou de vente |

**Code couleur** : cases jaunes ou en-têtes bleus = tu saisis. En-têtes gris et cases grisées = calculé, ne rien écrire dedans.

**Prix** : la formule GOOGLEFINANCE fonctionne pour la plupart des ETF cotés. Pour la crypto et les ETF non reconnus, tape le prix à la main dans Actifs.

> **Confidentialité** : ce fichier est vide. Une fois rempli, ne le mets jamais dans un dépôt public.

# 16. Tes fichiers privés

Tout ce qui te concerne est dans **`prive/<ton prénom>/`**. Ce dossier est exclu de git (`.gitignore`) : **il ne part jamais sur GitHub**. Chacun garde le sien sur son ordinateur.

| Fichier | Contenu | Qui l'écrit |
|---|---|---|
| `profil.md` | Situation, objectifs, risque, enveloppes, règles perso, rapport à l'argent, avancement de l'apprentissage | Accueil, puis tous les agents |
| `budget.md` | Revenus, dépenses, taux d'épargne, abonnements, épargne de précaution | Conseiller budget |
| `positions.csv` | Tes placements et leur valeur | Analyste |
| `cibles.csv` | Ton allocation cible | Stratège, Analyste |
| `flux.csv` | Tes versements et retraits | Analyste (après ta confirmation) |
| `charte.md` | Ta charte d'investissement | Stratège avec toi |
| `profil-risque.md` | Ton profil de risque, ses alertes et l'historique de tes tests | Accueil, Stratège, Coach |
| `reponses-risque.csv` | Tes réponses au dernier test, lues par le script | Accueil, Stratège |
| `accueil.md` | L'avancement de l'accueil, pour reprendre après une pause | Directeur |
| `journal.md` | Tes décisions, leurs raisons et leurs bilans | Coach |
| `bilans.md` | Tes bilans mensuels et annuels, du plus récent au plus ancien | Analyste |

## Les règles de confidentialité

- Aucun montant, nom ou position réels n'est écrit ailleurs que dans `prive/`.
- Si tu sauvegardes le projet sur GitHub, seules les parties non personnelles partent (agents, fiches, scripts, modèles, guide).
- Les clés API vont dans `.env` (aussi exclu de git), jamais dans le code.

# 17. Ton rythme conseillé

Une heure par semaine suffit. Voici un rythme réaliste. Tu n'as rien à retenir : à chaque moment, dis simplement la phrase indiquée.

## Chaque dimanche (4 minutes)

Lis la newsletter « Ta semaine bourse ». Si elle ne dit rien d'actionnable, tu n'as rien à faire. Si une ligne du tableau « À recopier dans la feuille Veille » t'intéresse, recopie-la dans ton Sheet.

## Chaque mois (15 minutes)

| Quand | Tu dis | Résultat |
|---|---|---|
| Le jour de la paie | « Je viens d'être payé » | Le virement automatique est vérifié, le versement est réparti en ordres concrets |
| Après avoir passé les ordres | « J'ai fait mon versement » | `flux.csv` est mis à jour |
| Fin de mois | « Fais-moi le bilan du mois » | Performance, versements, frais, écarts, décisions hors plan |
| Début de mois | « Mets à jour l'historique des marchés » | La base historique gagne le mois écoulé, le classeur Excel est régénéré |

## Quand tu veux (2 minutes)

- « Quoi de neuf ce matin ? » : le brief du jour, qui conclut presque toujours « rien à faire ».
- Une envie d'agir : « coach, j'ai envie de... » **avant** d'agir.

## Chaque trimestre

- **Audit des abonnements** (Conseiller budget).
- **Mise à jour des données d'indices** de `donnees/` (Analyste).
- **Nouveaux événements marquants** ajoutés à la frise de l'historique, avec leur source (Veilleur).
- **Revue des thèses** de tes lignes satellites (Coach) et **veille structurée** (Veilleur).

## Chaque année

- **Nouveau test de profil de risque** : « refais mon test de risque ».
- **Revue de la charte** (Stratège), et **test de résistance** avant de la valider.
- **Déclaration** en avril : formulaires 3916, 2086, IFU (Stratège).
- **Revue de protection** : bénéficiaires, mutuelle, prévoyance (Conseiller budget).
- **Bilan annuel** et revue des taux fiscaux (le 1er février et le 1er août pour les livrets).
- **Bilans de décision à 12 mois** (Coach).

## Après un événement de vie

Naissance, séparation, perte d'emploi, héritage, achat immobilier, nouveau salaire : dis-le, et demande « on révise ma charte et mon profil ? ». La charte doit être revue tout de suite après un tel événement.

## Ce qui est prévu mais pas encore branché

Le cahier des charges (`docs/CAHIER-DES-CHARGES-MVP.md`) prévoit des évolutions qui **n'existent pas encore** :

- un brief automatique tous les matins à 8 h sur Telegram ;
- des commandes Telegram (`/point`, `/decision`, `/explique`, `/journal`) ;
- un score de santé du portefeuille sur 100 ;
- la lecture directe d'un Google Sheet.

Aujourd'hui, tout se passe en **conversation dans Claude Code**. Quand une de ces fonctions arrive, ce guide est mis à jour (voir le chapitre 19).

# 18. Limites, précautions et dépannage

## Les limites à garder en tête

- **Outil d'aide à la réflexion**, pas un conseil en investissement réglementé. Si tu le proposes à d'autres personnes avec des recommandations personnalisées, tu entres dans le territoire du conseil en investissement (statut CIF, AMF) : à trancher avant d'ouvrir à des tiers.
- **Pas de prédiction.** Si l'assistant semble en faire une, c'est une erreur : reprends-le.
- **Données de marché indicatives** : elles servent de repère, jamais de base unique à une décision.
- **Fiscalité** : les taux sont ceux de 2026 et changent avec les lois de finances. Pour un cas complexe, vérifie avec un professionnel.
- **Fiches « à vérifier »** : certains chiffres n'ont pas encore été confirmés à la source (voir le chapitre 13).
- **Données personnelles** : tu es responsable de leur traitement. Elles restent sur ton ordinateur.

## Dépannage

| Problème | Que faire |
|---|---|
| L'assistant ne te reconnaît pas | Dis « Salut, c'est <ton prénom> » avec le prénom exact de ton dossier `prive/` |
| Un chiffre te paraît faux | Demande « refais le calcul avec le script et montre-moi les données utilisées » |
| Les valeurs de ton portefeuille sont vieilles | Donne-lui les valeurs actuelles, il met à jour `positions.csv` |
| Pas de données de marché ou d'actualité | Relance `python scripts/installer_mcp.py`, redémarre Claude Code, accepte les serveurs |
| Un flux d'actualité ne répond pas | Demande « vérifie l'état des flux », il utilisera la recherche web en attendant |
| Les données d'indices ont plus de 3 mois | Demande « mets à jour les données d'indices » |
| Tu veux repartir de zéro | Renomme ton dossier `prive/<prénom>` : l'accueil se relancera |

## Installer sur un nouvel ordinateur

```bash
git clone https://github.com/magiegenie/assistant-bourse-investissement.git
cd assistant-bourse-investissement
python scripts/installer_mcp.py
```

Le dossier `externe/` (code des autres), `.mcp.json` et `prive/` (tes données) ne sont **jamais versionnés** : tes données ne se retrouvent donc que sur ton ordinateur, à sauvegarder toi-même si tu veux les garder.

# 19. Comment ce guide reste à jour

## Le principe

Ce guide est **vivant**. À chaque nouveauté importante dans le système, il est mis à jour et republié. Tu n'as rien à demander.

## Ce qui déclenche une mise à jour

- un **nouvel agent** ou une nouvelle routine d'un agent ;
- un **nouveau script** de calcul ;
- un **nouveau serveur** de données ou d'actualité ;
- une **nouvelle fiche** ou un nouveau manuel de compétences ;
- un changement de **règle** de fonctionnement (confidentialité, routage, cadre) ;
- une **fonction** qui passe de « prévue » à « disponible » (brief automatique, Telegram...).

## Comment

Les fichiers concernés :

| Fichier | Rôle |
|---|---|
| `docs/GUIDE.md` | Le texte du guide (la source) |
| `docs/Guide-assistant-bourse-investissement.pdf` | Le PDF à lire ou à partager |
| `scripts/generer_guide.py` | Fabrique le PDF à partir du texte |

À chaque nouveauté : on modifie `GUIDE.md`, on ajoute une ligne au journal ci-dessous, on augmente la version, on régénère le PDF avec `python scripts/generer_guide.py`, puis on enregistre et on envoie sur GitHub.

## Journal des versions

| Version | Date | Ce qui change |
|---|---|---|
| **1.4** | 02/11/2026 | Newsletter du dimanche refondue : nouvelle structure en 7 blocs, sources numérotées en bas, tableau des repères de marché, agenda des résultats d'entreprises (tes ETF et les plus suivies), partie « Pour toi », limites de l'édition ; email fabriqué par `newsletter_html.py` avec contrôles automatiques ; routine du dimanche réparée |
| **1.3** | 31/10/2026 | Historique élargi à 24 séries : Dow Jones depuis 1885, Hang Seng, 9 séries OCDE (le minimum de prix sur longue période pour la France, l'Allemagne, les émergents...) ; base de données `marches.sqlite` décrite et visible sur GitHub |
| **1.2** | 31/10/2026 | Nouveau chapitre 14 « L'historique des marchés » : base mensuelle de 14 indices (depuis 1927 à 1994 selon l'indice), macro, frise de 86 événements sourcés, scripts `historique.py` et `maj_historique.py`, classeur `Historique-marches.xlsx` ; chapitres suivants renumérotés |
| **1.1** | 31/10/2026 | Accueil en 6 étapes avec pause et reprise ; nouveau chapitre 3 « Ton profil de risque » (test en 4 dimensions, script `profil_risque.py`, alertes, lien avec le Stratège, l'Analyste et le Coach) ; test de résistance comparé à la perte maximale acceptable ; chapitres renumérotés |
| **1.0** | 31/10/2026 | Première édition du guide : le Directeur et les 5 agents, les 9 scripts, les 3 serveurs MCP, les 9 fiches et les 6 manuels de compétences, le classeur Excel, le rythme conseillé |

## Historique du système

| Date | Étape |
|---|---|
| 30/10/2026 | Version initiale anonymisée de l'assistant (5 agents, fiches, scripts, modèles) |
| 30/10/2026 | Fusion des skills open source dans des manuels de compétences par agent |
| 30/10/2026 | Branchement des flux d'actualité et de la lecture web sur le Veilleur |
| 30/10/2026 | Configuration MCP reproductible : liste des serveurs, installeur, liste des dépôts externes |
| 31/10/2026 | Guide d'utilisation complet en PDF |
| 31/10/2026 | Accueil enrichi et test de profil de risque (capacité, tolérance, besoin, connaissances) |
| 31/10/2026 | Base historique des marchés : 14 indices mensuels, macro, 86 événements sourcés |
| 31/10/2026 | Base historique élargie à 24 séries (Dow Jones depuis 1885, séries OCDE depuis 1955), base SQLite versionnée |
| 02/11/2026 | Newsletter du dimanche : nouvelle structure, générateur HTML, agenda des résultats, chaîne de veille hebdomadaire récupérée |
