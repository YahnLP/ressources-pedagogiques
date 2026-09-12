# 📖 FICHE COURS - S15 E31
## Wireshark - Capture & Analyse

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Capturer trafic réseau
- ✅ Filtrer paquets (display filters)
- ✅ Analyser protocoles (TCP, HTTP, DNS)
- ✅ Détecter données sensibles
- ✅ Comprendre chiffrement (HTTPS vs HTTP)

---

## 1️⃣ QU'EST-CE QUE WIRESHARK ?

### **Définition**

> **Wireshark** = Analyseur de protocoles réseau (packet sniffer)

**Fonction :** Capturer et analyser trafic réseau

**Créé par :** Gerald Combs (1998)  
**Licence :** Open source (gratuit)

**Lien OSI (S3) :** Wireshark capture **toutes les couches** (1-7)

---

## 2️⃣ INTERFACE WIRESHARK

### **3 Zones principales**

```
┌────────────────────────────────────┐
│ 1. LISTE PAQUETS                   │
│ (tous paquets capturés)            │
├────────────────────────────────────┤
│ 2. DÉTAILS PAQUET                  │
│ (arbre OSI : Eth → IP → TCP → HTTP)│
├────────────────────────────────────┤
│ 3. DONNÉES BRUTES                  │
│ (hexadécimal + ASCII)              │
└────────────────────────────────────┘
```

---

## 3️⃣ CAPTURER TRAFIC

### **Procédure**

**1. Choisir interface**
```
Capture → Options → Sélectionner WiFi ou Ethernet
```

**2. Démarrer capture**
```
Clic bouton bleu (aileron requin)
OU
Capture → Start
```

**3. Arrêter capture**
```
Clic bouton rouge (carré)
```

**4. Sauvegarder**
```
File → Save As → capture.pcap
```

---

### **⚠️ Promiscuous Mode**

**Activé par défaut :** Capture TOUS paquets (pas seulement vers/depuis votre PC)

**⚠️ ÉTHIQUE :** Capturer trafic tiers = **ILLÉGAL** sans autorisation

---

## 4️⃣ FILTRES DISPLAY

### **Syntaxe de base**

**Protocole :**
```
http
dns
tcp
icmp
arp
```

**Adresse IP :**
```
ip.addr == 192.168.1.10      (source OU destination)
ip.src == 192.168.1.10       (source uniquement)
ip.dst == 8.8.8.8            (destination uniquement)
```

**Port TCP/UDP :**
```
tcp.port == 80               (port 80 source OU dest)
tcp.dstport == 443           (destination port 443)
udp.port == 53               (DNS)
```

**TCP Flags :**
```
tcp.flags.syn == 1           (SYN)
tcp.flags.ack == 1           (ACK)
tcp.flags.reset == 1         (RST)
```

---

### **Opérateurs**

| **Opérateur** | **Signification** | **Exemple** |
|--------------|------------------|-------------|
| `&&` | ET logique | `http && ip.addr == 192.168.1.10` |
| `||` | OU logique | `tcp.port == 80 || tcp.port == 443` |
| `!` | NON logique | `!(arp || icmp)` |
| `==` | Égal | `ip.src == 192.168.1.1` |
| `!=` | Différent | `ip.dst != 8.8.8.8` |

---

### **Exemples Pratiques**

**Trafic HTTP vers Google :**
```
http && ip.dst == 142.250.185.78
```

**Requêtes DNS :**
```
dns.qry.name
```

**TCP SYN (début connexion) :**
```
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

**Exclure bruit (ARP, ICMP) :**
```
!(arp || icmp)
```

---

## 5️⃣ ANALYSER PROTOCOLES

### **TCP Handshake (3-way)**

**Établissement connexion TCP :**

```
Client → Serveur : SYN
Serveur → Client : SYN-ACK
Client → Serveur : ACK
```

**Dans Wireshark :**
1. Filtre : `tcp.flags.syn == 1`
2. Observer séquence 3 paquets
3. Vérifier ports (ex: client:49152 → serveur:80)

---

### **DNS Query (Requête)**

**Résolution nom → IP :**

```
Client → DNS : Query "google.com"
DNS → Client : Response "142.250.185.78"
```

**Dans Wireshark :**
1. Filtre : `dns`
2. Query (Standard query A google.com)
3. Response (A 142.250.185.78)

---

### **HTTP Request/Response**

**Communication web :**

```
Client → Serveur : GET /index.html HTTP/1.1
Serveur → Client : HTTP/1.1 200 OK + contenu
```

**Dans Wireshark :**
1. Filtre : `http`
2. Request : `GET /index.html`
3. Response : `200 OK` (ou 404 Not Found)

---

## 6️⃣ FOLLOW STREAM (Suivre Flux)

### **Principe**

> **Follow Stream** = Reconstituer conversation TCP complète

**Procédure :**
1. Clic droit paquet HTTP/TCP
2. `Follow → TCP Stream`
3. Fenêtre affiche conversation lisible

**Exemple HTTP :**
```
GET /login.php HTTP/1.1
Host: example.com

HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

---

## 7️⃣ VOIR ENCAPSULATION OSI

### **Arbre détails paquet**

**Exemple paquet HTTP :**

```
└─ Frame (Couche 1 Physique)
   └─ Ethernet II (Couche 2 Liaison)
      └─ Internet Protocol (Couche 3 Réseau)
         └─ Transmission Control Protocol (Couche 4 Transport)
            └─ Hypertext Transfer Protocol (Couche 7 Application)
```

**⭐ LIEN S3 :** C'est l'**encapsulation** vue en S3 !

**En-têtes visibles :**
- Ethernet : MAC source/dest
- IP : Adresses IP source/dest
- TCP : Ports source/dest, flags
- HTTP : GET, POST, User-Agent...

---

## 8️⃣ SÉCURITÉ - DANGER HTTP

### **HTTP vs HTTPS**

| **Critère** | **HTTP** | **HTTPS** |
|------------|---------|----------|
| **Chiffrement** | ❌ Aucun | ✅ TLS/SSL |
| **Port** | 80 | 443 |
| **MDP visible** | ✅ Oui (DANGER) | ❌ Non (chiffré) |
| **Wireshark** | Tout visible | Chiffré |

---

### **Démo Danger HTTP**

**Scénario :** Login site HTTP

**Capture Wireshark :**
```
POST /login.php HTTP/1.1

username=alice&password=Secret123
```

**⚠️ RÉSULTAT :** MDP **Secret123** visible en CLAIR !

**Sur WiFi ouvert (S14) :**
- Attaquant capture trafic
- Wireshark révèle TOUS MDP HTTP
- **CATASTROPHE**

---

### **Protection HTTPS**

**Même scénario HTTPS :**

**Capture Wireshark :**
```
TLSv1.2 Application Data (chiffré)
\x8f\x2a\x9c\x... (illisible)
```

**Résultat :** MDP **protégé** (chiffrement)

**⭐ RÈGLE SÉCURITÉ :**
> "JAMAIS saisir MDP sur site HTTP. TOUJOURS vérifier cadenas HTTPS !"

---

## 9️⃣ STATISTIQUES UTILES

### **Protocol Hierarchy**

```
Statistics → Protocol Hierarchy
```

**Affiche :** % trafic par protocole

**Exemple :**
- HTTP : 45%
- DNS : 5%
- TCP : 30%
- UDP : 10%

---

### **Conversations**

```
Statistics → Conversations → IPv4
```

**Affiche :** Top IP sources/destinations

**Utile :** Identifier qui parle à qui

---

## 🔟 CAPTURE vs DISPLAY FILTERS

| **Type** | **Quand** | **Exemple** |
|---------|----------|-------------|
| **Capture Filter** | AVANT capture (BPF) | `host 192.168.1.1` |
| **Display Filter** | APRÈS capture | `ip.addr == 192.168.1.1` |

**⚠️ A1 :** Focus sur **Display Filters** (plus simples)

---

## 📚 VOCABULAIRE

| **Terme** | **Définition** |
|-----------|----------------|
| **Packet sniffer** | Logiciel capture réseau |
| **Promiscuous mode** | Capture tous paquets |
| **Display filter** | Filtre après capture |
| **Follow Stream** | Reconstituer conversation TCP |
| **3-way handshake** | SYN → SYN-ACK → ACK |
| **.pcap** | Format fichier capture |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je capture trafic réseau
- [ ] J'écris filtres display (http, ip.addr...)
- [ ] J'analyse TCP handshake
- [ ] Je suis flux HTTP (Follow Stream)
- [ ] Je détecte MDP en clair
- [ ] Je comprends HTTPS vs HTTP

---

## 📌 POINTS-CLÉS

1. **Wireshark** = Rayon X du réseau
2. **Filtres** : `http`, `ip.addr == X`, `tcp.port == 80`
3. **TCP Handshake** : SYN → SYN-ACK → ACK
4. **Follow Stream** : Voir conversation complète
5. **HTTP** = DANGER (MDP clair)
6. **HTTPS** = Sécurisé (chiffré TLS)
7. **ÉTHIQUE** : Capturer son trafic OK, tiers = ILLÉGAL

---

**Document - Version 1.0 - Février 2026**
