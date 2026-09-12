# 📘 GUIDE TECHNIQUE — S16 · 2ᵉ ANNÉE · E31 · PROJET A2
## OSPF Multi-aires · Tunnel GRE · Haute Disponibilité · QoS LLQ VoIP

---

> **Document de référence technique pour le projet A2**
> Utiliser comme aide-mémoire pendant la configuration
> **Compétences** : C2.1 · C2.2 · S2.2 · S3.3 · S3.4

---

## 1️⃣ — OSPF Multi-aires : Architecture et configuration

### Concept des aires OSPF dans ce projet

```
┌─────────────────────────────────────────────────────────┐
│                      AREA 0 (Backbone)                   │
│                                                          │
│    R_SIEGE ──────── 10.1.4.0/30 ──────── R_DC           │
│       │                                                  │
│    R_SIEGE_BACKUP (aussi dans Area 0)                    │
└────────────────────────┬────────────────────────────────┘
                         │ ABR : R_SIEGE
              ┌──────────┴──────────┐
              │       AREA 1        │
              │    R_AGENCE_B       │
              │    192.168.50.0/24  │
              └─────────────────────┘
```

### Configuration OSPF — R_SIEGE (ABR Area 0 + Area 1)

```cisco
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
router ospf 1
 router-id 1.1.1.1
 ! Réseau vers R_DC
 network 10.1.4.0 0.0.0.3 area 0
 ! Réseau vers R_AGENCE_B (WAN principal)
 network 10.1.2.0 0.0.0.3 area 1
 ! VLANs locaux du Siège
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.20.0 0.0.0.255 area 0
 network 192.168.30.0 0.0.0.255 area 0
 ! Ne pas envoyer Hello sur les LANs (économie)
 passive-interface GigabitEthernet0/0.10
 passive-interface GigabitEthernet0/0.20
 passive-interface GigabitEthernet0/0.30
```

### Configuration OSPF — R_DC (Area 0)

```cisco
interface Loopback0
 ip address 4.4.4.4 255.255.255.255
!
router ospf 1
 router-id 4.4.4.4
 network 10.1.4.0 0.0.0.3 area 0
 network 192.168.200.0 0.0.0.255 area 0
 passive-interface GigabitEthernet0/0
```

### Configuration OSPF — R_AGENCE_B (Area 1)

```cisco
interface Loopback0
 ip address 2.2.2.2 255.255.255.255
!
router ospf 1
 router-id 2.2.2.2
 ! Lien WAN principal (Area 1)
 network 10.1.2.0 0.0.0.3 area 1
 ! LAN Agence B
 network 192.168.50.0 0.0.0.255 area 1
 passive-interface GigabitEthernet0/0
```

### Vérifications OSPF essentielles

```cisco
show ip ospf neighbor
! Attendu : FULL entre tous les voisins adjacents

show ip route
! Sur R_SIEGE : routes O et O IA vers 192.168.50.0 et 192.168.200.0
! Sur R_AGENCE_B : routes O IA vers 192.168.10.0, .20.0, .30.0, .200.0

show ip ospf database
! LSDB identique sur tous les routeurs de la même aire
```

> ⚠️ **Rappel wildcard** : /24 → `0.0.0.255` · /30 → `0.0.0.3` · /32 → `0.0.0.0`

---

**🖼️ ILLUSTRATION 1**
> *Légende* : Schéma d'architecture OSPF du projet A2 en 3 zones colorées. Zone centrale bleue "Area 0 / Backbone" : R_SIEGE (avec sa Loopback 1.1.1.1), R_DC (Loopback 4.4.4.4), R_SIEGE_BACKUP. Les réseaux WAN et VLANs du siège sont annotés. Zone verte droite "Area 1" : R_AGENCE_B (Loopback 2.2.2.2), réseau 192.168.50.0/24. R_SIEGE est marqué "ABR" à la frontière entre Area 0 et Area 1. Les liens WAN sont nommés avec leurs réseaux /30. Les codes O vs O IA sont indiqués dans les mini-tables de routage de chaque routeur.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 2️⃣ — Haute disponibilité WAN : Route flottante

### Principe

```
État normal :
  R_AGENCE_B utilise la route par défaut S* via WAN principal (10.1.2.1)
  Route secours : présente mais inactive (DA = 5, non utilisée car principale DA = 1)

Si WAN principal tombe (lien serie down) :
  Route principale disparaît de la table → route secours (DA=5) prend le relais
  Trafic redirigé automatiquement via 10.1.3.1 (R_SIEGE_BACKUP)
  Délai : quelques secondes (détection de la panne physique)
```

### Configuration sur R_AGENCE_B

```cisco
! Route principale (distance admin par défaut = 1)
ip route 0.0.0.0 0.0.0.0 10.1.2.1

! Route flottante (distance admin = 5 — ne s'active QUE si la principale disparaît)
ip route 0.0.0.0 0.0.0.0 10.1.3.1 5
```

### Configuration symétrique sur R_SIEGE_BACKUP

```cisco
! Retour du trafic vers l'Agence B via le lien secours
ip route 192.168.50.0 255.255.255.0 10.1.3.2

! OSPF ou route statique pour rediriger vers les VLANs du Siège
router ospf 1
 network 10.1.3.0 0.0.0.3 area 1
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.20.0 0.0.0.255 area 0
```

### Tester la haute disponibilité

```cisco
! Sur R_SIEGE : simuler la panne du WAN principal
interface Serial0/0/0
 shutdown

! Sur R_AGENCE_B : vérifier que la route secours est active
show ip route
! La route via 10.1.3.1 doit maintenant être visible

! Tester la continuité
ping 192.168.10.10 source 192.168.50.10
```

---

## 3️⃣ — Tunnel VPN GRE (site-à-site)

### Concept du tunnel GRE

```
Sans tunnel :                    Avec tunnel GRE :
  Paquet IP circule en clair       Paquet IP original est encapsulé
  dans un paquet GRE
  Visible sur le WAN                Invisible de l'extérieur
                                   Tunnel vu comme un lien point-à-point
```

### Configuration côté R_SIEGE

```cisco
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source Serial0/0/0      ! Interface physique WAN
 tunnel destination 10.1.2.2    ! IP distante de R_AGENCE_B
 no shutdown
!
! Annoncer le réseau du tunnel dans OSPF (optionnel)
router ospf 1
 network 172.16.0.0 0.0.0.3 area 0
```

### Configuration côté R_AGENCE_B

```cisco
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source Serial0/0/0
 tunnel destination 10.1.2.1
 no shutdown
```

### Vérification du tunnel

```cisco
show interfaces Tunnel0
! Attendu : Tunnel0 is up, line protocol is up

ping 172.16.0.2 source 172.16.0.1
! Test de la connectivité dans le tunnel
```

> 💡 **Note Packet Tracer** : PT implémente GRE basique. L'encapsulation IPsec (chiffrement) est limitée dans PT — se concentrer sur la configuration GRE et mentionner IPsec dans la documentation.

---

## 4️⃣ — QoS VoIP : Low Latency Queue (LLQ)

### Pourquoi LLQ pour la VoIP ?

```
VoIP nécessite :
  Délai < 150 ms (one-way) — sensible à la latence
  Gigue < 30 ms             — sensible aux variations de délai
  Perte < 1%                — tolérance zéro aux coupures

FIFO (sans QoS) : les paquets VoIP attendent derrière des gros fichiers FTP
LLQ              : les paquets VoIP passent TOUJOURS en tête de file
```

### Architecture MQC complète

```cisco
! Étape 1 : Identifier le trafic VoIP
class-map match-any VOIX
 match dscp ef
 match protocol rtp

class-map match-any SIGNALISATION
 match dscp cs3

! Étape 2 : Définir la politique
policy-map QOS_WAN
 class VOIX
  priority percent 30    ! LLQ — garanti 30% en priorité stricte
 class SIGNALISATION
  bandwidth percent 5    ! Bande passante garantie pour SIP/H.323
 class class-default
  fair-queue             ! Partage équitable pour le reste

! Étape 3 : Appliquer sur le lien WAN (sortie uniquement)
interface Serial0/0/0
 service-policy output QOS_WAN
```

### Marquage DSCP sur les téléphones IP

```cisco
! Sur le switch vers les téléphones — marquer le trafic VoIP en DSCP EF
mls qos
interface GigabitEthernet0/1   ! Port du téléphone IP
 mls qos trust dscp
 switchport voice vlan 20
```

### Vérification QoS

```cisco
show policy-map interface Serial0/0/0
! Voir les compteurs de paquets par classe (packets/bytes matched)

show policy-map
! Vue d'ensemble des policy-maps configurées
```

---

**🖼️ ILLUSTRATION 2**
> *Légende* : Schéma de flux QoS sur le lien WAN entre R_SIEGE et R_AGENCE_B. À gauche, 3 types de trafic entrants (VoIP DSCP EF en rouge, signalisation SIP en orange, données HTTP/FTP en bleu). Au centre, la boîte "Policy-map QOS_WAN" avec 3 files distinctes : file prioritaire "VOIX 30%" (en rouge, sort en premier), file "SIGNALISATION 5%", file "class-default fair-queue". À droite, le lien série avec les flux sortants dans l'ordre de priorité. Les pourcentages de bande passante sont annotés.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 5️⃣ — EtherChannel LACP au cœur du Siège

### Topologie switches Siège

```
SW_DIST_A1 ═══(Po1 - 2 liens LACP)═══ SW_CORE_A
SW_DIST_A2 ═══(Po2 - 2 liens LACP)═══ SW_CORE_A
```

### Configuration SW_CORE_A

```cisco
! Agrégation vers SW_DIST_A1 (groupe 1)
interface range GigabitEthernet0/1-2
 channel-group 1 mode active
 exit

interface port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 exit

! Agrégation vers SW_DIST_A2 (groupe 2)
interface range GigabitEthernet0/3-4
 channel-group 2 mode active
 exit

interface port-channel 2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

### Configuration SW_DIST_A1 (et A2 de façon symétrique)

```cisco
interface range GigabitEthernet0/1-2
 channel-group 1 mode active
 exit

interface port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30

! Ports accès utilisateurs
interface GigabitEthernet0/10
 switchport mode access
 switchport access vlan 10

interface GigabitEthernet0/11
 switchport voice vlan 20
 switchport mode access
 switchport access vlan 10
 mls qos trust dscp
```

---

## 6️⃣ — Inter-VLAN Routing au Siège (Router-on-a-stick)

```cisco
! Sur R_SIEGE — sous-interfaces vers SW_CORE_A
interface GigabitEthernet0/0
 no shutdown
!
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
interface GigabitEthernet0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
```

---

## 📌 Récapitulatif des vérifications finales

```
Test 1 — OSPF convergé :
  show ip ospf neighbor → FULL sur tous les routeurs

Test 2 — Routage complet :
  show ip route sur R_SIEGE → C, O, O IA pour tous les sites

Test 3 — EtherChannel opérationnel :
  show etherchannel summary → Po1/Po2 en SU, ports en (P)

Test 4 — Tunnel VPN actif :
  show interfaces Tunnel0 → up/up

Test 5 — QoS appliquée :
  show policy-map interface Se0/0/0 → classes VOIX avec compteurs

Test 6 — Haute disponibilité :
  shutdown WAN principal → ping reprend via WAN secours

Test 7 — Ping end-to-end :
  PC_Siege VLAN 10 → PC_Agence_B → SRV_Web DC → IP_Phone → SRV_VoIP
```

---

*Guide Technique Projet A2 — BAC PRO CIEL | E31 | 2ᵉ année S16*
*Compétences : C2.1 · C2.2 · S2.2 · S3.3 · S3.4*
