# 🔍 GUIDE WIRESHARK - S17 E31
## Captures Validation Projet TECHCORP

---

## 🎯 OBJECTIF

Capturer et analyser protocoles réseau pour PROUVER le bon fonctionnement de l'infrastructure TECHCORP.

**Wireshark = PREUVE TECHNIQUE** du projet

---

## 📋 CAPTURES OBLIGATOIRES (Livrables)

| **Capture** | **Protocole** | **Preuve de...** | **Fichier** |
|------------|--------------|----------------|------------|
| DHCP DORA | DHCP | Attribution IP automatique | dhcp-vlan10.pcap |
| DNS Query/Response | DNS | Résolution noms | dns-query.pcap |
| Ping Inter-VLAN | ICMP | Routage inter-VLAN | ping-inter.pcap |
| (Bonus) TCP Handshake | TCP | Connexion AD | tcp-ad.pcap |

---

## 1️⃣ CAPTURE DHCP (DORA)

### **Préparation**

**Objectif :** Voir séquence complète DHCP (4 paquets)

**Filtre capture :**
```
port 67 or port 68
```
(Ports DHCP serveur=67, client=68)

---

### **Procédure**

**1. Lancer Wireshark**
```
Interface réseau du PC client
```

**2. Démarrer capture**

**3. Forcer renouvellement DHCP**
```cmd
ipconfig /release
ipconfig /renew
```

**4. Arrêter capture (après ~5 secondes)**

---

### **Analyse attendue**

**Filtre display :** `dhcp`

**4 paquets DORA :**

**Paquet 1 : DHCP Discover**
```
Source : 0.0.0.0 (client sans IP)
Destination : 255.255.255.255 (broadcast)
Message Type : DHCP Discover
Transaction ID : 0x12345678
```

**Paquet 2 : DHCP Offer**
```
Source : 192.168.30.5 (serveur DHCP)
Destination : 255.255.255.255 (broadcast)
Message Type : DHCP Offer
Your IP : 192.168.10.10 (IP proposée)
Server Identifier : 192.168.30.5
```

**Paquet 3 : DHCP Request**
```
Source : 0.0.0.0
Destination : 255.255.255.255
Message Type : DHCP Request
Requested IP : 192.168.10.10
```

**Paquet 4 : DHCP ACK**
```
Source : 192.168.30.5
Destination : 255.255.255.255
Message Type : DHCP ACK
Your IP : 192.168.10.10
Lease Time : 8 days
```

---

### **Validation capture**

**Vérifier :**
- ✅ 4 paquets présents (Discover, Offer, Request, ACK)
- ✅ IP proposée = 192.168.10.10 (dans pool DHCP)
- ✅ Server Identifier = 192.168.30.5 (SRV-DC01)
- ✅ Options 003 (Gateway) et 006 (DNS) visibles

**Follow UDP Stream (optionnel) :**
```
Clic droit Offer → Follow → UDP Stream
Voir : Options DHCP complètes
```

**Sauvegarder :**
```
File → Save As → dhcp-vlan10.pcap
```

---

## 2️⃣ CAPTURE DNS (Query/Response)

### **Préparation**

**Filtre capture :**
```
port 53
```
(Port DNS)

---

### **Procédure**

**1. Wireshark** (interface client)

**2. Démarrer capture**

**3. Requête DNS**
```cmd
nslookup srv-dc01.techcorp.local
```

**4. Arrêter capture**

---

### **Analyse attendue**

**Filtre display :** `dns`

**2 paquets (Query + Response) :**

**Paquet 1 : DNS Query (Standard query)**
```
Source : 192.168.10.10 (client)
Destination : 192.168.30.5 (serveur DNS)
Protocol : DNS
Questions : 1
  Name : srv-dc01.techcorp.local
  Type : A (IPv4 address)
  Class : IN (Internet)
```

**Paquet 2 : DNS Response (Standard query response)**
```
Source : 192.168.30.5 (serveur DNS)
Destination : 192.168.10.10 (client)
Answers : 1
  srv-dc01.techcorp.local : type A, class IN
  Addr : 192.168.30.5
  TTL : 3600 (1 heure)
```

---

### **Validation capture**

**Vérifier :**
- ✅ Query : Question = srv-dc01.techcorp.local
- ✅ Response : Answer = 192.168.30.5
- ✅ Temps réponse < 100ms
- ✅ No error (Response code : No error)

**Détails réponse (dérouler arbre) :**
```
Domain Name System (response)
 └─ Answers
    └─ srv-dc01.techcorp.local: type A, class IN, addr 192.168.30.5
       ├─ Name: srv-dc01.techcorp.local
       ├─ Type: A (Host Address)
       ├─ Class: IN
       ├─ Time to live: 3600
       └─ Addr: 192.168.30.5
```

**Sauvegarder :** `dns-query.pcap`

---

## 3️⃣ CAPTURE PING INTER-VLAN

### **Préparation**

**Objectif :** Prouver routage inter-VLAN fonctionne

**Filtre capture :**
```
icmp
```

---

### **Procédure**

**1. Wireshark** (PC VLAN 10)

**2. Démarrer capture**

**3. Ping PC VLAN 20**
```cmd
ping 192.168.20.10 -n 4
```

**4. Arrêter capture**

---

### **Analyse attendue**

**Filtre display :** `icmp`

**8 paquets (4 Request + 4 Reply) :**

**Paquets impairs : Echo Request (Type 8)**
```
Source : 192.168.10.10 (VLAN10)
Destination : 192.168.20.10 (VLAN20)
Type : 8 (Echo Request)
Sequence : 1, 2, 3, 4
```

**Paquets pairs : Echo Reply (Type 0)**
```
Source : 192.168.20.10 (VLAN20)
Destination : 192.168.10.10 (VLAN10)
Type : 0 (Echo Reply)
Sequence : 1, 2, 3, 4
```

---

### **Validation routage**

**Observer ADRESSES MAC (couche 2) :**

**Request (VLAN10 → VLAN20) :**
```
Ethernet II
 ├─ Source MAC : [MAC PC VLAN10]
 ├─ Dest MAC : [MAC Gateway VLAN10] ← IMPORTANT
```

**⚠️ MAC destination = Gateway (pas PC VLAN20)**
→ **PREUVE** : Paquet passe par routeur

**TTL Analysis :**
- TTL Request (vu côté VLAN10) : 128
- TTL Reply (vu côté VLAN10) : **127** (TTL-1)
→ **PREUVE** : 1 saut routeur

**Sauvegarder :** `ping-inter-vlan.pcap`

---

## 4️⃣ CAPTURE BONUS : TCP Handshake (AD)

### **Préparation**

**Objectif :** Voir connexion TCP à Active Directory

**Filtre capture :**
```
tcp.port == 389
```
(Port LDAP AD)

---

### **Procédure**

**1. Wireshark**

**2. Démarrer capture**

**3. Connexion AD**
```
Sur client, ouvrir :
\\srv-dc01\NETLOGON
(Déclenche authentification LDAP)
```

**4. Arrêter capture**

---

### **Analyse TCP Handshake**

**Filtre :** `tcp.flags.syn == 1`

**3 premiers paquets (SYN → SYN-ACK → ACK) :**

**Paquet 1 : SYN**
```
Source : 192.168.10.10:[port élevé]
Destination : 192.168.30.5:389 (LDAP)
Flags : SYN
Seq : 0
```

**Paquet 2 : SYN-ACK**
```
Source : 192.168.30.5:389
Destination : 192.168.10.10:[port]
Flags : SYN, ACK
Seq : 0
Ack : 1
```

**Paquet 3 : ACK**
```
Source : 192.168.10.10
Destination : 192.168.30.5:389
Flags : ACK
Ack : 1
```

**✅ Connexion TCP établie**

**Sauvegarder :** `tcp-ad-handshake.pcap`

---

## 5️⃣ ENCAPSULATION OSI (Screenshot)

### **Objectif**

Montrer **VISUELLEMENT** encapsulation OSI (lien S3)

---

### **Procédure**

**1. Ouvrir capture ping-inter-vlan.pcap**

**2. Sélectionner 1 paquet Echo Request**

**3. Dérouler arbre détails (milieu Wireshark)**

**4. Observer couches :**

```
Frame 1: 74 bytes on wire
 └─ Ethernet II, Src: [MAC], Dst: [MAC]       ← Couche 2
    └─ Internet Protocol Version 4             ← Couche 3
       └─ Internet Control Message Protocol    ← Couche 3
          └─ Data (32 bytes)
```

**5. Screenshot**

---

### **Annotations screenshot**

**Ajouter texte :**
```
C2 Liaison : Ethernet II
C3 Réseau : IP + ICMP
```

**Légende :**
> "Encapsulation OSI visible (S3) :
> C2 = Adresses MAC
> C3 = Adresses IP
> Données = Payload ICMP"

---

## ✅ CHECKLIST LIVRABLES WIRESHARK

**Captures .pcap :**
- [ ] dhcp-vlan10.pcap (DORA complet)
- [ ] dns-query.pcap (Query + Response)
- [ ] ping-inter-vlan.pcap (ICMP Request/Reply)
- [ ] (Bonus) tcp-ad-handshake.pcap

**Screenshots :**
- [ ] Encapsulation OSI (arbre Wireshark)
- [ ] (Optionnel) DHCP Options visible
- [ ] (Optionnel) DNS Answer détails

**Documentation :**
- [ ] Tableau analyse (voir ci-dessous)

---

## 📊 TABLEAU ANALYSE CAPTURES (Livrable)

**À compléter pour chaque capture :**

| **Capture** | **Nb paquets** | **Protocoles** | **Validation** | **Anomalie** |
|------------|---------------|---------------|---------------|-------------|
| dhcp-vlan10 | 4 | DHCP | ✅ DORA complet | Aucune |
| dns-query | 2 | DNS | ✅ Résolution OK | Aucune |
| ping-inter | 8 | ICMP | ✅ Routage OK | Aucune |
| tcp-ad | 50+ | TCP, LDAP | ✅ Handshake OK | Aucune |

---

## 💡 ASTUCES WIRESHARK

### **Coloration paquets (lisibilité)**

**View → Coloring Rules**

**Règles utiles :**
- DHCP : Vert clair
- DNS : Bleu clair
- ICMP : Rose
- Erreurs : Rouge

---

### **Filtres display avancés**

**DHCP complet :**
```
dhcp
```

**DNS succès uniquement :**
```
dns.flags.rcode == 0
```

**Ping spécifique :**
```
icmp && ip.addr == 192.168.20.10
```

**TCP Handshake uniquement :**
```
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

---

### **Exporter objets (bonus)**

**File → Export Objects → HTTP**

Utile si capture HTTP (non applicable ici)

---

## ⚠️ ERREURS À ÉVITER

**❌ Capture trop longue**
- Capturer juste ce qui est nécessaire (5-10 secondes)
- Sinon fichier .pcap énorme + difficile analyser

**❌ Mauvais filtre**
- Utiliser filtres capture (pas display) pour performances
- Exemple : `port 67 or port 68` (DHCP)

**❌ Interface incorrecte**
- Capturer sur bonne interface (Ethernet ou WiFi)
- Pas "Loopback" ou interfaces virtuelles

**❌ Pas de trigger**
- Lancer capture AVANT déclencher action (ipconfig /renew, ping...)

---

**Document - Guide Wireshark Validation - Version 1.0 - Février 2026**
