# 🔬 TRAVAUX PRATIQUES — S13 · 2ᵉ ANNÉE · E31
## EtherChannel LACP : Configuration · Vérification · Redondance · Dépannage

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Packet Tracer**
> **Fichier .pkt** : `S13_E31_EtherChannel.pkt` (fourni par l'enseignant)
> **Épreuve ciblée** : **E31** – Épreuve pratique infrastructure réseau

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S2.1** | Configurer EtherChannel LACP entre switches |
| **S2.2** | Choisir les bons modes LACP |
| **S2.3** | Configurer et vérifier le load balancing |
| **C2.2** | Appliquer les commandes IOS sur switches |
| **C2.3** | Diagnostiquer des pannes via `show etherchannel summary` |

---

## 🗺️ Topologie du TP

```
            VLAN 10 : 192.168.10.0/24
  PC_A ─────────────────────┐
  (192.168.10.10)            │
                           [SW1] ═══════════════ [SW2]
  PC_C ─────────────────────┘   Po1 (Gi0/1-Gi0/4)    │─────── PC_B (192.168.10.20)
  (192.168.20.10)                4 liens physiques      └─────── PC_D (192.168.20.20)
            VLAN 20 : 192.168.20.0/24

VLANs présents sur les deux switches :
  VLAN 10 : PC_A et PC_B
  VLAN 20 : PC_C et PC_D

État initial : 4 câbles branchés MAIS EtherChannel NON configuré
→ STP bloque 3 des 4 liens → seul 1 lien actif → 1 Gbps effectif
```

---

## 🟢 NIVEAU 1 — Observer l'état initial (10 min)

> **Sans rien configurer**, observe ce que fait STP sans EtherChannel.

**1.1** — Sur SW1, tape `show spanning-tree vlan 10` et note les états des ports Gi0/1 à Gi0/4 :

```
Gi0/1 : rôle = __________ état = __________
Gi0/2 : rôle = __________ état = __________
Gi0/3 : rôle = __________ état = __________
Gi0/4 : rôle = __________ état = __________
```

**1.2** — Combien de ports sont en état `FWD` (forwarding) et combien sont bloqués (`BLK`) ?

```
FWD : ______  BLK : ______
Bande passante effective actuellement : _______ Gbps
```

**1.3** — PC_A peut-il pinguer PC_B ?

```
ping 192.168.10.20 depuis PC_A → ☐ Succès ☐ Échec
```

---

## 🟡 NIVEAU 2 — Configurer EtherChannel LACP (20 min)

### Sur SW1

**2.1** — Assigne les 4 interfaces au groupe 1 en mode LACP active :

```cisco
SW1(config)# interface range GigabitEthernet0/1-4
SW1(config-if-range)# channel-group 1 mode active
SW1(config-if-range)# exit
```

**2.2** — Configure le port-channel en trunk :

```cisco
SW1(config)# interface port-channel 1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan all
SW1(config-if)# exit
```

### Sur SW2 (même configuration)

**2.3** — Reproduis exactement la même configuration sur SW2 :

```cisco
SW2(config)# _________________________________________________________________
SW2(config-if-range)# ________________________________________________________
SW2(config-if-range)# ________________________________________________________
SW2(config)# _________________________________________________________________
SW2(config-if)# ______________________________________________________________
SW2(config-if)# ______________________________________________________________
```

### Vérification

**2.4** — Tape `show etherchannel summary` sur SW1 et complète :

```
Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------
___    Po___(__)     ________    Gi0/1(___)  Gi0/2(___)  Gi0/3(___)  Gi0/4(___)
```

**2.5** — Tous les ports sont-ils en état `(P)` (bundled) ?

```
☐ Oui — port-channel opérationnel ✓
☐ Non — ports problématiques : ________________ état : _______
```

**2.6** — Retape `show spanning-tree vlan 10`. Comment STP voit-il maintenant les liens ?

```
Avant EtherChannel : STP voyait _______ ports séparés
Après EtherChannel  : STP voit _______ port (Po___)
État du port Po1 dans STP : __________
```

**2.7** — Ping PC_A → PC_B. Succès ? Et PC_C → PC_D ?

```
PC_A → PC_B (VLAN 10) : ☐ Succès ☐ Échec
PC_C → PC_D (VLAN 20) : ☐ Succès ☐ Échec
```

---

## 🟠 NIVEAU 3 — Configurer le load balancing et observer (15 min)

**3.1** — Configure le load balancing sur SW1 :

```cisco
SW1(config)# port-channel load-balance src-dst-ip
```

**3.2** — Vérifie la méthode active :

```cisco
SW1# show etherchannel load-balance
```

```
Méthode affichée : ___________________________________________________________
```

**3.3** — Depuis PC_A, génère plusieurs pings vers différentes destinations :

```
ping 192.168.10.20 (PC_B)
ping 192.168.10.1  (gateway SW2)
ping 192.168.20.20 (PC_D, VLAN différent — via routage)
```

**3.4** — Sur SW1, tape `show etherchannel 1 detail` et note les compteurs de paquets par interface membre :

```
Gi0/1 : packets sent = _______
Gi0/2 : packets sent = _______
Gi0/3 : packets sent = _______
Gi0/4 : packets sent = _______
```

**3.5** — La charge est-elle parfaitement équilibrée ? Explique pourquoi ou pourquoi pas.

```
Équilibrage observé : ☐ Parfait (25% par lien) ☐ Inégal
Explication : le hash src-dst-ip dépend des ___________________________________
Avec 2 PCs seulement, le nombre de flux différents est ________________________
Conclusion : ________________________________________________________________
```

---

## 🔵 NIVEAU 4 — Simuler et observer la redondance (15 min)

**4.1** — Lance un ping continu de PC_A vers PC_B (dans PT : `ping 192.168.10.20 -n 100`).

**4.2** — Pendant que le ping tourne, **shutdown** une interface membre sur SW1 :

```cisco
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# shutdown
```

**4.3** — Note ce qui se passe :

```
Paquets perdus pendant le shutdown : _______ (sur 100)
Le ping reprend-il après ? ☐ Oui ☐ Non
Délai de reconvergence observé : ☐ Immédiat ☐ Quelques secondes ☐ > 30s
```

**4.4** — Vérifie la nouvelle table EtherChannel :

```
show etherchannel summary
Gi0/1 : état = _____ (normal après shutdown)
Gi0/2, 0/3, 0/4 : état = _____
Bande passante restante du Po1 : _______ Gbps
```

**4.5** — Compare avec ce qui se passerait avec STP classique (sans EtherChannel) :

```
Sans EC : si Gi0/1 tombe, STP doit recalculer → délai de reconvergence = _______ secondes
Avec EC  : délai observé = _______ secondes (ou ms)
Avantage EC : _________________________________________________________________
```

**4.6** — Remets le lien en service :

```cisco
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# no shutdown
```

---

## 🔴 NIVEAU 5 — Dépannage : 3 pannes à résoudre (20 min)

> **L'enseignant a injecté 3 pannes dans le fichier `.pkt` de dépannage.**
> (Ouvrir le fichier `S13_E31_EtherChannel_PANNES.pkt`)

### Panne A — Identifier et corriger

**5.1** — Sur SW1 : `show etherchannel summary` :

```
Recopie la sortie obtenue :
___________________________________________________________________________
___________________________________________________________________________
```

**5.2** — Le port-channel est-il UP (SU) ou DOWN (SD) ?

```
État : ______   Le trafic passe-t-il ? ☐ Oui ☐ Non
```

**5.3** — Analyse : compare les modes sur SW1 et SW2 :

```cisco
SW1# show lacp 1 internal     (note le mode)
SW2# show lacp 1 internal     (note le mode)
```

```
Mode SW1 : __________   Mode SW2 : __________
Compatible ? ☐ Oui ☐ Non — car : _________________________________________
```

**5.4** — Correction (écris la commande) :

```cisco
SW___(config)# interface range GigabitEthernet0/1-4
SW___(config-if-range)# channel-group 1 mode ____________
```

---

### Panne B — Identifier et corriger

**5.5** — `show etherchannel summary` sur SW1 :

```
Copier ici les lignes de la sortie :
___________________________________________________________________________
```

Quel port est en état `(I)` (stand-alone) ?

```
Port problématique : Gi0/_____
```

**5.6** — Vérifie la vitesse de ce port sur SW1 et SW2 :

```cisco
SW1# show interfaces Gi0/___ | include duplex
SW2# show interfaces Gi0/___ | include duplex
```

```
SW1 Gi0/___: _______ Mbps   SW2 Gi0/___: _______ Mbps
Problème : _______________________________________________________________
```

**5.7** — Correction :

```cisco
SW___(config)# interface GigabitEthernet0/___
SW___(config-if)# _______________________________________________
```

---

### Panne C — Identifier et corriger

**5.8** — Le port-channel Po1 est UP mais PC_C (VLAN 20) ne peut pas joindre PC_D.
PC_A (VLAN 10) fonctionne normalement.

```
Symptôme précis : VLAN _______ ne passe pas · VLAN _______ fonctionne
```

**5.9** — Vérifie la configuration trunk du port-channel :

```cisco
SW1# show interfaces port-channel 1 trunk
```

```
Mode trunk sur Po1 : ________________________________________________________
VLANs autorisés : ___________________________________________________________
VLAN 20 est-il dans la liste ? ☐ Oui ☐ Non → c'est le problème
```

**5.10** — Correction :

```cisco
SW1(config)# interface port-channel 1
SW1(config-if)# _______________________________________________
SW2(config)# interface port-channel 1
SW2(config-if)# _______________________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Configurer EtherChannel LACP (channel-group mode active) | ☐ | ☐ | ☐ |
| Configurer le trunk sur le port-channel | ☐ | ☐ | ☐ |
| Lire `show etherchannel summary` et interpréter (P/I/D/s) | ☐ | ☐ | ☐ |
| Observer la redondance en cas de panne d'un membre | ☐ | ☐ | ☐ |
| Diagnostiquer mode incompatible | ☐ | ☐ | ☐ |
| Diagnostiquer vitesse différente | ☐ | ☐ | ☐ |
| Diagnostiquer trunk manquant | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.2 — EC LACP configuré, tous ports en (P) | /6 |
| Niv.3 — Load balancing configuré + observation | /4 |
| Niv.4 — Redondance observée, ping continu OK | /5 |
| Niv.5 — 3 pannes diagnostiquées et corrigées | /10 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 1

```
Sans EtherChannel, STP laisse 1 port en FWD (root port/designated) et bloque les 3 autres.
Seul 1 Gbps effectif. PC_A peut pinguer PC_B via le seul lien forwarding.
```

## Correction Niveau 2 (commandes SW2)

```cisco
SW2(config)# interface range GigabitEthernet0/1-4
SW2(config-if-range)# channel-group 1 mode active
SW2(config-if-range)# exit
SW2(config)# interface port-channel 1
SW2(config-if)# switchport mode trunk
SW2(config-if)# switchport trunk allowed vlan all
```

`show etherchannel summary` attendu : `1 Po1(SU) LACP Gi0/1(P) Gi0/2(P) Gi0/3(P) Gi0/4(P)`

## Correction Niveau 4

```
Paquets perdus lors du shutdown : 0 ou 1 (le paquet en transit au moment exact)
Délai de reconvergence : immédiat (< 1s) — LACP détecte la panne en ms
STP sans EC : 30-50 secondes de reconvergence (Forward Delay)
```

## Correction Niveaux 5 — Pannes

**Panne A** : mode `on` sur SW2 vs `active` sur SW1 → incompatible → `Po1(SD)`
→ Fix sur SW2 : `channel-group 1 mode active`

**Panne B** : Gi0/3 forcé à 100Mbps sur SW1 → vitesse ≠ 1Gbps → (I) stand-alone
→ Fix : `SW1(config-if)# speed auto` sur Gi0/3

**Panne C** : `switchport trunk allowed vlan 10` sur Po1 (VLAN 20 manquant)
→ Fix : `switchport trunk allowed vlan all` ou `switchport trunk allowed vlan add 20`

---

*TP EtherChannel + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S13*
*Document Portfolio E31 — Compétences S2.1 · S2.2 · S2.3 · C2.2 · C2.3*
