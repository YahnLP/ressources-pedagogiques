# 🗂️ AIDE-MÉMOIRE FINAL E31/CCNA — À PLASTIFIER
## Synthèse Ultime · Toutes Commandes · Tout le Programme · BAC PRO CIEL · E31 · S20

---

> *La feuille que tu glisses dans ta trousse le jour de l'épreuve*
> *(si autorisée — sinon à mémoriser)*

---

## ⚡ Les 10 commandes INCONTOURNABLES

```
1. ip address [IP] [MASQUE] + no shutdown
2. ip route [réseau] [masque] [next-hop]
3. router ospf 1 / network [X] [wildcard] area [N]
4. switchport mode trunk / allowed vlan all
5. channel-group 1 mode active
6. interface port-channel 1 / switchport mode trunk
7. class-map VOIX / priority percent 30 / service-policy output
8. ip route 0.0.0.0 0.0.0.0 [nh2] 5     ← route flottante
9. copy running-config tftp:
10. ping [IP] / traceroute [IP] / show ip route
```

---

## 📐 Valeurs à connaître par cœur

```
OSPF     : DA=110 · Hello=10s · Dead=40s · Multicast=224.0.0.5
           Coût = 10⁸ / débit(bps)
LACP     : active+active ✓ · passive+passive ✗ · active+on ✗
EtherCh  : (P)=actif ✓ · (I)=stand-alone ✗ · (D)=down ✗
QoS      : DSCP EF=46 (VoIP) · BE=0 (données)
TFTP     : UDP 69 · Convention : HOST_running_AAAA-MM-JJ_HHMM.cfg
Masques  : /24=0.0.0.255 · /30=0.0.0.3 · /32=0.0.0.0
Mémoire  : RAM=running · NVRAM=startup · Flash=IOS+archives
```

---

## 🔄 Séquence universelle d'un lab PT

```
1. Lire TOUT le sujet avant de commencer
2. Schéma rapide sur brouillon (2 min)
3. Couche 1 : no shutdown partout
4. Couche 2 : VLANs → trunks → EtherChannel
5. Couche 3 : IP → routes statiques → OSPF
6. Ping après chaque bloc
7. Fonctions avancées : QoS → VPN → HA
8. Tests finaux E2E (le cas le plus difficile)
9. copy run start sur TOUS les équipements
```

---

## ✅ Vérifications essentielles

```
show ip route              → table complète
show ip ospf neighbor      → FULL ?
show etherchannel summary  → Po1(SU), ports (P) ?
show interfaces trunk      → VLANs autorisés ?
show vlan brief            → ports bien assignés ?
show policy-map interface  → QoS visible ?
show interfaces Tunnel0    → up/up ?
ping [IP]                  → succès ?
```

---

## 🚨 Top 5 erreurs fatales

```
❌ Masque au lieu de wildcard dans OSPF
   /24 → 0.0.0.255 (PAS 255.255.255.0 !)

❌ Config trunk sur Gi0/x au lieu de Port-channel

❌ active+on → EC ne se forme pas → vérifier les deux côtés

❌ Pas de route retour → ping aller OK, retour KO

❌ Oublier copy run start → config perdue au redémarrage
```

---

## 🔑 Structures config rapides

```cisco
! OSPF
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0
 network 10.1.2.0 0.0.0.3 area 0
 passive-interface Gi0/0.10

! EtherChannel
interface range Gi0/1-4
 channel-group 1 mode active
interface port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan all

! Route flottante
ip route 0.0.0.0 0.0.0.0 10.1.2.1      ← principale DA=1
ip route 0.0.0.0 0.0.0.0 10.1.3.1 5    ← secours DA=5

! QoS LLQ
class-map match-any VOIX
 match dscp ef
policy-map QOS_WAN
 class VOIX
  priority percent 30
 class class-default
  fair-queue
interface Serial0/0/0
 service-policy output QOS_WAN

! Sauvegarde + restauration
copy running-config tftp:
erase startup-config
copy tftp: startup-config / reload
```

---

## 📊 Interprétation du score CCNA Readiness

```
≥ 36/40 → Excellent → CCNA accessible maintenant
32-35   → Très bon  → Finaliser 1-2 domaines
28-31   → Bon       → Révisions ciblées
24-27   → Moyen     → Plan 4 semaines
< 24    → Reprendre S2, S3, S13
```

---

*Aide-Mémoire Final E31/CCNA — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S20*
*Tout le programme en une page*
