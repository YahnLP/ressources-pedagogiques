# 📋 SUJET ANNALE — SUJET 1 · S14 · 3ᵉ ANNÉE · E31
## Épreuve Blanche E31 : Infrastructure Multi-sites DELTACOM

---

> **⏱️ Durée : 80 minutes · Conditions d'examen · SILENCE**
> **Autorisé** : calculatrice, Packet Tracer · **Interdit** : fiches, Internet, aide extérieure
> **Fichier PT** : `S14_Annale_Sujet1_DEPART.pkt`
> **Nom** : ___________________________ **Groupe** : ___________________________

---

## 📋 Mise en situation

> **DELTACOM SA** est une entreprise de services numériques.
> Elle vient de fusionner avec ALPHANET pour créer une entité commune.
> Vous êtes en charge du déploiement de la nouvelle infrastructure réseau
> qui doit interconnecter les deux sites historiques et assurer les services essentiels.

---

## PARTIE A — Analyse et préparation (30 min) · /30

### A1 — Plan d'adressage (12 pts)

> L'entreprise dispose du bloc **172.20.0.0/16**. Le DSI a défini les besoins suivants :

| Réseau | Utilisation | Hôtes nécessaires |
|---|---|---|
| LAN Siège — VLAN 10 | Postes employés (60 postes) | ≥ 60 |
| LAN Siège — VLAN 20 | VoIP (40 téléphones) | ≥ 40 |
| LAN Siège — VLAN 30 | Management switches | ≥ 10 |
| LAN Agence | Postes agence (25 postes) | ≥ 25 |
| WAN Siège ↔ Agence | Lien point-à-point | 2 |
| Loopbacks routeurs | Router-IDs OSPF | 1 chacun |

**A1.a** — Pour chaque réseau, propose le sous-réseau le plus petit possible issu de 172.20.0.0/16.
Complète le tableau :

| Réseau | Sous-réseau proposé | Masque | Plage d'hôtes | Broadcast |
|---|---|---|---|---|
| VLAN 10 — Postes | | | | |
| VLAN 20 — VoIP | | | | |
| VLAN 30 — Management | | | | |
| LAN Agence | | | | |
| WAN Siège↔Agence | | | | |
| Loopback R_SIEGE | 172.20.255.1/32 | /32 | 172.20.255.1 | — |
| Loopback R_AGENCE | 172.20.255.2/32 | /32 | 172.20.255.2 | — |

**A1.b** — Le bloc 172.20.0.0/16 est-il suffisant pour contenir tous ces sous-réseaux ?
Justifie brièvement :

```
Espace total : 172.20.0.0/16 = __________ adresses
Espace utilisé (somme des sous-réseaux) : __________
Suffisant ? ☐ Oui ☐ Non — Justification : ______________________________
```

### A2 — Analyse d'une configuration OSPF (10 pts)

> Voici un extrait de configuration relevé sur R_SIEGE :

```
router ospf 1
 router-id 172.20.255.1
 network 172.20.10.0 255.255.255.0 area 0
 network 172.20.20.0 255.255.255.192 area 0
 network 172.20.100.0 255.255.255.252 area 1
```

**A2.a** — Identifie **2 erreurs** dans cette configuration OSPF et propose la correction :

```
Erreur 1 :
  Ligne concernée : __________________________________________________________
  Problème : _________________________________________________________________
  Correction : _______________________________________________________________

Erreur 2 :
  Ligne concernée : __________________________________________________________
  Problème : _________________________________________________________________
  Correction : _______________________________________________________________
```

**A2.b** — Le réseau WAN (`172.20.100.0/30`) est placé dans l'area 1 mais R_SIEGE est le seul routeur
dans l'area 0. Est-ce cohérent pour une architecture OSPF multi-aire ? Explique :

```
☐ Oui ☐ Non — Explication : _______________________________________________
___________________________________________________________________________
Le lien WAN devrait être dans l'area : _______  Raison : ____________________
```

### A3 — Vérification d'une table BGP (8 pts)

```
R_SIEGE# show bgp summary

BGP router identifier 172.20.255.1, local AS number 64512
Neighbor        V    AS    MsgRcvd MsgSent TblVer  Up/Down    State/PfxRcd
10.1.1.2        4  3215      4521    4518     89    2d04h           12340
10.2.2.2        4  5511       234     231     89    00:12:33           127
172.20.255.2    4 64512       445     442     89    01:22:33            48
```

**A3.a** — Identifie le type (eBGP/iBGP) de chaque session et indique le nombre de préfixes reçus :

| Voisin | Type | Préfixes reçus |
|---|---|---|
| 10.1.1.2 | | |
| 10.2.2.2 | | |
| 172.20.255.2 | | |

**A3.b** — La session avec 172.20.255.2 (AS 64512) transporte **48 préfixes** alors qu'il s'agit d'un pair interne. Pourquoi ce routeur peut-il avoir des routes à partager en interne ?

```
___________________________________________________________________________
___________________________________________________________________________
```

---

## PARTIE B — Configuration Packet Tracer (50 min) · /50

> **Ouvrir** `S14_Annale_Sujet1_DEPART.pkt`
> La topologie est **pré-câblée** mais non configurée.

### Topologie

```
        SIÈGE                                   AGENCE
                                           
  PC_EMP (VLAN 10) ──┐                    ┌── PC_AG1
  IP_PHONE (VLAN 20) ─┤                    │
  PC_MGMT (VLAN 30) ──┤                    │
                      [SW_SIEGE] ─ Gi0/24 ─ Gi0/0 ─ [R_SIEGE] ─ WAN ─ [R_AGENCE] ─ [SW_AGENCE]
                      [SW_DIST]  ─ EC ─ [SW_SIEGE]

Équipements :
  R_SIEGE  : routeur principal · Lo0:172.20.255.1 · WAN:172.20.100.1/30
  R_AGENCE : routeur agence · Lo0:172.20.255.2 · WAN:172.20.100.2/30
  SW_SIEGE : switch cœur (3560)
  SW_DIST  : switch distribution (2960)
  PC_EMP   : 172.20.10.10/26 · GW:172.20.10.1
  IP_PHONE : 172.20.20.10/27 · GW:172.20.20.1
  PC_AG1   : [selon plan A1]
```

### Mission B1 — VLANs et trunks (10 pts)

```
☐ Créer VLANs 10 (EMPLOYES), 20 (VOIP), 30 (MANAGEMENT) sur SW_SIEGE et SW_DIST
☐ Configurer les ports access : PC_EMP → VLAN 10, IP_PHONE → VLAN 20, PC_MGMT → VLAN 30
☐ Configurer le trunk SW_DIST → SW_SIEGE (VLANs 10, 20, 30 autorisés)
☐ Configurer le trunk SW_SIEGE → R_SIEGE (VLANs 10, 20, 30 autorisés)
```

### Mission B2 — EtherChannel LACP (6 pts)

```
☐ Configurer EtherChannel LACP (mode active/active) entre SW_SIEGE et SW_DIST
  → 2 liens Gigabit (Gi0/1 et Gi0/2 sur chaque switch)
  → Port-channel 1 en mode trunk, VLANs 10/20/30 autorisés
☐ Vérification : show etherchannel summary → Po1(SU), ports en (P)
```

### Mission B3 — Inter-VLAN et adressage R_SIEGE (12 pts)

```
☐ Configurer les sous-interfaces router-on-a-stick sur R_SIEGE :
  Gi0/0.10 → encapsulation dot1Q 10 · IP selon plan A1
  Gi0/0.20 → encapsulation dot1Q 20 · IP selon plan A1
  Gi0/0.30 → encapsulation dot1Q 30 · IP selon plan A1
☐ Configurer l'interface WAN de R_SIEGE (172.20.100.1/30)
☐ Configurer la Loopback0 de R_SIEGE (172.20.255.1/32)
☐ Configurer R_AGENCE : LAN, WAN, Loopback0
```

### Mission B4 — OSPF multi-aires (14 pts)

```
☐ R_SIEGE : process OSPF 1, router-id 172.20.255.1
  → Area 0 : VLANs 10/20/30 + Loopback
  → Area 1 : lien WAN
  → passive-interface sur Gi0/0.10, Gi0/0.20, Gi0/0.30
☐ R_AGENCE : process OSPF 1, router-id 172.20.255.2
  → Area 1 : lien WAN + LAN Agence
  → passive-interface LAN
☐ Vérification : show ip ospf neighbor → FULL entre R_SIEGE et R_AGENCE
☐ Vérification : show ip route sur R_AGENCE → routes O IA vers les VLANs
```

### Mission B5 — Tests de validation (8 pts)

```
☐ T1 : ping PC_EMP → PC_AG1 → Succès
☐ T2 : ping IP_PHONE → PC_AG1 → Succès (inter-VLAN + OSPF)
☐ T3 : show ip ospf neighbor → FULL sur R_SIEGE
☐ T4 : show etherchannel summary → Po1(SU)
☐ T5 : show vlan brief sur SW_SIEGE → VLANs 10/20/30 avec bons ports
☐ copy running-config startup-config sur tous les équipements
```

### Mission BONUS — QoS VoIP (5 pts)

```
☐ Configurer une policy-map QOS_WAN sur R_SIEGE (interface WAN)
  → Classe VOIX : match dscp ef · priority percent 30
  → class-default : fair-queue
```

---

## PARTIE C — Documentation (20 min) · /20

### C1 — Schéma d'architecture (12 pts)

> Sur papier ou dans le document, dessine le schéma annoté incluant :

```
☐ Tous les équipements avec leur nom et rôle
☐ Les VLANs (numéro + nom) avec les ports correspondants
☐ Les areas OSPF (Area 0 et Area 1) clairement délimitées
☐ Les adresses IP de chaque interface
☐ Le lien WAN avec le réseau /30
☐ L'EtherChannel indiqué avec son numéro de port-channel
```

### C2 — Justification des choix (8 pts)

```
Réponds aux 4 questions suivantes en 2-3 lignes chacune :

Q1 — Pourquoi utilise-t-on OSPF multi-aire et non OSPF single-area ?
Q2 — Pourquoi l'EtherChannel améliore-t-il la disponibilité du réseau ?
Q3 — Pourquoi la QoS est-elle nécessaire pour la téléphonie IP ?
Q4 — Quel est le rôle de passive-interface dans la configuration OSPF ?
```

---

## 📊 Grille de notation

| Mission | /pts | Score |
|---|---|---|
| A1 — Plan d'adressage | /12 | |
| A2 — Analyse OSPF | /10 | |
| A3 — Table BGP | /8 | |
| B1 — VLANs + trunks | /10 | |
| B2 — EtherChannel | /6 | |
| B3 — Inter-VLAN + adressage | /12 | |
| B4 — OSPF | /14 | |
| B5 — Tests validation | /8 | |
| C1 — Schéma | /12 | |
| C2 — Justifications | /8 | |
| **TOTAL** | **/100** | |

---

---

# ✅ CORRECTION COMMENTÉE SUJET 1 — Document enseignant uniquement

## A1 — Plan d'adressage

```
VLAN 10 — 60 hôtes → /26 = 62 hôtes utilisables → 172.20.10.0/26
  Plage : 172.20.10.1 – 172.20.10.62 · Broadcast : 172.20.10.63

VLAN 20 — 40 hôtes → /26 = 62h OU /27 = 30h → insuffisant → /26
  172.20.20.0/26 → Plage : 172.20.20.1 – 172.20.20.62

VLAN 30 — 10 hôtes → /28 = 14 hôtes → 172.20.30.0/28
  Plage : 172.20.30.1 – 172.20.30.14 · Broadcast : 172.20.30.15

LAN Agence — 25 hôtes → /27 = 30 hôtes → 172.20.40.0/27
  Plage : 172.20.40.1 – 172.20.40.30 · Broadcast : 172.20.40.31

WAN — 2 hôtes → /30 = 2 hôtes → 172.20.100.0/30
  172.20.100.1 (R_SIEGE) · 172.20.100.2 (R_AGENCE)

⚠️ Attention correcteur : accepter toute solution cohérente avec ≥ hôtes requis.
   Pénaliser uniquement les erreurs de calcul, pas les choix de plages.
```

## A2 — Erreurs OSPF

```
Erreur 1 : network 172.20.10.0 255.255.255.0 area 0
  Problème : MASQUE réseau au lieu de WILDCARD
  Correction : network 172.20.10.0 0.0.0.63 area 0  (pour /26)
  ⚠️ Point pédagogique clé : erreur la plus fréquente dans les sujets E31 !

Erreur 2 : network 172.20.100.0 255.255.255.252 area 1
  Problème 1 : Masque au lieu de wildcard (0.0.0.3)
  Problème 2 : Le lien WAN entre R_SIEGE (ABR) et R_AGENCE doit être en AREA 1
               MAIS R_SIEGE doit aussi annoncer Area 0 pour être ABR.
               Si le WAN est en Area 1 et que R_SIEGE a des réseaux en Area 0,
               c'est architecturalement CORRECT.
  
  En réalité, l'erreur principale ici est le masque (255.255.255.252 au lieu de 0.0.0.3).

⚠️ Note correcteur : Area 0 pour le WAN est aussi acceptable — ne pas pénaliser
   si l'apprenant justifie le choix (single-area simplifiée).
```

## A3 — Table BGP

```
10.1.1.2  → eBGP (AS 3215 ≠ 64512) · 12340 préfixes (table Internet du FAI)
10.2.2.2  → eBGP (AS 5511 ≠ 64512) · 127 préfixes (FAI secondaire ou filtré)
172.20.255.2 → iBGP (AS 64512 = local) · 48 préfixes (routes internes partagées)

172.20.255.2 partage des préfixes en interne car : c'est un routeur de bordure
qui a ses propres sessions eBGP avec d'autres FAI → il partage ces routes
en iBGP avec R_SIEGE pour que le trafic sortant puisse utiliser ses liens.
```

## B4 — Config OSPF correcte

```cisco
! R_SIEGE
router ospf 1
 router-id 172.20.255.1
 network 172.20.10.0 0.0.0.63 area 0        ! /26 → wildcard 0.0.0.63
 network 172.20.20.0 0.0.0.63 area 0        ! /26
 network 172.20.30.0 0.0.0.15 area 0        ! /28 → wildcard 0.0.0.15
 network 172.20.255.1 0.0.0.0 area 0        ! Loopback /32
 network 172.20.100.0 0.0.0.3 area 1        ! WAN /30
 passive-interface GigabitEthernet0/0.10
 passive-interface GigabitEthernet0/0.20
 passive-interface GigabitEthernet0/0.30
 passive-interface Loopback0

! R_AGENCE
router ospf 1
 router-id 172.20.255.2
 network 172.20.40.0 0.0.0.31 area 1        ! LAN Agence /27
 network 172.20.100.0 0.0.0.3 area 1        ! WAN /30
 network 172.20.255.2 0.0.0.0 area 1        ! Loopback /32
 passive-interface GigabitEthernet0/0       ! LAN
 passive-interface Loopback0
```

## C2 — Justifications attendues

```
Q1 — Multi-aire : Les aires limitent les LSA flooding (chaque aire a sa propre LSDB)
     → moins de calculs SPF · scalabilité · Area 0 = backbone obligatoire

Q2 — EtherChannel : Si Gi0/1 tombe, Gi0/2 continue → pas d'interruption
     + débit agrégé (2 × 1G = 2 Gbps logiques)

Q3 — QoS VoIP : VoIP sensible à la latence (<150ms) et la gigue (<30ms)
     → sans QoS, un téléchargement FTP peut saturer le lien WAN et couper les appels

Q4 — passive-interface : Empêche l'envoi de paquets Hello OSPF sur les interfaces
     vers les utilisateurs finaux (ils ne font pas tourner OSPF)
     → sécurité (pas de voisinage OSPF non autorisé) + économie CPU/bande passante
```

---

*Sujet 1 + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S14*
