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
- `.claude/agents/` : les 5 agents, et `.claude/skills/manuel-<agent>/` : leur manuel de compétences, chargé au démarrage
- `connaissances/` : les principes d'investissement et de budget, avec leurs sources
- `scripts/` : les calculs (répartition, performance, projection, rééquilibrage, exposition, stress, fiscalité) et le générateur du classeur
- `tests/` : tests des calculs (`python -m unittest discover tests`), sur le jeu fictif `templates/exemple/`
- `templates/` : modèles de profil, de budget, de charte, de newsletter et le classeur `Portefeuille-complet.xlsx`
- `docs/` : cahier des charges, idées, et `NEWSLETTER.md` (la newsletter automatique du dimanche)

## Le classeur (Google Sheets ou Excel)

`templates/Portefeuille-complet.xlsx` est un modèle vide de 15 feuilles : Dashboard (chiffres clés, alertes, graphiques), Paramètres, Actifs, Transactions, Positions, Historique, Cibles, Budget, Objectifs, Journal, Revenus et frais, Fiscalité, Idées, Veille. Pour l'utiliser dans Google Sheets : l'importer dans le dossier Drive « Assistant investissement », l'ouvrir, puis Fichier, Enregistrer au format Google Sheets, en gardant « Portefeuille » dans le titre. Pour le régénérer : `python scripts/creer_sheet.py` (ajouter `--exemple` pour une version remplie de données fictives).

## La newsletter du dimanche

Chaque dimanche à 18 h 47, une tâche planifiée Claude Code lit le Sheet, rassemble l'actualité de la semaine et l'agenda de la suivante, puis envoie un email. Détails et texte de la tâche : `docs/NEWSLETTER.md`.

Aide à la réflexion uniquement, pas un conseil en investissement réglementé. Les clés API éventuelles vont dans `.env`, jamais dans le code.

## Installer sur un nouvel ordinateur

```bash
git clone https://github.com/magiegenie/assistant-bourse-investissement.git
cd assistant-bourse-investissement
python scripts/installer_mcp.py
```

L'installeur lit `mcp/serveurs.json`, installe les trois serveurs MCP des agents (données de marché, flux d'actualité, lecture web) dans `externe/`, puis écrit `.mcp.json` avec les chemins de l'ordinateur. Redémarrer Claude Code ensuite et accepter les serveurs. Python 3.10 ou plus et git sont nécessaires.

Le dossier `externe/` (code des autres), `.mcp.json` et `prive/` (données personnelles) ne sont jamais versionnés. La liste des dépôts open source dont les compétences ont été reprises, avec version et licence, est dans `docs/externe/depots.csv` ; leur code n'est pas nécessaire pour faire tourner l'assistant, les compétences sont déjà fusionnées dans les skills `.claude/skills/manuel-<agent>/`.

