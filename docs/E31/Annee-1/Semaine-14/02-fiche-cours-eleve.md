# 📖 FICHE COURS - S14 E31
## WiFi Sécurisé - WPA2 - Filtrage MAC

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Configurer AP WiFi sécurisé
- ✅ Activer WPA2-PSK
- ✅ Implémenter filtrage MAC
- ✅ Comprendre limites sécurité WiFi

---

## 1️⃣ WIFI - BASES

### **802.11 (normes)**

| **Norme** | **Année** | **Débit** | **Fréquence** |
|----------|----------|----------|--------------|
| 802.11b | 1999 | 11 Mbps | 2.4 GHz |
| 802.11g | 2003 | 54 Mbps | 2.4 GHz |
| 802.11n | 2009 | 600 Mbps | 2.4/5 GHz |
| 802.11ac | 2014 | 1+ Gbps | 5 GHz |
| 802.11ax (WiFi 6) | 2019 | 10+ Gbps | 2.4/5/6 GHz |

**Lien OSI (S3) :** WiFi = **Couche 2** (Liaison)

---

## 2️⃣ SSID (Service Set Identifier)

### **Définition**

> **SSID** = Nom du réseau WiFi (max 32 caractères)

**Exemples :**
- MFR-TECHCIEL
- WiFi-Invites
- Livebox-A1B2

### **SSID caché**

**Principe :** Ne pas diffuser SSID (broadcast désactivé)

**⚠️ Faux sentiment sécurité :**
- SSID détectable (beacon frames)
- Outils : airodump-ng, Wireshark
- **Pas une vraie protection**

**ANSSI :** Ne pas se fier au SSID caché

---

## 3️⃣ ÉVOLUTION SÉCURITÉ WiFi

| **Sécu** | **Année** | **Niveau** | **État** |
|---------|----------|-----------|----------|
| **Aucune** (Ouvert) | - | ❌❌❌ | Dangereux |
| **WEP** | 1999 | ❌ | Cassé (< 5 min) |
| **WPA** | 2003 | ⚠️ | Vulnérable |
| **WPA2-PSK** | 2004 | ✅ | OK si MDP fort |
| **WPA2-Enterprise** | 2004 | ✅✅ | Serveur RADIUS |
| **WPA3** | 2018 | ✅✅✅ | Meilleur (récent) |

**Recommandation :** **WPA2-PSK minimum** (2026)

---

## 4️⃣ WPA2-PSK

### **Définition**

> **WPA2-PSK** (Pre-Shared Key) = Sécurité WiFi avec **mot de passe partagé**

**PSK** = Tous utilisent même clé

**Chiffrement :** AES (Advanced Encryption Standard)

### **2 formats clé**

**1. Passphrase (recommandé)**
- 8-63 caractères ASCII
- Exemple : `MFR-Techciel-2026-Secure!`

**2. Clé hexadécimale**
- 64 caractères hex (0-9, A-F)
- Générée automatiquement

### **ANSSI Recommandations**

| **Critère** | **ANSSI** |
|------------|----------|
| Longueur min | **20 caractères** |
| Complexité | Maj + min + chiffres + symboles |
| Dictionnaire | Éviter mots courants |
| Renouvellement | Tous les 90 jours (entreprise) |

**Mauvais MDP :**
- ❌ 12345678 (dictionnaire)
- ❌ password (évident)
- ❌ Livebox-1234 (défaut box)

**Bons MDP :**
- ✅ `MFR$Reseau2026!Securise`
- ✅ `WiFi-Admin#TechCiel@2026`

---

## 5️⃣ FILTRAGE MAC

### **Principe**

> **Filtrage MAC** = Autoriser uniquement adresses MAC spécifiques

**Liste blanche :**
```
AA:BB:CC:DD:EE:01 (PC Direction)
AA:BB:CC:DD:EE:02 (PC Admin)
AA:BB:CC:DD:EE:03 (PC IT)
```

**Résultat :** Autres MAC refusées

---

### **⚠️ LIMITES (IMPORTANTES)**

**1. MAC spoofing (usurpation)**

Attaquant change son MAC :
```
Vrai MAC : 11:22:33:44:55:66
Faux MAC : AA:BB:CC:DD:EE:01 (copie autorisée)
```

**Outil :** macchanger (Linux)

**2. Gestion lourde**

50 PC = 50 MAC à gérer manuellement

**3. Faux sentiment sécurité**

Filtrage MAC ≠ Chiffrement

**ANSSI :** Filtrage MAC = **Complément**, pas sécurité principale

---

## 6️⃣ CONFIGURATION AP

### **Accès interface web**

**1. Connexion Ethernet (S2 câble)**

**2. IP par défaut** (exemples)
- TP-Link : 192.168.0.1
- Ubiquiti : 192.168.1.1
- Netgear : 192.168.1.1

**3. Navigateur**
```
http://192.168.1.1
```

**4. Login défaut**
- User : admin
- Pass : admin (CHANGER !)

---

### **Paramètres essentiels**

**SSID :**
- Nom : MFR-TECHCIEL
- Broadcast : Activé

**Sécurité :**
- Mode : WPA2-PSK
- Chiffrement : AES
- Passphrase : 20+ caractères

**Canal :**
- 2.4 GHz : 1, 6 ou 11 (non-overlap)
- 5 GHz : Auto

**Filtrage MAC :**
- Liste blanche
- Ajouter MAC autorisées

---

## 7️⃣ WIFI INVITÉ ISOLÉ (VLAN)

### **Lien S13 (VLANs)**

**Problème :** Invités accèdent réseau interne

**Solution :** VLAN invité isolé

**Configuration :**

```
VLAN 10 : Réseau interne (employés)
VLAN 99 : WiFi invité (isolé)
```

**AP Config :**
- SSID1 : MFR-ADMIN (VLAN 10)
- SSID2 : MFR-INVITES (VLAN 99)

**Résultat :** Invités Internet seulement (pas LAN)

---

## 8️⃣ BONNES PRATIQUES ANSSI

### **Checklist sécurité WiFi**

**☑ WPA2-PSK minimum** (WPA3 si possible)  
**☑ Passphrase 20+ caractères**  
**☑ Changer MDP par défaut AP**  
**☑ Firmware AP à jour**  
**☑ Désactiver WPS** (vulnérable)  
**☑ WiFi invité isolé** (VLAN)  
**☑ Filtrage MAC** (complément)  
**☑ Monitoring logs** (détection intrusion)  

---

## 📚 VOCABULAIRE

| **Terme** | **Définition** |
|-----------|----------------|
| **SSID** | Nom réseau WiFi |
| **WPA2-PSK** | Sécurité WiFi clé partagée |
| **AES** | Chiffrement WPA2 |
| **Filtrage MAC** | Liste blanche adresses |
| **MAC spoofing** | Usurpation adresse MAC |
| **WPS** | WiFi Protected Setup (vulnérable) |
| **802.11** | Norme WiFi |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je configure AP WPA2-PSK
- [ ] Je crée passphrase 20+ car
- [ ] J'active filtrage MAC
- [ ] Je comprends limites filtrage
- [ ] J'isole WiFi invité (VLAN)

---

## 📌 POINTS-CLÉS

1. **WPA2-PSK** = Minimum sécurité (WEP obsolète)
2. **Passphrase** : 20+ caractères (ANSSI)
3. **Filtrage MAC** : Complément (pas sécu principale)
4. **SSID caché** : Fausse sécurité
5. **WiFi invité** : VLAN isolé (S13)

---

**Document - Version 1.0 - Février 2026**
