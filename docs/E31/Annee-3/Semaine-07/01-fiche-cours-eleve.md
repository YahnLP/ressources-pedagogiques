# 📖 FICHE COURS – S7 ANNÉE 3 – E31
## IPv6 Avancé : SLAAC, DHCPv6, OSPFv3 Multi-Area, RIPng, Coexistence en Production

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Configurer les 3 modes d'auto-configuration IPv6 (SLAAC, DHCPv6 stateless, stateful)
- ✅ Calculer une adresse EUI-64
- ✅ Configurer OSPFv3 multi-area avec ABR
- ✅ Configurer RIPng et choisir entre RIPng et OSPFv3 selon le contexte
- ✅ Déployer un réseau dual-stack IPv4+IPv6 en production

---

## 1️⃣ AUTO-CONFIGURATION IPv6 : LES 3 MODES

### Le mécanisme de base : Router Advertisement (RA)

> Avant de demander une adresse, un hôte IPv6 envoie un **Router Solicitation (RS)** multicast. Le routeur répond avec un **Router Advertisement (RA)** qui contient des instructions d'auto-configuration. Les RA sont aussi envoyés périodiquement sans sollicitation.

```
PC (nouvellement connecté)          Routeur
       │                               │
       │── Router Solicitation ───────►│  (ff02::2 — tous les routeurs)
       │◄── Router Advertisement ──────│  (ff02::1 — tous les nœuds)
       │                               │
       │  Contenu du RA :              │
       │    - Préfixe : 2001:db8:1::/64│
       │    - M flag : 0 ou 1          │
       │    - O flag : 0 ou 1          │
       │    - A flag : 1               │
       │    - Lifetime, MTU...         │
```

---

### Les 3 modes et leurs flags

| **Mode** | **M flag** | **O flag** | **Adresse obtenue de** | **DNS/options de** |
|---|---|---|---|---|
| **SLAAC pur** | 0 | 0 | Hôte calcule (EUI-64 ou aléatoire) | RA (option RDNSS) |
| **DHCPv6 Stateless** | 0 | 1 | Hôte calcule (EUI-64) | **Serveur DHCPv6** |
| **DHCPv6 Stateful** | **1** | 0 | **Serveur DHCPv6** (pool d'adresses) | Serveur DHCPv6 |

> **Mémo flags :**
> - **M** = **M**anaged = adresse **M**anagée par DHCPv6
> - **O** = **O**ther = autres options (DNS) par DHCPv6
> - **A** = **A**utonomous = le préfixe peut être utilisé pour SLAAC

---

## 2️⃣ SLAAC ET EUI-64

### Principe de SLAAC

> **SLAAC** (StateLess Address AutoConfiguration — RFC 4862) permet à un hôte de construire sa propre adresse IPv6 à partir du préfixe annoncé dans le RA et de son adresse MAC (via EUI-64).

```
Préfixe RA    :  2001:db8:1::/64
Adresse MAC   :  00:1A:2B:3C:4D:5E
                           ↓ EUI-64
Interface ID  :  021a:2bff:fe3c:4d5e
                           ↓ concaténation
Adresse IPv6  :  2001:db8:1::21a:2bff:fe3c:4d5e/64
```

---

### Calcul EUI-64 — Les 3 étapes

$$\boxed{\text{EUI-64 : Couper MAC → Insérer FF:FE → Inverser bit U/L}}$$

**Exemple : MAC = 00:1A:2B:3C:4D:5E**

```
ÉTAPE 1 — Couper l'adresse MAC en deux moitiés de 3 octets :
  00:1A:2B  |  3C:4D:5E
  (OUI)         (NIC)

ÉTAPE 2 — Insérer FF:FE au milieu :
  00:1A:2B:FF:FE:3C:4D:5E

ÉTAPE 3 — Inverser le bit U/L (7ème bit = bit 1 de l'octet 1) :
  00 en binaire = 0000 0000
                        ↑ 7ème bit (bit 6 en comptant depuis 0) = 0
  Inverser : 0 → 1
  0000 0010 = 02 en hexadécimal

Résultat EUI-64 : 02:1A:2B:FF:FE:3C:4D:5E
Notation IPv6   : 021a:2bff:fe3c:4d5e
```

> **Pourquoi inverser le bit U/L ?** En IEEE 802, le bit 7 de l'OUI indique si l'adresse est Universally (0) ou Locally (1) administered. En IPv6, la convention est inversée : 1 = universel. La plupart des MACs grand public ont ce bit à 0 → après inversion → 1 = universel (unique globalement).

---

### Privacy Extensions (RFC 4941)

> **Problème** : avec EUI-64, l'adresse IPv6 contient le MAC de la carte réseau → traçabilité de l'utilisateur possible d'un réseau à l'autre.

> **Solution** : les systèmes modernes (Windows, Linux, macOS, Android, iOS) utilisent les **Privacy Extensions** qui génèrent un identifiant d'interface **aléatoire** renouvelé régulièrement. L'adresse EUI-64 est toujours calculée mais n'est généralement pas utilisée comme adresse source préférée.

```
Sur Windows :
netsh interface ipv6 show privacy
→ "Temporary Address" : l'adresse aléatoire préférée (expire)
→ "Public Address"    : l'adresse EUI-64 permanente
```

---

## 3️⃣ DHCPV6 STATELESS ET STATEFUL

### DHCPv6 Stateless — Adresse SLAAC + options DHCPv6

> **Cas d'usage :** on veut SLAAC (simple, sans serveur pour les adresses) mais avec un DNS centralisé géré par un serveur DHCPv6.

```
RA envoyé par le routeur :
  M = 0 (ne pas contacter DHCPv6 pour une adresse)
  O = 1 (contacter DHCPv6 pour les AUTRES options — DNS, domaine)
  Prefix : 2001:db8:1::/64, A=1 (utiliser SLAAC)
```

**Configuration Cisco IOS :**

```ios
! Créer le pool DHCPv6 (options seulement — pas de pool d'adresses)
ipv6 dhcp pool STATELESS-POOL
  dns-server 2001:db8:cafe::53
  domain-name ciel-ent.fr

! Appliquer sur l'interface LAN
interface GigabitEthernet0/0
  ipv6 address 2001:db8:1::1/64
  ipv6 nd other-config-flag          ! → O=1 dans les RA
  ipv6 dhcp server STATELESS-POOL
  no shutdown
```

---

### DHCPv6 Stateful — Adresse ET options depuis DHCPv6

> **Cas d'usage :** l'entreprise a besoin de traçabilité (qui a quelle adresse à quelle heure). Comme DHCP en IPv4. Contrôle total des attributions.

```
RA envoyé par le routeur :
  M = 1 (contacter DHCPv6 pour obtenir une adresse)
  O = 0 (le serveur DHCPv6 fournira aussi les options)
  Prefix : 2001:db8:1::/64, A=0 (ne PAS utiliser SLAAC)
```

**Configuration Cisco IOS :**

```ios
! Pool DHCPv6 avec plage d'adresses
ipv6 dhcp pool STATEFUL-POOL
  address prefix 2001:db8:1::/64 lifetime 86400 preferred 43200
  dns-server 2001:db8:cafe::53
  domain-name ciel-ent.fr

! Appliquer sur l'interface LAN
interface GigabitEthernet0/0
  ipv6 address 2001:db8:1::1/64
  ipv6 nd managed-config-flag        ! → M=1 dans les RA
  ipv6 dhcp server STATEFUL-POOL
  no shutdown
```

> ⚠️ **Client vs Relais** : si le serveur DHCPv6 n'est pas sur le même segment que les hôtes, un **DHCPv6 relay** (comme le DHCP helper-address en IPv4) est nécessaire :
> ```ios
> interface GigabitEthernet0/0
>   ipv6 dhcp relay destination 2001:db8:server::1  ! IP du serveur DHCPv6
> ```

---

📷 **[ILLUSTRATION 1]**
*Diagramme comparatif en trois colonnes montrant les 3 modes d'auto-configuration IPv6. Colonne gauche "SLAAC pur" : PC calcule EUI-64 depuis MAC + préfixe RA, DNS dans le RA (RDNSS). Colonne centrale "DHCPv6 Stateless" : même EUI-64 mais flèche vers serveur DHCPv6 pour DNS uniquement. Colonne droite "DHCPv6 Stateful" : flèche vers serveur DHCPv6 pour l'adresse ET le DNS, le RA a M=1. Sous chaque colonne : les flags M/O correspondants (0/0, 0/1, 1/0). Style tableau comparatif infographique, fond blanc, couleurs distinctes par mode.*

> **Légende :** Les trois modes d'auto-configuration IPv6. SLAAC pur : autonome et simple, sans serveur. DHCPv6 Stateless : autonomie pour l'adresse, mais les options (DNS, nom de domaine) sont gérées centralement. DHCPv6 Stateful : contrôle total des attributions d'adresses, nécessaire pour la traçabilité réglementaire.

---

## 4️⃣ OSPFV3 MULTI-AREA

### Rappel S1-A3 : OSPFv3 single-area

> En S1-A3, OSPFv3 opérait dans l'area 0 (backbone). Pour les grands réseaux, OSPF se divise en **areas** pour limiter la taille de la LSDB et réduire la charge SPF.

### ABR — Area Border Router

> Un **ABR** (Area Border Router) est un routeur qui appartient à **l'area 0 (backbone) ET à au moins une autre area**. Il redistribue les informations de routage entre les areas sous forme de **Type-3 LSA** (routes sommaires).

```
                Area 1                  Area 0                  Area 2
        ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
        │  R1 ── R2 ── ABR│────│ ABR ── R5 ── ABR │────│ ABR ── R7 ── R8 │
        │  LAN-A  LAN-B   │    │       backbone    │    │  LAN-C  LAN-D  │
        └─────────────────┘    └──────────────────┘    └─────────────────┘
        Routes connues ici     Type-3 LSA traverse     Reçoit résumé Area 1
        restent dans Area 1    l'area 0                depuis ABR
```

### Configuration OSPFv3 multi-area

```ios
! Sur R-ABR (appartient à Area 0 et Area 1) :
ipv6 unicast-routing
ipv6 router ospf 1
  router-id 10.0.0.1

! Interface vers Area 0 (backbone) :
interface GigabitEthernet0/0
  ipv6 address 2001:db8:core::1/64
  ipv6 ospf 1 area 0

! Interface vers Area 1 :
interface GigabitEthernet0/1
  ipv6 address 2001:db8:area1::1/64
  ipv6 ospf 1 area 1          ← Area différente !

! Route summary (optionnel — réduire les LSA) :
ipv6 router ospf 1
  area 1 range 2001:db8:10::/48  ! Résumer toutes les routes Area 1
```

### Stub Area en OSPFv3

> Une **stub area** reçoit une route par défaut depuis l'ABR au lieu de toutes les routes externes. Réduit la taille de la LSDB dans les areas périphériques.

```ios
! Configurer une stub area (sur TOUS les routeurs de l'area) :
ipv6 router ospf 1
  area 2 stub
```

---

## 5️⃣ RIPNG — ALTERNATIVE LÉGÈRE À OSPFV3

### Qu'est-ce que RIPng ?

> **RIPng** (RIP next generation — RFC 2080) est l'adaptation de RIP pour IPv6. Simple à configurer, adapté aux petits réseaux. Pas d'élection DR/BDR, pas d'areas.

| **Critère** | **RIPng** | **OSPFv3** |
|---|---|---|
| Algorithme | Bellman-Ford (Distance Vector) | Dijkstra (Link State) |
| Métrique | Nombre de sauts (max **15**) | Coût (bande passante) |
| Convergence | Lente (~180s) | Rapide (< 10s) |
| Multi-area | ❌ Non | ✅ Oui |
| Scalabilité | Petits réseaux (< 15 sauts) | Grands réseaux |
| Multicast hellos | **ff02::9** | ff02::5 / ff02::6 |
| Timer update | 30 secondes | Sur événement |
| Config complexité | Très simple | Modérée |

**Quand utiliser RIPng ?**
- Réseau de < 5 routeurs
- Environnement de lab / test
- Interopérabilité avec du matériel ne supportant pas OSPFv3
- Réseau de succursale isolée simple

### Configuration RIPng (Cisco IOS)

```ios
! Créer le processus RIPng :
ipv6 router rip MON-RIP

! Activer sur chaque interface :
interface GigabitEthernet0/0
  ipv6 rip MON-RIP enable

interface GigabitEthernet0/1
  ipv6 rip MON-RIP enable

! Route par défaut (si besoin) :
ipv6 router rip MON-RIP
  default-information originate   ! Annoncer ::/0 aux voisins

! Vérification :
show ipv6 rip                    ! Voisins et interfaces RIPng
show ipv6 route rip              ! Routes IPv6 apprises via RIPng (R)
show ipv6 rip database           ! Table RIPng complète
```

---

📷 **[ILLUSTRATION 2]**
*Schéma comparatif RIPng vs OSPFv3. Deux réseaux côte à côte. À gauche : réseau simple de 4 routeurs linéaires avec RIPng — flèches de mise à jour toutes les 30s, annotation "max 15 sauts, convergence 180s". À droite : réseau d'entreprise de 12 routeurs organisés en 3 areas (0, 1, 2) avec OSPFv3 — un ABR au centre, annotation "convergence < 10s, scalable". Encadrés verts/rouges pour indiquer où chaque protocole est adapté. Style diagramme réseau comparatif, fond blanc.*

> **Légende :** RIPng et OSPFv3 couvrent des besoins différents. RIPng est idéal pour les petits réseaux (< 5-6 routeurs) où sa simplicité est un avantage. OSPFv3 est indispensable pour les réseaux d'entreprise avec plus de 10 routeurs ou des exigences de convergence rapide.

---

## 6️⃣ COEXISTENCE IPv4/IPv6 EN PRODUCTION

### La réalité actuelle : le dual-stack est universel

> En 2026, aucune entreprise ne migre en IPv6 pur du jour au lendemain. La stratégie universelle est le **dual-stack** : chaque interface dispose simultanément d'une adresse IPv4 **et** d'une adresse IPv6. Les deux protocoles coexistent indéfiniment.

```ios
! Interface dual-stack sur Cisco IOS :
interface GigabitEthernet0/0
  ip address 192.168.1.1 255.255.255.0        ! IPv4
  ipv6 address 2001:db8:1::1/64               ! IPv6 GUA
  ipv6 nd managed-config-flag                  ! RA pour DHCPv6
  no shutdown
```

### Préférence IPv6 (RFC 6724)

> Quand un hôte dual-stack contacte un serveur qui répond aussi en dual-stack, l'OS préfère **IPv6** sur IPv4. Ce comportement est défini par la RFC 6724. Il peut être modifié par la configuration locale.

```
PC dual-stack → ping google.com
  DNS retourne : A = 216.58.209.46 (IPv4)
                AAAA = 2a00:1450:4007:80e::200e (IPv6)
  OS dual-stack : préfère l'adresse AAAA → connexion via IPv6
```

---

### Tunnel 6in4 — Traverser un réseau IPv4 en IPv6

> Quand deux îlots IPv6 sont séparés par un réseau IPv4, on encapsule les paquets IPv6 dans des paquets IPv4 (**6in4**, RFC 4213).

```
[Site A IPv6] ──IPv6── [R1]───6in4 tunnel (IPv4)───[R2] ──IPv6── [Site B IPv6]
             R1 IP WAN: 203.0.113.1                 R2 IP WAN: 203.0.113.5
```

```ios
! Configuration tunnel 6in4 sur R1 :
interface Tunnel0
  ipv6 address 2001:db8:tunnel::1/64
  tunnel source GigabitEthernet0/1   ! Interface IPv4 locale
  tunnel destination 203.0.113.5     ! IP IPv4 du site distant
  tunnel mode ipv6ip                 ! Mode : IPv6 dans IPv4

! Route IPv6 vers le site B via le tunnel :
ipv6 route 2001:db8:siteB::/48 Tunnel0
```

> **Limitations 6in4 :** ne fonctionne pas derrière NAT (les deux extrémités doivent avoir des IPs IPv4 publiques). Solution alternative : **6to4** (automatique mais déprécié) ou **Teredo** (UDP, traverse NAT).

---

### 464XLAT — Relier des appareils IPv6-only à des services IPv4

> Dans les réseaux modernes (FAI mobiles notamment), certains segments sont **IPv6-only**. Le **464XLAT** (RFC 6877) permet à des applications qui ne supportent que l'IPv4 de communiquer via un réseau IPv6-only.

```
[App IPv4-only] → [CLAT: traduit IPv4→IPv6] → [Réseau IPv6] → [PLAT: IPv6→IPv4] → [Serveur IPv4]
```

> **Exemple réel :** votre smartphone peut n'avoir qu'une adresse IPv6 sur le réseau mobile (FAI mobile souvent en IPv6-only). Les apps qui ne connaissent que l'IPv4 fonctionnent grâce à 464XLAT embarqué dans l'OS Android/iOS.

---

### Tableau des mécanismes de transition

| **Mécanisme** | **Principe** | **Usage** | **Statut** |
|---|---|---|---|
| **Dual-stack** | IPv4 + IPv6 simultanément | Transition progressive | ✅ Recommandé |
| **6in4** | IPv6 dans IPv4 (tunnel statique) | Îlots IPv6 séparés par IPv4 | ✅ Production |
| **6to4** | Tunnel automatique (préfixe 2002::/16) | Dépanage rapide | ⚠️ Déprécié |
| **Teredo** | Tunnel IPv6 via UDP/IPv4 (traverse NAT) | Windows legacy | ⚠️ Déprécié |
| **NAT64** | Traduction IPv6 → IPv4 | Réseaux IPv6-only vers services IPv4 | ✅ Production |
| **464XLAT** | CLAT (client) + PLAT (fournisseur) | Mobiles IPv6-only | ✅ Production |
| **DS-Lite** | IPv4 dans IPv6 (ISP natif IPv6) | FAI modernes | ✅ Production |

---

## 7️⃣ COMMANDES DE VÉRIFICATION IPv6 AVANCÉES

```ios
! ── Auto-configuration ────────────────────────────────────────────────
show ipv6 interface Gi0/0         ! Voir adresses, LLA, RA envoyés
show ipv6 nd ra                   ! Router Advertisements envoyés
show ipv6 dhcp pool               ! Pools DHCPv6 configurés
show ipv6 dhcp binding            ! Baux DHCPv6 (mode stateful)

! ── Routage ──────────────────────────────────────────────────────────
show ipv6 route                   ! Table de routage IPv6 complète
show ipv6 route ospf              ! Routes OSPFv3 seulement
show ipv6 route rip               ! Routes RIPng seulement
show ipv6 ospf neighbor           ! Voisins OSPFv3
show ipv6 ospf database           ! LSDB OSPFv3

! ── Dual-stack ──────────────────────────────────────────────────────
show ip interface brief           ! Résumé IPv4
show ipv6 interface brief         ! Résumé IPv6 (toutes interfaces)
ping ipv6 <adresse>               ! Test connectivité IPv6
traceroute ipv6 <adresse>         ! Traceroute IPv6

! ── Tunnel ────────────────────────────────────────────────────────────
show interface Tunnel0            ! État du tunnel
show ipv6 interface Tunnel0       ! Adresses IPv6 du tunnel
```

---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais calculer une adresse EUI-64 depuis une adresse MAC (3 étapes)
- [ ] Je distingue les 3 modes d'auto-config IPv6 (SLAAC / DHCPv6 stateless / stateful)
- [ ] Je sais quand utiliser M=0/O=1 vs M=1/O=0
- [ ] Je sais configurer `ipv6 nd managed-config-flag` et `ipv6 nd other-config-flag`
- [ ] Je sais configurer un pool DHCPv6 stateful avec plage d'adresses
- [ ] Je comprends le rôle de l'ABR en OSPFv3 multi-area
- [ ] Je sais activer RIPng sur une interface (`ipv6 rip NOM enable`)
- [ ] Je connais la limite de RIPng (15 sauts max)
- [ ] Je sais configurer un tunnel 6in4
- [ ] Je comprends la préférence IPv6 sur IPv4 en dual-stack (RFC 6724)

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **SLAAC** | StateLess Address AutoConfiguration — l'hôte calcule sa propre adresse IPv6 |
| **EUI-64** | Extended Unique Identifier 64 bits — interface ID dérivé de l'adresse MAC |
| **M flag** | Managed flag dans RA — M=1 → obtenir l'adresse depuis DHCPv6 |
| **O flag** | Other flag dans RA — O=1 → obtenir les options (DNS) depuis DHCPv6 |
| **RA / RS** | Router Advertisement / Router Solicitation — échanges NDP d'auto-config |
| **DHCPv6 Stateful** | Attribution d'adresses IPv6 par un serveur DHCP (traçabilité) |
| **DHCPv6 Stateless** | Attribution des options DNS/domaine par DHCPv6 ; adresse via SLAAC |
| **ABR** | Area Border Router — routeur OSPF à la frontière de l'area 0 et d'une autre area |
| **Type-3 LSA** | Summary LSA — annonce de routes inter-area dans OSPFv3 |
| **RIPng** | RIP Next Generation — protocole de routage IPv6 simple (max 15 sauts) |
| **Dual-stack** | Configuration IPv4+IPv6 simultanée sur une interface |
| **6in4** | Encapsulation de paquets IPv6 dans des paquets IPv4 (tunnel statique) |
| **464XLAT** | Mécanisme de traduction permettant aux applications IPv4-only d'utiliser un réseau IPv6-only |
| **Privacy Extensions** | RFC 4941 — génération d'un interface ID aléatoire pour remplacer EUI-64 |

---

## 📌 POINTS-CLÉS À RETENIR

1. **SLAAC** = M=0/O=0 = EUI-64 depuis MAC + préfixe RA = sans serveur
2. **DHCPv6 Stateless** = M=0/**O=1** = EUI-64 + DNS depuis DHCPv6
3. **DHCPv6 Stateful** = **M=1**/O=0 = adresse ET DNS depuis DHCPv6 (comme DHCP IPv4)
4. **EUI-64** : couper MAC → insérer FF:FE → inverser bit U/L
5. **OSPFv3 multi-area** = ABR au carrefour de l'area 0 et d'une autre area
6. **RIPng** = max 15 sauts = petits réseaux seulement, multicast ff02::9
7. **Dual-stack** = IPv4+IPv6 simultanément = stratégie de migration recommandée
8. **RFC 6724** = les clients dual-stack préfèrent IPv6 sur IPv4 (surprise en production !)
9. **6in4** = tunnel IPv6 dans IPv4 = pour relier deux îlots IPv6 via un réseau IPv4

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
