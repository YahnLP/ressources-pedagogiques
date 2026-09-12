# 🗂️ AIDE-MÉMOIRE PROJET A2 — À PLASTIFIER
## OSPF Multi-aires · Tunnel GRE · Haute Dispo · QoS LLQ · EtherChannel · BAC PRO CIEL · E31 · S16

---

> *Référence rapide pendant la configuration du projet*

---

## 🌐 OSPF Multi-aires — Essentiel

```cisco
router ospf 1
 router-id X.X.X.X           ! Loopback : 1.1.1.1 / 2.2.2.2 / 4.4.4.4
 network 10.1.4.0 0.0.0.3 area 0     ! /30 → wildcard 0.0.0.3
 network 192.168.10.0 0.0.0.255 area 0 ! /24 → wildcard 0.0.0.255
 network 10.1.2.0 0.0.0.3 area 1     ! Lien vers Area 1
 passive-interface Gi0/0.10          ! Ne pas envoyer Hello sur LAN

Vérifier : show ip ospf neighbor → FULL
           show ip route → O (intra) et O IA (inter-aire)
```

---

## 🔁 Haute disponibilité WAN (R_AGENCE_B)

```cisco
! Route principale (DA=1, active)
ip route 0.0.0.0 0.0.0.0 10.1.2.1

! Route flottante (DA=5, active SEULEMENT si principale DOWN)
ip route 0.0.0.0 0.0.0.0 10.1.3.1 5

Test : shutdown Se0/0/0 → show ip route → route secours visible
```

---

## 🔐 Tunnel GRE

```cisco
! R_SIEGE
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source Serial0/0/0
 tunnel destination 10.1.2.2
 no shutdown

! R_AGENCE_B (miroir)
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source Serial0/0/0
 tunnel destination 10.1.2.1
 no shutdown

Vérifier : show interfaces Tunnel0 → up/up
```

---

## 🎵 QoS LLQ VoIP

```cisco
class-map match-any VOIX
 match dscp ef

policy-map QOS_WAN
 class VOIX
  priority percent 30
 class class-default
  fair-queue

interface Serial0/0/0
 service-policy output QOS_WAN

Vérifier : show policy-map interface Se0/0/0
```

---

## ⚡ EtherChannel LACP (SW_CORE_A)

```cisco
interface range Gi0/1-2
 channel-group 1 mode active
interface port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30

Vérifier : show etherchannel summary → Po1(SU), (P)
```

---

## 🔌 Inter-VLAN (R_SIEGE)

```cisco
interface Gi0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
interface Gi0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
```

---

## ✅ 12 Tests de validation

```
T1  PC Siège → PC Agence B          ping 192.168.50.10
T2  PC Siège → SRV Web              ping 192.168.200.10
T3  IP_Phone → SRV VoIP             ping 192.168.200.20
T4  OSPF R_SIEGE                    show ip ospf neighbor → FULL ×2
T5  Table R_AGENCE_B                show ip route → O IA pour tous
T6  EtherChannel Po1/Po2            show etherchannel summary → SU, (P)
T7  Résilience EC                   shutdown Gi0/1 → ping continue
T8  Basculement WAN                 shutdown Se0/0/0 → ping reprend
T9  QoS appliquée                   show policy-map int Se0/0/0
T10 Tunnel GRE                      show interfaces Tunnel0 → up/up
T11 PC Agence B → PC Siège VLAN 10  ping 192.168.10.10
T12 Sauvegarde                      copy run start (tous équipements)
```

---

## 🚨 Top 5 erreurs à éviter

```
❌ Masque au lieu de wildcard dans OSPF
   /24 → 0.0.0.255  (PAS 255.255.255.0)

❌ Oublier no shutdown sur Tunnel0

❌ Route flottante avec même DA que la principale
   La secours doit avoir DA > 1 (ex : 5)

❌ QoS sur mauvaise interface
   service-policy OUTPUT sur le lien WAN (Serial)

❌ Pas de copy run start à la fin
```

---

*Aide-Mémoire Projet A2 — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S16*
*Compétences C2.1 · C2.2 · S2.2 · S3.3 · S3.4*
