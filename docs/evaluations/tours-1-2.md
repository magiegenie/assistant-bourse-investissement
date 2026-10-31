# Tour 1 (30/10/2026)

Profil fictif `prive/lea/`. Grille de `tests/scenarios.md` (5 critères notés 0 à 2).

| Scénario | Chiffres | Fond | Interdits | Clarté | Action | Total | Défaut principal |
|---|---|---|---|---|---|---|---|
| AN1 versement | 2 | 1 | 2 | 2 | 2 | 9 | Gains CTO « imposés à 30 % » : taux 2025, 31,4 % en 2026 |
| CB1 prime | 2 | 2 | 2 | 2 | 2 | 10 | Aucun |
| ST1 apport 2029 | 1 | 2 | 2 | 2 | 2 | 9 | Deux montants « estimés, pas calculés » |
| CO1 Nvidia | 2 | 2 | 2 | 2 | 2 | 10 | Écart de la poche Monde annoncé à -9,9 points au lieu de -4,8 (simulation avec achat, non précisé) |
| VE1 brief | 1 | 2 | 2 | 2 | 2 | 9 | Part du bitcoin « calculée de tête » ; n'utilise pas de veille collectée |

Corrections appliquées : règle commune à tous les agents (aucun chiffre de tête, taux fiscaux uniquement depuis la fiche C ou `scripts/fiscalite.py`) ; le Veilleur lit d'abord le digest de `docs/veille/`.

# Tour 2 (31/10/2026)

| Scénario | Total | Remarque |
|---|---|---|
| AN1 versement | 10 | Taux corrigé, plus d'erreur fiscale ; signale l'arrondi du script |
| AN2 performance | 9 | XIRR 8,63 % bien expliqué ; une part « à confirmer » au lieu d'être calculée ; a repéré une incohérence du profil de test (versements par enveloppe), corrigée |
| CB2 arnaque | 10 | Calcul 1,02^52 fait en Python, parcours AMF, THESEE et PHAROS ; taux du Livret A conforme à la fiche A point 83 |
| ST1 apport 2029 | 10 | Tous les montants calculés, poche apport séparée, fiscalité PEA juste |
| ST2 vente CTO | 10 | `fiscalite.py`, PFU 31,4 %, alternative sans impôt (fiche C point 117) |
| CO2 panique | 10 | Tests de résistance en euros, règles du profil, précédent d'avril 2025, aucune prédiction |

Tous les scénarios passent le seuil de 9/10. Point restant : une part de portefeuille donnée « à confirmer » au lieu d'être calculée (AN2).

# Routage du Directeur (31/10/2026)

15 phrases testées, 15 routées vers l'agent attendu. Trois cas frontières signalés (rentrée d'argent, notion liée à l'actualité, frais d'une ligne ou d'une enveloppe) : règles de départage ajoutées dans `CLAUDE.md`, section 2.
