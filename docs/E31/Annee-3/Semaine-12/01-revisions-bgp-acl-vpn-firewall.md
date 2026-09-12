# 📋 RÉVISIONS STRUCTURÉES — S12 · 3ᵉ ANNÉE · E31
## BGP · ACL · VPN · Firewall : Exercices et Fiches de Révision

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Utilisation** : séance S12 + révisions personnelles avant E31

---

## ⚡ QCM DIAGNOSTIC — 10 questions (15 min)

> À remplir EN PREMIER sans fiche de cours.

**D1** — Dans BGP, `neighbor 10.0.12.2 remote-as 200` sur un routeur en AS 100 configure :

```
A) Une session iBGP    B) Une session eBGP    C) Une route statique
```
___

**D2** — Quelle ACL filtre uniquement sur l'adresse IP **source** ?

```
A) ACL standard (1-99)    B) ACL étendue (100-199)    C) Les deux
```
___

**D3** — Dans `show bgp summary`, "Active" dans la colonne State signifie :

```
A) Session BGP opérationnelle    B) Session BGP en tentative (non établie)    C) Routeur actif
```
___

**D4** — Quelle commande bloque Telnet (port 23) en entrée sur Gi0/0 ?

```
A) access-list 10 deny tcp any any eq 23 / ip access-group 10 in
B) access-list 110 deny tcp any any eq 23 / ip access-group 110 in
C) access-list 10 deny host 23 / ip access-group 10 in
```
___

**D5** — Un tunnel GRE nécessite sur chaque extrémité :

```
A) tunnel source [IP locale] + tunnel destination [IP distante]
B) tunnel source [IP distante] + tunnel destination [IP locale]
C) Une seule commande suffit
```
___

**D6** — Dans l'attribut BGP Local-Preference, quelle valeur est préférée ?

```
A) La plus basse    B) La plus haute    C) La valeur par défaut (100) est toujours choisie
```
___

**D7** — Où placer une ACL étendue pour être la plus efficace ?

```
A) Près de la DESTINATION    B) Près de la SOURCE    C) N'importe où (le résultat est identique)
```
___

**D8** — Dans ZPF (Zone-based Firewall), le trafic entre deux zones sans policy-map est :

```
A) Autorisé    B) Refusé    C) Inspecté mais autorisé
```
___

**D9** — Quelle est la différence entre GRE et IPsec ?

```
A) GRE chiffre les données, IPsec tunnelise
B) GRE tunnelise sans chiffrement, IPsec chiffre et authentifie
C) Ils sont identiques, juste des noms différents
```
___

**D10** — Quelle est la distance administrative d'eBGP ?

```
A) 20    B) 110    C) 200    D) 1
```
___

**Score diagnostic : _____ / 10**

---

## 📚 BLOC 1 — BGP Avancé

### 1.1 — Rappel express des attributs

```
┌─────────────────────────────────────────────────────────────────────┐
│ Attribut     │ Priorité │ Règle       │ Portée        │ Défaut     │
├─────────────────────────────────────────────────────────────────────┤
│ Weight       │    1     │ + haut ✓   │ Local router   │ 32768 (loc)│
│ Local-Pref   │    2     │ + haut ✓   │ AS entier (iBGP)│ 100       │
│ Locally orig │    3     │ Préféré     │ —              │ —          │
│ AS-path      │    4     │ + court ✓  │ Tout           │ vide       │
│ Origin       │    5     │ i>e>?       │ Tout           │ ?          │
│ MED          │    6     │ + bas ✓    │ AS voisin direct│ 0         │
│ eBGP > iBGP  │    7     │ eBGP pref. │ —              │ —          │
│ IGP metric   │    8     │ + bas ✓    │ Local          │ —          │
│ Router-ID    │    9     │ + bas ✓    │ Dernier recours│ —          │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 — Exercice : Sélection du chemin BGP

> Un routeur reçoit 3 chemins pour `203.0.113.0/24` :

```
Chemin A : via AS300  · AS-path="300"        · Local-Pref=100 · MED=50
Chemin B : via AS400  · AS-path="400 300"    · Local-Pref=150 · MED=0
Chemin C : via AS500  · AS-path="500 300"    · Local-Pref=150 · MED=10
```

**Q1.2a** — Quel chemin BGP sélectionne-t-il ? Justifie étape par étape :

```
Étape 1 (Weight) : tous identiques → continuer
Étape 2 (Local-Pref) :
  Chemin A : LocPrf = _____  Chemin B : LocPrf = _____  Chemin C : LocPrf = _____
  Chemin(s) éliminé(s) : _____  Car : _____
  Chemins restants : _____ et _____

Étape 3-4 (AS-path) — si nécessaire :
  Chemin B longueur = _____  Chemin C longueur = _____
  Éliminé : _____  Raison : _____

CHEMIN GAGNANT : _____
```

**Q1.2b** — Si l'admin veut forcer le chemin A, quel attribut doit-il modifier et comment ?

```
Attribut à modifier : _____________________
Nouvelle valeur pour chemin A : _____  (vs _____ pour B et C)
Commande route-map (complète) :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

### 1.3 — Analyser une sortie `show bgp summary`

```
BGP router identifier 5.5.5.5, local AS number 64512

Neighbor        V    AS     MsgRcvd  MsgSent  TblVer  Up/Down    State/PfxRcd
10.0.12.1       4   3215     12045    12041      89    3d14h          8234
198.51.100.2    4   5511       234      231      89    00:45:12         127
172.16.1.1      4  64512       445      442      89    01:22:33          48
10.0.99.5       4   9999         0        0       0    never         Active
```

**Q1.3a** — Identifie le type de chaque session (eBGP/iBGP) :

| Voisin | Type | Justification |
|---|---|---|
| 10.0.12.1 | | |
| 198.51.100.2 | | |
| 172.16.1.1 | | |
| 10.0.99.5 | | |

**Q1.3b** — Que signifie "never" dans la colonne Up/Down pour 10.0.99.5 ?

```
___________________________________________________________________________
```

**Q1.3c** — Liste 3 causes possibles pour l'état "Active" de 10.0.99.5 :

```
Cause 1 : ___________________________________________________________________
Cause 2 : ___________________________________________________________________
Cause 3 : ___________________________________________________________________
```

---

## 📚 BLOC 2 — ACL Standard et Étendue

### 2.1 — Rappel des règles de placement

```
ACL STANDARD (filtre IP SOURCE) :
  → Placer PRÈS de la DESTINATION
  Raison : l'ACL standard ne peut pas filtrer par destination → si on la place près
           de la source, on risque de bloquer le trafic vers d'autres destinations

ACL ÉTENDUE (filtre src + dst + port + protocole) :
  → Placer PRÈS de la SOURCE
  Raison : bloque le trafic le plus tôt possible → évite de charger inutilement
           les liens intermédiaires

DIRECTION :
  in  = filtre le trafic ENTRANT sur l'interface
  out = filtre le trafic SORTANT de l'interface

DENY IMPLICITE : toute ACL se termine par "deny any" implicite
  → Toujours ajouter "permit ip any any" si besoin de tout laisser passer
```

### 2.2 — Exercice ACL étendue

> **Scénario** : R1 connecte LAN-A (192.168.1.0/24) à Internet (Gi0/1). Tu veux :
> 1. Bloquer **tout** Telnet (port 23) depuis LAN-A
> 2. Autoriser **seulement** HTTP (80) et HTTPS (443) vers Internet depuis LAN-A
> 3. Permettre le ping (ICMP) entre LAN-A et Internet

**Q2.2a** — Écris l'ACL étendue nommée "SORTIE_LAN_A" :

```cisco
! ACL étendue nommée - FICHIER ip access-list extended SORTIE_LAN_A
ip access-list extended SORTIE_LAN_A
  ! Règle 1 : Bloquer Telnet sortant
  _________________________________________________________________________
  ! Règle 2 : Autoriser HTTP
  _________________________________________________________________________
  ! Règle 3 : Autoriser HTTPS
  _________________________________________________________________________
  ! Règle 4 : Autoriser ICMP
  _________________________________________________________________________
  ! Règle 5 : Bloquer tout le reste
  _________________________________________________________________________
```

**Q2.2b** — Sur quelle interface et dans quelle direction appliquer cette ACL pour être optimal ?

```
Interface : ________________________  Direction : __________
Commande d'application :
___________________________________________________________________________
```

**Q2.2c** — Quelle commande vérifie le nombre de hits (paquets filtrés) par règle ?

```
Commande : _________________________________________________________________
```

### 2.3 — Dépannage : trouver le problème

```
Un admin se plaint : "les utilisateurs de LAN-A ne peuvent pas accéder au serveur web
192.168.5.10 (port 80) mais peuvent pinguer n'importe où."

ACL configurée :
  access-list 110 permit tcp 192.168.1.0 0.0.0.255 host 192.168.5.10 eq 443
  access-list 110 permit icmp any any
  (appliquée in sur Gi0/0)
```

**Q2.3** — Identifie le problème et propose la correction :

```
Problème : __________________________________________________________________
La règle manquante : _________________________________________________________
Commande de correction :
___________________________________________________________________________
```

---

## 📚 BLOC 3 — VPN Site-à-Site : GRE + IPsec

### 3.1 — Architecture VPN site-à-site

```
SITE A ─── [R1] ════ INTERNET ════ [R2] ─── SITE B
           │          Tunnel GRE          │
           │    (ou GRE over IPsec)       │
           10.1.0.1                  10.1.0.2
                 Réseau tunnel : 172.16.0.0/30
```

### 3.2 — Configuration tunnel GRE (révision)

```cisco
! Sur R1
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source GigabitEthernet0/0      ← Interface WAN de R1
 tunnel destination [IP WAN de R2]     ← IP publique de R2
 no shutdown

! Sur R2 (miroir)
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source GigabitEthernet0/0      ← Interface WAN de R2
 tunnel destination [IP WAN de R1]     ← IP publique de R1
 no shutdown

! Vérification
show interfaces Tunnel0                → doit être up/up
ping 172.16.0.2 source Tunnel0         → doit fonctionner
```

> ⚠️ **Erreur classique** : confondre source et destination. Sur R1, la **source** est l'IP WAN de R1, la **destination** est l'IP WAN de R2. Sur R2, c'est l'inverse.

### 3.3 — IPsec : les concepts clés

```
GRE seul    : tunnel sans chiffrement → paquets lisibles sur Internet
GRE + IPsec : tunnel + chiffrement → protection de la confidentialité

IPsec en deux phases :
  Phase 1 (IKE) : Authentification mutuelle + négociation des paramètres
    → Mode Main (plus lent, plus sécurisé) ou Aggressive (plus rapide)
    → Algorithmes : AES-256, SHA-256, DH group 14+
    
  Phase 2 (IPsec SA) : Chiffrement des données réelles
    → ESP (Encapsulating Security Payload) → chiffrement + authentification
    → AH (Authentication Header) → authentification seulement (pas de chiffrement)
```

### 3.4 — Exercice : diagnostiquer un tunnel GRE défaillant

```
R1# show interfaces Tunnel0
Tunnel0 is up, line protocol is down

R1# ping 172.16.0.2
.....
Success rate is 0 percent
```

**Q3.4** — Analyse ce symptôme (`up/down`) et propose les étapes de diagnostic :

```
"up, line protocol is down" signifie :
  Plan physique : ____________________________________________________________
  Plan logique  : ____________________________________________________________

Cause la plus probable : _____________________________________________________
Vérification 1 : ____________________________________________________________
Vérification 2 : ____________________________________________________________
Commande pour voir l'état détaillé du tunnel : ________________________________
```

### 3.5 — GRE vs IPsec vs SSL VPN

```
Complète le tableau comparatif :

             GRE          IPsec site-to-site    SSL/TLS (VPN client)
Chiffrement  Non          _________________     Oui (TLS)
Authentif.   Non          _________________     Oui (cert. ou PSK)
Usage        Tunnel multi-protocole            ___________________________
Config       Simple       ________________     Agent VPN sur le client
Protocole    IP proto 47  _________________    TCP port 443
```

---

## 📚 BLOC 4 — Firewall : Zone-Based Policy Firewall (ZPF)

### 4.1 — Concept ZPF

```
RÉSEAU TRADITIONNEL : ACL par interface — statique, complexe à maintenir
ZONE-BASED FIREWALL : grouper les interfaces en zones, définir des politiques entre zones

Principe :
  → Chaque interface est assignée à UNE zone
  → Le trafic INTRA-ZONE (même zone) est autorisé par défaut
  → Le trafic INTER-ZONES est REFUSÉ par défaut
  → Une policy-map définit ce qui est autorisé entre zones

Zones typiques :
  Inside (réseau interne)
  Outside (Internet)
  DMZ (serveurs publics)
```

### 4.2 — Inspection stateful vs ACL statique

```
ACL STATIQUE :
  → Filtre chaque paquet indépendamment
  → Problème : doit autoriser explicitement le trafic de RETOUR
  Exemple : autoriser DNS (UDP 53) → doit aussi autoriser les réponses UDP src 53

STATEFUL INSPECTION (ZPF, inspect) :
  → Suivi des connexions dans une table d'état
  → Le trafic de retour est autorisé automatiquement
  → Bien plus sécurisé et plus simple à maintenir
```

### 4.3 — Configuration ZPF simplifiée (concept)

```cisco
! Étape 1 : Créer les zones
zone security INSIDE
zone security OUTSIDE

! Étape 2 : Assigner les interfaces aux zones
interface GigabitEthernet0/0
 zone-member security INSIDE

interface GigabitEthernet0/1
 zone-member security OUTSIDE

! Étape 3 : Créer la class-map (ce qui est inspecté)
class-map type inspect match-any TRAFIC_AUTORISE
 match protocol http
 match protocol https
 match protocol dns

! Étape 4 : Créer la policy-map (action)
policy-map type inspect POLITIQUE_INSIDE_OUTSIDE
 class type inspect TRAFIC_AUTORISE
  inspect

! Étape 5 : Créer le zone-pair et appliquer la politique
zone-pair security INSIDE_TO_OUTSIDE source INSIDE destination OUTSIDE
 service-policy type inspect POLITIQUE_INSIDE_OUTSIDE
```

### 4.4 — Exercice ZPF : compléter le schéma

> **Topologie** : Un routeur avec 3 interfaces : LAN (Gi0/0), WAN/Internet (Gi0/1), DMZ serveur web (Gi0/2)

**Q4.4** — Complète le tableau des autorisations de flux :

| Zone source | Zone destination | Trafic autorisé | Trafic refusé | Raison |
|---|---|---|---|---|
| INSIDE | OUTSIDE | HTTP, HTTPS, DNS | Telnet, FTP brut | Navigation web + sécurité |
| OUTSIDE | INSIDE | | Tout le reste | |
| INSIDE | DMZ | | | |
| OUTSIDE | DMZ | | Tout accès admin | |
| DMZ | INSIDE | | | Cloisonnement DMZ |

---

## 📊 Auto-évaluation finale

### Score par domaine

```
BGP          : /20  → ___% → ☐ Acquis ☐ À retravailler
ACL          : /20  → ___% → ☐ Acquis ☐ À retravailler
VPN/GRE      : /20  → ___% → ☐ Acquis ☐ À retravailler
Firewall ZPF : /20  → ___% → ☐ Acquis ☐ À retravailler
QCM Initial  : /10  → ___% → ☐ Acquis ☐ À retravailler
```

### Erreurs à ne plus faire

```
Mes 3 erreurs principales identifiées aujourd'hui :
1. ___________________________________________________________________________
2. ___________________________________________________________________________
3. ___________________________________________________________________________
```

---

## ✅ Correction QCM Diagnostic

| Q | Rép | Justification |
|---|---|---|
| D1 | B | AS 100 ≠ AS 200 → eBGP |
| D2 | A | ACL standard = IP source uniquement |
| D3 | B | Active = session TCP en tentative, pas établie |
| D4 | B | Telnet = TCP port 23 → ACL étendue (100-199) obligatoire |
| D5 | A | source=IP locale, destination=IP distante |
| D6 | B | Local-Pref : + haute = préférée |
| D7 | B | ACL étendue : près de la source |
| D8 | B | ZPF inter-zone : refusé par défaut sans policy-map |
| D9 | B | GRE = tunnel sans chiffrement, IPsec = chiffrement |
| D10 | A | eBGP DA = 20 (iBGP = 200) |

---

*Révisions Structurées S12 — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année*
*Compétences : S2.4 · S2.5 · S5.1 · S5.2 · S5.3 · C2.2 · C2.3*
