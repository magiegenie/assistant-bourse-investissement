# Cahier des charges MVP

Version 1, 30/10/2026. Les réponses marquées **(hypothèse)** ont été choisies par défaut, à corriger si besoin.

---

## 1. Mission

Un assistant pour deux investisseurs débutants à intermédiaires, qui investissent sur le long terme.

**Deux objectifs mesurables :**
1. **Augmenter le rendement annuel net**, en jouant sur les leviers qui marchent vraiment : frais bas, bonne diversification, régularité, rester investi, enveloppes fiscales adaptées.
2. **Réduire le stress**, avec moins de décisions impulsives et une information triée (seulement ce qui compte pour nos lignes).

**Ce que l'assistant ne fait pas :** il ne prédit pas, ne donne pas de "bon plan", ne passe aucun ordre.

---

## 2. Les utilisateurs

| | Utilisateur 1 | Utilisateur 2 |
|---|---|---|
| Niveau | Débutant à intermédiaire | Débutant à intermédiaire |
| Style | Long terme, versements réguliers | Long terme |
| Actifs | Principalement ETF | Principalement ETF, quelques actions |
| Enveloppes | À renseigner dans le profil privé | À renseigner dans le profil privé |
| Temps disponible | 1 h par semaine maximum | idem |

Les informations réelles de chacun sont uniquement dans `prive/<prenom>/` (jamais versionné).

Portefeuilles **séparés**, avec visibilité mutuelle complète **(hypothèse)**. Chaque utilisateur a son dossier privé `prive/<prenom>/`.

---

## 3. Les 5 fonctions du MVP

### F1. Profil utilisateur
- Fichier YAML : prénom, horizon, objectif, enveloppes, allocation cible, tolérance au risque, canal de réception.
- **Règles par défaut** (en attendant la charte d'investissement) :
  - aucune ligne hors ETF monde au-dessus de 10 % du portefeuille
  - crypto plafonnée à 10 % du total
  - pas d'achat ou de vente hors plan sans délai de 24 h
  - versement mensuel programmé, quoi qu'il arrive sur les marchés

### F2. Données
- **Un Google Sheet par personne**, sur un modèle commun (onglet `Transactions`) :
  `date | enveloppe | type (achat, vente, dividende, versement, frais) | ticker ou ISIN | nom | quantité | prix unitaire | devise | frais`
- Lecture seule par l'assistant. Écriture uniquement dans un onglet `Journal`.
- Prix : yfinance (ETF, actions) et CoinGecko (crypto). Gratuit.
- News : flux RSS (Reuters, Les Echos, Boursorama, Zonebourse) + calendrier macro.
- Contrôle qualité à chaque lecture : doublons, devises, frais manquants.

### F3. Radiographie du portefeuille
Calculs faits en Python (jamais de tête), commentés ensuite par Claude.
- Valeur, plus-values, **performance réelle** (XIRR) depuis le début et sur l'année.
- **Comparaison à un ETF MSCI World** sur la même période et avec les mêmes versements.
- Répartition par zone, secteur, devise, enveloppe. Transparence des ETF : exposition réelle (ex. "tu as 5 % de Nvidia sans le savoir").
- Frais totaux par an et projetés sur 20 ans.
- Écart à l'allocation cible et **montant à placer sur chaque ligne au prochain versement** pour rééquilibrer sans rien vendre.
- **Score de santé sur 100** : diversification, frais, concentration, respect des règles.
- Envoyé à la demande, et automatiquement chaque dimanche.

### F4. Brief du matin
- **8 h, du lundi au vendredi, sur Telegram**, un par personne. Lecture en 2 minutes maximum.
- Contenu, dans l'ordre :
  1. Ton portefeuille hier : variation en % et en euros, et les lignes qui expliquent le mouvement.
  2. Les 3 infos qui touchent tes lignes (macro, politique, entreprises), avec la source et un niveau d'importance (à ignorer, à surveiller, à agir).
  3. L'agenda du jour (Fed, BCE, inflation, résultats).
  4. **Le verdict : "rien à faire aujourd'hui"** dans 95 % des cas, avec la raison.
  5. Une notion expliquée en 3 lignes, liée à l'actualité du jour.
- Si le marché baisse de plus de 3 % : un message de mise en perspective (historique des baisses, rappel du plan) plutôt qu'une alarme.

### F5. Garde-fou de décision
- Commande Telegram `/decision` avant tout achat ou vente hors plan.
- L'assistant demande : quoi, combien, pourquoi, pourquoi maintenant, ce qui invaliderait l'idée.
- Il vérifie : règles du profil, impact sur la diversification, frais, fiscalité de l'enveloppe.
- Il donne **les arguments contre** (avocat du diable), puis un verdict : conforme au plan, à reporter de 24 h, ou contraire aux règles.
- Tout est enregistré dans le journal. Rappel à 3 mois : "ta décision, bilan ?"

---

## 4. Commandes Telegram

| Commande | Effet |
|---|---|
| `/point` | Radiographie rapide du portefeuille |
| `/decision` | Garde-fou avant un achat ou une vente |
| `/explique <sujet>` | Explication simple d'une notion ou d'une news |
| `/pistes` | Trous de diversification et pistes à étudier (zones, secteurs, classes d'actifs) |
| `/journal` | Dernières décisions et leur bilan |

---

## 5. Choix techniques

- **Langage** : Python.
- **Exécution** : GitHub Actions (gratuit, tourne même PC éteint) pour le brief de 8 h et le rapport du dimanche. Bot Telegram hébergé gratuitement (Railway ou Render) pour les commandes.
- **IA** : API Claude (Haiku pour le brief, Sonnet pour les analyses).
- **Accès au Sheet** : compte de service Google, avec le Sheet partagé en lecture.
- **Budget** : moins de 10 euros par mois, essentiellement l'API Claude.
- **Secrets** : `.env` en local, secrets GitHub en ligne. Jamais dans le code.

Structure :
```
profiles/     un YAML par personne
data/         connecteurs (Sheets, prix, news)
analytics/    calculs (performance, répartition, frais, score)
agents/       prompts et appels Claude
reports/      brief, radiographie, décision
bot/          bot Telegram
tests/        tests des calculs
```

---

## 6. Hors MVP (V1 et après)

Charte d'investissement écrite, coût des émotions en euros, check-in émotionnel en cas de chute, cœur/satellite, qualité des sources d'idées, décisions à l'aveugle à deux, paris non pris, fiscalité détaillée, backtests, dashboard web, parcours d'apprentissage.

---

## 7. Critères de succès (à 1 mois)

- Le brief arrive tous les matins, sans erreur de chiffres.
- La radiographie donne la même performance qu'un calcul manuel vérifié.
- Chacun connaît sa performance réelle face au MSCI World et ses frais annuels.
- Aucune décision hors plan prise sans passer par `/decision`.
- Les deux utilisateurs disent consulter les marchés moins souvent, et stresser moins.

## 8. Ce qu'on ne veut pas

Trop de notifications, du jargon sans explication, des conseils péremptoires, des chiffres inventés, des "opportunités" à la mode.

---

## 9. Reste à fournir

1. Le lien de ton Google Sheet (ou on part du modèle ci-dessus).
2. Le profil de l'associé : expérience, actifs, enveloppes.
3. Ton allocation cible souhaitée (sinon proposition par défaut : 70 % ETF monde, 20 % ETF émergents ou Europe, 10 % crypto maximum).
