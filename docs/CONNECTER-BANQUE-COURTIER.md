# Relier ta banque et ton courtier à l'assistant

_Mis à jour le 31/10/2026._

L'objectif : que l'assistant connaisse tes vraies opérations, sans que tu aies à tout ressaisir, et **sans jamais lui confier un identifiant bancaire**.

## La règle d'or

**Tu ne donnes jamais ton identifiant, ton mot de passe ou un code reçu par SMS à l'assistant**, ni à un outil qui te le demanderait en son nom. L'assistant travaille uniquement à partir de **fichiers que tu exportes toi-même** depuis ton espace client.

## La voie recommandée : l'export mensuel du relevé

Une fois par mois, à la fin du mois :

1. **Dans l'espace client de ton courtier** (application ou site), cherche une rubrique du type « Historique des opérations », « Relevés », « Mouvements », « Exporter » ou « Transaction export ».
2. **Exporte au format CSV** (ou Excel), sur la période depuis le dernier export. Exemple : Trade Republic propose, depuis avril 2026, un export CSV des transactions (Profil, puis Relevés, puis Export des transactions).
3. **Dépose le fichier** dans ton dossier privé `prive/<ton prénom>/`, ou joins-le dans la conversation.
4. **Dis à l'assistant** : « importe mon relevé ». Il lance `scripts/importer_releve.py`, qui :
   - reconnaît tout seul les colonnes (date, type d'opération, ISIN, quantité, cours, montant, frais), en français, anglais ou allemand ;
   - écarte les opérations déjà importées ;
   - prépare un fichier `import-<date>.xlsx` à coller dans la feuille Transactions de ton Google Sheet ;
   - te liste les nouveaux actifs à ajouter dans la feuille Actifs.
5. **Colle les lignes** dans ton Sheet, puis dis « synchronise mon Sheet ».

Si ton courtier ne propose qu'un **relevé PDF**, ou si tu n'as qu'une **capture d'écran**, joins-la : l'Analyste la lit et te prépare les mêmes lignes.

Si les colonnes de ton courtier ne sont pas reconnues, le script te dit lesquelles manquent. On ajoute alors leur nom dans `templates/courtiers.csv`, une fois pour toutes.

## Les autres voies, et pourquoi on ne les prend pas pour l'instant

| Voie | Ce que c'est | Pourquoi pas maintenant |
|---|---|---|
| **Applications d'agrégation** grand public | Des applications qui affichent tous tes comptes au même endroit | Pratiques pour une vue d'ensemble, mais l'assistant ne peut pas s'y brancher. Si l'une propose un export CSV, il peut servir de relevé |
| **API d'open banking (DSP2)** | Accès officiel aux comptes par des prestataires agréés | Réservé à des comptes développeur, souvent payants, avec une procédure de validation. À étudier si l'assistant est un jour proposé à d'autres personnes |
| **Outils non officiels** qui se connectent avec ton code | Scripts ou extensions qui imitent l'application du courtier | **Jamais** : ils demandent tes identifiants, peuvent enfreindre les conditions de ton courtier et exposer ton compte |

## Ta banque (budget)

Même logique pour le budget : exporte le relevé de ton compte courant en CSV une fois par mois, et dis « fais mon point budget avec ce relevé ». Le Conseiller budget classe les dépenses (besoins, envies, épargne) et met à jour la feuille Budget. Aucune connexion directe à ta banque n'est nécessaire.

## Données personnelles

Tes relevés restent dans `prive/`, qui n'est jamais envoyé sur GitHub. Tu restes responsable de tes données, et de celles de toute autre personne qui utiliserait l'assistant (RGPD).
