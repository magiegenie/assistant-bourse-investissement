# Assistant Bourse Investissement

Un assistant pour investir mieux, gérer son budget et progresser, sans stress. Il fonctionne dans Claude Code, en parlant normalement : **aucune commande à retenir**.

## Démarrer (5 minutes)

1. Cloner le dépôt : `git clone https://github.com/magiegenie/assistant-bourse-investissement.git`
2. Ouvrir le dossier dans Claude Code
3. Écrire « Salut, c'est <ton prénom> ». La première fois, l'assistant te pose quelques questions et crée ton espace privé.
4. Ensuite, parle-lui comme à un conseiller : « je viens d'être payé, je mets combien où ? », « j'ai envie d'acheter du X », « quoi de neuf ce matin ? »

## L'équipe (elle se répartit le travail toute seule)

| Agent | Il s'occupe de |
|---|---|
| Conseiller budget | budget, épargne, dettes, primes, arnaques, prévoyance |
| Stratège | objectifs, enveloppes (PEA, assurance vie...), impôts, charte d'investissement |
| Analyste | portefeuille, versement du mois, performance, frais |
| Coach | décisions d'achat et de vente, émotions, journal, apprentissage |
| Veilleur | actualités filtrées sur tes placements |

Tu peux aussi en appeler un par son nom : « coach, j'ai peur avec la baisse ».

## Confidentialité

Tes données (profil, portefeuille, budget, journal) sont dans `prive/<prénom>/`, **jamais envoyées sur GitHub**. Chacun garde les siennes sur son ordinateur.

## Contenu du dépôt

- `CLAUDE.md` : le Directeur, qui comprend ta demande et appelle le bon agent
- `.claude/agents/` : les 5 agents
- `connaissances/` : les 50 principes d'investissement et de budget, avec leurs sources
- `scripts/` : les calculs (répartition, performance, projection)
- `templates/` : modèles de profil, de budget et de portefeuille
- `docs/` : cahier des charges et idées

Aide à la réflexion uniquement, pas un conseil en investissement réglementé. Les clés API éventuelles vont dans `.env`, jamais dans le code.
