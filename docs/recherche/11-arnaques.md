# Recherche 11 : arnaques et fraudes financières

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Statut : **non vérifié**. Rien n'est intégré dans `connaissances/`.
- Fichier de données associé : `arnaques-signaux.csv` (10 lignes, copié tel quel).

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

1. **Arbre de décision (point 15), règle d'interprétation fausse** : le texte dit de s'arrêter si on répond « OUI » aux questions 1, 2, 3, 5, 6, 7, 9, 10 ou « NON » aux questions 4 et 8. C'est inversé : la question 4 est « l'intermédiaire est-il **absent** du registre ? » et la question 8 « les frais sont-ils **flous** ? ». La mauvaise réponse est « OUI » dans les deux cas, comme pour les autres. À corriger à l'intégration : stopper dès un OUI, quelle que soit la question.
2. **Registre PSAN (point 3)** : le régime français des PSAN est en cours de remplacement par l'agrément européen MiCA (prestataires de services sur crypto-actifs). Le rapport ne le mentionne pas dans ce point. À vérifier : à la date de la recherche, la vérification d'une plateforme crypto passe-t-elle encore par le registre PSAN ou par le registre MiCA ?
3. **Chiffres sans lien précis** : « 1 290 inscriptions frauduleuses en 2024 et début 2025 » (ACPR), « 43 sites Forex ajoutés au T3 2025 », « 361 adresses de faux sites de diamants depuis 2017 ». Plausibles mais non vérifiables en l'état. Le rapport cite le site d'ABE Infoservice et de l'AMF en bloc.
4. **Exemple n° 10 (point 14)** : ce n'est pas un message d'arnaque mais un avertissement de l'AMF reformulé. Il reste utile comme rappel (faux articles de presse).
5. **Garanties** : 100 000 € pour les dépôts, 70 000 € pour les titres, 70 000 € pour l'assurance vie (FGAP), délai de remboursement de sept jours ouvrables : chiffres cohérents avec ce que je connais, à confirmer sur les sites des fonds.
6. **« Rendement sans risque autour de 2,5 % à 3 % »** (point 8) : incohérent avec la recherche 10 (Livret A à 1,70 %, inflation à 3,4 %). À aligner.
7. **Manques** : montants de pertes chiffrés des victimes (AMF, Banque de France, Gendarmerie), cas réels documentés avec dates, dispositif de remboursement des fraudes autorisées par la banque (le texte dit que la banque ne rembourse « presque jamais », à nuancer selon l'authentification et la nature de l'opération).
8. Le CSV fournit des liens plus précis que le texte (liste noire AMF, ABE Infoservice, ORIAS, Cybermalveillance).

---

## 1. Comment vérifier si un site financier est sur liste noire en moins de 3 minutes ?

L'AMF et l'ACPR tiennent des listes noires communes (ABE Infoservice) recensant les sites frauduleux. Il suffit de taper le nom du site ou l'e-mail dans le moteur de recherche d'ABE Infoservice pour vérifier s'il a été signalé.

**Détail :** L'ACPR a procédé à 1 290 inscriptions frauduleuses (crédits, livrets, entités) en 2024 et début 2025. Six listes thématiques (Forex, options binaires, biens divers, etc.) sont téléchargeables au format PDF ou CSV.

**Piège fréquent :** L'absence d'un site sur la liste noire ne signifie pas qu'il est légal. Les escrocs créent de nouvelles adresses chaque jour.

**Source(s) :** ABE Infoservice, abe-infoservice.fr, consulté le 30/10/2026.

## 2. Comment s'assurer qu'un courtier ou conseiller a le droit d'exercer en France ?

Un courtier légal doit figurer sur le registre de l'ORIAS (intermédiaires en assurance et banque) ou le registre REGAFI (Banque de France). Une simple recherche par numéro SIREN sur orias.fr ou regafi.fr permet de valider l'agrément.

**Détail :** En France, l'inscription à l'ORIAS est obligatoire pour conseiller ou vendre des produits financiers. Le registre est mis à jour quotidiennement.

**Piège fréquent :** L'escroc utilise le numéro d'agrément d'une vraie société (usurpation d'identité). Il faut toujours appeler le standard de l'entreprise via un numéro trouvé indépendamment.

**Source(s) :** ORIAS, orias.fr, consulté le 30/10/2026.

## 3. Comment vérifier la légalité d'une plateforme de cryptomonnaies ?

En France, toute plateforme offrant des services sur actifs numériques doit être enregistrée comme PSAN (prestataire de services sur actifs numériques) auprès de l'AMF. L'AMF publie le registre officiel des PSAN agréés.

**Détail :** Au 30 octobre 2026, l'AMF met constamment à jour sa liste noire dédiée aux crypto-actifs et produits dérivés non autorisés. Le registre PSAN liste uniquement les acteurs légaux.

**Piège fréquent :** Les escrocs prétendent être basés à l'étranger pour justifier l'absence d'agrément PSAN, ce qui les place hors de tout contrôle protecteur français.

**Source(s) :** AMF, amf-france.org, consulté le 30/10/2026.

## 4. Quels sont les risques liés aux faux courtiers, Forex et options binaires ?

Ces arnaques ciblent les investisseurs avec la promesse de rendements massifs et rapides sur des marchés non régulés. Le client dépose des fonds sur une fausse plateforme de trading dont les graphiques sont manipulés par le fraudeur.

**Détail :** L'AMF et l'ACPR ajoutent continuellement de nouveaux sites à leurs listes (exemple : 43 sites Forex non autorisés ont été ajoutés sur le T3 2025).

**Piège fréquent :** Le client voit des gains fictifs sur son écran, mais lorsqu'il demande un retrait, le faux courtier exige le paiement de taxes ou frais imaginaires.

**Source(s) :** ABE Infoservice, abe-infoservice.fr, consulté le 30/10/2026.

## 5. Comment fonctionne l'usurpation d'identité de conseillers et de sites officiels ?

Les escrocs reprennent le nom, le logo et les numéros d'agrément de vraies banques ou courtiers pour tromper les épargnants. Ils utilisent des adresses e-mail très proches des vraies, par exemple en modifiant simplement le nom de domaine.

**Détail :** L'AMF a identifié et mis sur liste noire de nombreuses fausses adresses e-mail usurpant des sociétés de gestion prestigieuses (ex : prenom.nom@societe-gestion-frauduleuse.com).

**Piège fréquent :** Croire un document PDF portant le logo de l'AMF ou d'une grande banque. Les fraudeurs copient parfaitement la mise en page de ces documents officiels.

**Source(s) :** AMF, amf-france.org, consulté le 30/10/2026.

## 6. En quoi consistent les arnaques aux placements atypiques (diamants, vins, terres rares, SCPI) ?

Ces arnaques misent sur des actifs tangibles et soi-disant refuges, présentés comme décorrélés de la bourse. L'investisseur achète des biens qui n'existent pas ou sont invendables.

**Détail :** L'AMF a inscrit 361 adresses de faux sites de diamants sur sa liste noire depuis la création de celle-ci en 2017. Pour les SCPI, les fraudeurs usurpent l'identité de vraies sociétés pour capter les virements.

**Piège fréquent :** Investir sans vérifier la liste noire « Biens divers » de l'AMF. Tout intermédiaire proposant ces biens doit avoir un numéro d'enregistrement spécifique.

**Source(s) :** AMF, amf-france.org, consulté le 30/10/2026.

## 7. Qu'est-ce qu'une arnaque au recouvrement de pertes (recovery room) ?

Les victimes d'une première escroquerie sont recontactées par de faux avocats, de faux agents de l'AMF ou des agences de cybersécurité fictives. Ils promettent de récupérer les fonds perdus en échange d'honoraires payables d'avance.

**Détail :** Aucun organisme officiel, qu'il s'agisse de l'AMF ou de la police, ne demande jamais de frais pour restituer des fonds volés ou instruire un dossier.

**Piège fréquent :** La victime, désespérée, paie ces frais préalables et perd à nouveau de l'argent de façon définitive.

**Source(s) :** Cybermalveillance, cybermalveillance.gouv.fr, consulté le 30/10/2026.

## 8. Quels sont les signaux d'alerte universels d'une arnaque financière ?

Une escroquerie se repère souvent à un rendement élevé garanti, une urgence artificielle à souscrire, des demandes de paiement en cryptomonnaies, une pression psychologique ou l'absence totale d'agrément vérifiable.

**Détail :** Le couple rendement/risque est une règle mathématique absolue. En octobre 2026, tout rendement garanti supérieur au taux sans risque (autour de 2,5 % à 3 % nets, À VÉRIFIER selon taux directeurs BCE en vigueur) doit éveiller la plus grande méfiance.

**Piège fréquent :** Autoriser le fraudeur à installer un logiciel de partage d'écran (AnyDesk, TeamViewer) soi-disant pour vous assister, ce qui lui donne un accès direct à vos comptes.

**Source(s) :** ABE Infoservice, abe-infoservice.fr, consulté le 30/10/2026.

## 9. Quelles démarches entreprendre immédiatement si j'ai été victime d'une arnaque ?

Il faut cesser tout paiement, rompre le contact avec l'interlocuteur et déposer plainte (commissariat ou plateforme officielle THESEE). Il est indispensable de prévenir sa banque pour demander un rappel de fonds (recall) et de signaler le site sur internet-signalement.gouv.fr (PHAROS).

**Détail :** Le médiateur de l'AMF n'a pas compétence pour intervenir contre des escrocs ou des entités non régulées, il n'intervient que pour des litiges avec des acteurs agréés.

**Piège fréquent :** Garder le silence par sentiment de honte. Plus le signalement à la banque est rapide (idéalement moins de 24 h), plus les chances de bloquer le transfert existent.

**Source(s) :** Service-public.fr, service-public.fr, consulté le 30/10/2026.

## 10. Est-il possible de récupérer les fonds perdus (virement, carte, crypto) ?

Les chances de récupération sont historiquement très faibles. La procédure de « recall » d'un virement échoue le plus souvent car les escrocs vident les comptes destinataires instantanément. Les transactions en cryptomonnaies sont par conception irréversibles.

**Détail :** La révocation d'un virement ne fonctionne que si la banque de réception n'a pas encore crédité le compte du fraudeur. Pour la carte bancaire, la procédure de rétrofacturation (chargeback) exige des conditions très strictes.

**Piège fréquent :** Croire que la banque remboursera systématiquement. La banque ne rembourse une arnaque (où le client a authentifié le virement) que si une faille de sécurité majeure imputable à l'établissement est démontrée par la justice.

**Source(s) :** Banque de France, banque-france.fr, consulté le 30/10/2026.

## 11. Comment sécuriser efficacement l'accès à mes comptes d'investissement ?

Il faut utiliser un mot de passe complexe et unique pour chaque compte financier. Activez systématiquement l'authentification à double facteur (2FA) via une application sécurisée plutôt que par simple SMS, plus vulnérable.

**Détail :** Le SMS peut être contourné par le « SIM swapping » (le vol de votre ligne téléphonique). Méfiez-vous également du « vishing » (le fraudeur appelle, se fait passer pour la banque et demande le code de validation reçu).

**Piège fréquent :** Lire un code de sécurité à voix haute au téléphone. Un véritable conseiller bancaire n'en a techniquement jamais besoin.

**Source(s) :** Cybermalveillance, cybermalveillance.gouv.fr, consulté le 30/10/2026.

## 12. Que couvre la garantie des dépôts bancaires et à quelle hauteur ?

Le Fonds de garantie des dépôts et de résolution (FGDR) protège obligatoirement les sommes déposées sur les comptes courants et les livrets bancaires de tous les établissements agréés en France.

**Détail :** La couverture monte à 100 000 euros maximum par client et par banque. Le délai légal de remboursement en cas de faillite est de sept jours ouvrables.

**Piège fréquent :** Penser que cette protection légale s'applique aux comptes détenus chez des courtiers non régulés. Seuls les établissements agréés cotisent au FGDR.

**Source(s) :** FGDR, garantiedesdepots.fr, consulté le 30/10/2026.

## 13. Comment sont protégés mes titres financiers et mon assurance vie en cas de faillite ?

Le FGDR garantit vos instruments financiers (actions ou ETF sur un PEA/CTO) jusqu'à 70 000 euros par client. Pour les fonds placés en assurance vie, c'est le Fonds de garantie des assurances de personnes (FGAP) qui offre une protection similaire de 70 000 euros.

**Détail :** Ces plafonds s'appliquent par client et par établissement. Ces mécanismes protègent uniquement contre la faillite de l'intermédiaire, et non contre les baisses naturelles des marchés boursiers.

**Piège fréquent :** Confondre risque de marché (normal) et fraude. Aucune de ces garanties ne couvre les pertes si vous avez volontairement viré vos fonds à une société écran frauduleuse.

**Source(s) :** FGAP (fgap.fr) et FGDR (garantiedesdepots.fr), consultés le 30/10/2026.

## 14. Quels sont dix exemples de messages d'arnaques réalistes à éviter ?

1. « Placez votre épargne à 6 % net garanti, sans risque, dans nos parkings. » (rendement garanti décorrélé de l'économie)
2. « Opportunité réservée à nos 50 premiers clients, clôture ce soir. » (urgence artificielle)
3. « Vous devez payer 15 % de frais de dossier pour débloquer les 5 000 euros de votre compte de trading. » (demande de paiement pour retirer son dû)
4. « Achetez du Bitcoin sécurisé via un virement sur ce compte basé à Chypre. » (absence d'agrément français)
5. « Bonjour, je suis Marc de votre banque, votre compte est piraté, validez l'annulation de l'opération. » (vishing classique)
6. « Nouveau produit défiscalisé de l'État, ouvrez votre Livret Épargne Vert à 5,5 %. » (imitation d'un livret réglementé)
7. « Téléchargez ce logiciel pour que notre conseiller technique configure votre portefeuille. » (prise de contrôle de la machine)
8. « Nous avons retrouvé les auteurs de votre dernière arnaque. Payez 500 euros pour lancer la procédure de remboursement. » (recovery room)
9. « Projet crypto ultra-secret, potentiel de x100 dans les 48 h. Investissez vite. » (pump and dump sur les réseaux)
10. « L'AMF alerte sur la recrudescence de faux articles de presse vantant des méthodes miracles pour s'enrichir rapidement. » (fausses recommandations imitant des articles de médias connus)

**Détail :** Ces approches correspondent aux modes opératoires documentés par le régulateur pour contourner la méfiance des épargnants.

**Piège fréquent :** Surestimer ses propres connaissances. Les escrocs adaptent le niveau de technicité de leur discours en fonction de leur cible.

**Source(s) :** AMF et ABE Infoservice, abe-infoservice.fr, consulté le 30/10/2026.

## 15. Quel arbre de décision en 10 questions utiliser pour juger une offre d'investissement ?

1. Le produit offre-t-il un rendement élevé tout en affirmant qu'il n'y a « aucun risque » ?
2. Le nom de l'intermédiaire figure-t-il sur les listes noires de l'AMF ou de l'ACPR ?
3. Le conseiller vous presse-t-il de prendre une décision immédiatement ?
4. L'intermédiaire financier est-il absent du registre de l'ORIAS ou du REGAFI ?
5. L'adresse e-mail du conseiller comporte-t-elle des anomalies (fautes, nom de domaine étrange) ?
6. L'IBAN de destination du virement est-il localisé à l'étranger alors que la société affirme être française ?
7. Avez-vous reçu la consigne de télécharger un logiciel de contrôle à distance sur votre ordinateur ?
8. Les frais ou les mécanismes de génération de rendement de ce produit sont-ils flous ou incompréhensibles pour vous ?
9. Demande-t-on de payer votre investissement directement en cryptomonnaies ou en cartes cadeaux ?
10. S'agit-il d'un démarchage agressif (téléphone, réseaux sociaux) que vous n'avez jamais sollicité ?

**Détail :** Si vous répondez « OUI » à l'une des questions 1, 2, 3, 5, 6, 7, 9, 10 ou « NON » à la 4 et 8, il est impératif de stopper toute démarche. *(Voir la note de relecture n° 1 : règle inversée pour les questions 4 et 8.)*

**Piège fréquent :** Se contenter des promesses rassurantes du commercial sans vérifier l'information par une recherche indépendante.

**Source(s) :** AMF, amf-france.org, consulté le 30/10/2026.

---

## Ce qui a changé récemment

1. Une hausse massive des usurpations d'identité visant les grandes sociétés de gestion prestigieuses a été documentée au cours des 24 derniers mois.
2. L'encadrement strict des influenceurs financiers par le législateur français (loi de 2023) a clarifié leurs obligations de transparence sur les partenariats rémunérés.
3. Les arnaques téléphoniques se sont complexifiées grâce aux outils de deepfake vocal et au masquage des numéros de téléphone (spoofing) pour imiter le standard des banques.

## Ce que je n'ai pas pu trancher

1. Les statistiques officielles et publiques sur le montant exact récupéré par la procédure de rétrofacturation (chargeback) en France sont très parcellaires.
2. Le volume financier précis des pertes indirectes liées au vol pur de données personnelles (et leur revente sur le dark web) n'est pas quantifié avec exactitude par une source primaire.

## Sources utilisées

1. Autorité des marchés financiers (AMF), listes noires et alertes : https://www.amf-france.org/fr/espace-epargnants/proteger-son-epargne/listes-noires-et-mises-en-garde
2. ABE Infoservice (ACPR et AMF), prévention arnaques : https://www.abe-infoservice.fr
3. Fonds de garantie des dépôts et de résolution (FGDR) : https://www.garantiedesdepots.fr
4. Fonds de garantie des assurances de personnes (FGAP) : https://www.fgap.fr
5. Registre ORIAS : https://www.orias.fr
6. Registre REGAFI (Banque de France) : https://www.regafi.fr
7. Assistance aux victimes de cybermalveillance : https://www.cybermalveillance.gouv.fr/
