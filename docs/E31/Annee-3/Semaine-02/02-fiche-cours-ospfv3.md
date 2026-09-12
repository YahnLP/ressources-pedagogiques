# 📘 FICHE DE COURS — S2 · 3ᵉ ANNÉE · E31
## OSPFv3 IPv6 : Multi-AF · Coexistence IPv4/IPv6 · Double Stack · Transition

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences travaillées** : S2.2 · S2.6 · C2.2 · C2.3

---

## 🔑 Vocabulaire clé à maîtriser

| Terme | Définition |
|---|---|
| **OSPFv3** | Version 3 d'OSPF — conçue pour IPv6 natif, peut aussi transporter IPv4 via Multi-AF (RFC 5838) |
| **Multi-AF** | Multi Address Family — capacité d'OSPFv3 à transporter plusieurs familles d'adresses (IPv4 ET IPv6) dans un seul processus |
| **Address Family** | Famille d'adresses — IPv4 unicast ou IPv6 unicast — chacune a sa propre LSDB dans OSPFv3 Multi-AF |
| **Double Stack (Dual Stack)** | Configuration d'une interface avec IPv4 ET IPv6 simultanément |
| **Link-Local** | Adresse IPv6 commençant par `FE80::/10` — valide uniquement sur un seul lien physique |
| **EUI-64** | Méthode de génération automatique de l'identifiant d'interface IPv6 depuis l'adresse MAC |
| **Tunneling** | Encapsulation de paquets IPv6 dans des paquets IPv4 pour traverser des réseaux IPv4 |
| **NAT64** | Mécanisme de translation qui permet à des hôtes IPv6 d'accéder à des services IPv4 uniquement |
| **FF02::5** | Adresse multicast OSPFv3 pour tous les routeurs OSPF (équivalent de 224.0.0.5 pour OSPFv2) |
| **FF02::6** | Adresse multicast OSPFv3 pour les routeurs DR/BDR uniquement (équivalent de 224.0.0.6) |
| **ipv6 unicast-routing** | Commande globale IOS activant le routage IPv6 — obligatoire avant toute config IPv6 |
| **Router-ID** | Identifiant unique du routeur dans OSPF — toujours au format IPv4 même en OSPFv3 pur |

---

## 1️⃣ — Pourquoi OSPFv3 ? Les limites d'OSPFv2 face à IPv6

### OSPFv2 ne parle pas IPv6

OSPFv2 a été conçu pour IPv4 uniquement. Les adresses dans ses LSA, ses paquets Hello et ses tables de routage sont des adresses IPv4 — il ne peut pas annoncer de préfixes IPv6.

### Deux approches historiques

```
APPROCHE 1 — Deux processus séparés (approche ancienne)
  router ospf 1        → gère IPv4 (OSPFv2)
  ipv6 router ospf 2   → gère IPv6 (OSPFv3 "classique")
  → 2 processus · 2 LSDBs · 2 fois plus de Hello · plus lourd

APPROCHE 2 — OSPFv3 Multi-AF (approche moderne, recommandée)
  router ospfv3 1
    address-family ipv4 unicast  → remplace OSPFv2
    address-family ipv6 unicast  → ajoute IPv6
  → 1 seul processus · 2 LSDBs séparées mais un seul engine
```

> 💡 **En production aujourd'hui** : OSPFv3 Multi-AF est la norme dans les nouvelles infrastructures. Elle simplifie l'opération et réduit la charge CPU/mémoire.

---

**🖼️ ILLUSTRATION 1**
> *Légende* : Comparaison en 3 colonnes : OSPFv2 seul (une seule table IPv4), OSPFv3 classique (une seule table IPv6), OSPFv3 Multi-AF (deux tables IPv4 et IPv6 dans un seul processus). Chaque colonne montre le process OSPF, les LSDBs, les tables de routage résultantes et les commandes de configuration. La colonne Multi-AF est mise en valeur avec un cadre vert "Approche recommandée".
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 2️⃣ — Différences fondamentales OSPFv2 vs OSPFv3

### Tableau comparatif complet

| Critère | OSPFv2 | OSPFv3 |
|---|---|---|
| **Transport** | IPv4 uniquement | IPv6 natif + IPv4 via Multi-AF |
| **Activation OSPF** | `network X.X.X.X wildcard area N` (dans le process) | `ospfv3 1 ipv4 area N` (sur l'interface) |
| **Hello multicast** | 224.0.0.5 (tous) / 224.0.0.6 (DR/BDR) | FF02::5 (tous) / FF02::6 (DR/BDR) |
| **Next-hop** | Adresse IPv4 | Adresse **link-local** (FE80::) |
| **Authentification** | MD5 ou cleartext intégré | IPsec externe (séparé) |
| **Router-ID** | Adresse IPv4 ou Loopback | Format IPv4 **obligatoire** (même sans IPv4 sur le routeur) |
| **LSA types** | 1, 2, 3, 4, 5 | 1, 2, 3, 4, 5 + 8 (Link LSA), 9 (Intra-Area Prefix) |
| **Commande globale** | `ip routing` (active par défaut) | `ipv6 unicast-routing` (à activer explicitement) |

### Le Router-ID : toujours au format IPv4

> En OSPFv3, même sur un routeur 100% IPv6, le **Router-ID reste au format adresse IPv4**.
>
> Ordre de priorité (identique à OSPFv2) :
> 1. Configuré manuellement : `router-id X.X.X.X`
> 2. Plus haute adresse IPv4 sur une interface Loopback active
> 3. Plus haute adresse IPv4 sur n'importe quelle interface active
>
> ⚠️ Sur un routeur sans IPv4 → **OBLIGATOIRE** de configurer manuellement le Router-ID.

---

## 3️⃣ — Configuration OSPFv3 Multi-AF : les 3 étapes

### Étape 1 — Activer IPv6 routing (globalement)

```cisco
R1(config)# ipv6 unicast-routing
```

> Sans cette commande, le routeur reçoit les paquets IPv6 mais ne les **relaie pas**.
> C'est l'équivalent IPv6 de `ip routing` (qui est actif par défaut sur les routeurs).

### Étape 2 — Configurer le processus OSPFv3 Multi-AF

```cisco
R1(config)# router ospfv3 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# address-family ipv4 unicast
R1(config-router-af)# exit-address-family
R1(config-router)# address-family ipv6 unicast
R1(config-router-af)# exit-address-family
```

> **Note** : les sections `address-family` ne nécessitent généralement pas de commandes supplémentaires — l'activation se fait sur l'interface.

### Étape 3 — Activer OSPFv3 sur chaque interface

```cisco
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ospfv3 1 ipv4 area 0   ! Active l'AF IPv4 sur cette interface
R1(config-if)# ospfv3 1 ipv6 area 0   ! Active l'AF IPv6 sur cette interface
```

> ✅ Ces deux commandes remplacent à la fois la commande `network` d'OSPFv2 et la commande `ipv6 ospf area` de l'ancien OSPFv3 "classique".

### Configuration complète — R1

```cisco
! Obligatoire pour IPv6
ipv6 unicast-routing

! Adressage dual stack
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
 ipv6 address FE80::1 link-local

interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:DB8:1::1/64
 ipv6 address FE80::1 link-local
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
 no shutdown

interface GigabitEthernet0/1
 ip address 10.0.12.1 255.255.255.252
 ipv6 address 2001:DB8:12::1/64
 ipv6 address FE80::1 link-local
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
 no shutdown

! Processus OSPFv3 Multi-AF
router ospfv3 1
 router-id 1.1.1.1
 address-family ipv4 unicast
 exit-address-family
 address-family ipv6 unicast
 exit-address-family
```

---

**🖼️ ILLUSTRATION 2**
> *Légende* : Schéma d'interface dual stack avec les deux couches d'adressage visibles. Une interface GigabitEthernet est représentée avec trois adresses IPv6 (link-local FE80::1, global 2001:DB8:1::1/64) et une adresse IPv4 (192.168.1.1/24). Les flèches montrent que les paquets OSPFv3 IPv4 (AF ipv4) et OSPFv3 IPv6 (AF ipv6) sont tous deux envoyés via cette interface. L'adresse FE80 est mise en évidence comme "next-hop OSPFv3". En dessous, les deux commandes ospfv3 avec leurs annotations.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 4️⃣ — Lire et interpréter `show ipv6 ospf neighbor`

### Format de la sortie

```
R2# show ipv6 ospf neighbor

          OSPFv3 Router with ID (2.2.2.2) (Process ID 1)

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
1.1.1.1           1   FULL/  -        00:00:36    4               GigabitEthernet0/0
3.3.3.3           1   FULL/  -        00:00:39    4               GigabitEthernet0/1
```

### Décoder chaque champ

```
Neighbor ID   = Router-ID du voisin (format IPv4 même en IPv6 pur)
Pri           = Priorité pour l'élection DR/BDR (0 = ne participe pas)
State         = État de l'adjacence (FULL = opérationnelle ✓)
Dead Time     = Compte à rebours avant de déclarer le voisin mort (40s par défaut)
Interface ID  = Identifiant interne de l'interface du voisin
Interface     = Interface locale sur laquelle ce voisin est vu
/  -          = Aucun DR/BDR élu (lien point à point)
/DR           = Ce voisin est le DR sur ce lien
/BDR          = Ce voisin est le BDR
```

### Commandes de vérification complémentaires

```cisco
! Tables de routage séparées
show ip route ospf            → Routes IPv4 apprises via OSPFv3 AF ipv4
show ipv6 route ospf          → Routes IPv6 apprises via OSPFv3 AF ipv6

! Voisins OSPFv3
show ipv6 ospf neighbor       → Adjacences (tous les AF confondus)
show ospfv3 neighbor          → Variante plus détaillée

! Base de données LSDB
show ipv6 ospf database       → LSDB IPv6
show ospfv3 database          → LSDB des deux AF

! Interfaces OSPFv3
show ipv6 ospf interface Gi0/0  → Coût, area, hello interval, next-hello
```

---

**🖼️ ILLUSTRATION 3**
> *Légende* : Sortie `show ipv6 ospf neighbor` annotée avec 7 flèches pointant vers chaque champ : Neighbor ID (format IPv4 obligatoire), Pri (priorité DR), State (FULL=OK), Dead Time (40s countdown), Interface ID (interne), Interface (locale), le symbole `-` après le slash indiquant "pas de DR/BDR sur lien P2P". En dessous, un tableau des états possibles (DOWN/INIT/2-WAY/FULL) avec leur signification, similaire à OSPFv2.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 5️⃣ — Double Stack : coexistence IPv4/IPv6

### Principe du double stack

```
Interface en double stack :
  ip address 192.168.1.1 255.255.255.0    ← IPv4 traditionnel
  ipv6 address 2001:DB8:1::1/64           ← IPv6 global unicast
  ipv6 address FE80::1 link-local         ← IPv6 link-local (généré auto ou manuel)

→ Les deux protocoles fonctionnent en parallèle, indépendamment
→ Un PC dual stack choisit IPv6 en priorité si la destination est joignable en IPv6
→ Aucune translation — chaque protocole achemine ses propres paquets
```

### Ce que voit le routeur en double stack

```
R1# show ip route
C    192.168.1.0/24  is directly connected, Gi0/0
O    192.168.3.0/24  [110/2] via 10.0.12.2

R1# show ipv6 route
C    2001:DB8:1::/64  directly connected, Gi0/0
O    2001:DB8:3::/64  [110/2] via FE80::2, Gi0/1
```

> Deux tables de routage séparées — chacune pour son protocole.

### Adressage IPv6 : les types à connaître

```
Type              Préfixe          Rôle
Global Unicast    2000::/3         Équivalent IPv4 public — routable sur Internet
Link-Local        FE80::/10        Valide sur un seul lien — non routable — OBLIGATOIRE
                                   Utilisé par OSPF, NDP, DHCPv6 link-local
Multicast         FF00::/8         Groupes de diffusion
Loopback          ::1/128          Équivalent 127.0.0.1
```

---

## 6️⃣ — Les 3 mécanismes de transition IPv4 → IPv6

### Mécanisme 1 — Double Stack (Dual Stack)

```
PRINCIPE : L'équipement supporte les deux protocoles simultanément
QUAND    : Réseau progressivement mis à jour — la majorité du parc CIEL
AVANTAGE : Pas de translation — performance native, pas de complexité
LIMITE   : Nécessite de mettre à jour CHAQUE équipement
EXEMPLE  : Ce que vous configurez dans ce TP
```

### Mécanisme 2 — Tunneling (6in4, GRE, 6to4)

```
PRINCIPE : Paquets IPv6 encapsulés dans des paquets IPv4 pour traverser
           une infrastructure IPv4 non encore mise à jour
QUAND    : Connecter deux îlots IPv6 à travers un réseau IPv4
AVANTAGE : Pas besoin de mettre à jour le réseau de transit
LIMITE   : Overhead d'encapsulation · debugging complexe
EXEMPLE  : Tunnel GRE vu en 2A S16 (même concept, ici IPv6 dans IPv4)
```

### Mécanisme 3 — Translation (NAT64)

```
PRINCIPE : Un équipement traduit les paquets IPv6 ↔ IPv4
           en modifiant les en-têtes (similaire au NAT classique)
QUAND    : Hôtes IPv6 uniquement doivent accéder à serveurs IPv4 uniquement
AVANTAGE : Transition partielle possible sans tout mettre à jour
LIMITE   : Perte de transparence end-to-end · problèmes avec certains protocoles
EXEMPLE  : Accès depuis un mobile 5G (IPv6 natif) vers un vieux serveur IPv4
```

---

**🖼️ ILLUSTRATION 4**
> *Légende* : Schéma en trois bandes horizontales illustrant les 3 mécanismes de transition. Bande 1 "Double Stack" : équipements avec les deux logos IPv4+IPv6, communication directe. Bande 2 "Tunneling" : deux îlots IPv6 (bleu) avec un nuage IPv4 (orange) entre eux, un tunnel pointillé traverse le nuage avec "IPv6 encapsulé dans IPv4". Bande 3 "NAT64/Translation" : côté gauche IPv6 (hôte 5G), au centre boîte NAT64 avec des flèches de conversion, côté droit IPv4 (vieux serveur). Chaque bande indique "Quand utiliser" et "Limitation".
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 7️⃣ — Configurer les adresses IPv6 : rappels clés

### Adresse link-local manuelle vs automatique

```cisco
! Automatique (générée depuis la MAC via EUI-64)
interface GigabitEthernet0/0
 ipv6 enable
! → Génère FE80::[dérivé de MAC] — difficile à retenir

! Manuelle (RECOMMANDÉE en production et en TP)
interface GigabitEthernet0/0
 ipv6 address FE80::1 link-local
! → FE80::1 facile à mémoriser et configurer
```

### Convention de nommage EUI-64 sur les LANs

```
Convention lisible pour les examens :
  LAN 1 Site Siège  : 2001:DB8:1::/64 → R1: ::1 · PC: ::10, ::11...
  LAN 2 Site Agence : 2001:DB8:2::/64 → R2: ::1 · PC: ::10...
  WAN R1-R2         : 2001:DB8:12::/64 → R1: ::1 · R2: ::2
  WAN R2-R3         : 2001:DB8:23::/64 → R2: ::1 · R3: ::2
```

---

**🖼️ ILLUSTRATION 5**
> *Légende* : Topologie complète à 3 routeurs avec double stack. R1-R2-R3 en ligne, avec LAN1 sur R1 et LAN3 sur R3. Chaque interface montre ses deux adresses (IPv4 dessus, IPv6 dessous). Les liens WAN affichent les réseaux IPv4 /30 et IPv6 /64. Les adjacences OSPFv3 sont représentées par des arcs verts avec le Router-ID (format IPv4) indiqué. Les tables de routage simplifiées de R2 sont affichées à côté (show ip route + show ipv6 route).
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 📌 Les essentiels à retenir pour l'examen

> ✅ `ipv6 unicast-routing` → obligatoire pour activer le routage IPv6 sur un routeur
> ✅ `router ospfv3 1` + `router-id X.X.X.X` → process Multi-AF (router-id toujours IPv4)
> ✅ `address-family ipv4 unicast` et `address-family ipv6 unicast` → les deux AF
> ✅ Activation sur interface : `ospfv3 1 ipv4 area 0` ET `ospfv3 1 ipv6 area 0`
> ✅ Hello OSPFv3 : multicast **FF02::5** (≠ 224.0.0.5 pour OSPFv2)
> ✅ Next-hop OSPFv3 : adresse **link-local** (FE80::) — pas l'adresse globale
> ✅ `show ipv6 ospf neighbor` → état FULL/- sur liens P2P
> ✅ Double stack = deux tables de routage séparées (show ip route ET show ipv6 route)
> ✅ Trois mécanismes de transition : **Double Stack** (natif) · **Tunneling** (encapsulation) · **NAT64** (translation)

---

*Fiche de Cours — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S2*
*Compétences : S2.2 · S2.6 · C2.2 · C2.3*
