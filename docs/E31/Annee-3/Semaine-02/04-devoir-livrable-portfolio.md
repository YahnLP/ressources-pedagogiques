# 📝 DEVOIR & LIVRABLE PORTFOLIO — S2 · 3ᵉ ANNÉE · E31
## OSPFv3 Multi-AF · Dual Stack · Transition IPv4/IPv6

---

> **Module** : E31 – Infrastructure Réseau — IPv6 et OSPFv3
> **Épreuve visée** : **E31** – Épreuve pratique
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S2.2** | OSPFv3 Multi-AF — concepts et configuration | /35 |
| **S2.6** | Transition IPv4/IPv6 — dual stack, mécanismes | /30 |
| **C2.2** | Écrire les commandes IOS OSPFv3 | /20 |
| **C2.3** | Analyser `show ipv6 ospf neighbor` | /15 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation

> **Tu es administrateur réseau** d'une entreprise qui reçoit la directive suivante :
> *"D'ici 6 mois, tous nos sites doivent être accessibles en IPv6.
> L'infrastructure OSPFv2 IPv4 existante ne doit pas être perturbée pendant la migration."*

---

## 🅰️ PARTIE A — En classe (45 min)

### 📡 Exercice 1 — Concepts OSPFv3 (/35)

**1.a** — Explique en 4 lignes pourquoi OSPFv3 Multi-AF est préféré à deux processus séparés (un OSPFv2 pour IPv4 + un OSPFv3 "classique" pour IPv6) : *(8 pts)*

```
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**1.b** — Complète le tableau comparatif OSPFv2 / OSPFv3 Multi-AF : *(12 pts)*

| Critère | OSPFv2 | OSPFv3 Multi-AF |
|---|---|---|
| Commande d'activation | `network X wildcard area N` dans le process | |
| Multicast Hello | 224.0.0.5 | |
| Format du Router-ID | Adresse IPv4 | |
| Next-hop dans la table de routage IPv6 | N/A | |
| Protocoles transportés | IPv4 uniquement | |
| Commande globale requise | Non | |

**1.c** — Un routeur OSPFv3 n'a **aucune interface IPv4** configurée. Comment s'assurer qu'il peut former des adjacences OSPF ? *(5 pts)*

```
Problème : le Router-ID est toujours au format ________________________________
Sans interface IPv4 : OSPF ne peut pas choisir automatiquement un Router-ID
Solution : _____________________________________________________________________
Commande exacte : ______________________________________________________________
```

**1.d** — Dans `show ipv6 ospf neighbor`, l'état affiché est `FULL/  -`.
Dans OSPFv2, on voyait `FULL/DR` ou `FULL/BDR`. Explique la différence. *(10 pts)*

```
Sur un réseau Ethernet multi-accès, OSPFv2/v3 élit : __________________________
Sur un lien point à point (WAN série ou connexion directe entre 2 routeurs) :
  L'élection DR/BDR est : ☐ Réalisée ☐ Inutile
  Le symbole affiché est : _______________
  Raison : ____________________________________________________________________
```

---

### ⌨️ Exercice 2 — Analyse de sortie (/15)

> Voici la sortie `show ipv6 ospf neighbor` relevée sur R_CENTRE :

```
          OSPFv3 Router with ID (10.10.10.10) (Process ID 1)

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
1.1.1.1           1   FULL/  -        00:00:37    3               GigabitEthernet0/0
2.2.2.2           1   2WAY/DROTHER    00:00:33    4               GigabitEthernet1/0
3.3.3.3           1   INIT/  -        00:00:28    5               GigabitEthernet2/0
```

**2.a** — Pour chaque voisin, identifie le problème (s'il y en a un) et propose une explication : *(9 pts)*

| Voisin | État | Problème ? | Explication probable |
|---|---|---|---|
| 1.1.1.1 | FULL/- | | |
| 2.2.2.2 | 2WAY/DROTHER | | |
| 3.3.3.3 | INIT/- | | |

**2.b** — Le voisin `3.3.3.3` est en état INIT. Cite 2 causes possibles : *(6 pts)*

```
Cause 1 : ____________________________________________________________________
Cause 2 : ____________________________________________________________________
Commande pour diagnostiquer : _________________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/50)

### ⌨️ Exercice 3 — Configuration OSPFv3 Multi-AF (/20)

> Topologie : 2 routeurs (R_A et R_B) reliés par un lien WAN `10.5.0.0/30` et `2001:DB8:AB::/64`.
> LAN de R_A : `172.16.1.0/24` + `2001:DB8:A::/64`
> LAN de R_B : `172.16.2.0/24` + `2001:DB8:B::/64`

**3.a** — Écris la configuration complète de **R_A** (adressage dual stack + OSPFv3 Multi-AF) : *(15 pts)*

```cisco
! R_A — Configuration complète dual stack + OSPFv3 Multi-AF

! Activer IPv6 routing
___________________________________________________________________________

! Interface LAN
interface GigabitEthernet0/0
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

! Interface WAN vers R_B
interface GigabitEthernet0/1
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

! Loopback (Router-ID)
___________________________________________________________________________
___________________________________________________________________________

! OSPFv3 Multi-AF
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**3.b** — Quelle commande taper sur R_A pour vérifier les adjacences OSPFv3 et quel résultat attendre ? *(5 pts)*

```
Commande : __________________________________________________________________
Résultat attendu :
  Neighbor ID = _____________   State = _____________   Interface = ___________
```

---

### 🌐 Exercice 4 — Mécanismes de transition (/20)

**4.a** — Pour chaque scénario, indique quel mécanisme de transition utiliser et pourquoi : *(12 pts)*

| Scénario | Mécanisme | Justification |
|---|---|---|
| Un FAI veut offrir la connectivité IPv6 à ses clients derrière un réseau cœur IPv4 non migré | | |
| Une entreprise veut que ses 500 postes accèdent aux serveurs en IPv4 ET en IPv6 | | |
| Un opérateur mobile 5G (IPv6 natif) veut que ses abonnés accèdent à un vieux serveur IPv4 uniquement | | |

**4.b** — Explique pourquoi OSPFv3 utilise les adresses **link-local** (FE80::) comme next-hop plutôt que les adresses globales (2001:...) : *(8 pts)*

```
Une adresse link-local est valable : ____________________________________________
Une adresse globale IPv6 peut : ☐ changer ☐ rester toujours identique
L'avantage d'utiliser FE80:: comme next-hop : ___________________________________
_______________________________________________________________________________
Inconvénient : les adresses FE80:: ne sont pas ________________ → impossible
à voir dans un traceroute depuis un réseau distant
```

---

### 📝 Exercice 5 — Plan de migration (/10)

> L'entreprise a actuellement OSPFv2 (IPv4) en production sur 10 routeurs.
> Elle veut migrer vers OSPFv3 Multi-AF **sans coupure de service**.

**5.a** — Décris la stratégie de migration en 5 étapes, dans l'ordre : *(6 pts)*

```
Étape 1 : ____________________________________________________________________
Étape 2 : ____________________________________________________________________
Étape 3 : ____________________________________________________________________
Étape 4 : ____________________________________________________________________
Étape 5 : ____________________________________________________________________
```

**5.b** — Peut-on faire coexister OSPFv2 et OSPFv3 Multi-AF temporairement ? Quel est le risque ? *(4 pts)*

```
Coexistence : ☐ Possible ☐ Impossible
Risque principal : ______________________________________________________________
Indicateur à surveiller : ______________________________________________________
```

---

## 🏅 Barème global

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Concepts OSPFv3 | S2.2 | /35 | ≥ 20 |
| Ex. 2 — Analyse show ipv6 ospf neighbor | C2.3 | /15 | ≥ 8 |
| Ex. 3 — Configuration IOS OSPFv3 Multi-AF | C2.2 | /20 | ≥ 11 |
| Ex. 4 — Mécanismes de transition | S2.6 | /20 | ≥ 11 |
| Ex. 5 — Plan de migration | S2.6 | /10 | ≥ 5 |
| **TOTAL** | | **/100** | **≥ 55** |

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** : 2 processus = 2 fois plus de Hello packets, 2 LSDBs à maintenir, 2 fois plus de config, risque de divergence · Multi-AF = 1 seul processus, 1 engine SPF partagé, config centralisée, moins de charge CPU/mémoire

**1.b** :

| Critère | OSPFv3 Multi-AF |
|---|---|
| Activation | `ospfv3 1 ipv4/ipv6 area N` sur l'interface |
| Multicast | FF02::5 / FF02::6 |
| Router-ID | Format IPv4 obligatoire |
| Next-hop IPv6 | Adresse link-local FE80:: |
| Transporte | IPv4 ET IPv6 |
| Commande globale | `ipv6 unicast-routing` obligatoire |

**1.c** : `router-id X.X.X.X` dans le process `router ospfv3 1`

**1.d** : P2P → DR/BDR inutile (seulement 2 routeurs) → le rôle est `-` · Sur réseau multi-accès Ethernet → DR/BDR élus pour réduire les adjacences (n² → n)

## Correction Exercice 2

**2.a** :

| Voisin | État | Problème | Explication |
|---|---|---|---|
| 1.1.1.1 | FULL/- | Aucun ✓ | Adjacence P2P opérationnelle |
| 2.2.2.2 | 2WAY/DROTHER | Normal sur réseau multi-accès | R_CENTRE n'est pas DR ni BDR sur ce segment |
| 3.3.3.3 | INIT/- | Problème ! | R_CENTRE reçoit les Hello de 3.3.3.3 mais 3.3.3.3 ne voit pas encore R_CENTRE dans ses Hello |

**2.b** : Cause 1 = Hello/Dead intervals différents · Cause 2 = Area IDs différents · Diagnostic = `show ipv6 ospf interface Gi2/0`

## Correction Exercice 3

```cisco
ipv6 unicast-routing

interface GigabitEthernet0/0
 ip address 172.16.1.1 255.255.255.0
 ipv6 address 2001:DB8:A::1/64
 ipv6 address FE80::A link-local
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
 no shutdown

interface GigabitEthernet0/1
 ip address 10.5.0.1 255.255.255.252
 ipv6 address 2001:DB8:AB::1/64
 ipv6 address FE80::A link-local
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
 no shutdown

interface Loopback0
 ip address 100.100.100.100 255.255.255.255

router ospfv3 1
 router-id 100.100.100.100
 address-family ipv4 unicast
 exit-address-family
 address-family ipv6 unicast
 exit-address-family
```

## Correction Exercice 4

**4.a** :
- FAI IPv4 core → Tunneling (6in4 ou 6rd) · transporter IPv6 sans changer l'infra
- 500 postes IPv4+IPv6 → Double Stack · natif, aucune translation
- Mobile 5G (IPv6 pur) → serveur IPv4 → NAT64 · translation par un équipement intermédiaire

**4.b** : Link-local valable sur un seul lien · L'adresse globale peut changer (renumbering) → instabilité · FE80:: est toujours présente même si le préfixe global change · Inconvénient = FE80 non routable → invisible dans traceroute depuis un autre réseau

## Correction Exercice 5

**5.a** :
1. Activer `ipv6 unicast-routing` sur tous les routeurs
2. Configurer les adresses IPv6 sur toutes les interfaces (dual stack)
3. Ajouter le process `router ospfv3 1` avec les deux AF sur chaque routeur
4. Ajouter `ospfv3 1 ipv6 area N` sur chaque interface
5. Valider la connectivité IPv6 end-to-end puis supprimer `router ospf 1` (OSPFv2)

**5.b** : Coexistence possible · Risque : routes IPv4 présentes en double dans deux processus → entrées redondantes, difficile à déboguer · Surveiller : `show ip route` ne doit pas avoir des doublons O avec des next-hops différents

---

*Devoir + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S2*
*Épreuve E31 | Compétences S2.2 · S2.6 · C2.2 · C2.3*
