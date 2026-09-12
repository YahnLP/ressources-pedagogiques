# 📝 DEVOIR & LIVRABLE PORTFOLIO — S14 · 2ᵉ ANNÉE · E31
## Bilan de parcours : Sujet intégré CCNA · Analyse · Configuration · Dépannage

---

> **Module** : E31 – Infrastructure Réseau — Bilan de compétences
> **Épreuve visée** : **E31** – Épreuve pratique · **CCNA 200-301**
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 60 min)
> **Format du rendu** : Fiche complétée + commandes IOS + schéma d'architecture

---

## 📌 Compétences évaluées (bilan de parcours)

| Code | Compétence | Séance | Barème |
|---|---|---|---|
| **S2.1** | VLANs, trunks, inter-VLAN routing | A1 | /15 |
| **S2.2** | OSPF — config, vérification, dépannage | S3 | /20 |
| **S2.3** | Routage statique + table de routage | S2 | /15 |
| **S3.3** | EtherChannel LACP | S13 | /20 |
| **C2.3** | Diagnostiquer depuis sorties de commandes | S2-S13 | /20 |
| **C3.1** | Documenter l'infrastructure (schéma) | Toutes | /10 |
| | **TOTAL** | | **/100** |

---

## 🎯 Mise en situation professionnelle

> **Tu es technicien réseau junior** dans une entreprise de 3 sites.
> Le réseau vient d'être partiellement installé par un prestataire qui n'a pas terminé.
> Le responsable réseau te confie le dossier avec ces mots :
>
> *"Tu as 3 problèmes à résoudre et une configuration à finir. Les utilisateurs du Site B
> ne peuvent pas joindre les serveurs du Site C. Le Site A fonctionne mais je ne sais pas trop
> comment c'est configuré. Tu as la journée."*

---

## 🅰️ PARTIE A — En classe (45 min)

### 🔎 Exercice 1 — Analyser l'existant (/30)

> Le prestataire t'a laissé les sorties de commandes suivantes.

**Sortie 1 — R_B `show ip route`**

```
Codes: C - connected, S - static, O - OSPF

      10.0.0.0/8 is variably subnetted
C        10.0.12.0/30 is directly connected, GigabitEthernet0/1
C        10.0.23.0/30 is directly connected, GigabitEthernet0/2
O     192.168.10.0/24 [110/2] via 10.0.12.1
O     192.168.20.0/24 [110/2] via 10.0.12.1
```

**Sortie 2 — SW_B `show etherchannel summary`**

```
Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------
1      Po1(SD)         LACP      Gi0/1(D)   Gi0/2(I)
```

**Sortie 3 — SW_B `show interfaces Gi0/2`**

```
GigabitEthernet0/2 is up, line protocol is up
  Half-duplex, 100Mb/s
```

**Sortie 4 — SW_C `show interfaces Gi0/2`**

```
GigabitEthernet0/2 is up, line protocol is up
  Full-duplex, 1000Mb/s (Auto)
```

---

**1.a** — Sur R_B, la route vers le réseau `192.168.30.0/24` (réseau du Site C) est-elle présente ?
Quelle est la conséquence sur la connectivité Site B → Site C ? *(5 pts)*

```
Route 192.168.30.0/24 : ☐ Présente ☐ ABSENTE
Conséquence : _________________________________________________________________
Type de panne : _______________________________________________________________
```

**1.b** — La table de routage de R_B montre qu'il connaît les réseaux du Site A via OSPF.
Cela prouve que R_A et R_B sont voisins OSPF. Quelle commande sur R_B confirme ce fait et quel état dois-tu voir ? *(4 pts)*

```
Commande : ___________________________________________________________________
État attendu entre R_A et R_B : ______________________________________________
```

**1.c** — `Po1(SD)` sur SW_B : décris précisément ce que cela signifie et l'impact sur le trafic. *(6 pts)*

```
S = ___________ D = ___________
Po1(SD) signifie : ____________________________________________________________
Impact : les _______ VLANs qui devaient passer sur Po1 ________________________
```

**1.d** — Gi0/1 est en état (D) et Gi0/2 en état (I). Pour chaque port, identifie la cause et propose la correction : *(10 pts)*

| Port | Code | Cause précise | Commande de correction |
|---|---|---|---|
| Gi0/1 | (D) | | |
| Gi0/2 | (I) | | |

**1.e** — Si la panne de Gi0/2 (vitesse/duplex) est corrigée, la panne de Gi0/1 (câble déconnecté) persiste. Quel sera l'état du Po1 ? Quel sera l'état de Gi0/2 une fois correctement configuré ? *(5 pts)*

```
Si seulement Gi0/2 est corrigé (Gi0/1 reste D) :
  Po1 état : _______________  (UP ou DOWN ? Le bundle peut-il se former avec 1 seul port ?)
  Gi0/2 état : _______________
Trafic transitant : ☐ Oui, via Gi0/2 seulement ☐ Non, le bundle reste DOWN
```

---

### ⌨️ Exercice 2 — Compléter la configuration de R_C (/15)

> R_C (Site C) n'est pas encore configuré pour OSPF.
> Le lien R_B ↔ R_C est `10.0.23.0/30` (R_B=.1, R_C=.2).
> R_C doit annoncer `192.168.30.0/24` (son réseau local) dans OSPF Area 0.
> Router-ID de R_C : `3.3.3.3` (via Loopback 0 : 3.3.3.3/32).

**2.a** — Écris la configuration OSPF complète de R_C : *(10 pts)*

```cisco
! R_C — Configuration OSPF complète
R_C(config)# ________________________________________________________________
R_C(config-router)# __________________________________________________________
R_C(config-router)# __________________________________________________________
R_C(config-router)# __________________________________________________________
R_C(config-router)# __________________________________________________________
```

**2.b** — Après l'ajout d'OSPF sur R_C, quelle commande sur R_B confirme l'adjacence ? Quel résultat attends-tu ? *(5 pts)*

```
Commande : ___________________________________________________________________
Résultat attendu :
  Neighbor     State  Interface
  _________    _____  ___________     ← R_A côté
  _________    _____  ___________     ← R_C côté (nouveau)
```

---

## 🅱️ PARTIE B — En autonomie (/55)

### 🏗️ Exercice 3 — Concevoir une extension (/25)

> Le DSI souhaite ajouter un **Site D** au réseau.
> Plan d'adressage imposé :
> - VLAN 10 Site D : `192.168.40.0/24`
> - VLAN 20 Site D : `192.168.50.0/24`
> - Lien WAN R_C ↔ R_D : `10.0.34.0/30`
> - R_D doit utiliser OSPF Area 0
> - EtherChannel LACP (2 liens) entre SW_D_A et SW_D_B

**3.a** — Écris la configuration complète de **R_D** : interfaces WAN, sous-interfaces inter-VLAN, Loopback (4.4.4.4/32), et OSPF. *(15 pts)*

```cisco
! R_D — Configuration complète

! Loopback
___________________________________________________________________________

! Interface WAN vers R_C
___________________________________________________________________________
___________________________________________________________________________

! Sous-interfaces inter-VLAN (lien vers SW_D_A)
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

! OSPF
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**3.b** — Écris la configuration EtherChannel LACP sur **SW_D_A** pour les 2 liens Gi0/1 et Gi0/2 vers SW_D_B, avec le trunk permettant les VLANs 10 et 20 : *(10 pts)*

```cisco
! SW_D_A — EtherChannel + trunk

___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

---

### 🔍 Exercice 4 — Analyse de sortie de commande (/20)

> Voici la sortie `show ip route` de R_A dans le réseau final (Sites A, B, C, D).

```
R_A# show ip route
Codes: C - connected, S - static, O - OSPF, IA - inter area

C    192.168.10.0/24 is directly connected, GigabitEthernet0/0.10
C    192.168.20.0/24 is directly connected, GigabitEthernet0/0.20
C    10.0.12.0/30 is directly connected, GigabitEthernet0/1
O    10.0.23.0/30 [110/2] via 10.0.12.2, GigabitEthernet0/1
O    10.0.34.0/30 [110/3] via 10.0.12.2, GigabitEthernet0/1
O    192.168.30.0/24 [110/3] via 10.0.12.2, GigabitEthernet0/1
O    192.168.40.0/24 [110/4] via 10.0.12.2, GigabitEthernet0/1
O    192.168.50.0/24 [110/4] via 10.0.12.2, GigabitEthernet0/1
```

**4.a** — Combien de sauts (routeurs) séparent R_A de Site D (192.168.40.0) ? Justifie depuis la table. *(5 pts)*

```
Coût OSPF vers 192.168.40.0 : [110/___]
Coût d'un lien GigabitEthernet (défaut) : _______
Nombre de liens (sauts routeurs) : _____ → chemin : R_A → ___ → ___ → ___ → Site D
```

**4.b** — Le lien R_B ↔ R_C (10.0.23.0/30) tombe en panne. Décris précisément ce qui se passe côté OSPF et dans la table de routage de R_A : *(8 pts)*

```
1. R_C envoie un nouveau LSA indiquant : _______________________________________
2. R_B reçoit ce LSA et ________________________________________________________
3. Tous les routeurs recalculent avec : ________________________________________
4. Dans la table de R_A, les routes vers Site C (192.168.30.0) et Site D :
   ☐ Disparaissent (plus de chemin)
   ☐ Restent inchangées
   ☐ Changent de métrique
   Explication : _______________________________________________________________
```

**4.c** — Quelle commande sur R_A permettrait de tracer le chemin exact vers `192.168.40.10` et de voir chaque routeur traversé ? Que verra-t-on dans la sortie ? *(7 pts)*

```
Commande : ___________________________________________________________________
Sortie attendue :
  1  10.0.12.2   (R_B)
  2  ___________  (R_C)
  3  ___________  (R_D)
  4  192.168.40.10 (PC destination)
```

---

### 📐 Exercice 5 — Schéma d'architecture (/10)

> Dessine le schéma complet du réseau 4 sites avec :
> - Les équipements (R_A, R_B, R_C, R_D, switches, PCs)
> - Les liens WAN avec leurs adresses réseau
> - Les VLANs sur chaque site
> - Les EtherChannel indiqués par les doubles liaisons
> - Le domaine OSPF Area 0 encerclé en pointillé

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏅 Barème global et grille Qualiopi

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Analyser sorties de commandes | C2.3 + S3.3 | /30 | ≥ 17 |
| Ex. 2 — Config OSPF sur R_C | S2.2 | /15 | ≥ 8 |
| Ex. 3 — Extension Site D | S2.2 + S3.3 | /25 | ≥ 14 |
| Ex. 4 — Lecture table de routage | S2.3 + S2.2 | /20 | ≥ 11 |
| Ex. 5 — Schéma d'architecture | C3.1 | /10 | ≥ 5 |
| **TOTAL** | | **/100** | **≥ 55** |

> 📌 **Note Qualiopi** : Ce devoir constitue une **preuve de bilan d'acquisition** de toutes les compétences E31 de 2ᵉ année. À conserver avec signature enseignant et date.

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** : Route 192.168.30.0/24 ABSENTE → R_B ne sait pas joindre Site C → les paquets Site B → Site C sont droppés sur R_B → route manquante dans OSPF (R_C pas encore configuré)

**1.b** : `show ip ospf neighbor` → état FULL avec 10.0.12.1 (R_A)

**1.c** : S=Layer2, D=Down → Po1 est un port-channel L2 qui est complètement DOWN → aucun trafic inter-switches sur Po1

**1.d** :

| Port | Cause | Fix |
|---|---|---|
| Gi0/1 (D) | Câble physiquement déconnecté (notconnect) | Rebrancher physiquement le câble |
| Gi0/2 (I) | Vitesse/duplex incompatible (100M half-duplex vs 1G full-duplex SW_C) | `speed auto` et `duplex auto` sur SW_B Gi0/2 |

**1.e** : Avec 1 seul port opérationnel, le bundle EtherChannel peut se former (min 1 port actif) → Po1(SU), Gi0/2(P), Gi0/1(D) → trafic transite via Gi0/2 uniquement (1 Gbps)

## Correction Exercice 2

```cisco
R_C(config)# interface loopback 0
R_C(config-if)# ip address 3.3.3.3 255.255.255.255 / no shutdown
R_C(config)# router ospf 1
R_C(config-router)# router-id 3.3.3.3
R_C(config-router)# network 10.0.23.0 0.0.0.3 area 0
R_C(config-router)# network 192.168.30.0 0.0.0.255 area 0
R_C(config-router)# passive-interface GigabitEthernet0/1
```

## Correction Exercice 3

**R_D** :
```cisco
interface loopback 0
 ip address 4.4.4.4 255.255.255.255
interface GigabitEthernet0/1
 ip address 10.0.34.2 255.255.255.252 / no shutdown
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.40.1 255.255.255.0
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.50.1 255.255.255.0
router ospf 1
 router-id 4.4.4.4
 network 10.0.34.0 0.0.0.3 area 0
 network 192.168.40.0 0.0.0.255 area 0
 network 192.168.50.0 0.0.0.255 area 0
 passive-interface GigabitEthernet0/0.10
 passive-interface GigabitEthernet0/0.20
```

## Correction Exercice 4

**4.a** : Coût [110/4] → 4 liens GigabitEthernet (coût 1 chacun) = 4 sauts → R_A → R_B → R_C → R_D → Site D

**4.b** : R_C et R_B inondent un nouveau LSA "lien R_B↔R_C DOWN" → tous les routeurs recalculent SPF → les routes vers Site C et Site D **disparaissent** de la table de R_A (plus de chemin alternatif dans cette topologie simple)

**4.c** : `traceroute 192.168.40.10` → 4 hops : R_B (10.0.12.2) · R_C (10.0.23.2) · R_D (10.0.34.2) · 192.168.40.10

---

*Devoir Bilan Portfolio + Correction — Ne pas distribuer avant le rendu*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S14*
*Épreuves E31 + CCNA 200-301 | Bilan compétences C2.2 · C2.3 · S2.1 · S2.2 · S2.3 · S3.3 · C3.1*
*Conforme référentiel Qualiopi*
