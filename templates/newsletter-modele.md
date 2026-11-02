# Ta semaine bourse : modèle de l'édition

Lecture : 4 minutes maximum. Outil d'aide à la réflexion, pas un conseil en investissement réglementé.

L'édition se prépare en **contenu JSON**, puis un script fabrique l'email HTML :

```
python scripts/newsletter_html.py edition.json --sortie edition.html
```

Le script impose la mise en forme et refuse tout ce qui casse les règles de lecture (voir « Règles du script »). Un exemple complet et rendu se trouve dans `docs/exemples/newsletter-2026-11-01.json` et `.html`. **Copier cet exemple et remplacer son contenu**, ne jamais inventer un autre format.

## Ordre de l'email (celui de la lecture)

| # | Bloc | Clé JSON | Contenu attendu |
|---|---|---|---|
| 1 | En-tête | `periode`, `lecture_min` | Dates du lundi au dimanche, temps de lecture. |
| 2 | Vue d'ensemble | `verdict`, `pastilles`, `chiffre_cle`, `rdv` | Verdict en 2 phrases (le plus souvent « Rien à faire »), 3 pastilles (Marchés, Taux et banques centrales, Politique) classées `ignorer`, `surveiller` ou `agir`, le chiffre clé de la semaine, les 3 rendez-vous à ne pas rater. |
| 3 | Les marchés | `reperes`, `reperes_note` | MSCI World, S&P 500, Stoxx Europe 600, CAC 40, MSCI Emerging Markets, euro/dollar, taux à 10 ans allemand et américain, bitcoin : valeur et variation sur la semaine. Chiffre introuvable : `null`, la case affichera « non disponible ». |
| 4 | Ce qui s'est passé | `faits` | 3 à 5 faits. Chacun : titre, texte factuel, « pourquoi ça compte », classement. |
| 5 | Pour toi | `pour_toi` | Depuis le Google Sheet : valeur approximative et variation, poches à plus de 5 points de leur cible, alertes du Dashboard, et pour chaque fait de quoi il touche ses placements. Si le Sheet est illisible : `statut: "indisponible"` et une phrase de diagnostic. |
| 6 | La semaine qui vient | `agenda` | `macro` (banques centrales, inflation, emploi, politique, avec heure de Paris), `resultats_etf`, `resultats_marche`, `note`. |
| 7 | Une notion en 3 lignes | `notion` | Une notion liée à la semaine. |
| 8 | À recopier dans la feuille Veille | `veille` | 3 à 5 lignes de 8 colonnes : Semaine, Thème, Importance (À ignorer, À surveiller, À agir), Fait chiffré, Source et date, Positions concernées, Impact estimé, Action. |
| 9 | Limites de cette édition | `limites` | Tout ce qui n'a pas pu être trouvé ou lu, en 2 à 4 puces. Rien de ce genre ailleurs dans le texte. |
| 10 | Sources | `sources` | Générée par le script, dans l'ordre de lecture. |

## Les résultats d'entreprises (bloc 6)

- **`resultats_etf` : tes ETF.** Prendre dans `donnees/indices-entreprises.csv` les entreprises des indices que la personne détient (lire ses positions dans le Sheet). Chercher la date de publication de chacune pour la semaine qui vient. Ne garder que celles qui publient, les plus lourdes d'abord (8 au maximum). Indiquer le poids dans l'indice et ce qu'on regardera. Aucune ne publie : laisser la liste vide, le texte « Aucune grosse ligne de tes ETF ne publie cette semaine » s'affichera tout seul.
- **`resultats_marche` : les plus suivis du marché.** 5 à 8 publications attendues de la semaine, Europe et États-Unis, avec le jour et si c'est avant ou après la clôture.
- Les dates viennent d'une source citée. Si la date n'est pas confirmée par l'entreprise, le dire dans `agenda.note`. Si l'Europe n'a pas pu être couverte, le dire aussi.

## Règles du script (`scripts/newsletter_html.py`)

- **Aucun lien dans le texte.** Citer une source dans n'importe quel champ avec `[[src:cle]]`. Le script la remplace par [1], [2]... dans l'ordre où la lecture les rencontre, puis les rassemble en bas.
- Chaque clé citée doit être déclarée dans `sources` (`nom`, `url`, `date` si connue), et chaque source déclarée doit être citée au moins une fois.
- **Gras** : `**mot**`. Pas d'autre mise en forme à écrire.
- Refus automatique : tiret long, emoji, adresse web dans le corps, lien hors du bloc Sources.

## Règles de fond (fiche H)

- Chaque chiffre a sa source et sa date. Source primaire (communiqué BCE, Fed, Insee, AMF) avant la presse. Si seule une source secondaire a été lue, le dire dans `limites`.
- Une cause n'est donnée que si une source la fournit (« selon Reuters ... »). Sinon : « cause non établie » (point 79).
- Politique et macro : pour chaque point, le fait daté, le canal concret (taux, devise, secteur, pays des ETF détenus) et l'horizon. Sans canal concret : `ignorer`. Jamais « donc acheter ou vendre ».
- Aucune prédiction, aucun objectif de cours, aucun « bon plan ». Le verdict suit la charte (versement du mois, rééquilibrage au-delà de 10 points d'écart), jamais une idée de marché.
- Français, tutoiement, phrases simples, aucun tiret long, aucun emoji, jargon expliqué en une phrase.
