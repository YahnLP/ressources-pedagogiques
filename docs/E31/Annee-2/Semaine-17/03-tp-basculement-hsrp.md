# 🔬 TP PACKET TRACER – S17 ANNÉE 2 – E31
## Infra Multi-Sites : Tests de Basculement HSRP et Capture de Trafic

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Déployer HSRP sur une infrastructure multi-sites avec OSPF
- ✅ Exécuter un plan de test de basculement documenté (5 scénarios)
- ✅ Mesurer le temps de basculement réel et le comparer au théorique
- ✅ Observer les Gratuitous ARP en mode simulation Packet Tracer
- ✅ Rédiger un rapport de tests de basculement

---

## ⏱️ DURÉE : 150 min

---

## 📋 TOPOLOGIE MULTI-SITES

```
                              INTERNET (WAN)
                             /              \
                        Gi0/2            Gi0/2
                  [R-PARIS-1]          [R-PARIS-2]
                  203.0.113.1          203.0.113.5
                        Gi0/0              Gi0/0
                   192.168.10.1       192.168.10.2
                              \              /
                           [SW-PARIS-CORE]
                          /       |       \
                      [PC-P1] [PC-P2]  [PC-P3]
                     .10      .20      .30/24

            WAN Paris-Lyon (R-PARIS-1 ↔ R-LYON-1) : 10.0.12.0/30
            WAN Paris-Lyon (R-PARIS-2 ↔ R-LYON-2) : 10.0.34.0/30

                   [R-LYON-1]            [R-LYON-2]
                   10.10.50.1           10.10.50.2
                              \              /
                           [SW-LYON-CORE]
                                   │
                               [PC-L1]
                              10.10.50.10/24
```

---

## 📋 PLAN D'ADRESSAGE COMPLET

| **Équipement** | **Interface** | **IP** | **Masque** |
|---|---|---|---|
| R-PARIS-1 | Gi0/0 (LAN Paris) | 192.168.10.1 | /24 |
| R-PARIS-1 | Gi0/1 (WAN → R-LYON-1) | 10.0.12.1 | /30 |
| R-PARIS-1 | Gi0/2 (Internet) | 203.0.113.1 | /30 |
| R-PARIS-2 | Gi0/0 (LAN Paris) | 192.168.10.2 | /24 |
| R-PARIS-2 | Gi0/1 (WAN → R-LYON-2) | 10.0.34.1 | /30 |
| R-PARIS-2 | Gi0/2 (Internet) | 203.0.113.5 | /30 |
| R-LYON-1 | Gi0/0 (LAN Lyon) | 10.10.50.1 | /24 |
| R-LYON-1 | Gi0/1 (WAN ← R-PARIS-1) | 10.0.12.2 | /30 |
| R-LYON-2 | Gi0/0 (LAN Lyon) | 10.10.50.2 | /24 |
| R-LYON-2 | Gi0/1 (WAN ← R-PARIS-2) | 10.0.34.2 | /30 |
| PC-P1, P2, P3 | — | 192.168.10.10–.30 | /24, GW .254 |
| PC-L1 | — | 10.10.50.10 | /24, GW 10.10.50.254 |

---

## 📋 PARAMÈTRES HSRP

| **Site** | **Groupe** | **IP Virtuelle** | **R Active** | **Prio** | **R Standby** | **Prio** | **Timers** |
|---|---|---|---|---|---|---|---|
| Paris | 1 | 192.168.10.254 | R-PARIS-1 | 120 | R-PARIS-2 | 100 | 1s/3s |
| Lyon | 2 | 10.10.50.254 | R-LYON-1 | 110 | R-LYON-2 | 90 | 1s/3s |

**Tracking :**

| **Routeur** | **Interface trackée** | **Décrement** |
|---|---|---|
| R-PARIS-1 | Gi0/2 (Internet) | 30 |
| R-LYON-1 | Gi0/1 (WAN Paris) | 30 |

---

## 🧪 PARTIE 1 – Construction et Configuration (30 min)

### 1.1 – Prérequis : Vérification du routage de base

> Le routage OSPF de base est déjà configuré sur la topologie. Vérifiez avant de commencer HSRP.

```
R-PARIS-1# show ip route
R-PARIS-1# ping 10.10.50.1     → _______   (R-LYON-1 LAN)
PC-P1# ping 10.10.50.10        → _______   (PC-L1 via OSPF)
```

**Q1.** La connectivité inter-sites fonctionne-t-elle avant HSRP ? ___________

---

### 1.2 – Configuration HSRP Paris

**Sur R-PARIS-1 :**

```ios
R-PARIS-1(config)# interface GigabitEthernet0/0
R-PARIS-1(config-if)# standby _____ ip _____________
R-PARIS-1(config-if)# standby _____ priority _____
R-PARIS-1(config-if)# standby _____ preempt
R-PARIS-1(config-if)# standby _____ timers _____ _____
R-PARIS-1(config-if)# standby _____ track GigabitEthernet0/2 _____
```

**Sur R-PARIS-2 :**

```ios
R-PARIS-2(config)# interface GigabitEthernet0/0
R-PARIS-2(config-if)# standby _____ ip _____________
R-PARIS-2(config-if)# standby _____ priority _____
R-PARIS-2(config-if)# standby _____ preempt
R-PARIS-2(config-if)# standby _____ timers _____ _____
```

---

### 1.3 – Configuration HSRP Lyon

**Sur R-LYON-1 et R-LYON-2 :** (selon les paramètres du tableau)

```ios
! [Compléter selon le tableau de paramètres HSRP]
```

---

### 1.4 – Vérification initiale

```ios
R-PARIS-1# show standby brief
```

```
Interface   Grp  Pri P State   Active   Standby   Virtual IP
_________   ___  ___ _ _____   ______   ________  ___________
```

**Q2.** R-PARIS-1 est-il bien Active (prio 120 > 100) ? ___________

```
PC-P1# ping 192.168.10.254    → _______   (IP virtuelle HSRP Paris)
PC-P1# ping 10.10.50.10       → _______   (PC-L1 via R-PARIS-1 Active)
```

---

## 📋 PARTIE 2 – Plan de Tests de Basculement (20 min)

> **IMPORTANT : Rédigez le plan AVANT d'exécuter les tests.** C'est la démarche professionnelle.

### Complétez le plan de test pour les 4 scénarios :

---

**TEST 1 — Panne interface LAN de R-PARIS-1**

```
Objectif   : Vérifier bascule HSRP lors d'une panne LAN de l'Active

Scénario   : shutdown GigabitEthernet0/0 de R-PARIS-1

Résultat attendu :
  Temps de bascule théorique : Hold Timer = _____ secondes
  Paquets ICMP perdus maximum : _____ (calcul : _____)
  État final R-PARIS-2 : _____
  Observation dans capture : _____

Résultat obtenu :
  Temps mesuré : _____s    Paquets perdus : _____    ☐ PASS  ☐ FAIL
```

---

**TEST 2 — Panne interface WAN (Internet) de R-PARIS-1**

```
Objectif   : Vérifier déclenchement bascule via tracking d'interface

Scénario   : shutdown GigabitEthernet0/2 de R-PARIS-1

Calcul avant test :
  Priorité R-PARIS-1 avant : _____
  Décrement tracking : _____
  Priorité R-PARIS-1 après : _____
  Bascule attendue ? : _____  (Pourquoi : _____ < _____ ?)

Résultat attendu :
  R-PARIS-2 doit devenir Active : OUI / NON
  Trafic doit être rerouté via R-PARIS-2 WAN : OUI / NON

Résultat obtenu :
  Priorité R-PARIS-1 mesurée après panne : _____
  Bascule observée : OUI/NON    ☐ PASS  ☐ FAIL
```

---

**TEST 3 — Retour de R-PARIS-1 après panne LAN (TEST 1) avec preempt**

```
Objectif   : Vérifier que R-PARIS-1 reprend Active grâce à preempt

Scénario   : no shutdown GigabitEthernet0/0 de R-PARIS-1

Résultat attendu :
  R-PARIS-1 reprend Active : OUI / NON
  Délai de reprise : ≈ _____ s (hello timer + marge)

Résultat obtenu :
  R-PARIS-1 est redevenu Active : OUI/NON
  Délai observé : _____s    ☐ PASS  ☐ FAIL
```

---

**TEST 4 — Comparaison timers défaut vs optimisé**

```
Objectif   : Mesurer l'impact des timers sur le temps de basculement

Scénario A : Changer les timers en 3s/10s (défaut) et simuler panne LAN
  Résultat attendu : ≈ 10s de coupure

Scénario B : Revenir aux timers 1s/3s et simuler panne LAN  
  Résultat attendu : ≈ 3s de coupure

Commandes :
  ! Pour passer aux timers défaut :
  standby 1 timers 3 10

  ! Pour revenir aux timers optimisés :
  standby 1 timers 1 3

Résultats :
  Timers 3s/10s → paquets perdus : _____   temps : _____ s
  Timers 1s/3s  → paquets perdus : _____   temps : _____ s
  Différence    : _____ paquets / _____ secondes   ☐ Gain significatif
```

---

## 🔬 PARTIE 3 – Exécution des Tests (60 min)

### 3.1 – Préparer un ping continu depuis PC-P1

> Avant chaque test, lancer un ping continu depuis PC-P1 vers 8.8.8.8 (Internet) :

```
PC-P1# ping 8.8.8.8 repeat 200 timeout 1
```

> Observer les `.` (echecs) et `!` (succès) dans la sortie.

---

### 3.2 – Activer la capture en mode Simulation (Packet Tracer)

> Si Packet Tracer est utilisé :
> 1. Cliquer sur **Simulation** (bouton bas droite)
> 2. Ajouter un filtre pour ARP et ICMP
> 3. Lancer le ping depuis PC-P1
> 4. Exécuter le scénario de panne
> 5. Observer les paquets capturés

---

### 3.3 – Exécution TEST 1 — Panne LAN R-PARIS-1

```ios
! Vérifier l'état avant :
R-PARIS-1# show standby brief

! Lancer le ping continu sur PC-P1 (dans un autre onglet)

! Déclencher la panne :
R-PARIS-1(config)# interface GigabitEthernet0/0
R-PARIS-1(config-if)# shutdown
```

**Observer et mesurer :**

| **Observation** | **Valeur mesurée** |
|---|---|
| Nombre de paquets ICMP perdus (comptage des `.`) | |
| Temps de coupure (nb paquets × 1s) | |
| État final R-PARIS-2 (`show standby brief`) | |
| R-PARIS-2 est maintenant Active ? | |

**Capture simulée — paquets observés pendant la bascule :**

| **N°** | **Heure** | **Source** | **Destination** | **Type** | **Info** |
|---|---|---|---|---|---|
| | | | 224.0.0.2 | HSRP | Hello State=Active R-PARIS-1 |
| | | | — | — | (silence pendant Hold timer) |
| | | | 224.0.0.2 | HSRP | Coup R-PARIS-2 prend Active |
| | | ff:ff:ff:ff:ff:ff | | ARP | Gratuitous ARP de R-PARIS-2 |

**Conclusion TEST 1 :**

```
Temps de bascule mesuré  : _____ secondes
Temps de bascule attendu : _____ secondes (= Hold Timer)
Écart                    : _____
Résultat                 : ☐ PASS (≤ Hold timer + 1s)  ☐ FAIL
```

---

### 3.4 – Exécution TEST 2 — Panne WAN (tracking)

```ios
! Vérifier la priorité actuelle de R-PARIS-1 :
R-PARIS-1# show standby | include Priority

! Déclencher la panne WAN :
R-PARIS-1(config)# interface GigabitEthernet0/2
R-PARIS-1(config-if)# shutdown

! Observer immédiatement :
R-PARIS-1# show standby | include Priority
```

**Mesures :**

| **Mesure** | **Avant panne** | **Après panne WAN** |
|---|---|---|
| Priorité R-PARIS-1 | 120 | |
| État R-PARIS-1 (Active/Standby) | Active | |
| État R-PARIS-2 | Standby | |

**Q3.** La bascule a-t-elle eu lieu ? Le calcul fait en Partie 2 était-il correct ?

_________________________________________________________________________

---

### 3.5 – Exécution TEST 3 — Retour de R-PARIS-1

```ios
! Rétablir l'interface LAN de R-PARIS-1 :
R-PARIS-1(config)# interface GigabitEthernet0/0
R-PARIS-1(config-if)# no shutdown

! Attendre ~5 secondes puis vérifier :
R-PARIS-1# show standby brief
R-PARIS-2# show standby brief
```

**Q4.** R-PARIS-1 est-il redevenu Active ? Quelle commande a rendu cela possible ?

_________________________________________________________________________

---

### 3.6 – Exécution TEST 4 — Comparaison timers

```ios
! Passer aux timers défaut sur les deux routeurs Paris :
R-PARIS-1(config-if)# standby 1 timers 3 10
R-PARIS-2(config-if)# standby 1 timers 3 10

! Simuler panne LAN R-PARIS-1, compter les paquets perdus
! Puis rétablir et revenir aux timers 1/3 :
R-PARIS-1(config-if)# standby 1 timers 1 3
R-PARIS-2(config-if)# standby 1 timers 1 3
```

**Résultats comparatifs :**

| **Timers** | **Paquets perdus** | **Secondes de coupure** |
|---|---|---|
| 3s/10s (défaut) | | |
| 1s/3s (optimisé) | | |

---

## 📊 PARTIE 4 – Rapport de Tests (20 min)

### Synthèse des résultats

**Tableau récapitulatif final :**

| **Test** | **Scénario** | **Temps attendu** | **Temps mesuré** | **Paquets perdus** | **Résultat** |
|---|---|---|---|---|---|
| TEST 1 | Panne LAN R-PARIS-1 | ≈ 3 s | | | ☐ P ☐ F |
| TEST 2 | Panne WAN (tracking) | ≈ 3 s | | | ☐ P ☐ F |
| TEST 3 | Retour preempt | ≈ 1-2 s | | | ☐ P ☐ F |
| TEST 4 (défaut) | Panne LAN, timers défaut | ≈ 10 s | | | — |

---

### Questions d'analyse pour le rapport

**Q5.** Sur l'infrastructure multi-sites, si R-PARIS-1 tombe complètement (LAN et WAN), quels mécanismes de redondance interviennent et dans quel ordre ?

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**Q6.** Dans la capture de la bascule TEST 1, vous observez plusieurs paquets ARP avec `Sender IP == Target IP`. Qu'est-ce que cela indique et pourquoi y en a-t-il plusieurs (pas juste un) ?

_________________________________________________________________________
_________________________________________________________________________

**Q7.** Un gestionnaire de réseau vous demande quel est le RTO (Recovery Time Objective) de l'infrastructure Paris avec vos timers actuels. Que répondez-vous et comment justifiez-vous ?

_________________________________________________________________________
_________________________________________________________________________

**Q8.** Test 4 : l'entreprise exige que le RTO soit inférieur à 2 secondes. Proposez des timers HSRP adaptés en respectant la contrainte Hold ≥ 3 × Hello, et nommez un risque potentiel.

```
Timers proposés : Hello = _____ ms, Hold = _____ ms
Commande : standby 1 timers msec _____ _____
Risque : _______________________________________________________
```

**Q9.** Pourquoi faut-il configurer `preempt` sur R-PARIS-1 mais aussi sur R-PARIS-2 dans cette topologie ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 | Config HSRP Paris + Lyon + vérification initiale | /4 |
| Partie 2 | Plan de tests complet (4 plans rédigés avant exécution) | /4 |
| Partie 3 – Test 1 | Bascule mesurée + tableau observations | /4 |
| Partie 3 – Test 2 | Calcul tracking + bascule WAN | /3 |
| Partie 3 – Test 3 | Retour preempt + Q4 | /2 |
| Partie 3 – Test 4 | Comparaison timers | /2 |
| Partie 4 | Tableau synthèse + Q5 à Q9 | /5 |
| Présentation / Clarté rapport | — | /1 |
| **TOTAL** | | **/25** |

> *Ramené à /20 : score × 0,8*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
