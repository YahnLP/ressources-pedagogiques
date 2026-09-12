# 🗂️ AIDE-MÉMOIRE OSPFv3 Multi-AF — À PLASTIFIER
## IPv6 · Dual Stack · Transition · BAC PRO CIEL · E31 · 3ᵉ année S2

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## ⚡ OSPFv2 vs OSPFv3 Multi-AF

```
              OSPFv2          OSPFv3 Multi-AF
Activation    network (process)  ospfv3 1 ipv4/ipv6 area N (interface)
Hello addr    224.0.0.5          FF02::5
Next-hop      IP source          FE80:: (link-local)
Router-ID     IPv4               IPv4 obligatoire (même sans IPv4 !)
Transporte    IPv4 only          IPv4 ET IPv6 dans 1 seul process
Commande req  ip routing (auto)  ipv6 unicast-routing (obligatoire)
```

---

## ⚙️ Configuration OSPFv3 Multi-AF — 3 étapes

```cisco
! 1. Activer IPv6 routing (OBLIGATOIRE)
ipv6 unicast-routing

! 2. Process Multi-AF
router ospfv3 1
 router-id 1.1.1.1          ! Toujours format IPv4 !
 address-family ipv4 unicast
 exit-address-family
 address-family ipv6 unicast
 exit-address-family

! 3. Activer sur chaque interface
interface GigabitEthernet0/0
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
```

---

## 📐 Adressage dual stack

```cisco
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0   ← IPv4
 ipv6 address 2001:DB8:1::1/64           ← IPv6 global
 ipv6 address FE80::1 link-local         ← IPv6 link-local (OBLIGATOIRE)
 no shutdown
```

---

## 🔍 Lire show ipv6 ospf neighbor

```
Neighbor ID   Pri  State        Dead Time  Interface
1.1.1.1         1  FULL/  -     00:00:36   GigabitEthernet0/0
               │   │     │
               │   │     └─ - = P2P (pas de DR/BDR)
               │   └─ État adjacence
               └─ Format IPv4 TOUJOURS

FULL/- = lien P2P opérationnel ✓
FULL/DR = ce voisin est DR sur multi-accès
INIT = Hello reçu mais pas de retour (problème !)
2WAY = bidirectionnel mais pas encore adjacent
```

---

## ✅ Vérifications essentielles

```cisco
show ipv6 ospf neighbor    → adjacences IPv6 (+ IPv4 via Multi-AF)
show ip route ospf         → routes IPv4 apprises par OSPFv3
show ipv6 route ospf       → routes IPv6 apprises par OSPFv3
show ipv6 ospf interface   → coût, area, hello interval
show ospfv3 neighbor       → variante détaillée
```

---

## 🌐 3 mécanismes de transition

```
DOUBLE STACK  → IPv4 + IPv6 sur même interface (ce TP)
               Quand : réseau progressivement mis à jour
               
TUNNELING     → IPv6 encapsulé dans IPv4 (comme GRE)
               Quand : traverser réseau IPv4 non migré
               
NAT64         → Translation IPv6 ↔ IPv4
               Quand : hôte IPv6 pur vers serveur IPv4 pur
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| Oublier `ipv6 unicast-routing` | Toujours en premier ! |
| Router-ID en format IPv6 | Toujours IPv4 : `router-id 1.1.1.1` |
| `network` dans le process OSPFv3 | Utiliser `ospfv3 1 ipv4 area 0` sur l'interface |
| Oublier la commande IPv6 AF | `address-family ipv6 unicast` dans le process |
| Link-local manquante | `ipv6 address FE80::X link-local` sur chaque interface |

---

## 🔑 Adresses clés IPv6

```
FF02::5  = Tous les routeurs OSPF (Hello OSPFv3)
FF02::6  = Routeurs DR/BDR OSPF
FE80::/10 = Link-Local (non routable, next-hop OSPFv3)
::1/128   = Loopback IPv6
2000::/3  = Global Unicast (routable)
```

---

*Aide-Mémoire OSPFv3 Multi-AF — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S2*
*Compétences S2.2 · S2.6 · C2.2 · C2.3*
