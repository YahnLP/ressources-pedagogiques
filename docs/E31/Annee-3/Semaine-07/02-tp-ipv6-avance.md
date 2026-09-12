# 🔬 TP PACKET TRACER – S7 ANNÉE 3 – E31
## IPv6 Avancé : SLAAC, DHCPv6, OSPFv3 Multi-Area, RIPng, Dual-Stack

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Observer et configurer SLAAC sur une interface LAN
- ✅ Configurer DHCPv6 stateless (O=1) puis stateful (M=1) et comparer
- ✅ Déployer OSPFv3 sur 3 areas (backbone + 2 areas)
- ✅ Configurer RIPng sur un sous-réseau et comparer avec OSPFv3
- ✅ Vérifier la connectivité dual-stack (IPv4 ET IPv6 simultanément)

---

## ⏱️ DURÉE : 70 min

---

## 📋 TOPOLOGIE

```
                        AREA 0 (BACKBONE OSPFv3)
        ┌────────────────────────────────────────────────────────────┐
        │                                                            │
  [R-PARIS]──────────── 2001:db8:12::/64 ──────────────[R-LYON]    │
    │                         Area 0                        │        │
    │ Area 1                                           Area 2 │      │
    └──[R-SITE-A]                                    [R-SITE-B]──┘  │
         │                                                 │         │
    [LAN-A: 2001:db8:a::/64]                     [LAN-B: 2001:db8:b::/64]
    [aussi 192.168.1.0/24]                        [aussi 192.168.2.0/24]
         │                                                 │
    [PC-A, PC-B]                                     [PC-C, PC-D]
    (dual-stack)                                     (dual-stack)

RIPng (réseau séparé) :
  [R-SMALL-1]── ff02::9 ──[R-SMALL-2]
  LAN-SMALL: 2001:db8:ff::/64
```

---

## 📋 PLAN D'ADRESSAGE

| **Lien** | **IPv6** | **Router-ID** |
|---|---|---|
| R-PARIS ↔ R-LYON (Area 0) | `2001:db8:12::/64` | PARIS=1.1.1.1, LYON=2.2.2.2 |
| R-PARIS ↔ R-SITE-A (Area 1) | `2001:db8:1a::/64` | SITE-A=3.3.3.3 |
| R-LYON ↔ R-SITE-B (Area 2) | `2001:db8:2b::/64` | SITE-B=4.4.4.4 |
| LAN-A | `2001:db8:a::/64` + `192.168.1.0/24` | — |
| LAN-B | `2001:db8:b::/64` + `192.168.2.0/24` | — |
| RIPng | `2001:db8:ff::/64` | SMALL-1=5.5.5.5, SMALL-2=6.6.6.6 |

**LLA manuelles recommandées :**
- R-PARIS : fe80::1 sur toutes ses interfaces
- R-LYON : fe80::2 sur toutes ses interfaces
- R-SITE-A : fe80::3 ; R-SITE-B : fe80::4

---

## 🧪 PARTIE 1 — SLAAC et DHCPv6 sur LAN-A (20 min)

### 1.1 — Configurer l'interface LAN-A de R-SITE-A pour SLAAC pur

```ios
R-SITE-A(config)# ipv6 unicast-routing

R-SITE-A(config)# interface GigabitEthernet0/0
R-SITE-A(config-if)# ipv6 address 2001:db8:a::1/64
R-SITE-A(config-if)# ipv6 nd ra-interval 10
R-SITE-A(config-if)# no shutdown
```

**Depuis PC-A (après ~15 secondes) :**

```
PC-A# ipv6config
```

**Q1.** Quelle adresse IPv6 a-t-il obtenu ? ___________________________________________

**Q2.** La fin de cette adresse ressemble-t-elle à l'adresse MAC du PC-A ? Regardez la MAC avec `ipconfig/all`. Expliquez le mécanisme.

_________________________________________________________________________
_________________________________________________________________________

---

### 1.2 — Passer en DHCPv6 Stateless (O=1)

```ios
R-SITE-A(config)# ipv6 dhcp pool POOL-LAN-A
R-SITE-A(config-dhcpv6)# dns-server 2001:db8:cafe::53
R-SITE-A(config-dhcpv6)# domain-name ciel-a3.fr

R-SITE-A(config)# interface GigabitEthernet0/0
R-SITE-A(config-if)# ipv6 nd other-config-flag
R-SITE-A(config-if)# ipv6 dhcp server POOL-LAN-A
```

**Renouveler la configuration IP sur PC-A.**

**Q3.** L'adresse IPv6 de PC-A a-t-elle changé ? Pourquoi ?

_________________________________________________________________________

**Q4.** Quelle commande sur R-SITE-A montre le pool DHCPv6 configuré ?

```ios
R-SITE-A# _______________________________________
```

---

### 1.3 — Passer en DHCPv6 Stateful (M=1)

```ios
R-SITE-A(config)# ipv6 dhcp pool POOL-LAN-A-STATEFUL
R-SITE-A(config-dhcpv6)# address prefix 2001:db8:a::/64 lifetime 3600 preferred 1800
R-SITE-A(config-dhcpv6)# dns-server 2001:db8:cafe::53

R-SITE-A(config)# interface GigabitEthernet0/0
R-SITE-A(config-if)# no ipv6 nd other-config-flag
R-SITE-A(config-if)# ipv6 nd managed-config-flag
R-SITE-A(config-if)# no ipv6 dhcp server POOL-LAN-A
R-SITE-A(config-if)# ipv6 dhcp server POOL-LAN-A-STATEFUL
```

**Q5.** Comment a changé l'adresse IPv6 de PC-A ? Pourquoi est-elle différente du mode SLAAC ?

_________________________________________________________________________
_________________________________________________________________________

**Q6.** Quelle commande affiche les baux DHCPv6 actifs (à qui quelle adresse a été attribuée) ?

```ios
R-SITE-A# _______________________________________
```

---

## 🔬 PARTIE 2 — OSPFv3 Multi-Area (25 min)

### 2.1 — Configuration OSPFv3

**Rappel : R-PARIS et R-LYON sont des ABR (Area 0 + Area 1/2).**

**Sur R-PARIS (ABR Area 0 + Area 1) :**

```ios
R-PARIS(config)# ipv6 unicast-routing

R-PARIS(config)# ipv6 router ospf 1
R-PARIS(config-rtr)# router-id 1.1.1.1

! Interface vers R-LYON (Area 0) :
R-PARIS(config)# interface GigabitEthernet0/1
R-PARIS(config-if)# ipv6 address 2001:db8:12::1/64
R-PARIS(config-if)# ipv6 ospf 1 area ______    ← Backbone

! Interface vers R-SITE-A (Area 1) :
R-PARIS(config)# interface GigabitEthernet0/0
R-PARIS(config-if)# ipv6 address 2001:db8:1a::1/64
R-PARIS(config-if)# ipv6 ospf 1 area ______    ← Area 1
```

**Sur R-SITE-A (routeur interne Area 1) :**

```ios
! [Compléter — router-id 3.3.3.3, toutes interfaces en area 1]
! N'oubliez pas passive-interface sur le LAN !
```

**Sur R-LYON et R-SITE-B :** (même logique, adapter les areas)

---

### 2.2 — Vérification OSPFv3 multi-area

```ios
R-PARIS# show ipv6 ospf neighbor
```

**Q7.** R-PARIS doit voir deux voisins. Remplissez :

| **Neighbor ID** | **State** | **Interface** | **Area (déduire)** |
|---|---|---|---|
| | | | |
| | | | |

**Q8.** Exécutez `show ipv6 ospf database` sur R-PARIS. Quels types de LSA voyez-vous ? (Chercher Type-1, Type-3, Type-9)

_________________________________________________________________________

**Q9.** Sur R-SITE-A, vérifiez `show ipv6 route ospf`. Voyez-vous les routes de LAN-B (`2001:db8:b::/64`) ? Quel est leur marqueur dans la table de routage ?

_________________________________________________________________________

**Q10.** Testez la connectivité complète :

```
PC-A# ping 2001:db8:b::10   (PC-C dans LAN-B)
```

Résultat : _______ 

---

## 📡 PARTIE 3 — RIPng (10 min)

### 3.1 — Configuration RIPng sur R-SMALL-1 et R-SMALL-2

**Sur R-SMALL-1 :**

```ios
R-SMALL-1(config)# ipv6 unicast-routing

R-SMALL-1(config)# ipv6 router rip PETITRESEAU

R-SMALL-1(config)# interface GigabitEthernet0/0
R-SMALL-1(config-if)# ipv6 address 2001:db8:ff::1/64
R-SMALL-1(config-if)# ipv6 rip PETITRESEAU enable

R-SMALL-1(config)# interface GigabitEthernet0/1
R-SMALL-1(config-if)# ipv6 address 2001:db8:small-a::1/64
R-SMALL-1(config-if)# ipv6 rip PETITRESEAU enable
```

**Même logique sur R-SMALL-2.**

**Q11.** Vérifiez avec `show ipv6 rip` sur R-SMALL-1. Quelles interfaces sont actives ?

_________________________________________________________________________

**Q12.** Quelle commande permet de voir les routes apprises via RIPng ?

```ios
R-SMALL-1# _______________________________________
```

**Q13.** Quelle est la métrique maximale de RIPng ? Qu'arrive-t-il à une route qui atteint cette valeur ?

_________________________________________________________________________

---

## 💻 PARTIE 4 — Dual-Stack et Connectivité (15 min)

### 4.1 — Configurer IPv4 sur LAN-A (dual-stack)

```ios
R-SITE-A(config)# interface GigabitEthernet0/0
R-SITE-A(config-if)# ip address 192.168.1.1 255.255.255.0

! Et configurer OSPF pour IPv4 :
R-SITE-A(config)# router ospf 10
R-SITE-A(config-router)# network 192.168.1.0 0.0.0.255 area 0
```

> *Note : En production, on aurait aussi OSPFv2 sur les liaisons WAN. Pour ce TP, concentrons-nous sur les LANs.*

**Configurer les PCs en dual-stack :**
- PC-A : `192.168.1.10/24`, GW `192.168.1.1`
- PC-A garde son adresse IPv6 de la Partie 1

---

### 4.2 — Tests de connectivité dual-stack

```
PC-A# ping 192.168.1.1       → IPv4 LAN local   : _______
PC-A# ping 2001:db8:a::1     → IPv6 LAN local   : _______
PC-A# ping 2001:db8:b::10    → IPv6 inter-sites : _______
```

**Q14.** Si vous pinguez l'ADRESSE DNS `dns.google` (si résolution disponible en PT), quel protocole est utilisé en premier par le PC dual-stack ? Pourquoi ?

_________________________________________________________________________

**Q15.** Quelle commande affiche simultanément les adresses IPv4 ET IPv6 de toutes les interfaces du routeur ?

```ios
R-SITE-A# _________________________________ ! Pour IPv6
R-SITE-A# _________________________________ ! Pour IPv4
```

**Q16.** Expliquez pourquoi `show ipv6 interface brief` montre des LLA même sur des interfaces qui n'ont pas d'adresse GUA configurée.

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 – SLAAC | Config + Q1-Q2 | /3 |
| Partie 1 – DHCPv6 SL | Config + Q3-Q4 | /2 |
| Partie 1 – DHCPv6 SF | Config + Q5-Q6 | /3 |
| Partie 2 – OSPFv3 | Config 4 routeurs + Q7-Q10 | /6 |
| Partie 3 – RIPng | Config + Q11-Q13 | /3 |
| Partie 4 – Dual-stack | Config + Q14-Q16 | /3 |
| **TOTAL** | | **/20** |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
