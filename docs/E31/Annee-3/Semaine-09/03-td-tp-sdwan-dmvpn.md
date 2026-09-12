# 🎯 TD + TP – S9 ANNÉE 3 – E31
## SD-WAN, VXLAN, DMVPN : Analyse, Conception, Configuration

**Nom : ________________  Prénom : ________________  Date : ________________**

---

# ═══════════════════════════════════════════
# PARTIE 1 — TD : Analyse et Conception (35 min)
# ═══════════════════════════════════════════

## TD1 — Underlay / Overlay : Classification (4 pts)

> Pour chaque élément réseau ci-dessous, indiquez s'il appartient à l'**underlay**, à l'**overlay**, ou aux **deux** — et justifiez en une phrase.

| **Élément** | **U / O / 2** | **Justification** |
|---|---|---|
| Fibre optique d'un FAI | | |
| Tunnel VPN IPsec | | |
| Switch Ethernet en agence | | |
| Politique SD-WAN "VoIP via MPLS" | | |
| Interface mGRE d'un hub DMVPN | | |
| Segment VXLAN VNI 5000 | | |
| Protocole OMP (SD-WAN Cisco) | | |
| Lien 4G d'une agence | | |

---

## TD2 — Architecture SD-WAN : Rôles des Composants (4 pts)

### Scénario

> **AgroSud** est une coopérative agricole avec 35 agences en France et 1 datacenter central. Elle veut déployer un SD-WAN Cisco. Elle a identifié les besoins suivants :
>
> 1. Chaque agence a 2 liens : fibre + 4G LTE
> 2. La VoIP doit toujours utiliser la fibre si disponible et sans perte > 0,5%
> 3. Les nouvelles agences doivent pouvoir se configurer seules (technicien non-expert)
> 4. Le responsable IT veut voir l'état de tous les liens en temps réel depuis 1 interface

**TD2.1 *(2 pts)*** — Associez chaque besoin à un composant SD-WAN :

| **Besoin** | **Composant SD-WAN** | **Justification** |
|---|---|---|
| Besoin 1 : 2 liens, sélection automatique | | |
| Besoin 2 : VoIP via fibre si SLA respecté | | |
| Besoin 3 : auto-configuration agences | | |
| Besoin 4 : tableau de bord centralisé | | |

**TD2.2 *(1 pt)*** — Pour le besoin 2, quel mécanisme SD-WAN mesure en temps réel si la fibre respecte le SLA VoIP (latence < 150 ms, perte < 0,5%) ?

_________________________________________________________________________

**TD2.3 *(1 pt)*** — Si la fibre de l'agence de Montpellier tombe soudainement, décrivez en 3 étapes ce que fait le SD-WAN pour maintenir la VoIP :

1. _______________________________________________________________________
2. _______________________________________________________________________
3. _______________________________________________________________________

---

## TD3 — VXLAN : Analyse d'un Datacenter (4 pts)

### Contexte

> **CloudDataSud** héberge 8 000 clients dans son datacenter. Chaque client a besoin d'une isolation réseau complète.

**TD3.1 *(1 pt)*** — Peut-on utiliser des VLANs 802.1Q classiques pour isoler 8 000 clients ? Justifiez avec des nombres précis.

_________________________________________________________________________
_________________________________________________________________________

**TD3.2 *(1 pt)*** — Combien de bits le VNI VXLAN utilise-t-il ? Combien de réseaux virtuels distincts cela permet-il ?

_________________________________________________________________________

**TD3.3 *(1 pt)*** — Un client dans la salle A veut communiquer avec sa VM dans la salle B (même VNI). Ces deux salles sont reliées par un réseau IP routable. Schématisez en texte les composants nécessaires :

```
[VM Client Salle A]
        │
   [________] ← encapsule la trame dans VXLAN VNI 5000
        │
   Réseau IP (L3, entre les salles)
        │
   [________] ← décapsule la trame VXLAN
        │
[VM Client Salle B]
```

*Nommez les deux équipements entre crochets :*

**TD3.4 *(1 pt)*** — Un ingénieur réseau vous dit : "VXLAN c'est juste un VLAN qui traverse Internet." Qu'est-ce qui est correct et qu'est-ce qui est imprécis dans cette affirmation ?

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

## TD4 — DMVPN : Analyse et Choix (4 pts)

**TD4.1 *(1 pt)*** — Une PME a 1 siège et 8 agences. Combien de tunnels IPsec point-à-point faudrait-il pour que toutes les agences communiquent directement entre elles (mesh complet) ?

```
Calcul : _________________________________
Nombre de tunnels : _____
```

**TD4.2 *(1 pt)*** — Avec DMVPN Phase 2, combien de configurations de tunnel le hub doit-il gérer ? Et chaque spoke ? Expliquez la différence.

_________________________________________________________________________
_________________________________________________________________________

**TD4.3 *(1 pt)*** — Dans `show ip nhrp` sur le hub DMVPN, vous voyez :

```
10.0.0.2/32 via 10.0.0.2
   Tunnel0 created 00:15:23, expire 01:44:37
   Type: dynamic, Flags: registered
   NBMA address: 203.0.113.10

10.0.0.3/32 via 10.0.0.3
   Tunnel0 created 00:08:12, expire 01:51:48
   Type: dynamic, Flags: registered
   NBMA address: 198.51.100.5
```

Que signifient les colonnes "10.0.0.x" et "NBMA address" ? Faites le lien avec les concepts DMVPN.

_________________________________________________________________________
_________________________________________________________________________

**TD4.4 *(1 pt)*** — Une entreprise a 200 agences et veut une communication directe entre elles sur Internet. Elle hésite entre DMVPN Phase 2 et SD-WAN. Quel argument décisif fait pencher vers SD-WAN ?

_________________________________________________________________________
_________________________________________________________________________

---

# ═══════════════════════════════════════════
# PARTIE 2 — TP : Configuration DMVPN Phase 1 (35 min)
# ═══════════════════════════════════════════

## Topologie

```
          INTERNET (réseau underlay simulé)
         203.0.113.0/29
         /            \
    Gi0/1              Gi0/1           Gi0/1
[R-HUB]           [R-SPOKE-1]    [R-SPOKE-2]
203.0.113.1        203.0.113.2    203.0.113.3
Tunnel: 10.0.0.1   Tunnel: 10.0.0.2  Tunnel: 10.0.0.3
    │                   │               │
  LAN-HUB          LAN-SPOKE-1    LAN-SPOKE-2
192.168.0.0/24   192.168.1.0/24  192.168.2.0/24
```

---

## TP1 — Configuration R-HUB

### Étape 1 — Interface WAN et LAN

```ios
! Interfaces déjà configurées (vérifier avec show ip int brief)
! R-HUB Gi0/1 : 203.0.113.1/29
! R-HUB Gi0/0 : 192.168.0.1/24
```

### Étape 2 — Interface Tunnel mGRE

```ios
R-HUB(config)# interface Tunnel0
R-HUB(config-if)# ip address _____________ _____________
R-HUB(config-if)# tunnel source _____________             ! Interface WAN du hub
R-HUB(config-if)# tunnel mode gre multipoint
R-HUB(config-if)# ip nhrp network-id _____________
R-HUB(config-if)# ip nhrp map multicast dynamic
R-HUB(config-if)# ip nhrp authentication CIEL2026
R-HUB(config-if)# ip mtu 1400
R-HUB(config-if)# no shutdown
```

### Étape 3 — Routage OSPF sur le hub

```ios
R-HUB(config)# router ospf 1
R-HUB(config-router)# network 10.0.0.0 0.0.0.255 area 0
R-HUB(config-router)# network 192.168.0.0 0.0.0.255 area 0
```

---

## TP2 — Configuration R-SPOKE-1 (et R-SPOKE-2 par analogie)

```ios
R-SPOKE-1(config)# interface Tunnel0
R-SPOKE-1(config-if)# ip address _____________ _____________
R-SPOKE-1(config-if)# tunnel source _____________
R-SPOKE-1(config-if)# tunnel mode gre multipoint
R-SPOKE-1(config-if)# ip nhrp network-id _____________
R-SPOKE-1(config-if)# ip nhrp authentication CIEL2026
R-SPOKE-1(config-if)# ip nhrp map 10.0.0.1 _____________    ! IP WAN du hub
R-SPOKE-1(config-if)# ip nhrp nhs _____________             ! IP tunnel du hub
R-SPOKE-1(config-if)# ip mtu 1400
R-SPOKE-1(config-if)# no shutdown

R-SPOKE-1(config)# router ospf 1
R-SPOKE-1(config-router)# network 10.0.0.0 0.0.0.255 area 0
R-SPOKE-1(config-router)# network 192.168.1.0 0.0.0.255 area 0
```

---

## TP3 — Vérifications

### 3.1 — État DMVPN

```ios
R-HUB# show dmvpn
```

**Notez l'état des tunnels :**

```
Interface: Tunnel0, IPv4 NHRP Details
Type:Hub, NHRP Peers: ____

  # Ent  Peer NBMA Addr    Peer Tunnel Add  State    UpDn Tm
  ----- ----------------  ---------------  -----  --------
    1   ___.___.___.___ → ___.___.___.___ ____     ________
    1   ___.___.___.___ → ___.___.___.___ ____     ________
```

**Q1.** Combien de spokes le hub voit-il dans `show dmvpn` ? ___________

### 3.2 — Table NHRP

```ios
R-HUB# show ip nhrp
```

**Q2.** Que représentent les entrées dans cette table ? Faites le lien avec le rôle de NHRP.

_________________________________________________________________________

### 3.3 — Table de routage

```ios
R-SPOKE-1# show ip route
```

**Q3.** R-SPOKE-1 voit-il les réseaux LAN-SPOKE-2 (192.168.2.0/24) et LAN-HUB (192.168.0.0/24) ?

_________________________________________________________________________

### 3.4 — Test de connectivité

```
PC-SPOKE-1# ping 192.168.2.10    → _______  (PC dans LAN-SPOKE-2)
PC-SPOKE-1# ping 192.168.0.10    → _______  (PC dans LAN-HUB)
```

**Q4.** En Phase 1, le trafic PC-SPOKE-1 → PC-SPOKE-2 passe-t-il directement ou via le hub ? Comment le vérifier avec un `traceroute` ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME TD + TP

| **Section** | **Points** |
|---|---|
| TD1 – Classification U/O | /4 |
| TD2 – Architecture SD-WAN | /4 |
| TD3 – VXLAN datacenter | /4 |
| TD4 – DMVPN analyse | /4 |
| TP1 – Config Hub | /3 |
| TP2 – Config Spoke-1+2 | /3 |
| TP3 – Vérifications + Q1–Q4 | /4 |
| Soin / Clarté | /2 |
| **TOTAL** | **/28** |

> *Ramené à /20 : score × 0,71*

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
