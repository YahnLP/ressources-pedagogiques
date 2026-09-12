# 📘 FICHE DE RÉFÉRENCE — S12 · 3ᵉ ANNÉE · E31
## Synthèse BGP · ACL · VPN · Firewall : Toutes les commandes essentielles

---

> **Nom** : ___________________________
> **Compétences** : S2.4 · S2.5 · S5.1 · S5.2 · S5.3 · C2.2 · C2.3

---

## 🌐 SECTION 1 — BGP : Configuration et vérification

### Configuration eBGP de base

```cisco
! Routeur en AS 100, voisin en AS 200
router bgp 100
 bgp router-id 1.1.1.1
 neighbor 10.0.12.2 remote-as 200          ← eBGP (AS différent)
 network 192.168.1.0 mask 255.255.255.0    ← Annoncer son LAN
 ! ⚠️ Le réseau DOIT être dans la table de routage IOS !

! Pour iBGP (même AS)
 neighbor 172.16.1.1 remote-as 100         ← iBGP (même AS)
 neighbor 172.16.1.1 update-source Loopback0
```

### Manipulation des attributs BGP

```cisco
! Appliquer Local-Preference (sortie de l'AS)
route-map PREFER_FAI1 permit 10
 set local-preference 200              ← Plus haut = préféré

router bgp 100
 neighbor 10.0.12.2 route-map PREFER_FAI1 in

! AS-path prepending (rendre un chemin moins attractif)
route-map DEGRADE_LIEN_B permit 10
 set as-path prepend 100 100 100       ← Ajoute l'AS 3 fois → longueur +3

! MED (suggestion d'entrée dans notre AS pour le voisin)
route-map SET_MED permit 10
 set metric 50                         ← Plus bas = préféré

router bgp 100
 neighbor 10.0.12.2 route-map SET_MED out
```

### Vérifications BGP complètes

```cisco
show bgp summary                       ← Sessions + préfixes reçus
show bgp ipv4 unicast                  ← Table BGP complète (> = best path)
show bgp ipv4 unicast 203.0.113.0/24   ← Détail d'un préfixe
show ip bgp neighbors 10.0.12.2        ← Détail d'un voisin
show ip bgp neighbors 10.0.12.2 routes ← Routes reçues de ce voisin
show ip bgp neighbors 10.0.12.2 advertised-routes ← Routes envoyées
debug ip bgp 10.0.12.2 events          ← Débogage BGP (désactiver après)
```

### Lecture de `show bgp ipv4 unicast`

```
   Network         Next Hop    Metric  LocPrf  Weight  Path
*> 192.168.1.0/24  0.0.0.0          0          32768  i  ← Réseau local
*> 203.0.113.0/24  10.0.12.2        0     150       0  200 i  ← Best (LocPrf 150)
*  203.0.113.0/24  10.0.34.1       20     100       0  300 i  ← Alternatif

* = valide (next-hop joignable)
> = meilleur chemin → installé dans la table de routage
i = appris en iBGP (sans >, non best)
```

---

## 🛡️ SECTION 2 — ACL : Standard, Étendue, Nommée

### ACL Standard (1-99, 1300-1999)

```cisco
! Filtre sur IP SOURCE uniquement
access-list 10 deny host 192.168.1.100   ← Refuser une IP précise
access-list 10 deny 192.168.1.0 0.0.0.255  ← Refuser tout un sous-réseau
access-list 10 permit any                ← Autoriser tout le reste

! Appliquer sur interface
interface GigabitEthernet0/0
 ip access-group 10 in                  ← Filtrer le trafic entrant

! Placer PRÈS de la DESTINATION
```

### ACL Étendue (100-199, 2000-2699)

```cisco
! Filtre sur src + dst + protocole + port
access-list 110 deny tcp 192.168.1.0 0.0.0.255 any eq 23   ← Bloquer Telnet
access-list 110 permit tcp 192.168.1.0 0.0.0.255 any eq 80  ← HTTP
access-list 110 permit tcp 192.168.1.0 0.0.0.255 any eq 443 ← HTTPS
access-list 110 permit icmp any any                          ← Ping
access-list 110 deny ip any any                              ← Tout bloquer (redondant avec implicite)
access-list 110 permit ip any any                            ← Autoriser tout le reste si besoin

! Appliquer
interface GigabitEthernet0/0
 ip access-group 110 in

! Placer PRÈS de la SOURCE
```

### ACL Nommée (recommandée en production)

```cisco
ip access-list extended SECURITE_LAN
 10 deny   tcp 192.168.1.0 0.0.0.255 any eq 23
 20 permit tcp 192.168.1.0 0.0.0.255 any eq 80
 30 permit tcp 192.168.1.0 0.0.0.255 any eq 443
 40 permit icmp any any
 50 permit ip any any

interface GigabitEthernet0/0
 ip access-group SECURITE_LAN in

! Avantage : modifier une règle sans réécrire toute l'ACL
ip access-list extended SECURITE_LAN
 no 10
 10 deny tcp 10.0.0.0 0.255.255.255 any eq 23
```

### Vérifications ACL

```cisco
show ip access-lists                   ← Toutes les ACL + compteurs de hits
show ip access-lists SECURITE_LAN      ← Une ACL spécifique
show run | section access-list         ← ACL dans la config
show run interface GigabitEthernet0/0  ← Voir quelle ACL est appliquée
clear ip access-list counters          ← Remettre les compteurs à 0
```

### Ports TCP/UDP courants à connaître

```
20/21 = FTP (données/contrôle)    23 = Telnet      25 = SMTP
53 = DNS (UDP)                    80 = HTTP        110 = POP3
443 = HTTPS                       3389 = RDP       8080 = HTTP alt
514 = Syslog (UDP)                22 = SSH         179 = BGP
```

---

## 🔒 SECTION 3 — VPN : GRE et IPsec

### Tunnel GRE (Generic Routing Encapsulation)

```cisco
! === R1 (site A) ===
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source GigabitEthernet0/1       ← Interface WAN de R1
 tunnel destination 203.0.113.2         ← IP WAN de R2
 no shutdown
!
! Annoncer le réseau tunnel dans le routage
router ospf 1
 network 172.16.0.0 0.0.0.3 area 0

! === R2 (site B) — configuration miroir ===
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source GigabitEthernet0/1       ← Interface WAN de R2
 tunnel destination 203.0.113.1         ← IP WAN de R1  ← INVERSÉ !
 no shutdown
```

### Vérifications GRE

```cisco
show interfaces Tunnel0                 → Doit être "up, line protocol up"
show ip route                           → Route via l'interface Tunnel0 ?
ping 172.16.0.2 source Tunnel0          → Test du tunnel
traceroute 192.168.2.10 source Tunnel0  → Trajet à travers le tunnel
```

### IPsec — configuration simplifiée (concept)

```cisco
! Phase 1 — IKE Policy
crypto isakmp policy 10
 encryption aes 256
 hash sha256
 authentication pre-share
 group 14
 lifetime 86400

! Clé pré-partagée
crypto isakmp key MonSecret address 203.0.113.2

! Phase 2 — IPsec Transform Set
crypto ipsec transform-set TS_AES esp-aes 256 esp-sha256-hmac
 mode tunnel

! Crypto Map — appliquer IPsec au trafic intéressant
crypto map VPN_MAP 10 ipsec-isakmp
 set peer 203.0.113.2
 set transform-set TS_AES
 match address ACL_TRAFIC_VPN

access-list 100 permit ip 192.168.1.0 0.0.0.255 192.168.2.0 0.0.0.255

interface GigabitEthernet0/1
 crypto map VPN_MAP

! Vérification IPsec
show crypto isakmp sa                   → Phase 1 active ?
show crypto ipsec sa                    → Phase 2 active + compteurs de paquets
```

---

## 🔥 SECTION 4 — Firewall : ZPF (Zone-Based Policy Firewall)

### Concept et règles fondamentales

```
Règle 1 : Trafic INTRA-ZONE → autorisé par défaut
Règle 2 : Trafic INTER-ZONES → REFUSÉ par défaut
Règle 3 : Interface self (routeur lui-même) → zone spéciale
Règle 4 : Interface sans zone → peut communiquer avec toutes les zones

Zones typiques :
  INSIDE  → LAN utilisateurs (zone de confiance)
  OUTSIDE → Internet (zone non fiable)
  DMZ     → Serveurs exposés (zone semi-fiable)
```

### Configuration ZPF complète

```cisco
! 1. Créer les zones de sécurité
zone security INSIDE
zone security OUTSIDE
zone security DMZ

! 2. Assigner les interfaces
interface GigabitEthernet0/0
 zone-member security INSIDE
interface GigabitEthernet0/1
 zone-member security OUTSIDE
interface GigabitEthernet0/2
 zone-member security DMZ

! 3. Class-map (identifier le trafic à inspecter)
class-map type inspect match-any TRAFIC_INTERNET
 match protocol http
 match protocol https
 match protocol dns

class-map type inspect match-any ACCES_DMZ
 match protocol http
 match protocol https

! 4. Policy-map (définir l'action)
policy-map type inspect INSIDE_TO_OUTSIDE
 class type inspect TRAFIC_INTERNET
  inspect                              ← Inspection stateful
 class class-default
  drop                                 ← Tout le reste → bloqué

policy-map type inspect OUTSIDE_TO_DMZ
 class type inspect ACCES_DMZ
  inspect
 class class-default
  drop

! 5. Zone-pairs (appliquer les politiques entre zones)
zone-pair security INSIDE_OUTSIDE source INSIDE destination OUTSIDE
 service-policy type inspect INSIDE_TO_OUTSIDE

zone-pair security OUTSIDE_DMZ source OUTSIDE destination DMZ
 service-policy type inspect OUTSIDE_TO_DMZ

! Vérifications
show zone security
show zone-pair security
show policy-map type inspect zone-pair
```

### Stateful vs Statique — Exemple concret

```
PROBLÈME AVEC ACL STATIQUE POUR DNS :
  access-list 110 permit udp any any eq 53   ← DNS → correct
  Mais on ouvre aussi les RÉPONSES entrant sur port 53 !
  Un attaquant peut forger une réponse DNS → DNS spoofing

AVEC ZPF STATEFUL (inspect) :
  Le firewall suit la connexion DNS sortante :
  "R1 a envoyé une requête DNS → la réponse DNS est autorisée"
  Les réponses DNS non sollicitées sont bloquées automatiquement
```

---

## 📌 Les 10 commandes incontournables révision S12

```cisco
! BGP
show bgp summary                       ← Sessions + états
show bgp ipv4 unicast                  ← Table BGP complète
neighbor X remote-as Y                 ← Déclarer un voisin

! ACL
show ip access-lists                   ← ACL + compteurs
ip access-list extended NOM            ← ACL nommée
ip access-group NOM in/out             ← Appliquer sur interface

! VPN / GRE
show interfaces Tunnel0                ← État du tunnel
tunnel source / tunnel destination     ← Config GRE
show crypto ipsec sa                   ← État IPsec Phase 2

! Firewall
show zone security                     ← Zones et interfaces
```

---

## ⚠️ Les 8 erreurs classiques E31 sur ces thèmes

```
BGP :
  ❌ remote-as = son propre AS (→ iBGP involontaire)
  ❌ network avec masque au lieu de wildcard
  ❌ Réseau non dans la table de routage → BGP ne l'annonce pas

ACL :
  ❌ ACL standard filtre destination → FAUX, filtre SOURCE seulement
  ❌ Oublier le permit any → tout est bloqué par l'implicite
  ❌ ACL étendue près de la destination au lieu de la source

VPN :
  ❌ tunnel destination = même IP des deux côtés (doit être inversé)
  ❌ Oublier no shutdown sur Tunnel0
```

---

*Fiche de Référence S12 — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année*
*Compétences : S2.4 · S2.5 · S5.1 · S5.2 · S5.3 · C2.2 · C2.3*
