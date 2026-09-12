# 🔬 LABS EN TEMPS LIMITÉ — S14 · 2ᵉ ANNÉE · E31
## Simulation d'Examen Packet Tracer — 3 Labs Progressifs

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Conditions** : Examen blanc · Aucune aide extérieure · Temps affiché au tableau
> **Épreuve simulée** : **E31** – Épreuve pratique infrastructure réseau · **CCNA 200-301**

---

---

# 🔵 LAB 1 — Routage statique et OSPF
## ⏱️ Temps alloué : 35 minutes · Barème : /20 pts
## Fichier : `S14_E31_Lab1_Routage.pkt`

---

## 📋 Cahier des charges — Lab 1

### Topologie

```
[PC1]──────[R1]─────────[R2]────────[R3]──────[PC3]
192.168.1.x  │  10.1.2.0/30  10.2.3.0/30  │  192.168.3.x
             │                             │
           [R4]                          (lien OSPF R2↔R3)
           10.1.4.0/30
             │
           [PC4]
         192.168.4.x
```

### Plan d'adressage

| Interface | Adresse IP | Masque |
|---|---|---|
| R1 Gi0/0 | 192.168.1.1 | /24 |
| R1 Gi0/1 | 10.1.2.1 | /30 |
| R1 Gi0/2 | 10.1.4.1 | /30 |
| R2 Gi0/0 | 10.1.2.2 | /30 |
| R2 Gi0/1 | 10.2.3.1 | /30 |
| R3 Gi0/0 | 10.2.3.2 | /30 |
| R3 Gi0/1 | 192.168.3.1 | /24 |
| R4 Gi0/0 | 10.1.4.2 | /30 |
| R4 Gi0/1 | 192.168.4.1 | /24 |
| PC1 | 192.168.1.10 | /24 · GW : 192.168.1.1 |
| PC3 | 192.168.3.10 | /24 · GW : 192.168.3.1 |
| PC4 | 192.168.4.10 | /24 · GW : 192.168.4.1 |

### Mission

1. **Configurer l'adressage IP** sur toutes les interfaces des routeurs (5 pts)
2. **Configurer des routes statiques** sur R1 et R4 vers les réseaux distants (5 pts)
3. **Configurer OSPF** (process 1, Area 0) sur R2 et R3 pour échanger les routes (5 pts)
4. **Vérifier** que PC1 peut pinguer PC3 et PC4 (5 pts)

### Espace de travail — Commandes à noter

```
# R1 — Adressage + routes statiques :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

# R2 — Adressage + OSPF :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

# R3 — Adressage + OSPF :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

# R4 — Adressage + routes statiques :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

### Vérification Lab 1

| Test | Résultat |
|---|---|
| PC1 ping 192.168.3.10 (PC3) | ☐ Succès ☐ Échec |
| PC1 ping 192.168.4.10 (PC4) | ☐ Succès ☐ Échec |
| R2 `show ip ospf neighbor` → état FULL avec R3 | ☐ Oui ☐ Non |
| R1 `show ip route` → routes S vers 192.168.3.0 et 192.168.4.0 | ☐ Oui ☐ Non |

**Score Lab 1 : _____ / 20**

---

---

# 🟠 LAB 2 — VLANs, EtherChannel, Dépannage
## ⏱️ Temps alloué : 45 minutes · Barème : /20 pts
## Fichier : `S14_E31_Lab2_VLANs.pkt`

---

## 📋 Cahier des charges — Lab 2

### Topologie

```
PC_A (VLAN 10)──[SW1]═══Po1 (4 liens)═══[SW2]──PC_B (VLAN 10)
PC_C (VLAN 20)──┤      Gi0/1 à Gi0/4        ├──PC_D (VLAN 20)
                │                             │
               Gi0/0                        Gi0/0
               (vers PC_A/C)               (vers PC_B/D)
```

### État initial du fichier .pkt

```
✓ VLANs 10 et 20 créés sur les deux switches
✓ Ports des PCs assignés aux bons VLANs
✗ EtherChannel : intentionnellement cassé (3 pannes injectées)
✗ Trunk sur Po1 : absent
```

### Mission

1. **Diagnostiquer** les pannes EtherChannel depuis `show etherchannel summary` (5 pts)
2. **Corriger** les pannes pour que les 4 liens soient en état (P) (10 pts)
3. **Configurer** le trunk sur Po1 pour les VLAN 10 et 20 (5 pts)

### Espace de diagnostic

```
SW1# show etherchannel summary
─────────────────────────────────────────
Recopie la sortie ici :
___________________________________________________________________________
___________________________________________________________________________

Analyse :
  Port-channel état : Po1(__)  → opérationnel ? ☐ Oui ☐ Non
  Ports en (P) : ___________________________________________________________
  Ports en (I) ou (D) ou (s) : _____________________________________________

Problèmes identifiés :
  Problème 1 : ______________________________________________________________
  Problème 2 (si présent) : ________________________________________________
  Problème 3 (si présent) : ________________________________________________
```

### Espace de correction

```
# Corrections SW1 :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

# Corrections SW2 :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

# Configuration trunk sur Po1 (SW1 et SW2) :
___________________________________________________________________________
___________________________________________________________________________
```

### Vérification Lab 2

| Test | Résultat |
|---|---|
| `show etherchannel summary` → Po1(SU), tous ports (P) | ☐ Oui ☐ Non |
| PC_A ping PC_B (VLAN 10 cross-switch) | ☐ Succès ☐ Échec |
| PC_C ping PC_D (VLAN 20 cross-switch) | ☐ Succès ☐ Échec |
| `show interfaces port-channel 1 trunk` → VLAN 10 et 20 autorisés | ☐ Oui ☐ Non |

**Score Lab 2 : _____ / 20**

---

---

# 🔴 LAB 3 — Infrastructure complète (sujet intégré)
## ⏱️ Temps alloué : 50 minutes · Barème : /30 pts
## Fichier : `S14_E31_Lab3_Integre.pkt`
## ⚠️ Aucune aide autorisée — conditions d'examen strictes

---

## 📋 Cahier des charges — Lab 3

### Topologie complète

```
        SITE A                              SITE B
  PC_Sales (VLAN 10)                 PC_Compta (VLAN 10)
  PC_IT    (VLAN 20)                 PC_Serveur (VLAN 20)
       │                                    │
     [SW_A]  ═══(EtherChannel Po1)═══  [SW_B]
     Gi0/1-Gi0/2                         Gi0/1-Gi0/2
       │                                    │
       Gi0/0                              Gi0/0
       │                                    │
     [R_A]   ─────(lien WAN OSPF)─────  [R_B]
  Gi0/1: 10.0.12.1/30                 Gi0/0: 10.0.12.2/30
  Lo0  : 1.1.1.1/32                   Lo0  : 2.2.2.2/32
```

### Plan d'adressage complet

| Réseau | Plage | Équipements |
|---|---|---|
| VLAN 10 Site A | 192.168.10.0/24 | PC_Sales (.10), R_A VLAN 10 SVI (.1) |
| VLAN 20 Site A | 192.168.20.0/24 | PC_IT (.10), R_A VLAN 20 SVI (.1) |
| VLAN 10 Site B | 192.168.110.0/24 | PC_Compta (.10), R_B VLAN 10 SVI (.1) |
| VLAN 20 Site B | 192.168.120.0/24 | PC_Serveur (.10), R_B VLAN 20 SVI (.1) |
| Lien WAN | 10.0.12.0/30 | R_A (.1), R_B (.2) |

### Livrables attendus

**BLOC A — Switching Site A (8 pts)**
- VLANs 10 et 20 créés sur SW_A
- Ports PC_Sales et PC_IT en mode access dans les bons VLANs
- EtherChannel LACP (2 liens, Po1) entre SW_A et SW_B, mode active/active
- Trunk sur Po1 autorisant VLAN 10 et 20

**BLOC B — Switching Site B (7 pts)**
- Même configuration VLANs sur SW_B
- Ports PC_Compta et PC_Serveur en mode access
- Côté SW_B du EtherChannel + trunk

**BLOC C — Routage R_A (8 pts)**
- Adressage IP du lien WAN
- Router-id OSPF = 1.1.1.1 (Loopback)
- OSPF Area 0 sur tous les réseaux de R_A
- Inter-VLAN routing via sous-interfaces Gi0/0 (dot1Q encapsulation)

**BLOC D — Routage R_B (7 pts)**
- Adressage IP lien WAN
- Router-id OSPF = 2.2.2.2
- OSPF Area 0 — annonce tous les réseaux de R_B
- Inter-VLAN routing via sous-interfaces

### Espace de travail Lab 3

```
═══════════════════ SW_A ═══════════════════
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

═══════════════════ SW_B ═══════════════════
(configuration symétrique à SW_A)
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

═══════════════════ R_A ════════════════════
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

═══════════════════ R_B ════════════════════
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

### Vérification Lab 3 — Grille de tests

| Test | Points | Résultat |
|---|---|---|
| PC_Sales ping PC_IT (inter-VLAN Site A) | /2 | ☐ |
| PC_Compta ping PC_Serveur (inter-VLAN Site B) | /2 | ☐ |
| PC_Sales ping PC_Compta (inter-site VLAN 10) | /3 | ☐ |
| PC_IT ping PC_Serveur (inter-site VLAN 20) | /3 | ☐ |
| `show etherchannel summary` → Po1(SU), 2 ports (P) SW_A | /3 | ☐ |
| `show etherchannel summary` → Po1(SU), 2 ports (P) SW_B | /3 | ☐ |
| `show ip ospf neighbor` → R_A et R_B en état FULL | /4 | ☐ |
| `show ip route` → R_A voit les réseaux de Site B via OSPF | /3 | ☐ |
| Traceroute PC_Sales → PC_Compta → chemin correct | /3 | ☐ |
| `copy run start` effectué sur tous les équipements | /1 | ☐ |
| **TOTAL Lab 3** | **/30** | |

---

## 📊 Bilan des 3 labs

| Lab | Thèmes | Temps alloué | Score |
|---|---|---|---|
| Lab 1 | Routage statique + OSPF | 35 min | /20 |
| Lab 2 | VLANs + EtherChannel + dépannage | 45 min | /20 |
| Lab 3 | Infrastructure complète | 50 min | /30 |
| **TOTAL** | | **130 min** | **/70** |

**Mon score global : _____ / 70 → _____ %**

**Interprétation :**
- ≥ 60/70 (85%) : Prêt pour le E31 et le CCNA
- 50-59/70 (70-84%) : Quelques points à consolider
- 40-49/70 (57-69%) : Révisions ciblées nécessaires
- < 40/70 : Reprendre les séances S2, S3, S13

---

---

# ✅ CORRECTIONS DES LABS — Document enseignant uniquement

---

## Correction Lab 1

```cisco
! R1
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
interface GigabitEthernet0/1
 ip address 10.1.2.1 255.255.255.252
 no shutdown
interface GigabitEthernet0/2
 ip address 10.1.4.1 255.255.255.252
 no shutdown
ip route 192.168.3.0 255.255.255.0 10.1.2.2
ip route 192.168.4.0 255.255.255.0 10.1.4.2

! R2
interface GigabitEthernet0/0
 ip address 10.1.2.2 255.255.255.252 / no shutdown
interface GigabitEthernet0/1
 ip address 10.2.3.1 255.255.255.252 / no shutdown
router ospf 1
 router-id 2.2.2.2
 network 10.1.2.0 0.0.0.3 area 0
 network 10.2.3.0 0.0.0.3 area 0
 passive-interface GigabitEthernet0/0

! R3
interface GigabitEthernet0/0
 ip address 10.2.3.2 255.255.255.252 / no shutdown
interface GigabitEthernet0/1
 ip address 192.168.3.1 255.255.255.0 / no shutdown
router ospf 1
 router-id 3.3.3.3
 network 10.2.3.0 0.0.0.3 area 0
 network 192.168.3.0 0.0.0.255 area 0

! R4
interface GigabitEthernet0/0
 ip address 10.1.4.2 255.255.255.252 / no shutdown
interface GigabitEthernet0/1
 ip address 192.168.4.1 255.255.255.0 / no shutdown
ip route 192.168.1.0 255.255.255.0 10.1.4.1
ip route 192.168.3.0 255.255.255.0 10.1.4.1
```

## Correction Lab 2

```
Pannes typiques injectées :
  Panne A : SW2 en mode "on" au lieu de "active" → fix: channel-group 1 mode active
  Panne B : Gi0/3 sur SW1 forcé à 100Mbps → fix: speed auto
  Panne C : trunk absent sur Po1 → fix: switchport mode trunk + allowed vlan all

Configuration complète attendue :
SW1/SW2 identiques :
  interface range Gi0/1-4
   channel-group 1 mode active
  interface port-channel 1
   switchport mode trunk
   switchport trunk allowed vlan all
```

## Correction Lab 3 — Éléments clés

```cisco
! SW_A (SW_B symétrique)
vlan 10 / name SALES
vlan 20 / name IT
interface Gi0/0 (vers PC_Sales)
 switchport mode access / switchport access vlan 10
interface Gi0/1-2
 channel-group 1 mode active
interface port-channel 1
 switchport mode trunk / switchport trunk allowed vlan 10,20

! R_A (sous-interfaces inter-VLAN + OSPF)
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
interface GigabitEthernet0/1
 ip address 10.0.12.1 255.255.255.252 / no shutdown
interface loopback 0
 ip address 1.1.1.1 255.255.255.255
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.20.0 0.0.0.255 area 0
 network 10.0.12.0 0.0.0.3 area 0
 passive-interface GigabitEthernet0/0.10
 passive-interface GigabitEthernet0/0.20
```

---

*Labs en temps limité + Corrections — BAC PRO CIEL | E31 | 2ᵉ année S14*
*Simulation examen — Compétences C2.2 · C2.3 · S2.1 · S2.2 · S2.3 · S3.3*
