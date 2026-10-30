---
name: manuel-conseiller-budget
description: Manuel de compétences du Conseiller budget (épargne de précaution, dettes, budget, arnaques, prévoyance). Chargé automatiquement dans l'agent conseiller-budget.
---

# Manuel de compétences du Conseiller budget

Fusion des meilleurs skills open source (joellewis, lyndonkl, onewave), adaptés à la France : livrets réglementés, assurances, fiscalité française. Chiffres de référence : fiche A (taux et plafonds vérifiés), fiche I. Ouvre seulement la section utile.

## 1. Épargne de précaution
*Base : `emergency-fund`.*
- **Montant** = dépenses **essentielles** mensuelles × mois de couverture (logement, alimentation, assurances, énergie et internet, transport, remboursements minimums, santé ; **pas** sorties, voyages, abonnements résiliables). 3 à 6 mois pour un salarié stable ; **3 mois** peuvent suffire dans un couple à deux revenus stables ; **6 à 12 mois** pour un revenu variable, un indépendant, un métier de niche.
- Revenu variable : moyenne sur 12 à 24 mois, budget de base calé sur les 3 pires mois, plus un « tampon de lissage » séparé du fonds d'urgence.
- **Paliers** : 1 mois sur le compte courant (accès immédiat) ; 2 à 3 mois sur Livret A ou LDDS (LEP d'abord si on y a droit) ; le reste en livrets aussi (en France, pas besoin d'un étage plus risqué). Taux du moment : fiche A, point 83 (Livret A 1,7 %, LEP 2,5 % depuis le 1er août 2026).
- **Coût d'opportunité** : avec l'inflation à 3,1 % en septembre 2026, le rendement réel d'un livret est négatif. C'est le prix d'une assurance : ne pas dépasser 6 mois (12 mois de réserve = capital qui dort).
- **Quand y puiser** (à décider à l'avance) : perte de revenu, urgence médicale, réparation indispensable. Pas pour une promotion, un « bon plan » ou une opportunité de marché. **Reconstituer en priorité** après usage.

## 2. Plan de dépenses et suivi
*Base : `finance-psychology` (4 enveloppes), `budget-optimizer`, `financial-parser`, `category-trend-analyzer`, `transaction-categorizer`, `household-finance-dashboard-builder`.*
- **Quatre enveloppes** (fiche A, point 109) : charges fixes 50 à 60 % du net, investissement 10 % ou plus, épargne pour projets 5 à 10 %, plaisir sans culpabilité 20 à 35 %. Le mot « budget » braque : parler de plan.
- **Catégoriser** les dépenses à partir des relevés (CSV de la banque) : besoins / envies / épargne, avec une table de règles par libellé qu'on corrige une fois ; repérer les paiements récurrents.
- **Suivi par catégorie** : dépense du mois, moyenne glissante sur 6 mois, écart sur un an, écart avec le plan. Alerter sur les hausses nettes, pas sur chaque variation.
- **Tableau de bord du foyer** : une page (revenus, dépenses par catégorie, taux d'épargne, épargne de précaution en mois, dettes, patrimoine net) ; générer avec `scripts/creer_sheet.py`.
- **Taux d'épargne** : comparer à 50/30/20 puis à 30 % (fiche A, points 2 et 82). Rembourser le capital d'un crédit compte comme de l'épargne.
- Mensualiser les dépenses annuelles pour connaître le vrai reste à vivre.

## 3. Trésorerie du foyer
*Base : `cash-flow-forecaster`, `liquidity-management`.* Projeter 30 à 90 jours : solde actuel, entrées prévues (salaire, primes), sorties récurrentes et annuelles (assurances, impôts, taxe foncière, vacances), points bas. Prévenir **avant** un découvert ; décider d'avance où prendre l'argent d'une grosse dépense.

## 4. Dettes et crédit
*Base : `debt-management`, `lending`.*
- **Avalanche** (taux le plus haut d'abord : le moins cher) contre **boule de neige** (la plus petite dette d'abord : plus motivant). Choisir celle que la personne tiendra.
- **Rapport dette/revenus** : jusqu'à 35 % assurance comprise (recommandation du HCSF).
- **Rembourser ou investir** : comparer le taux du crédit au rendement net espéré **après risque** ; au-dessus de 5-6 % rembourser d'abord. Pour un crédit immobilier à taux bas, les deux peuvent cohabiter ; ne pas vider son épargne de précaution pour rembourser.
- **Renégocier ou racheter un crédit** : calculer le point mort (frais divisés par l'économie mensuelle) ; regroupement de crédits : vérifier le coût total, pas la mensualité.
- Bonnes et mauvaises dettes : une dette qui finance un actif utile à taux raisonnable peut se défendre ; un crédit renouvelable ne se défend pas.
- Seuil de l'usure : repère pour repérer les offres abusives (fiche A).

## 5. Revenus et négociation
*Base : `raise-negotiation-prep`.* Préparer : valeur de marché de son poste (offres, enquêtes salariales), réalisations chiffrées (euros, délais, clients), rémunération globale (variable, intéressement, participation, abondement, avantages), moment (après un résultat, lors de l'entretien annuel), scénarios de réponse. Prime ou augmentation : au moins la moitié vers l'investissement (fiche A, point 7). Activité annexe : fiche A, point 88.

## 6. Assurances et prévoyance
*Base : `insurance-planning`, `cowork-medical-bill-auditor`, `cowork-home-inventory`.*
- **Utiles** : mutuelle santé, responsabilité civile, assurance habitation, prévoyance décès-invalidité si des proches dépendent du revenu, assurance emprunteur (changement possible avec la loi Lemoine). **À éviter** : garanties de téléphone ou d'électroménager, couvertures pleines d'exclusions. Auto-assurer les petits sinistres.
- **Factures médicales** : rapprocher chaque facture du remboursement de la mutuelle, repérer doublons et frais non remboursés à contester.
- **Inventaire du logement** : photos et factures des biens de valeur, valeur de remplacement, stocké hors du domicile ; aide en cas de sinistre.
- Revue annuelle (fiche I, points 107 et 108).

## 7. Lire un contrat
*Base : `contract-analyzer`.* Repérer : durée et reconduction tacite, préavis et frais de résiliation, hausses unilatérales, frais cachés, exclusions, clauses de pénalité. Faire une liste « à négocier » et « à refuser ». Rappel : aide à la lecture, pas un avis juridique.

## 8. Détection d'anomalies et fraudes
*Base : `anomaly-fraud-scanner`.* Sur les relevés : prélèvement en double sous 48 heures, montant à plus de 3 écarts-types de d'habitude, nouveau bénéficiaire inconnu, abonnement jamais utilisé. À signaler à la banque rapidement (fiche I, points 100 à 106).

## 9. Priorités
Voir fiche A, point 111 : précaution, abondement employeur, dettes chères, PEA, assurance vie, projets. Se concentrer sur les grandes manettes avant les petites économies. Couple : point argent mensuel d'une heure (manuel du Coach, section 1).

---
Sources : joellewis/finance_skills (MIT) : emergency-fund, debt-management, lending, insurance-planning, liquidity-management, finance-psychology. onewave-ai (MIT) : budget-optimizer, financial-parser, raise-negotiation-prep, cowork-medical-bill-auditor, cowork-home-inventory, contract-analyzer. lyndonkl (pas de licence, idées reformulées) : household-finance-dashboard-builder, category-trend-analyzer, transaction-categorizer, cash-flow-forecaster, anomaly-fraud-scanner.
