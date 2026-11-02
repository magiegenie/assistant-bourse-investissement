# Sources de veille : la sélection

Base complète, notée et datée : `donnees/sources.csv` (101 lignes). Méthode et grille de notation : `docs/METHODE-SOURCES.md`. Toutes les lignes sont au statut « à vérifier » tant qu'une ouverture réelle n'a pas eu lieu : le réseau de la session de travail est fermé, la vérification des flux se fait chaque dimanche par GitHub Actions, celle des pages et des comptes sociaux depuis un ordinateur.

## Les meilleures par usage

| Usage | Sources de premier rang (note 8 à 10) |
|---|---|
| Décisions de taux et chiffres officiels | BCE, Fed, Insee, Eurostat, BLS |
| Chiffres de clôture et faits du jour | Reuters, Bloomberg, Les Echos, Le Monde économie |
| Fiscalité, règles, arnaques | service-public.fr, impots.gouv, AMF (listes noires, règles des finfluenceurs), ABE Info Service |
| Contexte de fond sur les marchés | J.P. Morgan Guide to the Markets, BNP Paribas Études économiques, Vanguard (hypothèses à 10 ans), SPIVA |
| Choisir un ETF | justETF, Morningstar, fiches MSCI, catalogue `donnees/etf-pea.csv` |
| Apprendre | La finance pour tous, Bogleheads, Ben Felix, The Plain Bagel |

## Macroéconomie et politique par région (note 8 à 10)

| Région | Macro | Politique et géopolitique |
|---|---|---|
| Monde | FMI, OCDE, Banque mondiale, BRI, AIE, PMI S&P Global, CEPII, indice EPU | AFP, AP, Reuters, The Economist, IFRI, Chatham House |
| France | Insee, Banque de France, Cour des comptes, OFCE | Vie publique, Assemblée nationale (budget) |
| Europe | BCE, Commission européenne, Eurostat, Banque d'Angleterre, Bruegel | Toute l'Europe, Politico Europe, Le Grand Continent |
| États-Unis | Fed, FRED, GDPNow, BEA, BLS, Trésor, PIIE | CBO (dette, budget), Council on Foreign Relations |
| Japon | Banque du Japon | Nikkei Asia |
| Chine | Banque populaire de Chine, statistiques nationales (à croiser), PMI Caixin | Caixin (7), South China Morning Post (6, propriétaire industriel) |
| Inde | Reserve Bank of India | AFP, Reuters |

Rendez-vous politiques et macro datés : `donnees/calendrier-recurrent.csv` (mi-mandat américain du 3 novembre 2026, présidentielle française des 18 avril et 2 mai 2027, FMI, G7...).

## Complément (note 6 et 7)
Zonebourse, Le Figaro, Mieux Vivre Votre Argent, Amundi Investment Institute, Société Générale, Crédit Agricole, Natixis, UBS, Quantalys, S'investir, Osez devenir libre, La Martingale. Utiles, mais chacun a un intérêt à déclarer (abonnement, produits, affiliation) : à croiser avec une source de premier rang.

## Utilisées avec prudence (note 5 et moins)
BFM Bourse (beaucoup de court terme), Finary (éditeur d'une application payante), conseils de titres d'Investir (opinions). Exclus : comptes de signaux de trading, promesses de gains.

## Réseaux sociaux (Instagram, TikTok, YouTube)
Aucun compte n'est retenu comme source d'information : ce sont des sources de pédagogie, jamais des signaux. Pour juger un compte : est-il titulaire du certificat de l'influence responsable de l'AMF et de l'ARPP, déclare-t-il ses partenariats, vend-il une formation, promet-il un rendement ? Une seule réponse inquiétante suffit pour l'écarter.

## À faire
- Lire l'Excel des grandes banques dès qu'il est déposé dans le dossier Drive « Assistant investissement », et ajouter chaque banque avec sa page de recherche.
- Confirmer les URL marquées « URL à confirmer » et trouver les flux RSS manquants (podcasts, Insee, AMF).
- Repasser la note de chaque source tous les six mois.
