# Newsletter du dimanche

Une routine Claude (claude.ai/code, « Newsletter bourse du dimanche ») tourne chaque dimanche à 18 h 47 (heure de Paris), dans une nouvelle session. Elle envoie l'email « Ta semaine bourse » à l'adresse du compte Gmail connecté. Elle n'écrit rien dans le dépôt.

## Ce dont elle a besoin (sinon elle s'arrête et le dit)

- Le dépôt `magiegenie/assistant-bourse-investissement`, branche `main`, comme source de la routine. Sans lui, elle ne trouve ni le modèle ni le script.
- Les connecteurs **Gmail** (envoi) et **Google Drive** (lecture du Sheet) activés pour la routine. Connectés sur le compte ne suffit pas : ils doivent aussi être activés pour la routine.
- Un Google Sheet dont le titre contient « Portefeuille », rangé dans le dossier Drive « Assistant investissement ». Pour le créer : importer `templates/Portefeuille-complet.xlsx` dans ce dossier, puis l'ouvrir avec Google Sheets (Fichier, Enregistrer au format Google Sheets).

Limite connue : le connecteur Drive lit le Sheet mais ne sait pas y écrire. La newsletter donne donc en fin d'email les lignes à recopier dans la feuille Veille.

## Comment l'email est fabriqué

1. La routine écrit le contenu de l'édition dans un fichier JSON, en suivant `templates/newsletter-modele.md` et l'exemple `docs/exemples/newsletter-2026-11-01.json`.
2. `python scripts/newsletter_html.py edition.json` fabrique l'email HTML : mise en forme fixe, sources numérotées dans l'ordre de lecture et rassemblées en bas, contrôle automatique (aucun tiret long, aucun emoji, aucun lien dans le corps).
3. La routine envoie le HTML par Gmail. Si l'envoi échoue, elle crée un brouillon.

Chaque dimanche à 16 h UTC, le workflow GitHub `veille-hebdo.yml` collecte les flux publics de `donnees/sources.csv` et dépose le digest dans `docs/veille/`. La routine le lit d'abord, puis complète par la recherche web.

Pour modifier la routine : demander à Claude de mettre à jour la tâche « Newsletter bourse du dimanche » avec le texte ci-dessous.

## Texte de la tâche

```
Tu prépares et envoies la newsletter bourse hebdomadaire de l'utilisateur du compte (son adresse Gmail est celle du compte connecté). Écris en français, tutoiement, phrases simples, aucun tiret long, aucun emoji, jargon expliqué en une phrase.

0. Prérequis : le dossier de travail est le dépôt assistant-bourse-investissement et les outils Gmail et Google Drive sont chargés. S'il en manque un, n'invente rien : envoie une notification qui dit lequel manque, puis arrête-toi.
1. Lis templates/newsletter-modele.md (structure, clés du JSON, règles), connaissances/H-information.md (règles de sources) et docs/exemples/newsletter-2026-11-01.json (exemple complet à copier, en remplaçant tout son contenu).
2. Sheet : avec Google Drive, cherche le Google Sheet dont le titre contient « Portefeuille » dans le dossier « Assistant investissement ». Lis les feuilles Dashboard, Positions, Cibles et Veille. N'invente aucun chiffre : si une donnée manque, passe pour_toi en « indisponible » avec une phrase de diagnostic. Ne mets jamais de montant réel dans le dépôt.
3. Actualité : lis le digest le plus récent de docs/veille/ et donnees/calendrier-recurrent.csv, puis complète avec la recherche web. Rassemble les faits de la semaine écoulée (lundi au vendredi), les clôtures de vendredi pour les repères chiffrés, et l'agenda de la semaine suivante. Sources fiables uniquement (Reuters, Les Echos, Financial Times, Bloomberg, BCE, Fed, AMF, Insee), source primaire avant la presse. Chaque chiffre a sa source et sa date. Une cause n'est donnée que si une source la donne, sinon « cause non établie ». Aucune prédiction, aucun conseil d'achat ou de vente, aucun « bon plan ».
4. Résultats d'entreprises de la semaine qui vient : partie « tes ETF » à partir de donnees/indices-entreprises.csv et des positions du Sheet (les plus lourdes d'abord, 8 au maximum, uniquement celles qui publient), partie « les plus suivis du marché » (5 à 8 publications, Europe et États-Unis). Cite la source de chaque date, dis dans agenda.note si elle n'est pas confirmée par l'entreprise ou si l'Europe n'a pas été couverte.
5. Écris edition.json dans /tmp, puis lance : python scripts/newsletter_html.py /tmp/edition.json --sortie /tmp/edition.html. Si le script refuse l'édition, corrige le JSON selon son message et relance. Tout ce qui n'a pas pu être trouvé ou lu va dans « limites », jamais éparpillé dans le texte.
6. Envoie avec Gmail à l'adresse du compte, objet : « Ta semaine bourse : <date du lundi> au <date du dimanche> », le corps étant le contenu exact de /tmp/edition.html en HTML. Si l'envoi échoue, crée un brouillon Gmail avec le même contenu.
7. Ne fais rien d'autre : pas de commit, pas de push, pas de modification du Drive.
```
