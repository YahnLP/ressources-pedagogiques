# 🔬 LAB INTÉGRÉ — S12 · 3ᵉ ANNÉE · E31
## BGP + ACL + VPN + Firewall : Infrastructure Multi-sites Sécurisée

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **⏱️ Durée : 35 minutes · Conditions d'examen · Fiche de cours autorisée**
> **Fichier** : `S12_E31_Lab_Integre_Securite.pkt`

---

## 🗺️ Topologie

```
        AS 100                  AS 200 (Transit)             AS 300
   ┌────────────┐          ┌────────────────────┐      ┌────────────┐
   │    R1      │          │         R2         │      │     R3     │
   │ 10.0.12.1  ├─ eBGP ───┤ 10.0.12.2          │      │            │
   │            │          │ 10.0.23.1 ─ eBGP ──┤──────┤ 10.0.23.2  │
   │  Lo:1.1.1.1│          │                    │      │  Lo:3.3.3.3│
   └────────────┘          └────────────────────┘      └────────────┘
         │                                                    │
      Gi0/0                                               Gi0/1
         │                                                    │
   LAN-A (VLAN 10)                                    LAN-B (VLAN 30)
   192.168.1.0/24                                    192.168.3.0/24
   PC_A : 192.168.1.10                               PC_B : 192.168.3.10
   SRV_WEB : 192.168.1.20 (port 80/443)

Tunnel GRE entre R1 et R3 :
  Réseau tunnel : 172.16.0.0/30
  R1 Tunnel0 : 172.16.0.1/30
  R3 Tunnel0 : 172.16.0.2/30
```

---

## ✅ Missions à accomplir

| # | Mission | Pts |
|---|---|---|
| **M1** | eBGP entre R1-R2 et R2-R3 + annoncer les LANs | /8 |
| **M2** | ACL : Bloquer Telnet (23) de LAN-A → LAN-B | /5 |
| **M3** | ACL : Autoriser seulement HTTP/HTTPS (80/443) de LAN-B → SRV_WEB | /6 |
| **M4** | Tunnel GRE R1 ↔ R3 opérationnel | /6 |
| **M5** | Vérifications : show bgp + show interfaces Tunnel0 + tests ping | /5 |
| **BONUS** | Ajouter une route statique sur R1 vers LAN-B via le tunnel | /3 |
| **TOTAL** | | **/30 + 3 bonus** |

---

## 📝 Espace de travail

### M1 — Configuration BGP

```cisco
! R1 (AS 100)
router bgp ___
 bgp router-id _______________
 neighbor _______________ remote-as ___          ← vers R2
 network 192.168.1.0 mask ___________________

! R2 (AS 200) — routeur de transit
router bgp ___
 bgp router-id 2.2.2.2
 neighbor _______________ remote-as ___          ← vers R1
 neighbor _______________ remote-as ___          ← vers R3

! R3 (AS 300)
router bgp ___
 bgp router-id _______________
 neighbor _______________ remote-as ___          ← vers R2
 network 192.168.3.0 mask ___________________
```

### M2 — ACL Bloquer Telnet depuis LAN-A

```cisco
! Sur R1 — ACL étendue nommée (ou numérotée)
ip access-list extended SECURITE_LAN_A
 ! Règle 1 : Bloquer Telnet sortant de LAN-A
 _______________________________________________
 ! Autoriser tout le reste
 _______________________________________________

! Appliquer sur R1 (quelle interface, quelle direction ?)
interface ________________________
 ip access-group SECURITE_LAN_A ___
```

### M3 — ACL Filtrer accès à SRV_WEB depuis LAN-B

```cisco
! Sur R3 — ACL sur Gi0/1 (vers LAN-B)
ip access-list extended FILTRE_LAN_B
 ! Autoriser HTTP vers SRV_WEB
 _______________________________________________
 ! Autoriser HTTPS vers SRV_WEB
 _______________________________________________
 ! Bloquer tout le reste vers SRV_WEB
 _______________________________________________
 ! Autoriser le reste du trafic
 _______________________________________________

! Appliquer (quelle interface, quelle direction ?)
interface ________________________
 ip access-group FILTRE_LAN_B ___
```

### M4 — Tunnel GRE R1 ↔ R3

```cisco
! R1
interface Tunnel0
 ip address _______________ _______________
 tunnel source _______________             ← IP WAN de R1 (vers R2)
 tunnel destination _______________        ← IP WAN de R3 (vers R2)
 no shutdown

! R3 (miroir — attention à l'inversion source/destination !)
interface Tunnel0
 ip address _______________ _______________
 tunnel source _______________
 tunnel destination _______________
 no shutdown
```

---

## 🔍 Vérifications obligatoires

```
□ show bgp summary sur R2 → sessions Established avec R1 et R3
□ show bgp ipv4 unicast sur R1 → 192.168.3.0/24 présent
□ ping 192.168.3.10 depuis PC_A → Succès
□ ping 23.0.0.1 de PC_A (simulation Telnet bloqué) → voir résultat ACL
□ show interfaces Tunnel0 sur R1 → up/up
□ ping 172.16.0.2 source Tunnel0 depuis R1 → Succès
□ show ip access-lists → compteurs sur les règles ACL
□ copy run start sur tous les équipements
```

---

---

# ✅ CORRECTION DU LAB — Document enseignant uniquement

## M1 — BGP

```cisco
! R1
router bgp 100
 bgp router-id 1.1.1.1
 neighbor 10.0.12.2 remote-as 200
 network 192.168.1.0 mask 255.255.255.0

! R2
router bgp 200
 bgp router-id 2.2.2.2
 neighbor 10.0.12.1 remote-as 100
 neighbor 10.0.23.2 remote-as 300

! R3
router bgp 300
 bgp router-id 3.3.3.3
 neighbor 10.0.23.1 remote-as 200
 network 192.168.3.0 mask 255.255.255.0
```

## M2 — ACL Telnet

```cisco
ip access-list extended SECURITE_LAN_A
 deny tcp 192.168.1.0 0.0.0.255 any eq 23
 permit ip any any

interface GigabitEthernet0/0
 ip access-group SECURITE_LAN_A in
```

**Placement** : Gi0/0 in = trafic entrant depuis LAN-A sur R1 → near source ✓

## M3 — ACL HTTP/HTTPS vers SRV_WEB

```cisco
ip access-list extended FILTRE_LAN_B
 permit tcp 192.168.3.0 0.0.0.255 host 192.168.1.20 eq 80
 permit tcp 192.168.3.0 0.0.0.255 host 192.168.1.20 eq 443
 deny tcp 192.168.3.0 0.0.0.255 host 192.168.1.20 any
 permit ip any any

interface GigabitEthernet0/1  ! Interface LAN de R3
 ip access-group FILTRE_LAN_B in
```

**Placement** : Gi0/1 in = trafic entrant depuis LAN-B → near source ✓

## M4 — Tunnel GRE

```cisco
! IP WAN de R1 = 10.0.12.1 (Gi0/1 WAN)
! IP WAN de R3 = 10.0.23.2 (Gi0/0 WAN)

! R1
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source 10.0.12.1
 tunnel destination 10.0.23.2
 no shutdown

! R3
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source 10.0.23.2
 tunnel destination 10.0.12.1
 no shutdown
```

**BONUS** : `ip route 192.168.3.0 255.255.255.0 172.16.0.2` sur R1

**Points fréquemment perdus** :
- Oublier `no shutdown` sur Tunnel0
- Confondre source/destination GRE (doit être miroir)
- ACL M3 : ne pas oublier `permit ip any any` à la fin sinon tout le reste est bloqué
- BGP : réseau doit être dans la table de routage locale (IP sur Gi0/0)

---

*Lab Intégré S12 + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S12*
*Compétences : S2.4 · S5.1 · S5.2 · C2.2 · C2.3*
