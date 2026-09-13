# 📝 DEVOIR ÉVALUATIF - U31 RÉSEAUX - SEMAINE 6

## 🎯 ROUTAGE STATIQUE ET TABLE DE ROUTAGE

---

## 📋 INFORMATIONS GÉNÉRALES

| **Élément** | **Détail** |
|-------------|------------|
| **Bloc** | U31 - Mise en œuvre de réseaux informatiques |
| **Semaine** | S6 / Année 1 - Découverte |
| **Thématique** | Routage statique, Table de routage, Passerelle par défaut |
| **Durée** | 40 minutes |
| **Modalité** | Travail individuel |
| **Barème** | 20 points |
| **Support** | Ordinateur avec accès terminal |

---

## 🎓 COMPÉTENCES RNCP ÉVALUÉES

| **Code** | **Compétence** | **Niveau évalué** |
|----------|----------------|------------------|
| **C2.1** | Installer et configurer un service réseau | Initiation |
| **C2.2** | Installer et configurer les éléments d'interconnexion réseau | Découverte |
| **C2.3** | Diagnostiquer un dysfonctionnement d'un réseau | Découverte |

---

## 📌 CONSIGNES GÉNÉRALES

✅ **Travail strictement individuel**  
✅ **Durée : 40 minutes** (respecter le temps imparti)  
✅ **Supports autorisés :** Fiche de cours élève  
✅ **Outils nécessaires :** Terminal (cmd, PowerShell ou Terminal Linux)  
✅ **Rendu :** Compléter ce document et l'enregistrer au format **PDF** dans votre portfolio  
✅ **Nom du fichier :** `NOM_Prenom_U31_S6_Routage_Devoir.pdf`

---

## 🚀 MISE EN SITUATION PROFESSIONNELLE

**Contexte :**

Vous êtes technicien réseau junior dans l'entreprise **NetConnect Solutions**. Un utilisateur signale qu'il ne parvient plus à accéder à Internet depuis son poste, mais qu'il peut toujours accéder aux ressources du réseau local (imprimante, serveur interne).

**Votre mission :**

1. Analyser la configuration réseau du poste utilisateur
2. Identifier le problème de routage
3. Proposer une solution
4. Documenter votre intervention pour le portfolio technique

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

## 🖥️ PARTIE 2 : AFFICHER SA PROPRE TABLE DE ROUTAGE (5 points)

### Exercice 2.1 : Exécuter la commande adaptée (2 points)

**Consigne :** Ouvrez un terminal et exécutez la commande pour afficher votre table de routage.

**Sous Windows :**
```bash
route print
```
**ou**
```bash
netstat -r
```

**Sous Linux :**
```bash
ip route
```
**ou**
```bash
route -n
```

**Questions :**

1. **Quelle commande avez-vous utilisée ?**  
   ___________________________________________________________________

2. **Quel système d'exploitation utilisez-vous ?**  
   ☐ Windows  
   ☐ Linux

---

### Exercice 2.2 : Identifier les informations clés (3 points)

**Consigne :** En analysant votre table de routage, répondez aux questions suivantes :

1. **Quelle est l'adresse IP de votre ordinateur ?**  
   Adresse IP : ______________________________

2. **Quelle est votre passerelle par défaut ?**  
   Passerelle : ______________________________

3. **Quelle est l'adresse de votre réseau local ?**  
   Réseau : ______________________________

**💡 Aide :** 
- La passerelle par défaut se trouve sur la ligne avec la destination 0.0.0.0 (Windows) ou "default" (Linux)
- Votre réseau local est souvent 192.168.x.0 ou 10.x.x.0

---

## 📊 PARTIE 3 : ANALYSER UNE TABLE DE ROUTAGE (6 points)

### Exercice 3.1 : Lecture de table de routage Windows (3 points)

**Contexte :** Voici la table de routage d'un ordinateur Windows :

```
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface  Métrique
          0.0.0.0          0.0.0.0   192.168.10.1    192.168.10.50       25
     192.168.10.0    255.255.255.0       On-link      192.168.10.50      281
       10.50.0.0      255.255.0.0   192.168.10.200   192.168.10.50       35
        127.0.0.0        255.0.0.0       On-link         127.0.0.1      331
```

**Questions :**

1. **Quelle est l'adresse IP de cet ordinateur ?**  
   ___________________________________________________________________

2. **Quelle est sa passerelle par défaut ?**  
   ___________________________________________________________________

3. **Combien de réseaux cet ordinateur peut-il atteindre ?** (ne comptez pas la boucle locale 127.0.0.0)  
   ___________________________________________________________________

---

### Exercice 3.2 : Lecture de table de routage Linux (3 points)

**Contexte :** Voici la table de routage d'un ordinateur Linux :

```
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.254   0.0.0.0         UG    100    0        0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eth0
172.16.0.0      192.168.1.200   255.255.0.0     UG    200    0        0 eth0
```

**Questions :**

1. **Quelle est la passerelle par défaut ?**  
   ___________________________________________________________________

2. **Quelle interface réseau est utilisée pour la route par défaut ?**  
   ___________________________________________________________________

3. **Pour atteindre le réseau 172.16.0.0, quel routeur l'ordinateur va-t-il contacter ?**  
   ___________________________________________________________________

---

## 🗺️ PARTIE 4 : COMPLÉTER UN SCHÉMA DE ROUTAGE (5 points)

### Exercice 4.1 : Tracer le chemin d'un paquet

**Contexte :** Voici un réseau composé de 3 réseaux interconnectés :

```
    RÉSEAU A               RÉSEAU B               RÉSEAU C
  (10.0.1.0/24)         (10.0.2.0/24)         (10.0.3.0/24)
        │                     │                     │
        │                     │                     │
  ┌──────────┐          ┌──────────┐          ┌──────────┐
  │ PC-A     │          │ ROUTEUR2 │          │ PC-C     │
  │10.0.1.10 │──────────│.1.254  .2.254────────│10.0.3.10 │
  └──────────┘          └──────────┘          └──────────┘
        │                     │
        │                     │
  ┌──────────┐                │
  │ ROUTEUR1 │────────────────┘
  │.1.1  .2.1│
  └──────────┘
```

**Configuration des machines :**

| **Machine** | **IP** | **Masque** | **Passerelle** |
|------------|--------|-----------|---------------|
| PC-A | 10.0.1.10 | 255.255.255.0 | 10.0.1.1 |
| PC-C | 10.0.3.10 | 255.255.255.0 | 10.0.3.254 |
| Routeur1 | 10.0.1.1 (eth0) et 10.0.2.1 (eth1) | - | 10.0.2.254 (vers Internet) |
| Routeur2 | 10.0.2.254 (eth0) et 10.0.3.254 (eth1) | - | - |

**Question :**

**PC-A envoie un paquet vers PC-C (10.0.3.10). Tracez le chemin emprunté par le paquet en complétant les étapes ci-dessous :**

```
Étape 1 : PC-A (10.0.1.10) consulte sa table de routage.
         → La destination 10.0.3.10 est-elle dans son réseau local ?
         ☐ Oui  ☐ Non

Étape 2 : PC-A envoie le paquet à :
         ___________________________________________________________________

Étape 3 : Ce routeur reçoit le paquet. Quel routeur est-ce ?
         ☐ ROUTEUR1  ☐ ROUTEUR2

Étape 4 : Ce routeur consulte sa table de routage et transmet le paquet à :
         ___________________________________________________________________

Étape 5 : Ce deuxième routeur livre le paquet à :
         ___________________________________________________________________
```

**Résumé du chemin :**

Complétez ce schéma avec les adresses IP des étapes :

```
PC-A (______) → ROUTEUR___ (______) → ROUTEUR___ (______) → PC-C (______)
```

---

## 🔧 PARTIE 5 : DIAGNOSTIC DE PANNE (3 points)

### Exercice 5.1 : Identifier le problème

**Contexte :** Un utilisateur appelle le support technique :

> *"Bonjour, je ne peux plus accéder à Internet depuis mon ordinateur. Par contre, je peux toujours imprimer sur l'imprimante réseau et accéder au serveur de fichiers de l'entreprise."*

**Configuration de son poste :**

| **Paramètre** | **Valeur actuelle** |
|--------------|-------------------|
| Adresse IP | 192.168.50.25 |
| Masque | 255.255.255.0 |
| Passerelle par défaut | **Non configurée** |
| Serveur DNS | 8.8.8.8 |

**Réseau de l'entreprise :**
- Réseau local : 192.168.50.0/24
- Routeur (box Internet) : 192.168.50.254

**Questions :**

1. **Quel est le problème qui empêche l'utilisateur d'accéder à Internet ?**  
   ___________________________________________________________________  
   ___________________________________________________________________

2. **Pourquoi l'utilisateur peut-il toujours accéder à l'imprimante et au serveur local ?**  
   ___________________________________________________________________  
   ___________________________________________________________________

3. **Quelle est la solution pour résoudre ce problème ?**  
   ___________________________________________________________________  
   ___________________________________________________________________

---

## ✅ CRITÈRES D'ÉVALUATION

### Barème détaillé

| **Partie** | **Exercice** | **Points** | **Critères** |
|------------|-------------|-----------|--------------|
| **Partie 1** | Identification | 1 pt | Toutes les informations renseignées |
| **Partie 2** | Afficher sa table de routage | 5 pts | |
| | 2.1 Commande exécutée | 2 pts | Commande correcte selon l'OS |
| | 2.2 Identification des infos | 3 pts | IP + passerelle + réseau corrects |
| **Partie 3** | Analyser une table de routage | 6 pts | |
| | 3.1 Table Windows | 3 pts | 3 réponses correctes |
| | 3.2 Table Linux | 3 pts | 3 réponses correctes |
| **Partie 4** | Schéma de routage | 5 pts | Chemin complet et correct |
| **Partie 5** | Diagnostic de panne | 3 pts | Problème identifié + solution |
| **TOTAL** | | **20 pts** | |

---

## 🎯 GRILLE D'AUTO-ÉVALUATION

**Avant de rendre votre devoir, vérifiez :**

- [ ] J'ai rempli mes informations d'identification
- [ ] J'ai exécuté la commande pour afficher ma table de routage
- [ ] J'ai identifié ma passerelle par défaut
- [ ] J'ai analysé les deux tables de routage (Windows et Linux)
- [ ] J'ai tracé le chemin complet du paquet dans le schéma
- [ ] J'ai diagnostiqué le problème de panne et proposé une solution
- [ ] J'ai vérifié l'orthographe de mes réponses techniques
- [ ] J'ai enregistré mon fichier au bon format (PDF)

---

## 📁 INTÉGRATION PORTFOLIO

**Ce livrable servira de preuve pour :**

✅ **Épreuve E4** : Étude et réalisation de systèmes  
✅ **Compétence C2.2** : Installer et configurer les éléments d'interconnexion réseau  
✅ **Compétence C2.3** : Diagnostiquer un dysfonctionnement d'un réseau  

**Conseils pour le portfolio :**
- Ajouter une capture d'écran de votre table de routage
- Annoter le schéma de routage pour montrer votre compréhension
- Rédiger 2-3 phrases sur ce que vous avez appris

---

## 💡 CONSEILS DE RÉUSSITE

✅ **Prenez votre temps** pour lire attentivement chaque question  
✅ **Exécutez vraiment les commandes** sur votre ordinateur  
✅ **Utilisez la fiche de cours** en cas de doute  
✅ **Vérifiez vos réponses** avant de passer à la partie suivante  
✅ **Soyez précis** dans vos réponses (adresses IP complètes)  

---

## ⚠️ POINTS DE VIGILANCE

**Erreurs fréquentes à éviter :**

❌ Confondre l'IP de sa machine avec sa passerelle par défaut  
❌ Oublier de noter l'unité (ex : 192.168.1.0/24 et non juste 192.168.1.0)  
❌ Inverser les étapes dans le schéma de routage  
❌ Proposer une solution technique sans expliquer le problème  
❌ Ne pas rendre les captures d'écran lisibles  

---

## 🔧 EN CAS DE PROBLÈME TECHNIQUE

**Problème : Ma table de routage est très longue**  
→ C'est normal ! Concentrez-vous sur la ligne avec 0.0.0.0 (passerelle par défaut) et votre réseau local

**Problème : Je n'arrive pas à identifier ma passerelle**  
→ Cherchez la ligne avec "0.0.0.0" (Windows) ou "default" (Linux)

**Problème : Ma commande ne fonctionne pas sous Linux**  
→ Essayez avec `sudo` devant : `sudo ip route` ou `sudo route -n`

---

## 📅 MODALITÉS DE RENDU

| **Élément** | **Détail** |
|-------------|------------|
| **Date limite** | Fin de la séance (12h40) |
| **Format** | PDF uniquement |
| **Nom fichier** | `NOM_Prenom_U31_S6_Routage_Devoir.pdf` |
| **Dépôt** | Plateforme LMS du CFA ou remise au formateur |
| **Retard** | -2 points par tranche de 24h |

---

## 🎓 APRÈS LE DEVOIR

**La correction sera :**
- Distribuée la semaine prochaine (S7)
- Expliquée collectivement en début de séance
- Annotée individuellement sur vos copies

**Vous recevrez :**
- Votre note sur 20
- Un feedback personnalisé sur vos points forts et axes d'amélioration
- Des conseils pour progresser

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

**🎓 BON COURAGE ! Le routage est la base du réseau, montrez que vous avez bien compris ! 💪**
