# Skills et agents d'investissement open source : ce qu'on a repris

Date : 30/10/2026. Les dépôts sont clonés dans `externe/` (ignoré par git : on ne versionne pas le code des autres). Rien n'a été installé ni exécuté : on a lu les fichiers, puis recodé ou reformulé en français ce qui était utile. Tout est gratuit.

## 1. Inventaire et verdict

| Dépôt | Licence | Contenu | Verdict |
|---|---|---|---|
| `anthropics/financial-services-plugins` (et `financial-services`, identique) | Apache 2.0 | 112 skills et 10 agents pour banques d'affaires, private equity, analyse actions, conseillers en gestion de patrimoine | **Peu adapté** : modèles DCF, LBO, présentations de deals, rapprochements comptables. Repris : la structure du suivi de thèse (`thesis-tracker`) et l'idée de la revue client (`client-review`). |
| `joellewis/finance_skills` | MIT | 91 skills dont 38 en gestion de patrimoine (allocation, rééquilibrage, politique d'investissement, psychologie, fonds d'urgence, retraite) | **La meilleure source.** Repris : structure de la charte, rééquilibrage (flux d'abord, seuils, ordre fiscal), psychologie (profils face à l'argent, « raisonnable plutôt que rationnel », plan en 4 enveloppes), fonds d'urgence en paliers, ordre des priorités, garde-fous de retrait. Contexte américain (401k, IRA, fiscalité US), donc reformulé pour PEA, assurance vie, CTO. |
| `lyndonkl/claude` (`portfolio-drift-rebalancer`) | **aucune licence trouvée** | Agrégation multi-comptes, écart à la cible, plan de rééquilibrage fiscalement optimisé, jamais exécuté | **Idées seulement** (sans licence, on ne copie pas le texte) : seuil de 5 points, versement d'abord, ventes dans les comptes non imposés d'abord, contrôle achats = ventes, alertes « argent laissé sur la table ». Recodé from scratch dans `scripts/reequilibrage.py`. |
| `longonlyx/Skills` (`portfolio-cio`) | **aucune licence trouvée** | Tableau de bord HTML « niveau directeur des investissements » : transparisation des ETF, stress tests, recommandations d'achat et de vente avec nombre de titres, sentiment Reddit et Polymarket | **Idées seulement, et en partie contraires à nos règles** (recommandations chiffrées, prévisions, sentiment des forums). Repris : stress tests en euros (`scripts/stress.py`), bilan daté ajouté sans effacer les précédents. |
| `onewave-ai/claude-skills` | MIT | Skills génériques (`portfolio-analyzer`, `financial-goal-planner`, `budget-optimizer`) | **Écarté** : gabarits vides sans contenu métier. |
| `staskh/trading_skills` | MIT | Options, Interactive Brokers, scanners, trading | **Écarté** : trading actif, hors de notre philosophie. |
| `triplom/financial-mcp-server` | **aucune licence trouvée** | Serveur MCP : actions, SEC, FRED, crypto, change | **Pas installé** (voir §3). |
| `VoxLink-org/finance-tools-mcp` | MIT | Serveur MCP : yfinance, FRED, indicateurs techniques | **Pas installé** (voir §3). |

## 2. Ce qui a été intégré

| Où | Ajout | Source d'inspiration |
|---|---|---|
| `scripts/reequilibrage.py` | Plan de ventes si une poche dépasse le seuil : PEA et assurance vie d'abord, puis CTO en moins-value, puis plus petite plus-value ; réinvestissement dans la même enveloppe ; impôt estimé ; contrôle achats = ventes. Ne passe aucun ordre. | `portfolio-drift-rebalancer`, `rebalancing` |
| `scripts/stress.py` | 6 scénarios de crise en euros (correction, 2008, 2020, 2022, crypto, dollar), avec effet du dollar selon la poche. | `portfolio-cio` |
| `templates/charte-modele.md` | Charte d'une page : objectifs et « assez », capacité et volonté (la plus prudente décide), contraintes, allocation avec fourchettes, règles d'achat, de vente et de rééquilibrage, conduite en cas de baisse, indice choisi à l'avance, revues déclenchées par les événements de vie. | `investment-policy`, `finance-psychology` |
| Analyste | Rééquilibrage par ventes, test de résistance, alertes « argent laissé sur la table » (abondement employeur, LEP, épargne qui dort), historique des bilans dans `bilans.md`. | `portfolio-drift-rebalancer`, `portfolio-cio` |
| Stratège | Charte à partir du modèle, test de résistance avant validation, retraits à garde-fous. | `investment-policy`, `retirement-decumulation` |
| Coach | Profils face à l'argent, croyances héritées, « assez », raisonnable plutôt que rationnel, réduire de 5 à 10 points plutôt que tout vendre, thèse réfutable pour le satellite. | `finance-psychology`, `thesis-tracker` |
| Conseiller budget | Épargne de précaution sur dépenses essentielles et en paliers, plan en 4 enveloppes, ordre des priorités, point argent mensuel en couple, grandes manettes avant petites économies. | `emergency-fund`, `savings-goals`, `finance-psychology` |
| Fiches | A 109 à 111, D 116, E 114 et 115, F 112 et 113. | idem |

## 3. Données de marché (serveurs MCP)

Non installés. Raisons : un serveur MCP exécute du code tiers sur la machine et pourrait lire `prive/` ; deux n'ont pas de licence claire ; yfinance repose sur une API non officielle. Options gratuites pour plus tard, si on veut des données automatiques :
- **BCE Data Portal** (data.ecb.europa.eu) : API publique sans clé (taux, inflation zone euro).
- **FRED** (fred.stlouisfed.org) : API gratuite avec clé personnelle.
- **INSEE** : séries publiques (inflation France).
Le plus sûr serait un petit script maison qui interroge ces API officielles, plutôt qu'un serveur tiers. À décider.

## 4. Ce qu'on n'a trouvé nulle part

Aucun skill ne couvre la fiscalité française (PEA, assurance vie, PFU, prélèvements sociaux, formulaires 3916 et 2086), le plafond du PEA, l'éligibilité des ETF au PEA ou les livrets réglementés. Nos fiches A, C, D, I et `scripts/fiscalite.py` restent notre valeur propre.

## 5. Installé à la demande de l'équipe (30/10/2026)

| Élément | Où | Comment | Remarque |
|---|---|---|---|
| Skills `client-report`, `client-review`, `investment-proposal` (plugin « meeting-prep-agent » d'Anthropic, Apache 2.0) | `.claude/skills/` | copie des fichiers (pas de `npx`) | Il n'existe pas de plugin nommé « wealth-management » dans le dépôt Anthropic : ce sont ses skills de gestion de patrimoine. Pensés pour un conseiller face à un client. |
| Skill `report-stock` (staskh/trading_skills, MIT) | `.claude/skills/report-stock/`, code dans `externe/staskh_trading_skills` | `uv` (installé avec pip) + Python 3.13 géré par uv | Commandes réécrites avec des chemins absolus. Une note en tête du skill interdit de relayer sa « recommendation » et l'analyse d'options : faits uniquement. |
| Serveur MCP `financial-mcp-server` (déclaré MIT dans pyproject, pas de fichier LICENSE) | `externe/triplom_financial-mcp-server/.venv` + `.mcp.json` (ignoré par git, chemin propre à ce PC) | `pip install -e .` dans un environnement dédié, `mcp` limité à la version 1.x (la 2.x fait planter le serveur) | 24 outils testés : cours de CW8.PA reçu. Clés facultatives (FRED, Tiingo...) dans un fichier `.env` du dossier du serveur. Accès donné au Veilleur et à l'Analyste. |

Sur un autre ordinateur, il faudra refaire ces installations (le dossier `externe/` et `.mcp.json` ne sont pas versionnés).

## 6. Fusion dans les agents (30/10/2026)

Les skills autonomes ne sont plus dans le projet : `.claude/skills/` est supprimé (client-report, client-review, investment-proposal, report-stock). Leur contenu est fusionné dans un **manuel de compétences par agent** (`.claude/skills/manuel-*/SKILL.md`), que chaque agent ouvre au besoin. Le Directeur a aussi le sien. Le code de `report-stock` (Python 3.13) n'est plus utilisé : l'Analyste fait la fiche entreprise avec le serveur `financial-data`.

**Tri** : 737 fichiers de skills lus (hors le dépôt `anthropics/financial-services`, identique à `-plugins`), dont 51 doublons exacts. **148 retenus, 78 compétences** distinctes ; détail ligne par ligne dans `tri-des-skills.csv` (verdict, agent, compétence, raison) et inventaire brut dans `inventaire-brut.csv`.

| Dépôt | Skills lus | Retenus | Écartés |
|---|---|---|---|
| Anthropic (64 skills distincts) | 112 fichiers | 23 | banque d'affaires et private equity, comptabilité, KYC, trading institutionnel, outils Microsoft 365 et PowerPoint |
| joellewis | 91 | 46 | réglementation américaine, opérations d'établissement, cabinet de conseil, intégration de données |
| lyndonkl | 271 | 55 | sport fantasy, écriture de newsletter, architecture logicielle, science et recherche |
| onewave-ai | 233 | 19 | vente, marketing, design, code, rédaction |
| staskh | 29 | 5 | trading d'options et Interactive Brokers |
| longonlyx | 1 | 0 | idées déjà reprises, recommandations contraires à nos règles |

Répartition des 148 retenus : Analyste 65, Stratège 26, Coach 21, Conseiller budget 17, Veilleur 13, Directeur 6 (plusieurs skills se fondent en une même compétence).

**Anthropic n'a pas 86 skills utiles pour un particulier** : sur 64 skills distincts, 23 sont retenus. Les autres servent des métiers que notre équipe n'a pas (banquier d'affaires, comptable, fonds de capital-investissement). Anthropic a été prioritaire à chaque fois qu'un de ses skills couvrait une compétence ; sinon c'est la meilleure version parmi les autres dépôts.

**Retiré systématiquement des skills retenus** : recommandations d'achat et de vente, objectifs de cours, « idées de trades », vocabulaire de conformité américaine, fiscalité américaine (401k, IRA, 529, wash sale).

## 7. Serveurs d'actualité (installés le 30/10/2026, validés par Melvin)

| Serveur | Rôle | Installation | Test |
|---|---|---|---|
| `feed-mcp` (PyPI, MIT, code de 545 lignes relu : bibliothèque standard, lecture HTTP avec protection contre les adresses internes, aucune écriture ni commande) | Lecteur de flux RSS : derniers articles, recherche, synthèse | `externe/.venv-actu`, déclaré dans `.mcp.json` avec 3 flux : BCE (communiqués), Le Monde économie, BBC Business | 9 outils ; articles du jour reçus |
| `mcp-server-fetch` (serveur de référence du projet Model Context Protocol) | Lire une page web précise | `externe/.venv-fetch` | 1 outil ; page de la BCE lue |

Accès donné au Veilleur seulement. Flux qui bloquent les robots depuis ce poste (AMF, INSEE, Les Échos, Boursorama, Zonebourse) : non ajoutés. Pour ajouter un flux : `add_feed` pour la séance, ou modifier `.mcp.json` (fichier local, non versionné). Comme pour `financial-data`, il faudra réinstaller sur un autre ordinateur, et redémarrer Claude Code pour que les serveurs apparaissent.
