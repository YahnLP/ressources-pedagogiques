# 🔍 ACTIVITÉ DE DÉCOUVERTE — S3 · 2ᵉ ANNÉE · E31
## « Le réseau qui se connaît lui-même » — Simuler OSPF sans ordinateur

---

> **Durée** : 35 minutes
> **Format** : Groupes de 4 (chaque apprenant joue le rôle d'un routeur)
> **Matériel** : Cette fiche · Fiches "routeur" distribuées par l'enseignant · Enveloppes LSA · Grande feuille LSDB collective
> **Principe** : Avant d'ouvrir Packet Tracer, tu vas ÊTRE un routeur OSPF — tu découvriras ainsi de façon active ce que le protocole fait réellement.

---

## 🎯 Mise en situation

> Imagine que tu es un **routeur** dans un bâtiment d'entreprise.
> À ton démarrage, tu ne connais **que tes propres voisins directs**.
> Pourtant, en quelques secondes, tu vas connaître **la topologie complète du réseau**.
>
> Comment est-ce possible ?
> C'est exactement ce que tu vas découvrir dans cet atelier.

---

## 🗺️ La topologie simulée

```
          192.168.10.0/24                192.168.20.0/24
                │                                │
             Gi0/0                            Gi0/0
           ┌──────┐   10.0.12.0/30          ┌──────┐
           │  R1  ├──────────────────────────┤  R2  │
           └──┬───┘                          └───┬──┘
              │ Gi0/1                      Gi0/1 │
         10.0.14.0/30                    10.0.23.0/30
              │ Gi0/0                      Gi0/0 │
           ┌──┴───┐   10.0.34.0/30          ┌───┴──┐
           │  R4  ├──────────────────────────┤  R3  │
           └──────┘                          └──────┘
             Gi0/1                            Gi0/1
                │                                │
          192.168.40.0/24                192.168.30.0/24
```

---

## 📋 Tes fiches "Routeur" (distribuées par l'enseignant)

> Chaque apprenant reçoit une fiche. Tu ne connais que ce qui est écrit dessus — rien d'autre !

```
┌────────────────────────────────────────────┐
│  JE SUIS : R1                              │
│                                            │
│  Mes réseaux directement connectés :       │
│  • 192.168.10.0/24 (Gi0/0)                │
│  • 10.0.12.0/30    (Gi0/1 → vers R2)      │
│  • 10.0.14.0/30    (Gi0/1 → vers R4)      │
│                                            │
│  Mes voisins directs :                     │
│  • R2 sur 10.0.12.2                       │
│  • R4 sur 10.0.14.2                       │
└────────────────────────────────────────────┘
```

*(Fiches équivalentes pour R2, R3, R4 — distribuées par l'enseignant)*

---

## 🔁 PHASE 1 — Discovery : je salue mes voisins (5 min)

> Dans OSPF, la première chose qu'un routeur fait au démarrage est d'envoyer des **paquets Hello**
> à tous ses voisins directs pour leur signaler son existence.

**Action :** Chaque "routeur" (apprenant) dit à voix haute à ses voisins directs :
*"Hello ! Je suis [nom] et je viens de démarrer. Es-tu là ?"*

Le voisin répond : *"Hello ! Je te reçois. Tu deviens mon voisin."*

**Question 1.1** — Après cette phase, R1 connaît-il la topologie complète du réseau ?

```
☐ Oui, R1 connaît maintenant tout le réseau
☐ Non, R1 ne connaît encore que : _________________________________________
```

**Question 1.2** — À ce stade, combien de routeurs R1 a-t-il découverts ?

```
Routeurs voisins de R1 : ___________________________________________________
Routeurs encore inconnus de R1 : ___________________________________________
```

---

## 📨 PHASE 2 — Exchange : j'envoie mes LSA (10 min)

> Chaque routeur crée un **LSA (Link-State Advertisement)** — un message qui décrit
> TOUS ses réseaux directement connectés et ses voisins.
> Il envoie ce LSA à TOUS ses voisins.

**Action :** Remplis ta "enveloppe LSA" avec les informations de ta fiche routeur :

```
┌──────────────────────────────────────────────────────────┐
│  MON LSA                                                 │
│  Expéditeur (Router-ID) : _______________________________│
│  Mes réseaux connectés :                                 │
│    • _____________________________________________________│
│    • _____________________________________________________│
│    • _____________________________________________________│
│  Mes voisins OSPF (et via quelle interface) :           │
│    • _____________________________________________________│
│    • _____________________________________________________│
│  Numéro de séquence : 1                                  │
└──────────────────────────────────────────────────────────┘
```

**Passe ton enveloppe LSA à chacun de tes voisins directs.**

**Question 2.1** — R1 vient de recevoir le LSA de R2. Que contient ce LSA ?

```
Réseaux de R2 : _____________________________________________________________
Voisins de R2 : _____________________________________________________________
Grâce au LSA de R2, R1 connaît maintenant des réseaux qu'il ne connaissait pas avant :
_______________________________________________________________________________
```

---

## 🌊 PHASE 3 — Flood : je transmets les LSA que je reçois (10 min)

> Un routeur OSPF ne garde pas les LSA pour lui :
> il les **retransmet (flood)** à TOUS ses voisins, sauf celui qui lui a envoyé le LSA.
> Ainsi, l'information se propage dans tout le réseau comme une onde.

**Action :** Quand tu reçois le LSA d'un autre routeur :
1. Ajoute son contenu dans ta **LSDB (la grande feuille collective)**
2. Retransmet ce LSA à tes autres voisins (pas à celui qui te l'a envoyé)

**Remplis ta LSDB locale — note tout ce que tu as reçu :**

```
LSDB DE _______

┌────────────────┬──────────────────────────────────┬───────────────────┐
│  Router-ID     │  Réseaux connectés               │  Voisins déclarés │
│  (expéditeur)  │                                  │                   │
├────────────────┼──────────────────────────────────┼───────────────────┤
│ R1             │                                  │                   │
├────────────────┼──────────────────────────────────┼───────────────────┤
│ R2             │                                  │                   │
├────────────────┼──────────────────────────────────┼───────────────────┤
│ R3             │                                  │                   │
├────────────────┼──────────────────────────────────┼───────────────────┤
│ R4             │                                  │                   │
└────────────────┴──────────────────────────────────┴───────────────────┘
```

**Question 3.1** — Après le flood, les LSDB de R1, R2, R3 et R4 sont-elles identiques ?

```
☐ Oui — chaque routeur a reçu les LSA de TOUS les autres
☐ Non — certains routeurs ont des informations différentes
Explication : _________________________________________________________________
```

**Question 3.2** — La LSDB contient-elle maintenant assez d'informations pour reconstruire la **carte complète** du réseau ?

```
☐ Oui — elle contient tous les liens et tous les réseaux
☐ Non — il manque : _________________________________________________________
```

---

## 🧮 PHASE 4 — SPF : je calcule le meilleur chemin (5 min)

> Chaque routeur **calcule lui-même** le meilleur chemin vers chaque destination
> en utilisant l'algorithme SPF (Shortest Path First) de Dijkstra.
> Il ne demande pas aux autres — il calcule depuis sa propre LSDB.

> Pour simplifier, on suppose que tous les liens ont le même coût (**cost = 1**).

**À partir de ta LSDB, complète le tableau des meilleurs chemins depuis TON routeur :**

| Destination | Chemin le plus court | Cost total |
|---|---|---|
| 192.168.10.0/24 | | |
| 192.168.20.0/24 | | |
| 192.168.30.0/24 | | |
| 192.168.40.0/24 | | |

**Question 4.1** — Deux chemins différents existent pour aller de R1 à 192.168.30.0/24.
En supposant tous les liens à cost 1, lequel OSPF choisit-il ?

```
Chemin A : R1 → R2 → R3 → 192.168.30.0  Cost = _____ + _____ + _____ = _____
Chemin B : R1 → R4 → R3 → 192.168.30.0  Cost = _____ + _____ + _____ = _____
OSPF choisit : ☐ Chemin A  ☐ Chemin B  ☐ Les deux (ECMP)
```

**Question 4.2** — Si le lien R1-R2 tombe en panne, OSPF doit-il reconfigurer les routes manuellement ?

```
☐ Oui — un admin doit intervenir
☐ Non — OSPF recalcule automatiquement

Voici ce qui se passe en cas de panne :
1. R1 et R2 ne reçoivent plus les _______ (paquets de keepalive OSPF)
2. Après _____ secondes (Dead Interval), ils déclarent le voisin mort
3. Ils envoient un nouveau _______ pour informer tout le réseau
4. Chaque routeur recalcule son arbre _______ depuis sa LSDB mise à jour
5. Les nouvelles routes apparaissent dans la table de routage → trafic redirigé
```

---

## 🏁 Bilan de l'atelier

**Complète avec tes propres mots :**

```
OSPF est un protocole de routage à "état de ___________".

La différence avec RIP (vecteur de distance) : OSPF partage une _______ complète
du réseau, alors que RIP partage seulement une _______ de distance.

Le LSA contient : ___________________________________________________________

La LSDB est : _______________________________________________________________
et elle est __________________ sur tous les routeurs de la même _______.

L'algorithme SPF sert à : ___________________________________________________

Si un lien tombe, OSPF converge en quelques ____________ de façon _____________.
```

> ✅ Tu viens de simuler exactement ce que OSPF fait en quelques secondes.
> Le cours va maintenant préciser les métriques, les aires et les identifiants de routeurs.

---

## 📎 Pour l'enseignant — Corrections et points de débrieffe

**Réponses clés :**
- 1.1 : Non — R1 ne connaît que R2 et R4 après le Hello
- 3.1 : **Oui** — c'est LA propriété fondamentale d'OSPF : toutes les LSDB sont identiques dans une aire
- 4.1 : Les deux chemins ont cost 3 — OSPF installe les deux (ECMP — Equal Cost Multi-Path)
- 4.2 : Non — recalcul automatique ; les 4 étapes : Hello manquant → Dead Interval → LSA de mise à jour → SPF recalcul

**Points à souligner impérativement lors du débrieffe :**
1. *"Chaque routeur calcule LUI-MÊME le chemin — il ne demande pas à ses voisins"* (différence fondamentale avec RIP)
2. *"La LSDB est identique sur tous les routeurs de l'aire — c'est la clé"*
3. *"Le flood s'arrête quand tous ont reçu le LSA (numéro de séquence)"*

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S3*
*Compétences : S2.3 · S2.4*
