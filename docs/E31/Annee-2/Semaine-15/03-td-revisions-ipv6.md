# 🎯 TD RÉVISIONS E31 A2 + TD IPv6 – S15 ANNÉE 2 – E31

**Nom : ________________  Prénom : ________________  Date : ________________**

---

# ═══════════════════════════════════════════
# PARTIE 1 — TD RÉVISIONS E31 A2
# ═══════════════════════════════════════════

> *Ces exercices couvrent les points les plus souvent défaillants en E31 A2. Durée : 30 min.*

---

## R1 – Adressage et Plan d'adressage (8 pts)

### R1.1 – Calcul rapide

Pour chaque besoin, donnez le préfixe CIDR minimal et le nombre d'hôtes max :

| **Hôtes requis** | **Préfixe** | **Hôtes max** | **Masque décimal** |
|---|---|---|---|
| 14 | | | |
| 50 | | | |
| 2 (liaison P-à-P) | | | |
| 100 | | | |

### R1.2 – Plan d'adressage

Découpez `10.20.0.0/24` pour ces 3 LANs en utilisant le moins d'espace possible :

| **LAN** | **Hôtes** | **Préfixe** | **Réseau** | **Broadcast** | **Passerelle** |
|---|---|---|---|---|---|
| LAN-A | 60 | | | | |
| LAN-B | 25 | | | | |
| LAN-C | 10 | | | | |

---

## R2 – OSPF Révision (6 pts)

### R2.1 – Network Statement

Le routeur R-EDGE a les interfaces suivantes :

| **Interface** | **IP** |
|---|---|
| Gi0/0 | 10.20.0.1/26 (LAN-A) |
| Gi0/1 | 10.20.0.65/27 (LAN-B) |
| Gi0/2 | 10.20.0.97/28 (LAN-C) |
| Gi0/3 | 172.16.0.1/30 (liaison WAN) |

Écrivez les 4 network statements OSPF pour annoncer toutes ces interfaces dans l'area 0 :

```ios
router ospf 1
  router-id 2.2.2.2
  network __________ __________ area 0
  network __________ __________ area 0
  network __________ __________ area 0
  network __________ __________ area 0
```

### R2.2 – Lecture de `show ip ospf neighbor`

```
Neighbor ID   Pri   State           Dead Time   Address       Interface
10.0.0.1        1   FULL/DR         00:00:38    10.20.0.2     Gi0/2
10.0.0.3        0   2WAY/DROTHER    00:00:31    10.20.0.3     Gi0/2
10.0.0.4        1   FULL/ -         00:00:36    172.16.0.2    Gi0/3
```

**Q1.** Sur le segment Gi0/2, qui est le DR ? Qui est R-EDGE (quel rôle a-t-il sur ce segment) ?

_________________________________________________________________________

**Q2.** Pourquoi 10.0.0.3 a-t-il la priorité 0 et l'état 2WAY/DROTHER ? Est-ce normal ?

_________________________________________________________________________

**Q3.** Sur Gi0/3, l'état est `FULL/ -` (sans rôle DR/BDR). Pourquoi ?

_________________________________________________________________________

---

## R3 – ACL Étendue Révision (6 pts)

### Politique de sécurité à implémenter

Réseau : LAN-PROD (172.16.1.0/24) → DMZ-SRV (10.50.0.0/24)

| **Règle** | **Description** |
|---|---|
| P1 | Seul 172.16.1.100 (DBA) peut accéder à 10.50.0.5 (SQL) sur le port 3306 |
| P2 | Tout le LAN-PROD peut accéder à 10.50.0.10 (WEB) en HTTP et HTTPS |
| P3 | Personne du LAN-PROD ne peut faire de Telnet vers la DMZ |
| P4 | Le reste est autorisé |

**R3.1 *(3 pts)*** — Rédigez l'ACL nommée `VERS_DMZ` :

```ios
ip access-list extended VERS_DMZ
  remark P1 - DBA vers SQL
  ___________________________________________________
  remark P2 - LAN vers WEB HTTP
  ___________________________________________________
  remark P2 - LAN vers WEB HTTPS
  ___________________________________________________
  remark P3 - Bloquer Telnet
  ___________________________________________________
  remark P4 - Reste autorisé
  ___________________________________________________
```

**R3.2 *(1 pt)*** — Où et dans quelle direction appliquer cette ACL ? Justifiez.

_________________________________________________________________________
_________________________________________________________________________

**R3.3 *(2 pts)*** — `show ip access-lists VERS_DMZ` montre que la règle P3 (deny Telnet) a 0 matches après 1 heure de fonctionnement. Le DBA vous dit "je ne peux pas me connecter à SQL". Identifiez le problème probable et corrigez-le en 1 commande.

_________________________________________________________________________
_________________________________________________________________________

---

## R4 – HSRP Révision (5 pts)

### Contexte

Deux routeurs sur le LAN 192.168.50.0/24 :

| **Routeur** | **IP réelle** | **Priorité HSRP** | **WAN** | **Tracking** |
|---|---|---|---|---|
| R-CORE | 192.168.50.1 | 130 | Gi0/1 | Décrement 50 |
| R-DIST | 192.168.50.2 | 100 | Gi0/1 | Non configuré |

IP virtuelle HSRP : 192.168.50.254, groupe 2, preempt sur les deux.

**R4.1 *(1 pt)*** — Qui est Active au démarrage ? Pourquoi ?

_________________________________________________________________________

**R4.2 *(1,5 pt)*** — Le WAN de R-CORE tombe. Calculez la nouvelle priorité de R-CORE et concluez si R-DIST prend Active.

```
Priorité R-CORE après tracking : _______ - _______ = _______
Bascule si _______ < _______ ? OUI/NON
Résultat : _______
```

**R4.3 *(1 pt)*** — Le WAN de R-CORE revient. R-CORE reprend-il Active ? Pourquoi ?

_________________________________________________________________________

**R4.4 *(1,5 pt)*** — Écrivez les commandes de configuration HSRP sur R-CORE (interface Gi0/0, groupe 2, avec tracking) :

```ios
R-CORE(config)# interface GigabitEthernet0/0
R-CORE(config-if)# standby _____ ip _____________
R-CORE(config-if)# standby _____ priority _____
R-CORE(config-if)# standby _____ preempt
R-CORE(config-if)# standby _____ timers _____ _____
R-CORE(config-if)# standby _____ track GigabitEthernet0/1 _____
```

---

# ═══════════════════════════════════════════
# PARTIE 2 — TD IPv6 INITIATION
# ═══════════════════════════════════════════

> *Ces exercices couvrent la notation, les types d'adresses et la configuration basique. Durée : 30 min.*

---

## I1 – Notation et Simplification (8 pts)

### I1.1 – Simplifier les adresses suivantes (4 pts)

| **Adresse complète** | **Forme simplifiée** |
|---|---|
| `2001:0db8:0000:0000:0001:0000:0000:0001` | |
| `fe80:0000:0000:0000:0000:0000:0000:0001` | |
| `0000:0000:0000:0000:0000:0000:0000:0001` | |
| `2001:0db8:1234:0000:0000:0ab0:0000:00ff` | |
| `ff02:0000:0000:0000:0000:0000:0000:0005` | |

### I1.2 – Reconstruire les adresses simplifiées (4 pts)

> Développez complètement chaque adresse (8 groupes de 4 chiffres hex) :

| **Adresse simplifiée** | **Forme complète** |
|---|---|
| `2001:db8::1` | |
| `::1` | |
| `fe80::a1b2:c3d4` | |
| `2001:db8:cafe:1::ff` | |

---

## I2 – Identification des types d'adresses (4 pts)

> Pour chaque adresse, identifiez le type (GUA / LLA / ULA / Multicast / Loopback / Non-spécifiée) et indiquez si elle est routable sur Internet :

| **Adresse** | **Type** | **Routable Internet ?** |
|---|---|---|
| `2001:41d0:a:1::1/64` | | |
| `fe80::1/64` | | |
| `::1/128` | | |
| `ff02::5` | | |
| `fd12:3456:7890::1/48` | | |
| `2001:db8::1/32` | | |
| `::` | | |

---

## I3 – Configuration IPv6 sur Cisco IOS (4 pts)

### Topologie

```
[PC-A : 2001:db8:a::10/64]           [PC-B : 2001:db8:b::10/64]
         │                                      │
     Gi0/0                                  Gi0/0
  [  R1  ]──── Gi0/1 ── 2001:db8:12::1/64 ──── Gi0/1 ─[  R2  ]
         R1 : 2001:db8:a::1/64                    R2 : 2001:db8:b::1/64
              fe80::1 (LLA)                             fe80::2 (LLA)
```

**I3.a *(2 pts)*** — Écrivez la configuration IPv6 complète de R1 (les deux interfaces Gi0/0 et Gi0/1, avec LLA manuelles fe80::1) :

```ios
R1(config)# _______________________________________________

R1(config)# interface GigabitEthernet0/0
R1(config-if)# ipv6 address _______________________________
R1(config-if)# ipv6 address _______________________________
R1(config-if)# no shutdown

R1(config)# interface GigabitEthernet0/1
R1(config-if)# ipv6 address _______________________________
R1(config-if)# ipv6 address _______________________________
R1(config-if)# no shutdown
```

**I3.b *(1 pt)*** — Quelle commande permet de voir toutes les adresses IPv6 de toutes les interfaces en une seule sortie ?

```ios
R1# _______________________________________
```

**I3.c *(1 pt)*** — Sans route statique ni OSPFv3 configuré, R1 peut-il pinger `2001:db8:b::10` (PC-B) ? Pourquoi ?

_________________________________________________________________________
_________________________________________________________________________

---

## I4 – Questions de compréhension (4 pts)

**I4.1 *(1 pt)*** — Vous êtes en train de configurer OSPFv3 (A3). Le formateur vous dit : "les hellos OSPFv3 sont envoyés depuis les LLA, pas depuis les GUA". Expliquez pourquoi cela a du sens.

_________________________________________________________________________
_________________________________________________________________________

**I4.2 *(1 pt)*** — Sur un réseau IPv6 dual-stack, une machine a `192.168.1.10` ET `2001:db8:a::10`. Quand elle contacte un serveur web qui supporte les deux versions, quelle adresse préfère généralement le système d'exploitation ? (RFC 6724)

_________________________________________________________________________

**I4.3 *(1 pt)*** — Pourquoi n'y a-t-il pas de broadcast en IPv6 ? Qu'est-ce qui le remplace et quel avantage cela apporte-t-il ?

_________________________________________________________________________
_________________________________________________________________________

**I4.4 *(1 pt)*** — En IPv6, /64 est le préfixe standard pour les LANs. Combien cela représente-t-il d'adresses hôtes disponibles ? Est-ce utile d'avoir autant pour un LAN de 50 PCs ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME TOTAL TD

| **Section** | **Points** |
|---|---|
| R1 – Adressage | /8 |
| R2 – OSPF | /6 |
| R3 – ACL | /6 |
| R4 – HSRP | /5 |
| I1 – Notation | /8 |
| I2 – Types | /4 |
| I3 – Config IOS | /4 |
| I4 – Compréhension | /4 |
| **TOTAL** | **/45** |

> *Ramené à /20 : score × 0,44*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
