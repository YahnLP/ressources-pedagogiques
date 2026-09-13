# 📝 DEVOIR ÉVALUATIF - U31 RÉSEAUX - SEMAINE 8

## 🎯 DNS : RÉSOLUTION ET DIAGNOSTIC

---

## 📋 INFORMATIONS GÉNÉRALES

| **Élément** | **Détail** |
|-------------|------------|
| **Bloc** | U31 - Mise en œuvre de réseaux informatiques |
| **Semaine** | S8 / Année 1 - Découverte |
| **Thématique** | DNS : Résolution, Nslookup, dig, Hiérarchie DNS |
| **Durée** | 45 minutes |
| **Modalité** | Travail individuel |
| **Barème** | 20 points |
| **Support** | Ordinateur avec accès terminal + connexion Internet |

---

## 🎓 COMPÉTENCES RNCP ÉVALUÉES

| **Code** | **Compétence** | **Niveau évalué** |
|----------|----------------|------------------|
| **C2.1** | Installer et configurer un service réseau | Initiation |
| **C2.3** | Diagnostiquer un dysfonctionnement d'un réseau | Découverte |
| **C3.2** | Exploiter des outils de surveillance et de diagnostic | Découverte |

---

## 📌 CONSIGNES GÉNÉRALES

✅ **Travail strictement individuel**  
✅ **Durée : 45 minutes** (gestion du temps importante)  
✅ **Supports autorisés :** Fiche de cours élève  
✅ **Outils nécessaires :** Terminal (cmd ou PowerShell sous Windows, Terminal sous Linux)  
✅ **Rendu :** Compléter ce document et l'enregistrer au format **PDF** dans votre portfolio  
✅ **Nom du fichier :** `NOM_Prenom_U31_S8_DNS_Devoir.pdf`

---

## 🚀 MISE EN SITUATION PROFESSIONNELLE

**Contexte :**

Vous êtes technicien réseau junior dans l'entreprise **TechConnect SARL**. Votre responsable vous confie une mission de diagnostic DNS suite à des plaintes d'utilisateurs qui ne parviennent pas à accéder à certains sites web.

**Votre mission :**

1. Effectuer des requêtes DNS pour diagnostiquer le problème
2. Analyser les résultats obtenus
3. Rédiger un compte-rendu technique pour votre responsable

**Ce livrable sera intégré à votre portfolio pour l'épreuve E4.**

---

## 📋 PARTIE 1 : IDENTIFICATION (1 point)

**Remplissez vos informations personnelles :**

| **Champ** | **Réponse** |
|-----------|-------------|
| **Nom** | |
| **Prénom** | |
| **Promotion** | |
| **Date** | |
| **CFA** | |

---

## 🔍 PARTIE 2 : REQUÊTES DNS AVEC `nslookup` (8 points)

### Exercice 2.1 : Résolution simple (2 points)

**Consigne :** Ouvrez un terminal et effectuez la requête suivante :

```bash
nslookup www.education.gouv.fr
```

**Questions :**

1. **Quel serveur DNS a répondu à votre requête ?**  
   Nom : ______________________________  
   Adresse IP : ______________________________

2. **Quelle est l'adresse IPv4 de `www.education.gouv.fr` ?**  
   Adresse IPv4 : ______________________________

---

### Exercice 2.2 : Recherche d'enregistrements MX (3 points)

**Consigne :** Effectuez la requête suivante pour trouver les serveurs de messagerie de Gmail :

```bash
nslookup -type=MX gmail.com
```

**Questions :**

1. **Listez les 3 premiers serveurs mail (MX) de gmail.com avec leur priorité :**

| **Priorité** | **Serveur mail** |
|--------------|------------------|
| | |
| | |
| | |

2. **Quel serveur mail sera contacté en premier ? Pourquoi ?**  
   ___________________________________________________________________  
   ___________________________________________________________________

---

### Exercice 2.3 : Recherche d'enregistrements NS (3 points)

**Consigne :** Effectuez la requête suivante pour trouver les serveurs DNS autoritaires de Google :

```bash
nslookup -type=NS google.com
```

**Questions :**

1. **Listez 3 serveurs DNS autoritaires (NS) de google.com :**

   - ______________________________
   - ______________________________
   - ______________________________

2. **Pourquoi y a-t-il plusieurs serveurs NS pour un même domaine ?**  
   ___________________________________________________________________  
   ___________________________________________________________________

---

## 🛠️ PARTIE 3 : REQUÊTES DNS AVEC `dig` (6 points)

### Exercice 3.1 : Analyse détaillée avec `dig` (3 points)

**Consigne :** Effectuez la requête suivante :

```bash
dig www.lemonde.fr
```

**Questions :**

1. **Dans quelle section du résultat se trouve la réponse ?**  
   ☐ QUESTION SECTION  
   ☐ ANSWER SECTION  
   ☐ AUTHORITY SECTION  
   ☐ ADDITIONAL SECTION

2. **Quelle est l'adresse IPv4 de `www.lemonde.fr` ?**  
   Adresse IPv4 : ______________________________

3. **Quel est le temps de réponse de la requête (Query time) ?**  
   Temps : ______________ msec

---

### Exercice 3.2 : Utilisation du mode court (1 point)

**Consigne :** Effectuez la requête suivante :

```bash
dig +short www.wikipedia.org
```

**Question :**

1. **Quelle(s) adresse(s) IP obtenez-vous ?**  
   ___________________________________________________________________

---

### Exercice 3.3 : Interroger un DNS spécifique (2 points)

**Consigne :** Effectuez la requête suivante en utilisant le DNS de Cloudflare :

```bash
dig @1.1.1.1 www.amazon.fr
```

**Questions :**

1. **Quel serveur DNS a répondu (ligne SERVER) ?**  
   ___________________________________________________________________

2. **Comparez le temps de réponse avec l'exercice 3.1. Lequel est le plus rapide ?**  
   ☐ Exercice 3.1 (DNS par défaut)  
   ☐ Exercice 3.3 (Cloudflare 1.1.1.1)

---

## 🌳 PARTIE 4 : HIÉRARCHIE DNS (4 points)

### Exercice 4.1 : Décomposition d'un nom de domaine (2 points)

**Consigne :** Décomposez le nom de domaine suivant : **mail.support.microsoft.com**

| **Composant** | **Partie du nom** | **Rôle** |
|---------------|------------------|----------|
| **Racine** | | |
| **TLD** | | |
| **Domaine** | | |
| **Sous-domaine(s)** | | |

---

### Exercice 4.2 : Schéma de résolution DNS (2 points)

**Consigne :** Complétez le schéma ci-dessous en numérotant les étapes de 1 à 6.

```
[ ] NAVIGATEUR ────────────────► [ ] DNS LOCAL (Résolveur)
                "Je veux accéder à www.amazon.fr"

[ ] DNS LOCAL ─────────────────► [ ] DNS RACINE
                "Qui gère les .fr ?"

[ ] DNS RACINE ────────────────► [ ] DNS LOCAL
                "C'est le DNS TLD .fr"

[ ] DNS LOCAL ─────────────────► [ ] DNS TLD (.fr)
                "IP de www.amazon.fr ?"

[ ] DNS TLD (.fr) ─────────────► [ ] DNS LOCAL
                "C'est 52.95.220.10"

[ ] DNS LOCAL ─────────────────► [ ] NAVIGATEUR
                "Voici l'IP : 52.95.220.10"
```

**Numérotez chaque étape dans les cases [ ] de 1 à 6.**

---

## 📊 PARTIE 5 : SYNTHÈSE PROFESSIONNELLE (1 point)

### Exercice 5.1 : Compte-rendu technique

**Consigne :** Rédigez un court compte-rendu (3-5 lignes) pour votre responsable résumant :
- Les outils utilisés
- Les résultats obtenus
- Votre conclusion sur l'état du DNS

**Compte-rendu :**

___________________________________________________________________  
___________________________________________________________________  
___________________________________________________________________  
___________________________________________________________________  
___________________________________________________________________  

---

## ✅ CRITÈRES D'ÉVALUATION

### Barème détaillé

| **Partie** | **Exercice** | **Points** | **Critères** |
|------------|-------------|-----------|--------------|
| **Partie 1** | Identification | 1 pt | Toutes les informations renseignées |
| **Partie 2** | Requêtes nslookup | 8 pts | |
| | 2.1 Résolution simple | 2 pts | Réponses exactes (serveur DNS + IP) |
| | 2.2 Enregistrements MX | 3 pts | Liste complète + justification priorité |
| | 2.3 Enregistrements NS | 3 pts | Liste complète + explication redondance |
| **Partie 3** | Requêtes dig | 6 pts | |
| | 3.1 Analyse détaillée | 3 pts | Section correcte + IP + temps |
| | 3.2 Mode court | 1 pt | Adresse(s) IP correcte(s) |
| | 3.3 DNS spécifique | 2 pts | Serveur identifié + comparaison |
| **Partie 4** | Hiérarchie DNS | 4 pts | |
| | 4.1 Décomposition | 2 pts | Tous les composants identifiés |
| | 4.2 Schéma résolution | 2 pts | Numérotation correcte (ordre logique) |
| **Partie 5** | Synthèse pro | 1 pt | Compte-rendu clair et structuré |
| **TOTAL** | | **20 pts** | |

---

## 🎯 GRILLE D'AUTO-ÉVALUATION

**Avant de rendre votre devoir, vérifiez :**

- [ ] J'ai rempli mes informations d'identification
- [ ] J'ai effectué toutes les requêtes demandées
- [ ] J'ai répondu à toutes les questions
- [ ] J'ai vérifié l'orthographe de mes réponses techniques
- [ ] Mon compte-rendu est professionnel et clair
- [ ] J'ai enregistré mon fichier au bon format (PDF)
- [ ] Le nom de fichier respecte la nomenclature demandée

---

## 📁 INTÉGRATION PORTFOLIO

**Ce livrable servira de preuve pour :**

✅ **Épreuve E4** : Étude et réalisation de systèmes  
✅ **Compétence C2.3** : Diagnostiquer un dysfonctionnement d'un réseau  
✅ **Compétence C3.2** : Exploiter des outils de surveillance et de diagnostic  

**Conseils pour le portfolio :**
- Ajouter une capture d'écran de vos requêtes dans le terminal
- Annoter les résultats importants
- Rédiger 2-3 phrases sur ce que vous avez appris

---

## 💡 CONSEILS DE RÉUSSITE

✅ **Prenez votre temps** pour lire chaque consigne  
✅ **Testez vos commandes** avant de noter les résultats  
✅ **Utilisez la fiche de cours** en cas de doute  
✅ **Vérifiez vos réponses** avant de passer à l'exercice suivant  
✅ **Soignez la présentation** de votre compte-rendu  

---

## ⚠️ POINTS DE VIGILANCE

**Erreurs fréquentes à éviter :**

❌ Confondre le serveur DNS qui répond (ligne "Serveur:") avec l'IP du site recherché  
❌ Oublier d'indiquer l'unité (msec pour les temps, priorité pour les MX)  
❌ Noter des résultats sans les avoir vérifiés dans le terminal  
❌ Mal numéroter les étapes du schéma de résolution DNS  

---

## 🔧 EN CAS DE PROBLÈME TECHNIQUE

**Problème : `dig` n'est pas reconnu sous Windows**  
→ Utilisez uniquement `nslookup` pour la Partie 3 et adaptez les commandes

**Problème : Pas de connexion Internet**  
→ Signalez-le immédiatement au formateur

**Problème : Résultats différents des autres apprenants**  
→ C'est normal ! Le cache DNS peut donner des résultats légèrement différents

---

## 📅 MODALITÉS DE RENDU

| **Élément** | **Détail** |
|-------------|------------|
| **Date limite** | Fin de la séance (12h30) |
| **Format** | PDF uniquement |
| **Nom fichier** | `NOM_Prenom_U31_S8_DNS_Devoir.pdf` |
| **Dépôt** | Plateforme LMS du CFA ou remise au formateur |
| **Retard** | -2 points par tranche de 24h |

---

## 🎓 APRÈS LE DEVOIR

**La correction sera :**
- Distribuée la semaine prochaine (S9)
- Expliquée collectivement en début de séance
- Annotée individuellement sur vos copies

**Vous recevrez :**
- Votre note sur 20
- Un feedback personnalisé
- Des pistes d'amélioration

**N'oubliez pas :**
- D'intégrer ce livrable à votre portfolio
- De conserver une copie pour révision future
- De poser vos questions lors de la correction

---

**📅 Devoir conçu le :** 25/02/2026  
**✍️ Auteur :** Yahn LE PRETTRE  
**🎯 Conformité :** Qualiopi + Référentiel RNCP BAC PRO CIEL  
**📧 Questions :** yahn.leprettre@mfr.asso.fr

---

**🎓 BON COURAGE ! Appliquez ce que vous avez appris et montrez vos compétences ! 💪**
