# Méthode de recherche et de notation des sources

But : une base de sources unique (`donnees/sources.csv`) d'où part toute veille. On préfère 60 sources fiables à 300 sources bruyantes (fiche H).

## Familles à couvrir
1. **Officielles** : régulateurs, banques centrales, statistiques, administration fiscale.
2. **Banques et gestionnaires** : pages de recherche et de perspectives publiques des banques françaises et des grands gestionnaires mondiaux.
3. **Presse et sites de bourse** : presse économique de référence, sites de cours et d'analyse.
4. **Pédagogie** : chaînes YouTube, podcasts, comptes Instagram et TikTok, blogs, forums.
5. **Outils et données** : comparateurs d'ETF, bases de fonds, simulateurs officiels.

## Requêtes types (à relancer à chaque mise à jour)
- « <institution> recherche économique perspectives marchés page officielle »
- « <institution> flux RSS publications »
- « meilleures chaînes YouTube finances personnelles investissement passif France <année> »
- « podcast français investissement ETF bourse <année> classement »
- « compte Instagram TikTok finance personnelle français fiable AMF influenceurs »
- « AMF influenceurs finance mise en garde liste <année> » (pour exclure)
- « <site> conflit d'intérêts affiliation rémunération »
Chaque source retenue doit apparaître dans au moins deux résultats indépendants, ou être officielle.

## Grille de notation (sur 10)
| Critère | 0 | 1 | 2 |
|---|---|---|---|
| Autorité | inconnue | spécialisée reconnue | officielle ou presse de référence |
| Indépendance | vend ou affilie sans le dire | intérêt déclaré (émetteur, courtier) | aucun produit à vendre |
| Exactitude vérifiable | affirmations sans source | sources parfois citées | sources et dates systématiques |
| Utilité pour un particulier français en ETF et PEA | faible | partielle | directe |
| Accès et régularité | payant ou irrégulier | gratuit, irrégulier | gratuit, régulier, flux ou calendrier |

Usage par note : 8 à 10, source de premier rang pour le Veilleur et la newsletter ; 6 et 7, complément ; 5 et moins, pas utilisée.

## Exclusions
Promesses de gains, signaux d'achat ou de vente, formations payantes poussées en permanence, affiliation non déclarée, compte ou site cité dans une mise en garde AMF.

## Statuts
- **vérifiée** : l'URL a été ouverte et le contenu correspond (ou flux lu par `scripts/verifier_sources.py`).
- **à vérifier** : repérée par recherche web, pas encore ouverte (cas des réseaux sociaux depuis le cloud).
- **exclue** : gardée dans la liste avec la raison, pour ne pas la réévaluer à chaque fois.

## Mise à jour
Tous les six mois, ou dès qu'une source change (paywall, ligne éditoriale, faute grave). Les flux RSS sont vérifiés chaque dimanche par GitHub Actions.
