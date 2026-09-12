# 🗂️ AIDE-MÉMOIRE CCNA RÉVISIONS — À PLASTIFIER
## Synthèse Commandes · VLANs · OSPF · EtherChannel · Dépannage · BAC PRO CIEL · E31 · S14

---

> *Dernière révision avant E31 et CCNA 200-301*

---

## ⚡ Les 10 commandes incontournables

```
1. ip address [IP] [MASQUE] + no shutdown
2. ip route [réseau] [masque] [next-hop]
3. router ospf 1 / network [X] [wildcard] area 0
4. switchport mode trunk
5. switchport access vlan [N]
6. channel-group [N] mode active
7. show ip route
8. show etherchannel summary
9. show ip ospf neighbor
10. ping [IP] / traceroute [IP]
```

---

## 📐 Masques et wildcards courants

```
/24 → 255.255.255.0   wildcard: 0.0.0.255
/30 → 255.255.255.252 wildcard: 0.0.0.3
/25 → 255.255.255.128 wildcard: 0.0.0.127
/16 → 255.255.0.0     wildcard: 0.255.255.255
/8  → 255.0.0.0       wildcard: 0.255.255.255
```

---

## 🔌 VLANs + Trunks + Inter-VLAN

```cisco
vlan 10 / name SALES
interface Gi0/0 / switchport mode access / switchport access vlan 10
interface Gi0/1 / switchport mode trunk / switchport trunk allowed vlan all
show vlan brief / show interfaces trunk

Inter-VLAN (sous-interfaces) :
interface Gi0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
```

---

## 🌐 OSPF — Essentiel

```cisco
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0
 passive-interface Gi0/0.10  (ne pas envoyer Hello sur les LANs)

Vérifier :
show ip ospf neighbor      → FULL = adjacence OK
show ip route              → O = intra-aire, O IA = inter-aire [110/coût]
show ip ospf interface     → coût (réf 100Mbps: GigaEth=1, FE=1, Série=64)

Coût = 10⁸ / débit(bps)
Wildcard = inverse du masque !
```

---

## ⚡ EtherChannel LACP

```cisco
interface range Gi0/1-4
 channel-group 1 mode active
interface port-channel 1
 switchport mode trunk / switchport trunk allowed vlan all
port-channel load-balance src-dst-ip

Compatibilité :
  active + active → ✓    active + passive → ✓
  passive + passive → ✗  active + on → ✗

Codes show etherchannel summary :
  (P) bundled ✓   (I) stand-alone ✗   (D) down ✗   (s) suspended ✗
  (SU) = Layer2 + actif ✓
```

---

## 🔁 Distances administratives

```
Connected (C) :   0
Static (S) :      1
OSPF (O) :      110
RIP (R) :       120
```

---

## 🔍 Dépannage express

```
Problème → Commande → Cause → Fix

EC stand-alone (I) → show interfaces Gi0/x | inc duplex
  → vitesse/duplex différent → speed auto + duplex auto

EC Po1(SD) → show lacp 1 internal + neighbor
  → modes incompatibles → active/active des deux côtés

VLAN ne passe pas → show interfaces Po1 trunk
  → trunk absent → switchport mode trunk

OSPF pas de voisin → show ip ospf interface
  → Hello/Dead intervals différents OU réseau mal annoté

Ping E2E échoue → traceroute → trouver le dernier hop
  → show ip route sur ce routeur → route manquante
```

---

## 📋 Séquence de vérification universelle

```
Après config → vérifier dans l'ordre :
1. no shutdown sur toutes les interfaces
2. show vlan brief → VLANs présents + ports
3. show interfaces trunk → liens trunk OK
4. show etherchannel summary → Po1(SU), ports (P)
5. show ip ospf neighbor → FULL
6. show ip route → routes O présentes
7. ping E2E (le test le plus difficile en dernier)
8. copy run start !
```

---

## ⚠️ Top 5 des erreurs qui font perdre des points

```
❌ Oublier no shutdown     → interface reste down
❌ Masque au lieu wildcard (OSPF) → network mal annoncé
❌ Config trunk sur Gi (pas Po1) → EtherChannel ignoré
❌ Pas de route retour     → ping aller OK, retour KO
❌ Pas de copy run start   → config perdue au redémarrage
```

---

*Aide-Mémoire CCNA — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S14*
*Bilan compétences C2.2 · C2.3 · S2.1 · S2.2 · S2.3 · S3.3*
