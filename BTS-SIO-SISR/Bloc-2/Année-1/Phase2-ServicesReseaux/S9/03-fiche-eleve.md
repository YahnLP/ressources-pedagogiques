# Pack de Formation - Semaine 9 (S9) - BLOC 2
## "Service DNS, Bind9 et Spanning Tree Protocol"

---

## 📚 FICHE DE COURS ÉLÈVE
### "Service DNS, Bind9 et Spanning Tree Protocol"

*Version 1.0 – BTS SIO SISR – Semestre 1 – Semaine 9*

---

### I. Le Service DNS

#### A. Pourquoi le DNS ?

Les machines communiquent par **adresses IP** (192.168.10.50). Les humains retiennent des **noms** (www.techpro.local, google.fr).

**Le DNS** (Domain Name System) fait le lien : il traduit les noms de domaine en adresses IP, et inversement.

**Sans DNS :** Vous devriez mémoriser l'IP de chaque site web. `http://142.250.185.78` à la place de `http://www.google.fr`.

**Avec DNS :** Vous tapez un nom, le système trouve l'IP pour vous, de façon transparente.

---

#### B. Vocabulaire Essentiel

| **Terme** | **Définition** | **Exemple** |
|-----------|----------------|-------------|
| **Domaine** | Espace de noms hiérarchique | `techpro.local`, `google.fr` |
| **FQDN** | Fully Qualified Domain Name – nom complet avec le point final | `www.techpro.local.` |
| **Zone** | Portion de l'espace de noms gérée par un serveur DNS | Zone `techpro.local` gérée par `ns1.techpro.local` |
| **Zone directe** | Traduit noms → adresses IP | `www` → `192.168.10.50` |
| **Zone inverse** | Traduit adresses IP → noms | `192.168.10.50` → `www.techpro.local.` |
| **Résolveur** | Client DNS qui interroge les serveurs | Pile réseau du PC, box Internet |
| **Serveur autoritaire** | Possède les fichiers de zone et fait référence | Le serveur Bind9 qu'on configure |
| **Cache DNS** | Mémorisation temporaire des réponses (durée = TTL) | Cache de la box, du PC |
| **TTL** | Time To Live – durée de validité d'un enregistrement en cache | `3600` = 1 heure |
| **Forwarder** | Serveur DNS vers lequel on renvoie les requêtes non résolues localement | `8.8.8.8` (Google DNS) |

---

#### C. Les Types d'Enregistrements DNS

Chaque ligne dans un fichier de zone est un **enregistrement DNS (Resource Record)**.

| **Type** | **Nom** | **Rôle** | **Exemple** |
|----------|---------|----------|-------------|
| **A** | Address | Nom → IPv4 | `www IN A 192.168.10.50` |
| **AAAA** | Address IPv6 | Nom → IPv6 | `www IN AAAA 2001:db8::1` |
| **PTR** | Pointer | IPv4 → Nom (zone inverse) | `50 IN PTR www.techpro.local.` |
| **CNAME** | Canonical Name | Alias pointant vers un autre nom | `web IN CNAME www` |
| **NS** | Name Server | Serveur de noms autoritaire pour la zone | `@ IN NS ns1.techpro.local.` |
| **MX** | Mail Exchanger | Serveur de messagerie | `@ IN MX 10 mail.techpro.local.` |
| **SOA** | Start of Authority | Informations d'autorité de la zone | (voir ci-dessous) |
| **TXT** | Text | Enregistrement texte libre (SPF, DKIM...) | `@ IN TXT "v=spf1 mx -all"` |

---

#### D. Le Processus de Résolution DNS

Il existe deux types de résolution :

##### 🔹 Résolution Récursive (vue du client)

Le client pose **une seule question** au résolveur et attend **une seule réponse complète**. Le résolveur fait tout le travail.

```
Client          Résolveur            Serveur Racine     Serveur Autoritaire
  │                  │                      │                    │
  │──"www.google.fr?"│                      │                    │
  │                  │──"Qui gère .fr ?" ──>│                    │
  │                  │<─"ns1.nic.fr"────────│                    │
  │                  │─────"Qui gère google.fr ?" ─────────────>│
  │                  │<────"ns1.google.com" ───────────────────│
  │                  │─────"IP de www.google.fr ?" ───────────>│
  │                  │<────"142.250.185.78" ────────────────────│
  │<─"142.250.185.78"│                      │                    │
```

##### 🔹 Résolution Itérative (vue du résolveur)

Le serveur renvoie la **meilleure réponse** qu'il peut donner (pas une réponse complète). Le résolveur pose ensuite la question au serveur suivant. C'est la mécanique interne que le résolveur utilise.

---

#### E. Zones Directe et Inverse

##### 🔹 Zone Directe (forward zone)

Traduit des **noms → adresses IP** via des enregistrements **A**.

**Fichier de zone directe `db.techpro.local` (exemple) :**
```
$TTL 3600                        ; TTL par défaut : 1 heure
@ IN SOA ns1.techpro.local. admin.techpro.local. (
                2024112001       ; Serial : YYYYMMDDNN
                3600             ; Refresh : 1h
                900              ; Retry : 15min
                604800           ; Expire : 1 semaine
                3600 )           ; Negative cache TTL : 1h

; Serveur(s) de noms
@ IN NS ns1.techpro.local.

; Enregistrements A (nom → IP)
ns1      IN A 192.168.10.1       ; Serveur DNS lui-même
www      IN A 192.168.10.50      ; Serveur web
mail     IN A 192.168.10.51      ; Serveur mail
srv-nas  IN A 192.168.10.10      ; NAS

; Alias CNAME
web      IN CNAME www            ; "web" pointe vers "www"
intranet IN CNAME www
```

**Lecture :**
- `@` = origine de la zone (= `techpro.local.`)
- `IN` = classe Internet (toujours IN)
- Un nom sans point final est **relatif** à la zone (`www` = `www.techpro.local.`)
- Un nom **avec point final** est **absolu** (FQDN) : `ns1.techpro.local.`

---

##### 🔹 Zone Inverse (reverse zone)

Traduit des **adresses IP → noms** via des enregistrements **PTR**.

Le nom de la zone inverse pour `192.168.10.0/24` est : `10.168.192.in-addr.arpa`
*(les octets du réseau sont inversés, + `.in-addr.arpa`)*

**Fichier de zone inverse `db.192.168.10.rev` (exemple) :**
```
$TTL 3600
@ IN SOA ns1.techpro.local. admin.techpro.local. (
                2024112001
                3600
                900
                604800
                3600 )

@ IN NS ns1.techpro.local.

; Enregistrements PTR (dernier octet de l'IP → nom complet)
1  IN PTR ns1.techpro.local.
10 IN PTR srv-nas.techpro.local.
50 IN PTR www.techpro.local.
51 IN PTR mail.techpro.local.
```

**Lecture :**
- `1 IN PTR ns1.techpro.local.` → l'IP `192.168.10.1` (zone `10.168.192.in-addr.arpa`) correspond à `ns1.techpro.local.`
- On n'écrit que le **dernier octet** (le reste est dans le nom de la zone)
- Le nom cible d'un PTR doit **toujours** avoir un point final

---

#### F. L'Enregistrement SOA – Start of Authority

L'enregistrement SOA est le premier de chaque zone. Il contient les métadonnées de la zone.

```
@ IN SOA ns1.techpro.local. admin.techpro.local. (
          2024112001   ; Serial
          3600         ; Refresh
          900          ; Retry
          604800       ; Expire
          3600 )       ; Negative TTL
```

| **Champ** | **Rôle** |
|-----------|----------|
| `ns1.techpro.local.` | Serveur DNS primaire de la zone |
| `admin.techpro.local.` | Email de l'administrateur (le `.` remplace le `@`) |
| **Serial** | Numéro de version (convention : AAAAMMJJNN). Doit être incrémenté à chaque modif pour que les secondaires rechargent la zone |
| **Refresh** | Délai entre deux vérifications du secondaire (en secondes) |
| **Retry** | Délai avant nouvelle tentative si le secondaire ne peut pas contacter le primaire |
| **Expire** | Durée après laquelle le secondaire considère sa copie comme obsolète |
| **Negative TTL** | Durée de mise en cache d'une réponse NXDOMAIN (nom inexistant) |

---

### II. Spanning Tree Protocol (STP)

#### A. Le Problème des Boucles Réseau

En commuté (switches), on peut être tenté de relier plusieurs switches par plusieurs câbles pour la **redondance** (si un lien tombe, l'autre prend le relais). Mais cela crée des **boucles physiques**.

**Problème 1 : Tempête de broadcast (Broadcast Storm)**

```
[SW1]────────────────[SW2]
  │                    │
  └──────[SW3]─────────┘

PC-A envoie un broadcast :
1. SW1 reçoit → Flood vers SW2 et SW3
2. SW2 reçoit de SW1 → Flood vers SW3 (et SW1 !)
3. SW3 reçoit de SW1 et SW2 → Flood vers SW1 et SW2...
→ Tempête ! Le broadcast tourne indéfiniment, saturant le réseau à 100%
```

**Problème 2 : Instabilité de la table MAC**

Un switch reçoit la même trame de plusieurs ports → la MAC Source change de port → la table MAC est mise à jour en boucle → tous les paquets sont floodés.

**Conséquence :** Sans protection, une boucle réseau rend le réseau totalement inutilisable en quelques secondes.

---

#### B. La Solution : STP (802.1d)

**STP** (Spanning Tree Protocol) est un protocole de couche 2 qui :
1. **Détecte** automatiquement les boucles
2. **Bloque** logiquement certains ports pour casser la boucle
3. **Réactive** les ports bloqués si un lien principal tombe (redondance)

**Principe :** STP construit un **arbre recouvrant** (spanning tree) — une topologie sans boucle — en désactivant logiquement les liens redondants.

```
Avant STP (boucle) :           Après STP (arbre sans boucle) :
[SW1]───[SW2]                  [SW1]───[SW2]
  │       │             →        │
  └──[SW3]┘                    [SW3]
                         (lien SW3-SW2 bloqué logiquement)
```

---

#### C. Fonctionnement de STP : Les 4 Étapes

##### Étape 1 : Élection du Root Bridge (Pont Racine)

Tous les switches échangent des messages **BPDU** (Bridge Protocol Data Unit) contenant leur **Bridge ID**.

**Bridge ID = Priorité (16 bits) + Adresse MAC (48 bits)**

- **Priorité par défaut :** 32768 (sur tous les switches Cisco 2960)
- **Le switch avec le Bridge ID le plus petit devient Root Bridge**
- En cas d'égalité de priorité → le switch avec la **MAC la plus faible** gagne

**Exemple :**

| **Switch** | **Priorité** | **MAC** | **Bridge ID** | **Résultat** |
|------------|-------------|---------|---------------|--------------|
| SW1 | 32768 | 00:0A:00:00:00:01 | 32768 + 00:0A... | |
| SW2 | 32768 | 00:0A:00:00:00:02 | 32768 + 00:0A... | |
| SW3 | **4096** | 00:0A:00:00:00:03 | 4096 + 00:0A... | ✅ **ROOT BRIDGE** (priorité plus basse) |

⚠️ **Mémo :** "Priorité la **plus basse** = Root Bridge" (comme à une enchère : on veut la mise la plus basse)

##### Étape 2 : Élection des Root Ports

Sur chaque switch **non-root**, on élit le port offrant le **chemin le moins coûteux** vers le Root Bridge : le **Root Port (RP)**.

**Coût de port STP (selon la vitesse du lien) :**

| **Vitesse** | **Coût STP** |
|-------------|-------------|
| 10 Mb/s | 100 |
| 100 Mb/s (Fast Ethernet) | 19 |
| 1 Gb/s | 4 |
| 10 Gb/s | 2 |

*Principe : plus le lien est rapide, plus le coût est faible = chemin préféré*

##### Étape 3 : Élection des Designated Ports

Sur chaque **segment réseau** (chaque lien entre deux switches), un seul port est élu **Designated Port (DP)** : le port qui transmet les trames sur ce segment. C'est toujours le port du côté ayant le meilleur chemin vers le Root Bridge.

##### Étape 4 : Blocage des Ports Restants

Tout port qui n'est ni Root Port ni Designated Port devient **Alternate Port** et est placé en état **Blocking** : il ne transmet plus de trames normales, mais surveille les BPDU pour réagir en cas de panne.

---

#### D. États des Ports STP

| **État** | **Durée** | **Reçoit BPDU ?** | **Envoie BPDU ?** | **Transmet trames ?** | **Apprend MAC ?** |
|----------|-----------|-------------------|-------------------|----------------------|-------------------|
| **Blocking** | Permanent (ports redondants) | ✅ | ❌ | ❌ | ❌ |
| **Listening** | 15 secondes (Forward Delay) | ✅ | ✅ | ❌ | ❌ |
| **Learning** | 15 secondes (Forward Delay) | ✅ | ✅ | ❌ | ✅ |
| **Forwarding** | Permanent (ports actifs) | ✅ | ✅ | ✅ | ✅ |
| **Disabled** | Si admin ou erreur | ❌ | ❌ | ❌ | ❌ |

**Temps de convergence STP classique (802.1d) :**
- Détection de panne : ~20 secondes (Max Age timer)
- Listening + Learning : 2 × 15 secondes = 30 secondes
- **Total : ~50 secondes** avant qu'un lien de secours soit actif

**Remarque :** Rapid STP (802.1w / Rapid PVST+) réduit ce délai à **quelques secondes** — à voir en Année 2.

---

#### E. Observer STP avec Cisco IOS

```cisco
! Afficher l'état STP complet (VLAN 1 par défaut)
Switch# show spanning-tree

! Exemple de sortie commentée :
VLAN0001
  Spanning tree enabled protocol ieee
  Root ID    Priority    32769                  ← Priorité + ID VLAN
             Address     0001.4300.0001         ← MAC du Root Bridge
             This bridge is the root            ← Ce switch EST le root bridge
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     0001.4300.0001
             ...

Interface        Role  Sts  Cost   Prio.Nbr Type
Fa0/1           Desg  FWD  19     128.1    P2p  ← Designated, Forwarding
Fa0/2           Desg  FWD  19     128.2    P2p
Fa0/3           Desg  FWD  19     128.3    P2p
```

**Lecture des colonnes :**
- **Role :** Root (RP), Desg (Designated), Altn (Alternate/Blocked)
- **Sts :** FWD (Forwarding), BLK (Blocking), LIS (Listening), LRN (Learning)
- **Cost :** Coût cumulatif vers le Root Bridge
- **Prio.Nbr :** Priorité du port (valeur par défaut 128)

---

### III. TP Linux : Serveur DNS Bind9

#### A. Installation de Bind9

```bash
# Mettre à jour et installer
sudo apt update
sudo apt install bind9 bind9utils bind9-doc -y

# Vérifier que le service tourne
sudo systemctl status bind9
# Attendu : Active: active (running)

# Vérifier qu'il écoute sur le port 53
ss -tlnup | grep 53
```

---

#### B. Configuration des Options Globales

```bash
sudo nano /etc/bind/named.conf.options
```

**Remplacer le contenu par :**

```
options {
    directory "/var/cache/bind";

    // Forwarders : à qui déléguer les requêtes qu'on ne sait pas résoudre
    forwarders {
        8.8.8.8;      // DNS Google primaire
        8.8.4.4;      // DNS Google secondaire
    };

    // Autoriser la récursion pour notre réseau local uniquement
    allow-recursion { 127.0.0.1; 192.168.10.0/24; };

    // Accepter les requêtes de notre réseau
    allow-query { any; };

    dnssec-validation auto;
    listen-on { any; };
};
```

---

#### C. Déclarer les Zones Locales

```bash
sudo nano /etc/bind/named.conf.local
```

**Ajouter à la fin du fichier :**

```
// Zone directe : techpro.local (nom → IP)
zone "techpro.local" {
    type master;
    file "/etc/bind/db.techpro.local";
};

// Zone inverse : 192.168.10.0/24 (IP → nom)
zone "10.168.192.in-addr.arpa" {
    type master;
    file "/etc/bind/db.192.168.10.rev";
};
```

---

#### D. Créer le Fichier de Zone Directe

```bash
sudo nano /etc/bind/db.techpro.local
```

**Contenu à saisir :**

```
;
; Fichier de zone directe : techpro.local
; Créé le 2024-11-20 - BTS SIO SISR
;
$TTL 3600        ; TTL par défaut : 1 heure

; === SOA - Début de zone ===
@   IN  SOA ns1.techpro.local. admin.techpro.local. (
                2024112001  ; Serial YYYYMMDDNN - INCRÉMENTER à chaque modif
                3600        ; Refresh : toutes les heures
                900         ; Retry : 15 min en cas d'échec
                604800      ; Expire : 7 jours
                3600 )      ; Negative TTL : 1 heure

; === NS - Serveur(s) de noms ===
@       IN  NS  ns1.techpro.local.

; === A - Enregistrements nom vers IP ===
ns1         IN  A   192.168.10.1    ; Ce serveur DNS
www         IN  A   192.168.10.50   ; Serveur web
mail        IN  A   192.168.10.51   ; Serveur mail
srv-fichier IN  A   192.168.10.20   ; Serveur de fichiers
srv-nas     IN  A   192.168.10.10   ; NAS

; === CNAME - Alias ===
web         IN  CNAME   www         ; "web.techpro.local" = alias de "www.techpro.local"
intranet    IN  CNAME   www
ftp         IN  CNAME   srv-fichier
```

---

#### E. Créer le Fichier de Zone Inverse

```bash
sudo nano /etc/bind/db.192.168.10.rev
```

**Contenu à saisir :**

```
;
; Fichier de zone inverse : 192.168.10.0/24
; Zone : 10.168.192.in-addr.arpa
;
$TTL 3600

@   IN  SOA ns1.techpro.local. admin.techpro.local. (
                2024112001
                3600
                900
                604800
                3600 )

@   IN  NS  ns1.techpro.local.

; === PTR - Enregistrements IP vers nom ===
; Format : dernier octet IN PTR nom-complet.
1   IN  PTR ns1.techpro.local.
10  IN  PTR srv-nas.techpro.local.
20  IN  PTR srv-fichier.techpro.local.
50  IN  PTR www.techpro.local.
51  IN  PTR mail.techpro.local.
```

---

#### F. Appliquer les Permissions et Vérifier la Syntaxe

```bash
# Appliquer les bonnes permissions (bind doit pouvoir lire les fichiers)
sudo chown bind:bind /etc/bind/db.techpro.local
sudo chown bind:bind /etc/bind/db.192.168.10.rev

# Vérifier la syntaxe du fichier de configuration principal
sudo named-checkconf
# Si aucune sortie = OK (les erreurs s'affichent, le silence = succès)

# Vérifier la syntaxe des fichiers de zone
sudo named-checkzone techpro.local /etc/bind/db.techpro.local
# Attendu : zone techpro.local/IN: loaded serial 2024112001
#           OK

sudo named-checkzone 10.168.192.in-addr.arpa /etc/bind/db.192.168.10.rev
# Attendu : zone 10.168.192.in-addr.arpa/IN: loaded serial 2024112001
#           OK
```

⚠️ **NE PAS redémarrer Bind9 si `named-checkzone` affiche des erreurs — corriger d'abord !**

---

#### G. Démarrer et Recharger Bind9

```bash
# Redémarrer le service
sudo systemctl restart bind9

# Vérifier l'état
sudo systemctl status bind9
# Attendu : Active: active (running)

# Si le service était déjà en route et qu'on veut recharger les zones
# sans couper le service (recommandé en production)
sudo rndc reload
```

**Activer au démarrage :**
```bash
sudo systemctl enable bind9
```

---

#### H. Configurer le Client DNS

Pour que la VM elle-même utilise son propre serveur DNS :

```bash
# Méthode simple : modifier /etc/resolv.conf
# ATTENTION : ce fichier est souvent régénéré automatiquement
sudo nano /etc/resolv.conf
```

**Contenu :**
```
nameserver 127.0.0.1       # Utiliser le serveur local
nameserver 8.8.8.8         # Serveur de secours (Internet)
search techpro.local       # Domaine de recherche par défaut
```

---

#### I. Tester le Serveur DNS

```bash
# === TEST ZONE DIRECTE (A records) ===

# dig : outil complet
dig @127.0.0.1 www.techpro.local A

# Sortie attendue :
# ;; ANSWER SECTION:
# www.techpro.local.  3600  IN  A  192.168.10.50

dig @127.0.0.1 mail.techpro.local A
dig @127.0.0.1 web.techpro.local A        # Doit retourner l'IP de www (CNAME)
dig @127.0.0.1 srv-nas.techpro.local A

# === TEST ZONE INVERSE (PTR records) ===

dig @127.0.0.1 -x 192.168.10.50           # Résolution inverse de .50
dig @127.0.0.1 -x 192.168.10.1            # Résolution inverse du serveur NS

# === TEST AVEC nslookup ===

nslookup www.techpro.local 127.0.0.1
nslookup 192.168.10.50 127.0.0.1          # Résolution inverse

# === TEST AVEC host ===

host www.techpro.local 127.0.0.1
host 192.168.10.50 127.0.0.1

# === TEST ALIAS CNAME ===

dig @127.0.0.1 web.techpro.local          # Doit montrer CNAME vers www
dig @127.0.0.1 intranet.techpro.local

# === TEST RÉSOLUTION INTERNET (Forwarder) ===

dig @127.0.0.1 www.google.fr              # Notre serveur doit forwarder vers 8.8.8.8
```

**Analyser une réponse `dig` :**

```
; <<>> DiG 9.18.x <<>> @127.0.0.1 www.techpro.local A
;; QUESTION SECTION:
;www.techpro.local.         IN  A

;; ANSWER SECTION:
www.techpro.local.  3600    IN  A   192.168.10.50
   ↑ nom FQDN        ↑TTL       ↑type ↑IP réponse

;; AUTHORITY SECTION:
techpro.local.      3600    IN  NS  ns1.techpro.local.

;; Query time: 1 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)     ← Serveur interrogé
;; WHEN: ...
;; MSG SIZE rcvd: 75

Flags importants :
qr  = Query Response (c'est une réponse)
aa  = Authoritative Answer (le serveur fait autorité) ✅
rd  = Recursion Desired (le client a demandé la récursion)
ra  = Recursion Available (le serveur supporte la récursion)
```

---

#### J. Consulter les Logs Bind9

```bash
# Logs en temps réel (très utile pour déboguer)
sudo journalctl -u bind9 -f

# Ou chercher dans syslog
sudo tail -f /var/log/syslog | grep named
```

---

### IV. TP Cisco – Observer le STP sur 3 Switches

#### Topologie

```
        [SW1]
       /     \
  Fa0/1       Fa0/2
     /           \
[SW2]─────────[SW3]
    Fa0/1   Fa0/1
```

Trois switches reliés en **triangle** = 3 liens, donc **1 boucle** → STP doit bloquer 1 port.

---

#### Étape 1 : Créer la Topologie dans Packet Tracer (5 min)

1. Placer **3 switches Cisco 2960** (SW1, SW2, SW3)
2. Câbler :
   - SW1 Fa0/1 ↔ SW2 Fa0/1 (câble droit)
   - SW1 Fa0/2 ↔ SW3 Fa0/1 (câble droit)
   - SW2 Fa0/2 ↔ SW3 Fa0/2 (câble droit)
3. Attendre la convergence STP (~30-50 secondes)
4. Observer les voyants : certains doivent être **orange** (Blocking) d'autres **vert** (Forwarding)

---

#### Étape 2 : Identifier le Root Bridge (10 min)

```cisco
! Sur CHAQUE switch, taper :
SW1# show spanning-tree

! Chercher la ligne :
"This bridge is the root"   → ce switch EST le root bridge
OU
"Root ID ... Address xx:xx:xx..."  → adresse du root bridge (différente du switch)
```

📝 **Tableau à remplir :**

| **Switch** | **Bridge ID (MAC)** | **Priorité** | **Root Bridge ?** |
|------------|--------------------|--------------|--------------------|
| SW1 | | 32769 | |
| SW2 | | 32769 | |
| SW3 | | 32769 | |

**Question :** Comment Packet Tracer a-t-il désigné le root bridge ? (priorité égale → MAC la plus basse)

---

#### Étape 3 : Observer les Rôles et États des Ports (10 min)

Sur **chaque switch**, taper `show spanning-tree` et relever :

```cisco
SW2# show spanning-tree

! Chercher la section "Interface" :
Interface        Role  Sts  Cost   Prio.Nbr Type
Fa0/1           Root  FWD  19     128.1    P2p
Fa0/2           Altn  BLK  19     128.2    P2p
```

📝 **Tableau à remplir :**

| **Switch** | **Interface** | **Rôle (Root/Desg/Altn)** | **État (FWD/BLK)** |
|------------|---------------|--------------------------|---------------------|
| SW1 | Fa0/1 | | |
| SW1 | Fa0/2 | | |
| SW2 | Fa0/1 | | |
| SW2 | Fa0/2 | | |
| SW3 | Fa0/1 | | |
| SW3 | Fa0/2 | | |

**Questions :**
- Quel port est en état BLK (Blocking) ?
- Sur quel switch se trouve-t-il ?
- Pourquoi STP a-t-il choisi CE port à bloquer ?

---

#### Étape 4 : Tester la Connectivité (5 min)

Ajouter **1 PC** sur chaque switch :
- PC1 sur SW1 (Fa0/3), PC2 sur SW2 (Fa0/3), PC3 sur SW3 (Fa0/3)
- Configurer les IP : `192.168.1.11/24`, `192.168.1.12/24`, `192.168.1.13/24`

**Tests :**
```
PC1 → ping 192.168.1.12   ✅ Doit répondre (via le chemin STP actif)
PC1 → ping 192.168.1.13   ✅ Doit répondre
```

---

#### Étape 5 : Observer la Reconvergence (15 min)

**Simuler une panne :** Dans Packet Tracer, débrancher le câble entre SW1 et SW2 (clic sur le câble → supprimer).

**Observer :**
1. Les voyants changent (orange = STP en convergence)
2. Attendre ~30-50 secondes
3. Retaper `show spanning-tree` sur SW2 et SW3
4. Le port précédemment en BLK doit passer en FWD !

```cisco
SW2# show spanning-tree
! Le port Altn/BLK doit maintenant être Root/FWD
```

📝 **Questions :**
- Quel port était BLK avant la panne ?
- Quel état a-t-il pris après la panne ?
- Combien de secondes a pris la reconvergence (estimer en observant les voyants) ?

---

#### Étape 6 : Forcer le Root Bridge (10 min)

Modifier la priorité STP pour forcer **SW3** à devenir root bridge :

```cisco
SW3# configure terminal
SW3(config)# spanning-tree vlan 1 priority 4096
SW3(config)# end
```

Attendre la reconvergence, puis vérifier :
```cisco
SW3# show spanning-tree
! "This bridge is the root" doit apparaître sur SW3
```

📝 **Question :** Pourquoi utilise-t-on une valeur comme 4096 plutôt qu'une valeur quelconque ?
(Réponse : La priorité STP doit être un multiple de 4096)

---

### V. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|----------------|
| **DNS** | Domain Name System – traduit noms de domaine ↔ adresses IP |
| **Zone directe** | Fichier de zone résolvant noms → IP (enregistrements A) |
| **Zone inverse** | Fichier de zone résolvant IP → noms (enregistrements PTR) |
| **Enregistrement A** | Associe un nom à une adresse IPv4 |
| **Enregistrement PTR** | Associe une adresse IP à un nom (zone inverse) |
| **Enregistrement CNAME** | Alias pointant vers un autre nom canonique |
| **Enregistrement NS** | Déclare les serveurs de noms d'une zone |
| **SOA** | Start of Authority – métadonnées de la zone (serial, refresh, TTL…) |
| **FQDN** | Fully Qualified Domain Name – nom absolu terminé par un `.` |
| **TTL** | Time To Live – durée de validité en cache d'un enregistrement DNS |
| **Résolveur** | Client DNS qui interroge les serveurs |
| **Serveur autoritaire** | Serveur possédant les fichiers de zone officiels |
| **Forwarder** | Serveur externe auquel on délègue les requêtes non résolues localement |
| **Bind9** | Implémentation de référence du serveur DNS sous Linux |
| **named** | Démon Bind9 (Named = Name Daemon) |
| **named.conf** | Fichier de configuration principal de Bind9 |
| **named-checkzone** | Commande de vérification syntaxique d'un fichier de zone |
| **dig** | Outil de diagnostic DNS en ligne de commande |
| **STP** | Spanning Tree Protocol (802.1d) – évite les boucles réseau en couche 2 |
| **Root Bridge** | Switch élu centre de l'arbre STP (Bridge ID le plus faible) |
| **Bridge ID** | Identifiant STP = Priorité (16 bits) + Adresse MAC (48 bits) |
| **BPDU** | Bridge Protocol Data Unit – messages échangés par STP |
| **Root Port** | Port du switch non-root offrant le meilleur chemin vers le Root Bridge |
| **Designated Port** | Port en Forwarding sur chaque segment réseau |
| **Alternate Port** | Port bloqué (logiquement désactivé) par STP |
| **Blocking** | État STP d'un port : reçoit les BPDU mais ne transmet pas de trames |
| **Forwarding** | État STP d'un port actif : transmet les trames normalement |
| **Broadcast Storm** | Saturation réseau causée par une boucle et une trame broadcast en boucle infinie |

---

### VI. Exercices d'Entraînement

#### Exercice 1 : Fichier de Zone

Écrire les enregistrements DNS pour le réseau `cabinet-archi.local` (192.168.50.0/24) :

| **Machine** | **Nom** | **IP** |
|-------------|---------|--------|
| Serveur DNS | ns1.cabinet-archi.local | 192.168.50.1 |
| Serveur web | www.cabinet-archi.local | 192.168.50.100 |
| Serveur impression | print.cabinet-archi.local | 192.168.50.200 |
| Alias | web.cabinet-archi.local | → www |

1. Écrire le fichier de zone directe complet (avec SOA)
2. Écrire les 4 enregistrements PTR correspondants
3. Quel est le nom de la zone inverse pour `192.168.50.0/24` ?

---

#### Exercice 2 : Analyse STP

Trois switches reliés en triangle. Les Bridge IDs sont :

- SW-A : Priorité 32768, MAC `0010.0000.0001`
- SW-B : Priorité 32768, MAC `0010.0000.0002`
- SW-C : Priorité **4096**, MAC `0010.0000.0003`

1. Quel switch devient Root Bridge ? Pourquoi ?
2. Sur SW-A : quel est son Root Port (liaison vers SW-B ou vers SW-C) ?
3. Sur SW-B : quel port sera probablement en état Blocking ?
4. Si SW-C tombe en panne, que se passe-t-il ?

---

#### Exercice 3 : Diagnostic DNS

Une machine cliente (`192.168.10.30`) n'arrive pas à résoudre `www.techpro.local`. Proposer une procédure de diagnostic de 5 étapes, de la plus simple à la plus complexe.

---

### VII. Auto-évaluation : Suis-je Prêt ?

- [ ] Expliquer le rôle du DNS et les 4 étapes de la résolution récursive
- [ ] Distinguer zone directe (A) et zone inverse (PTR)
- [ ] Lire et interpréter un enregistrement A, PTR, CNAME, NS, SOA
- [ ] Installer Bind9 sous Debian et vérifier qu'il tourne
- [ ] Configurer `named.conf.options` (forwarders, allow-recursion)
- [ ] Créer un fichier de zone directe avec enregistrements A et CNAME
- [ ] Créer un fichier de zone inverse avec enregistrements PTR
- [ ] Vérifier la syntaxe avec `named-checkzone` avant de redémarrer
- [ ] Tester avec `dig` et `nslookup` les résolutions directe et inverse
- [ ] Expliquer pourquoi les boucles réseau sont dangereuses (broadcast storm)
- [ ] Décrire le processus d'élection du Root Bridge STP (Bridge ID le plus faible)
- [ ] Identifier les états des ports STP (Forwarding, Blocking, Listening, Learning)
- [ ] Lire `show spanning-tree` et identifier Root Port, Designated Port, Alternate Port


