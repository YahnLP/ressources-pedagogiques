# 📖 FICHE COURS - S4 E31
## Adressage IPv4 - Classes - CIDR

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Comprendre format IPv4 (32 bits)
- ✅ Différencier classes A/B/C
- ✅ Utiliser notation CIDR
- ✅ Calculer nombre d'hôtes
- ✅ Créer plan d'adressage

---

## 1️⃣ QU'EST-CE QU'UNE ADRESSE IPv4 ?

### **Définition**

> **IPv4** = Internet Protocol version 4  
> Adresse **unique** qui identifie un équipement sur un réseau.

**Format :** 4 octets (32 bits)

**Notation décimale pointée :**
```
192.168.1.10
 │   │   │  │
 └───┴───┴──┴─ 4 octets (0-255)
```

**Exemple :**
- Ordinateur : 192.168.1.50
- Serveur : 192.168.1.5
- Routeur : 192.168.1.1

---

### **Lien avec OSI (S3)**

**IPv4 = Couche 3 (Réseau)**
- Permet routage entre réseaux
- Équipement : Routeur

---

## 2️⃣ STRUCTURE ADRESSE IP

**Composants :**

```
192.168.1.10
 └─┬──┘ └┬─┘
   │     │
Réseau  Hôte
```

- **Partie Réseau** : Identifie le réseau (ex: 192.168.1)
- **Partie Hôte** : Identifie l'équipement dans le réseau (ex: 10)

**Analogie adresse postale :**
- **Réseau** = Ville (Paris)
- **Hôte** = Numéro rue (12 rue Voltaire)

---

## 3️⃣ LES CLASSES IPv4

### **Classe A**

| **Critère** | **Valeur** |
|------------|-----------|
| **1er octet** | 1 - 126 |
| **Début** | 1.0.0.0 |
| **Fin** | 126.255.255.255 |
| **Masque défaut** | 255.0.0.0 (/8) |
| **Nb réseaux** | 126 |
| **Nb hôtes/réseau** | 16 777 214 |
| **Usage** | Très grandes entreprises |

**Exemple :** 10.50.100.20

---

### **Classe B**

| **Critère** | **Valeur** |
|------------|-----------|
| **1er octet** | 128 - 191 |
| **Début** | 128.0.0.0 |
| **Fin** | 191.255.255.255 |
| **Masque défaut** | 255.255.0.0 (/16) |
| **Nb hôtes/réseau** | 65 534 |
| **Usage** | Moyennes entreprises |

**Exemple :** 172.16.0.100

---

### **Classe C**

| **Critère** | **Valeur** |
|------------|-----------|
| **1er octet** | 192 - 223 |
| **Début** | 192.0.0.0 |
| **Fin** | 223.255.255.255 |
| **Masque défaut** | 255.255.255.0 (/24) |
| **Nb hôtes/réseau** | 254 |
| **Usage** | Petites entreprises, domicile |

**Exemple :** 192.168.1.50

---

### **Identifier la classe**

**Méthode :** Regarder le **1er octet**

| **1er octet** | **Classe** | **Exemple** |
|--------------|-----------|-------------|
| 1-126 | **A** | 10.0.0.1 |
| 128-191 | **B** | 172.16.0.1 |
| 192-223 | **C** | 192.168.1.1 |

**⚠️ Exception :** 127.x.x.x = **Loopback** (localhost)

---

## 4️⃣ ADRESSES PRIVÉES vs PUBLIQUES

### **Adresses privées (RFC 1918)**

**Non routées sur Internet**

| **Classe** | **Plage privée** | **Masque** |
|-----------|-----------------|-----------|
| **A** | 10.0.0.0 - 10.255.255.255 | 255.0.0.0 (/8) |
| **B** | 172.16.0.0 - 172.31.255.255 | 255.255.0.0 (/16) |
| **C** | 192.168.0.0 - 192.168.255.255 | 255.255.255.0 (/24) |

**Usage :** Réseaux locaux (LAN)

---

### **Adresses publiques**

**Routées sur Internet**

**Exemples :**
- 8.8.8.8 (Google DNS)
- 1.1.1.1 (Cloudflare DNS)

**Attribution :** IANA → RIR → FAI → Vous

---

### **Pourquoi privées ?**

✅ **Économie** : Pas assez d'IP publiques pour tous  
✅ **Sécurité** : Réseau local invisible d'Internet  
✅ **Gratuit** : Pas de location IP publique  

**NAT** (Network Address Translation) : Convertit IP privée ↔ publique

---

## 5️⃣ NOTATION CIDR

### **Définition**

**CIDR** = Classless Inter-Domain Routing

**Format :** `192.168.1.0/24`

**Le /24 signifie :**
- **24 bits** pour la partie **réseau**
- **32 - 24 = 8 bits** pour la partie **hôte**

---

### **Équivalence CIDR ↔ Masque**

| **CIDR** | **Masque** | **Classe par défaut** |
|---------|-----------|---------------------|
| **/8** | 255.0.0.0 | Classe A |
| **/16** | 255.255.0.0 | Classe B |
| **/24** | 255.255.255.0 | Classe C |

**Autres CIDR courants :**

| **CIDR** | **Masque** | **Nb hôtes** |
|---------|-----------|-------------|
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /30 | 255.255.255.252 | 2 |

---

## 6️⃣ MASQUE SOUS-RÉSEAU

### **Rôle**

> Le **masque** sépare la partie **réseau** de la partie **hôte**.

**Exemple :** 192.168.1.50 / 255.255.255.0

```
IP :     192.168.1.50
Masque : 255.255.255.0
         └──┬───┘ └┬┘
         Réseau  Hôte
         
Réseau = 192.168.1.0
Hôte = 50
```

---

### **Calcul nombre d'hôtes**

**Formule :** 2^n - 2

- **n** = nombre de bits pour hôte
- **-2** = retirer adresse réseau et broadcast

**Exemple /24 :**
- 32 - 24 = 8 bits hôte
- 2^8 - 2 = 256 - 2 = **254 hôtes**

**Tableau rapide :**

| **CIDR** | **Bits hôte** | **Calcul** | **Nb hôtes** |
|---------|--------------|-----------|-------------|
| /8 | 24 bits | 2^24 - 2 | 16 777 214 |
| /16 | 16 bits | 2^16 - 2 | 65 534 |
| /24 | 8 bits | 2^8 - 2 | 254 |
| /25 | 7 bits | 2^7 - 2 | 126 |
| /26 | 6 bits | 2^6 - 2 | 62 |
| /30 | 2 bits | 2^2 - 2 | 2 |

---

## 7️⃣ ADRESSES SPÉCIALES

### **Adresse réseau**

**Définition :** 1ère adresse du réseau (tous les bits hôte à 0)

**Exemple :** 192.168.1.0/24
- Adresse réseau = 192.168.1.**0**

**⚠️ Non assignable** à un équipement

---

### **Adresse broadcast**

**Définition :** Dernière adresse du réseau (tous les bits hôte à 1)

**Exemple :** 192.168.1.0/24
- Broadcast = 192.168.1.**255**

**Usage :** Envoyer message à **tous** les hôtes du réseau

**⚠️ Non assignable** à un équipement

---

### **Passerelle (Gateway)**

**Définition :** Adresse du routeur (sortie du réseau local)

**Convention :** Souvent 1ère adresse disponible

**Exemple :** 192.168.1.0/24
- Passerelle = 192.168.1.**1**

---

### **Plage utilisable**

**Exemple :** 192.168.1.0/24

- Réseau : 192.168.1.0 (non assignable)
- **Utilisable : 192.168.1.1 - 192.168.1.254**
- Broadcast : 192.168.1.255 (non assignable)

**Total utilisable :** 254 adresses

---

## 8️⃣ PLAN D'ADRESSAGE

### **Étapes**

**1. Analyser besoins**
- Combien d'équipements ?
- Combien de services ?

**2. Choisir classe**
- < 254 hôtes → Classe C
- 254-65k hôtes → Classe B
- > 65k hôtes → Classe A

**3. Choisir réseau**
- Privé (LAN) ou public (Internet)
- Exemple : 192.168.1.0/24

**4. Répartir adresses**
- Bloquer par service
- Réserver début (serveurs, équipements critiques)

**5. Documenter**
- Tableau récapitulatif
- Schéma réseau

---

### **Exemple : PME 80 PC**

| **Service** | **Nb PC** | **Plage IP** |
|------------|----------|-------------|
| Direction | 5 | 192.168.1.10-14 |
| Compta | 10 | 192.168.1.20-29 |
| Production | 50 | 192.168.1.50-99 |
| Logistique | 15 | 192.168.1.100-114 |
| **Serveurs** | 3 | 192.168.1.5-7 |
| **Passerelle** | 1 | 192.168.1.1 |

**Réseau :** 192.168.1.0/24  
**Total :** 84 adresses / 254 disponibles

---

## ✅ AUTO-ÉVALUATION

- [ ] Je différencie classes A/B/C
- [ ] Je convertis /24 en 255.255.255.0
- [ ] Je calcule nb hôtes d'un /24 (254)
- [ ] Je distingue IP privée vs publique
- [ ] Je peux créer plan adressage simple

---

## 📚 VOCABULAIRE

| **Terme** | **Définition** |
|-----------|----------------|
| **IPv4** | Adresse 32 bits (4 octets) |
| **Classe** | Catégorie IP (A/B/C) |
| **CIDR** | Notation /xx (nb bits réseau) |
| **Masque** | Sépare réseau/hôte |
| **Privé** | IP non routée Internet |
| **Public** | IP routée Internet |
| **Passerelle** | Routeur (sortie réseau) |
| **Broadcast** | Envoi à tous (dernière IP) |

---

## 📌 POINTS-CLÉS

1. **IPv4** = 32 bits (4 octets 0-255)
2. **Classes** : A (1-126), B (128-191), C (192-223)
3. **Privées** : 10.x, 172.16-31.x, 192.168.x
4. **/24** = 255.255.255.0 = 254 hôtes
5. **Plan** : Analyser → Choisir → Répartir → Documenter

---

## 📸 PORTFOLIO

- Plan d'adressage MFR complété
- Schéma réseau annoté
- Tableau classes A/B/C

---

**Document - BAC PRO CIEL - Version 1.0 - Février 2026**
