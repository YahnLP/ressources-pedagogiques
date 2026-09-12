# 🔧 PARCOURS DE REMÉDIATION — P5 · P6 · P7 · P8 · P9
## HSRP · Nagios · IPv6 avancé · Cloud · WAN avancé

**Nom : ________________  Parcours choisi : ___________**

---

# ══════════════════════════════════════════════
# P5 — HSRP / VRRP
# ══════════════════════════════════════════════

## P5-A — Calculs fondamentaux

**P5-A1.** Complétez le tableau pour chaque scénario :

| **R-Active prio** | **R-Standby prio** | **Tracking décrement** | **Prio après panne WAN** | **Bascule ?** |
|---|---|---|---|---|
| 110 | 100 | 20 | | |
| 150 | 100 | 60 | | |
| 120 | 100 | 15 | | |
| 130 | 110 | 25 | | |
| 100 (défaut) | 100 (défaut) | — | — | Élection par ? |

**P5-A2.** `[PIÈGE]` Pour chaque ligne du tableau, la bascule n'a lieu que si le décrement est suffisant. Quelle est la formule pour calculer le **décrement minimum** garanti ?

_________________________________________

---

## P5-B — Configuration et `show standby`

**P5-B1.** `show standby brief` sur R-MAIN :

```
Interface  Grp  Pri P State   Active   Standby          Virtual IP
Gi0/0      1    100   Active  local    10.0.1.2          10.0.1.254
```

Identifiez **deux problèmes de configuration** et écrivez les corrections :

Problème 1 : ___________________________
```ios
R-MAIN(config-if)# _______________________________________
```

Problème 2 : ___________________________
```ios
R-MAIN(config-if)# _______________________________________
```

**P5-B2.** Rédigez la configuration HSRP complète pour l'infrastructure suivante :
- LAN `10.200.0.0/24`, IP virtuelle = `10.200.0.254`, groupe 3
- R-A (Active) : prio 130, preempt, Hello=1s/Hold=3s, WAN=Gi0/2, décrement=40
- R-B (Standby) : prio 100, preempt, mêmes timers

```ios
! R-A :
interface GigabitEthernet0/0
  standby ___ ip _______________
  standby ___ priority ___
  standby ___ preempt
  standby ___ timers ___ ___
  standby ___ track GigabitEthernet0/2 ___

! R-B :
interface GigabitEthernet0/0
  [Compléter]
```

---

## P5-C — Pièges et scénarios complexes

**P5-C1.** `[PIÈGE DU HOLD TIMER]` Un formateur vous dit : "Avec des timers Hello=1s / Hold=3s, si R-A tombe, R-B devient Active en 1 seconde." A-t-il raison ? Expliquez précisément.

_________________________________________
_________________________________________

**P5-C2.** Deux routeurs affichent tous deux `State: Active` dans `show standby brief`. Quelle est la cause et quelle commande le confirme en 5 secondes ?

_________________________________________

**P5-C3.** HSRP vs VRRP : un réseau utilise des routeurs Cisco ET Juniper. Lequel choisir et pourquoi ?

_________________________________________

---

# ══════════════════════════════════════════════
# P6 — NAGIOS
# ══════════════════════════════════════════════

## P6-A — Codes retour et états

**P6-A1.** Complétez :

| **exit code** | **État Nagios** | **Couleur** | **Envoie une alerte ?** |
|---|---|---|---|
| 0 | | | |
| 1 | | | Si Hard State |
| 2 | | | |
| 3 | | | |

**P6-A2.** `[PIÈGE]` Un plugin utilise `exit 2` pour signaler "disque presque plein à 78%" et `exit 1` pour "disque critique à 92%". Qu'est-ce qui est incorrect ?

_________________________________________

---

## P6-B — Timing Soft/Hard State

**P6-B1.** Un service a `max_check_attempts=5`, `normal_check_interval=10 min`, `retry_check_interval=2 min`. Il tombe à 09h00. Tracez la chronologie :

```
09h00 + ___min : Tentative ___ → Soft (_/5)
      + ___min : Tentative ___ → Soft (_/5)
      + ___min : Tentative ___ → Soft (_/5)
      + ___min : Tentative ___ → Soft (_/5)
      + ___min : Tentative ___ → HARD → ALERTE ✅

Heure d'alerte : _______
Délai total : _____ minutes
```

**P6-B2.** Le service revient OK entre la 3ème et la 4ème tentative. Que se passe-t-il ?

_________________________________________

---

## P6-C — Plugin custom

**P6-C1.** Rédigez un plugin bash `check_cpu_load.sh` qui :
- Récupère la charge CPU via `cat /proc/loadavg | awk '{print $1}'`
- WARNING si > `$2`, CRITICAL si > `$3`
- Retourne la perf data `load=valeur;warn;crit;0;100`

```bash
#!/bin/bash
HOST=$1
WARN=$2
CRIT=$3

LOAD=$(cat /proc/loadavg | awk '{print $1}')

if [ -z "$LOAD" ]; then
    echo "_______________________________"
    exit ___
fi

# Comparaison float avec awk
if awk "BEGIN {exit !($LOAD >= $CRIT)}"; then
    echo "CPU CRITICAL - Load: $LOAD | _______________"
    exit ___
elif awk "BEGIN {exit !($LOAD >= $WARN)}"; then
    echo "_______________________________"
    exit ___
else
    echo "CPU OK - Load: $LOAD | _______________"
    exit ___
fi
```

**P6-C2.** Nommez les 2 commandes à exécuter après avoir modifié la configuration Nagios avant que les changements ne prennent effet :

```bash
1. _______________________________________
2. _______________________________________
```

---

# ══════════════════════════════════════════════
# P7 — IPv6 AVANCÉ
# ══════════════════════════════════════════════

## P7-A — EUI-64 et SLAAC

**P7-A1.** Calculez l'adresse IPv6 complète d'un hôte avec la MAC `3C:E0:72:AA:BB:CC` sur le préfixe `2001:db8:cafe:1::/64` via SLAAC. Montrez les 3 étapes EUI-64.

```
MAC : 3C:E0:72:AA:BB:CC

Étape 1 — Couper :
  ___________ | ___________

Étape 2 — Insérer FF:FE :
  ___________________________

Étape 3 — Inverser bit U/L du 1er octet :
  3C = ________ binaire → bit 6 = ___ → inverser → ___
  Résultat : ________ = ________ hex

EUI-64 final : _______________________________________________
Adresse GUA  : _______________________________________________
```

**P7-A2.** Quel mécanisme de protection de vie privée empêche d'utiliser EUI-64 comme adresse source principale ? En une phrase.

_________________________________________

---

## P7-B — DHCPv6 : Flags M et O

**P7-B1.** Pour chaque scénario, donnez les valeurs des flags M et O et la commande IOS à mettre sur l'interface :

| **Scénario** | **M** | **O** | **Commande IOS** |
|---|---|---|---|
| SLAAC pur — pas de serveur | 0 | 0 | *(rien de spécial)* |
| SLAAC + DNS via DHCPv6 | | | |
| Adresse ET DNS via DHCPv6 | | | |

**P7-B2.** Un routeur est configuré avec `ipv6 nd managed-config-flag`. Un administrateur lui demande : "Mais les hôtes n'ont plus d'adresses !" Expliquez pourquoi et ce qu'il manque dans la configuration.

_________________________________________
_________________________________________

---

## P7-C — OSPFv3 : La configuration par interface

**P7-C1.** Comparez ces deux configurations. Laquelle est correcte pour OSPFv3 ? Corrigez l'incorrecte.

```ios
! Configuration A :
ipv6 router ospf 1
  router-id 5.5.5.5
  network 2001:db8::/64 area 0

! Configuration B :
ipv6 router ospf 1
  router-id 5.5.5.5

interface GigabitEthernet0/0
  ipv6 ospf 1 area 0
```

Correcte : ___  |  Correction de l'incorrecte :

```ios
! Correction config _____ :
_______________________________________
```

**P7-C2.** Dans `show ipv6 route ospf`, le next-hop d'une route est `fe80::2`. Quel type d'adresse est `fe80::2` et pourquoi OSPFv3 utilise-t-il ce type comme next-hop ?

_________________________________________
_________________________________________

---

# ══════════════════════════════════════════════
# P8 — CLOUD NETWORKING
# ══════════════════════════════════════════════

## P8-A — VPC et types de subnets

**P8-A1.** Associez chaque configuration de route table à son type de subnet :

| **Route Table** | **Type de subnet** |
|---|---|
| `0.0.0.0/0 → igw-xxxx` | |
| `0.0.0.0/0 → nat-xxxx` | |
| Pas de route `0.0.0.0/0` | |

**P8-A2.** Une entreprise héberge ses serveurs App dans un subnet privé AWS. Les développeurs se plaignent que `apt update` ne fonctionne plus. Quel composant est probablement manquant ou mal configuré ?

_________________________________________

---

## P8-B — Security Groups : Stateful vs Stateless

**P8-B1.** `[PIÈGE]` Un développeur débutant ajoute ces règles à son Security Group :

```
Inbound  : TCP 443 from 0.0.0.0/0
Outbound : TCP 443 to 0.0.0.0/0   ← Il pense que c'est nécessaire
```

Pourquoi la règle Outbound est-elle inutile pour les réponses HTTPS ? Quelle est la règle Outbound utile ?

_________________________________________
_________________________________________

**P8-B2.** Concevez les règles inbound pour une architecture 3-tier :

| **Security Group** | **Règles inbound nécessaires** |
|---|---|
| SG-LB (Load Balancer public) | TCP 80 from _________, TCP 443 from _________, TCP 22 from _________ |
| SG-APP (Serveurs applicatifs) | TCP _____ from _________ (seulement depuis LB) |
| SG-DB (Base de données MySQL) | TCP _____ from _________ (seulement depuis App) |

---

## P8-C — VPN Cloud

**P8-C1.** Nommez les 2 composants AWS à créer pour un VPN site-à-site entre un VPC et un routeur Cisco on-premises :

1. _________________________ (côté AWS, attaché au VPC)
2. _________________________ (décrit le routeur Cisco : IP WAN + type de routage)

**P8-C2.** `[PIÈGE]` Un apprenti dit : "Le VPN AWS c'est différent du VPN IPsec d'A2, je dois réapprendre." A-t-il raison ? Expliquez.

_________________________________________
_________________________________________

---

# ══════════════════════════════════════════════
# P9 — WAN AVANCÉ
# ══════════════════════════════════════════════

## P9-A — Overlay / Underlay

**P9-A1.** Classez ces éléments en Overlay ou Underlay :

| **Élément** | **Overlay / Underlay** |
|---|---|
| Lien MPLS d'un opérateur | |
| Tunnel IPsec entre deux agences | |
| Interface mGRE d'un hub DMVPN | |
| Fibre optique en datacenter | |
| Politique SD-WAN "VoIP via MPLS" | |
| Segment VXLAN VNI 7000 | |

---

## P9-B — DMVPN : Hub et NHRP

**P9-B1.** Complétez la configuration du spoke DMVPN. Hub IP WAN = `198.51.100.1`, Hub IP tunnel = `10.0.0.1`, Spoke IP tunnel = `10.0.0.4/24`, réseau overlay `10.0.0.0/24` :

```ios
interface Tunnel0
  ip address _____________ _____________
  tunnel source GigabitEthernet0/1
  tunnel mode _____________
  ip nhrp network-id _____
  ip nhrp map _____________ _____________    ! overlay → underlay HUB
  ip nhrp nhs _____________
  ip nhrp authentication _____________
  ip mtu _____
```

**P9-B2.** `show ip nhrp nhs` retourne l'état `NE` (Not Responding / Expecting). Quelle est la cause probable et la première action de diagnostic ?

_________________________________________

---

## P9-C — SD-WAN vs DMVPN : le bon choix

**P9-C1.** Pour chaque cas d'usage, choisissez entre VPN IPsec P-à-P, DMVPN Phase 2 et SD-WAN. Justifiez en 1 phrase :

**a)** 7 agences, 1 siège, 1 seul lien WAN MPLS par agence, budget limité, tout Cisco.

Choix : _________  Justification : _________________________________________

**b)** 120 boutiques, 2 liens par boutique (fibre + 4G), VoIP déployé, besoin de dashboard centralisé.

Choix : _________  Justification : _________________________________________

**c)** 3 datacenters interconnectés, VMs qui doivent être dans le même VLAN L2 malgré la distance.

Choix : _________  (Astuce : ce n'est ni DMVPN ni SD-WAN)  Justification : _____
_________________________________________

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
