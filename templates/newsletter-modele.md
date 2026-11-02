# Ta semaine bourse : modèle de l'édition

Lecture : 12 à 14 minutes (calculée automatiquement d'après le nombre de mots). Le résumé du haut se lit en 30 secondes. Outil d'aide à la réflexion, pas un conseil en investissement réglementé.

L'édition se prépare en **contenu JSON**, puis un script fabrique l'email HTML :

```
python scripts/cloture_hebdo.py --fin AAAA-MM-JJ --sortie /tmp/clotures.json
python scripts/cloture_hebdo.py --fin AAAA-MM-JJ --liste actions-fr --sortie /tmp/actions-fr.json
python scripts/newsletter_html.py edition.json --sortie edition.html
```

Un exemple complet et rendu se trouve dans `docs/exemples/newsletter-2026-11-01.json` et `.html`. **Copier cet exemple et remplacer tout son contenu**, ne jamais inventer un autre format. Le script refuse l'édition si une règle est cassée (voir « Règles du script »).

## Ordre de l'email (celui de la lecture)

| # | Bloc | Clé JSON | Contenu attendu |
|---|---|---|---|
| 1 | En-tête et sommaire | `periode` | Dates du lundi au dimanche. Le temps de lecture est calculé. |
| 2 | Résumé express | `resume` | Verdict en 2 phrases (le plus souvent « Rien à faire »), 4 points clés, le chiffre de la semaine, 3 rendez-vous. Se lit en 30 secondes. |
| 3 | Bilan de la semaine | `bilan` | `reperes` : variations réelles de la semaine, venues de `cloture_hebdo.py` (Etats-Unis, monde et Asie, Europe, devises, taux, matières premières). `jours` : un récit du lundi au vendredi, détaillé. Pour chaque jour : `chiffres` (5 à 9 variations du jour : S&P 500, Nasdaq 100, CAC 40, Nikkei, KOSPI, taux, pétrole, bitcoin... selon ce qui compte, pris dans `variation` de `cloture_hebdo.py`), `texte` (le fait principal, avec la cause si une source la donne), `faits` (3 à 5 puces : entreprises qui publient et leur réaction, grosses hausses ou baisses de valeurs avec leurs pourcentages, taux, pétrole, banques centrales). Une note « depuis mercredi » montre ce qui s'est passé après le sommet de la semaine. Chiffre introuvable : `null`, la case affichera « non disponible ». Pour le VIX, les taux et le pétrole, ajouter `"neutre": true` (ni bon ni mauvais). |
| 4 | Pourquoi ça a baissé | `pourquoi_baisse` | Une carte par ETF de la personne : variation, **chaîne de causes en étapes numérotées** (événement, mécanisme, effet), ce qui reste non établi, précédents historiques (`scripts/historique.py baisses`, `evenement`), ce que ça change pour son plan. Si rien n'a baissé de façon notable dans ses ETF, le bloc est supprimé. |
| 5 | Ce qu'il se passe en ce moment | `contexte` | 4 à 6 thèmes (IA, pétrole et géopolitique, taux, inflation, politique américaine, etc.), chacun classé à ignorer, à surveiller ou à agir, en 1 à 3 phrases. |
| 6 | La France | `france` | `actions` : le CAC 40 sur la semaine, plus fortes hausses et baisses (`cloture_hebdo.py --liste actions-fr`). `politique` : notation, budget, élections, écart de taux. `infos` : énergie, carburants, informations générales qui comptent. |
| 7 | Pour toi | `pour_toi` | Depuis `donnees/etf-newsletter.csv` (ou le Google Sheet s'il existe) : quel fait touche quel ETF. Valeur et écarts si le Sheet est lu. Sinon `statut: "indisponible"` et une phrase de diagnostic. |
| 8 | La semaine qui vient | `agenda` | `macro` (avec heure de Paris), `resultats_etf` (grosses lignes des ETF de la personne, d'après `donnees/indices-entreprises.csv`), `resultats_marche` (5 à 8 publications les plus suivies), `note` (dates non confirmées, Europe non couverte). |
| 9 | Une notion | `notion` | Une notion en 3 lignes, liée à la semaine. |
| 10 | Limites | `limites` | Tout ce qui n'a pas pu être trouvé ou lu, en 3 à 5 puces. Rien de ce genre ailleurs dans le texte. |
| 11 | Sources | `sources` | Générée par le script, dans l'ordre de lecture. |

Il n'y a plus de tableau « À recopier dans la feuille Veille ».

## « Pourquoi ça a baissé » : règles propres

- Une carte par ETF détenu (`donnees/etf-newsletter.csv`), pas par indice.
- Chaque étape de cause **cite une source** `[[src:cle]]` ou dit « cause non établie ». Sinon le script refuse l'édition.
- Séparer ce qui est **établi** (sourcé) de ce qui reste **non établi**. Ne jamais compléter une cause à partir de ce qui « paraît logique » : une explication de bon sens est annoncée comme telle, avec « cause non établie ».
- Replacer la baisse dans l'histoire avec des chiffres de `scripts/historique.py` (baisse comparable, temps de récupération), sans jamais promettre un rebond.
- Toujours terminer par « ce que ça change pour toi » : le plus souvent rien, ce que dit la charte (versement du mois, rééquilibrage au-delà de 10 points d'écart).

## La partie France : règles propres

- Les variations viennent de `cloture_hebdo.py` ; ne rien dire des causes d'une valeur sans source.
- Corriger une idée reçue quand une source la contredit (exemple : « 10 millions de barils » est une mise sur le marché de réserves, pas un achat).
- Politique : toujours le canal concret vers les placements (taux, banques, note), ou classer « à ignorer ».

## Règles du script (`scripts/newsletter_html.py`)

- **Aucun lien dans le texte.** Citer une source dans n'importe quel champ avec `[[src:cle]]`. Le script la remplace par [1], [2]... dans l'ordre où la lecture les rencontre, puis les rassemble en bas.
- Chaque clé citée doit être déclarée dans `sources` (`nom`, `url`, `date` si connue), et chaque source déclarée doit être citée au moins une fois.
- **Gras** : `**mot**`. Pas d'autre mise en forme à écrire. Un champ de texte peut être une chaîne ou une liste de paragraphes.
- Refus automatique : tiret long, emoji, adresse web dans le corps, lien hors du bloc Sources, étape de cause sans source.

## Règles de fond (fiche H)

- Chaque chiffre a sa source et sa date. Source primaire (communiqué BCE, Fed, Insee, AMF) avant la presse. Si seule une source secondaire a été lue, le dire dans `limites`.
- Une cause n'est donnée que si une source la fournit. Sinon : « cause non établie » (point 79).
- Aucune prédiction, aucun objectif de cours, aucun « bon plan ».
- Français, tutoiement, phrases simples, aucun tiret long, aucun emoji, jargon expliqué en une phrase.

## Voix et mise en forme (à relire avant d'écrire)

La newsletter doit se lire comme un texte de Melvin, pas comme un rapport d'IA (skill `humanizer-melvin`, registre tutoiement, un peu oral).

- Tutoiement, phrases simples. Alterner phrases courtes et plus longues. Une touche orale de temps en temps (« du coup », « en vrai », « bref »), un seul « vraiment » par édition, pas plus.
- Dire le fait directement. Pas de « ce n'est pas X, c'est Y », pas de « non seulement... mais aussi », pas de phrase de chute qui répète ce qui précède, pas de formule pseudo-profonde (« au coeur de », « la vraie question est »), pas de triade par réflexe.
- Vocabulaire à éviter : crucial, essentiel (en tic), robuste, paysage, souligne, met en lumière, plonger dans, naviguer dans, « il est important de noter que », « à l'ère de ».
- **Pas de gras dans le texte** (`**mot**` interdit en pratique) : le gras est réservé aux titres que le gabarit met déjà.
- **Couleurs** : le gabarit les réserve à ce qui compte. Vert ou rouge pour une variation de marché (gris pour le VIX, les taux, le pétrole), pastille de classement (à ignorer, à surveiller, à agir) seulement dans le résumé et dans la partie France, bleu marine pour les grands titres et le chiffre de la semaine. Rien d'autre ne se colore.
- Aucun tiret long, aucun emoji.
