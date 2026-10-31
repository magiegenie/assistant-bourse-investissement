# Profil de risque de <Prénom>

_Test passé le : JJ/MM/AAAA. Contexte de marché ce jour-là : haut / normal / baisse. Prochain test : JJ/MM/AAAA (une fois par an, après un événement de vie, et après la prochaine grosse baisse)._

Calculé par `python scripts/profil_risque.py prive/<prenom>` à partir de `reponses-risque.csv`. Questions dans `connaissances/questionnaire-risque.json`. Outil d'aide à la réflexion, non validé scientifiquement.

## Résultat

| Dimension | Score | Niveau | En une phrase |
|---|---|---|---|
| Capacité (finances) | /100 | | |
| Tolérance (émotions) | /100 | | |
| Besoin de risque | rendement réel nécessaire : % | faible / moyen / élevé / irréaliste | |
| Connaissances | /100 | faible / moyen / bon | |

**Profil retenu : niveau _ , <nom>** (actions : ___ %). Règle : le plus prudent de la capacité et de la tolérance décide (fiche D, point 56).

- Perte maximale acceptable : ___ €, soit ___ % du montant.
- Choix de la personne si le script propose un cran plus prudent : ___

## Ce que ça veut dire pour toi

(3 à 5 lignes en langage simple : la part d'actions, ce que tu pourrais voir dans une mauvaise année, en euros, ce qui te protège.)

## Alertes à travailler

(Recopier les alertes du script, et pour chacune l'agent qui s'en occupe : Conseiller budget, Stratège ou Coach.)

## Historique des tests

| Date | Contexte | Capacité | Tolérance | Profil | Ce qui a changé |
|---|---|---|---|---|---|
| | | | | | |

Réaction réelle lors des baisses vécues depuis le dernier test (rempli par le Coach) :

## Données pour les scripts

Ne pas renommer ces lignes : `scripts/stress.py` les lit.

```
profil_niveau:
capacite_niveau:
tolerance_niveau:
perte_max_eur:
```
