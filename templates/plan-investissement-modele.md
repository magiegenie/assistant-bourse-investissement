# Plan d'investissement de <Prénom>

_Établi le : JJ/MM/AAAA, à partir de l'accueil et du profil de risque. Prochaine revue : JJ/MM/AAAA._

Ce plan traduit ta charte en actions concrètes. Tous les montants sont calculés par les scripts (`allocation.py`, `projection.py`, `stress.py`). Outil d'aide à la réflexion, pas un conseil en investissement réglementé.

## 1. D'où tu pars
- Profil de risque : niveau ___ (<nom>), actions entre ___ et ___ % (`profil-risque.md`)
- Épargne de précaution : ___ € pour une cible de ___ € (___ mois de dépenses essentielles)
- Déjà investi : ___ € (`positions.csv`)
- Versement mensuel possible : ___ €
- Dettes à plus de 6 % : oui / non

## 2. Les priorités, dans l'ordre
| # | Étape | État | Montant ou action |
|---|---|---|---|
| 1 | Épargne de précaution complète | à faire / en cours / fait | |
| 2 | Abondement de l'employeur (PEE, PER collectif) | | |
| 3 | Dettes à plus de 5 à 6 % remboursées | | |
| 4 | PEA ouvert (lance le compteur des 5 ans) | | |
| 5 | Assurance vie ouverte | | |
| 6 | Compte-titres ou PER, seulement si utile | | |

## 3. L'allocation cible
| Poche | Cible % | Fourchette | Enveloppe | Critères de choix du support |
|---|---|---|---|---|
| | | ±5 pts | | Frais (TER) bas, encours de plus de 100 M€, éligible PEA, réplication, écart de suivi |

Repère historique sur la durée du plan : `python scripts/historique.py glissant MSCI_WORLD --annees <durée> --eur --reel` (pire, médian, meilleur).

## 4. Chaque mois
- Le ___ (jour de la paie) : virement automatique de ___ € vers le compte d'investissement (« se payer en premier »).
- Le ___ : versement programmé chez le courtier, ou ordres passés à la main selon « Je mets combien où ce mois-ci ? ».
- Répartition du premier versement (`allocation.py`) :

| Poche | Montant |
|---|---|
| | |

## 5. Les automatismes à mettre en place
- [ ] Virement permanent le jour de la paie
- [ ] Versement programmé chez le courtier (si disponible)
- [ ] Rappel mensuel : export du relevé et mise à jour du Google Sheet
- [ ] Rappel trimestriel : abonnements, thèses des lignes satellites
- [ ] Rappel annuel : revue de la charte, test de risque, déclaration d'impôts

## 6. Ce que ça peut donner (projection)
Trois scénarios, jamais un chiffre unique (`projection.py`, nominal, avant frais et impôts) :

| Horizon | Prudent (4 %) | Central (6 %) | Favorable (8 %) |
|---|---|---|---|
| 5 ans | | | |
| 10 ans | | | |
| 20 ans | | | |

Test de résistance (`stress.py`) : pire scénario ___ €, pour une perte maximale acceptable de ___ €.

## 7. Les 12 prochains mois
| Mois | À faire |
|---|---|
| | |

## 8. Ce qui ferait changer le plan
Événement de vie (naissance, perte d'emploi, héritage, achat immobilier), objectif atteint ou modifié, profil de risque qui change. Dans ces cas : revue avec le Stratège.
