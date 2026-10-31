# Sources

Ces principes sont le socle commun. Tout agent qui donne une recommandation cite la fiche correspondante (ex. `D-allocation.md`, point 31).

## Fiche C (fiscalité), vérifiées

- service-public.fr, fiche F2329 « Prélèvements sociaux », vérifiée le 30/06/2026 : taux 2026 (18,6 % cas général, 17,2 % assurance vie, immobilier, PEL et CEL).
- service-public.fr, fiche F2613 « Revenus d'épargne et de placements », vérifiée le 15/04/2026 : PFU (12,8 % d'impôt sur le revenu plus prélèvements sociaux), livrets réglementés exonérés.
- service-public.fr, fiche F22449 « PEA », vérifiée le 15/04/2026 : retrait avant et après 5 ans.

## Composition des indices (vérifiée, fiche D points 25 et 26)

Fiches officielles MSCI au 30/09/2026 (World, ACWI, Emerging Markets, Europe), fiche Nasdaq-100 au 30/09/2026, positions quotidiennes de l'ETF SPY (State Street) au 29/10/2026. Données et liens dans `donnees/indices-pays.csv` et `donnees/indices-entreprises.csv`. À mettre à jour chaque trimestre.

## Fiches D et E (allocation, méthode), non vérifiées

Les compléments des fiches D et E viennent de recherches externes (`docs/recherche/02-produits.md`, `03-historique.md`, `06-allocation.md`, `06b-allocation-bis.md`), non confirmées à la source. Études citées à retrouver avant usage : Vanguard (2023) sur le versement échelonné, J.P. Morgan Guide to Retirement (market timing), Barber et Odean (2000), Bessembinder (la « mise à jour 2026 » n'est pas confirmée), factsheets MSCI et S&P Dow Jones Indices (poids des États-Unis et concentration), FGDR (garanties 100 000 € et 70 000 €).

## Fiches A, B, G, I

- **Vérifiés par recherche web** : taux du Livret A (1,7 %), du LDDS (1,7 %) et du LEP (2,5 %) au 1er août 2026 (info.gouv.fr, service-public.gouv.fr, presse spécialisée) ; inflation de 3,1 % en septembre 2026 (INSEE, via la presse économique). L'inflation d'octobre 2026 n'a pas été trouvée.
- **Non vérifiés** : le reste vient de `docs/recherche/03-historique.md`, `04-projection.md`, `05-retrait.md`, `10-budget.md` et `11-arnaques.md`. Sources à retrouver avant de citer un chiffre : Bengen (1994), étude Trinity (1998), Morningstar (taux de retrait sûr), Dimson, Marsh et Staunton (rendements 1900-2022), DREES (coût de la dépendance), HCSF (taux d'endettement 35 %), ABE Infoservice, ORIAS, REGAFI, FGDR, FGAP.
- Les calculs de capital et de frais des fiches B et G sont refaits avec `scripts/projection.py` : les montants des recherches 04 étaient en partie faux.

## Fiches F et H (comportement, information), non vérifiées

Les compléments viennent de `docs/recherche/07-comportement.md`, `09-veille.md` et `sources-veille.csv` (recherches externes), et du brouillon `08-pedagogie.md` (rédigé par Claude, sans source externe). Études à retrouver avant de citer un chiffre : Morningstar « Mind the Gap 2024 », Vanguard « Advisor's Alpha », DALBAR (méthode critiquée), Barber et Odean (2000), Benartzi et Thaler (1995), Kahneman et Tversky (1979), Shefrin et Statman (1985), études de l'AMF sur les CFD et Forex, loi n° 2023-451 sur l'influence commerciale.

## Base historique des marchés (fiche G, point 119)

Collectée le 31/10/2026 par `scripts/maj_historique.py`, depuis Yahoo Finance, le fichier officiel STOXX et FRED. Couverture réelle, sources indice par indice, contrôles et limites (prix seul, devises, séries synthétiques) dans `donnees/historique/SOURCES.md`. La frise `donnees/historique/evenements.csv` compte 86 événements, chacun avec un lien vérifié. Elle **remplace** `docs/recherche/rendements-annuels.csv` (resté largement « à vérifier ») et `baisses-majeures.csv` (recalculées et comparées) : pour un chiffre historique, passer par `scripts/historique.py`.

## Test de profil de risque (fiche D, point 118)

- **Vérifié le 31/10/2026** : page de l'AMF « Vous souhaitez mieux vous connaître en tant qu'épargnant ? » (amf-france.org, espace épargnants, conseils pratiques, article du 05/10/2022) : autodiagnostic pédagogique ; rappelle que le profil réglementaire MIF porte sur la situation financière, les objectifs, l'horizon, la capacité à subir des pertes, le profil d'investisseur et le niveau de connaissances et d'expérience. https://www.amf-france.org/fr/espace-epargnants/savoir-bien-investir/conseils-pratiques/mieux-se-connaitre-en-tant-quepargnant
- **Référence, non relue à la source** : Grable, J. et Lytton, R. H. (1999), « Financial risk tolerance revisited: the development of a risk assessment instrument », Financial Services Review, 8, 163-181 (échelle de 13 questions, trois facteurs : risque d'investissement, confort et expérience, risque spéculatif). Ses versions en ligne en anglais ont changé d'hébergeur ; aucun lien n'a pu être confirmé, donc aucun n'est donné.
- Les questions de `questionnaire-risque.json`, les points et les seuils (niveaux, plafonds) sont rédigés par nous à partir de ces thèmes et des fiches A, B, D et F. Ils ne sont pas validés scientifiquement.

## Skills open source (idées reprises et reformulées)

Fiches A 109 à 111, D 116, E 114 et 115, F 112 et 113, modèle de charte, scripts `reequilibrage.py` et `stress.py`. Inspirés de : joellewis/finance_skills (MIT : investment-policy, rebalancing, finance-psychology, emergency-fund, savings-goals, retirement-decumulation), anthropics/financial-services-plugins (Apache 2.0 : thesis-tracker), et, pour des idées seulement car sans licence, lyndonkl/claude (portfolio-drift-rebalancer) et longonlyx/Skills (portfolio-cio). Ouvrages cités par ces skills : Housel, *The Psychology of Money* ; Thaler et Sunstein, *Nudge* ; Sethi, *I Will Teach You to Be Rich*. Détail dans `docs/externe/ANALYSE-SKILLS.md`. Les manuels de compétences des agents (`connaissances/agents/`) fusionnent 148 skills en 78 compétences, avec les sources de chaque section en fin de fichier ; tri ligne par ligne dans `docs/externe/tri-des-skills.csv`.

Les autres points de la fiche C marqués « à vérifier » viennent de `docs/recherche/01-fiscalite.md` (recherche externe, non confirmée). La bibliographie complète proposée par la recherche 12 n'est pas reprise ici tant qu'elle n'est pas vérifiée.
