# 🎲 ACTIVITÉ - S15 E31
## "Détective Réseau" : Enquête Wireshark

---

## 🎯 OBJECTIFS

- ✅ Analyser capture réseau (.pcap)
- ✅ Filtrer paquets pertinents
- ✅ Extraire informations cachées
- ✅ Reconstituer scénario réseau

---

## ⏱️ DURÉE : 45 min

---

## 🧩 MATÉRIEL

- Wireshark installé
- Capture fournie : `enquete.pcap`
- Fiche enquête (à compléter)

---

## 📋 CONTEXTE

**Scénario :** Incident sécurité MFR

**15h30** : Alerte IT  
**Suspicion** : Connexion non autorisée serveur  
**Mission** : Analyser capture réseau (15h25-15h35)

**Questions à résoudre :**
1. Quelle IP a accédé au serveur ?
2. Quel protocole utilisé ?
3. Quelles données échangées ?
4. MDP compromis ?

---

## 🎮 DÉROULEMENT

### **ÉTAPE 1 : Ouvrir Capture (5 min)**

**1. Lancer Wireshark**

**2. Ouvrir fichier**
```
File → Open → enquete.pcap
```

**3. Observer**
- Nombre paquets : ~500
- Protocoles : HTTP, DNS, TCP, ICMP
- Durée capture : 10 minutes

---

### **ÉTAPE 2 : Identifier Acteurs (10 min)**

**Mission :** Trouver IP client et serveur

**Outil Wireshark :**
```
Statistics → Conversations → IPv4
```

**Résultat attendu :**

| **IP A** | **IP B** | **Paquets** | **Rôle** |
|---------|---------|------------|---------|
| 192.168.1.50 | 192.168.1.10 | 245 | Client → Serveur |
| 192.168.1.50 | 8.8.8.8 | 12 | Client → DNS Google |

**Réponse Q1 :** Client = **192.168.1.50**

---

### **ÉTAPE 3 : Analyser Protocole (10 min)**

**Mission :** Quel protocole utilisé ?

**Filtre display :**
```
ip.addr == 192.168.1.50 && ip.addr == 192.168.1.10
```

**Observer colonnes :**
- Protocol : **HTTP**
- Info : GET /admin.php

**Réponse Q2 :** Protocole = **HTTP** (port 80)

---

### **ÉTAPE 4 : Suivre Flux HTTP (15 min)**

**Mission :** Quelles données échangées ?

**Procédure :**

1. **Filtrer HTTP**
```
http
```

2. **Trouver requête POST**
- Chercher : `POST /login.php`
- Clic droit paquet

3. **Follow TCP Stream**
```
Analyze → Follow → TCP Stream
```

**Contenu visible :**

```
POST /login.php HTTP/1.1
Host: 192.168.1.10
Content-Type: application/x-www-form-urlencoded

username=admin&password=P@ssw0rd123
```

**⚠️ ALERTE :** MDP EN CLAIR !

**Réponse Q3 :** Données = Login form (user + MDP)

**Réponse Q4 :** MDP compromis = **P@ssw0rd123**

---

### **ÉTAPE 5 : Reconstitution Complète (5 min)**

**Chronologie événements :**

```
15h25:12 - DNS Query : serveur.mfr.local → 192.168.1.10
15h25:15 - TCP Handshake : 192.168.1.50 → 192.168.1.10:80
15h25:16 - HTTP GET /index.php
15h25:18 - HTTP POST /login.php (username=admin, password=P@ssw0rd123)
15h25:19 - HTTP 200 OK (connexion réussie)
15h25:20 - HTTP GET /admin.php (accès panel admin)
```

**Conclusion :**
> "User 192.168.1.50 s'est connecté serveur avec login **admin** / **P@ssw0rd123** en HTTP (NON CHIFFRÉ). Toute la session est visible en clair."

---

## 📊 RAPPORT ENQUÊTE

**Fiche à compléter :**

```
┌─────────────────────────────────────┐
│   RAPPORT ANALYSE RÉSEAU            │
├─────────────────────────────────────┤
│ Fichier : enquete.pcap              │
│ Analyste : ____________________     │
│                                     │
│ RÉSULTATS :                         │
│                                     │
│ IP source : _______________         │
│ IP destination : _______________    │
│ Protocole : _______________         │
│ Port : _______________              │
│                                     │
│ DONNÉES COMPROMISES :               │
│ - Username : _______________        │
│ - Password : _______________        │
│                                     │
│ VULNÉRABILITÉ IDENTIFIÉE :          │
│ ☑ HTTP non chiffré (données clair) │
│ ☐ WEP WiFi                          │
│ ☐ Telnet                            │
│                                     │
│ RECOMMANDATION :                    │
│ - Migrer vers HTTPS (TLS)           │
│ - Bannir HTTP pour authentification│
└─────────────────────────────────────┘
```

---

## 🔍 FILTRES UTILES (Aide-mémoire)

**Trouver requêtes POST :**
```
http.request.method == "POST"
```

**Trouver réponses 200 OK :**
```
http.response.code == 200
```

**Filtrer IP spécifique :**
```
ip.addr == 192.168.1.50
```

**Exclure ARP/ICMP (bruit) :**
```
!(arp || icmp)
```

---

## ⚠️ LEÇONS SÉCURITÉ

**Ce que Wireshark a révélé :**

1. **HTTP = DANGER**
   - MDP visible en clair
   - Session entière lisible
   - **Solution** : HTTPS obligatoire

2. **WiFi + HTTP = CATASTROPHE**
   - Ondes captables (S14)
   - Trafic HTTP déchiffrable
   - **Solution** : WPA2 + HTTPS

3. **Wireshark = Arme double tranchant**
   - Diagnostic réseau (pro)
   - Espionnage (illégal)
   - **Éthique** : Usage responsable

---

## ✅ VALIDATION

- 100% ouvrent capture
- 80% identifient IP source/dest
- 70% trouvent MDP en clair
- 60% expliquent danger HTTP

---

## 🎓 ALLER PLUS LOIN

**Autres captures à analyser :**

**Capture 2 : DNS Poisoning**
- Détecter fausse réponse DNS

**Capture 3 : TCP SYN Flood**
- Voir attaque DDoS

**Capture 4 : HTTPS vs HTTP**
- Comparer chiffré vs clair

---

**Document - Version 1.0 - Février 2026**
