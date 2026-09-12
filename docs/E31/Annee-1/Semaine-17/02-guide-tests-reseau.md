# 🧪 GUIDE TESTS RÉSEAU - S17 E31
## Validation Infrastructure TECHCORP

---

## 🎯 OBJECTIF

Tester et valider TOUS les aspects réseau de l'infrastructure TECHCORP avec méthodologie professionnelle.

---

## 📋 PLAN DE TESTS

### **3 niveaux de tests**

**Niveau 1 : Tests BASIQUES (ping)**
- Connectivité intra-VLAN
- Connectivité inter-VLAN
- Connectivité Internet

**Niveau 2 : Tests SERVICES (nslookup, tracert)**
- Résolution DNS
- Chemin réseau
- Latence

**Niveau 3 : Tests AVANCÉS (Wireshark)**
- Protocoles (DHCP, DNS, ICMP)
- Validation encapsulation OSI
- Détection anomalies

---

## 1️⃣ TESTS PING

### **TEST 1.1 : Ping Intra-VLAN (même réseau)**

**Objectif :** Vérifier communication dans même VLAN

**Procédure :**

**PC1 VLAN 10 (192.168.10.10) → PC2 VLAN 10 (192.168.10.11)**

```cmd
ping 192.168.10.11
```

**Résultat attendu :**
```
Envoi d'une requête 'ping' sur 192.168.10.11
Réponse de 192.168.10.11 : octets=32 temps<1ms TTL=128
Réponse de 192.168.10.11 : octets=32 temps<1ms TTL=128
Réponse de 192.168.10.11 : octets=32 temps<1ms TTL=128
Réponse de 192.168.10.11 : octets=32 temps<1ms TTL=128

Statistiques Ping pour 192.168.10.11:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (0% perte)
```

**✅ Validation :**
- 0% perte paquets
- Temps < 10ms (LAN local)
- TTL = 128 (Windows) ou 64 (Linux)

**❌ Échec :**
- "Délai d'attente dépassé" → Vérifier IP, câble, VLAN
- "Hôte de destination inaccessible" → Vérifier gateway

---

### **TEST 1.2 : Ping Inter-VLAN (routage)**

**Objectif :** Vérifier routage entre VLANs

**PC VLAN 10 (192.168.10.10) → PC VLAN 20 (192.168.20.10)**

```cmd
ping 192.168.20.10
```

**Résultat attendu :**
```
Réponse de 192.168.20.10 : octets=32 temps=2ms TTL=127
```

**⚠️ IMPORTANT :**
- TTL = **127** (pas 128) car passage routeur (TTL-1)

**✅ Validation :**
- Réponse OK
- TTL = 127 (1 saut routeur)

**❌ Échec :**
- Vérifier routage inter-VLAN configuré (S16)
- Vérifier gateway dans ipconfig

---

### **TEST 1.3 : Ping Gateway**

**Objectif :** Vérifier accès routeur

**PC VLAN 10 → Gateway VLAN 10**

```cmd
ping 192.168.10.1
```

**Résultat attendu :**
```
Réponse de 192.168.10.1 : octets=32 temps<1ms TTL=255
```

**TTL élevé (255) = équipement réseau**

---

### **TEST 1.4 : Ping Serveur DNS**

**PC VLAN 10 → Serveur DNS (192.168.30.5)**

```cmd
ping 192.168.30.5
```

**✅ OK = Routage VLAN10 → VLAN30 fonctionne**

---

### **TEST 1.5 : Ping Internet (optionnel)**

**PC VLAN 10 → Google DNS**

```cmd
ping 8.8.8.8
```

**Résultat attendu :**
```
Réponse de 8.8.8.8 : octets=32 temps=15ms TTL=115
```

**⚠️ Nécessite :** NAT configuré sur routeur (hors scope A1)

---

## 2️⃣ TESTS NSLOOKUP (DNS)

### **TEST 2.1 : Résolution hostname → IP**

**Objectif :** Vérifier DNS résout noms

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

**✅ Validation :**
- Serveur DNS répond
- Nom résolu en IP correcte

---

### **TEST 2.2 : Résolution IP → hostname (inverse)**

```cmd
nslookup 192.168.30.5
```

**Résultat attendu :**
```
Nom : srv-dc01.techcorp.local
Adresse : 192.168.30.5
```

**⚠️ Nécessite :** Zone inverse DNS configurée

---

### **TEST 2.3 : Résolution alias (CNAME)**

```cmd
nslookup dc.techcorp.local
```

**Résultat attendu :**
```
dc.techcorp.local
  canonical name = srv-dc01.techcorp.local
Nom : srv-dc01.techcorp.local
Adresse : 192.168.30.5
```

---

### **TEST 2.4 : Résolution externe (Internet)**

```cmd
nslookup google.com
```

**Résultat attendu :**
```
Serveur : srv-dc01.techcorp.local
Adresse : 192.168.30.5

Réponse ne faisant pas autorité :
Nom : google.com
Adresses : 142.250.x.x
```

**✅ OK = DNS forwarding configuré (externe)**

---

## 3️⃣ TESTS TRACERT (Chemin réseau)

### **TEST 3.1 : Tracert Inter-VLAN**

**Objectif :** Voir chemin réseau + gateways

**PC VLAN 10 → PC VLAN 20**

```cmd
tracert 192.168.20.10
```

**Résultat attendu :**
```
Détermination de l'itinéraire vers 192.168.20.10

  1    <1 ms    <1 ms    <1 ms  192.168.10.1 (Gateway VLAN10)
  2     2 ms     1 ms     1 ms  192.168.20.10
```

**✅ Validation :**
- 2 sauts (gateway + destination)
- Saut 1 = Gateway VLAN10 (192.168.10.1)

---

### **TEST 3.2 : Tracert Serveur**

**PC VLAN 10 → Serveur VLAN 30**

```cmd
tracert 192.168.30.5
```

**Résultat attendu :**
```
  1    <1 ms    192.168.10.1
  2     2 ms    192.168.30.5
```

---

### **TEST 3.3 : Tracert Internet**

```cmd
tracert 8.8.8.8
```

**Résultat attendu :**
```
  1    <1 ms    192.168.10.1 (Gateway interne)
  2    10 ms    [IP FAI]
  3    15 ms    ...
  ...
  N    20 ms    8.8.8.8
```

**⚠️ Plusieurs sauts = normal (Internet)**

---

## 4️⃣ TABLEAU RÉCAPITULATIF TESTS

### **Tableau à compléter (livrables projet)**

| **Test** | **Source** | **Destination** | **Résultat** | **Capture** |
|---------|-----------|----------------|-------------|------------|
| Ping intra-VLAN | VLAN10 | VLAN10 | ✅ OK | ping-intra.pcap |
| Ping inter-VLAN | VLAN10 | VLAN20 | ✅ OK | ping-inter.pcap |
| Ping gateway | VLAN10 | 192.168.10.1 | ✅ OK | - |
| Ping serveur DNS | VLAN10 | 192.168.30.5 | ✅ OK | - |
| nslookup hostname | Client | srv-dc01 | ✅ OK | dns-query.pcap |
| nslookup IP | Client | 192.168.30.5 | ✅ OK | - |
| DHCP renew | Client | DHCP Server | ✅ OK | dhcp-dora.pcap |
| tracert inter-VLAN | VLAN10 | VLAN20 | ✅ OK | - |

---

## 5️⃣ CAPTURES WIRESHARK OBLIGATOIRES

### **CAPTURE 1 : DHCP (DORA)**

**Procédure :**

1. **Lancer Wireshark** (interface réseau client)

2. **Filtre capture :** `port 67 or port 68`

3. **Déclencher DHCP :**
```cmd
ipconfig /release
ipconfig /renew
```

4. **Arrêter capture**

5. **Vérifier 4 paquets DORA :**
   - Discover
   - Offer
   - Request
   - ACK

6. **Sauvegarder :** `dhcp-vlan10.pcap`

---

### **CAPTURE 2 : DNS Query/Response**

**Procédure :**

1. **Wireshark** (filtre `dns`)

2. **Déclencher DNS :**
```cmd
nslookup srv-dc01.techcorp.local
```

3. **Vérifier 2 paquets :**
   - Query (Question : srv-dc01.techcorp.local)
   - Response (Answer : 192.168.30.5)

4. **Sauvegarder :** `dns-query.pcap`

---

### **CAPTURE 3 : Ping Inter-VLAN**

**Procédure :**

1. **Wireshark** (filtre `icmp`)

2. **Ping :**
```cmd
ping 192.168.20.10 -n 4
```

3. **Vérifier :**
   - Echo Request (Type 8)
   - Echo Reply (Type 0)

4. **Sauvegarder :** `ping-inter-vlan.pcap`

---

### **CAPTURE 4 : Encapsulation OSI (bonus)**

**Objectif :** Montrer empilement couches OSI (lien S3)

**Procédure :**

1. **Wireshark** capture ping

2. **Clic paquet → Détails**

3. **Observer arbre :**
```
Frame (C1 Physique)
 └─ Ethernet II (C2 Liaison)
    └─ Internet Protocol (C3 Réseau)
       └─ ICMP (C3 aussi)
```

4. **Screenshot** arbre encapsulation

---

## ✅ CHECKLIST VALIDATION TESTS

**Tests basiques :**
- [ ] Ping intra-VLAN réussi
- [ ] Ping inter-VLAN réussi
- [ ] Ping gateway réussi
- [ ] Ping serveur DNS réussi

**Tests services :**
- [ ] nslookup hostname → IP OK
- [ ] nslookup IP → hostname OK
- [ ] tracert montre gateways

**Captures Wireshark :**
- [ ] dhcp-vlan10.pcap (DORA complet)
- [ ] dns-query.pcap (Query + Response)
- [ ] ping-inter-vlan.pcap (ICMP)

**Documentation :**
- [ ] Tableau tests rempli
- [ ] Captures sauvegardées (.pcap)
- [ ] Screenshots résultats

---

## ⚠️ DÉPANNAGE TESTS

**Ping échoue :**
1. Vérifier IP source (`ipconfig`)
2. Vérifier gateway configurée
3. Vérifier routage inter-VLAN (routeur)
4. Vérifier pare-feu (désactiver temporairement)

**nslookup échoue :**
1. Vérifier serveur DNS client (ipconfig /all)
2. Vérifier service DNS démarré (serveur)
3. Vérifier zone DNS existe

**DHCP n'attribue pas :**
1. Vérifier scope actif
2. Vérifier pool IP non épuisé
3. Vérifier autorisation serveur DHCP

---

**Document - Guide Tests Réseau - Version 1.0 - Février 2026**
