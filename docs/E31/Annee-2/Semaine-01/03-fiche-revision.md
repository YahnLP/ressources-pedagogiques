# 📖 FICHE RÉVISION CIBLÉE – S1-A2 E31
## Adressage IP et Routage Statique — Bases Indispensables Avant OSPF

**Nom : ________________  Prénom : ________________**

> ℹ️ Cette fiche est un mémo condensé des points qui seront supposés acquis lors de l'introduction d'OSPF. Lire, annoter, puis utiliser pour vérifier les TD.

---

## MODULE 1 — ADRESSAGE IPv4 : MÉTHODE DE CALCUL

### La structure d'une adresse IP

```
Adresse IP  :  192  .  168  .  10  .  130    /26
               ─────────────────────────     ──
               Adresse sur 32 bits            Préfixe CIDR
                                              (nb de bits réseau)
```

Une adresse /26 : **26 bits réseau** + **6 bits hôtes**

### Formule fondamentale du nombre d'hôtes

$$\boxed{N_{hôtes} = 2^n - 2}$$

où **n = 32 − préfixe** = nombre de bits hôtes.

- Le **−2** est obligatoire : on retire l'adresse réseau (bits hôtes tous à 0) et l'adresse broadcast (bits hôtes tous à 1).
- **Ne jamais oublier ce −2.**

---

### Table CIDR de référence (à mémoriser)

| **Préfixe** | **Masque décimal** | **Bits hôtes (n)** | **Nb hôtes** | **Incrément** |
|---|---|---|---|---|
| **/24** | 255.255.255.**0** | 8 | 254 | 256 |
| **/25** | 255.255.255.**128** | 7 | 126 | 128 |
| **/26** | 255.255.255.**192** | 6 | 62 | 64 |
| **/27** | 255.255.255.**224** | 5 | 30 | 32 |
| **/28** | 255.255.255.**240** | 4 | 14 | 16 |
| **/29** | 255.255.255.**248** | 3 | 6 | 8 |
| **/30** | 255.255.255.**252** | 2 | 2 | 4 |

> 💡 **Astuce mémo pour le dernier octet du masque :**
> L'incrément = **256 − dernier octet du masque**
> /26 → masque 192 → incrément = 256−192 = **64** ✅

---

### Méthode en 5 étapes pour trouver adresse réseau et broadcast

```
Exemple : 192.168.10.130 /26

Étape 1 : Trouver le préfixe → /26 → incrément = 64

Étape 2 : Lister les multiples de l'incrément pour le dernier octet :
          0, 64, 128, 192...

Étape 3 : Trouver le multiple juste ≤ à l'octet de l'adresse (130) :
          128 ≤ 130 < 192 → BLOC = 128

Étape 4 : Adresse réseau  = 192.168.10.128 /26
          Adresse broadcast = 192.168.10.128 + 64 − 1 = 192.168.10.191

Étape 5 : 1ère @ hôte = 192.168.10.129
          Dernière @ hôte = 192.168.10.190
          Nb hôtes = 2^6 − 2 = 62
```

---

### Choisir le bon préfixe pour X hôtes

> **Objectif :** trouver le **plus petit préfixe** (moins de bits réseau = plus de bits hôtes) qui satisfait le besoin.

```
Besoin : 25 hôtes

Tester : /27 → 2^5 - 2 = 30 ≥ 25 → ✅ suffisant
         /28 → 2^4 - 2 = 14 < 25  → ❌ insuffisant

→ Choisir /27
```

**Règle :** Partir de /30 et monter (/29, /28…) jusqu'à ce que 2^n−2 ≥ besoin.

---

## MODULE 2 — PLAN D'ADRESSAGE : MÉTHODE

### Étapes de construction d'un plan d'adressage

```
ÉTAPE 1 : Inventorier tous les segments réseau
          → LAN utilisateurs, liaisons point-à-point entre routeurs

ÉTAPE 2 : Trier par taille décroissante (plus grand besoin d'abord)
          → Évite les "trous" dans l'espace d'adressage

ÉTAPE 3 : Pour chaque segment :
          a) Calculer le préfixe minimal (2^n - 2 ≥ nb hôtes)
          b) Trouver le prochain bloc disponible (multiple de l'incrément)
          c) Vérifier l'absence de chevauchement

ÉTAPE 4 : Pour les liaisons point-à-point routeur-routeur :
          → Toujours /30 (ou /31 si IOS le supporte)
          → Utiliser un espace d'adressage dédié (ex. 10.0.0.0/29 découpé en /30)

ÉTAPE 5 : Remplir le tableau récapitulatif :
          Réseau | Masque | Passerelle | 1ère @ hôte | Dernière @ | Nb hôtes
```

---

### Tableau de plan d'adressage (modèle type)

| **Segment** | **Réseau** | **Masque** | **Passerelle (IP routeur)** | **Plage hôtes** | **Nb hôtes** |
|---|---|---|---|---|---|
| LAN Direction | | | | | |
| LAN Production | | | | | |
| Liaison R1–R2 | | /30 | R1: .1 R2: .2 | — | 2 |

---

## MODULE 3 — ROUTAGE STATIQUE : PRINCIPE ET TABLE

### Concept fondamental

> Un routeur ne connaît que **ses réseaux directement connectés** (routes C dans `show ip route`). Pour atteindre les autres réseaux, il faut lui dire **explicitement** où envoyer les paquets → c'est le routage statique.

### Structure d'une table de routage

```
R1# show ip route
Codes : C - connected, S - static, O - OSPF, D - EIGRP, R - RIP

      10.0.0.0/30 is subnetted
C        10.0.0.0/30 [0/0] via Gi0/1
      192.168.1.0/24
C        192.168.1.0/24 [0/0] via Gi0/0
S        192.168.2.0/24 [1/0] via 10.0.0.2
S*       0.0.0.0/0 [1/0] via 203.0.113.1
         ↑ route par défaut (S*)
```

**Lecture d'une ligne S :**
```
S     192.168.2.0/24   [1/0]   via   10.0.0.2
│     ──────────────   ─────   ───   ────────
│     Réseau dest.     AD/    Mot-   Next-hop
│                      métrique clé
└── S = Static
```

---

### Le principe du chemin ALLER + RETOUR

> ⚠️ **Erreur la plus fréquente en classe :** configurer la route aller (R1→R2) sans la route retour (R2→R1).

```
PC-A → PC-B :  R1 doit connaître le réseau de PC-B
PC-B → PC-A :  R2 doit connaître le réseau de PC-A

Les deux routes sont nécessaires pour une communication bidirectionnelle.
```

**Schéma mnémotechnique :**

```
[Net-A]──R1──[liaison]──R2──[Net-B]

R1 doit avoir : S Net-B via R2  ← "je sais aller vers Net-B"
R2 doit avoir : S Net-A via R1  ← "je sais répondre vers Net-A"
```

---

## MODULE 4 — SYNTAXE IOS ROUTAGE STATIQUE

### Commandes essentielles

```ios
! ─── Route statique vers un réseau ───────────────────────────────────────
Router(config)# ip route <réseau_dest> <masque_dest> <next-hop_IP>

! Exemple :
R1(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.2

! ─── Route par défaut ─────────────────────────────────────────────────────
Router(config)# ip route 0.0.0.0 0.0.0.0 <next-hop_IP>

! ─── Vérifier la table de routage ────────────────────────────────────────
R1# show ip route
R1# show ip route static       ← seulement les routes statiques
R1# show ip route 192.168.2.0  ← détail d'une route spécifique

! ─── Vérifier une interface ──────────────────────────────────────────────
R1# show interfaces Gi0/1
R1# show ip interfaces brief   ← résumé de toutes les interfaces

! ─── Tester la connectivité ──────────────────────────────────────────────
R1# ping 10.0.0.2
R1# ping 192.168.2.10 source 192.168.1.1  ← ping avec source précise
R1# traceroute 192.168.2.10               ← chemin emprunté
```

---

### Ordre des arguments de `ip route`

```
ip route  [réseau_destination]  [masque]  [next-hop OU interface]
          ──────────────────────────────  ────────────────────────
           QUI je veux joindre ?          PAR OÙ j'envoie ?
```

> 💡 **Mémo :** "QUI ? → PAR OÙ ?"
> Toujours : réseau → masque → next-hop. **Jamais l'inverse.**

---

### Erreurs de syntaxe fréquentes à éviter

| **Erreur** | **Commande incorrecte** | **Commande correcte** |
|---|---|---|
| Ordre inversé (next-hop avant masque) | `ip route 192.168.2.0 10.0.0.2 255.255.255.0` | `ip route 192.168.2.0 255.255.255.0 10.0.0.2` |
| CIDR au lieu de masque | `ip route 192.168.2.0 /24 10.0.0.2` | `ip route 192.168.2.0 255.255.255.0 10.0.0.2` |
| Adresse hôte au lieu de réseau | `ip route 192.168.2.10 255.255.255.0 10.0.0.2` | `ip route 192.168.2.0 255.255.255.0 10.0.0.2` |
| Route par défaut mal écrite | `ip route 0.0.0.0 255.255.255.0 ...` | `ip route 0.0.0.0 0.0.0.0 ...` |

---

## MODULE 5 — POURQUOI LE ROUTAGE STATIQUE ATTEINT SES LIMITES

> Ce module prépare la transition vers OSPF.

### Problèmes du routage statique en conditions réelles

| **Problème** | **Illustration** | **Solution OSPF** |
|---|---|---|
| **Passage à l'échelle** | 50 routeurs × 30 routes = 1 500 commandes à saisir | OSPF calcule automatiquement toutes les routes |
| **Pannes non gérées** | Si un lien tombe, la route statique pointe vers le vide → trafic perdu | OSPF détecte la panne et recalcule un chemin alternatif en secondes |
| **Modifications manuelles** | Ajouter un réseau impose de reconfigurer TOUS les routeurs | OSPF propage automatiquement les nouvelles informations |
| **Erreurs humaines** | Route manquante, oubli du chemin retour | OSPF garantit la cohérence des tables |

### Ce qu'OSPF va apporter

```
Routage statique          →     Routage dynamique OSPF
─────────────────────────────────────────────────────
Manuel, par commande           Automatique
Rigide                         Adaptatif (convergence)
Pas de tolérance aux pannes    Recalcul après panne
Lourd à maintenir              Auto-découverte des voisins
```

> *"OSPF fait automatiquement ce que vous faisiez à la main. Pour que ça fonctionne, il faut que vous compreniez d'abord exactement ce que vous lui déléguez."*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
