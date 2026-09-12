# 🔬 TRAVAUX PRATIQUES — S2 · 3ᵉ ANNÉE · E31
## OSPFv3 Multi-AF : Dual Stack IPv4/IPv6 sur 3 routeurs

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Packet Tracer**
> **Fichier .pkt** : `S2_E31_OSPFv3_DualStack.pkt` (fourni par l'enseignant)
> **Épreuve ciblée** : **E31** – Épreuve pratique infrastructure réseau

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S2.2** | Configurer OSPFv3 Multi-AF sur 3 routeurs |
| **S2.6** | Mettre en œuvre le double stack IPv4/IPv6 |
| **C2.2** | Appliquer les commandes IOS OSPFv3 |
| **C2.3** | Vérifier et diagnostiquer avec `show ipv6 ospf neighbor` |

---

## 🗺️ Topologie du TP

```
PC_A ─────────────────────────────────────────────────── PC_B
IPv4 : 192.168.1.10/24          |                IPv4 : 192.168.3.10/24
IPv6 : 2001:DB8:1::10/64        |                IPv6 : 2001:DB8:3::10/64
GW   : 192.168.1.1 / ::1        |                GW   : 192.168.3.1 / ::1
                                 |
          ┌──────────┐   10.0.12.0/30           ┌──────────┐   10.0.23.0/30    ┌──────────┐
          │    R1    ├──────────────────────────┤    R2    ├──────────────────┤    R3    │
          │ ID:1.1.1 │  2001:DB8:12::/64        │ ID:2.2.2 │  2001:DB8:23::/64 │ ID:3.3.3 │
          └──────────┘                          └──────────┘                   └──────────┘
          Gi0/0 : 192.168.1.1  Gi0/1 : 10.0.12.1  Gi0/0 : 10.0.12.2  Gi0/1 : 10.0.23.1
                  2001:DB8:1::1       2001:DB8:12::1        2001:DB8:12::2       2001:DB8:23::1
```

---

## 🟢 NIVEAU 1 — Activer IPv6 et configurer l'adressage dual stack (15 min)

### Sur R1

**1.1** — Active le routage IPv6 :

```cisco
R1(config)# _______________________________________________
```

**1.2** — Configure l'interface Gi0/0 en dual stack (IPv4 + IPv6) :

```cisco
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address _________________ _________________
R1(config-if)# ipv6 address _________________ (adresse globale)
R1(config-if)# ipv6 address FE80::1 link-local
R1(config-if)# no shutdown
```

**1.3** — Configure Gi0/1 (lien WAN vers R2) :

```cisco
R1(config)# interface GigabitEthernet0/1
R1(config-if)# ip address _________________ _________________
R1(config-if)# ipv6 address _________________
R1(config-if)# ipv6 address _________________ link-local
R1(config-if)# no shutdown
```

**1.4** — Configure l'interface Loopback (pour le Router-ID stable) :

```cisco
R1(config)# interface Loopback0
R1(config-if)# ip address 1.1.1.1 255.255.255.255
```

**1.5** — Vérifie l'adressage dual stack sur R1 :

```cisco
R1# show ip interface brief | include Gi0
R1# show ipv6 interface brief | include Gi0
```

```
Gi0/0 IPv4 : ___________________   Gi0/0 IPv6 global : ___________________
Gi0/1 IPv4 : ___________________   Gi0/1 IPv6 global : ___________________
```

> Répète les étapes 1.1-1.4 pour **R2** et **R3** (selon le plan d'adressage fourni).

---

## 🟡 NIVEAU 2 — Configurer OSPFv3 Multi-AF (20 min)

### Sur R1

**2.1** — Crée le processus OSPFv3 Multi-AF :

```cisco
R1(config)# router ospfv3 1
R1(config-router)# router-id _______________
R1(config-router)# address-family ipv4 unicast
R1(config-router-af)# exit-address-family
R1(config-router)# address-family ipv6 unicast
R1(config-router-af)# exit-address-family
```

**2.2** — Active OSPFv3 sur les deux interfaces (les deux AF) :

```cisco
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ospfv3 1 _______ area 0
R1(config-if)# ospfv3 1 _______ area 0

R1(config)# interface GigabitEthernet0/1
R1(config-if)# ospfv3 1 _______ area 0
R1(config-if)# ospfv3 1 _______ area 0
```

> Répète pour R2 et R3 (router-id 2.2.2.2 et 3.3.3.3).

### Vérification des adjacences

**2.3** — Sur R2, vérifie les adjacences OSPFv3 :

```cisco
R2# show ipv6 ospf neighbor
```

```
Recopie la sortie :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**2.4** — Analyse la sortie :

```
Voisin 1 : Router-ID = _______________   État = _______________
Voisin 2 : Router-ID = _______________   État = _______________
Le symbole après l'état (FULL/___) indique : _______________________________
```

**2.5** — Vérifie que les deux AF fonctionnent sur R2 :

```cisco
R2# show ip route ospf
R2# show ipv6 route ospf
```

```
Routes IPv4 apprises via OSPFv3 :
O ____________________________________________
O ____________________________________________

Routes IPv6 apprises via OSPFv3 :
O ____________________________________________
O ____________________________________________
```

---

## 🟠 NIVEAU 3 — Tester la connectivité dual stack (15 min)

**3.1** — Depuis PC_A, teste la connectivité **IPv4** :

```
ping 192.168.3.10
```

```
Résultat : ☐ Succès !!!!!    ☐ Échec
```

**3.2** — Depuis PC_A, teste la connectivité **IPv6** :

```
ping 2001:DB8:3::10
```

```
Résultat : ☐ Succès !!!!!    ☐ Échec
```

**3.3** — Depuis PC_A, effectue un traceroute IPv6 :

```
tracert 2001:DB8:3::10     (Windows PT)
```

```
Hop 1 : _____________________ (quelle adresse de R1 ?)
Hop 2 : _____________________ (quelle adresse de R2 ?)
Hop 3 : _____________________ (quelle adresse de R3 ?)
Hop 4 : 2001:DB8:3::10 (PC_B)
```

**Question 3.4** — Dans le traceroute IPv6, les adresses des routeurs sont-elles des adresses **globales** (2001:...) ou des adresses **link-local** (FE80::) ?

```
Type d'adresses dans le traceroute : ___________________
Explication : le next-hop OSPFv3 utilise les adresses ______________ donc les ICMP
Time Exceeded reviennent depuis les adresses ______________ des routeurs
```

---

## 🔵 NIVEAU 4 — Analyser les différences OSPFv2 / OSPFv3 (15 min)

**4.1** — Compare les tables de routage IPv4 sur R2 selon le protocole :

```
Avec OSPFv2 (rappel 2A S3) :
  La commande d'activation était dans le process : network X.X.X.X wildcard area N
  Les routes apparaissaient avec le code : O

Avec OSPFv3 Multi-AF :
  La commande d'activation est sur l'interface : ospfv3 1 ______ area N
  Les routes apparaissent avec le code : ☐ O   ☐ O IA   ☐ OE2
```

**4.2** — Vérifie l'adresse multicast utilisée par OSPFv3 :

```cisco
R1# debug ipv6 ospf events
```

*(Observer quelques lignes puis désactiver avec `no debug all`)*

```
Adresse multicast Hello OSPFv3 observée : _________________________________
Comparer avec OSPFv2 : 224.0.0.5 → OSPFv3 : ______________________________
```

**4.3** — Vérifie le coût OSPF sur les interfaces de R2 :

```cisco
R2# show ipv6 ospf interface GigabitEthernet0/0
```

```
Coût affiché : _______
Ce coût est : ☐ identique au coût OSPFv2 ☐ différent
Le calcul du coût est donc : ☐ identique ☐ différent entre OSPFv2 et OSPFv3
```

**4.4** — Sur R1, modifie le Router-ID en `11.11.11.11` et observe l'impact :

```cisco
R1(config)# router ospfv3 1
R1(config-router)# router-id 11.11.11.11
R1(config-router)# end
R1# clear ipv6 ospf process
```

```
Après le changement de Router-ID :
  show ipv6 ospf neighbor sur R2 : le voisin R1 passe en état _______________
  Après reconvergence : le nouveau Router-ID de R1 est _______________
Conclusion : le Router-ID doit être ________________________ dans un domaine OSPF
```

> **Remettre le Router-ID à `1.1.1.1` avant de continuer**

---

## 🔴 NIVEAU 5 — Scénario de transition : ajouter IPv6 sur une infra existante (15 min)

> **Contexte** : Imagine que R1, R2, R3 étaient configurés avec OSPFv2 (IPv4 seulement).
> Tu dois **ajouter IPv6** sans perturber le service IPv4 existant.
> C'est exactement le scénario réel d'une migration.

**5.1** — Si OSPFv2 était déjà en place, quelle serait ta démarche pour migrer vers OSPFv3 Multi-AF ? Classe les étapes dans le bon ordre :

```
Étapes à ordonner (numéroter de 1 à 5) :

☐ Ajouter `ospfv3 1 ipv6 area 0` sur chaque interface
☐ Activer `ipv6 unicast-routing`
☐ Configurer les adresses IPv6 sur les interfaces
☐ Créer le process `router ospfv3 1` avec les deux address-family
☐ Supprimer l'ancien `router ospf 1` (OSPFv2) après vérification

Mon ordre : ___ → ___ → ___ → ___ → ___
```

**5.2** — Pendant la migration, peut-on faire coexister temporairement OSPFv2 ET OSPFv3 Multi-AF sur le même routeur ? Quel est l'avantage de cette approche ?

```
Coexistence OSPFv2 + OSPFv3 Multi-AF : ☐ Possible ☐ Impossible
Avantage : ___________________________________________________________________
Risque : ____________________________________________________________________
```

**5.3** — Complète le tableau comparatif final :

| Critère | OSPFv2 | OSPFv3 Multi-AF |
|---|---|---|
| Activation | `network` dans le process | |
| Multicast Hello | 224.0.0.5 | |
| Next-hop | Adresse IPv4 | |
| Router-ID format | IPv4 | |
| Transporte | IPv4 uniquement | |
| Commande `ipv6 unicast-routing` | Non nécessaire | |

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Configurer `ipv6 unicast-routing` | ☐ | ☐ | ☐ |
| Configurer adresses IPv4 ET IPv6 sur une interface | ☐ | ☐ | ☐ |
| Créer un process `router ospfv3 1` Multi-AF | ☐ | ☐ | ☐ |
| Activer OSPFv3 sur une interface (`ospfv3 1 ipv4/ipv6 area 0`) | ☐ | ☐ | ☐ |
| Lire `show ipv6 ospf neighbor` et interpréter l'état FULL | ☐ | ☐ | ☐ |
| Ping et traceroute IPv6 end-to-end | ☐ | ☐ | ☐ |
| Expliquer la différence OSPFv2 / OSPFv3 Multi-AF | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.1 — Adressage dual stack correct sur les 3 routeurs | /5 |
| Niv.2 — OSPFv3 Multi-AF convergé, adjacences FULL | /7 |
| Niv.3 — Ping IPv4 ET IPv6 end-to-end réussis | /5 |
| Niv.4 — Analyse OSPFv2 vs OSPFv3 | /5 |
| Niv.5 — Stratégie de migration expliquée | /3 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 1

```
R1(config)# ipv6 unicast-routing

R1(config)# interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:DB8:1::1/64
 ipv6 address FE80::1 link-local
 no shutdown

R1(config)# interface GigabitEthernet0/1
 ip address 10.0.12.1 255.255.255.252
 ipv6 address 2001:DB8:12::1/64
 ipv6 address FE80::1 link-local
 no shutdown
```

## Correction Niveau 2

```
router ospfv3 1
 router-id 1.1.1.1
 address-family ipv4 unicast
 exit-address-family
 address-family ipv6 unicast
 exit-address-family

interface GigabitEthernet0/0
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
interface GigabitEthernet0/1
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0

show ipv6 ospf neighbor → FULL/- pour les 2 voisins (lien P2P → pas de DR/BDR)
```

## Correction Niveau 3

```
3.4 : Le traceroute IPv6 affiche les adresses GLOBALES (2001:DB8:...) car les routeurs
répondent aux ICMP avec l'adresse de l'interface qui a reçu le paquet, qui est
l'adresse globale (pas la link-local).
Note : dans certaines implémentations, les adresses link-local peuvent apparaître.
```

## Correction Niveau 4

```
4.4 : Changement de Router-ID → adjacences tombent (les Hello contiennent l'ancien ID)
→ reconvergence avec le nouvel ID → panne temporaire du routage
Conclusion : Le Router-ID doit être UNIQUE et STABLE dans un domaine OSPF
```

## Correction Niveau 5

```
5.1 Ordre :
  1. ipv6 unicast-routing
  2. Configurer adresses IPv6 sur les interfaces
  3. Créer router ospfv3 1 avec les deux AF
  4. Ajouter ospfv3 1 ipv6 area 0 sur chaque interface
  5. Supprimer router ospf 1 (après validation que IPv4 fonctionne toujours)

5.2 : Coexistence OSPFv2 + OSPFv3 Multi-AF = POSSIBLE
→ Avantage : migration progressive sans coupure du service IPv4
→ Risque : duplication des routes IPv4 dans deux tables (à surveiller)
```

---

*TP OSPFv3 Multi-AF + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S2*
*Document Portfolio E31 — Compétences S2.2 · S2.6 · C2.2 · C2.3*
