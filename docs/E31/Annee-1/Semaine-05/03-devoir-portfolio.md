# DEVOIR PORTFOLIO - U31 Réseaux Informatiques
## Semaine 5 - Configuration Switch : Table MAC et VLANs

---

**Nom :** _________________________ **Prénom :** _________________________

**Classe :** Bac Pro CIEL - Année 1 **Date :** ___/___/______

**Binôme :** _________________________

---

## 🎯 OBJECTIF DU DEVOIR

Ce devoir constitue une **preuve de compétence** pour votre **portfolio professionnel** (Épreuve E4).

**Vous devez :**
1. Configurer un switch Cisco (création VLANs, ports access)
2. Analyser la table MAC du switch
3. Tester la segmentation VLAN (connectivité intra/inter-VLAN)
4. Diagnostiquer des problèmes de configuration
5. Documenter votre travail (captures CLI, schémas)

**Compétences évaluées :**
- C3.1 : Installer et configurer un réseau informatique local
- C3.3 : Exploiter un réseau informatique
- C1.3 : Respecter les normes, réglementations et standards

---

## 📋 CONSIGNES GÉNÉRALES

### Durée
- **1h45 de pratique** (TP guidé + TP avancé + Scénarios)

### Travail
- **Binôme** (1 switch pour 2 apprentis)

### Livrables à rendre
1. **Fiche TP complétée** (ce document)
2. **3 captures CLI** (copier-coller du terminal) :
   - Capture 1 : `show vlan brief` (après création des VLANs)
   - Capture 2 : `show mac address-table` (après tests)
   - Capture 3 : `show running-config` (configuration complète)
3. **Schéma réseau** (dessiné à la main ou sur PC)

### Critères de réussite
- ✅ 3 VLANs créés correctement
- ✅ Tous les ports configurés en mode access
- ✅ Tests de connectivité réussis (intra-VLAN OK, inter-VLAN KO)
- ✅ Configuration sauvegardée

---

## 🔧 EXERCICE 1 : CRÉATION DES VLANs (20 points)

### Cahier des charges

**Contexte :**

Vous êtes technicien réseau dans un lycée. On vous demande de segmenter le réseau en 3 VLANs :

| **VLAN ID** | **Nom** | **Usage** | **Ports** |
|------------|---------|-----------|-----------|
| 10 | ADMINISTRATION | Direction, secrétariat | Fa0/1 - Fa0/5 |
| 20 | ENSEIGNANTS | Salle des profs, CDI | Fa0/6 - Fa0/15 |
| 30 | ELEVES | Salles informatiques | Fa0/16 - Fa0/24 |

---

### Étape 1 : Connexion au switch (5 points)

**Manipulations :**

1. Brancher le câble console entre le PC et le switch
2. Ouvrir PuTTY (ou terminal) :
   - Port : COM__ (à identifier)
   - Vitesse : 9600 bauds
3. Se connecter et passer en mode privilégié :

```
Switch> enable
Switch#
```

**Questions :**

1. **Quel est le nom actuel du switch ?**
   - Nom : _______________________

2. **Afficher la version d'IOS :**
   ```
   Switch# show version
   ```
   - Version IOS : _______________________
   - Modèle du switch : _______________________

**☐ Étape 1 validée** (signature formateur : _______________)

---

### Étape 2 : Création des 3 VLANs (10 points)

**Commandes à exécuter :**

```
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name ADMINISTRATION
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name ENSEIGNANTS
Switch(config-vlan)# exit

Switch(config)# vlan 30
Switch(config-vlan)# name ELEVES
Switch(config-vlan)# exit
```

**Vérification :**

```
Switch(config)# exit
Switch# show vlan brief
```

**Copier-coller le résultat de `show vlan brief` ci-dessous :**

```
[CAPTURE 1 À COLLER ICI]







```

**Questions :**

1. **Combien de VLANs sont affichés au total ?** ___________

2. **Le VLAN 1 peut-il être supprimé ?**
   - ☐ Oui ☐ Non
   - Pourquoi ? ___________________________________________________

3. **Quels ports sont actuellement dans le VLAN 10 ?**
   - Réponse : _____________________________________________________

**☐ Étape 2 validée** (signature formateur : _______________)

---

### Étape 3 : Configuration des ports en mode access (5 points)

**Commandes à exécuter :**

**Ports 1-5 (VLAN 10 - ADMINISTRATION) :**

```
Switch# configure terminal
Switch(config)# interface range fastethernet 0/1 - 5
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
Switch(config-if-range)# description Postes_Administration
Switch(config-if-range)# exit
```

**Ports 6-15 (VLAN 20 - ENSEIGNANTS) :**

```
Switch(config)# interface range fastethernet 0/6 - 15
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 20
Switch(config-if-range)# description Postes_Enseignants
Switch(config-if-range)# exit
```

**Ports 16-24 (VLAN 30 - ELEVES) :**

```
Switch(config)# interface range fastethernet 0/16 - 24
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 30
Switch(config-if-range)# description Postes_Eleves
Switch(config-if-range)# exit
```

**Vérification finale :**

```
Switch(config)# exit
Switch# show vlan brief
```

**Questions :**

1. **Le VLAN 10 contient maintenant quels ports ?**
   - Réponse : _____________________________________________________

2. **Combien de ports sont dans le VLAN 20 ?** ___________

3. **Y a-t-il encore des ports dans le VLAN 1 ?**
   - ☐ Oui, lesquels : ____________________________________________
   - ☐ Non, tous les ports sont affectés

**☐ Étape 3 validée** (signature formateur : _______________)

---

## 📊 EXERCICE 2 : ANALYSE DE LA TABLE MAC (25 points)

### Étape 1 : Observation initiale de la table MAC (10 points)

**Commande :**

```
Switch# show mac address-table
```

**Questions :**

1. **Combien d'entrées MAC y a-t-il dans la table ?** ___________

2. **Quels sont les types d'entrées ?** (cocher)
   - ☐ DYNAMIC (apprises automatiquement)
   - ☐ STATIC (configurées manuellement)

3. **Afficher uniquement les entrées du VLAN 10 :**
   ```
   Switch# show mac address-table vlan 10
   ```
   - Nombre d'entrées : ___________

---

### Étape 2 : Vider la table MAC (5 points)

**Commande :**

```
Switch# clear mac address-table dynamic
```

**Vérification :**

```
Switch# show mac address-table
```

**Questions :**

1. **Que s'est-il passé ?**
   - ☐ La table est vide (aucune entrée DYNAMIC)
   - ☐ Il reste des entrées (lesquelles ?) _________________________

2. **Pourquoi vider la table MAC peut être utile ?**
   _________________________________________________________________
   _________________________________________________________________

---

### Étape 3 : Tests de connectivité et remplissage de la table (10 points)

**Manipulations :**

1. Connecter **2 PC** sur le **VLAN 10** (ports Fa0/1 et Fa0/2)
2. Configurer les PC :
   - PC1 : 192.168.10.10 / 255.255.255.0
   - PC2 : 192.168.10.20 / 255.255.255.0
3. Faire un **ping** de PC1 vers PC2 :
   ```cmd
   C:\> ping 192.168.10.20
   ```

**Résultat du ping :**
- ☐ Réussi (4 réponses reçues)
- ☐ Échec (Délai d'attente dépassé)

4. Sur le switch, afficher la table MAC :
   ```
   Switch# show mac address-table
   ```

**Copier-coller le résultat ci-dessous :**

```
[CAPTURE 2 À COLLER ICI]







```

**Questions :**

1. **Combien d'entrées MAC apparaissent maintenant ?** ___________

2. **Compléter le tableau :**

| **Adresse MAC** | **Port** | **VLAN** | **Type** |
|----------------|----------|----------|----------|
| | | | |
| | | | |

3. **Ces entrées MAC correspondent à quels équipements ?**
   - 1ère MAC : ______________________________________________________
   - 2ème MAC : ______________________________________________________

4. **Au bout de combien de temps ces entrées vont-elles disparaître ?**
   - Réponse : __________ minutes (= __________ secondes)

---

## 🧪 EXERCICE 3 : TESTS DE SEGMENTATION VLAN (30 points)

### Test 1 : Connectivité intra-VLAN (10 points)

**Objectif :** Vérifier que 2 PC dans le **même VLAN** peuvent communiquer.

**Configuration :**

| **Équipement** | **Port** | **VLAN** | **Adresse IP** |
|---------------|----------|----------|----------------|
| PC1 | Fa0/1 | 10 | 192.168.10.10 / 24 |
| PC2 | Fa0/2 | 10 | 192.168.10.20 / 24 |

**Test :**

```cmd
C:\> ping 192.168.10.20
```

**Résultat :**
- ☐ ✅ Ping réussi (4 réponses)
- ☐ ❌ Ping échoué

**Analyse :**

Expliquer pourquoi le ping fonctionne (ou pas) :
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**☐ Test 1 validé** (signature formateur : _______________)

---

### Test 2 : Isolation inter-VLAN (15 points)

**Objectif :** Vérifier que 2 PC dans des **VLANs différents** NE peuvent PAS communiquer.

**Configuration :**

| **Équipement** | **Port** | **VLAN** | **Adresse IP** |
|---------------|----------|----------|----------------|
| PC1 | Fa0/1 | 10 | 192.168.10.10 / 24 |
| PC3 | Fa0/6 | 20 | 192.168.20.10 / 24 |

**Test :**

```cmd
C:\> ping 192.168.20.10
```

**Résultat :**
- ☐ ✅ Ping réussi
- ☐ ❌ Ping échoué

**Analyse :**

1. **Pourquoi le ping échoue-t-il ?**
   _________________________________________________________________
   _________________________________________________________________

2. **Le switch a-t-il reçu la trame de PC1 ?**
   - ☐ Oui ☐ Non

3. **Le switch a-t-il transféré la trame vers PC3 ?**
   - ☐ Oui ☐ Non
   - Pourquoi ? ____________________________________________________

4. **Comment faire pour que PC1 et PC3 puissent communiquer ?**
   _________________________________________________________________
   _________________________________________________________________

**☐ Test 2 validé** (signature formateur : _______________)

---

### Test 3 : Broadcast et domaine de broadcast (5 points)

**Objectif :** Observer la propagation d'un broadcast dans un VLAN.

**Configuration :**

| **Équipement** | **Port** | **VLAN** |
|---------------|----------|----------|
| PC1 | Fa0/1 | 10 |
| PC2 | Fa0/2 | 10 |
| PC3 | Fa0/3 | 10 |
| PC4 | Fa0/6 | 20 |

**Test :** PC1 envoie un broadcast ARP (découverte d'adresse).

```cmd
C:\> arp -d
C:\> ping 192.168.10.20
```

**Questions :**

1. **Quels PC reçoivent le broadcast ARP de PC1 ?** (cocher)
   - ☐ PC2 (VLAN 10)
   - ☐ PC3 (VLAN 10)
   - ☐ PC4 (VLAN 20)

2. **Pourquoi PC4 ne reçoit-il pas le broadcast ?**
   _________________________________________________________________

3. **Combien de domaines de broadcast y a-t-il dans ce réseau ?**
   - Réponse : ___________
   - Justification : _________________________________________________

---

## 🛠️ EXERCICE 4 : DIAGNOSTIC DE PANNES (25 points)

### Scénario 1 : Port dans le mauvais VLAN (10 points)

**Contexte :**

Un enseignant (normalement VLAN 20) se plaint de ne plus pouvoir accéder au serveur pédagogique (VLAN 20). Après vérification, son PC est branché sur le port Fa0/10.

**Mission :**

1. **Vérifier dans quel VLAN est le port Fa0/10 :**
   ```
   Switch# show vlan brief
   ```
   - VLAN actuel du port Fa0/10 : ___________

2. **Hypothèse sur le problème :**
   _________________________________________________________________

3. **Corriger la configuration :**
   ```
   Switch# configure terminal
   Switch(config)# interface fastethernet 0/10
   Switch(config-if)# switchport access vlan 20
   Switch(config-if)# exit
   ```

4. **Vérifier la correction :**
   ```
   Switch# show vlan brief
   ```
   - Le port Fa0/10 est maintenant dans VLAN : ___________

5. **Tester la connectivité :** L'enseignant peut-il accéder au serveur ?
   - ☐ Oui ☐ Non

---

### Scénario 2 : VLAN non créé (8 points)

**Contexte :**

Vous essayez de configurer le port Fa0/12 dans le VLAN 40, mais la commande échoue.

```
Switch(config)# interface fastethernet 0/12
Switch(config-if)# switchport access vlan 40
% Access VLAN does not exist. Creating vlan 40
```

**Questions :**

1. **Que signifie ce message ?**
   _________________________________________________________________

2. **Le VLAN 40 a-t-il été créé automatiquement ?**
   - ☐ Oui ☐ Non

3. **Vérifier avec :**
   ```
   Switch# show vlan brief
   ```
   - VLAN 40 présent : ☐ Oui ☐ Non
   - Nom du VLAN 40 : _______________________

4. **Bonne pratique :** Faut-il créer le VLAN avant ou après d'affecter des ports ?
   - ☐ Avant (recommandé)
   - ☐ Après (automatique mais pas propre)

---

### Scénario 3 : Configuration non sauvegardée (7 points)

**Contexte :**

Vous avez passé 1 heure à configurer le switch. Le switch redémarre (coupure électrique). À la reconnexion, **toute la configuration a disparu !**

**Questions :**

1. **Quelle erreur avez-vous commise ?**
   _________________________________________________________________

2. **Quelle commande auriez-vous dû exécuter pour sauvegarder ?**
   ```
   Switch# _______________________________________
   ```

3. **Où est stockée la configuration courante (non sauvegardée) ?**
   - ☐ RAM (volatile)
   - ☐ NVRAM (non-volatile)
   - ☐ Flash

4. **Où est stockée la configuration sauvegardée ?**
   - ☐ RAM
   - ☐ NVRAM (non-volatile)
   - ☐ Flash

5. **Sauvegarder maintenant votre configuration :**
   ```
   Switch# write memory
   ```
   - Résultat : ☐ [OK] ☐ Erreur

---

## 📐 EXERCICE 5 : SCHÉMA RÉSEAU (10 points)

**Consignes :**

Dessiner le schéma du réseau configuré :
- 1 switch (avec nom et modèle)
- 3 VLANs (10, 20, 30) avec leurs noms
- Au moins 2 PC par VLAN avec adresses IP
- Indiquer les numéros de ports

**Espace pour le schéma :**

```
[DESSINER LE SCHÉMA ICI OU COLLER UNE IMPRESSION]
















```

**Éléments à faire apparaître :** (cocher)
- ☐ Nom du switch
- ☐ 3 VLANs colorés ou délimités
- ☐ Numéros de ports
- ☐ Adresses IP des PC
- ☐ Légende claire

---

## 📊 BARÈME D'ÉVALUATION (Compatible Qualiopi)

### Partie A : Compétences techniques (60 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Connexion au switch** | Connexion réussie, modes CLI maîtrisés | 5 pts | ___/5 |
| **Création VLANs** | 3 VLANs créés avec noms corrects | 10 pts | ___/10 |
| **Configuration ports access** | Tous les ports configurés dans bons VLANs | 5 pts | ___/5 |
| **Analyse table MAC** | Table MAC analysée, entrées identifiées | 10 pts | ___/10 |
| **Test connectivité intra-VLAN** | Ping réussi, explication correcte | 10 pts | ___/10 |
| **Test isolation inter-VLAN** | Ping échoué (normal), explication correcte | 15 pts | ___/15 |
| **Diagnostic pannes** | 3 scénarios résolus correctement | 15 pts | ___/15 |
| **Configuration sauvegardée** | `write memory` exécuté | 5 pts | ___/5 |

**Sous-total Partie A : ___/75 points** (converti sur 60)

---

### Partie B : Documentation et traçabilité (20 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Captures CLI** | 3 captures complètes et exploitables | 8 pts | ___/8 |
| **Schéma réseau** | Schéma clair avec tous les éléments | 6 pts | ___/6 |
| **Qualité des explications** | Réponses claires et argumentées | 4 pts | ___/4 |
| **Présentation** | Document soigné, lisible | 2 pts | ___/2 |

**Sous-total Partie B : ___/20 points**

---

### Partie C : Compétences transversales (20 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Travail en binôme** | Collaboration efficace, répartition des tâches | 6 pts | ___/6 |
| **Autonomie** | Réalise les manipulations avec peu d'aide | 6 pts | ___/6 |
| **Rigueur** | Vérifie la configuration avant de valider | 4 pts | ___/4 |
| **Gestion du temps** | Termine dans le temps imparti (1h45) | 4 pts | ___/4 |

**Sous-total Partie C : ___/20 points**

---

### Note finale

| **Partie** | **Points obtenus** | **Coefficient** | **Note sur 20** |
|------------|--------------------|-----------------|-----------------|
| Partie A - Compétences techniques | ___/75 | ×0,16 | ___/12 |
| Partie B - Documentation | ___/20 | ×1 | ___/4 |
| Partie C - Compétences transversales | ___/20 | ×1 | ___/4 |
| **TOTAL** | | | **___/20** |

**Appréciation formateur :**
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**Signature formateur :** ___________________ **Date :** ___/___/______

---

## 🎯 GRILLE D'ANALYSE DE COMPÉTENCES (Portfolio)

**Cette section est à remplir par l'apprenti pour alimenter son portfolio professionnel.**

### Compétence C3.1 : Installer et configurer un réseau informatique local

**Situation professionnelle vécue :**

*"J'ai configuré un switch Cisco en créant 3 VLANs (Administration, Enseignants, Élèves) et en affectant les ports en mode access. J'ai utilisé la ligne de commande (CLI) pour exécuter les commandes IOS et j'ai sauvegardé la configuration."*

**Ce que j'ai su faire :**
- ☐ Me connecter à un switch en console (PuTTY, 9600 bauds)
- ☐ Créer des VLANs avec noms descriptifs
- ☐ Configurer des ports en mode access
- ☐ Utiliser `interface range` pour configurer plusieurs ports
- ☐ Sauvegarder la configuration (`write memory`)

**Preuves :**
- ☐ Captures CLI (`show vlan brief`, `show running-config`)
- ☐ Fiche TP complétée
- ☐ Validation du formateur

---

### Compétence C3.3 : Exploiter un réseau informatique

**Situation professionnelle vécue :**

*"J'ai analysé la table MAC d'un switch pour identifier les équipements connectés. J'ai compris les processus de learning, forwarding et flooding. J'ai testé la segmentation VLAN en vérifiant que les domaines de broadcast étaient bien isolés."*

**Ce que j'ai su faire :**
- ☐ Afficher et interpréter la table MAC (`show mac address-table`)
- ☐ Vider la table MAC pour forcer un réapprentissage
- ☐ Identifier les adresses MAC, ports et VLANs
- ☐ Comprendre le principe de domaine de broadcast par VLAN

**Preuves :**
- ☐ Capture table MAC analysée
- ☐ Tests de connectivité documentés
- ☐ Explications des résultats

---

### Compétence C1.3 : Respecter les normes, réglementations et standards

**Situation professionnelle vécue :**

*"J'ai appliqué la norme IEEE 802.1Q pour créer des VLANs. J'ai respecté les bonnes pratiques : ne pas utiliser VLAN 1 pour les utilisateurs, créer les VLANs avant d'affecter les ports, sauvegarder systématiquement la configuration."*

**Ce que j'ai su faire :**
- ☐ Identifier la norme IEEE 802.1Q (VLANs)
- ☐ Respecter les bonnes pratiques de nommage (noms descriptifs)
- ☐ Documenter la configuration (schéma, captures)

**Preuves :**
- ☐ Schéma réseau avec conventions
- ☐ Configuration conforme aux standards
- ☐ Documentation technique

---

## ✍️ AUTO-ÉVALUATION

**Réponds honnêtement à ces questions pour progresser :**

1. **As-tu réussi à créer les VLANs du premier coup ?**
   - ☐ Oui ☐ Non
   - Si non, quelle difficulté ? _______________________________________

2. **Quelle commande as-tu trouvée la plus difficile ?**
   - ☐ `vlan 10`
   - ☐ `switchport mode access`
   - ☐ `interface range`
   - ☐ `show mac address-table`
   - ☐ Autre : _____________________________________________________

3. **Te sens-tu capable de configurer un switch seul en entreprise ?**
   - ☐ Oui, sans aide
   - ☐ Oui, avec un peu d'aide
   - ☐ Non, j'ai besoin de plus d'entraînement

4. **Qu'est-ce que tu as appris de nouveau aujourd'hui ?**
_________________________________________________________________________
_________________________________________________________________________

5. **Quel conseil donnerais-tu à un camarade pour réussir ce TP ?**
_________________________________________________________________________
_________________________________________________________________________

---

## 📝 COMMENTAIRES ET CONSEILS DU FORMATEUR

**Points forts :**
_________________________________________________________________________
_________________________________________________________________________

**Axes d'amélioration :**
_________________________________________________________________________
_________________________________________________________________________

**Conseils pour S6 (Routage statique) :**
_________________________________________________________________________
_________________________________________________________________________

---

## ✅ VALIDATION POUR LE PORTFOLIO

☐ **Ce devoir constitue une preuve acceptable pour le portfolio professionnel**

**Niveau de maîtrise atteint :**
- ☐ **Fragile** : L'apprenti a besoin d'un accompagnement renforcé
- ☐ **En cours d'acquisition** : L'apprenti progresse, continuer à pratiquer
- ☐ **Acquis** : L'apprenti maîtrise la compétence
- ☐ **Expert** : L'apprenti peut former d'autres personnes

**Signature formateur :** ___________________ **Date :** ___/___/______

---

**Document à conserver dans le portfolio pour les épreuves E4, E5 et E6**

**Date de création :** 24/02/2026  
**Version :** 1.0  
**Auteur :** Yahn LE PRETTRE
