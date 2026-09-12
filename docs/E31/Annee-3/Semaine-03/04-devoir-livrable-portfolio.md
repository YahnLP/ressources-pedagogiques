# 📝 DEVOIR & LIVRABLE PORTFOLIO — S3 · 3ᵉ ANNÉE · E31
## BGP : AS · eBGP vs iBGP · Attributs · Table BGP · Sélection du chemin

---

> **Module** : E31 – Infrastructure Réseau — BGP
> **Épreuve visée** : **E31** – Épreuve pratique
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 50 min)

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S2.4** | BGP : AS, eBGP/iBGP, peering, configuration | /35 |
| **S2.5** | Attributs BGP : AS-path, Local-Pref, MED | /30 |
| **C2.2** | Écrire les commandes de configuration BGP | /20 |
| **C2.3** | Analyser `show bgp summary` et `show bgp ipv4 unicast` | /15 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation

> Tu es **administrateur réseau** d'une entreprise multi-sites avec son propre AS.
> L'entreprise a deux FAI pour la redondance et doit contrôler comment le trafic entre et sort.

---

## 🅰️ PARTIE A — En classe (45 min)

### 🌐 Exercice 1 — Concepts BGP (/35)

**1.a** — Explique en 3 lignes pourquoi OSPF ne peut pas être utilisé pour interconnecter des AS différents sur Internet : *(6 pts)*

```
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**1.b** — Complète le tableau comparatif eBGP / iBGP : *(12 pts)*

| Critère | eBGP | iBGP |
|---|---|---|
| AS des deux voisins | Différents | |
| AS-path modifié à l'envoi | Oui (AS local ajouté) | |
| Next-hop modifié | Oui | |
| Utilisé pour | Entre FAI ou organisations | |
| Propagation des routes reçues | | Split horizon iBGP |
| Session TCP | Sur lien direct généralement | Via Loopback souvent |

**1.c** — Un routeur BGP reçoit le préfixe `203.0.113.0/24` par trois chemins :

```
Chemin 1 : AS-path = "200 300"      Local-Pref = 100    MED = 50
Chemin 2 : AS-path = "400"          Local-Pref = 80     MED = 10
Chemin 3 : AS-path = "200 500 300"  Local-Pref = 100    MED = 0
```

Quel chemin BGP sélectionne-t-il ? Justifie en détaillant l'algorithme étape par étape : *(12 pts)*

```
Étape 1 — Local-Pref (plus haut = préféré) :
  Chemin 1 : LocPrf = ___   Chemin 2 : LocPrf = ___   Chemin 3 : LocPrf = ___
  Éliminé : Chemin ___ (LocPrf trop basse)
  Restants : Chemin ___ et Chemin ___

Étape 2 — AS-path length (plus court = préféré) :
  Chemin 1 : longueur = ___   Chemin 3 : longueur = ___
  Éliminé : Chemin ___

CHEMIN GAGNANT : Chemin ___
Vérification MED : pas nécessaire car le gagnant est déjà identifié avant
Justification : _______________________________________________________________
```

**1.d** — Un administrateur veut que le trafic entrant dans son AS passe par son lien principal et non par le lien backup. Quel attribut BGP utilise-t-il et comment ? *(5 pts)*

```
Attribut à utiliser : ___________________________________________________________
Valeur sur le lien principal : ___   Valeur sur le lien backup : ___
Cet attribut est vu par : ☐ notre AS ☐ l'AS voisin directement connecté ☐ tous les AS
Règle : plus _______ = préféré
```

---

### 📊 Exercice 2 — Analyse de `show bgp summary` (/15)

> Sortie relevée sur le routeur de bordure R_Border (AS 64513) :

```
BGP router identifier 5.5.5.5, local AS number 64513
BGP table version is 89

Neighbor        V    AS     MsgRcvd  MsgSent  TblVer  InQ OutQ  Up/Down   State/PfxRcd
203.0.113.1     4  3215        8901     8897      89     0    0  2d03h34m        12450
198.51.100.2    4  5511        2341     2338      89     0    0  04:22:11          872
10.0.1.2        4 64513         441      438      89     0    0  01:11:05           48
172.16.5.5      4 64513           3        2       0     0    0  00:00:41       OpenSent
```

**2.a** — Pour chaque voisin, identifie le type de session (eBGP ou iBGP) et l'état : *(8 pts)*

| Voisin | Type (eBGP/iBGP) | État | Préfixes reçus |
|---|---|---|---|
| 203.0.113.1 | | | |
| 198.51.100.2 | | | |
| 10.0.1.2 | | | |
| 172.16.5.5 | | | |

**2.b** — Le voisin `172.16.5.5` est en état `OpenSent`. Que signifie cet état et quelle action peut-on faire pour diagnostiquer ? *(4 pts)*

```
OpenSent signifie : __________________________________________________________
Action de diagnostic : _______________________________________________________
```

**2.c** — Pourquoi le voisin `203.0.113.1` a-t-il un `Up/Down` de `2d03h34m` alors que `198.51.100.2` est à `04:22:11` ? Est-ce normal ? *(3 pts)*

```
Interprétation : _____________________________________________________________
En BGP, une session stable longtemps est : ☐ un problème ☐ souhaitable
Raison : ____________________________________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/50)

### ⌨️ Exercice 3 — Configuration BGP complète (/20)

> **Topologie** :
> ```
> Entreprise (AS 64512)  ──eBGP──  FAI_1 (AS 3215)  ──eBGP──  Internet
>                        ──eBGP──  FAI_2 (AS 5511)  ──eBGP──  Internet
> ```
> Lien R_Corp ↔ FAI_1 : 10.0.1.0/30 (R_Corp=.1, FAI_1=.2)
> Lien R_Corp ↔ FAI_2 : 10.0.2.0/30 (R_Corp=.1, FAI_2=.2)
> Loopback R_Corp : 192.168.99.99/32
> LAN entreprise : 192.168.10.0/24

**3.a** — Écris la configuration BGP complète de **R_Corp** : *(12 pts)*

```cisco
! R_Corp (AS 64512) — Configuration BGP complète

___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**3.b** — R_Corp doit préférer sortir par FAI_1 (lien principal). Écris la route-map et applique-la : *(8 pts)*

```cisco
! Appliquer Local-Pref 200 aux routes reçues de FAI_1
! Local-Pref 200 > défaut 100 → FAI_1 préféré pour la sortie

___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

---

### 📋 Exercice 4 — Lire la table BGP et déduire le chemin (/20)

> Table BGP de R_Corp après configuration :

```
R_Corp# show bgp ipv4 unicast

   Network            Next Hop     Metric  LocPrf  Weight  Path
*> 192.168.10.0/24    0.0.0.0           0           32768  i
*> 8.8.8.0/24         10.0.1.2          0     200       0  3215 15169 i
*  8.8.8.0/24         10.0.2.2          0     100       0  5511 15169 i
*  8.8.4.0/24         10.0.1.2         50     200       0  3215 15169 i
*> 8.8.4.0/24         10.0.2.2          0     100       0  5511 15169 i
*  1.1.1.0/24         10.0.1.2          0     200       0  3215 13335 i
*> 1.1.1.0/24         10.0.2.2          0     100       0  5511 13335 i
```

**4.a** — Pour chaque préfixe, identifie le chemin choisi par BGP (marqué >) et explique POURQUOI BGP a choisi ce chemin plutôt que l'autre : *(12 pts)*

| Préfixe | Chemin choisi (via) | Raison du choix |
|---|---|---|
| 8.8.8.0/24 | | |
| 8.8.4.0/24 | | |
| 1.1.1.0/24 | | |

**4.b** — Pour `8.8.4.0/24`, le chemin via FAI_1 a `LocPrf=200` mais est tout de même non choisi. Explique ce phénomène en t'appuyant sur les colonnes Metric et l'algorithme BGP : *(8 pts)*

```
Local-Pref via FAI_1 = _______   via FAI_2 = _______
À l'étape Local-Pref : les deux ont le même LocPrf ? ☐ Oui ☐ Non
→ Si oui, on passe à l'étape suivante : _______________________________________
MED via FAI_1 = _______   via FAI_2 = _______
L'étape MED s'applique-t-elle ici ? ☐ Oui, même AS voisin ☐ Non, AS différents
En réalité, l'étape qui différencie = ___________________________________________
Conclusion : ___________________________________________________________________
```

---

### 🔍 Exercice 5 — Comparatif final BGP vs OSPF (/10)

**5.a** — Complète le tableau comparatif : *(6 pts)*

| Critère | OSPF | BGP |
|---|---|---|
| Type | IGP (intra-AS) | |
| Découverte voisins | Automatique (Hello) | |
| Convergence | ~40 secondes | |
| Métriques | Coût (bande passante) | |
| Scalabilité | ~500 routeurs | |
| Politique de routage | Limitée | |

**5.b** — Donne un exemple concret où BGP est indispensable et OSPF insuffisant : *(4 pts)*

```
Scénario : ___________________________________________________________________
Pourquoi OSPF est insuffisant : _______________________________________________
Pourquoi BGP répond au besoin : _______________________________________________
```

---

## 🏅 Barème global

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Concepts BGP | S2.4 + S2.5 | /35 | ≥ 20 |
| Ex. 2 — show bgp summary | C2.3 | /15 | ≥ 8 |
| Ex. 3 — Configuration R_Corp | C2.2 | /20 | ≥ 11 |
| Ex. 4 — Lecture table BGP | S2.5 + C2.3 | /20 | ≥ 11 |
| Ex. 5 — BGP vs OSPF | S2.4 | /10 | ≥ 5 |
| **TOTAL** | | **/100** | **≥ 55** |

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** : OSPF est conçu pour un réseau interne unique (même entité) · Pas de notion d'AS ou de politique entre organisations · Pas scalable à l'échelle d'Internet (millions de routes, millions de routeurs)

**1.b** :

| Critère | iBGP |
|---|---|
| AS | Identiques |
| AS-path | Non modifié |
| Next-hop | Non modifié (problème courant) |
| Usage | Partage routes eBGP dans l'AS |
| Propagation | Split horizon iBGP (non re-propagé à d'autres iBGP) |
| Session | Via Loopback pour stabilité |

**1.c** :
- Étape 1 Local-Pref : Ch1=100, Ch2=80, Ch3=100 → Éliminé Ch2 (80 < 100)
- Étape 2 AS-path : Ch1="200 300"=2, Ch3="200 500 300"=3 → Éliminé Ch3
- GAGNANT : **Chemin 1** (LocPrf=100, AS-path=2 AS — le MED n'est pas évalué car un seul chemin reste)

**1.d** : **MED** · Lien principal : MED=10 · Lien backup : MED=100 · Vu par l'AS voisin directement connecté seulement · Plus bas = préféré

## Correction Exercice 2

**2.a** :

| Voisin | Type | État | Préfixes |
|---|---|---|---|
| 203.0.113.1 | eBGP (AS 3215 ≠ 64513) | Established ✓ | 12450 |
| 198.51.100.2 | eBGP (AS 5511 ≠ 64513) | Established ✓ | 872 |
| 10.0.1.2 | iBGP (AS 64513 = local) | Established ✓ | 48 |
| 172.16.5.5 | iBGP (AS 64513 = local) | OpenSent (problème) | — |

**2.b** : OpenSent = paquet BGP OPEN envoyé mais pas encore reçu de réponse · Diagnostic : `show ip bgp neighbors 172.16.5.5` + vérifier connectivité IP + vérifier remote-as

**2.c** : 2d03h = session stable depuis 2 jours → normal et souhaitable en BGP · BGP privilégie la stabilité sur Internet, les sessions restent actives très longtemps · Reconvergence lente = volontaire (éviter oscillations)

## Correction Exercice 3

```cisco
router bgp 64512
 bgp router-id 192.168.99.99
 neighbor 10.0.1.2 remote-as 3215
 neighbor 10.0.2.2 remote-as 5511
 network 192.168.10.0 mask 255.255.255.0

! Route-map Local-Pref pour FAI_1
route-map PREFER_FAI1 permit 10
 set local-preference 200
!
router bgp 64512
 neighbor 10.0.1.2 route-map PREFER_FAI1 in
```

## Correction Exercice 4

**4.a** :

| Préfixe | Chemin choisi | Raison |
|---|---|---|
| 8.8.8.0/24 | via FAI_1 (10.0.1.2) | LocPrf 200 > 100 |
| 8.8.4.0/24 | via FAI_2 (10.0.2.2) | LocPrf égal (200=200 non — voir 4b) |
| 1.1.1.0/24 | via FAI_2 (10.0.2.2) | LocPrf 200 mais MED 0 < 50 ← Attention |

**4.b** : Pour 8.8.4.0/24 — LocPrf FAI_1=200, FAI_2=100 DONC le chemin FAI_1 devrait gagner sauf si… on regarde la table : c'est FAI_2 qui est best malgré LocPrf plus faible. Cela indique que dans la table affichée la LocPrf est déjà égale (200 pour les deux — voir que la table montre bien LocPrf=200 pour FAI_1 ET LocPrf=100 pour FAI_2) → Normalement FAI_1 gagne. Si FAI_2 gagne c'est qu'il y a eu une autre manipulation. **Point pédagogique** : le MED 50 (FAI_1) vs 0 (FAI_2) n'intervient que si les deux voisins sont dans le MÊME AS (même neighbor AS) — ici FAI_1=AS3215 et FAI_2=AS5511 sont différents → le MED n'est pas comparé entre eux. L'ordre d'évaluation s'arrête donc à l'AS-path (égal 2 AS dans les deux cas). Le Router-ID départage.

## Correction Exercice 5

**5.b** : Scénario : entreprise avec deux FAI différents voulant contrôler la sortie préférée · OSPF insuffisant car ne comprend pas la notion d'AS ni les politiques inter-organisationnelles · BGP répond avec les attributs Local-Pref (sortie préférée) et MED (entrée suggérée)

---

*Devoir + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S3*
*Épreuve E31 | Compétences S2.4 · S2.5 · C2.2 · C2.3*
