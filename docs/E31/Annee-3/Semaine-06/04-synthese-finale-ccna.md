# 📋 SYNTHÈSE FINALE — TOUT LE PROGRAMME CCNA 200-301
## La feuille ultime · S6 · 3ᵉ année · E31

---

> **Nom** : ___________________________
> **Date de l'examen** : ___________________________

---

## 🌐 D1 — Network Fundamentals (20%)

### Sous-réseau rapide

```
Masque → Wildcard → Hôtes utilisables
/24 → 0.0.0.255    → 254
/25 → 0.0.0.127    → 126
/26 → 0.0.0.63     → 62
/27 → 0.0.0.31     → 30
/28 → 0.0.0.15     → 14
/29 → 0.0.0.7      → 6
/30 → 0.0.0.3      → 2 (liens WAN)
/32 → 0.0.0.0      → 1 (Loopback)

RFC 1918 (privées) : 10.0.0.0/8 · 172.16.0.0/12 · 192.168.0.0/16
IPv6 Link-Local : FE80::/10 · Multicast OSPF : FF02::5
```

### Ports et protocoles

```
20/21=FTP · 22=SSH · 23=Telnet · 25=SMTP · 53=DNS
67/68=DHCP · 69=TFTP(UDP) · 80=HTTP · 443=HTTPS
110=POP3 · 123=NTP(UDP) · 161=SNMP(UDP) · 514=Syslog(UDP)
179=BGP(TCP) · 1812=RADIUS auth · 1813=RADIUS acct
```

### Distances administratives

```
Connected=0 · Static=1 · OSPF=110 · RIP=120 · eBGP=20 · iBGP=200
Longest prefix match TOUJOURS prioritaire sur la DA
```

---

## 🔌 D2 — Network Access (20%)

### VLANs et trunks

```cisco
vlan 10 / name DATA
interface Gi0/1 / switchport mode access / switchport access vlan 10
interface Gi0/2 / switchport mode trunk / switchport trunk allowed vlan all
show vlan brief · show interfaces trunk
```

### EtherChannel LACP

```cisco
interface range Gi0/1-4 / channel-group 1 mode active
interface port-channel 1 / switchport mode trunk / switchport trunk allowed vlan all
port-channel load-balance src-dst-ip
show etherchannel summary → (P)=actif ✓ · (I)=stand-alone ✗ · (D)=down ✗
active+active ✓ · active+passive ✓ · passive+passive ✗ · active+on ✗
```

### STP / Portfast

```cisco
spanning-tree portfast         ! Forwarding immédiat (ports PC uniquement)
spanning-tree bpduguard enable ! Protection contre les switches non autorisés
show spanning-tree vlan 10
```

### Port Security

```cisco
switchport port-security maximum 2
switchport port-security violation restrict   ! drop silencieux + log
switchport port-security violation protect    ! drop silencieux
switchport port-security violation shutdown   ! err-disabled
! Sortir de err-disabled : shutdown → no shutdown
```

---

## 🌍 D3 — IP Connectivity (25%)

### Routage statique

```cisco
ip route 192.168.3.0 255.255.255.0 10.0.0.2   ! route normale (DA=1)
ip route 0.0.0.0 0.0.0.0 10.0.0.1             ! route par défaut
ip route 0.0.0.0 0.0.0.0 10.0.0.2 5           ! route flottante (DA=5)
```

### OSPF

```cisco
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0    ! wildcard ≠ masque !
 passive-interface Gi0/0.10               ! pas de Hello sur les LANs
show ip ospf neighbor → FULL = OK ✓
DA=110 · Hello=10s · Dead=40s · Multicast=224.0.0.5
Coût = 10⁸/bande passante · auto-cost reference-bandwidth 1000
```

### OSPFv3 Multi-AF

```cisco
ipv6 unicast-routing
router ospfv3 1
 router-id 1.1.1.1       ! Toujours format IPv4 !
 address-family ipv4 unicast
 exit-address-family
 address-family ipv6 unicast
 exit-address-family
interface Gi0/0
 ospfv3 1 ipv4 area 0 / ospfv3 1 ipv6 area 0
show ipv6 ospf neighbor  ! Next-hop = FE80:: (link-local)
```

### BGP

```cisco
router bgp 100
 bgp router-id 1.1.1.1
 neighbor 10.0.12.2 remote-as 200    ! eBGP (AS différent)
 neighbor 172.16.1.1 remote-as 100   ! iBGP (même AS)
 network 192.168.1.0 mask 255.255.255.0
show bgp summary → chiffre = Established · "Active" = KO
Local-Pref: sortie AS, + haut = préféré · AS-path: + court = préféré
MED: entrée AS voisin, + bas = préféré
```

---

## 🛠️ D4 — IP Services (10%)

### DHCP

```cisco
ip dhcp excluded-address 192.168.1.1 192.168.1.10
ip dhcp pool LAN
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.1
 dns-server 8.8.8.8
```

### NAT / PAT

```cisco
! PAT (overload)
ip nat inside source list 1 interface Gi0/0 overload
access-list 1 permit 192.168.0.0 0.0.255.255
interface Gi0/0 → ip nat outside
interface Gi0/1 → ip nat inside
```

### QoS

```cisco
class-map match-any VOIX / match dscp ef
policy-map QOS / class VOIX / priority percent 30
interface Se0/0/0 / service-policy output QOS
DSCP EF=46 (VoIP) · DSCP 0=Best Effort
```

### Syslog / NTP / SNMP

```cisco
logging 192.168.1.50            ! Serveur syslog
ntp server 192.168.1.100        ! Client NTP
snmp-server community public RO ! SNMP lecture seule
```

---

## 🛡️ D5 — Security Fundamentals (15%)

### ACL

```cisco
! Standard (filtre IP SOURCE seulement)
access-list 10 deny host 192.168.1.100
access-list 10 permit any
interface Gi0/0 / ip access-group 10 in

! Étendue (filtre src + dst + port + protocole)
access-list 110 deny tcp 10.0.0.0 0.0.0.255 any eq 23   ! Block Telnet
access-list 110 permit ip any any
! Placer les ACL étendues PRÈS de la source, standard PRÈS de la destination
```

### SSH

```cisco
hostname R1 / ip domain-name cisco.com
crypto key generate rsa modulus 2048
username admin secret Cisco123!
line vty 0 4 / login local / transport input ssh
ip ssh version 2
```

### DHCP Snooping / DAI

```cisco
ip dhcp snooping / ip dhcp snooping vlan 10
interface Gi0/0 / ip dhcp snooping trust    ! Seuls les ports de confiance
ip arp inspection vlan 10
```

### 802.1X / RADIUS

```
3 acteurs : Supplicant (PC) · Authenticator (switch/AP) · RADIUS Server
Ports : UDP 1812 (auth) · UDP 1813 (accounting)
EAP-TLS = certif client + serveur · PEAP = certif serveur seulement
```

---

## 🤖 D6 — Automation & Programmability (10%)

### SDN

```
Plan Contrôle (décide) → Centralisé dans le contrôleur
Plan Données (transmet) → Distribué dans les switches
Northbound API (vers apps) = REST/JSON
Southbound API (vers switches) = OpenFlow TCP 6633
Flow Table : match + priority + action (output/drop/controller)
Packet-In (switch→ctrl) · Flow-Mod (ctrl→switch)
```

### NFV

```
Appliance physique → VNF (VM sur hyperviseur)
Avantages : coût, rapidité, élasticité
Risque : performances limitées · SPOF hyperviseur
```

### Automatisation

```
Ansible : playbooks YAML · agentless · SSH
NETCONF/RESTCONF : configuration via XML/JSON
Cisco DNA Center : contrôleur d'entreprise Cisco
Python + requests : appels API REST
JSON : format standard des API réseau modernes
```

---

## ⚡ Top 10 commandes à avoir en mémoire

```
1. show ip route / show ipv6 route          → tables de routage
2. show ip ospf neighbor                    → adjacences (FULL ?)
3. show etherchannel summary               → état EC (SU, P, I)
4. show vlan brief                          → VLANs + ports
5. show interfaces trunk                    → trunks actifs
6. show bgp summary                         → sessions BGP
7. show policy-map interface               → QoS appliquée
8. ping [IP] source [interface]             → test E2E
9. traceroute [IP]                          → chemin exact
10. copy running-config startup-config      → sauvegarder !
```

---

## 🚨 Les 8 pièges qui coûtent des points

```
1. Masque au lieu de wildcard dans OSPF : /24=0.0.0.255 (pas 255.255.255.0)
2. Longest prefix match : /24 bat /16 bat /0 indépendamment de la DA
3. ACL standard = IP SOURCE seulement
4. "Active" dans show bgp summary = session BGP KO (pas opérationnelle)
5. passive+passive LACP = aucun EC formé
6. copy run start ≠ sauvegarde externe (tftp = la vraie sauvegarde)
7. (I) dans show etherchannel = stand-alone, hors bundle, problème
8. Router-ID OSPFv3 = toujours format IPv4 même sur réseau IPv6 pur
```

---

## 🏆 Dernier conseil

> **La différence entre 780/1000 et 825/1000, c'est souvent 4-5 questions.**
> Ces 4-5 questions se gagnent par :
> - Lire ATTENTIVEMENT chaque question (les mots "NOT", "EXCEPT", "MOST")
> - Ne pas perdre de points sur les "questions faciles" par inattention
> - Gérer son temps (pas 10 min sur 1 question difficile)
> - Répondre à TOUT (pas de pénalité pour mauvaise réponse)
>
> **Tu as le niveau. Confiance.**

---

*Synthèse Finale CCNA 200-301 — BAC PRO CIEL | E31 | 3ᵉ année S6*
*Cisco CCNA · Pearson VUE · 825/1000 pour valider*
