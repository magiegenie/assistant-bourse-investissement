# Recherche 07 : comportement et psychologie de l'investisseur

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichier de données associé : `etudes-comportement.csv`. Le fichier n'a pas été téléchargé : je l'ai recréé à partir du code Python que l'autre IA a fourni dans sa réponse (mêmes 8 lignes, mêmes colonnes).

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

1. **Chiffre contradictoire sur l'AMF et mars 2020** : le texte dit « plus de 150 000 nouveaux comptes actifs en quelques semaines », le CSV « plus de 1,5 million de nouveaux investisseurs depuis 2019 ». Ce sont deux périmètres différents ou une erreur. À vérifier dans la cartographie de l'AMF.
2. **Benartzi et Thaler (point 5)** : les chiffres « 70 % d'actions avec une évaluation annuelle, 40 % avec une évaluation mensuelle ou quotidienne » ne correspondent pas à ce que je connais de l'article. À vérifier dans le texte original.
3. **Fréquence de consultation** : le rapport recommande une à deux fois par an. La fiche F du dépôt (point 35) dit « une fois par semaine maximum ». À arbitrer.
4. **Effet de disposition « 50 % trop tôt »** : chiffre sans source dans le texte. Shefrin et Statman décrivent la tendance, pas ce chiffre à ma connaissance.
5. **Barber et Odean** : l'écart 11,4 % contre 17,9 % concerne le groupe de ménages le plus actif. Le texte le formule correctement.
6. **« Frais de transaction plafonnés réglementairement à 0,5 % par ordre »** (point 2) : je ne connais pas ce plafond. Même affirmation que dans la recherche 02. À vérifier.
7. **« Certificat de l'influence responsable en finance » de l'AMF** : je ne peux pas confirmer que ce certificat existe sous ce nom. La loi n° 2023-451 sur l'influence commerciale existe bien.
8. **« 9 fois sur 10 les performances promises sont fausses »** : chiffre non sourcé, que l'autre IA signale elle-même comme « À VÉRIFIER ».
9. **Scripts de coaching (point 9)** : bonne base pour le Coach, mais trois formulations sont à retoucher à l'intégration pour respecter les règles de `coach.md` (« jamais acheter ou vendre ») : « maintenir tes versements te permet d'acheter à un meilleur prix qu'hier » (prédiction implicite), « laisser courir les gains » comme contre-mesure à l'effet de disposition (consigne d'action), « budget découverte de maximum 5 % » (proche d'une recommandation).
10. **Parties demandées mais absentes** : chiffres Morningstar et DALBAR année par année, données de ventes de particuliers en 2008 et 2022 chiffrées, grille de seuils d'alerte du stress financier.

---

## 1. Pourquoi mon portefeuille gagne-t-il moins que les fonds dans lesquels j'investis ?

**Réponse courte :** L'écart de comportement (« behavior gap ») correspond au manque à gagner subi par l'investisseur à cause de ses propres décisions émotionnelles. En achetant au plus haut par euphorie et en vendant au plus bas par peur, il ampute son rendement réel par rapport à une stratégie passive.

**Détail :** Le rapport « Mind the Gap 2024 » de Morningstar (données clôturées au 31 décembre 2023) chiffre cette perte à 1,1 point de pourcentage par an sur 10 ans pour les investisseurs en fonds et ETF mondiaux. L'étude DALBAR (QAIB) cite régulièrement un écart historique plus élevé (souvent supérieur à 3 %), mais sa méthodologie de calcul des flux entrants et sortants est fortement critiquée pour surestimer le gap. À l'inverse, Vanguard estime dans son rapport « Advisor's Alpha » (mis à jour en 2025) que le cadrage comportemental opéré par un coach financier permet de générer entre 1,5 % et 2 % de rendement net annuel en évitant les erreurs de timing.

**Piège fréquent ou erreur courante :** Croire que l'on possède un don pour le « market timing » (anticiper les points hauts et bas du marché).

**Source(s) :** Morningstar (https://www.morningstar.com/personal-finance/fund-investors-who-kept-it-simple-captured-more-return, août 2024), Vanguard (https://advisors.vanguard.com, 2025).

## 2. Vais-je gagner plus en multipliant mes achats et ventes au quotidien ?

**Réponse courte :** Non. Le trading actif (« sur-trading ») détruit systématiquement la valeur pour l'immense majorité des particuliers. Les frais de courtage s'accumulent et la sélection des points d'entrée s'avère souvent perdante face au marché global.

**Détail :** L'étude universitaire de référence de Barber et Odean (« Trading Is Hazardous to Your Wealth », 2000) portant sur 66 465 foyers américains entre 1991 et 1996 montre que si le marché rapportait 17,9 % par an, les investisseurs les plus actifs stagnaient à 11,4 % net de frais. En France, l'AMF a dénombré 1,3 million de particuliers actifs en bourse en 2023. Les publications de l'AMF prouvent de manière répétée que sur les instruments à fort levier (CFD, Forex), entre 73 % et 89 % des particuliers perdent du capital. L'hyperactivité sur des portefeuilles classiques type PEA ou CTO génère des frais de transaction (plafonnés réglementairement à 0,5 % par ordre en ligne, mais destructeurs à long terme).

**Piège fréquent ou erreur courante :** Confondre « être actif » et « être rentable ». En bourse, l'inaction est très souvent la stratégie la plus performante.

**Source(s) :** Journal of Finance / Barber & Odean (https://onlinelibrary.wiley.com, avril 2000), AMF (https://www.amf-france.org, 2023).

## 3. Quels sont les biais psychologiques qui faussent mes décisions d'investissement ?

**Réponse courte :** Le cerveau humain recourt à des raccourcis cognitifs utiles pour la survie, mais désastreux en finance. Les identifier permet de concevoir des mécanismes de défense mécaniques (charte, ordres automatiques) pour protéger son épargne.

**Détail :**

- **Aversion aux pertes** : douleur d'une perte de 1 000 euros deux fois plus intense que la joie d'un gain équivalent (Kahneman et Tversky, 1979). Alerte : « J'attends que ça revienne à zéro pour vendre ». Contre-mesure : automatisation.
- **Ancrage** : fixation sur un prix passé. Alerte : « C'est bradé, ça valait le double ». Contre-mesure : évaluer l'actif à son prix du jour.
- **Excès de confiance** : surestimer ses compétences. Alerte : « Le marché se trompe, l'action va exploser ». Contre-mesure : comparer son portefeuille à l'indice MSCI World.
- **Biais de récence** : projeter la situation immédiate vers l'avenir. Alerte : « Le marché baisse depuis 5 jours, je vends tout ». Contre-mesure : analyser les graphiques sur 10 ans.
- **Effet de disposition** : vendre les gagnants 50 % trop tôt et conserver les perdants trop longtemps (Shefrin et Statman, 1985). Alerte : « Je prends ma plus-value pour sécuriser ». Contre-mesure : laisser courir les gains.
- **Biais de confirmation** : ne lire que ce qui conforte sa thèse. Alerte : « J'ai trouvé un article qui valide exactement mon achat ». Contre-mesure : technique du « pré-mortem ».
- **FOMO** : peur de manquer l'opportunité. Alerte : « Tout le monde s'enrichit avec ça ». Contre-mesure : imposer la règle des 72 heures.
- **Effet de troupeau** : suivre la masse aveuglément. Alerte : « Mon entourage vient d'acheter ce titre ». Contre-mesure : respect de la charte d'investissement personnelle.
- **Comptabilité mentale** : traiter l'argent différemment selon sa source (Thaler, 1985). Alerte : « C'est l'argent d'un pari, je peux le risquer ». Contre-mesure : considérer le patrimoine global.
- **Illusion de contrôle** : penser influencer le hasard (Langer, 1975). Alerte : « Mon analyse graphique à 5 minutes est infaillible ». Contre-mesure : accepter l'incertitude.

**Piège fréquent ou erreur courante :** Penser que l'on est immunisé contre ces biais simplement parce qu'on vient d'en lire la définition.

**Source(s) :** Econometrica (Kahneman et Tversky, 1979), Journal of Finance (Shefrin et Statman, 1985).

## 4. Comment réagissent réellement les particuliers lors d'un effondrement du marché ?

**Réponse courte :** L'idée que les particuliers vendent toujours dans la panique est nuancée. Lors des crises récentes, les investisseurs particuliers français se sont massivement positionnés à l'achat pour profiter des baisses de valorisations.

**Détail :** Lors du krach de mars 2020 lié à la Covid-19, l'AMF a relevé un afflux massif avec plus de 150 000 nouveaux comptes actifs ouverts en quelques semaines. Contrairement aux fonds institutionnels qui vendaient pour trouver de la liquidité, les particuliers ont été des acheteurs nets. La situation contraste avec fin 2008 où la décollecte sur actions en direct s'était fait ressentir au profit des fonds euros. Lors de la baisse de 2022, les flux vers les ETF sont restés positifs en France, démontrant une résilience nouvelle liée aux plans d'investissement programmés.

**Piège fréquent ou erreur courante :** Vendre au plus bas d'un krach, ce qui matérialise définitivement une moins-value latente.

**Source(s) :** AMF, Cartographie des marchés et des risques (https://www.amf-france.org, juillet 2020 et actualisations 2023).

## 5. À quelle fréquence dois-je consulter l'application de mon courtier ?

**Réponse courte :** Le moins possible, idéalement une à deux fois par an. Une consultation excessive augmente artificiellement la perception du risque à cause de la volatilité quotidienne, poussant l'investisseur à sous-investir en actions.

**Détail :** L'étude de Benartzi et Thaler (1995) sur la « myopie face aux pertes » démontre l'impact de la fréquence de vérification. Si un investisseur évalue son portefeuille annuellement, il tolère psychologiquement d'avoir environ 70 % de son patrimoine en actions. S'il consulte ses lignes tous les mois ou tous les jours, il subit l'aversion aux pertes liée aux micro-variations naturelles du marché et abaisse son allocation en actions à près de 40 %.

**Piège fréquent ou erreur courante :** Conserver l'application de son courtier sur la première page de son smartphone avec les notifications activées.

**Source(s) :** Quarterly Journal of Economics / Benartzi et Thaler (https://academic.oup.com/qje, 1995).

## 6. Comment me protéger de mes propres émotions grâce à des outils ?

**Réponse courte :** En mettant en place des systèmes automatisés et un cadre écrit avant même d'investir le premier euro. La clé est de séparer le moment de l'analyse (à froid) du moment de l'exécution.

**Détail :**

- **Charte d'investissement** : document d'une page fixant formellement l'allocation cible, les supports d'investissement (ETF, obligations) et les conditions de vente strictes.
- **Règle des 24-72 h** : ne jamais exécuter un ordre d'achat spontané (délai de réflexion imposé).
- **Pré-mortem** : se projeter dans 5 ans, acter que l'investissement a échoué, et en lister les causes rationnelles à l'avance.
- **Journal de décision** : noter (date, actif, thèse de départ, émotion ressentie) pour chaque mouvement.
- **Ordre à l'avance** : utiliser des ordres à cours limité pour que les transactions s'exécutent seules hors écran.
- **Automatisation des versements (DCA)** : programmer des prélèvements fixes chaque mois vers le PEA ou l'assurance vie pour neutraliser le risque de timing.

**Piège fréquent ou erreur courante :** Rédiger ses règles de conduite ou sa charte pendant une tempête boursière, sous l'emprise du stress.

**Source(s) :** Daniel Kahneman, « Thinking, Fast and Slow » (2011).

## 7. Dois-je suivre les conseils des influenceurs sur les réseaux sociaux ?

**Réponse courte :** Avec la plus grande prudence. Les réseaux sociaux amplifient l'effet de groupe (FOMO) et regorgent de conflits d'intérêts ou d'arnaques, ciblant tout particulièrement les débutants.

**Détail :** Le système du « pump and dump » (faire acheter en masse un titre illiquide ou une crypto par une communauté pour le faire monter, puis revendre au prix fort) est très courant. Les signaux de trading payants ou garanties de rendement sont illégaux en France sans le statut de Conseil en Investissements Financiers (CIF) ou de Prestataire de Services d'Investissement. 9 fois sur 10 « À VÉRIFIER », les performances promises sur les groupes privés sont fausses ou impossibles à reproduire avec les frais réels.

**Piège fréquent ou erreur courante :** Confondre un contenu divertissant, rassurant ou visuellement professionnel avec un conseil financier agréé.

**Source(s) :** Loi n° 2023-451 visant à encadrer l'influence commerciale / AMF (https://www.amf-france.org, 2023).

## 8. Comment éviter que la bourse génère du stress ou de l'anxiété ?

**Réponse courte :** Le stress financier indique que l'allocation d'actifs ne correspond pas à la tolérance au risque réelle ou que le matelas de sécurité n'est pas suffisant. L'argent indispensable à court terme ne doit pas être exposé aux marchés.

**Détail :** Les indicateurs d'alerte cliniques sont clairs : consultation des cours pendant la nuit, insomnies, irritabilité au moment des baisses de marché. Le franchissement de ces seuils démontre que l'investisseur s'est surexposé. La recommandation universelle est de maintenir une épargne de précaution équivalente à 3 à 6 mois de charges fixes sur un Livret A ou LDDS, et de ne placer en bourse que des sommes bloquées mentalement pour 5 à 10 ans minimum.

**Piège fréquent ou erreur courante :** Surestimer sa propre tolérance au risque pendant des mois de marché haussier (bull market), ce qui conduit à paniquer à la première grosse correction.

**Source(s) :** Banque de France, portail d'éducation financière (https://www.mesquestionsdargent.fr, consulté en 2026).

## 9. Comment le coach (ou l'IA) doit-il structurer ses échanges face aux émotions ?

**Réponse courte :** Le coach (humain ou IA) ne fournit jamais de conseils d'achats précis, mais utilise un questionnement maïeutique. Il doit valider l'émotion ressentie avant d'utiliser la logique pour recadrer les décisions de l'investisseur.

**Détail :**

1. **Envie d'acheter un titre qui monte fort**
   - Questions : Depuis quand le suis-tu ? Quelle est sa valorisation réelle ? Que fais-tu s'il perd 30 % demain ? Respecte-t-il la charte ? Pourquoi acheter aujourd'hui ?
   - Pièges : interdire sèchement, dire que c'est trop tard, prédire une chute.
   - Phrase : « L'ascension de ce titre est impressionnante. Assurons-nous que cela rentre dans ton plan à long terme. Prenons 72h pour poser les chiffres. »
2. **Envie de vendre après -20 %**
   - Questions : As-tu besoin de ces liquidités ce mois-ci ? Les fondamentaux ont-ils changé ? Aurais-tu vendu pour une baisse de 2 % ? Sais-tu quand tu rachèteras ? Que prévoyait ta charte ?
   - Pièges : promettre un rebond rapide, juger la panique, banaliser la perte.
   - Phrase : « Je comprends ton inconfort. Reprenons ensemble ta charte rédigée à froid pour vérifier si cette volatilité était budgétée. »
3. **FOMO sur une cryptomonnaie**
   - Questions : Quel pourcentage de ton patrimoine cela représente-t-il ? Es-tu prêt psychologiquement à perdre l'intégralité ? As-tu compris la technologie derrière ? Le matelas de sécurité est-il plein ? Connais-tu la fiscalité à la sortie ?
   - Pièges : traiter le projet d'arnaque d'office, avoir un ton paternaliste, nier l'engouement.
   - Phrase : « Le potentiel est tentant. Si tu souhaites allouer un budget "découverte" de maximum 5 % de ton capital, mettons en place un cadre strict. »
4. **Certitude après un « bon tuyau »**
   - Questions : Qui t'a donné l'information et quel est son intérêt ? Si c'est public, pourquoi n'est-ce pas déjà intégré dans le prix par le marché ? Quel est le pire scénario ? As-tu lu les documents financiers ? S'agit-il d'argent vital ?
   - Pièges : se moquer de la source, jouer à l'avocat, bloquer sans écouter la thèse.
   - Phrase : « Ce tuyau semble séduisant en apparence. Faisons un petit exercice de "pré-mortem" avant de valider quoi que ce soit. »
5. **Envie d'arrêter les versements (DCA)**
   - Questions : As-tu subi une perte de revenus ? Est-ce la peur des annonces économiques ? Sais-tu que couper le DCA tue l'effet des intérêts composés ? Quel signal attendras-tu pour reprendre ? Ton objectif initial est-il caduc ?
   - Pièges : faire culpabiliser sur le manque de rigueur, forcer psychologiquement le versement, oublier l'impact de l'inflation.
   - Phrase : « Le contexte macroéconomique est stressant, c'est vrai. Mais souviens-toi que maintenir tes versements aujourd'hui te permet d'acheter des parts à un meilleur prix qu'hier. »
6. **Euphorie après un gain massif**
   - Questions : Penses-tu que ce gain est lié à ta compétence ou à une chance de marché ? Ta tolérance au risque a-t-elle changé ? As-tu pris tes bénéfices ? As-tu consigné l'opération dans le journal ? Quel est ton prochain palier ?
   - Pièges : briser la dynamique, s'attribuer le mérite, encourager implicitement le levier.
   - Phrase : « Félicitations, c'est une très belle opération. Le vent est favorable, c'est le moment idéal pour rééquilibrer ton portefeuille et sécuriser intelligemment. »
7. **Culpabilité après une erreur coûteuse**
   - Questions : Quelle leçon concrète et opérationnelle as-tu tirée ? Ton matelas d'urgence est-il préservé ? Peux-tu l'écrire dans ton journal ? Que vas-tu automatiser pour ne pas recommencer ? Cette perte impacte-t-elle ton niveau de vie actuel ?
   - Pièges : lancer un « je te l'avais bien dit », dramatiser, ou à l'inverse minimiser en disant « ce n'est que de l'argent ».
   - Phrase : « Ce type d'erreur fait partie intégrante du parcours d'investisseur. Considérons cette perte comme des frais de scolarité : actons-la, et améliorons ton processus. »

**Piège fréquent ou erreur courante :** Croire qu'apporter des chiffres et des statistiques rationnelles suffit à calmer un biais émotionnel.

**Source(s) :** Méthodologies extraites de Vanguard « Advisor's Alpha » (https://advisors.vanguard.com, 2025).

---

## Ce qui a changé récemment

- **Démocratisation technologique du DCA** : l'arrivée de néo-courtiers (Trade Republic, Scalable Capital) proposant des versements automatisés gratuits sur des ETF a massivement modifié le comportement des particuliers français depuis 2024. Le « behavior gap » tend à se réduire sur ces cohortes car les investisseurs n'ont plus à timer le marché manuellement chaque mois.
- **Régulation des « finfluenceurs »** : depuis le milieu de l'année 2023, la loi française encadrant l'influence commerciale interdit la promotion de produits financiers complexes non régulés. L'AMF a également systématisé le « Certificat de l'influence responsable en finance », créant un net recul des pratiques de pump and dump grand public sur le marché français en 2025 et 2026.

## Ce que je n'ai pas pu trancher

- Le volume chiffré exact perdu par les particuliers spécifiquement en France sur les supports « sains » (PEA et CTO sur actions/ETF). Si l'AMF fournit les données exactes du désastre que représentent les CFD/Forex (où la vaste majorité perd), le chiffre précis du « behavior gap » sur les enveloppes fiscales françaises de base n'est pas mesuré publiquement par l'État. L'estimation s'appuie donc nécessairement sur les études nord-américaines et mondiales des grands émetteurs (comme Morningstar et Vanguard).
- Le chiffre exact du taux de fraude des « signaux de trading » vendus sur les réseaux sociaux. Le chiffre symbolique de 9/10 (« À VÉRIFIER ») est un consensus issu de la prévention contre les arnaques financières, mais il n'existe pas d'étude primaire validée de l'AMF ou de la Répression des fraudes mesurant le pourcentage décimal exact de faux signaux.

## Sources utilisées

- Morningstar, Mind the Gap 2024: Reviewing Investor Returns (octobre 2024) : https://www.morningstar.com/personal-finance/fund-investors-who-kept-it-simple-captured-more-return
- Vanguard, Advisor's Alpha (2025) : https://advisors.vanguard.com/insights/article/putting-a-value-on-your-value-quantifying-vanguard-advisors-alpha
- B. Barber et T. Odean, Trading Is Hazardous to Your Wealth, Journal of Finance (avril 2000) : https://onlinelibrary.wiley.com
- S. Benartzi et R. Thaler, Myopic Loss Aversion and the Equity Premium Puzzle, Quarterly Journal of Economics (1995) : https://academic.oup.com/qje/article-abstract/110/1/73/1892809
- AMF, Cartographie des marchés et des risques (2020) : https://www.amf-france.org/sites/institutionnel/files/2020-07/cartographie-2020-consolidee.pdf
- AMF, Tableau de bord des investisseurs particuliers actifs (2023) : https://www.amf-france.org/fr/actualites-publications/publications/statistiques/tableau-de-bord-des-investisseurs-particuliers-actifs
- Banque de France, portail Mes questions d'argent : https://www.mesquestionsdargent.fr/
- D. Kahneman et A. Tversky, Prospect Theory: An Analysis of Decision under Risk, Econometrica (1979).
- H. Shefrin et M. Statman, The Disposition to Sell Winners Too Early and Ride Losers Too Long, Journal of Finance (1985).
