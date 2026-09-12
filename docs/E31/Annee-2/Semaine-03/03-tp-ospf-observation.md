# 🔬 TRAVAUX PRATIQUES — S3 · 2ᵉ ANNÉE · E31
## Observer OSPF en fonctionnement · Costs · Convergence · Packet Tracer

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Packet Tracer**
> **Fichier .pkt** : `S3_E31_TP_OSPF_Observation.pkt` (fourni par l'enseignant)
> **Épreuve ciblée** : **E31** – Épreuve pratique infrastructure réseau

---

## 📌 Compétences travaillées

| Code | Compétence | Niveau attendu |
|---|---|---|
| **S2.3** | Fonctionnement OSPF | Observer les phases, la LSDB, les voisinages |
| **S2.4** | Métriques OSPF | Calculer les costs et identifier le chemin choisi |
| **C2.3** | Diagnostic | Analyser la table de routage OSPF et prédire le comportement |

> ⚠️ Ce TP est en **mode observation** uniquement — tu ne configures PAS OSPF (→ S4).
> OSPF est déjà configuré sur tous les routeurs. Tu observes et analyses.

---

## 🗺️ Topologie

```
               LAN1                              LAN2
          192.168.1.0/24                    192.168.2.0/24
                │                                  │
             Gi0/0                              Gi0/0
           ┌──────┐                            ┌──────┐
           │  R1  │                            │  R2  │
           │1.1.1.1│                           │2.2.2.2│
           └──┬───┘                            └───┬──┘
              │Gi0/2           Gi0/2               │Gi0/2
         Serial(64K)═══════Serial(64K)        GE(1G)║
              │Gi0/1           Gi0/1               │Gi0/1
              │                                    │
           ┌──┴───┐   GE(1G)   ┌──────┐  GE(1G)  ┌───┴──┐
           │  R4  ├────────────┤  R3  ├───────────┤  R2  │
           │4.4.4.4│            │3.3.3.3│           └──────┘
           └──────┘            └──────┘
             Gi0/1              Gi0/0
                │                  │
           192.168.4.0/24   192.168.3.0/24
               LAN4               LAN3

Liens et vitesses :
  R1-R2 : Serial 64 kbps → cost ≈ 1562
  R1-R4 : GigabitEthernet 1 Gbps → cost = 1
  R2-R3 : GigabitEthernet 1 Gbps → cost = 1
  R3-R4 : GigabitEthernet 1 Gbps → cost = 1

Router-IDs (configurés via loopback) :
  R1 = 1.1.1.1   R2 = 2.2.2.2   R3 = 3.3.3.3   R4 = 4.4.4.4
```

---

## 🔵 PARTIE 1 — Calculs de costs AVANT de lancer Packet Tracer (15 min)

> **Avant d'ouvrir le fichier .pkt**, réponds à ces questions par le calcul.
> Tu vérifieras tes réponses avec Packet Tracer ensuite.

**1.1** — Calcule le cost de chaque lien (référence par défaut : 100 Mbps) :

| Lien | Débit | Formule | Cost calculé |
|---|---|---|---|
| R1 ─ R2 (Serial 64k) | 0,064 Mbps | 100 / 0,064 = | |
| R1 ─ R4 (GE) | 1 000 Mbps | 100 / 1 000 = | arrondi à |
| R2 ─ R3 (GE) | 1 000 Mbps | | |
| R3 ─ R4 (GE) | 1 000 Mbps | | |

**1.2** — Il existe deux chemins de R1 vers LAN2 (192.168.2.0/24). Calcule le cost total de chacun :

```
Chemin A : R1 ─(Serial)─ R2 ─ LAN2
  Cost = _______ + cost interface d'entrée R2 Gi0/0 (gratuit, non comptabilisé)
  Cost total A = _______

Chemin B : R1 ─(GE)─ R4 ─(GE)─ R3 ─(GE)─ R2 ─ LAN2
  Cost = _______ + _______ + _______ = _______
  Cost total B = _______
```

**1.3** — Quel chemin OSPF choisit-il pour aller de R1 vers LAN2 ? Justifie.

```
OSPF choisit : ☐ Chemin A (direct via Serial)  ☐ Chemin B (via R4-R3)
Car : cost ______ < cost ______
La route dans la table de R1 sera : O 192.168.2.0/24 [110/_____] via _______
```

---

## 🔵 PARTIE 2 — Observer les voisinages OSPF (10 min)

**2.1** — Ouvre le fichier .pkt et va sur R1. Tape la commande `show ip ospf neighbor` :

```
Copie le résultat :
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
```

**2.2** — Identifie les voisins de R1 et leur état :

| Voisin (Router-ID) | Adresse IP | Interface | État |
|---|---|---|---|
| | | | |
| | | | |

**2.3** — L'état `FULL` signifie que l'adjacence est complètement établie.
Y a-t-il des voisins dans un autre état ? Si oui, c'est une anomalie.

```
Tous les voisins sont en état FULL ? ☐ Oui ✓   ☐ Non → anomalie sur : _______
```

**2.4** — `show ip ospf neighbor` affiche aussi les Dead Time restants. À quoi sert cette information ?

```
Dead Time restant = _______ secondes (environ)
Si ce compteur atteint 0, cela signifie : _____________________________________
La valeur Dead Interval configurée est probablement : _______ secondes
```

---

## 🔵 PARTIE 3 — Inspecter la LSDB (10 min)

**3.1** — Sur R1, tape `show ip ospf database`. Observe la structure :

```
Combien de routeurs apparaissent dans la section "Router Link States" ? _______
Ces routeurs correspondent à : ☐ tous les routeurs du réseau ☐ seulement les voisins de R1
```

**3.2** — Vérifie que la même LSDB est présente sur R3 (`show ip ospf database` sur R3).
Le nombre d'entrées est-il identique ?

```
Nombre d'entrées LSDB sur R1 : _______
Nombre d'entrées LSDB sur R3 : _______
Identiques ? ☐ Oui — LSDB synchronisée ✓   ☐ Non — problème de synchronisation
```

**3.3** — Cette propriété (LSDB identique sur tous les routeurs) est fondamentale dans OSPF.
Pourquoi est-elle nécessaire pour que le SPF fonctionne correctement ?

```
___________________________________________________________________________
___________________________________________________________________________
```

---

## 🔵 PARTIE 4 — Analyser la table de routage OSPF (15 min)

**4.1** — Sur R1, tape `show ip route ospf`. Copie et complète le tableau :

| Code | Réseau destination | Cost (métrique) | Next-hop | Via |
|---|---|---|---|---|
| O | | | | |
| O | | | | |
| O | | | | |
| O | | | | |

**4.2** — Compare le cost réel affiché par Packet Tracer avec tes calculs de la Partie 1 :

```
Cost calculé pour R1→LAN2 : _______   Cost affiché dans la table : _______
Sont-ils identiques ? ☐ Oui ✓   ☐ Non — différence due à : ________________
```

**4.3** — Sur R1, tape `show ip ospf interface GigabitEthernet0/1`.
Quel cost est affiché pour cette interface ?

```
Cost de l'interface Gi0/1 (R1-R4) : _______
Ce cost correspond à une interface de type : _______________________________
```

**4.4** — Sur R1, tape `show ip ospf interface Serial0/0/0`.
Quel cost est affiché pour cette interface Serial ?

```
Cost de l'interface Serial (R1-R2) : _______
Ce cost élevé explique pourquoi OSPF : ____________________________________
```

---

## 🔴 PARTIE 5 — Simuler une panne et observer la convergence (20 min)

> **OBJECTIF** : couper le lien R1-R4 (GE) et observer ce qui se passe dans la table de R1.

**5.1 — AVANT la panne** : note le chemin actuel vers LAN2 (192.168.2.0/24) depuis R1 :

```
Route actuelle : O 192.168.2.0/24 [110/_____] via _______
Chemin emprunté : R1 → _______ → _______ → R2
```

**5.2 — PROVOQUER LA PANNE** :
- Va sur le routeur R4
- Tape : `interface GigabitEthernet0/0` puis `shutdown`
- Reviens sur R1

**5.3 — ATTENDRE** : observe en temps réel pendant environ 45 secondes.
Note ce qui se passe dans `show ip ospf neighbor` :

```
Immédiatement après shutdown :
Voisin R4 toujours présent ? ☐ Oui ☐ Non
Dead Time restant pour R4 : _______ secondes

Après ~40 secondes :
R4 a-t-il disparu de la liste des voisins ? ☐ Oui ☐ Non
```

**5.4 — APRÈS CONVERGENCE** : tape `show ip route ospf` et note la nouvelle route vers LAN2 :

```
Nouvelle route : O 192.168.2.0/24 [110/_____] via _______
Nouveau chemin : R1 → _______ (via quel lien ? _______)
```

**5.5** — La route vers LAN2 a-t-elle disparu pendant la convergence, ou OSPF a-t-il basculé directement ?

```
☐ La route a disparu pendant environ _______ secondes (trou de connectivité)
☐ OSPF a basculé instantanément vers l'autre chemin
☐ Je n'ai pas pu observer (timing)

Le Dead Interval (40s) représente : ___________________________________________
```

**5.6 — RÉTABLISSEMENT** : sur R4, tape `no shutdown` sur l'interface.
Quelle route vers LAN2 OSPF réinstalle-t-il ?

```
Route rétablie : O 192.168.2.0/24 [110/_____] via _______
OSPF est revenu au chemin ☐ optimal (via GE)  ☐ alternatif (via Serial)
Car : ______________________________________________________________________
```

---

## 📄 Compte rendu synthétique

**Réponds aux 3 questions en 2-3 lignes chacune :**

**Q1 — Pourquoi OSPF préfère-t-il les liens GigabitEthernet aux liens Serial dans ce TP ?**

```
___________________________________________________________________________
___________________________________________________________________________
```

**Q2 — Quel avantage concret OSPF offre-t-il par rapport au routage statique vu en S2 ?**

```
___________________________________________________________________________
___________________________________________________________________________
```

**Q3 — Que devrait-on modifier si on voulait qu'OSPF distingue un lien 100 Mbps d'un lien 1 Gbps ?**

```
___________________________________________________________________________
___________________________________________________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Calculer le cost d'un lien (formule) | ☐ | ☐ | ☐ |
| Calculer le cost cumulé d'un chemin | ☐ | ☐ | ☐ |
| Lire la table de routage OSPF ([110/cost]) | ☐ | ☐ | ☐ |
| Utiliser show ip ospf neighbor | ☐ | ☐ | ☐ |
| Comprendre le rôle de la LSDB | ☐ | ☐ | ☐ |
| Observer la convergence OSPF après panne | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Calculs de costs corrects (Partie 1) | /5 |
| Observation des voisinages (Partie 2) | /5 |
| Analyse de la LSDB (Partie 3) | /5 |
| Lecture de la table de routage OSPF (Partie 4) | /5 |
| Observation et analyse de la convergence (Partie 5) | /5 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Partie 1 — Calculs de costs

| Lien | Cost |
|---|---|
| R1-R2 Serial 64k | 100 000 / 64 ≈ **1 562** |
| R1-R4 GE | 100 / 1 000 = 0,1 → arrondi à **1** (minimum) |
| R2-R3 GE | **1** |
| R3-R4 GE | **1** |

**Chemin A** : Serial cost 1 562 → total **1 562**
**Chemin B** : GE(1) + GE(1) + GE(1) = **3**
→ OSPF choisit Chemin B · `O 192.168.2.0/24 [110/3] via R4 (ou 10.0.14.2)`

## Partie 5 — Convergence

- Immédiatement : R4 toujours présent (Dead Interval pas encore expiré)
- Après ~40s : R4 disparaît · OSPF recalcule
- Nouvelle route : via Serial (R1→R2 direct), cost 1 562
- Après `no shutdown` : OSPF rétablit la route via GE (cost 3 < 1 562)

**Q3** : Taper `auto-cost reference-bandwidth 1000` sur tous les routeurs → GE=1, FE=10, plus de confusion entre les deux vitesses.

---

*TP OSPF Observation + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S3*
*Document Portfolio E31 — Compétences S2.3 · S2.4 · C2.3*
