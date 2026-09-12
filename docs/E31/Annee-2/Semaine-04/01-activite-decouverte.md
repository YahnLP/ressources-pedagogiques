# 🎲 ACTIVITÉ DÉCOUVERTE – S4 ANNÉE 2 – E31
## « Qui est le Chef du Réseau ? » — Le Problème des Échanges OSPF sur Multi-Accès

---

## 🎯 OBJECTIFS

- ✅ Faire émerger intuitivement le **problème de l'explosion des adjacences** sur un segment LAN
- ✅ Comprendre pourquoi un routeur **DR** est nécessaire sur les réseaux multi-accès
- ✅ Poser la question de **l'élection** : qui devient DR et selon quels critères ?
- ✅ Introduire la notion d'**adjacence sélective** (Full uniquement avec DR/BDR)

---

## ⏱️ DURÉE : 30 min

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur pose l'accroche :**

> *"En S3, vous avez configuré OSPF sur une topologie linéaire A–B–C. Ça fonctionne. Maintenant imaginez qu'un immeuble de bureaux a 8 routeurs tous connectés au même switch central — un LAN partagé. Qu'est-ce qui change pour OSPF ?"*

---

## 🔢 PHASE 1 – Calcul du problème (8 min)

**Le formateur dessine au tableau :**

```
        R1
       / | \
      /  |  \
    R2   R3  R4
     \   |  /
      \  | /
        R5
(tous sur le même switch / segment LAN)
```

**Question au groupe :**

> *"Si chaque routeur OSPF veut former une adjacence Full avec CHACUN des autres, combien d'adjacences bi-directionnelles y a-t-il sur un LAN de N routeurs ?"*

**Chaque groupe calcule :**

| **N routeurs sur le LAN** | **Nb d'adjacences (N×(N-1)/2)** | **Nb d'échanges LSA** |
|---|---|---|
| 2 | | |
| 4 | | |
| 6 | | |
| 8 | | |
| 10 | | |

**Réponses attendues :**

| **N** | **Adjacences** | **Problème** |
|---|---|---|
| 2 | 1 | OK |
| 4 | 6 | Gérable |
| 6 | 15 | Commence à peser |
| 8 | 28 | Beaucoup de trafic OSPF |
| 10 | **45** | Flood de LSA sur tout le LAN |

**Question :** *"Si chaque routeur inonde le segment de ses LSA à chaque changement, que se passe-t-il avec 10 routeurs ?"*

> → **Tempête de LSA** : chaque changement de topologie génère des rafales de paquets OSPF sur le segment. Congestion, instabilité, convergence lente.

---

## 💡 PHASE 2 – La solution intuitive (8 min)

**Le formateur propose :**

> *"Et si on élisait un représentant — un 'chef de réseau' — et que tous les autres lui parlaient SEULEMENT à lui ?"*

**Schéma amélioré :**

```
        R1
        │
    ────┼────   ← Segment LAN partagé
   │    │    │
  R2   DR   R3
        │
       R4
```

> *"Le DR (Designated Router) collecte toutes les informations de topologie et les redistribue. Chaque routeur n'a qu'UNE adjacence Full (avec le DR). Le nombre d'échanges tombe de N×(N-1)/2 à N-1."*

**Nouveau calcul :**

| **N routeurs** | **Sans DR (adj. pleine)** | **Avec DR (adj. avec DR seulement)** |
|---|---|---|
| 4 | 6 | 3 |
| 8 | 28 | 7 |
| 10 | 45 | 9 |

**Question pour le groupe :**

> *"Si le DR tombe en panne, que se passe-t-il ?"*

→ **Nécessité du BDR** (Backup DR) : prêt à prendre le relais immédiatement si le DR disparaît.

---

## 🤔 PHASE 3 – Le problème de l'élection (8 min)

**Le formateur pose la question centrale :**

> *"Très bien. Mais si on a 8 routeurs et qu'on doit élire UN DR, comment on choisit ? Qui décide ? Sur quels critères ?"*

**Brainstorming groupes de 4 — Proposez des critères d'élection :**

| **Critère proposé** | **Avantage** | **Inconvénient** |
|---|---|---|
| | | |
| | | |
| | | |

**Critères typiquement proposés par les apprentis :**

| **Critère** | **Problème** |
|---|---|
| Le plus rapide | Difficile à mesurer de façon neutre |
| Le premier à démarrer | Hasardeux, dépend de l'ordre de démarrage |
| Celui que configure l'admin | Bonne idée ! → c'est `ip ospf priority` |
| Un identifiant unique | Bonne idée ! → c'est le `router-id` |

**Le formateur révèle :**

> *"OSPF utilise deux critères dans l'ordre :*
> *1. La valeur de PRIORITÉ configurée sur l'interface (0–255, défaut 1) — le plus haut gagne*
> *2. En cas d'égalité : le ROUTER-ID le plus élevé*
>
> *Et c'est non-préemptif : une fois élu, le DR garde son rôle même si un routeur plus 'fort' arrive ensuite. L'admin doit relancer pour changer ça."*

---

## ✍️ PHASE 4 – Synthèse à noter (4 min)

**Chaque apprenti note dans sa fiche :**

```
┌─────────────────────────────────────────────────────────────────────┐
│  PROBLÈME : N routeurs sur LAN → N×(N-1)/2 adjacences → flood LSA  │
│                                                                     │
│  SOLUTION OSPF : Élection DR + BDR                                  │
│  → Seuls DR et BDR ont des adjacences Full avec tous                │
│  → Les autres (DROthers) sont en état 2-Way entre eux              │
│                                                                     │
│  CRITÈRES D'ÉLECTION :                                              │
│  1. Priorité OSPF interface (0–255, défaut 1) → plus élevée gagne  │
│     Priority = 0 → ne participe PAS à l'élection                   │
│  2. Router-ID le plus élevé (en cas d'égalité de priorité)         │
│                                                                     │
│  NON-PRÉEMPTIF : DR en place reste DR même si un challenger arrive │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ✅ VALIDATION DE L'ACTIVITÉ

**L'activité est réussie si :**

- ✅ Les apprentis comprennent pourquoi le DR réduit le nombre d'échanges
- ✅ Ils savent que l'élection se base sur priority puis router-id
- ✅ Ils ont formulé le concept de BDR comme secours
- ✅ Ils comprennent l'état 2-Way entre DROthers (normal, pas une erreur)

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
