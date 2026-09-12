# DEVOIR PORTFOLIO - U31 Réseaux Informatiques
## Semaine 7 - Configuration Client DHCP et Analyse de Trafic

---

**Nom :** _________________________ **Prénom :** _________________________

**Classe :** Bac Pro CIEL - Année 1 **Date :** ___/___/______

---

## 🎯 OBJECTIF DU DEVOIR

Ce devoir constitue une **preuve de compétence** pour votre **portfolio professionnel** (Épreuve E4 - Situations professionnelles).

**Vous devez :**
1. Configurer et tester un client DHCP sur votre poste
2. Capturer et analyser une transaction DHCP avec Wireshark
3. Diagnostiquer des scénarios de pannes DHCP
4. Documenter votre travail (captures d'écran, rapports d'analyse)

**Compétences évaluées :**
- C3.1 : Installer et configurer un réseau informatique local
- C3.2 : Assurer la maintenance d'un réseau informatique  
- C3.3 : Exploiter un réseau informatique
- C2.2 : Communiquer et documenter

---

## 📋 CONSIGNES GÉNÉRALES

### Durée
- **1h45 de pratique** (TP guidé + TP avancé + Dépannage)

### Travail
- **Individuel** pour les manipulations
- **Binôme** pour l'analyse Wireshark

### Livrables à rendre
1. **Fiche TP complétée** (ce document)
2. **3 captures d'écran** :
   - Capture 1 : Résultat de `ipconfig /all` montrant DHCP activé
   - Capture 2 : Capture Wireshark des 4 messages DORA
   - Capture 3 : Résultat de `ipconfig` après un release (adresse APIPA)
3. **Rapport d'analyse Wireshark** (tableau à remplir page 6)

### Critères de réussite
- ✅ Le client DHCP fonctionne correctement (obtient une IP valide)
- ✅ La capture Wireshark montre les 4 messages DORA
- ✅ Les scénarios de panne sont correctement diagnostiqués

---

## 🔧 EXERCICE 1 : CONFIGURATION CLIENT DHCP (30 points)

### Partie A : Vérification de la configuration initiale (10 points)

#### Manipulation 1 : Afficher la configuration réseau

**Commande à exécuter :**

```cmd
C:\> ipconfig /all
```

**Copier les informations suivantes :**

| **Information** | **Valeur relevée** |
|----------------|-------------------|
| Nom de la carte réseau | __________________________ |
| Adresse physique (MAC) | __________________________ |
| DHCP activé | ☐ Oui ☐ Non |
| Adresse IPv4 | __________________________ |
| Masque de sous-réseau | __________________________ |
| Passerelle par défaut | __________________________ |
| Serveur DHCP | __________________________ |
| Serveurs DNS | __________________________ |
| Bail obtenu le | ___/___/____ à __:__ |
| Bail expirant le | ___/___/____ à __:__ |

**Calculs à effectuer :**

1. **Durée du bail :**
   - Différence entre "Bail expirant" et "Bail obtenu" : __________ heures

2. **Moment du renouvellement T1 (50%) :**
   - Bail obtenu + (Durée × 50%) : ___/___/____ à __:__

3. **Moment du renouvellement T2 (87,5%) :**
   - Bail obtenu + (Durée × 87,5%) : ___/___/____ à __:__

**☐ Manipulation 1 validée** (signature formateur : _______________)

---

### Partie B : Tests de libération et renouvellement (10 points)

#### Manipulation 2 : Libérer l'adresse IP (Release)

**Commande à exécuter :**

```cmd
C:\> ipconfig /release
```

**Observer le résultat :**

| **Information** | **Valeur après release** |
|----------------|--------------------------|
| Adresse IPv4 | __________________________ |
| Masque de sous-réseau | __________________________ |
| Passerelle par défaut | __________________________ |

**Test de connectivité :**

Exécuter : `ping 8.8.8.8`

**Résultat :**
- ☐ Succès (paquets reçus)
- ☐ Échec (Délai d'attente dépassé ou "Destination inaccessible")

**Explication du résultat :**
_________________________________________________________________________
_________________________________________________________________________

---

#### Manipulation 3 : Renouveler l'adresse IP (Renew)

**Commande à exécuter :**

```cmd
C:\> ipconfig /renew
```

**Observer le résultat :**

| **Information** | **Valeur après renew** | **Identique à avant release ?** |
|----------------|------------------------|---------------------------------|
| Adresse IPv4 | __________________________ | ☐ Oui ☐ Non |
| Masque de sous-réseau | __________________________ | ☐ Oui ☐ Non |
| Passerelle par défaut | __________________________ | ☐ Oui ☐ Non |

**Test de connectivité :**

Exécuter : `ping 8.8.8.8`

**Résultat :**
- ☐ Succès (paquets reçus)
- ☐ Échec

**Analyse :**

1. **Avez-vous récupéré la même adresse IP qu'avant le release ?**
   - ☐ Oui, pourquoi ? ___________________________________________________
   - ☐ Non, pourquoi ? ___________________________________________________

2. **Combien de temps a pris le processus de renouvellement ?**
   - __________ secondes (estimer)

**☐ Manipulation 2 et 3 validées** (signature formateur : _______________)

---

### Partie C : Test de durée de bail (10 points)

#### Manipulation 4 : Observer le comportement du bail

**Scénario :**

Votre formateur a configuré le serveur DHCP avec un **bail de 5 minutes** pour ce TP.

**Objectif :** Observer ce qui se passe à l'expiration du bail.

**Procédure :**

1. Noter l'heure actuelle : __:__
2. Noter l'heure d'expiration du bail : __:__
3. **Attendre 5 minutes** (en silence, sans toucher au PC)
4. Après 5 minutes, exécuter : `ipconfig /all`

**Résultat après expiration :**

| **Information** | **Valeur après expiration** |
|----------------|----------------------------|
| Adresse IPv4 | __________________________ |
| Serveur DHCP | __________________________ |

**Question :**

> "Avez-vous perdu votre adresse IP après 5 minutes ?"

- ☐ Non, j'ai toujours une IP valide → **Normal**, le renouvellement automatique (T1) a fonctionné à 50% du bail (2,5 min)
- ☐ Oui, j'ai une adresse APIPA (169.254.x.x) → **Problème**, le serveur DHCP n'a pas répondu

**Analyse :**

Expliquez pourquoi le renouvellement automatique évite que vous perdiez votre connexion :
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**☐ Manipulation 4 validée** (signature formateur : _______________)

---

## 🔍 EXERCICE 2 : ANALYSE WIRESHARK (40 points)

### Partie A : Capture d'une transaction DHCP (15 points)

#### Manipulation 5 : Capturer les messages DORA

**Procédure :**

1. **Ouvrir Wireshark**
   - Sélectionner l'interface réseau active (Ethernet ou Wi-Fi)
   - Cliquer sur "Start capturing" (aileron de requin bleu)

2. **Provoquer une transaction DHCP**
   - Dans l'invite de commandes :
     ```cmd
     ipconfig /release
     ipconfig /renew
     ```

3. **Arrêter la capture**
   - Cliquer sur le carré rouge dans Wireshark

4. **Filtrer les paquets DHCP**
   - Dans la barre de filtre, taper : `dhcp`
   - Appuyer sur Entrée

**Résultat attendu :**

Vous devez voir **4 paquets** correspondant aux 4 messages DORA :
1. DHCP Discover
2. DHCP Offer
3. DHCP Request
4. DHCP ACK

**Nombre de paquets DHCP capturés :** __________

**☐ Capture réussie** (4 paquets DHCP visibles)

**☐ Manipulation 5 validée** (signature formateur : _______________)

---

### Partie B : Analyse détaillée des messages DHCP (25 points)

#### Tableau d'analyse à compléter

**Instructions :**

Pour chaque message DHCP capturé, cliquer dessus dans Wireshark et compléter le tableau ci-dessous en observant les détails dans le panneau du bas.

---

**MESSAGE 1 : DHCP DISCOVER**

| **Champ** | **Valeur observée dans Wireshark** |
|-----------|-----------------------------------|
| **Adresse IP source** | __________________________ |
| **Adresse IP destination** | __________________________ |
| **Port UDP source** | __________________________ |
| **Port UDP destination** | __________________________ |
| **Type de message** (Broadcast/Unicast) | ☐ Broadcast ☐ Unicast |
| **Adresse MAC du client** | __________________________ |

**Analyse :**

1. **Pourquoi l'adresse IP source est-elle 0.0.0.0 ?**
   _________________________________________________________________________

2. **Pourquoi l'adresse IP destination est-elle 255.255.255.255 ?**
   _________________________________________________________________________

---

**MESSAGE 2 : DHCP OFFER**

| **Champ** | **Valeur observée dans Wireshark** |
|-----------|-----------------------------------|
| **Adresse IP source** | __________________________ |
| **Adresse IP destination** | __________________________ |
| **Port UDP source** | __________________________ |
| **Port UDP destination** | __________________________ |
| **Adresse IP proposée** ("Your IP Address") | __________________________ |
| **Option 1 - Masque de sous-réseau** | __________________________ |
| **Option 3 - Passerelle** | __________________________ |
| **Option 6 - Serveur DNS** | __________________________ |
| **Option 51 - Durée de bail** | __________ secondes |

**Analyse :**

1. **Quelle IP le serveur propose-t-il au client ?**
   _________________________________________________________________________

2. **Convertir la durée du bail en heures :**
   - __________ secondes ÷ 3600 = __________ heures

---

**MESSAGE 3 : DHCP REQUEST**

| **Champ** | **Valeur observée dans Wireshark** |
|-----------|-----------------------------------|
| **Adresse IP source** | __________________________ |
| **Adresse IP destination** | __________________________ |
| **Port UDP source** | __________________________ |
| **Port UDP destination** | __________________________ |
| **Type de message** (Broadcast/Unicast) | ☐ Broadcast ☐ Unicast |
| **Option 50 - IP demandée** ("Requested IP Address") | __________________________ |
| **Option 54 - Serveur DHCP choisi** | __________________________ |

**Analyse :**

1. **Pourquoi le client envoie-t-il encore en broadcast alors qu'il connaît l'IP du serveur ?**
   _________________________________________________________________________
   _________________________________________________________________________

---

**MESSAGE 4 : DHCP ACKNOWLEDGE**

| **Champ** | **Valeur observée dans Wireshark** |
|-----------|-----------------------------------|
| **Adresse IP source** | __________________________ |
| **Adresse IP destination** | __________________________ |
| **Port UDP source** | __________________________ |
| **Port UDP destination** | __________________________ |
| **Type de message** (Broadcast/Unicast) | ☐ Broadcast ☐ Unicast |
| **Adresse IP confirmée** ("Your IP Address") | __________________________ |

**Analyse :**

1. **Comparer l'IP confirmée dans l'ACK avec l'IP proposée dans l'OFFER. Sont-elles identiques ?**
   - ☐ Oui ☐ Non

2. **Le client peut-il maintenant utiliser cette adresse IP ?**
   - ☐ Oui ☐ Non

---

### Tableau récapitulatif des 4 messages

| **Message** | **IP Source** | **IP Dest** | **Port Src** | **Port Dest** | **Broadcast/Unicast** |
|-------------|---------------|-------------|--------------|---------------|-----------------------|
| DISCOVER | | | | | |
| OFFER | | | | | |
| REQUEST | | | | | |
| ACK | | | | | |

**☐ Analyse Wireshark complète** (signature formateur : _______________)

---

## 🛠️ EXERCICE 3 : DIAGNOSTIC DE PANNES (30 points)

### Scénario 1 : Adresse APIPA détectée (10 points)

**Contexte :**

Un utilisateur vous appelle au support informatique :

> "Bonjour, mon ordinateur ne se connecte plus à Internet. J'ai fait ipconfig et mon adresse IP est 169.254.27.193. Est-ce normal ?"

**Questions :**

1. **Quel est le problème identifié ?**
   - ☐ Adresse IP valide, pas de problème
   - ☐ Adresse APIPA, le client n'a pas trouvé le serveur DHCP
   - ☐ Adresse IP en conflit

2. **Quelle est la plage d'adresses APIPA ?**
   - Plage : _____________________ à _____________________

3. **Quelles sont les 3 causes possibles ?**
   1. _________________________________________________________________
   2. _________________________________________________________________
   3. _________________________________________________________________

4. **Quelles vérifications allez-vous faire en premier ?** (Numéroter par ordre de priorité)

   - ☐ Vérifier que le câble réseau est bien branché
   - ☐ Vérifier que le switch est allumé
   - ☐ Exécuter `ipconfig /renew` pour forcer une nouvelle demande
   - ☐ Redémarrer l'ordinateur
   - ☐ Contacter l'administrateur pour vérifier l'état du serveur DHCP

**Ordre de priorité :**

1. ____________________________________________________________________
2. ____________________________________________________________________
3. ____________________________________________________________________
4. ____________________________________________________________________
5. ____________________________________________________________________

---

### Scénario 2 : Bail expiré (10 points)

**Contexte :**

Un ordinateur portable a été éteint pendant **3 semaines** (vacances d'été). Son bail DHCP était de **7 jours**. L'utilisateur rallume son PC aujourd'hui.

**Questions :**

1. **Que s'est-il passé pendant les 3 semaines ?**
   _________________________________________________________________
   _________________________________________________________________

2. **Que va faire le client au démarrage du PC ?**
   - ☐ Garder l'ancienne adresse IP
   - ☐ Afficher une adresse APIPA (169.254.x.x)
   - ☐ Relancer automatiquement un processus DORA

3. **Le client peut-il récupérer la même IP qu'il y a 3 semaines ?**
   - ☐ Oui, certainement
   - ☐ Peut-être, si elle est encore disponible
   - ☐ Non, impossible

4. **L'utilisateur doit-il faire une manipulation manuelle ?**
   - ☐ Oui : ____________________________________________________________
   - ☐ Non, c'est automatique

---

### Scénario 3 : Pool DHCP saturé (10 points)

**Contexte :**

Une entreprise a **300 postes de travail**. Le serveur DHCP a une étendue de **250 adresses** (192.168.1.50 à 192.168.1.299). Un nouvel employé arrive avec son PC portable.

**Questions :**

1. **Quel problème va-t-il rencontrer ?**
   _________________________________________________________________
   _________________________________________________________________

2. **Quelle adresse IP son PC va-t-il obtenir ?**
   - ☐ Une adresse normale (192.168.1.x)
   - ☐ Une adresse APIPA (169.254.x.x)
   - ☐ Aucune adresse (0.0.0.0)

3. **Comment vérifier sur le serveur DHCP que le pool est saturé ?**
   _________________________________________________________________
   _________________________________________________________________

4. **Quelles sont les 3 solutions possibles pour l'administrateur ?**
   1. _________________________________________________________________
   2. _________________________________________________________________
   3. _________________________________________________________________

5. **Solution immédiate pour dépanner le nouvel employé (en attendant que l'admin agisse) :**
   _________________________________________________________________
   _________________________________________________________________

---

## 📊 BARÈME D'ÉVALUATION (Compatible Qualiopi)

### Partie A : Compétences techniques (60 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Configuration initiale relevée** | Toutes les informations ipconfig collectées correctement | 10 pts | ___/10 |
| **Tests Release/Renew** | Commandes exécutées, résultats observés et expliqués | 10 pts | ___/10 |
| **Observation du bail** | Calcul T1/T2 correct, compréhension du renouvellement | 10 pts | ___/10 |
| **Capture Wireshark** | 4 messages DORA capturés et filtrés | 15 pts | ___/15 |
| **Analyse messages DHCP** | Tableau d'analyse complet et pertinent | 25 pts | ___/25 |
| **Diagnostic pannes** | 3 scénarios analysés correctement | 30 pts | ___/30 |

**Sous-total Partie A : ___/100 points**

**Note sur 12 (partie technique) : ___/12**

---

### Partie B : Documentation et traçabilité (20 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Captures d'écran** | 3 captures nettes et exploitables | 6 pts | ___/6 |
| **Qualité des explications** | Réponses claires et argumentées | 8 pts | ___/8 |
| **Rigueur** | Tableaux remplis complètement, pas d'oubli | 4 pts | ___/4 |
| **Présentation** | Document soigné, lisible | 2 pts | ___/2 |

**Sous-total Partie B : ___/20 points**

---

### Partie C : Compétences transversales (20 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Autonomie** | Réalise les manipulations sans aide constante | 6 pts | ___/6 |
| **Rigueur** | Vérifie ses résultats, ne saute pas d'étapes | 6 pts | ___/6 |
| **Analyse** | Fait le lien entre théorie et pratique | 4 pts | ___/4 |
| **Gestion du temps** | Termine dans le temps imparti (1h45) | 4 pts | ___/4 |

**Sous-total Partie C : ___/20 points**

---

### Note finale

| **Partie** | **Points obtenus** | **Coefficient** | **Note sur 20** |
|------------|--------------------|-----------------|-----------------|
| Partie A - Compétences techniques | ___/100 | ×0,12 | ___/12 |
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

*"J'ai configuré et testé un client DHCP sur un poste Windows. J'ai utilisé les commandes ipconfig pour libérer et renouveler une adresse IP. J'ai observé le processus d'obtention automatique d'adresse IP et calculé les moments de renouvellement (T1/T2) en fonction de la durée du bail."*

**Ce que j'ai su faire :**
- ☐ Vérifier la configuration DHCP d'un poste (ipconfig /all)
- ☐ Libérer et renouveler une adresse IP (release/renew)
- ☐ Calculer les timers de renouvellement (T1 et T2)
- ☐ Interpréter les informations fournies par le serveur DHCP

**Preuves :**
- ☐ Captures d'écran ipconfig
- ☐ Fiche TP complétée
- ☐ Validation du formateur

---

### Compétence C3.2 : Assurer la maintenance d'un réseau informatique

**Situation professionnelle vécue :**

*"J'ai diagnostiqué plusieurs scénarios de pannes DHCP : adresse APIPA (169.254.x.x), bail expiré, pool DHCP saturé. J'ai proposé des solutions adaptées à chaque situation et expliqué les vérifications à effectuer dans un ordre logique."*

**Ce que j'ai su faire :**
- ☐ Identifier une adresse APIPA et comprendre sa signification
- ☐ Diagnostiquer un problème de connectivité réseau
- ☐ Proposer des solutions de dépannage adaptées
- ☐ Prioriser les vérifications (méthode de diagnostic)

**Preuves :**
- ☐ Scénarios de pannes résolus
- ☐ Capture d'écran d'une adresse APIPA
- ☐ Explications des solutions proposées

---

### Compétence C2.2 : Communiquer et documenter

**Situation professionnelle vécue :**

*"J'ai capturé et analysé une transaction DHCP complète avec Wireshark. J'ai identifié les 4 messages du processus DORA (Discover, Offer, Request, Acknowledge) et documenté les caractéristiques de chaque message (adresses IP source/destination, ports UDP, type broadcast/unicast)."*

**Ce que j'ai su faire :**
- ☐ Utiliser Wireshark pour capturer du trafic réseau
- ☐ Filtrer les paquets DHCP
- ☐ Analyser les champs d'un paquet DHCP
- ☐ Documenter une analyse réseau de manière structurée

**Preuves :**
- ☐ Capture Wireshark avec filtres DHCP
- ☐ Tableau d'analyse rempli
- ☐ Explications des observations

---

## ✍️ AUTO-ÉVALUATION

**Réponds honnêtement à ces questions pour progresser :**

1. **As-tu réussi à capturer les 4 messages DORA du premier coup ?**
   - ☐ Oui ☐ Non
   - Si non, quelle difficulté as-tu rencontrée ? _______________________________

2. **Quelle manipulation as-tu trouvée la plus difficile ?**
   - ☐ Commandes ipconfig
   - ☐ Capture Wireshark
   - ☐ Analyse des messages DHCP
   - ☐ Diagnostic des pannes
   - ☐ Autre : _______________________________________________________

3. **Te sens-tu capable de diagnostiquer une panne DHCP en situation réelle (en entreprise) ?**
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

**Conseils pour la prochaine séance (S8 - DNS) :**
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
**Auteur :** Équipe pédagogique CFA
