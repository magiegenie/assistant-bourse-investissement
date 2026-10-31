# Idées d'automatisations

Réserve d'idées, rien n'est encore construit ici sauf mention « en place ». Chaque idée indique ce qui la déclenche, ce qu'elle fait, ce qu'il faut pour la brancher, et un effort estimé (petit, moyen, gros). Règle commune : une automatisation peut lire, calculer, prévenir et préparer ; elle ne passe jamais d'ordre de bourse et ne déplace jamais d'argent toute seule.

Outils disponibles ou possibles : tâches planifiées Claude Code (cloud), GitHub Actions, connecteurs Gmail, Google Drive et Google Calendar, Google Sheets (formules, GOOGLEFINANCE, Apps Script), serveurs MCP locaux (financial-data, actualite-flux, lecture-web), notifications push du téléphone, scripts du dossier `scripts/`.

## Déjà en place
- **Collecte de l'actualité du dimanche** (GitHub Actions) : titres de la semaine depuis `donnees/sources.csv`, vérification des sources, tests. Active une fois la branche fusionnée dans `main`.
- **Newsletter du dimanche 18 h 47** (tâche planifiée) : à brancher sur Gmail, Google Drive et le dépôt.

## Chaque jour
- **Alerte de grosse baisse seulement** : si le portefeuille ou le MSCI World perd plus de 7 % sur une semaine, une notification calme avec ton test de résistance en euros et la phrase de ta charte (« je verse quoi qu'il arrive »). Rien les autres jours, pour moins regarder les marchés (fiche F). Besoin : prix via financial-data ou GOOGLEFINANCE, notification push. Moyen.
- **Brief du matin facultatif** en 5 lignes, désactivé par défaut. Petit.
- **Surveillance des listes noires AMF** : si un nom présent dans tes onglets Idées ou Journal apparaît dans une mise en garde AMF, alerte immédiate. Besoin : flux AMF, lecture du Sheet. Moyen.

## Chaque semaine
- **Newsletter enrichie** : ajouter ta valeur de la semaine, l'écart à tes cibles et le compte à rebours de tes objectifs. Petit, une fois la lecture du Sheet branchée.
- **Écriture automatique dans l'onglet Veille** : via une petite Apps Script dans le Sheet qui lit le digest `docs/veille/` publié sur GitHub. Moyen.
- **Rappel des idées en attente** : chaque dimanche, les idées de l'onglet Idées arrivées à 30 jours, avec la question « toujours envie ? ». Petit.
- **Rapport de santé du système** : sources mortes, tests en échec, données d'indices trop vieilles, envoyé seulement s'il y a un problème. Petit (les vérifications existent déjà).

## Chaque mois
- **Le jour de la paie** (le 5 par défaut) : un email ou une notification « ton versement de 500 € : 280 € sur le World, 220 € sur l'Europe », calculé par `allocation.py`, avec un bouton de réponse « fait ». Besoin : tâche planifiée, Gmail ou push. Moyen.
- **Lecture des relevés du courtier dans Gmail** : repérer l'avis d'opéré ou le relevé mensuel, en extraire les achats et les passer dans `saisie.py`, puis demander confirmation. Plus aucune saisie. Besoin : Gmail, un format de relevé par courtier. Gros.
- **Bilan mensuel automatique** le 1er : `bilan_mensuel.py` mis en forme et envoyé, avec une seule action proposée. Moyen.
- **Ligne Historique ajoutée seule** dans le Sheet à la fin du mois (valeur, total versé, indice). Besoin : Apps Script ou écriture Drive. Moyen.
- **Rappel budget** : si le taux d'épargne du mois tombe sous 20 %, un message bienveillant avec l'écart en euros. Petit.

## Chaque trimestre
- **Rafraîchissement des compositions d'indices** (`donnees/indices-*.csv`) depuis les fiches MSCI et émetteurs, avec date et source. Besoin : réseau ouvert (GitHub Actions). Moyen.
- **Revérification du catalogue d'ETF** (`donnees/etf-pea.csv`) : frais, ISIN, nouveaux ETF moins chers ; alerte si un de tes ETF a un équivalent nettement moins cher. Moyen.
- **Audit des abonnements** : à partir des prélèvements repérés dans les emails de facture, liste et coût annuel. Gros.
- **Banc d'essai des agents relancé** (`tests/scenarios.md`) pour vérifier qu'aucune modification n'a dégradé les conseils. Moyen.

## Chaque année
- **Calendrier fiscal dans Google Calendar** : ouverture de la déclaration, dates limites par zone, rappel IFU et formulaires 3916 ou 2086 si concernés. Besoin : Calendar. Petit.
- **Mise à jour des taux fiscaux** au 1er janvier : recherche des nouveaux taux, mise à jour proposée de `scripts/fiscalite.py` et de la fiche C, avec les sources. Moyen.
- **Révision du Livret A** (1er février, 1er août) : nouveau taux noté, rendement réel recalculé. Petit.
- **Anniversaires d'enveloppes** : rappel quand le PEA atteint 5 ans ou l'assurance vie 8 ans, avec ce que ça change. Petit.
- **Bilan annuel et revue de la charte** en décembre, avec le coût des décisions hors plan de l'année. Moyen.

## Sur événement
- **Prime ou salaire inhabituel** détecté dans un email de paie : proposition « 50 % pour l'avenir, 50 % pour toi ». Gros.
- **Poche hors limite** (écart de plus de 10 points, crypto au-dessus du plafond) : alerte avec le plan de rééquilibrage de `reequilibrage.py`. Moyen.
- **Objectif en retard** : si la trajectoire de l'apport ou d'un autre objectif décroche, message du Stratège avec le versement nécessaire recalculé. Moyen.
- **Annonce d'une banque centrale** dans tes jours de réunion (`donnees/calendrier-recurrent.csv`) : explication courte le soir même par le Veilleur. Moyen.
- **Achat impulsif détecté** : une opération « hors plan » saisie déclenche automatiquement la fiche Journal et le bilan à 3 mois. Petit.
- **Bilan à 3 mois d'une décision** : rappel à la date prévue dans le Journal, avec le résultat calculé. Petit.

## Liens entre outils
- **Google Sheet et assistant dans les deux sens** : le Sheet reste la saisie, l'assistant le lit (déjà possible via export) puis, avec Apps Script ou un connecteur Sheets, y écrit Historique, Veille et bilans.
- **Google Calendar** : versements, réunions BCE et Fed qui te concernent, échéances fiscales, revues trimestrielles, bilans de décisions.
- **Gmail** : newsletter, alertes rares, lecture des relevés et factures, brouillons de messages à ta banque ou ton courtier (jamais envoyés sans toi).
- **Google Drive** : archive mensuelle des bilans en PDF, classeur, calendrier, catalogue ETF.
- **Téléphone** : notifications seulement pour ce qui demande une action ; tout le reste attend la newsletter.
- **Telegram ou messagerie** (idée du cahier des charges) : parler à l'assistant depuis le téléphone (« paie », « bilan ») sans ouvrir l'ordinateur. Gros.
- **Courtier** : aucun courtier grand public français n'offre d'API simple ; l'export CSV ou les emails restent la voie réaliste.

## Pour le couple ou l'associé
- **Point argent mensuel** préparé automatiquement pour deux (chacun ses chiffres, partage seulement si autorisé dans les profils).
- **Objectifs communs** suivis dans un onglet partagé, sans montrer les portefeuilles individuels.

## Garde-fous à garder pour toute automatisation
- Jamais d'ordre de bourse ni de virement automatique.
- Peu de notifications : une alerte qui sonne souvent n'est plus lue.
- Chaque chiffre envoyé vient d'un script, avec sa date et sa source.
- Les données personnelles restent dans `prive/`, le Drive et la boîte mail, jamais dans le dépôt.
- Toute automatisation qui écrit garde une copie de l'état précédent.

## Par où commencer (ordre suggéré)
1. Brancher la newsletter du dimanche (connecteurs) et fusionner la branche.
2. Rappel du jour de paie avec la répartition calculée.
3. Calendrier fiscal et anniversaires d'enveloppes dans Google Calendar.
4. Alerte rare de grosse baisse avec la charte.
5. Lecture des relevés du courtier dans Gmail, pour supprimer la dernière saisie.
