# 🔬 LAB OSPF v2 COMPLET 1H + TD OSPFv3 – S1 ANNÉE 3 – E31

**Nom : ________________  Prénom : ________________  Date : ________________**

---

# ═══════════════════════════════════════════
# PARTIE 1 — LAB OSPF v2 COMPLET (60 min chrono)
# ═══════════════════════════════════════════

> **⏱️ Durée : 60 minutes — Conditions d'évaluation — Packet Tracer + Feuille**
> *Vous pouvez utiliser votre fiche cours. Aucun autre document.*

---

## CONTEXTE

> Vous déployez l'infrastructure réseau de **DataVert**, une entreprise avec 3 sites. Chaque site est desservi par un routeur. Le routage dynamique OSPF relie les 3 sites.

---

## 📋 ÉTAPE 1 — Plan d'adressage VLSM (15 min)

### Spécifications des réseaux

Vous disposez du bloc `10.50.0.0/21`. Allouez les sous-réseaux dans l'ordre suivant (du plus grand au plus petit) :

| **Réseau** | **Hôtes requis** | **Préfixe** | **Adresse réseau** | **Broadcast** | **1ère IP utilisable** |
|---|---|---|---|---|---|
| LAN-LYON (site A) | 120 | | | | |
| LAN-PARIS (site B) | 60 | | | | |
| LAN-BORDEAUX (site C) | 28 | | | | |
| WAN A–B (Lyon–Paris) | 2 | | | | |
| WAN B–C (Paris–Bordeaux) | 2 | | | | |

**Q1.** Combien d'adresses reste-t-il dans `10.50.0.0/21` après ces allocations ? (Pour montrer que votre plan ne déborde pas)

_________________________________________________________________________

---

## 📋 ÉTAPE 2 — Configuration OSPF sur 3 routeurs (30 min)

### Topologie

```
[LAN-LYON]──[R-LYON]──WAN-A-B──[R-PARIS]──WAN-B-C──[R-BORDEAUX]──[LAN-BORDEAUX]
                                    │
                               [LAN-PARIS]
```

### Paramètres fixes

| **Routeur** | **Router-ID** | **Interface LAN** | **Interface WAN** |
|---|---|---|---|
| R-LYON | 1.1.1.1 | Gi0/0 | Gi0/1 (vers Paris) |
| R-PARIS | 2.2.2.2 | Gi0/0 | Gi0/1 (Lyon) + Gi0/2 (Bordeaux) |
| R-BORDEAUX | 3.3.3.3 | Gi0/0 | Gi0/1 (vers Paris) |

### Configuration R-LYON

> Configurez les adresses IP sur les interfaces de R-LYON à partir de votre plan d'adressage Étape 1, puis configurez OSPF.

```ios
! Interfaces (adapter avec vos adresses de l'Étape 1) :
R-LYON(config)# interface GigabitEthernet0/0
R-LYON(config-if)# ip address _____________ _____________
R-LYON(config-if)# no shutdown

R-LYON(config)# interface GigabitEthernet0/1
R-LYON(config-if)# ip address _____________ _____________
R-LYON(config-if)# no shutdown

! Configuration OSPF :
R-LYON(config)# router ospf 1
R-LYON(config-router)# router-id _____________
R-LYON(config-router)# network _____________ _____________ area 0
R-LYON(config-router)# network _____________ _____________ area 0
R-LYON(config-router)# passive-interface _____________
```

### Configuration R-PARIS

```ios
R-PARIS(config)# interface GigabitEthernet0/0
R-PARIS(config-if)# ip address _____________ _____________
R-PARIS(config-if)# no shutdown

R-PARIS(config)# interface GigabitEthernet0/1
R-PARIS(config-if)# ip address _____________ _____________
R-PARIS(config-if)# no shutdown

R-PARIS(config)# interface GigabitEthernet0/2
R-PARIS(config-if)# ip address _____________ _____________
R-PARIS(config-if)# no shutdown

R-PARIS(config)# router ospf 1
R-PARIS(config-router)# router-id _____________
R-PARIS(config-router)# network _____________ _____________ area 0
R-PARIS(config-router)# network _____________ _____________ area 0
R-PARIS(config-router)# network _____________ _____________ area 0
R-PARIS(config-router)# passive-interface _____________
```

### Configuration R-BORDEAUX

```ios
! [À compléter par le candidat]
```

---

## 📋 ÉTAPE 3 — Vérification (10 min)

### Relevez les sorties suivantes :

**Sur R-PARIS :**

```ios
R-PARIS# show ip ospf neighbor
```

```
Neighbor ID  Pri  State   Dead Time  Address    Interface
___________  ___  ______  _________  _________  _________
___________  ___  ______  _________  _________  _________
```

**Q2.** R-PARIS voit-il ses deux voisins en état FULL ? ___________

**Q3.** Sur le lien Lyon–Paris (/30), quel état attendez-vous (`FULL/DR` ou `FULL/ -`) ? Pourquoi ?

_________________________________________________________________________

```ios
R-LYON# show ip route ospf
```

**Q4.** Quels réseaux R-LYON a-t-il appris via OSPF (lignes commençant par `O`) ?

_________________________________________________________________________

---

## 📋 ÉTAPE 4 — Troubleshooting (5 min)

> Le formateur a injecté une erreur dans la configuration. Les réseaux Lyon et Bordeaux ne se voient pas via `show ip route`.

**Commandes de diagnostic à exécuter :**

```ios
! Sur R-PARIS :
show ip ospf neighbor
show ip route ospf
show ip ospf interface
```

**Symptôme observé :** _________________________________________

**Hypothèse :** _________________________________________

**Commande de correction :** _________________________________________

**Vérification :** _________________________________________

---

## 📊 BARÈME LAB OSPF v2

| **Étape** | **Critère** | **Points** |
|---|---|---|
| VLSM | 5 sous-réseaux corrects (préfixe, réseau, broadcast) | /5 |
| Config R-LYON | Adresses + OSPF correct + passive-interface | /3 |
| Config R-PARIS | Adresses + OSPF 3 réseaux + passive-interface | /4 |
| Config R-BORDEAUX | Adresses + OSPF correct | /3 |
| Vérification | show ospf neighbor FULL + show ip route ospf | /3 |
| Troubleshooting | Diagnostic + correction + vérification | /2 |
| **TOTAL** | | **/20** |

> Seuil de validation Lab : **10/20**

---

# ═══════════════════════════════════════════
# PARTIE 2 — TD OSPFv3 (30 min)
# ═══════════════════════════════════════════

> *Ces exercices couvrent les concepts et la configuration OSPFv3. Documents autorisés.*

---

## T1 — Vrai / Faux OSPFv3 (4 pts)

| **Affirmation** | **V/F** | **Correction si fausse** |
|---|---|---|
| En OSPFv3, on utilise `network` dans `ipv6 router ospf` pour déclarer les interfaces | | |
| Le router-id d'OSPFv3 sur Cisco peut être une adresse IPv6 | | |
| Les messages hello OSPFv3 sont envoyés depuis les adresses LLA (fe80::x) | | |
| Dans `show ipv6 route ospf`, le next-hop est une adresse GUA du voisin | | |

---

## T2 — Comparatif OSPFv2 / OSPFv3 (4 pts)

Complétez le tableau :

| **Critère** | **OSPFv2** | **OSPFv3** |
|---|---|---|
| Commande pour déclarer un réseau | `network X.X.X.X wc area n` | |
| Adresse source des hellos | IP réelle de l'interface | |
| Multicast hello | 224.0.0.5 | |
| Vérification des voisins | `show ip ospf neighbor` | |
| Prérequis routeur | Aucun de spécifique | |

---

## T3 — Lecture de `show ipv6 ospf neighbor` (4 pts)

```
R-CORE# show ipv6 ospf neighbor

            OSPFv3 Router with ID (10.0.0.1) (Process ID 1)

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
10.0.0.2          1   FULL/ -         00:00:38    4               Gi0/0
10.0.0.3          1   FULL/DR         00:00:36    3               Gi0/1
10.0.0.4          0   2WAY/DROTHER    00:00:34    5               Gi0/1
```

**T3.1 *(1 pt)*** — Quel est le Router-ID de R-CORE ? Pourquoi est-ce une adresse IPv4 et non IPv6 ?

_________________________________________________________________________
_________________________________________________________________________

**T3.2 *(1 pt)*** — Sur l'interface Gi0/0, quel type de lien existe-il entre R-CORE et 10.0.0.2 ? Justifiez avec l'état affiché.

_________________________________________________________________________

**T3.3 *(1 pt)*** — 10.0.0.4 a la priorité 0 et l'état `2WAY/DROTHER`. Est-ce normal ou anormal ? Expliquez.

_________________________________________________________________________
_________________________________________________________________________

**T3.4 *(1 pt)*** — Pour connaître l'adresse LLA du voisin 10.0.0.3, quelle commande utiliser ?

```ios
R-CORE# _______________________________________
```

---

## T4 — Configuration OSPFv3 (8 pts)

### Topologie simple

```
[PC-A : 2001:db8:10::10/64]        [PC-B : 2001:db8:20::10/64]
         │                                    │
     Gi0/0                                Gi0/0
  [  RA  ]──── Gi0/1 ─ 2001:db8:12::/64 ─ Gi0/1 ──[  RB  ]
  R-ID: 1.1.1.1                                    R-ID: 2.2.2.2
  Gi0/0: 2001:db8:10::1/64                         Gi0/0: 2001:db8:20::1/64
  Gi0/1: 2001:db8:12::1/64                         Gi0/1: 2001:db8:12::2/64
```

**T4.a *(3 pts)*** — Rédigez la configuration OSPFv3 complète de RA (y compris `ipv6 unicast-routing`, les adresses IPv6 sur les interfaces, l'activation OSPFv3, le router-id et la passive-interface côté PC) :

```ios
! Activer le routage IPv6 :
_____________________________

! Processus OSPFv3 :
_____________________________
_____________________________

! Interface LAN :
interface GigabitEthernet0/0
  ipv6 address _____________________________
  _____________________________

! Interface WAN :
interface GigabitEthernet0/1
  ipv6 address _____________________________
  _____________________________

! Passive-interface LAN :
_____________________________
  passive-interface _____________________________
```

**T4.b *(2 pts)*** — Rédigez la configuration OSPFv3 sur RB (sans répéter `ipv6 unicast-routing`) :

```ios
ipv6 router ospf 1
  router-id _____________________________

interface GigabitEthernet0/0
  ipv6 address _____________________________
  _____________________________

interface GigabitEthernet0/1
  ipv6 address _____________________________
  _____________________________

ipv6 router ospf 1
  passive-interface _____________________________
```

**T4.c *(1 pt)*** — Après configuration, quelle commande permet de vérifier que l'adjacence est bien établie entre RA et RB ?

```ios
RA# _______________________________________
```

**T4.d *(1 pt)*** — Dans `show ipv6 route ospf` sur RA, quelle route attendez-vous ? Quel sera le **next-hop** de cette route ?

```
Route apprise : _____________________________
Next-hop      : _____________________________ (type d'adresse : _____)
```

**T4.e *(1 pt)*** — PC-A peut-il pinger PC-B après cette configuration ? Sinon, que manque-t-il ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME TD OSPFv3

| **Section** | **Points** |
|---|---|
| T1 – Vrai/Faux | /4 |
| T2 – Comparatif | /4 |
| T3 – Lecture show | /4 |
| T4 – Configuration | /8 |
| **TOTAL** | **/20** |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
