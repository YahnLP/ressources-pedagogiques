# 🎯 TD DIFFÉRENCIÉS – S1-A2 E31
## Révision Ciblée : Adressage IP et Routage Statique

> **Identification de votre TD :**
> - **TD-A** → Profil : bases d'adressage IP à reconsolider (score < 8/40 ou Ex.1 lacunaire)
> - **TD-B** → Profil : plan d'adressage et table de routage à revoir (score 8–20/40)
> - **TD-C** → Profil : syntaxe IOS à rafraîchir (score 20–30 avec lacune Ex.3)
> - **TD-Expert** → Profil : tout acquis, préparer la transition vers OSPF (score ≥ 30/40)

**Mon profil : ______  Nom : ________________  Prénom : ________________**

---

# ═══════════════════════════════════════════════
# TD-A — BASES D'ADRESSAGE IP
# ═══════════════════════════════════════════════

> *Utiliser la table CIDR de la Fiche Révision (Module 1). Montrer tous les calculs.*

## A1 – Entraînement calcul (8 pts)

Pour chaque adresse, compléter **ligne par ligne avec les étapes** :

**A1.1 — 10.1.1.200 /27**

```
Incrément = _____
Multiples de l'incrément : 0, _____, _____, _____...
Bloc contenant 200 : _____
Adresse réseau    : _________________________
Adresse broadcast : _________________________
1ère @ hôte       : _________________________
Dernière @ hôte   : _________________________
Nb hôtes          : 2^ _____ - 2 = _____
```

---

**A1.2 — 172.16.50.100 /26**

```
Incrément = _____
Multiples : 0, _____, _____, _____...
Bloc contenant 100 : _____
Adresse réseau    : _________________________
Adresse broadcast : _________________________
Nb hôtes          : _____
```

---

**A1.3 — 192.168.5.45 /29**

```
Incrément = _____
Bloc : _____
Adresse réseau    : _________________________
Adresse broadcast : _________________________
Nb hôtes          : _____
```

---

**A1.4 — 10.0.0.17 /30**

```
Adresse réseau    : _________________________
Broadcast         : _________________________
Les 2 @ hôtes     : __________ et __________
```

---

## A2 – Quel préfixe choisir ? (4 pts)

Pour chaque besoin, indiquer le préfixe CIDR minimal adapté et justifier :

| **Besoin** | **Calcul** | **Préfixe choisi** |
|---|---|---|
| 10 hôtes | 2^? - 2 ≥ 10 → 2^? = ? | |
| 28 hôtes | | |
| 55 hôtes | | |
| 100 hôtes | | |
| 2 hôtes (liaison point-à-point) | | |

---

## A3 – Conversion CIDR ↔ masque décimal (4 pts)

Compléter le tableau sans la fiche révision (exercice de mémorisation) :

| **CIDR** | **Masque décimal** | **Incrément** | **Nb hôtes** |
|---|---|---|---|
| /24 | | | |
| /25 | | | |
| /26 | | | |
| /27 | | | |
| /28 | | | |
| /29 | | | |
| /30 | | | |

---

## A4 – Application complète (4 pts)

Un réseau 192.168.20.0/24 doit être découpé en 4 sous-réseaux de taille égale.

a) Quel préfixe donne exactement 4 sous-réseaux de même taille depuis un /24 ?

```
/24 découpé en /26 → 2^(26-24) = 2^2 = 4 sous-réseaux
```

b) Listez les 4 sous-réseaux avec leur adresse réseau, broadcast et passerelle :

| **Sous-réseau** | **Réseau** | **Broadcast** | **Passerelle** |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

---

# ═══════════════════════════════════════════════
# TD-B — PLAN D'ADRESSAGE ET TABLE DE ROUTAGE
# ═══════════════════════════════════════════════

> *Commencer par relire le Module 2 et 3 de la Fiche Révision.*

## B1 – Plan d'adressage complet (12 pts)

### Topologie

```
                        ┌──────────────┐
                        │  Agence HQ   │
                        │   (WAN FAI)  │
                        └──────┬───────┘
                               │
                          ┌────┴────┐
                     ──── │   R1    │ ────
                    │     └─────────┘     │
               ┌────┴─────┐         ┌────┴─────┐
               │    R2    │         │    R3    │
               └────┬─────┘         └────┬─────┘
                    │                    │
            ┌───────┴───────┐    ┌───────┴───────┐
        [LAN-Ventes]    [LAN-RH] [LAN-Dev]   [LAN-Servers]
```

### Contraintes d'adressage

| **Segment** | **Besoin hôtes** | **Espace disponible** |
|---|---|---|
| LAN-Ventes | 45 hôtes | 192.168.1.0/24 à découper |
| LAN-RH | 20 hôtes | 192.168.1.0/24 (suite) |
| LAN-Dev | 100 hôtes | 192.168.2.0/24 entier ou découpé |
| LAN-Servers | 10 hôtes | 192.168.1.0/24 (suite) |
| Liaison R1–R2 | 2 | 10.0.12.0/30 |
| Liaison R1–R3 | 2 | 10.0.13.0/30 |
| Liaison R2–R3 | 2 | 10.0.23.0/30 |

### B1.a – Tableau de plan d'adressage (8 pts)

| **Segment** | **Préfixe choisi** | **Justification** | **Réseau** | **Broadcast** | **Passerelle** |
|---|---|---|---|---|---|
| LAN-Ventes (45 h.) | | | | | |
| LAN-RH (20 h.) | | | | | |
| LAN-Dev (100 h.) | | | | | |
| LAN-Servers (10 h.) | | | | | |
| Liaison R1–R2 | /30 | 2 hôtes | 10.0.12.0 | 10.0.12.3 | R1:.1 R2:.2 |
| Liaison R1–R3 | /30 | 2 hôtes | 10.0.13.0 | 10.0.13.3 | R1:.1 R3:.2 |
| Liaison R2–R3 | /30 | 2 hôtes | 10.0.23.0 | 10.0.23.3 | R2:.1 R3:.2 |

### B1.b – Vérification anti-chevauchement (2 pts)

Vérifiez que les 4 sous-réseaux LAN ne se chevauchent pas. Listez-les dans l'ordre croissant :

| **Ordre** | **Réseau** | **Broadcast** |
|---|---|---|
| 1er | | |
| 2ème | | |
| 3ème | | |
| 4ème | | |

*Confirmer que broadcast du réseau N < adresse réseau du réseau N+1.*

### B1.c – Table de routage R1 (2 pts)

> R1 doit pouvoir joindre tous les LAN. Complétez sa table (routes statiques uniquement, les routes C sont déjà présentes) :

| **Type** | **Réseau** | **Masque** | **Next-hop** |
|---|---|---|---|
| C | 10.0.12.0 | /30 | — (liaison R1-R2) |
| C | 10.0.13.0 | /30 | — (liaison R1-R3) |
| S | LAN-Ventes | | |
| S | LAN-RH | | |
| S | LAN-Dev | | |
| S | LAN-Servers | | |
| S | (route par défaut) | | WAN FAI |

---

## B2 – Analyse d'une table de routage (8 pts)

**Table de routage de R-CENTRAL :**

```
R-CENTRAL# show ip route
C    10.1.0.0/30   via Gi0/0
C    10.1.0.4/30   via Gi0/1
C    10.1.0.8/30   via Gi0/2
S    172.16.1.0/24  [1/0] via 10.1.0.2
S    172.16.2.0/24  [1/0] via 10.1.0.6
S    172.16.3.0/25  [1/0] via 10.1.0.10
S    172.16.3.128/25 [1/0] via 10.1.0.10
S*   0.0.0.0/0     [1/0] via 10.1.0.1
```

**B2.a** — Combien de réseaux directement connectés ce routeur possède-t-il ?

_________

**B2.b** — Un paquet arrive à destination de **172.16.3.200**. Vers quel next-hop est-il envoyé ?

```
Calcul : 172.16.3.128/25 → réseau 172.16.3.128, broadcast 172.16.3.255
200 est dans 172.16.3.128–.255 → next-hop : __________
```

**B2.c** — Un paquet arrive à destination de **8.8.8.8** (DNS Google). Vers quel next-hop ?

_________

**B2.d** — Pourquoi y a-t-il deux routes vers 172.16.3.x (une pour .0/25 et une pour .128/25) au lieu d'une seule vers 172.16.3.0/24 ?

_________________________________________________________________________
_________________________________________________________________________

---

# ═══════════════════════════════════════════════
# TD-C — SYNTAXE IOS ET CONFIGURATION COMPLÈTE
# ═══════════════════════════════════════════════

> *Se référer au Module 4 de la Fiche Révision pour la syntaxe.*

## C1 – Correction de configurations incorrectes (6 pts)

Chaque commande ci-dessous contient **une erreur**. Identifiez-la et réécrivez la commande correcte.

**C1.1 :**
```
R1(config)# ip route 192.168.5.0 10.0.0.2 255.255.255.0
```
Erreur : _________________________________________________________________
Correction : `______________________________________________________________`

---

**C1.2 :**
```
R2(config)# ip route 10.5.0.0 255.255.0.0 Gi0/1 10.0.1.1
```
Erreur : _________________________________________________________________
Correction : `______________________________________________________________`

---

**C1.3 :**
```
R3(config)# ip route 0.0.0.0 255.0.0.0 172.16.0.1
```
Erreur : _________________________________________________________________
Correction : `______________________________________________________________`

---

**C1.4 :**
```
R4(config)# ip route 192.168.1.10 255.255.255.0 10.0.0.1
```
Erreur : _________________________________________________________________
Correction : `______________________________________________________________`

---

## C2 – Configuration complète d'une topologie 3 routeurs (14 pts)

### Topologie

```
[PC-LAN-A]─────[R1]──────────[R2]──────────[R3]─────[PC-LAN-C]
192.168.10.0/24   10.0.0.0/30   10.0.0.4/30   192.168.30.0/24
                                    │
                              [PC-LAN-B]
                             192.168.20.0/24
```

### Plan d'adressage fourni

| **Interface** | **Adresse IP** |
|---|---|
| R1 Gi0/0 (vers LAN-A) | 192.168.10.1/24 |
| R1 Gi0/1 (vers R2) | 10.0.0.1/30 |
| R2 Gi0/0 (vers R1) | 10.0.0.2/30 |
| R2 Gi0/1 (vers R3) | 10.0.0.5/30 |
| R2 Gi0/2 (vers LAN-B) | 192.168.20.1/24 |
| R3 Gi0/0 (vers R2) | 10.0.0.6/30 |
| R3 Gi0/1 (vers LAN-C) | 192.168.30.1/24 |

### C2.a – Écrire TOUTES les routes statiques nécessaires (9 pts)

> Chaque routeur doit pouvoir joindre TOUS les réseaux. Indiquez les commandes exactes.

**Sur R1 :**

```
R1(config)# ip route _______________________________________________
R1(config)# ip route _______________________________________________
R1(config)# ip route _______________________________________________
```

*(R1 doit joindre : LAN-B, LAN-C, et la liaison 10.0.0.4/30)*

---

**Sur R2 :**

```
R2(config)# ip route _______________________________________________
R2(config)# ip route _______________________________________________
```

*(R2 connaît déjà les 3 LANs directement ou via ses liaisons - quelles routes manquent ?)*

---

**Sur R3 :**

```
R3(config)# ip route _______________________________________________
R3(config)# ip route _______________________________________________
R3(config)# ip route _______________________________________________
```

*(R3 doit joindre : LAN-A, LAN-B, et la liaison 10.0.0.0/30)*

---

### C2.b – Vérification (3 pts)

Après configuration, écrivez les commandes de vérification sur **R2** pour confirmer :

1. Que les routes sont bien installées :
```
R2# _______________________________________________
```

2. Que R2 peut joindre le PC-LAN-A (192.168.10.10) :
```
R2# _______________________________________________
```

3. Que vous pouvez voir le chemin emprunté vers LAN-C :
```
R2# _______________________________________________
```

### C2.c – Simulation de panne (2 pts)

La liaison R1–R2 (10.0.0.0/30) tombe. Qu'arrive-t-il à la communication LAN-A → LAN-C ? Le routage statique peut-il gérer cette panne automatiquement ? Justifiez en 2 phrases.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

*(→ Cette réponse introduit la motivation d'OSPF)*

---

# ═══════════════════════════════════════════════
# TD-EXPERT — CONSOLIDATION ET PRÉPARATION OSPF
# ═══════════════════════════════════════════════

> *TD pour apprentis ayant obtenu ≥ 30/40 au diagnostic.*

## E1 – Plan d'adressage hiérarchique complexe (10 pts)

### Contexte

Une PME de 3 sites doit être adressée depuis le bloc **172.16.0.0/16**. Les contraintes sont :

| **Site** | **Département** | **Hôtes** |
|---|---|---|
| Site Paris | Commercial | 200 |
| Site Paris | Technique | 100 |
| Site Paris | Direction | 20 |
| Site Lyon | Production | 150 |
| Site Lyon | Qualité | 30 |
| Site Bordeaux | Commercial | 80 |
| Liaisons WAN (3 liaisons inter-sites) | — | 2 par liaison |

**E1.a** — Proposez une structure d'adressage hiérarchique :
- Un /20 par site
- Découpage interne par site
- Liaisons WAN dans un espace dédié

**E1.b** — Remplissez le plan d'adressage complet (tableau à construire).

**E1.c** — Quelle est la plage totale utilisée ? Quel pourcentage du /16 est consommé ?

---

## E2 – Limites du routage statique : démonstration par le calcul (5 pts)

### Contexte

Un réseau entreprise comprend 20 routeurs, chacun ayant en moyenne 4 interfaces (donc 4 réseaux connectés). Chaque routeur doit connaître tous les réseaux.

**E2.a** — Nombre total de réseaux dans l'entreprise :

```
20 routeurs × 4 réseaux = _____ réseaux au total
(certains réseaux sont partagés entre 2 routeurs — liaisons P-à-P)
Estimation nette : _____ réseaux distincts
```

**E2.b** — Nombre de commandes `ip route` à saisir (chaque routeur a besoin d'une route vers chaque réseau non directement connecté) :

```
Routeurs : 20
Réseaux connectés par routeur : 4
Réseaux à apprendre par routeur : _____ - 4 = _____
Total commandes : 20 × _____ = _____ commandes !!!
```

**E2.c** — Un lien tombe (un routeur perd une interface). Combien de commandes `ip route` faut-il modifier MANUELLEMENT pour rétablir la connectivité via un chemin alternatif ?

_________________________________________________________________________

**E2.d** — Concluez en 3 phrases sur la nécessité d'un protocole de routage dynamique.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

## E3 – Pré-requis OSPF : analyse de convergence (5 pts)

OSPF calcule le **plus court chemin** (Shortest Path First) entre deux routeurs en utilisant l'algorithme de Dijkstra appliqué à une **carte du réseau** (LSDB — Link State DataBase).

**E3.a** — Dans le graphe suivant, trouvez le chemin de coût minimum entre R1 et R5 (les chiffres sur les liaisons sont les coûts OSPF) :

```
R1 ──(10)── R2 ──(5)── R4
│                       │
(20)                  (10)
│                       │
R3 ──(15)── R5 ──(5)── R4
             │
            (30)
             │
            R2
```

Chemin 1 : R1→R2→R4→R5 = 10 + 5 + 10 = _____
Chemin 2 : R1→R3→R5    = 20 + 15     = _____
Chemin 3 : R1→R2→R5    = 10 + 30     = _____

**Meilleur chemin : R1 → _____ → _____ → _____ (coût : _____)**

**E3.b** — La liaison R2–R4 tombe. OSPF recalcule automatiquement. Quel est maintenant le meilleur chemin ?

_________________________________________________________________________

**E3.c** — Qu'aurait-il fallu faire en routage STATIQUE pour gérer cette panne ? Comparez avec OSPF.

_________________________________________________________________________
_________________________________________________________________________

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
