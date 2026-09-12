# 📖 FICHE COURS – S17 ANNÉE 2 – E31
## Tests de Basculement HSRP : Gratuitous ARP, Capture de Trafic, Plan de Test

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS DE LA SÉANCE

- ✅ Analyser les messages HSRP dans une capture de trafic
- ✅ Comprendre le mécanisme des Gratuitous ARP lors d'une bascule
- ✅ Mesurer le temps de basculement réel
- ✅ Rédiger un plan de test de basculement professionnel
- ✅ Diagnostiquer une bascule défaillante

---

## 1️⃣ RAPPEL : CE QUI SE PASSE LORS D'UNE BASCULE HSRP

### La séquence complète

> Rappel S12 : en HSRP, le routeur Active envoie des messages **Hello** régulièrement. Si le Standby ne les reçoit plus pendant la durée du Hold Timer, il considère l'Active comme mort et prend le relais.

```
Timeline d'une bascule :

t=0s    : R1 Active, envoie Hello (Hello Timer = 1s)
t=1s    : R1 envoie Hello
t=2s    : R1 tombe (panne interface LAN)
t=2s    : R2 n'a plus de Hello → déclenche le Hold Timer (3s configuré)
t=5s    : Hold Timer expire → R2 envoie un message COUP et passe Active
t=5,001s: R2 envoie 3 × Gratuitous ARP pour mettre à jour les caches ARP
t=5,002s: Trafic reprend via R2

Durée de coupure ≈ Hold Timer = 3 secondes
(avec les timers optimisés 1s/3s — le défaut 3s/10s donne 10s de coupure)
```

---

## 2️⃣ LES MESSAGES HSRP DANS UNE CAPTURE

### Types de messages HSRP

| **Message** | **Op Code** | **Qui l'envoie** | **Quand** |
|---|---|---|---|
| **Hello** | 0 | Active ET Standby | Périodiquement (toutes les Hello Timer secondes) |
| **Coup** | 1 | Routeur qui prend Active | Quand il prend le rôle Active (avec preempt ou après expiration Hold) |
| **Resign** | 2 | Active actuel | Quand il cède volontairement (interface shutdown) |

### Adresse multicast et port UDP

> - Les messages HSRP sont envoyés en **multicast UDP** vers `224.0.0.2` (All Routers)
> - **Port UDP source et destination : 1985** (port enregistré par Cisco pour HSRP)
> - Le filtre Wireshark : `udp.port == 1985` ou simplement `hsrp`

---

### Structure d'un paquet HSRP Hello (simplifié)

```
┌─────────────────────────────────────────────────────────────────┐
│  Ethernet II                                                    │
│    Src MAC : 0000.0C07.XXXX (MAC virtuelle si Active envoie)   │
│    Dst MAC : 0100.5E00.0002 (multicast 224.0.0.2)              │
│  IP                                                             │
│    Src IP  : 192.168.1.1 (IP réelle du routeur)                │
│    Dst IP  : 224.0.0.2                                          │
│  UDP Port  : 1985                                               │
│  HSRP                                                           │
│    Version : 0 (v1) ou 1 (v2)                                  │
│    Op Code : 0 (Hello) ← le champ le plus important            │
│    State   : 32 (Active) ou 16 (Standby) ← état du routeur    │
│    Hello Time : 3 s                                             │
│    Hold Time  : 10 s                                            │
│    Priority   : 110 (priorité configurée)                       │
│    Group      : 1 (numéro de groupe HSRP)                      │
│    Virtual IP : 192.168.1.254 (l'IP virtuelle)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

📷 **[ILLUSTRATION 1]**
*Capture Wireshark annotée montrant une séquence de bascule HSRP. Timeline horizontale avec 3 zones : Zone verte (normal - hellos périodiques de R1 Active), Zone rouge (bascule - plus de hellos R1, attente Hold Timer, coup de R2), Zone verte (nouveau normal - hellos de R2 Active). Sur la ligne du temps, les paquets sont représentés par des icônes colorées : bleu pour les hellos HSRP, rouge pour le coup, jaune pour les Gratuitous ARP, gris pour les paquets ICMP (avec une interruption correspondant à la coupure). Style capture Wireshark annotée pédagogique, fond sombre type Wireshark.*

> **Légende :** Chronologie d'une bascule HSRP observée dans Wireshark. Les hellos HSRP (bleu) sont émis toutes les 1 seconde par R1 (Active). Après la panne de R1, R2 attend l'expiration du Hold Timer (3 s) puis envoie un message Coup (rouge) pour prendre le rôle Active. Les Gratuitous ARP (jaune) suivent immédiatement. Le trafic ICMP (gris) est interrompu pendant la durée de la bascule.

---

## 3️⃣ LE GRATUITOUS ARP (GARP) — CLEF DE LA BASCULE

### Pourquoi est-il indispensable ?

> Quand R2 prend le rôle Active HSRP, il "hérite" de l'IP virtuelle `192.168.1.254`. Mais les PCs du LAN ont dans leur **cache ARP** l'ancienne association :
> `192.168.1.254 → MAC de R1`
>
> Si R2 ne fait rien, les PCs continueront d'envoyer les paquets vers le MAC de R1 — qui est mort. Le trafic serait perdu jusqu'à **l'expiration naturelle du cache ARP** (typiquement 2 à 4 minutes).
>
> Solution : **Gratuitous ARP** — R2 envoie un ARP non sollicité en broadcast pour forcer la mise à jour immédiate de tous les caches ARP.

---

📷 **[ILLUSTRATION 2]**
*Schéma en 3 étapes montrant l'impact du Gratuitous ARP. Étape 1 (avant panne) : PC avec cache ARP pointant vers MAC-R1, flèche de trafic vers R1. Étape 2 (pendant bascule, avant GARP) : R1 mort, PC envoie encore vers MAC-R1, trafic perdu (flèche rouge barrée). Étape 3 (après GARP) : R2 a envoyé le GARP, cache ARP du PC mis à jour avec MAC-R2, trafic reprend via R2 (flèche verte). Style diagramme réseau en 3 états, fond blanc, couleurs distinctes.*

> **Légende :** Le Gratuitous ARP (GARP) est le mécanisme qui permet au trafic de reprendre immédiatement après une bascule HSRP. Sans GARP, les hôtes du LAN continueraient à envoyer leurs paquets vers le MAC de l'ancien Active (désormais mort), perdant tous les paquets jusqu'à l'expiration naturelle du cache ARP.

---

### Structure d'un Gratuitous ARP dans Wireshark

```
ARP
  Hardware type: Ethernet (1)
  Protocol type: IPv4 (0x0800)
  Opcode: request (1)    ← Ou reply (2), les deux sont utilisés pour GARP
  Sender MAC address: MAC_de_R2
  Sender IP address: 192.168.1.254    ← IP virtuelle (source et destination identiques)
  Target MAC address: ff:ff:ff:ff:ff:ff  ← Broadcast
  Target IP address: 192.168.1.254    ← MÊME que la source → c'est le signe d'un GARP
```

> Le filtre Wireshark pour voir uniquement les GARP : `arp.isgratuitous == 1`
> Ou plus simplement : dans un ARP, si `Sender IP == Target IP` → c'est un GARP

---

## 4️⃣ INFRA MULTI-SITES : TOPOLOGIE DE RÉFÉRENCE S17

### Vue d'ensemble

```
                            ┌──── INTERNET ────┐
                            │                  │
                      [R-PARIS-1]        [R-PARIS-2]
                        (HSRP Active)    (HSRP Standby)
                           \               /
                            [SW-PARIS-CORE]
                           /     |      \
                       [VLAN10] [VLAN20] [VLAN30]
                    (Direction)(Atelier)(Informatique)

                       WAN1 (R-PARIS-1 → R-LYON-1)
                       WAN2 (R-PARIS-2 → R-LYON-2)

                    [R-LYON-1]         [R-LYON-2]
                    (HSRP Active)      (HSRP Standby)
                           \               /
                            [SW-LYON-CORE]
                                  │
                              [VLAN50]
                            (Production)
```

### Tableau des composants HSRP par site

| **Site** | **Routeur Active** | **Priorité** | **Routeur Standby** | **Priorité** | **IP Virtuelle** |
|---|---|---|---|---|---|
| Paris | R-PARIS-1 | 120 | R-PARIS-2 | 100 | 192.168.10.254 (VLAN10) |
| Paris | R-PARIS-1 | 120 | R-PARIS-2 | 100 | 192.168.20.254 (VLAN20) |
| Lyon | R-LYON-1 | 110 | R-LYON-2 | 90 | 10.10.50.254 |

---

## 5️⃣ PLAN DE TEST DE BASCULEMENT — FORMAT PROFESSIONNEL

### Pourquoi documenter avant d'exécuter ?

> Un ingénieur réseau ne "teste" jamais à l'aveugle. Il **planifie** : définir ce qu'on attend avant d'observer permet de détecter les anomalies et de ne pas confondre le comportement attendu avec un bug.

### Template de plan de test

```
═══════════════════════════════════════════════════════════════
PLAN DE TEST DE BASCULEMENT — Site : ____________
Rédigé par : ____________  Date : ____________
═══════════════════════════════════════════════════════════════

TEST N° ___
───────────────────────────────────────────────────────────────
Objectif      : Vérifier que HSRP bascule vers Standby en cas
                de panne de l'interface LAN du routeur Active

Prérequis     : HSRP configuré (timers 1 3, preempt, tracking)
                Ping continu en cours depuis PC vers Internet

Scénario      : Désactiver l'interface LAN du routeur Active
                (R-PARIS-1, interface Gi0/0, shutdown)

Résultat attendu :
  - R-PARIS-2 passe Active en < 4 secondes
  - Maximum X paquets ICMP perdus (calcul : Hold_timer / 1s = X paquets)
  - show standby brief sur R-PARIS-2 affiche Active
  - Gratuitous ARP visible dans la capture

Résultat obtenu : (à remplir pendant le test)
  - Temps de bascule mesuré : _____
  - Paquets ICMP perdus : _____
  - Comportement observé : _____

Conclusion :    ☐ PASS  ☐ FAIL  ☐ PARTIEL
Commentaires : _____
═══════════════════════════════════════════════════════════════
```

---

## 6️⃣ MESURE DU TEMPS DE BASCULEMENT

### Méthodes de mesure dans Packet Tracer

**Méthode 1 — Ping continu avec timestamp :**

```
PC# ping 8.8.8.8 repeat 100 timeout 1
```

> Compter les `....` (échecs) dans la sortie du ping.
> Chaque `.` = 1 seconde de timeout → nb de `.` ≈ nb secondes de coupure

**Méthode 2 — Simulation Wireshark (Packet Tracer) :**

> Activer le mode Simulation dans Packet Tracer → capturer les paquets → noter le timestamp du dernier ICMP Reply avant la bascule et du premier ICMP Reply après.

**Méthode 3 — show standby (timestamp Cisco) :**

```ios
R-PARIS-2# show standby
  ...
  State is Active
    2 state changes, last state change 00:00:03  ← Temps depuis la bascule
```

---

### Tableau de mesures attendu

| **Test** | **Timers** | **Temps bascule théorique** | **Temps mesuré** | **Paquets perdus** | **Résultat** |
|---|---|---|---|---|---|
| Test 1 — Panne LAN | 1s/3s | ≈ 3 s | | | |
| Test 2 — Panne WAN (tracking) | 1s/3s | ≈ 3 s | | | |
| Test 3 — Retour Active (preempt) | 1s/3s | ≈ 1 s | | | |
| Test 4 — Timers défaut | 3s/10s | ≈ 10 s | | | |

---

## 7️⃣ TROUBLESHOOTING : BASCULE QUI NE SE PRODUIT PAS

### Checklist de diagnostic

Quand la bascule HSRP **ne se produit pas** (Standby ne prend pas Active) :

```
Étape 1 — Vérifier que HSRP est bien configuré des deux côtés
  R1# show standby brief → State = Active ? Standby présent ?
  R2# show standby brief → State = Standby ? Active visible ?

Étape 2 — Vérifier que les deux routeurs se voient
  R2# show standby → "Standby router is X.X.X.X, priority Y, expires in Z sec"
  Si "Unknown" → R2 ne reçoit pas les hellos de R1

Étape 3 — Vérifier les timers (identiques des deux côtés ?)
  R1# show standby → "Hello time X sec, hold time Y sec"
  R2# show standby → même chose ?

Étape 4 — Vérifier preempt (si la bascule retour ne se produit pas)
  R1# show standby → "Preemption enabled" ?
  Sans preempt → R1 ne reprend pas Active après retour

Étape 5 — Vérifier le tracking (si bascule WAN ne se produit pas)
  R1# show standby → "Track interface X state Up decrement Y"
  Décrement suffisant ? (prio_Active - décrement < prio_Standby)

Étape 6 — Debug si nécessaire
  R1# debug standby events  ← moins verbeux que debug standby complet
```

---

## 8️⃣ INTERACTION HSRP + OSPF DANS UNE INFRA MULTI-SITES

### Le cas multi-sites : deux couches de redondance

```
┌─────────────────────────────────────────────────────────────────┐
│  Couche 3 (réseau) : OSPF reconverge les routes WAN             │
│    → Si lien WAN Paris-Lyon tombe, OSPF trouve une autre route  │
│    → Temps de convergence OSPF : 30-60s (sans optimisation)     │
│                                                                 │
│  Couche 3 (LAN) : HSRP bascule la passerelle locale            │
│    → Si R-PARIS-1 tombe, R-PARIS-2 prend la passerelle          │
│    → Temps de bascule HSRP : 3-10s (selon timers)              │
└─────────────────────────────────────────────────────────────────┘
```

### Important : HSRP et OSPF sont indépendants

> ⚠️ La bascule HSRP change **qui est la passerelle locale** — elle ne change pas les routes OSPF. Et inversement, la convergence OSPF (changement de route vers un site distant) ne déclenche pas automatiquement une bascule HSRP.

**Scénario combiné :**

| **Événement** | **Impact HSRP** | **Impact OSPF** |
|---|---|---|
| R-PARIS-1 LAN down | Bascule HSRP → R-PARIS-2 Active | Aucun (R-PARIS-2 était déjà dans OSPF) |
| Lien WAN Paris-Lyon down | Aucun HSRP | OSPF reconverge → route alternative |
| R-PARIS-1 WAN down + tracking | Bascule HSRP (décrement priorité) | OSPF reconverge aussi |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais distinguer un message HSRP Hello, Coup et Resign
- [ ] Je comprends le rôle du Gratuitous ARP lors d'une bascule
- [ ] Je sais que sans GARP, le cache ARP met plusieurs minutes à expirer
- [ ] Je sais filtrer les paquets HSRP dans Wireshark (`udp.port == 1985`)
- [ ] Je sais mesurer le temps de basculement (ping continu ou timestamp)
- [ ] Je sais rédiger un plan de test (objectif, scénario, résultat attendu, résultat obtenu)
- [ ] Je comprends que HSRP et OSPF sont deux mécanismes de redondance indépendants
- [ ] Je sais diagnostiquer pourquoi une bascule ne se produit pas

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **Coup (HSRP)** | Message envoyé par un routeur qui prend le rôle Active |
| **Resign (HSRP)** | Message envoyé par l'Active qui cède volontairement son rôle |
| **Gratuitous ARP (GARP)** | ARP non sollicité envoyé pour forcer la mise à jour des caches ARP |
| **Cache ARP** | Table associant IP → MAC sur chaque hôte (durée de vie par défaut ~2-4 min) |
| **RTO** | Recovery Time Objective — temps maximum acceptable pour le rétablissement |
| **Plan de test** | Document décrivant l'objectif, le scénario, et les résultats attendus/obtenus |
| **udp.port == 1985** | Filtre Wireshark pour capturer les messages HSRP |
| **State=32 (Active) / 16 (Standby)** | Valeurs numériques des états HSRP dans les paquets capturés |

---

## 📌 POINTS-CLÉS À RETENIR

1. **Hello** = périodique (Active et Standby) ; **Coup** = prise de rôle Active ; **Resign** = cession volontaire
2. **Gratuitous ARP** = essentiel après une bascule → force la mise à jour des caches ARP de tout le LAN
3. **Temps de coupure ≈ Hold Timer** (réductible avec des timers plus courts)
4. Filtre Wireshark : `udp.port == 1985` pour HSRP ; `arp.isgratuitous == 1` pour les GARP
5. **Documenter avant d'exécuter** : plan de test = résultat attendu défini a priori
6. **HSRP et OSPF sont indépendants** — chacun gère sa couche de redondance
7. Bascule qui ne se produit pas → vérifier preempt, décrement tracking, IP virtuelle identique

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
