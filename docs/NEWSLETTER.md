# Newsletter du dimanche

Une tâche planifiée Claude Code tourne chaque dimanche à 18 h 47 (heure de Paris), dans une nouvelle session sur ce dépôt. Elle a accès à deux connecteurs seulement : Gmail (envoi de l'email) et Google Drive (lecture du Sheet). Elle n'écrit rien dans le dépôt.

Le Sheet attendu : un Google Sheet dont le titre contient « Portefeuille », rangé dans le dossier Drive « Assistant investissement ». Pour le créer : importer `templates/Portefeuille-complet.xlsx` dans ce dossier, puis l'ouvrir avec Google Sheets (Fichier, Enregistrer au format Google Sheets).

Limite connue : le connecteur Drive lit le Sheet mais ne sait pas y écrire. La newsletter donne donc en fin d'email les lignes à recopier dans la feuille Veille.

Pour modifier la tâche : demander à Claude de mettre à jour la tâche planifiée « Newsletter bourse du dimanche » avec le nouveau texte ci-dessous.

## Texte de la tâche

```
Tu prépares et envoies la newsletter bourse hebdomadaire de l'utilisateur du compte (son adresse Gmail est celle du compte connecté). Écris en français, tutoiement, phrases simples, aucun tiret long, aucun emoji, pas de jargon non expliqué.

1. Dépôt : si le dossier de travail est le dépôt assistant-bourse-investissement, lis templates/newsletter-modele.md (structure à suivre) et connaissances/H-information.md (règles de sources). Si le fichier manque sur la branche courante, fais git fetch origin claude/bold-carson-gjrlxk puis lis-les avec git show origin/claude/bold-carson-gjrlxk:<chemin>.
2. Sheet : avec Google Drive, cherche le Google Sheet dont le titre contient « Portefeuille » dans le dossier « Assistant investissement ». Lis les feuilles Dashboard, Positions, Cibles et Veille. N'invente aucun chiffre : si une donnée manque, dis-le. Ne mets jamais de montant réel dans le dépôt.
3. Actualité : avec la recherche web, rassemble les faits de la semaine écoulée (lundi au vendredi) et l'agenda de la semaine suivante, uniquement depuis des sources fiables (Reuters, Les Echos, Financial Times, Bloomberg, BCE, Fed, AMF, Insee). Chaque chiffre a sa source et sa date. Une cause n'est donnée que si une source la donne, sinon écris « cause non établie ». Aucune prédiction, aucun conseil d'achat ou de vente, aucun « bon plan ».
4. Rédige l'email selon le modèle : verdict, ce qui s'est passé, ce que ça change pour toi, la semaine qui vient, une notion, lignes à recopier dans la feuille Veille. 4 minutes de lecture maximum. Termine par : « Outil d'aide à la réflexion, pas un conseil en investissement réglementé. »
5. Envoie l'email avec Gmail à l'adresse du compte, objet : « Ta semaine bourse : <date du lundi> au <date du dimanche> ». Corps en HTML simple (titres h2, paragraphes, un tableau pour la Veille).
6. Si l'envoi échoue, crée un brouillon Gmail avec le même contenu. Ne fais rien d'autre : pas de commit, pas de push, pas de modification du Drive.
```
