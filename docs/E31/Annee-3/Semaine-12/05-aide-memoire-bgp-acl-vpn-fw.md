# 🗂️ AIDE-MÉMOIRE BGP · ACL · VPN · FIREWALL — À PLASTIFIER
## Routage Avancé + Sécurité · BAC PRO CIEL · E31 · 3ᵉ année S12

---

> *Référence rapide pour les révisions et l'examen E31*

---

## 🌐 BGP — Essentiel

```cisco
router bgp 100
 bgp router-id 1.1.1.1
 neighbor 10.0.12.2 remote-as 200    ! eBGP (AS différent)
 neighbor 172.16.1.1 remote-as 100   ! iBGP (même AS)
 network 192.168.1.0 mask 255.255.255.0

show bgp summary        → chiffre=OK · Active=KO · never=jamais connecté
show bgp ipv4 unicast   → *=valide · >=best path
```

### 3 attributs clés

```
Local-Pref : sortie AS · + HAUT = préféré · propagé iBGP seul · défaut 100
AS-path    : + COURT = préféré · anti-boucle
MED        : entrée AS voisin · + BAS = préféré · défaut 0

Algorithme (ordre) : Weight > Local-Pref > Locally orig > AS-path >
                     Origin > MED > eBGP>iBGP > IGP metric > Router-ID
```

### Manipulation attributs

```cisco
! Forcer sortie via FAI1 (Local-Pref)
route-map PREFER_FAI1 permit 10
 set local-preference 200
neighbor 10.0.1.2 route-map PREFER_FAI1 in

! Dégrader un chemin (AS-path prepend)
route-map DEGRADE permit 10
 set as-path prepend 100 100 100
neighbor 10.0.2.2 route-map DEGRADE out
```

---

## 🛡️ ACL — Règles fondamentales

```
Standard (1-99) : filtre IP SOURCE uniquement → placer près DESTINATION
Étendue (100-199) : filtre src+dst+port → placer près SOURCE
Implicite : deny any en fin → toujours ajouter permit ip any any si besoin
```

```cisco
! ACL standard
access-list 10 deny 192.168.1.0 0.0.0.255
access-list 10 permit any

! ACL étendue nommée
ip access-list extended SECURITE
 deny  tcp any any eq 23         ! Bloquer Telnet
 permit tcp any any eq 80        ! HTTP
 permit tcp any any eq 443       ! HTTPS
 permit icmp any any             ! Ping
 permit ip any any               ! Reste

! Appliquer
interface Gi0/0
 ip access-group SECURITE in

show ip access-lists             ! Compteurs de hits
```

### Ports à connaître

```
22=SSH · 23=Telnet · 25=SMTP · 53=DNS · 80=HTTP
443=HTTPS · 3389=RDP · 514=Syslog · 179=BGP
```

---

## 🔒 VPN — Tunnel GRE

```cisco
! R1 (source = IP WAN R1, destination = IP WAN R2)
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source GigabitEthernet0/1   ! Interface WAN locale
 tunnel destination 203.0.113.2     ! IP WAN distante
 no shutdown

! R2 — MIROIR (source/destination inversées !)
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source GigabitEthernet0/1
 tunnel destination 203.0.113.1     ! ← IP WAN de R1
 no shutdown

show interfaces Tunnel0             ! up/up = OK
ping 172.16.0.2 source Tunnel0      ! Test tunnel
```

### GRE vs IPsec

```
GRE seul    : tunnel SANS chiffrement (visible sur Internet)
GRE + IPsec : tunnel + chiffrement AES + auth IKE
IPsec Phase 1 : IKE, authentification, négociation
IPsec Phase 2 : ESP chiffrement données réelles
show crypto isakmp sa   ! Phase 1 active ?
show crypto ipsec sa    ! Phase 2 + compteurs
```

---

## 🔥 Firewall ZPF — Règles d'or

```
INTRA-ZONE (même zone) → autorisé par défaut
INTER-ZONES sans policy → REFUSÉ par défaut

3 zones typiques : INSIDE · OUTSIDE · DMZ
```

```cisco
! Config ZPF (structure)
zone security INSIDE
zone security OUTSIDE

interface Gi0/0
 zone-member security INSIDE
interface Gi0/1
 zone-member security OUTSIDE

class-map type inspect match-any WEB
 match protocol http
 match protocol https

policy-map type inspect INSIDE_OUT
 class type inspect WEB
  inspect        ! stateful = retour autorisé auto
 class class-default
  drop

zone-pair security IN_OUT source INSIDE destination OUTSIDE
 service-policy type inspect INSIDE_OUT

show zone security         ! Zones et interfaces
show zone-pair security    ! Politiques actives
```

---

## ⚠️ 8 erreurs à ne plus faire

```
BGP :
  ❌ remote-as = son propre AS → iBGP involontaire
  ❌ network avec masque (/24=255.255.255.0) → wildcard (/24=0.0.0.255)
  ❌ Réseau non dans la table de routage → BGP ne l'annonce pas

ACL :
  ❌ ACL standard filtre destination → FAUX, seulement SOURCE
  ❌ Oublier permit any → tout bloqué par l'implicite
  ❌ ACL étendue près de la destination → doit être près de la SOURCE

VPN :
  ❌ tunnel destination identique des deux côtés → doit être INVERSÉ
  ❌ Oublier no shutdown sur Tunnel0
```

---

*Aide-Mémoire BGP · ACL · VPN · Firewall — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S12*
*Compétences S2.4 · S2.5 · S5.1 · S5.2 · S5.3*
