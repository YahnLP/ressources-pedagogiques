# 🔧 PARCOURS DE REMÉDIATION — P1 · P2 · P3 · P4
## Adressage IPv4 · OSPF · ACL · VPN IPsec

**Nom : ________________  Parcours choisi : ___________**

> **Mode d'utilisation :** Travaillez uniquement le(s) parcours identifié(s) dans votre plan de remédiation. Chaque parcours contient 3 niveaux : A (fondamental), B (application), C (piège/expert). Commencez par A, passez à B quand A est réussi.

---

# ══════════════════════════════════════════════
# P1 — ADRESSAGE IPv4
# ══════════════════════════════════════════════

## P1-A — Calculs fondamentaux

**P1-A1.** Complétez le tableau :

| **Préfixe CIDR** | **Masque décimal** | **Wildcard** | **Hôtes max** |
|---|---|---|---|
| /24 | | | |
| /25 | | | |
| /26 | | | |
| /27 | | | |
| /28 | | | |
| /29 | | | |
| /30 | | | |

**P1-A2.** Donnez le réseau et le broadcast pour :

| **Adresse hôte** | **Réseau** | **Broadcast** |
|---|---|---|
| `172.16.10.37/27` | | |
| `10.0.4.200/26` | | |
| `192.168.5.130/25` | | |

---

## P1-B — Plan d'adressage VLSM

> Bloc disponible : `10.60.0.0/22`. Allocations requises :

| **Réseau** | **Hôtes** | **Préfixe** | **Adresse réseau** | **Broadcast** | **Plage hôtes** |
|---|---|---|---|---|---|
| LAN-PROD | 200 | | | | |
| LAN-DEV | 80 | | | | |
| LAN-DMZ | 30 | | | | |
| WAN-1 | 2 | | | | |
| WAN-2 | 2 | | | | |

**P1-B1.** Écrivez le network statement OSPF pour chacun de ces sous-réseaux (avec le wildcard correct) :

```ios
network _____________ _____________ area 0   ! LAN-PROD
network _____________ _____________ area 0   ! LAN-DEV
network _____________ _____________ area 0   ! LAN-DMZ
network _____________ _____________ area 0   ! WAN-1
```

---

## P1-C — Pièges et cas limites

**P1-C1.** `[PIÈGE AWS]` AWS réserve 5 adresses par subnet (réseau, broadcast + 3 managées). Pour un subnet qui doit loger **27 hôtes** dans AWS, quel préfixe CIDR devez-vous choisir ? Montrez le calcul.

```
Besoin réel = 27 + 5 = _____ adresses
2ⁿ ≥ _____ → n = _____ → préfixe = /_____
Nombre d'hôtes disponibles pour les VMs : _____
```

**P1-C2.** Vous avez `192.168.100.0/24`. Un collègue dit : "Je vais faire 4 sous-réseaux de taille identique." Quels sont les 4 blocs obtenus et leur préfixe ?

---

# ══════════════════════════════════════════════
# P2 — OSPF
# ══════════════════════════════════════════════

## P2-A — Network statements et wildcards

**P2-A1.** R-DIST a les interfaces suivantes. Écrivez les 4 network statements OSPF area 0 :

| **Interface** | **IP** |
|---|---|
| Gi0/0 (LAN-A) | 10.10.1.1/26 |
| Gi0/1 (LAN-B) | 10.10.1.65/27 |
| Gi0/2 (WAN-1) | 192.168.200.1/30 |
| Gi0/3 (WAN-2) | 192.168.200.5/30 |

```ios
router ospf 1
  router-id 4.4.4.4
  network _____________ _____________ area 0
  network _____________ _____________ area 0
  network _____________ _____________ area 0
  network _____________ _____________ area 0
  passive-interface _____________   ! LAN-A côté utilisateurs
  passive-interface _____________   ! LAN-B côté utilisateurs
```

---

## P2-B — Lecture de `show ip ospf neighbor`

```
R-HUB# show ip ospf neighbor

Neighbor ID  Pri  State          Dead Time  Address       Interface
1.1.1.1        1  FULL/DR        00:00:38   10.0.1.1      Gi0/0
2.2.2.2        0  FULL/DROTHER   00:00:32   10.0.1.2      Gi0/0
3.3.3.3        1  EXSTART/-      00:00:35   192.168.5.1   Gi0/1
4.4.4.4        1  FULL/-         00:00:39   172.16.0.2    Gi0/2
```

**P2-B1.** Quel routeur est DR sur le segment Gi0/0 ? Quelle est la priorité du routeur `2.2.2.2` et pourquoi ne peut-il pas être DR ?

_________________________________________

**P2-B2.** L'adjacence `3.3.3.3` est bloquée en EXSTART. Quelle est la cause la plus probable ? Quelle commande confirme votre hypothèse ?

_________________________________________

**P2-B3.** Sur Gi0/2 l'état est `FULL/-` (tiret). Pourquoi n'y a-t-il pas de DR/BDR ?

_________________________________________

---

## P2-C — OSPFv3 : le piège du router-id

**P2-C1.** Vous configurez OSPFv3 sur un routeur sans aucune interface IPv4. L'adjacence ne se forme pas. Voici la config :

```ios
ipv6 unicast-routing
ipv6 router ospf 1

interface GigabitEthernet0/0
  ipv6 address 2001:db8:1::1/64
  ipv6 ospf 1 area 0
  no shutdown
```

Identifiez le problème et corrigez-le :

_________________________________________
```ios
! Correction :
_________________________________________
```

**P2-C2.** Quelle est la différence entre les marqueurs `O` et `OI` dans `show ip route` ?

_________________________________________

---

# ══════════════════════════════════════════════
# P3 — ACL ÉTENDUES
# ══════════════════════════════════════════════

## P3-A — Syntaxe et placement

**P3-A1.** Rédigez les règles ACL pour cette politique sur le réseau `172.20.0.0/16` :

| **Règle** | **Politique** |
|---|---|
| R1 | Bloquer HTTP (80) depuis `172.20.1.0/24` vers `172.20.100.5` (SRV-WEB) |
| R2 | Autoriser HTTPS (443) depuis n'importe qui vers `172.20.100.5` |
| R3 | Bloquer Telnet (23) depuis n'importe qui vers n'importe qui |
| R4 | Tout le reste est autorisé |

```ios
ip access-list extended POLITIQUE_LAN
  remark R1
  deny   _____ _________________ _________________ _____ _________________ _____
  remark R2
  permit _____ _________________ _________________ _____ _____
  remark R3
  deny   _____ _________________ _________________ _____
  remark R4
  _______________________________________
```

**P3-A2.** Sur quelle interface et dans quelle direction appliquez-vous cette ACL si la source du trafic est le réseau `172.20.1.0/24` connecté à `Gi0/0` ?

Interface : _________, direction : _________. Commande IOS :

```ios
interface GigabitEthernet0/0
  _______________________________________
```

---

## P3-B — Diagnostic ACL

**P3-B1.** `show ip access-lists FILTRAGE` retourne :

```
Extended IP access list FILTRAGE
  10 deny tcp 10.0.0.0 0.0.0.255 host 192.168.5.10 eq 22 (248 matches)
  20 deny tcp 10.0.0.0 0.0.0.255 host 192.168.5.10 eq 23 (0 matches)
  30 permit ip 10.0.0.0 0.0.0.255 any (12453 matches)
  40 deny ip any any (0 matches)
```

**a)** La règle 20 a 0 matches après 4h. Donnez 2 interprétations possibles (l'une est normale, l'autre indique un problème) :

_________________________________________
_________________________________________

**b)** La règle 40 a 0 matches. Pourquoi est-ce logique ?

_________________________________________

---

## P3-C — Le piège du `deny implicite`

**P3-C1.** Un apprenti configure cette ACL pour bloquer SSH depuis son VLAN20 vers la DMZ :

```ios
ip access-list extended BLOCAGE_SSH
  deny tcp 192.168.20.0 0.0.0.255 192.168.100.0 0.0.0.255 eq 22

interface GigabitEthernet0/1
  ip access-group BLOCAGE_SSH in
```

Après application, les utilisateurs du VLAN20 ne peuvent plus rien faire (HTTP, DNS, tout bloqué). Expliquez le problème et corrigez :

_________________________________________
```ios
! Ligne manquante à ajouter :
_______________________________________
```

---

# ══════════════════════════════════════════════
# P4 — VPN IPSEC
# ══════════════════════════════════════════════

## P4-A — Les 5 étapes

**P4-A1.** Numérotez et nommez les 5 étapes de configuration VPN IPsec côté Cisco IOS :

1. _________________________________________ (définir le trafic à chiffrer)
2. _________________________________________ (paramètres Phase 1 IKEv1/v2)
3. _________________________________________ (clé pré-partagée + adresse du peer)
4. _________________________________________ (algorithmes Phase 2)
5. _________________________________________ (relier tout + appliquer sur interface WAN)

**P4-A2.** Écrivez la configuration minimale pour le VPN entre R-A (`WAN: 10.1.1.1`) et R-B (`WAN: 10.1.1.2`). Réseau A = `192.168.10.0/24`, Réseau B = `192.168.20.0/24`. PSK = `MON-VPN-SECRET`.

```ios
! Sur R-A :
ip access-list extended CRYPTO-RA
  permit ip _____________ _____________ _____________ _____________

crypto isakmp policy 10
  encryption aes 256
  hash sha256
  authentication pre-share
  group 14

crypto isakmp key _____________ address _____________

crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac
  mode tunnel

crypto map CMAP 10 ipsec-isakmp
  set peer _____________
  set transform-set TS
  match address _____________

interface GigabitEthernet0/1
  crypto map _____________
```

---

## P4-B — Diagnostic VPN

**P4-B1.** `show crypto isakmp sa` ne retourne rien (vide). Citez 3 causes possibles par ordre de vérification :

1. _______________________________________
2. _______________________________________
3. _______________________________________

**P4-B2.** `show crypto ipsec sa` affiche `#pkts encaps: 450, #pkts decaps: 0`. Décrivez précisément le problème et les 2 premières commandes de diagnostic :

_________________________________________
_________________________________________

---

## P4-C — Le piège de l'ACL non-miroir

**P4-C1.** R-PARIS a cette ACL crypto :

```ios
permit ip 10.100.0.0 0.0.0.255 172.20.5.0 0.0.0.255
```

L'administrateur de R-LYON a configuré ceci sur son routeur :

```ios
! ACL crypto R-LYON
permit ip 10.100.0.0 0.0.0.255 172.20.5.0 0.0.0.255
```

**a)** Quel est le problème ?

_________________________________________

**b)** Écrivez l'ACL correcte pour R-LYON :

```ios
permit ip _____________ _____________ _____________ _____________
```

**c)** `show crypto ipsec sa` sur R-PARIS après un ping `172.20.5.10` depuis `10.100.0.10` : `encaps=5, decaps=0`. Sur R-LYON : `encaps=0, decaps=5`. Ce résultat est-il cohérent avec le problème identifié ?

_________________________________________

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
