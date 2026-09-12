# 📘 FICHE DE COURS ÉLÈVE - U31 RÉSEAUX - SEMAINE 6

## 🛣️ LE ROUTAGE IP ET LA TABLE DE ROUTAGE

---

## 📋 INFORMATIONS

| **Élément** | **Détail** |
|-------------|------------|
| **Bloc** | U31 - Mise en œuvre de réseaux informatiques |
| **Semaine** | S6 / Année 1 |
| **Thématique** | Routage statique, Table de routage, Passerelle par défaut |
| **Durée cours** | 50 minutes |

---

## 🎯 OBJECTIFS D'APPRENTISSAGE

À la fin de ce cours, je serai capable de :

✅ Expliquer ce qu'est le routage IP  
✅ Identifier le rôle d'un routeur  
✅ Lire et interpréter une table de routage  
✅ Différencier passerelle par défaut et routes spécifiques  
✅ Afficher la table de routage de mon ordinateur  
✅ Diagnostiquer un problème de routage simple  

---

## 1️⃣ QU'EST-CE QUE LE ROUTAGE ?

### 📖 Définition

Le **routage** est le processus par lequel un paquet IP trouve son chemin d'un réseau à un autre réseau sur Internet.

**Analogie :** Le routage fonctionne comme le **GPS de votre voiture** qui calcule le meilleur itinéraire pour aller d'un point A à un point B.

| **Concept réseau** | **Analogie GPS** |
|-------------------|------------------|
| **Paquet IP** | Voiture en déplacement |
| **Routeur** | Carrefour / Échangeur autoroutier |
| **Table de routage** | Carte routière / GPS |
| **Passerelle par défaut** | "Sortie de ville" par défaut |

### 🤔 Pourquoi le routage est-il nécessaire ?

**Problème :** Internet est composé de **millions de réseaux** interconnectés. Un paquet doit traverser plusieurs réseaux pour arriver à destination.

**Solution :** Les **routeurs** se transmettent les paquets de proche en proche (hop by hop) jusqu'à la destination finale.

**Exemple concret :**

Vous êtes à Paris et vous voulez envoyer un email à quelqu'un à Tokyo.

1. Votre ordinateur envoie le paquet à votre **box Internet** (routeur domestique)
2. La box l'envoie au **routeur de votre FAI** (Orange, Free, SFR...)
3. Ce routeur l'envoie à un **routeur international**
4. Le paquet traverse plusieurs routeurs en Europe, puis en Asie
5. Il arrive finalement au **routeur japonais** puis au destinataire

**⏱️ Temps total :** Environ 150-300 millisecondes pour traverser le monde !

![Illustration : Schéma montrant un ordinateur à Paris envoyant un paquet email vers Tokyo. Le paquet traverse 4-5 routeurs représentés par des carrés bleus interconnectés. Chaque routeur est étiqueté (Box Internet, FAI, International, Asie, Tokyo). Des flèches indiquent le chemin du paquet. Style : diagramme pédagogique, couleurs vives sur fond blanc.]

> 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 2️⃣ QU'EST-CE QU'UN ROUTEUR ?

### 📖 Définition

Un **routeur** est un équipement réseau qui **interconnecte plusieurs réseaux** et qui **décide du chemin** que doit emprunter un paquet pour atteindre sa destination.

### 🔍 Caractéristiques d'un routeur

| **Caractéristique** | **Explication** |
|--------------------|-----------------|
| **Plusieurs interfaces réseau** | Un routeur possède au minimum 2 interfaces (connexions) pour relier 2 réseaux |
| **Possède une table de routage** | Une sorte de "carte routière" qui lui dit où envoyer chaque paquet |
| **Travaille au niveau 3 (IP)** | Il lit l'adresse IP de destination dans chaque paquet |
| **Prend des décisions** | Il choisit la meilleure route selon sa table de routage |

### 📊 Exemples de routeurs

| **Type** | **Exemple** | **Usage** |
|----------|------------|----------|
| **Routeur domestique** | Box Internet (Livebox, Freebox...) | Connecte votre maison à Internet |
| **Routeur d'entreprise** | Cisco, HP, Ubiquiti | Connecte les différents services de l'entreprise |
| **Routeur de cœur de réseau** | Juniper, Cisco ASR | Utilisé par les opérateurs télécom |

### 🆚 Routeur vs Switch

| **Critère** | **Routeur** | **Switch** |
|-------------|------------|-----------|
| **Fonction** | Interconnecte des réseaux **différents** | Interconnecte des machines dans le **même** réseau |
| **Niveau OSI** | Couche 3 (Réseau / IP) | Couche 2 (Liaison / Ethernet) |
| **Adressage** | Utilise les adresses **IP** | Utilise les adresses **MAC** |
| **Exemple** | Box Internet | Switch de bureau 8 ports |

![Illustration : Deux schémas côte à côte. À gauche : un switch (boîte verte) connectant 4 ordinateurs dans le même nuage "Réseau 192.168.1.0". À droite : un routeur (boîte bleue) avec deux côtés, chaque côté connecté à un nuage différent "Réseau A 192.168.1.0" et "Réseau B 192.168.2.0". Style : schéma réseau simple et clair.]

> 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 3️⃣ LA TABLE DE ROUTAGE

### 📖 Définition

La **table de routage** est une base de données stockée dans un routeur (ou un ordinateur) qui contient la **liste des réseaux accessibles** et le **chemin à emprunter** pour les atteindre.

**Analogie :** La table de routage, c'est comme le GPS de votre voiture qui contient toutes les routes possibles.

### 📊 Structure d'une table de routage

Une table de routage contient plusieurs colonnes :

| **Colonne** | **Signification** | **Exemple** |
|------------|------------------|-------------|
| **Destination** | Réseau de destination | 192.168.1.0/24 |
| **Masque** | Masque de sous-réseau | 255.255.255.0 |
| **Passerelle (Gateway)** | Routeur suivant à contacter | 192.168.0.254 |
| **Interface** | Carte réseau à utiliser | eth0, Wi-Fi |
| **Métrique** | Coût de la route (optionnel) | 10 |

### 🔎 Exemple de table de routage simple

Voici à quoi ressemble une table de routage d'un ordinateur :

| **Destination** | **Masque** | **Passerelle** | **Interface** |
|----------------|-----------|---------------|--------------|
| **0.0.0.0** | 0.0.0.0 | 192.168.1.254 | Wi-Fi |
| **192.168.1.0** | 255.255.255.0 | Direct | Wi-Fi |
| **127.0.0.0** | 255.0.0.0 | 127.0.0.1 | Loopback |

**Lecture de cette table :**

1. **Ligne 1** : Pour toutes les destinations non spécifiées (0.0.0.0 = Internet), envoyer vers **192.168.1.254** (la box Internet)
2. **Ligne 2** : Pour le réseau local 192.168.1.0, envoyer **directement** (pas besoin de routeur)
3. **Ligne 3** : Pour l'adresse de bouclage 127.0.0.1 (localhost), envoyer vers soi-même

---

## 4️⃣ LA PASSERELLE PAR DÉFAUT (DEFAULT GATEWAY)

### 📖 Définition

La **passerelle par défaut** (ou **default gateway**) est le routeur vers lequel un ordinateur envoie tous les paquets dont la destination n'est **pas dans le réseau local**.

**Analogie :** La passerelle par défaut, c'est comme la **sortie d'autoroute par défaut** sur un panneau routier : "Si vous ne savez pas où aller, prenez cette sortie".

### 🔍 Identification de la passerelle par défaut

Dans une table de routage, la passerelle par défaut se reconnaît par :

- **Destination = 0.0.0.0** (ou 0.0.0.0/0)
- **Masque = 0.0.0.0**

**0.0.0.0 signifie :** "Toutes les adresses IP possibles" = "Par défaut, tout le reste"

### 📍 Pourquoi la passerelle par défaut est-elle importante ?

**Sans passerelle par défaut :**
- ❌ Vous ne pouvez communiquer qu'avec votre réseau local
- ❌ Impossible d'accéder à Internet
- ❌ Impossible d'accéder aux autres réseaux de l'entreprise

**Avec passerelle par défaut :**
- ✅ Vous pouvez accéder à Internet
- ✅ Vous pouvez accéder à tous les réseaux (le routeur se charge de trouver le chemin)

### 🛠️ Configuration typique

Pour un ordinateur à la maison :

| **Paramètre** | **Valeur typique** |
|--------------|-------------------|
| **Adresse IP** | 192.168.1.10 |
| **Masque** | 255.255.255.0 |
| **Passerelle par défaut** | 192.168.1.1 (la box Internet) |

---

## 5️⃣ ROUTES PAR DÉFAUT VS ROUTES SPÉCIFIQUES

### 🆚 Comparaison

| **Type de route** | **Définition** | **Exemple** |
|------------------|----------------|-------------|
| **Route par défaut** | Route utilisée quand aucune autre route ne correspond | 0.0.0.0/0 → 192.168.1.254 |
| **Route spécifique** | Route vers un réseau précis | 10.0.0.0/8 → 192.168.1.200 |

### 📐 Principe de sélection de route

Quand un routeur reçoit un paquet, il suit cette logique :

```
1. Chercher une route SPÉCIFIQUE vers cette destination
   ↓
   Si trouvée → Utiliser cette route
   ↓
   Si non trouvée ↓
2. Utiliser la route PAR DÉFAUT (0.0.0.0/0)
   ↓
   Si trouvée → Utiliser cette route
   ↓
   Si non trouvée ↓
3. ERREUR : "Destination unreachable" (destination inaccessible)
```

### 🔍 Exemple concret

**Table de routage d'un ordinateur :**

| **Destination** | **Masque** | **Passerelle** | **Type** |
|----------------|-----------|---------------|----------|
| 0.0.0.0 | 0.0.0.0 | 192.168.1.254 | Route par défaut |
| 192.168.1.0 | 255.255.255.0 | Direct | Route spécifique (réseau local) |
| 10.50.0.0 | 255.255.0.0 | 192.168.1.200 | Route spécifique (réseau distant) |

**Scénarios :**

1. **Paquet vers 192.168.1.50** → Route spécifique (réseau local) → Envoi direct
2. **Paquet vers 10.50.20.30** → Route spécifique (10.50.0.0/16) → Envoi vers 192.168.1.200
3. **Paquet vers 8.8.8.8** (Google DNS) → Aucune route spécifique → Route par défaut → Envoi vers 192.168.1.254

---

## 6️⃣ AFFICHER LA TABLE DE ROUTAGE

### 🖥️ Commandes selon l'OS

#### Windows

**Commande 1 : `route print`**

```bash
route print
```

**Exemple de résultat :**

```
===========================================================================
Liste d'itinéraires
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0   192.168.1.254    192.168.1.10      25
      192.168.1.0    255.255.255.0       On-link       192.168.1.10     281
```

**Commande 2 : `netstat -r`** (équivalent à `route print`)

```bash
netstat -r
```

---

#### Linux

**Commande 1 : `ip route`** (moderne, recommandée)

```bash
ip route
```

**Exemple de résultat :**

```
default via 192.168.1.254 dev wlan0 proto dhcp metric 600
192.168.1.0/24 dev wlan0 proto kernel scope link src 192.168.1.10
```

**Lecture :**
- **default** = route par défaut (0.0.0.0/0)
- **via 192.168.1.254** = passe par cette passerelle
- **dev wlan0** = utilise l'interface Wi-Fi

---

**Commande 2 : `route -n`** (ancienne, mais encore utilisée)

```bash
route -n
```

**Exemple de résultat :**

```
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.254   0.0.0.0         UG    600    0        0 wlan0
192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 wlan0
```

---

### 🔍 Commande de diagnostic : `tracert` / `traceroute`

Pour voir le **chemin complet** emprunté par un paquet :

**Windows :**
```bash
tracert www.google.com
```

**Linux :**
```bash
traceroute www.google.com
```

**Résultat type :**

```
Tracing route to www.google.com [142.250.178.78]
over a maximum of 30 hops:

  1    <1 ms    <1 ms    <1 ms  192.168.1.254  (box Internet)
  2     5 ms     5 ms     5 ms  80.10.246.1     (routeur FAI)
  3    10 ms    10 ms    11 ms  72.14.212.65    (routeur Google)
  4    11 ms    10 ms    11 ms  142.250.178.78  (serveur Google)
```

**Lecture :** Le paquet a traversé **4 routeurs** avant d'atteindre www.google.com.

---

## 7️⃣ ROUTAGE STATIQUE VS ROUTAGE DYNAMIQUE

### 🆚 Comparaison

| **Critère** | **Routage statique** | **Routage dynamique** |
|-------------|---------------------|----------------------|
| **Configuration** | Manuelle (administrateur saisit les routes) | Automatique (protocoles : OSPF, RIP, BGP) |
| **Mise à jour** | Manuelle en cas de changement | Automatique en cas de panne |
| **Complexité** | Simple | Complexe |
| **Usage** | Petits réseaux, routes fixes | Grands réseaux, Internet |
| **Exemple** | Route vers un réseau spécifique | Internet (millions de routes) |

**Note :** Dans ce cours, nous étudions le **routage statique** (Année 1). Le routage dynamique sera vu en **Année 2**.

---

## 📝 VOCABULAIRE CLÉ À MAÎTRISER

| **Terme** | **Définition** |
|-----------|----------------|
| **Routage** | Processus d'acheminement d'un paquet d'un réseau à un autre |
| **Routeur** | Équipement qui interconnecte des réseaux et achemine les paquets |
| **Table de routage** | Base de données des réseaux accessibles et des chemins |
| **Passerelle (Gateway)** | Routeur suivant vers lequel envoyer un paquet |
| **Passerelle par défaut** | Routeur vers lequel envoyer les paquets non reconnus |
| **Route par défaut** | Route utilisée quand aucune autre route ne correspond (0.0.0.0/0) |
| **Route spécifique** | Route vers un réseau précis (ex : 10.0.0.0/8) |
| **Interface réseau** | Carte réseau d'un routeur (ex : eth0, wlan0) |
| **Métrique** | Coût d'une route (plus c'est bas, mieux c'est) |
| **Hop** | Saut (passage par un routeur) |
| **Traceroute** | Commande pour voir le chemin emprunté par un paquet |
| **Default gateway** | Passerelle par défaut (terme anglais) |
| **Next hop** | Prochain routeur à contacter |
| **Destination unreachable** | Erreur : destination inaccessible |

---

## ✅ AUTO-ÉVALUATION : AI-JE COMPRIS ?

Cochez les affirmations vraies :

- [ ] Un routeur interconnecte plusieurs réseaux
- [ ] La passerelle par défaut a l'adresse 255.255.255.255
- [ ] La route par défaut est identifiée par 0.0.0.0
- [ ] Un switch et un routeur ont la même fonction
- [ ] La table de routage contient la liste des réseaux accessibles
- [ ] Sans passerelle par défaut, je ne peux pas accéder à Internet
- [ ] `tracert` permet de voir le chemin emprunté par un paquet
- [ ] Un paquet ne traverse jamais plus d'un routeur

**Réponses :**
✅ Vrai : 1, 3, 5, 6, 7  
❌ Faux : 2 (la passerelle par défaut est généralement 192.168.x.254 ou .1), 4 (switch = réseau local, routeur = interconnexion de réseaux), 8 (un paquet peut traverser plusieurs routeurs)

---

## 🔗 POUR ALLER PLUS LOIN

### 📚 Ressources complémentaires

- 🎥 **Vidéo** : "Le routage IP expliqué simplement" - Cookie Connecté (YouTube)
- 🌐 **Simulateur** : Cisco Packet Tracer (créer des réseaux virtuels et tester le routage)
- 📖 **Article** : "Comment fonctionne une table de routage ?" - Cisco Networking Academy
- 🛠️ **Outil en ligne** : [https://www.subnetonline.com/](https://www.subnetonline.com/) - Calculateur de routes

### 🎯 Exercices pratiques suggérés

1. Affichez la table de routage de votre ordinateur et identifiez votre passerelle par défaut
2. Faites un `tracert` vers www.google.com et comptez le nombre de routeurs traversés
3. Comparez votre table de routage en Wi-Fi vs en Ethernet (câble)
4. Dessinez le schéma réseau de votre maison avec la box comme routeur

---

## 🏢 APPLICATION EN ENTREPRISE

**Situations professionnelles où vous utiliserez le routage :**

✅ **Diagnostic réseau** : "Pourquoi cet utilisateur ne peut pas accéder au serveur ?" → Vérifier la passerelle par défaut  
✅ **Configuration poste** : Paramétrer l'IP, le masque et la passerelle d'un nouvel ordinateur  
✅ **Architecture réseau** : Comprendre comment les différents services de l'entreprise communiquent  
✅ **Dépannage** : Utiliser `tracert` pour identifier où un paquet est bloqué  
✅ **Documentation** : Documenter la configuration réseau des postes utilisateurs  

**Missions possibles en entreprise cette semaine :**
- Vérifier que tous les postes ont une passerelle par défaut configurée
- Documenter la table de routage de 3 postes différents
- Faire un `tracert` vers le serveur principal de l'entreprise

---

## 🛠️ DÉPANNAGE : PROBLÈMES COURANTS

| **Symptôme** | **Cause probable** | **Solution** |
|-------------|-------------------|-------------|
| "Je ne peux pas accéder à Internet" | Pas de passerelle par défaut | Vérifier avec `ipconfig /all` (Windows) ou `ip a` (Linux) |
| "Je peux accéder au réseau local mais pas à Internet" | Passerelle incorrecte ou en panne | Tester avec `ping` vers la passerelle |
| "Je peux accéder à certains sites mais pas à d'autres" | Route spécifique manquante | Vérifier la table de routage |
| "Erreur : destination unreachable" | Aucune route vers cette destination | Ajouter une route ou vérifier la passerelle |

---

**📅 Fiche rédigée le :** 25/02/2026  
**✍️ Auteur :** Équipe pédagogique CFA  
**📧 Questions :** formation@cfa-exemple.fr  
**🔄 Prochaine mise à jour :** Juin 2026

---

**💡 ASTUCE RÉVISION :** La clé pour comprendre le routage, c'est de bien faire la différence entre "réseau local" (pas besoin de routeur) et "réseau distant" (besoin d'un routeur). Relisez cette fiche et entraînez-vous à afficher votre table de routage ! 🎓
