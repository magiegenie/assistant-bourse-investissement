# Recherche 01 : fiscalité de l'investisseur particulier en France

- Origine : recherche externe (autre IA), déposée le 30/10/2026. Texte brut, mis en forme Markdown, contenu non modifié.
- Statut : **non vérifié**. Aucune de ces données n'est encore intégrée dans `connaissances/`.
- Fichier de données associé : `fiscalite-parametres.csv`.

## Notes de relecture (ajoutées par Claude, ne font pas partie du rapport)

À contrôler avant toute intégration dans la fiche C :

1. **Prélèvements sociaux à 18,6 % sur PEA et assurance vie** : le rapport les applique partout (PEA, AV, CTO, crypto). Une recherche web (sites d'information, pas le texte de loi) indique que la hausse à 18,6 % est bien réelle (PFU à 31,4 %), mais que l'**assurance vie est exclue** (17,2 % maintenus). Le PEA serait concerné, avec une incertitude sur les gains antérieurs à 2026. Les simulations 2 et 3 sont donc à refaire. Voir `00-SYNTHESE.md`, §2.
2. **Prélèvements sociaux de l'assurance vie** : le rapport les calcule en une fois sur les gains lors du rachat (simulation 3). En pratique, ceux des fonds en euros sont prélevés chaque année, et le taux dépend de l'année de formation des gains. La simulation est donc simplifiée.
3. **PEA, prélèvements sociaux selon la date des gains** : même remarque de simplification (taux appliqués selon la période de formation du gain).
4. **PER, plafonds de déduction** : « environ 4 710 € min et 37 680 € max (indicatif) ». Chiffres signalés comme indicatifs par le rapport lui-même, à vérifier.
5. **Barème IR** : seuils cohérents entre texte (181 917) et CSV (181 918) à une unité près ; à contrôler sur service-public.fr.
6. **Formulaire 3916 et amende** : montants cohérents avec ce que je connais (1 500 € par compte, 10 000 € en État non coopératif), à confirmer.
7. Plusieurs URL citées sont longues ou tronquées (formulaire 3916, olympe.services pour les PS immobiliers) : source non officielle pour le taux de 17,2 % immobilier.
8. Les sources sont « consultées le 30 octobre 2026 » par l'autre IA : je n'ai pas de moyen de confirmer qu'elle les a vraiment lues.

---

## 1. Comment s'applique le Prélèvement Forfaitaire Unique (PFU) et quels sont ses taux actuels ?

**Réponse courte :** Le Prélèvement Forfaitaire Unique (PFU) est un impôt proportionnel s'appliquant par défaut aux revenus du capital mobilier. Depuis le 1er janvier 2026, son taux global a été porté à 31,4 % suite à une hausse des prélèvements sociaux.

**Détail :** Le PFU, instauré initialement en 2018 pour simplifier la taxation du capital, se décompose en deux volets distincts prélevés simultanément sur le montant brut des revenus. Le premier volet correspond à l'impôt sur le revenu, dont le taux reste figé à 12,8 %. Le second volet concerne les prélèvements sociaux, qui ont subi une modification majeure avec la loi de financement de la sécurité sociale (LFSS) pour 2026. Le taux des prélèvements sociaux sur les revenus de placements financiers est passé de 17,2 % à 18,6 %. Cette nouvelle ventilation des prélèvements sociaux de 18,6 % comprend la Contribution Sociale Généralisée (CSG) rehaussée à 10,6 %, la Contribution pour le Remboursement de la Dette Sociale (CRDS) à 0,5 %, et le prélèvement de solidarité maintenu à 7,5 %. Les produits concernés par ce taux global de 31,4 % incluent les dividendes, les intérêts des comptes à terme et livrets bancaires non réglementés, les plus-values sur cessions de valeurs mobilières, ainsi que la part de gains lors d'un rachat sur assurance vie (pour les primes versées après le 27 septembre 2017 excédant 150 000 euros). Il est fondamental de noter que la hausse des prélèvements sociaux à 18,6 % ne s'applique qu'aux revenus mobiliers. Les revenus fonciers classiques, les plus-values immobilières, et les revenus issus de la location nue restent soumis au taux historique de 17,2 %. Par ailleurs, les contribuables non-résidents affiliés à un régime de sécurité sociale d'un autre État de l'Espace Économique Européen (EEE) ou de la Suisse sont exemptés de CSG et de CRDS, ne redevant que le prélèvement de solidarité de 7,5 %.

**Piège fréquent ou erreur courante :** Une erreur récurrente consiste à appliquer le taux de 31,4 % à l'ensemble du patrimoine, en oubliant que l'immobilier en direct conserve des prélèvements sociaux à 17,2 %. Une autre confusion fréquente concerne les personnes non imposables : le PFU prélève systématiquement 12,8 % d'impôt sur le revenu, ce qui pénalise les foyers dont la tranche marginale est à 0 % s'ils n'optent pas pour le barème.

**Source(s) :** Service-Public.fr, https://www.service-public.fr/particuliers/vosdroits/F34913/1_7, consulté le 30 octobre 2026.

## 2. Quand l'option pour le barème progressif de l'impôt sur le revenu est-elle avantageuse et comment s'applique-t-elle ?

**Réponse courte :** L'option pour le barème progressif est financièrement avantageuse pour les contribuables situés dans les tranches d'imposition à 0 % et 11 %. Elle permet de bénéficier d'un abattement de 40 % sur les dividendes et de déduire une partie de la CSG.

**Détail :** Le contribuable a la faculté de renoncer à l'imposition forfaitaire de 12,8 % du PFU pour soumettre l'intégralité de ses revenus de capitaux mobiliers au barème progressif de l'impôt sur le revenu. Cette option, matérialisée par la case 2OP de la déclaration annuelle (formulaire 2042), présente un caractère global et irrévocable pour l'année d'imposition concernée. Le choix de cette option déclenche trois mécanismes fiscaux impossibles sous le régime du PFU. Premièrement, elle active un abattement de 40 % sur le montant brut des dividendes perçus, sous réserve que la société distributrice soit soumise à l'impôt sur les sociétés et résidente d'un État coopératif. Deuxièmement, elle rend déductible une fraction de la CSG payée sur ces revenus, à hauteur de 6,8 %, qui viendra minorer le revenu imposable de l'année suivante. Troisièmement, elle autorise la déduction des frais de garde et autres charges financières justifiées. L'option s'avère mathématiquement favorable pour un contribuable dont la Tranche Marginale d'Imposition (TMI) est de 11 %. Par exemple, pour 1000 euros de dividendes bruts, le PFU génère 128 euros d'impôt (12,8 %). Avec l'option au barème, l'abattement de 40 % réduit l'assiette à 600 euros. Appliqué à la TMI de 11 %, l'impôt s'élève à 66 euros. Les prélèvements sociaux de 18,6 % restent exigibles sur la base brute de 1000 euros dans les deux scénarios. Si la TMI est de 30 % ou plus, le PFU à 12,8 % redevient systématiquement plus favorable.

**Piège fréquent ou erreur courante :** Le caractère "global" de l'option est souvent ignoré. Cocher la case 2OP pour réduire l'impôt sur quelques dividendes entraîne automatiquement l'imposition au barème progressif de toutes les plus-values de cession de l'année, ce qui peut générer une charge fiscale dramatiquement supérieure si d'importantes plus-values mobilières ont été encaissées.

**Source(s) :** BOFiP, https://bofip.impots.gouv.fr/bofip/11224-PGP.html/identifiant=BOI-RPPM-RCM-20-15-20210621, consulté le 30 octobre 2026.

## 3. Quelles sont les règles fiscales et les plafonds applicables au PEA et au PEA-PME ?

**Réponse courte :** Le Plan d'Épargne en Actions (PEA) offre une exonération d'impôt sur le revenu sur les plus-values et dividendes après cinq ans de détention. Les plafonds de versement sont de 150 000 euros pour le PEA classique et de 225 000 euros pour le PEA-PME.

**Détail :** Le PEA bancaire est plafonné à 150 000 euros de versements nets, tandis que le PEA-PME bénéficie d'un plafond de 225 000 euros. Les jeunes majeurs rattachés au foyer fiscal de leurs parents disposent d'un PEA spécifique plafonné à 20 000 euros. Le cumul des versements sur un PEA et un PEA-PME par un même titulaire ne peut excéder 225 000 euros. La fiscalité de ces enveloppes est structurée autour du cap des cinq ans. Tout retrait effectué avant le cinquième anniversaire entraîne la clôture automatique et définitive du plan, sauf exceptions légales telles que le licenciement, l'invalidité, ou le retrait destiné à la création ou reprise d'une entreprise. En cas de retrait anticipé, le gain net est taxé au PFU de 31,4 % (12,8 % d'impôt et 18,6 % de prélèvements sociaux). Après le cinquième anniversaire, les retraits partiels n'entraînent plus la clôture du plan et les versements restent possibles dans la limite des plafonds. Les gains retirés après cinq ans bénéficient d'une exonération totale d'impôt sur le revenu, seuls les prélèvements sociaux de 18,6 % s'appliquent sur la fraction de gain comprise dans le retrait. Pour être éligibles au PEA, les titres en direct ou les fonds d'investissement doivent être investis à hauteur de 75 % au moins en actions de sociétés ayant leur siège dans l'Union Européenne ou l'Espace Économique Européen. Toutefois, l'ingénierie financière permet aux émetteurs d'ETF d'utiliser la réplication synthétique : le fonds détient un panier d'actions européennes (respectant le quota de 75 %) et échange la performance de ce panier contre celle d'un indice mondial ou américain via un contrat d'échange (swap), rendant ainsi des indices internationaux éligibles au PEA. Les dividendes perçus à l'intérieur du PEA sont exonérés et peuvent être réinvestis sans frottement fiscal, avec une limitation stricte pour les titres non cotés, dont l'exonération des dividendes est plafonnée à 10 % de la valeur d'acquisition de ces titres.

**Piège fréquent ou erreur courante :** Une erreur courante est de confondre la valeur du portefeuille et le plafond de versement. Le plafond de 150 000 euros s'applique uniquement au capital injecté par l'investisseur. Si le portefeuille croît à 300 000 euros grâce aux plus-values, le PEA est en parfaite conformité. Une autre erreur est d'effectuer un retrait de "test" la première année, ce qui détruit irrémédiablement l'enveloppe fiscale.

**Source(s) :** Service-Public.fr, https://www.service-public.gouv.fr/particuliers/vosdroits/F2385, consulté le 30 octobre 2026.

## 4. Quelle est la fiscalité de l'assurance vie en cas de rachat et lors de la succession ?

**Réponse courte :** L'assurance vie permet de bénéficier d'abattements annuels sur les gains lors des rachats après huit ans. En cas de décès, elle offre un cadre dérogatoire puissant permettant de transmettre des capitaux hors succession avec des abattements très élevés.

**Détail :** La fiscalité en cas de vie dépend de l'ancienneté du contrat et de la date des versements. L'architecture du contrat distingue les fonds en euros (capital garanti, rendement annuel) et les Unités de Compte (actions, obligations, SCPI, ETF, sans garantie en capital). Lors d'un rachat (retrait), seule la part de gain est taxée. Si le contrat a moins de huit ans, les gains issus des primes versées après le 27 septembre 2017 sont imposés au PFU (12,8 % d'impôt plus 18,6 % de prélèvements sociaux). Après le huitième anniversaire du contrat, un abattement fiscal annuel est accordé sur la part de gain retirée : 4 600 euros pour une personne seule, et 9 200 euros pour un couple soumis à imposition commune. Au-delà de cet abattement, le taux d'impôt dépend de l'encours global des primes nettes versées par l'assuré sur l'ensemble de ses contrats. Si cet encours est inférieur à 150 000 euros, le taux d'imposition est réduit à 7,5 % (plus les prélèvements sociaux). Si l'encours excède 150 000 euros, la fraction des gains correspondant aux primes sous ce seuil est taxée à 7,5 %, tandis que la fraction liée aux primes au-dessus du seuil est taxée à 12,8 %. L'attrait principal de l'assurance vie réside dans sa fiscalité successorale. Selon l'article 990 I du Code général des impôts, pour les primes versées avant le soixante-dixième anniversaire de l'assuré, le capital transmis à chaque bénéficiaire profite d'un abattement de 152 500 euros. La fraction excédant cet abattement est taxée à 20 % jusqu'à un plafond de 700 000 euros (soit 852 500 euros transmis au total), et à 31,25 % au-delà de cette limite. Si les primes ont été versées après le soixante-dixième anniversaire, c'est l'article 757 B qui s'applique : un abattement unique et global de 30 500 euros est partagé entre l'ensemble des bénéficiaires, mais cet abattement ne s'applique que sur les primes versées. La totalité des plus-values générées par ces primes est entièrement exonérée de droits de succession.

**Piège fréquent ou erreur courante :** Penser que les fonds sont bloqués pendant huit ans. L'assurance vie reste un placement liquide dont l'épargne peut être rachetée à tout moment. La barrière des huit ans ne concerne que l'optimisation fiscale via l'abattement de 4 600 ou 9 200 euros.

**Source(s) :** Légifrance, Article 990 I du CGI, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047288653, consulté le 30 octobre 2026.

## 5. Comment sont imposés les revenus d'un Compte-Titres Ordinaire (CTO) et quelles sont les contraintes liées aux actifs étrangers ?

**Réponse courte :** Le CTO n'offre aucun avantage fiscal spécifique. Les plus-values et dividendes sont taxés annuellement au PFU (31,4 %), avec la possibilité d'imputer les moins-values sur dix ans, tout en exigeant des déclarations rigoureuses pour les comptes et revenus étrangers.

**Détail :** Sur un CTO, chaque encaissement de dividende et chaque plus-value de cession déclenche le paiement du PFU (12,8 % d'impôt et 18,6 % de prélèvements sociaux pour 2026) l'année de réalisation. En cas de cession générant une moins-value, celle-ci s'impute obligatoirement sur les plus-values de même nature réalisées la même année. Si le solde global de l'année est négatif, cette moins-value nette est reportable et imputable sur les plus-values des dix années suivantes. L'utilisation d'un CTO implique souvent la détention d'actifs étrangers, ce qui soulève plusieurs contraintes réglementaires. Les investisseurs particuliers ne peuvent plus accéder directement aux ETF domiciliés aux États-Unis. La réglementation européenne PRIIPs exige en effet la remise d'un Document d'Informations Clés (DIC / KID) rédigé en français avant toute souscription. Les émetteurs américains (comme Vanguard ou State Street aux États-Unis) ne produisant pas ce document au format européen, l'Autorité des Marchés Financiers (AMF) interdit formellement aux courtiers de proposer ces produits à la clientèle de détail résidant en France. Par ailleurs, la perception de dividendes étrangers entraîne généralement l'application d'une retenue à la source par le pays d'origine (par exemple, 15 % pour les actions américaines si le formulaire W-8BEN a été complété). Ces revenus de source étrangère doivent être reportés sur le formulaire déclaratif 2047, ce qui permet à l'administration fiscale d'octroyer un crédit d'impôt équivalent à la retenue subie, neutralisant ainsi la double imposition. Enfin, tout CTO ouvert auprès d'un courtier dont le siège est situé hors de France (comme Trade Republic en Allemagne ou Interactive Brokers en Irlande) doit être impérativement déclaré chaque année via le formulaire 3916.

**Piège fréquent ou erreur courante :** Omettre de remplir le formulaire 3916 pour déclarer un compte-titres étranger. L'administration fiscale sanctionne cet oubli par une amende fixe de 1 500 euros par compte non déclaré et par année, amende qui est portée à 10 000 euros si l'établissement est situé dans un État ou territoire non coopératif.

**Source(s) :** AMF, Position-Recommandation DOC-2020-03, https://www.amf-france.org, consulté le 30 octobre 2026 ; BOFiP, https://bofip.impots.gouv.fr/bofip/7151-PGP.html/identifiant=BOI-RPPM-PVBMI-20-30-20-20141014.

## 6. Quelles sont les règles de déductibilité du Plan d'Épargne Retraite (PER) et la fiscalité applicable à la sortie ?

**Réponse courte :** Le PER permet de déduire les versements de ses revenus imposables, offrant un gain fiscal immédiat proportionnel à sa tranche d'imposition. En contrepartie, le capital et les plus-values sont lourdement taxés lors du déblocage à la retraite.

**Détail :** Le PER est une enveloppe de capitalisation bloquée conçue pour la préparation à la retraite. Les versements volontaires réalisés par l'investisseur sont déductibles de son revenu net global, dans la limite d'un plafond personnalisé calculé chaque année. Pour un salarié, ce plafond s'élève à 10 % des revenus d'activité professionnelle de l'année précédente, avec un minimum garanti d'environ 4 710 euros et un maximum de 37 680 euros (données indicatives pour la base 2025/2026). Le reliquat de plafond non utilisé est reportable sur les trois années suivantes. L'épargne est strictement bloquée jusqu'à la liquidation de la retraite, à l'exception de cas de déblocage anticipé couvrant les "accidents de la vie" (décès du conjoint, invalidité, surendettement, expiration des droits au chômage, liquidation judiciaire). Dans ces cas de force majeure, la sortie en capital bénéficie d'une exonération totale d'impôt sur le revenu, la part de gains ne subissant que les prélèvements sociaux. L'acquisition de la résidence principale constitue également un motif de déblocage anticipé, mais la fiscalité reste alors identique à une sortie à l'âge de la retraite. Lors du déblocage normal à la retraite, si l'investisseur a opté pour la déduction fiscale à l'entrée, la sortie en capital est imposée de manière scindée : la fraction correspondant aux versements initiaux est réintégrée au revenu imposable et soumise au barème progressif (sans l'abattement de 10 % des pensions), tandis que la fraction correspondant aux plus-values est taxée au PFU de 31,4 %. En cas de sortie en rente viagère, celle-ci est soumise au régime des pensions de retraite. Le PER s'avère particulièrement pertinent pour les investisseurs subissant une Tranche Marginale d'Imposition (TMI) élevée (30 %, 41 % ou 45 %) durant leur vie active, et qui anticipent une baisse de leurs revenus (et donc de leur TMI) à la retraite, réalisant ainsi un arbitrage fiscal positif.

**Piège fréquent ou erreur courante :** Ouvrir un PER en début de carrière alors que la TMI est de 0 % ou 11 %. Dans ce scénario, le gain fiscal à l'entrée est dérisoire, l'épargne est bloquée pendant des décennies, et le capital risque d'être taxé à une TMI supérieure à la retraite si les revenus ont augmenté entre-temps.

**Source(s) :** Service-Public.fr, https://www.service-public.gouv.fr/particuliers/vosdroits/F34982, consulté le 30 octobre 2026.

## 7. Comment se structure le barème de l'impôt sur le revenu et la contribution sur les hauts revenus ?

**Réponse courte :** Le calcul de l'impôt repose sur un barème progressif à cinq tranches (de 0 % à 45 %) appliqué au quotient familial. Une contribution exceptionnelle (CEHR) s'ajoute pour les foyers dépassant des seuils de revenus très élevés.

**Détail :** Le mécanisme central de l'impôt sur le revenu repose sur le barème progressif, qui s'applique après division du revenu net imposable du foyer par le nombre de parts du quotient familial. Pour les revenus de 2025 déclarés en 2026, la LFSS et la loi de finances ont réévalué les tranches d'imposition pour compenser l'inflation. Les seuils en vigueur sont les suivants : la tranche à 0 % s'applique jusqu'à 11 600 euros par part ; la tranche à 11 % couvre les revenus de 11 601 à 29 579 euros ; la tranche à 30 % de 29 580 à 84 577 euros ; la tranche à 41 % de 84 578 à 181 917 euros ; et la tranche maximale à 45 % s'applique à la fraction des revenus supérieure à 181 917 euros. Le quotient familial attribue une part pour un célibataire et deux parts pour un couple marié ou pacsé, avec des demi-parts supplémentaires pour les enfants à charge. L'avantage fiscal procuré par chaque demi-part liée à un enfant est strictement plafonné à 1 807 euros (plafond de base 2026). En sus de ce barème, l'article 223 sexies du Code général des impôts institue la Contribution Exceptionnelle sur les Hauts Revenus (CEHR). Cette surtaxe frappe le revenu fiscal de référence global. Pour une personne seule, elle s'élève à 3 % sur la fraction de revenu comprise entre 250 000 et 500 000 euros, et à 4 % au-delà de 500 000 euros. Pour un couple soumis à imposition commune, ces seuils sont doublés (3 % de 500 000 à 1 000 000 euros, et 4 % au-delà).

**Piège fréquent ou erreur courante :** La confusion entre le taux marginal d'imposition (TMI) et le taux moyen. Atteindre la tranche à 30 % signifie qu'uniquement la fraction des revenus dépassant 29 580 euros par part sera taxée à 30 %. Le taux moyen global de l'impôt par rapport au revenu total sera toujours nettement inférieur.

**Source(s) :** Service-Public.fr, https://www.service-public.fr/particuliers/vosdroits/F1419, consulté le 30 octobre 2026.

## 8. Comment déclarer les cessions de crypto-actifs et quels formulaires utiliser ?

**Réponse courte :** Les plus-values sur crypto-actifs ne sont imposables que lors d'une conversion en monnaie traditionnelle (fiat) ou d'un achat de bien. Elles sont taxées au PFU via le formulaire 2086, et les comptes étrangers doivent être déclarés.

**Détail :** Le régime fiscal applicable aux actifs numériques, régi par l'article 150 VH bis du Code général des impôts, repose sur un principe de sursis d'imposition pour les opérations inter-cryptos. Concrètement, échanger du Bitcoin contre de l'Ethereum ne déclenche aucun événement fiscal. Le fait générateur de l'impôt survient exclusivement lors de la cession d'un crypto-actif contre une monnaie ayant cours légal (euros, dollars) ou lors de l'utilisation d'une cryptomonnaie pour acquérir un bien ou un service matériel. La plus-value réalisée lors de ces opérations est imposée au PFU au taux global de 31,4 %. Le calcul de la plus-value brute imposable est complexe, car il exige d'évaluer la valeur totale du portefeuille d'actifs numériques (toutes plateformes confondues) à la seconde précise de chaque transaction en euros, afin d'extraire la quote-part de gain associée à la cession. L'ensemble de ces transactions taxables et le détail des calculs doivent être renseignés dans l'annexe n° 2086 accompagnant la déclaration de revenus. En parallèle, l'investisseur est tenu de déclarer chaque année tous ses comptes d'actifs numériques ouverts, détenus, utilisés ou clos auprès de plateformes d'échange domiciliées à l'étranger (telles que Binance, Kraken ou Coinbase) via le formulaire spécifique 3916-bis.

**Piège fréquent ou erreur courante :** Oublier de déclarer les dépenses quotidiennes effectuées avec une carte de paiement crypto (ex: carte Visa Binance). Chaque paiement chez un commerçant opère techniquement une conversion de crypto vers l'euro, constituant ainsi une cession imposable qui doit être traçable et déclarée sur le formulaire 2086.

**Source(s) :** Impots.gouv.fr, https://www.impots.gouv.fr/formulaire/2086/declaration-des-plus-ou-moins-values-de-cessions-dactifs-numeriques, consulté le 30 octobre 2026.

## 9. Quel est le calendrier déclaratif annuel et quels formulaires annexes maîtriser ?

**Réponse courte :** La campagne déclarative se déroule au printemps. Le contribuable doit consolider les données préremplies de l'IFU sur le formulaire 2042 et remplir les annexes indispensables pour les revenus étrangers, les plus-values complexes et les comptes hors de France.

**Détail :** Chaque année, l'administration fiscale ouvre le portail de télédéclaration en avril pour la déclaration des revenus perçus durant l'année civile précédente. Les dates limites s'échelonnent entre la fin mai et le début juin, selon un calendrier défini par le département de résidence. Pour faciliter cette démarche, les établissements financiers français émettent au premier trimestre un Imprimé Fiscal Unique (IFU) résumant les montants à reporter. Le formulaire central est la déclaration 2042. S'y greffent plusieurs formulaires spécifiques incontournables pour l'investisseur intermédiaire : la 2042-C pour les revenus de capitaux mobiliers non préremplis et certains reports ; le formulaire 2047, dédié aux revenus encaissés à l'étranger (dividendes étrangers, intérêts) permettant le calcul des crédits d'impôt ; le formulaire 2074 pour la déclaration détaillée des plus-values mobilières (lorsque le courtier ne fournit pas de calcul consolidé ou pour reporter des moins-values) ; le formulaire 2086 pour calculer la plus-value sur les crypto-actifs ; et enfin, le formulaire combiné 3916-3916 bis, obligatoire pour déclarer l'existence de comptes bancaires, de comptes-titres ou de comptes d'actifs numériques ouverts, détenus ou clos à l'étranger.

**Piège fréquent ou erreur courante :** Considérer que l'IFU prérempli par les courtiers français est infaillible et ne nécessite aucune vérification, particulièrement pour les revenus de source étrangère où les conventions fiscales internationales appliquent des retenues à la source qui nécessitent souvent des corrections manuelles sur la 2047. De plus, les courtiers étrangers ne fournissent généralement pas d'IFU aux normes de l'administration française, laissant l'entière responsabilité du calcul à l'investisseur.

**Source(s) :** Impots.gouv.fr, https://www.impots.gouv.fr/formulaire/3916/declaration-par-un-resident-dun-compte-letranger-ou-dun-contrat-de-capitalisation-o, consulté le 30 octobre 2026.

---

## Tableau comparatif : PEA / AV / CTO / PER

| Caractéristique | PEA | Assurance vie | CTO | PER |
|---|---|---|---|---|
| Plafond de versement | 150 000 € pour le PEA classique (225 000 € cumulés avec PEA-PME) | Aucun plafond légal | Aucun plafond | Aucun plafond de dépôt, mais déductibilité plafonnée annuellement |
| Fiscalité à la sortie (gains) | Après 5 ans : exonération d'IR, prélèvements sociaux de 18,6 % dus | Après 8 ans : abattement annuel (4 600 € / 9 200 €) puis PFL 7,5 % ou 12,8 % + 18,6 % PS | PFU de 31,4 % ou option barème progressif de l'IR | Capital réintégré au barème de l'IR, gains taxés au PFU (31,4 %) |
| Durée minimale | 5 ans pour acquérir l'exonération fiscale | Aucune durée de blocage, mais 8 ans pour optimisation fiscale maximale | Aucune | Épargne bloquée jusqu'à l'âge de la retraite (sauf cas exceptionnels) |
| Liquidité | Cédable à tout moment, mais un retrait avant 5 ans entraîne la clôture définitive | Totalement liquide, rachat partiel ou total possible à tout moment | Totalement liquide | Illiquide par conception, blocage des fonds |
| Avantage succession | Aucun (réintégration à l'actif successoral, bien que les plus-values latentes soient purgées d'IR) | Majeur (art. 990 I : abattement 152 500 € par bénéficiaire si primes < 70 ans) | Aucun (réintégration à l'actif successoral) | Avantage selon l'âge au décès, similaire à l'assurance vie en cas de décès avant liquidation |

## Exemples chiffrés de simulation de vente

### Simulation 1 : Compte-Titres Ordinaire (CTO) au PFU

Un investisseur cède un ETF mondial sur son CTO avec une plus-value latente. Il n'a aucune moins-value en report.

- Prix d'acquisition total (PRU) : 5 000 €
- Valeur de cession (revente) : 8 000 €
- Plus-value brute réalisée : 3 000 €
- Imposition applicable : PFU à 31,4 % (12,8 % impôt sur le revenu + 18,6 % prélèvements sociaux)
- Montant de l'impôt dû : 3 000 € × 31,4 % = 942 €
- Capital net restitué à l'investisseur : 8 000 € - 942 € = 7 058 €

### Simulation 2 : PEA de plus de 5 ans

L'investisseur effectue un retrait partiel de 8 000 € sur un PEA ouvert il y a 6 ans. L'enveloppe ne sera pas clôturée. L'ensemble du portefeuille vaut 24 000 €, constitué de 15 000 € de versements et 9 000 € de gains latents. La part de gain dans le portefeuille est de 37,5 % (9 000 / 24 000).

- Retrait brut souhaité : 8 000 €
- Quote-part de gain contenue dans le retrait : 8 000 € × 37,5 % = 3 000 €
- Imposition applicable : le plan ayant plus de 5 ans, l'impôt sur le revenu est exonéré (0 %). Seuls les prélèvements sociaux de 18,6 % s'appliquent sur le gain.
- Montant de l'impôt dû : 3 000 € × 18,6 % = 558 € (prélevés à la source par la banque)
- Capital net restitué à l'investisseur : 8 000 € - 558 € = 7 442 €

### Simulation 3 : Assurance vie de plus de 8 ans

Un investisseur célibataire retire de l'argent de son assurance vie ouverte il y a 10 ans. Les primes totales versées sur le contrat s'élèvent à 100 000 € (inférieur au seuil de 150 000 €).

- Retrait brut souhaité : 15 000 €. Le calcul de la quote-part détermine que ce retrait inclut 6 000 € de gains.
- Abattement annuel disponible pour un célibataire : 4 600 €
- Assiette imposable à l'impôt sur le revenu : 6 000 € - 4 600 € = 1 400 €
- Impôt sur le revenu (taux réduit à 7,5 %) : 1 400 € × 7,5 % = 105 €
- Prélèvements sociaux (18,6 % sur la totalité du gain avant l'abattement) : 6 000 € × 18,6 % = 1 116 €
- Montant de l'impôt total dû : 105 € + 1 116 € = 1 221 €
- Capital net restitué à l'investisseur : 15 000 € - 1 221 € = 13 779 €

## Ce qui a changé récemment

Au cours des 24 derniers mois, l'évolution la plus structurante pour les investisseurs a été la promulgation de la loi de financement de la sécurité sociale pour 2026, qui a acté une hausse de la fiscalité sur l'épargne. Les prélèvements sociaux affectés aux revenus du capital mobilier ont été rehaussés de 17,2 % à 18,6 %, portant de fait le Prélèvement Forfaitaire Unique (PFU) à un taux global de 31,4 %. Cette modification cible spécifiquement la détention de valeurs mobilières et de liquidités, car les revenus fonciers (location nue, SCPI en direct) ainsi que les plus-values immobilières restent exemptés de cette hausse et maintenus au taux historique de 17,2 %. Cette asymétrie modifie les calculs de rendement net lors des arbitrages entre actifs financiers et actifs tangibles. Par ailleurs, sur le plan réglementaire, l'application stricte de la directive européenne PRIIPs a définitivement évincé les ETF de droit américain des portefeuilles des investisseurs de détail européens. L'incapacité réglementaire des gestionnaires d'actifs américains à produire un Document d'Informations Clés (KID) en français a conduit l'Autorité des Marchés Financiers à verrouiller les plateformes de courtage, forçant les investisseurs à se replier vers des fonds répliquant ces indices domiciliés en Irlande ou au Luxembourg (format UCITS).

## Ce que je n'ai pas pu trancher

L'impact exact du nouveau taux de prélèvements sociaux à 18,6 % sur les Sociétés Civiles de Placement Immobilier (SCPI) logées au sein d'un contrat d'assurance vie reste à vérifier. Bien que la détention de SCPI en direct génère des revenus fonciers taxés à 17,2 %, la jurisprudence fiscale considère qu'un rachat sur un contrat d'assurance vie produit des revenus de capitaux mobiliers, sans faire de transparence sur la nature des actifs sous-jacents (fonds euros, actions, ou parts de SCPI). La doctrine administrative n'a pas encore clarifié explicitement si un traitement d'exception (maintien à 17,2 %) serait appliqué par transparence à la fraction de gain issue des unités de compte immobilières au sein de l'assurance vie, ou si la qualification mobilière de l'enveloppe imposera inexorablement le taux de 18,6 %. La pratique des assureurs, chargés de prélever cet impôt à la source, tend vers l'application stricte de la nature de l'enveloppe, mais des précisions du Bulletin officiel des finances publiques (BOFiP) sont attendues.

## Sources utilisées

- Service-Public.fr, Les prélèvements sociaux : https://www.service-public.fr/particuliers/vosdroits/F2329
- Service-Public.fr, Imposition des revenus de valeurs mobilières (PFU et barème) : https://www.service-public.fr/particuliers/vosdroits/F34913/1_7
- Service-Public.fr, Fonctionnement et fiscalité du PEA : https://www.service-public.gouv.fr/particuliers/vosdroits/F2385
- Service-Public.fr, Fiscalité de l'assurance vie : https://www.service-public.gouv.fr/particuliers/vosdroits/F22414
- Service-Public.fr, Fonctionnement et déductibilité du PER : https://www.service-public.gouv.fr/particuliers/vosdroits/F34982
- Service-Public.fr, Tranches du barème de l'impôt sur le revenu : https://www.service-public.fr/particuliers/vosdroits/F1419
- Impots.gouv.fr, Déclaration des comptes à l'étranger (formulaire 3916) : https://www.impots.gouv.fr/formulaire/3916/declaration-par-un-resident-dun-compte-letranger-ou-dun-contrat-de-capitalisation-o
- Impots.gouv.fr, Déclaration des actifs numériques (formulaire 2086) : https://www.impots.gouv.fr/formulaire/2086/declaration-des-plus-ou-moins-values-de-cessions-dactifs-numeriques
- Impots.gouv.fr, Déclaration des revenus étrangers (formulaire 2047) : https://www.impots.gouv.fr/formulaire/2047/declaration-des-revenus-encaisses-letranger
- BOFiP, Option globale pour le barème progressif : https://bofip.impots.gouv.fr/bofip/11224-PGP.html/identifiant=BOI-RPPM-RCM-20-15-20210621
- BOFiP, Imputation des moins-values (10 ans) : https://bofip.impots.gouv.fr/bofip/7151-PGP.html/identifiant=BOI-RPPM-PVBMI-20-30-20-20141014
- Légifrance, Fiscalité en cas de décès (articles 990 I et 757 B du CGI) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047288653 et https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047288569
- AMF, Réglementation PRIIPs / KID : https://www.amf-france.org/en/amf-ombudsman/ombudsman-online-diary/latest/application-priips-regulation-what-happens-us-packaged-products-subscribed-regulation-came-forceExtrait de code
