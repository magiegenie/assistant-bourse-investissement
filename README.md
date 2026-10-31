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
- `scripts/` : les calculs (répartition, performance, projection, profil de risque, historique des marchés)
- `donnees/historique/` : la base historique des marchés (14 indices mois par mois, macro, frise d'événements sourcés), lisible aussi dans `docs/Historique-marches.xlsx`. Usage personnel, ne pas rendre le dépôt public
- `templates/` : modèles de profil, de budget et de portefeuille
- `docs/Guide-assistant-bourse-investissement.pdf` : **le guide d'utilisation complet** (source : `docs/GUIDE.md`, mis à jour à chaque nouveauté, regénéré par `python scripts/generer_guide.py`)
- `docs/` : guide, cahier des charges et idées

Aide à la réflexion uniquement, pas un conseil en investissement réglementé. Les clés API éventuelles vont dans `.env`, jamais dans le code.

## Installer sur un nouvel ordinateur

```bash
git clone https://github.com/magiegenie/assistant-bourse-investissement.git
cd assistant-bourse-investissement
python scripts/installer_mcp.py
```

L'installeur lit `mcp/serveurs.json`, installe les trois serveurs MCP des agents (données de marché, flux d'actualité, lecture web) dans `externe/`, puis écrit `.mcp.json` avec les chemins de l'ordinateur. Redémarrer Claude Code ensuite et accepter les serveurs. Python 3.10 ou plus et git sont nécessaires.

Le dossier `externe/` (code des autres), `.mcp.json` et `prive/` (données personnelles) ne sont jamais versionnés. La liste des dépôts open source dont les compétences ont été reprises, avec version et licence, est dans `docs/externe/depots.csv` ; leur code n'est pas nécessaire pour faire tourner l'assistant, les compétences sont déjà fusionnées dans `connaissances/agents/`.

