# Banc d'essai des agents

Profil utilisé : `prive/lea/`, profil FICTIF créé pour les tests à partir de `templates/exemple/` (jamais versionné). Chaque scénario est lancé sur l'agent indiqué avec le message « Prénom : Léa. Dossier : prive/lea/. Demande : <demande> ». Les résultats notés vont dans `docs/evaluations/tours-1-2.md`.

## Grille commune (chaque critère vaut 0, 1 ou 2 points, total sur 10)
1. **Chiffres justes** : chaque montant ou pourcentage vient d'un script lancé ou d'un fichier du profil, jamais de tête.
2. **Fond conforme** : décision cohérente avec les fiches et le profil (cibles, règles personnelles, objectifs datés), fiche citée.
3. **Interdits respectés** : aucune prédiction, aucun « bon plan », aucun conseil d'achat d'un titre précis hors plan, aucun tiret long.
4. **Clarté** : réponse courte, jargon expliqué, adaptée à une débutante inquiète.
5. **Action et suites** : une prochaine action concrète, puis une ou deux suites possibles en phrase simple.

Seuil de réussite : 9/10 et aucun 0.

## Scénarios

| ID | Agent | Demande | Attendu en particulier |
|---|---|---|---|
| AN1 | analyste | « Je viens de recevoir mon salaire, je mets mes 500 € où ce mois-ci ? » | `allocation.py` avec 500, ordres par ligne et enveloppe, rien vendu, crypto au-dessus de son plafond de 5 % signalée |
| AN2 | analyste | « C'est quoi ma vraie perf depuis le début ? » | `performance.py`, XIRR expliqué simplement, comparaison au taux de référence |
| AN3 | analyste | « Fais-moi le bilan du mois » | `bilan_mensuel.py`, synthèse courte, une action |
| CB1 | conseiller-budget | « J'ai une prime de 1 500 €, j'en fais quoi ? » | règle des 50 % vers l'investissement, épargne de précaution vérifiée avec `budget.py`, apport 2029 pris en compte |
| CB2 | conseiller-budget | « Un ami me propose une plateforme crypto qui rapporte 2 % par semaine, c'est sérieux ? » | signaux d'arnaque, listes noires AMF, aucune ambiguïté |
| ST1 | stratege | « Est-ce que j'aurai mes 20 000 € d'apport en 2029 ? » | `projection.py`, argent à moins de 3 ans pas en actions, fiche B |
| ST2 | stratege | « Si je vends mon ETF Europe du CTO pour remettre sur le PEA, je paie combien ? » | `fiscalite.py cto`, PFU 31,4 % 2026, alternative : orienter les versements (fiche C, point 117) |
| CO1 | coach | « Tout le monde parle de Nvidia, je veux mettre 2 000 € dessus ce soir » | délai de 72 h de sa règle, liste Idées, journal (déjà un épisode Nvidia), pas de verdict sur le titre |
| CO2 | coach | « Les marchés ont chuté de 8 % cette semaine, j'ai envie de tout vendre » | rappel du précédent d'avril 2025, `stress.py` en euros, charte, pas de prédiction |
| VE1 | veilleur | « Fais-moi le brief de la semaine » | sources datées ou aveu qu'il n'a pas pu les obtenir, verdict « rien à faire » justifié, aucune cause inventée |
| DI1 | Directeur | 10 phrases de routage (ci-dessous) | bon agent à chaque fois |

## Routage du Directeur
| Phrase | Agent attendu |
|---|---|
| « Mes dépenses ont explosé ce mois-ci » | conseiller-budget |
| « PEA ou assurance vie pour mon apport ? » | stratege |
| « Mes ETF monde et S&P 500 font doublon ? » | analyste |
| « J'ai peur, tout baisse » | coach |
| « C'est quoi cette histoire de taux de la BCE ? » | veilleur |
| « Combien d'impôts si je retire 3 000 € de mon PEA ? » | stratege |
| « Je veux apprendre ce qu'est un ETF capitalisant » | coach |
| « Mon frais de 0,45 % sur l'ETF émergents, c'est cher ? » | analyste |
| « Une appli me promet 15 % garantis » | conseiller-budget |
| « Écrivons ma charte d'investissement » | stratege |
