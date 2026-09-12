# 📝 DEVOIR & LIVRABLE PORTFOLIO — S3 · 2ᵉ ANNÉE · E31
## OSPF : Concepts · Convergence · Aires · Router-ID · Coût

---

> **Module** : E31 – Infrastructure Réseau · OSPF Concepts
> **Épreuve visée** : **E31** – Épreuve pratique infrastructure réseau
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)
> **Format du rendu** : Fiche complétée, schémas soignés

---

## 📌 Compétences du référentiel évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S2.3** | Fonctionnement OSPF, convergence, LSA, LSDB, SPF | /35 |
| **S2.4** | Aires OSPF, Area 0, ABR, O vs O IA | /25 |
| **C2.1** | Router-ID, calcul et impact des coûts | /25 |
| **C2.3** | Analyser une sortie de commande, diagnostiquer | /15 |
| | **TOTAL** | **/100** |

---

## 🅰️ PARTIE A — En classe (45 min)

### 📡 Exercice 1 — Convergence OSPF (/35)

**1.a** — Un réseau démarre avec 4 routeurs qui ne se connaissent pas encore. Décris les **5 étapes** par lesquelles OSPF passe pour converger. Pour chaque étape, indique le type de paquet ou mécanisme impliqué. *(15 pts)*

```
Étape 1 — Nom : ___________________________
  Mécanisme : ______________________________________________________________
  Paquet échangé : _________________________________________________________
  Intervalle : _______ secondes   Multicast utilisé : _______________________

Étape 2 — Nom : ___________________________
  Ce qui se passe : ________________________________________________________
  État final de la relation entre deux routeurs : ____________________________

Étape 3 — Nom : ___________________________
  Paquet : LSA (Link State Advertisement)
  Contenu d'un LSA : _______________________________________________________
  Portée de la diffusion : _________________________________________________

Étape 4 — Nom : ___________________________
  Résultat : tous les routeurs ont la même _________________________________
  Commande pour le vérifier : ______________________________________________

Étape 5 — Nom : ___________________________
  Algorithme utilisé : _____________________________________________________
  Résultat : mise à jour de ________________________________________________
  Commande pour voir le résultat : _________________________________________
```

**1.b** — Dans `show ip ospf neighbor`, un voisin apparaît à l'état **INIT** au lieu de **FULL**.
Qu'est-ce que cela signifie ? Quelle en est la cause probable ? *(5 pts)*

```
État INIT signifie : _________________________________________________________
Cause probable : ____________________________________________________________
Action pour diagnostiquer : __________________________________________________
```

**1.c** — Le Dead interval OSPF est de **40 secondes** par défaut. Explique ce qui se passe si un routeur ne reçoit plus de Hello d'un voisin pendant 40 secondes. *(5 pts)*

```
Après 40s sans Hello :
1. Le voisin est déclaré : ___________________________________________________
2. Le routeur envoie un nouveau : _____________ pour notifier tous les autres
3. Tous les routeurs de l'aire recalculent avec : _____________________________
4. La table de routage est mise à jour en : ______ secondes environ
5. Ce processus s'appelle la : _______________________________________________
```

**1.d** — Quel est l'avantage du Dead interval de 40s par rapport à un Dead interval de 5s ?
Et l'inconvénient ? *(5 pts)*

```
Dead interval 40s :
  Avantage : _______________________________________________________________
  Inconvénient : ___________________________________________________________

Dans un réseau critique (hôpital, salle de marché) tu préférerais : ☐ 40s ☐ 5s
Car : ______________________________________________________________________
```

**1.e** — Complète le schéma de séquence de convergence entre R1 et R2 en ajoutant les flèches et étiquettes manquantes. *(5 pts)*

```
R1                                          R2
│                                            │
│ ─────────────────────────────────────────► │  ← quel paquet ? __________
│ ◄───────────────────────────────────────── │
│                                            │
│         Adjacence ___________ établie      │
│                                            │
│ ─────────────────────────────────────────► │  ← LSA de R1 vers R2
│ ◄───────────────────────────────────────── │  ← LSA de ___ vers ___
│                                            │
│  LSDB R1 = _________________ de LSDB R2   │
│                                            │
│  Calcul _________________ sur R1 et R2     │
│                                            │
│  Table de routage mise à jour             │
```

---

### 🏛️ Exercice 2 — Aires OSPF (/25)

> Topologie : une entreprise avec 4 sites

```
Site Central (Area 0) :    RA ─── RB ─── RC
                                    │
                                  ABR1
                                  /   \
              Area 1 :          RD     RE ─── RF (Area 2)
```

**2.a** — Parmi les routeurs RA, RB, RC, RD, RE, RF, ABR1 : lequel (ou lesquels) est un ABR (Area Border Router) ? Justifie. *(5 pts)*

```
ABR = routeur qui est membre de _______ aires simultanément
ABR(s) dans cette topologie : _____________________________________________
Justification : ____________________________________________________________
```

**2.b** — Un paquet va de RF (Area 2) vers RC (Area 0). Quel chemin emprunte-t-il ? Indique les aires traversées. *(5 pts)*

```
Chemin : RF → ___ → ___ → ABR1 → ___ → ___ → RC
Aires : Area ___ → Area ___ → Area ___
```

**2.c** — Dans la table de routage de RD (Area 1), les routes vers les réseaux de Area 0 apparaissent avec le code **O IA**. Explique pourquoi O IA et non O. *(5 pts)*

```
Code O    signifie : route apprise via OSPF, réseau dans la _________________ aire
Code O IA signifie : route apprise via OSPF, réseau dans une ________________ aire
RD voit les réseaux de Area 0 en O IA car : ___________________________________
```

**2.d** — Dessine le schéma des aires de l'entreprise en respectant la règle fondamentale d'OSPF sur les aires. *(5 pts)*

```
(Réalise ton schéma dans l'espace ci-dessous en identifiant clairement Area 0, Area 1, Area 2 et les ABR)

┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**2.e** — Quelle est la règle fondamentale à ne jamais violer dans la conception des aires OSPF ? *(5 pts)*

```
Règle : ____________________________________________________________________
Conséquence si violée : _____________________________________________________
Solution si une aire est physiquement déconnectée de Area 0 : ________________
```

---

## 🅱️ PARTIE B — En autonomie (/40)

### 🆔 Exercice 3 — Router-ID et Loopback (/15)

> Un routeur R5 a les interfaces suivantes actives :
> - GigabitEthernet0/0 : 172.16.5.1/24
> - GigabitEthernet0/1 : 10.0.45.2/30
> - GigabitEthernet0/2 : 10.0.56.1/30
> - Loopback0 : 5.5.5.5/32

**3.a** — Quel est le Router-ID qu'OSPF choisira pour R5 ? Justifie en détaillant la règle de priorité. *(5 pts)*

```
Règle 1 — Router-ID configuré manuellement : ☐ présent ☐ absent
Règle 2 — Plus haute IP de Loopback active : ______________________
Règle 3 — Plus haute IP d'interface physique : ______________________
Router-ID choisi : _______________________  (applique la règle n° _____)
```

**3.b** — L'interface Gi0/2 (10.0.56.1) tombe en panne. Le Router-ID change-t-il ? *(3 pts)*

```
☐ Oui — nouveau Router-ID = _______________________
☐ Non — car ________________________________________________________________
Quel est l'avantage de la Loopback pour la stabilité OSPF ? ___________________
```

**3.c** — L'administrateur veut forcer le Router-ID à `55.55.55.55` indépendamment des interfaces.
Écris la suite de commandes IOS : *(4 pts)*

```
R5(config)# router ospf ___
R5(config-router)# router-id _______________
R5(config-router)# end
R5# _________________________ ospf process   ← pour appliquer immédiatement
```

**3.d** — Si deux routeurs d'un même domaine OSPF ont le même Router-ID, que se passe-t-il ? *(3 pts)*

```
Conséquence : _______________________________________________________________
Comment l'éviter : __________________________________________________________
```

---

### 💹 Exercice 4 — Calcul des coûts et choix de chemin (/25)

> Topologie : 3 chemins entre R1 et R6

```
      10 Mbps     100 Mbps     1 Gbps
R1 ─────────── R2 ─────────── R3 ─────────── R6 (LAN 192.168.6.0/24)
│                                              │
│  100 Mbps         100 Mbps                  │
└────────── R4 ─────────────── R5 ────────────┘
                 1 Gbps
```

*Référence de bande passante OSPF : 100 Mbps (par défaut)*

**4.a** — Calcule le coût de chaque lien : *(10 pts)*

| Lien | Débit | Formule | Coût |
|---|---|---|---|
| R1 → R2 | 10 Mbps | 100 Mbps / 10 Mbps = | |
| R2 → R3 | 100 Mbps | 100 / 100 = | |
| R3 → R6 | 1 Gbps | 100 / 1000 = | |
| R1 → R4 | 100 Mbps | | |
| R4 → R5 | 1 Gbps | | |
| R5 → R6 | 100 Mbps | | |

**4.b** — Calcule le coût total de chaque chemin (du réseau source de R1 jusqu'au LAN de R6) : *(8 pts)*

```
Chemin du haut (R1→R2→R3→R6) :
  Coût(R1→R2) + Coût(R2→R3) + Coût(R3→R6) + Coût(R6→LAN)
= _______ + _______ + _______ + 1 (LAN directement connecté à R6)
= _______

Chemin du bas (R1→R4→R5→R6) :
  Coût(R1→R4) + Coût(R4→R5) + Coût(R5→R6) + 1
= _______ + _______ + _______ + 1
= _______

OSPF choisit : chemin _______ (coût _______ < _______ )
```

**4.c** — Le problème de la référence par défaut. Que vaut le coût du lien R3→R6 (1 Gbps) avec la référence par défaut ? *(3 pts)*

```
Coût = 100 Mbps / 1 000 Mbps = _______ → arrondi à _______ (minimum)
Coût du lien R2→R3 (100 Mbps) = _______ 
Les deux liens ont-ils le même coût ? ☐ Oui → OSPF ne peut pas les différencier
Solution : auto-cost reference-bandwidth _______ (Mbps)
Avec cette nouvelle référence : coût R2→R3 = ______ Mbps / 100 Mbps = _______
                                  coût R3→R6 = ______ Mbps / 1000 Mbps = _______
```

**4.d** — Après avoir changé la référence à 1 000 Mbps sur TOUS les routeurs, recalcule les coûts et le chemin choisi : *(4 pts)*

```
Avec référence 1 000 Mbps :
  R1→R2 (10 Mbps) : coût = _______
  R2→R3 (100 Mbps) : coût = _______
  R3→R6 (1 Gbps) : coût = _______
  R1→R4 (100 Mbps) : coût = _______
  R4→R5 (1 Gbps) : coût = _______
  R5→R6 (100 Mbps) : coût = _______

Chemin du haut total : _______ + _______ + _______ + 1 = _______
Chemin du bas total  : _______ + _______ + _______ + 1 = _______
OSPF choisit maintenant : chemin _______ — la décision a-t-elle changé ? ☐ Oui ☐ Non
```

---

## 🏅 Barème global et grille Qualiopi

| Exercice | Compétences RNCP | Barème | Seuil de validation |
|---|---|---|---|
| Ex. 1 — Convergence OSPF (5 étapes + états) | S2.3 | /35 | ≥ 20/35 |
| Ex. 2 — Aires OSPF, ABR, O IA | S2.4 | /25 | ≥ 14/25 |
| Ex. 3 — Router-ID et Loopback | C2.1 | /15 | ≥ 8/15 |
| Ex. 4 — Calcul de coûts et chemin optimal | C2.1 + C2.3 | /25 | ≥ 14/25 |
| **TOTAL** | | **/100** | **≥ 55/100** |

> 📌 **Note Qualiopi** : Ce devoir constitue une preuve d'acquisition conceptuelle OSPF pour **E31**. Conserver avec signature enseignant et date.

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

---

## Correction Exercice 1

**1.a** :
1. Hello packets — envoyés toutes les 10s en 224.0.0.5 — découverte des voisins
2. Établissement des adjacences — état FULL
3. Échange LSA — description des liens directs, inondation dans l'aire
4. Construction LSDB — même base sur tous les routeurs · `show ip ospf database`
5. Calcul SPF/Dijkstra → table de routage avec codes O · `show ip route`

**1.b** : INIT = Hello reçu mais R2 n'est pas dans la liste du Hello de R1 (sens unique seulement) → problème de paramètres non correspondants (Hello interval, dead interval, area ID, auth) ou interface côté R1 pas encore UP

**1.c** : Le voisin est déclaré DOWN → nouveau LSA envoyé à toute l'aire → tous recalculent SPF → convergence en ~40-45s

**1.d** : Dead interval 40s : avantage = moins sensible aux pertes temporaires de paquets / inconvénient = convergence plus lente en cas de vraie panne. Dans un réseau critique : 5s préférable (convergence plus rapide au prix d'une plus grande sensibilité aux faux positifs)

---

## Correction Exercice 2

**2.a** : ABR1 est le seul ABR — il est membre de Area 0 ET Area 1 ET Area 2

**2.b** : RF → RE → ABR1 → RB → RC — Area 2 → Area 0 → Area 0

**2.c** : O = intra-aire (même aire) · O IA = inter-aire (autre aire) · RD est dans Area 1, les réseaux de Area 0 sont dans une autre aire → O IA

**2.e** : Règle : toutes les aires doivent être physiquement connectées à Area 0. Si violée : pas de routage inter-aires (les LSA inter-aires ne passent pas). Solution : Virtual Link (tunnel logique à travers une aire jusqu'à Area 0)

---

## Correction Exercice 3

**3.a** : Règle 2 (Loopback) s'applique → Router-ID = **5.5.5.5**

**3.b** : Non — Loopback0 (5.5.5.5) reste active → Router-ID stable même si Gi0/2 tombe

**3.c** :
```
R5(config)# router ospf 1
R5(config-router)# router-id 55.55.55.55
R5(config-router)# end
R5# clear ip ospf process
```

**3.d** : Conflit de Router-ID → instabilité OSPF, adjacences se cassent, convergence impossible → vérifier avec `show ip ospf` et forcer des Router-ID uniques

---

## Correction Exercice 4

**4.a** (référence 100 Mbps) :

| Lien | Coût |
|---|---|
| R1→R2 (10 Mbps) | **10** |
| R2→R3 (100 Mbps) | **1** |
| R3→R6 (1 Gbps) | **1** (minimum) |
| R1→R4 (100 Mbps) | **1** |
| R4→R5 (1 Gbps) | **1** |
| R5→R6 (100 Mbps) | **1** |

**4.b** :
- Chemin haut : 10 + 1 + 1 + 1 = **13**
- Chemin bas : 1 + 1 + 1 + 1 = **4**
- OSPF choisit le chemin **bas** (coût 4)

**4.c** : GigabitEthernet → 100/1000 = 0,1 → arrondi à **1** = même que FastEthernet → problème de différenciation · Solution : référence 1000 Mbps · FastEthernet → 1000/100 = **10** · GigabitEthernet → 1000/1000 = **1**

**4.d** (référence 1 000 Mbps) :
- R1→R2 (10 Mbps) : 1000/10 = **100**
- R2→R3 (100 Mbps) : 1000/100 = **10**
- R3→R6 (1 Gbps) : 1000/1000 = **1**
- R1→R4 (100 Mbps) : **10**
- R4→R5 (1 Gbps) : **1**
- R5→R6 (100 Mbps) : **10**
- Chemin haut : 100+10+1+1 = **112**
- Chemin bas : 10+1+10+1 = **22**
- OSPF choisit toujours le chemin **bas** — décision identique mais les coûts sont maintenant différenciés entre 100M et 1G

---

*Devoir & Livrable Portfolio + Correction — Ne pas distribuer avant le rendu*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S3*
*Épreuve E31 | Compétences S2.3 · S2.4 · C2.1 · C2.3*
*Conforme référentiel Qualiopi*
