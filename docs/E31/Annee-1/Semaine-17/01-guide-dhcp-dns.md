# 🔧 GUIDE TECHNIQUE - S17 E31
## Configuration DHCP + DNS - Projet TECHCORP

---

## 🎯 OBJECTIF

Installer et configurer DHCP + DNS pour attribution IP automatique et résolution noms sur infrastructure TECHCORP.

---

## 📋 PRÉREQUIS

- [ ] Active Directory installé (S16, domaine techcorp.local)
- [ ] VLANs créés et fonctionnels (S16)
- [ ] Routage inter-VLAN opérationnel (S16)
- [ ] Plan d'adressage validé (S16 Jalon 1)

---

## 1️⃣ INSTALLATION DHCP

### **Procédure Windows Server**

**Étape 1 : Ajouter rôle**

```
1. Gestionnaire de serveur
2. Gérer → Ajouter rôles et fonctionnalités
3. Type installation : Installation basée sur un rôle
4. Serveur : SRV-DC01 (local)
5. Rôles serveur : Cocher "Serveur DHCP"
6. Fonctionnalités : [Par défaut]
7. Confirmer → Installer
```

**Étape 2 : Configuration post-installation**

```
1. Notification (drapeau) → Terminer configuration DHCP
2. Description : [Par défaut]
3. Autorisation : Utiliser identifiants actuels
4. Résumé → Valider → Fermer
```

**⚠️ CRITIQUE :** Autorisation DHCP obligatoire (intégration AD)

---

### **Vérification installation**

**Ouvrir console DHCP :**
```
dhcpmgmt.msc
```

**Arborescence attendue :**
```
DHCP
 └─ srv-dc01.techcorp.local
    ├─ IPv4
    │  └─ [Vide pour l'instant]
    └─ IPv6
```

---

## 2️⃣ CONFIGURATION SCOPES DHCP

### **Scope = Pool IP par VLAN**

**TECHCORP = 5 scopes (5 VLANs)**

---

### **SCOPE 1 : VLAN 10 (Direction)**

**Clic droit IPv4 → Nouvelle étendue**

**Assistant configuration :**

| **Paramètre** | **Valeur** |
|--------------|-----------|
| **Nom** | VLAN10-Direction |
| **Description** | Pool DHCP Direction (5 PC) |
| **Adresse IP début** | 192.168.10.10 |
| **Adresse IP fin** | 192.168.10.50 |
| **Longueur masque** | 24 |
| **Masque sous-réseau** | 255.255.255.0 |

**Exclusions :**
```
192.168.10.1 - 192.168.10.9
(Réservé : Gateway .1, Serveurs .2-.9)
```

**Durée bail :**
```
8 jours (par défaut)
```

**Options DHCP (TRÈS IMPORTANT) :**

**Option 003 - Routeur (Gateway) :**
```
192.168.10.1
```

**Option 006 - Serveur DNS :**
```
192.168.30.5 (SRV-DC01)
```

**Option 015 - Nom domaine DNS :**
```
techcorp.local
```

**Activer étendue :** Oui

---

### **SCOPE 2 : VLAN 20 (Administration)**

| Paramètre | Valeur |
|-----------|--------|
| Nom | VLAN20-Administration |
| Début | 192.168.20.10 |
| Fin | 192.168.20.50 |
| Masque | 255.255.255.0 |
| Exclusions | 192.168.20.1 - .9 |
| Option 003 | 192.168.20.1 |
| Option 006 | 192.168.30.5 |
| Option 015 | techcorp.local |

---

### **SCOPE 3 : VLAN 30 (IT)**

| Paramètre | Valeur |
|-----------|--------|
| Nom | VLAN30-IT |
| Début | 192.168.30.10 |
| Fin | 192.168.30.50 |
| Masque | 255.255.255.0 |
| Exclusions | 192.168.30.1 - .9 |
| Option 003 | 192.168.30.1 |
| Option 006 | 192.168.30.5 |

---

### **SCOPE 4 : VLAN 40 (Commercial)**

| Paramètre | Valeur |
|-----------|--------|
| Nom | VLAN40-Commercial |
| Début | 192.168.40.10 |
| Fin | 192.168.40.50 |
| Exclusions | 192.168.40.1 - .9 |
| Option 003 | 192.168.40.1 |
| Option 006 | 192.168.30.5 |

---

### **SCOPE 5 : VLAN 99 (WiFi Invités)**

| Paramètre | Valeur |
|-----------|--------|
| Nom | VLAN99-WiFi-Invites |
| Début | 192.168.99.10 |
| Fin | 192.168.99.100 |
| Exclusions | 192.168.99.1 - .9 |
| Option 003 | 192.168.99.1 |
| Option 006 | 192.168.30.5 |

---

### **Vérification scopes**

**Console DHCP :**
```
IPv4
 ├─ Étendue [192.168.10.0] VLAN10-Direction
 │  ├─ Pool d'adresses (41 adresses)
 │  ├─ Exclusions (.1-.9)
 │  └─ Options d'étendue (003, 006, 015)
 ├─ Étendue [192.168.20.0] VLAN20-Administration
 ├─ Étendue [192.168.30.0] VLAN30-IT
 ├─ Étendue [192.168.40.0] VLAN40-Commercial
 └─ Étendue [192.168.99.0] VLAN99-WiFi-Invites
```

**Statut :** 🟢 Vert (actif) pour tous

---

## 3️⃣ TESTS DHCP

### **Test 1 : Attribution automatique**

**Sur PC client VLAN 10 :**

**1. Libérer IP actuelle (si statique)**
```cmd
ipconfig /release
```

**2. Demander nouvelle IP DHCP**
```cmd
ipconfig /renew
```

**3. Vérifier IP attribuée**
```cmd
ipconfig /all
```

**Résultat attendu :**
```
Carte Ethernet :
   Adresse IPv4 : 192.168.10.10 (DHCP activé)
   Masque sous-réseau : 255.255.255.0
   Passerelle par défaut : 192.168.10.1
   Serveur DHCP : 192.168.30.5
   Serveurs DNS : 192.168.30.5
```

---

### **Test 2 : Logs serveur DHCP**

**Console DHCP :**
```
IPv4 → Étendue VLAN10 → Baux d'adresses
```

**Voir :**
- Adresse IP louée : 192.168.10.10
- Client : PC-DIRECTION-01
- Bail expire : [Date + 8 jours]

---

### **Test 3 : Wireshark DHCP**

**Capturer sur interface réseau :**

**Filtre :** `dhcp`

**Séquence DORA attendue :**
```
1. DHCP Discover (Client → Broadcast)
   Source : 0.0.0.0
   Destination : 255.255.255.255

2. DHCP Offer (Serveur → Client)
   Your IP : 192.168.10.10
   Serveur DHCP : 192.168.30.5

3. DHCP Request (Client → Serveur)
   Requested IP : 192.168.10.10

4. DHCP ACK (Serveur → Client)
   Confirmation attribution
```

**Sauvegarder :** `dhcp-vlan10.pcap`

---

## 4️⃣ CONFIGURATION DNS

### **DNS installé avec AD (S16)**

**Zones déjà créées automatiquement :**

**Zone directe :**
```
techcorp.local
```

**Zone inverse :**
```
10.168.192.in-addr.arpa (pour 192.168.10.0/24)
20.168.192.in-addr.arpa (pour 192.168.20.0/24)
30.168.192.in-addr.arpa (pour 192.168.30.0/24)
...
```

---

### **Ajout enregistrements A (hôtes)**

**Ouvrir console DNS :**
```
dnsmgmt.msc
```

**Arborescence :**
```
DNS
 └─ SRV-DC01
    ├─ Zones de recherche directes
    │  └─ techcorp.local
    └─ Zones de recherche inversées
```

---

### **Enregistrement serveur DC**

**Zone techcorp.local → Clic droit → Nouvel hôte (A)**

| Paramètre | Valeur |
|-----------|--------|
| Nom | srv-dc01 |
| Adresse IP | 192.168.30.5 |
| TTL | Par défaut (1 heure) |
| ☑ Créer enregistrement PTR | Coché |

**Résultat :**
```
srv-dc01.techcorp.local → 192.168.30.5
```

---

### **Enregistrement serveur fichiers**

| Paramètre | Valeur |
|-----------|--------|
| Nom | srv-files |
| IP | 192.168.30.6 |
| PTR | Coché |

---

### **Enregistrements alias (CNAME)**

**Alias pratiques :**

| Alias | Cible |
|-------|-------|
| dc | srv-dc01.techcorp.local |
| fichiers | srv-files.techcorp.local |
| intranet | srv-dc01.techcorp.local |

**Procédure :**
```
Clic droit zone → Nouvel alias (CNAME)
Nom alias : dc
FQDN cible : srv-dc01.techcorp.local
```

---

## 5️⃣ TESTS DNS

### **Test 1 : nslookup nom → IP**

**Sur PC client :**

```cmd
nslookup srv-dc01.techcorp.local
```

**Résultat attendu :**
```
Serveur : srv-dc01.techcorp.local
Adresse : 192.168.30.5

Nom : srv-dc01.techcorp.local
Adresse : 192.168.30.5
```

---

### **Test 2 : nslookup IP → nom (inverse)**

```cmd
nslookup 192.168.30.5
```

**Résultat attendu :**
```
Nom : srv-dc01.techcorp.local
Adresse : 192.168.30.5
```

---

### **Test 3 : ping hostname**

```cmd
ping srv-dc01.techcorp.local
```

**Résultat attendu :**
```
Envoi d'une requête 'ping' sur srv-dc01.techcorp.local [192.168.30.5]
Réponse de 192.168.30.5 : octets=32 temps<1ms TTL=128
```

**✅ Succès = DNS résout correctement**

---

### **Test 4 : Wireshark DNS**

**Capturer :**

**Filtre :** `dns`

**Séquence Query/Response :**
```
1. DNS Query (Client → Serveur DNS)
   Questions : srv-dc01.techcorp.local
   Type : A (adresse IPv4)

2. DNS Response (Serveur → Client)
   Answers : 1
   srv-dc01.techcorp.local : 192.168.30.5
```

**Sauvegarder :** `dns-query.pcap`

---

## ✅ CHECKLIST VALIDATION

**DHCP :**
- [ ] Rôle DHCP installé
- [ ] 5 scopes créés et actifs
- [ ] Options 003/006 configurées
- [ ] Test ipconfig /renew réussi
- [ ] Capture Wireshark DORA sauvegardée

**DNS :**
- [ ] Zones directe/inverse créées
- [ ] Enregistrements A serveurs ajoutés
- [ ] nslookup nom → IP OK
- [ ] nslookup IP → nom OK
- [ ] ping hostname fonctionne
- [ ] Capture Wireshark Query/Response sauvegardée

---

## ⚠️ DÉPANNAGE

**Problème : DHCP ne distribue pas**

**Causes possibles :**
1. Serveur DHCP non autorisé (AD)
   → Vérifier Autorisation dans console DHCP
2. Scope désactivé
   → Activer étendue
3. Pool IP épuisé
   → Vérifier baux + augmenter plage

---

**Problème : DNS ne résout pas**

**Causes possibles :**
1. Service DNS arrêté
   → Démarrer service DNS (services.msc)
2. Zone mal configurée
   → Vérifier zone techcorp.local existe
3. Client pointe mauvais DNS
   → ipconfig /all → Vérifier serveur DNS = 192.168.30.5

---

**Document - Guide Technique DHCP+DNS - Version 1.0 - Février 2026**
