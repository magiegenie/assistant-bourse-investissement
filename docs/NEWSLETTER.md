# Newsletter du dimanche

Une routine Claude (claude.ai/code, « Newsletter bourse du dimanche ») tourne chaque dimanche à 18 h 47 (heure de Paris), dans une nouvelle session. Elle envoie l'email « Ta semaine bourse » (12 à 14 minutes de lecture) à l'adresse du compte Gmail connecté. Elle n'écrit rien dans le dépôt.

## Ce dont elle a besoin (sinon elle s'arrête et le dit)

- Le dépôt `magiegenie/assistant-bourse-investissement`, branche `main`, comme source de la routine. Sans lui, elle ne trouve ni le modèle ni les scripts.
- Les connecteurs **Gmail** (envoi) et **Google Drive** (lecture du Sheet) activés pour la routine. Connectés sur le compte ne suffit pas : ils doivent aussi être activés pour la routine.
- La liste des ETF de la personne : `donnees/etf-newsletter.csv` (nom, ISIN, indice suivi, poche, **aucun montant**). Si un Google Sheet dont le titre contient « Portefeuille » existe dans le dossier Drive « Assistant investissement », la routine le lit en plus (valeur, écarts, alertes). Sinon elle s'en passe et le dit dans les limites. Pour créer le Sheet : importer `templates/Portefeuille-complet.xlsx` dans ce dossier, puis l'ouvrir avec Google Sheets.
- Un accès au réseau depuis la session pour `scripts/cloture_hebdo.py` (cours Yahoo Finance). Sinon la routine cherche les clôtures sur le web et le dit dans les limites.

Limite connue : le connecteur Drive lit le Sheet mais ne sait pas y écrire.

## Comment l'email est fabriqué

1. `python scripts/cloture_hebdo.py` donne les variations de la semaine (indices, devises, taux, matières premières) et `--liste actions-fr` celles des valeurs du CAC 40.
2. La routine cherche les faits et leurs causes sur le web, écrit le contenu de l'édition dans un JSON en suivant `templates/newsletter-modele.md` et l'exemple `docs/exemples/newsletter-2026-11-01.json`.
3. `python scripts/newsletter_html.py edition.json` fabrique l'email HTML : mise en forme fixe, sources numérotées dans l'ordre de lecture et rassemblées en bas, temps de lecture calculé, contrôles (aucun tiret long, aucun emoji, aucun lien dans le corps, chaque cause citée ou « cause non établie »).
4. La routine envoie le HTML par Gmail. Si l'envoi échoue, elle crée un brouillon.

Chaque dimanche à 16 h UTC, le workflow GitHub `veille-hebdo.yml` collecte les flux publics de `donnees/sources.csv` et dépose le digest dans `docs/veille/`. La routine le lit d'abord, puis complète par la recherche web.

Pour modifier la routine : demander à Claude de mettre à jour la tâche « Newsletter bourse du dimanche » avec le texte ci-dessous.

## Texte de la tâche

```
Tu prépares et envoies la newsletter bourse hebdomadaire de l'utilisateur du compte (son adresse Gmail est celle du compte connecté). Écris en français, tutoiement, phrases simples, aucun tiret long, aucun emoji, jargon expliqué en une phrase. Longueur visée : 12 à 14 minutes de lecture. Pour le jour par jour, donne pour chaque jour les variations du jour (chiffres), le fait principal et 3 à 5 faits sourcés. Écris comme Melvin (section « Voix et mise en forme » de templates/newsletter-modele.md) : phrases courtes et longues mélangées, pas de tournure « ce n'est pas X, c'est Y », pas de gras dans le texte.

0. Prérequis : le dossier de travail est le dépôt assistant-bourse-investissement et les outils Gmail et Google Drive sont chargés. S'il en manque un, n'invente rien : envoie une notification qui dit lequel manque, puis arrête-toi.
1. Lis templates/newsletter-modele.md (blocs, clés du JSON, règles), connaissances/H-information.md (règles de sources) et docs/exemples/newsletter-2026-11-01.json (exemple complet à copier en remplaçant tout son contenu).
2. Portefeuille : lis donnees/etf-newsletter.csv (les ETF de la personne, sans montants). Avec Google Drive, cherche aussi le Google Sheet dont le titre contient « Portefeuille » dans le dossier « Assistant investissement » et lis ses feuilles Dashboard, Positions et Cibles. S'il n'existe pas, continue sans lui et dis-le dans les limites. N'invente aucun chiffre et ne mets jamais de montant réel dans le dépôt.
3. Chiffres : lance python scripts/cloture_hebdo.py --fin <vendredi de la semaine> --sortie /tmp/clotures.json, puis la même commande avec --liste actions-fr --sortie /tmp/actions-fr.json. Un repère sans donnée s'affiche « non disponible » : ne le remplace jamais par un chiffre de mémoire. Si le script n'a pas accès au réseau, cherche les clôtures sur le web et dis-le dans les limites.
4. Actualité : lis le digest le plus récent de docs/veille/ et donnees/calendrier-recurrent.csv, puis complète avec la recherche web : ce qui s'est passé du lundi au vendredi, jour par jour, et pourquoi (sources fiables : Reuters, AP, Les Echos, Financial Times, Bloomberg, BCE, Fed, AMF, Insee ; source primaire avant la presse). Pour chaque baisse notable des ETF de la personne, construis la carte « Pourquoi ça a baissé » : chaîne de causes sourcées, ce qui reste non établi, précédent historique avec python scripts/historique.py baisses, ce que ça change pour son plan. Une cause n'est donnée que si une source la donne, sinon « cause non établie ». Ajoute le contexte (3 à 6 thèmes), la partie France (actions, politique, informations générales), l'agenda de la semaine suivante et les résultats d'entreprises (tes ETF d'après donnees/indices-entreprises.csv, puis les plus suivis du marché). Aucune prédiction, aucun conseil d'achat ou de vente, aucun « bon plan ».
5. Écris edition.json dans /tmp, puis lance : python scripts/newsletter_html.py /tmp/edition.json --sortie /tmp/edition.html. Si le script refuse l'édition, corrige le JSON selon son message et relance. Tout ce qui n'a pas pu être trouvé ou lu va dans « limites », jamais éparpillé dans le texte. Il n'y a pas de tableau à recopier dans une feuille Veille.
6. Envoie avec Gmail à l'adresse du compte, objet : « Ta semaine bourse : <date du lundi> au <date du dimanche> », le corps étant le contenu exact de /tmp/edition.html en HTML. Si l'envoi échoue, crée un brouillon Gmail avec le même contenu.
7. Ne fais rien d'autre : pas de commit, pas de push, pas de modification du Drive.
```
