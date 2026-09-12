# 🔬 LAB FINAL INTÉGRÉ — S6 · 3ᵉ ANNÉE · E31
## Simulation Examen CCNA : Infrastructure Complète en Temps Limité

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **⏱️ DURÉE : 45 MINUTES — CHRONO AFFICHÉ AU TABLEAU**
> **Règles** : Fiche de cours autorisée · Packet Tracer · Aucune aide extérieure
> **Fichier** : `S6_E31_Lab_Final_CCNA.pkt`

---

## 📋 Cahier des charges — INFRASTRUCTECH SAS

> **Contexte** : INFRASTRUCTECH SAS vient d'ouvrir un second bureau (Site B).
> Tu dois déployer l'infrastructure réseau complète selon les spécifications suivantes.
> **Chaque tâche non complétée = points perdus.**

---

## 🗺️ Topologie

```
         SITE A (Siège)                         SITE B (Nouveau bureau)
                                                
  PC_Sales (VLAN 10) ──┐      10.0.0.0/30          ┌── PC_Finance (VLAN 10)
  PC_IT    (VLAN 20) ──┤                            ├── PC_RH (VLAN 20)
                       │    ┌─────────────┐         │
                     [SW1]═══[Port-Channel]═══[SW2]  │
                     [SW3]   4 liens max            │
                       │                            │
                     Gi0/0                        Gi0/0
                       │                            │
                     [R_A]  ──────────────────  [R_B]
                     Lo:1.1.1.1                   Lo:2.2.2.2
                  OSPF Area 0                  OSPF Area 1
                                                
        VLAN 10 : 192.168.10.0/24             VLAN 10 : 192.168.20.0/24
        VLAN 20 : 192.168.11.0/24             VLAN 20 : 192.168.21.0/24
        Lien WAN : R_A=10.0.0.1/30  R_B=10.0.0.2/30
```

---

## 📐 Plan d'adressage fourni

| Équipement | Interface | Adresse IP | Masque |
|---|---|---|---|
| R_A | Gi0/0.10 | 192.168.10.1 | /24 |
| R_A | Gi0/0.20 | 192.168.11.1 | /24 |
| R_A | Gi0/1 (WAN) | 10.0.0.1 | /30 |
| R_A | Lo0 | 1.1.1.1 | /32 |
| R_B | Gi0/0.10 | 192.168.20.1 | /24 |
| R_B | Gi0/0.20 | 192.168.21.1 | /24 |
| R_B | Gi0/0 (WAN) | 10.0.0.2 | /30 |
| R_B | Lo0 | 2.2.2.2 | /32 |
| PC_Sales | NIC | 192.168.10.10 | /24 · GW : .1 |
| PC_IT | NIC | 192.168.11.10 | /24 · GW : .1 |
| PC_Finance | NIC | 192.168.20.10 | /24 · GW : .1 |
| PC_RH | NIC | 192.168.21.10 | /24 · GW : .1 |

---

## ✅ Missions — Grille de validation

| # | Mission | Points | ✓ |
|---|---|---|---|
| **M1** | VLANs 10 et 20 créés sur SW1 et SW2 | /4 | |
| **M2** | Ports PC en mode access dans le bon VLAN | /4 | |
| **M3** | EtherChannel LACP (2 liens Gi0/1-Gi0/2) entre SW1 et SW2, mode active/active | /6 | |
| **M4** | Trunk sur Po1 avec VLAN 10 et 20 autorisés | /3 | |
| **M5** | R_A : adressage WAN + sous-interfaces inter-VLAN (dot1Q encapsulation) | /6 | |
| **M6** | R_B : adressage WAN + sous-interfaces inter-VLAN | /5 | |
| **M7** | OSPF process 1 — R_A dans Area 0 · R_B dans Area 1 | /7 | |
| **M8** | Router-IDs : R_A=1.1.1.1 (Lo0) · R_B=2.2.2.2 (Lo0) | /3 | |
| **M9** | Toutes les routes présentes sur R_A (C, O, O IA) | /4 | |
| **M10** | PC_Sales ping PC_Finance (inter-sites VLAN 10) | /4 | |
| **M11** | PC_IT ping PC_RH (inter-sites VLAN 20) | /4 | |
| **M12** | copy running-config startup-config sur tous les équipements | /2 | |
| **BONUS** | Route statique par défaut sur R_B → R_A (DA=1) + floating (DA=5) via Lo0 de R_A | /3 bonus |
| **TOTAL** | | **/52** + bonus | |

> **Convertir en /30** : score/52 × 30 = note du lab

---

## 📝 Espace de travail — Notes de configuration

```
┌──────── SW1 ───────────────────────────────────────────────────────────┐
│                                                                        │
│                                                                        │
│                                                                        │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘

┌──────── SW2 (symétrique) ──────────────────────────────────────────────┐
│                                                                        │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘

┌──────── R_A ───────────────────────────────────────────────────────────┐
│                                                                        │
│                                                                        │
│                                                                        │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘

┌──────── R_B ───────────────────────────────────────────────────────────┐
│                                                                        │
│                                                                        │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 Vérifications finales à effectuer

Avant de terminer, **exécute chaque vérification et note le résultat** :

```
□ show vlan brief sur SW1
  → VLAN 10 et 20 présents avec les bons ports : ☐ OK ☐ KO

□ show etherchannel summary sur SW1
  → Po1(SU) avec Gi0/1(P) Gi0/2(P) : ☐ OK ☐ KO

□ show ip ospf neighbor sur R_A
  → R_B en état FULL : ☐ OK ☐ KO

□ show ip route sur R_A
  → Routes O et O IA présentes : ☐ OK ☐ KO

□ ping 192.168.20.10 depuis PC_Sales
  → Succès : ☐ OK ☐ KO

□ ping 192.168.21.10 depuis PC_IT
  → Succès : ☐ OK ☐ KO

□ copy run start exécuté partout : ☐ OK ☐ KO
```

**Score vérifications** : _____ / 7 ✓

---

---

# ✅ CORRECTION DU LAB — Document enseignant uniquement

```cisco
! ═══ SW1 ═══
vlan 10
 name SALES
vlan 20
 name IT

interface range GigabitEthernet0/1-2
 channel-group 1 mode active
 exit

interface port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
 exit

interface GigabitEthernet0/3
 switchport mode access
 switchport access vlan 10   ! PC_Sales

interface GigabitEthernet0/4
 switchport mode access
 switchport access vlan 20   ! PC_IT

interface GigabitEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20  ! vers R_A

! ═══ R_A ═══
interface Loopback0
 ip address 1.1.1.1 255.255.255.255

interface GigabitEthernet0/0
 no shutdown

interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.11.1 255.255.255.0

interface GigabitEthernet0/1
 ip address 10.0.0.1 255.255.255.252
 no shutdown

router ospf 1
 router-id 1.1.1.1
 network 10.0.0.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.11.0 0.0.0.255 area 0
 passive-interface GigabitEthernet0/0.10
 passive-interface GigabitEthernet0/0.20

! ═══ R_B ═══ (configuration similaire)
interface Loopback0
 ip address 2.2.2.2 255.255.255.255

interface GigabitEthernet0/0
 no shutdown

interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.20.1 255.255.255.0

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.21.1 255.255.255.0

interface GigabitEthernet0/1   ! ou Gi0/0 selon le .pkt
 ip address 10.0.0.2 255.255.255.252
 no shutdown

router ospf 1
 router-id 2.2.2.2
 network 10.0.0.0 0.0.0.3 area 1
 network 192.168.20.0 0.0.0.255 area 1
 network 192.168.21.0 0.0.0.255 area 1
 passive-interface GigabitEthernet0/0.10
 passive-interface GigabitEthernet0/0.20

! BONUS route flottante
ip route 0.0.0.0 0.0.0.0 10.0.0.1
ip route 0.0.0.0 0.0.0.0 1.1.1.1 5
```

**Points fréquemment perdus** :
- Oublier `no shutdown` sur Gi0/0 (interface mère des sous-interfaces)
- `encapsulation dot1Q` avant l'adresse IP sur la sous-interface
- passive-interface sur les LANs (bonne pratique OSPF)
- Trunk manquant sur le lien SW1/SW2 → R_A (Gi0/24)

---

*Lab Final CCNA + Correction — BAC PRO CIEL | E31 | 3ᵉ année S6*
