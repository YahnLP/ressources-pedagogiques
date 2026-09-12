# 🔬 TRAVAUX PRATIQUES — S3 · 3ᵉ ANNÉE · E31
## BGP eBGP : Configuration 3 AS · Attributs · Table BGP · Sélection du chemin

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Packet Tracer**
> **Fichier .pkt** : `S3_E31_BGP_3AS.pkt` (fourni par l'enseignant)
> **Épreuve ciblée** : **E31** – Épreuve pratique infrastructure réseau

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S2.4** | Configurer eBGP entre 3 AS |
| **S2.5** | Observer et manipuler les attributs AS-path et Local-Pref |
| **C2.2** | Appliquer les commandes IOS BGP |
| **C2.3** | Interpréter `show bgp summary` et `show bgp ipv4 unicast` |

---

## 🗺️ Topologie du TP

```
        AS 100                    AS 200                    AS 300
   ┌──────────────┐         ┌──────────────┐         ┌──────────────┐
   │     R1       │         │     R2       │         │     R3       │
   │ Lo: 1.1.1.1  │─ eBGP ─│ Lo: 2.2.2.2  │─ eBGP ─│ Lo: 3.3.3.3  │
   │ Gi0/0: LAN-A │         │              │         │ Gi0/1: LAN-C │
   │ Gi0/1: WAN   │         │ Gi0/0: WAN12 │         │ Gi0/0: WAN23 │
   └──────────────┘         │ Gi0/1: WAN23 │         └──────────────┘
   LAN-A: 192.168.1.0/24    └──────────────┘         LAN-C: 192.168.3.0/24
   PC_A: 192.168.1.10       R2 = AS de transit (pas de LAN propre)

Plan d'adressage :
  R1 Gi0/0  : 192.168.1.1/24      R1 Gi0/1 : 10.0.12.1/30
  R2 Gi0/0  : 10.0.12.2/30        R2 Gi0/1 : 10.0.23.1/30
  R3 Gi0/0  : 10.0.23.2/30        R3 Gi0/1 : 192.168.3.1/24
  PC_A: 192.168.1.10/24 GW:.1     PC_C: 192.168.3.10/24 GW:.1
```

---

## 🟢 NIVEAU 1 — Préparer l'infrastructure et comprendre le contexte (10 min)

**1.1** — Vérifie la connectivité des liens WAN directs entre routeurs :

```cisco
R1# ping 10.0.12.2
R2# ping 10.0.23.2
```

```
R1 → R2 (10.0.12.2) : ☐ Succès ☐ Échec
R2 → R3 (10.0.23.2) : ☐ Succès ☐ Échec
```

**1.2** — Avant toute config BGP, R1 peut-il pinguer le LAN de R3 (192.168.3.0) ?

```cisco
R1# ping 192.168.3.10
```

```
Résultat : ☐ Succès ☐ Échec — car ___________________________________________
```

**1.3** — Pourquoi ne configure-t-on PAS OSPF entre R1, R2 et R3 dans ce TP ?

```
Chaque routeur est dans un AS _______ (différent / identique)
OSPF est un protocole : ☐ IGP (intra-AS) ☐ EGP (inter-AS)
BGP est prévu pour : ___________________________________________________
```

---

## 🟡 NIVEAU 2 — Configurer eBGP sur les 3 routeurs (25 min)

### Sur R1 (AS 100)

**2.1** — Configure BGP sur R1 :

```cisco
R1(config)# router bgp 100
R1(config-router)# bgp router-id _______________
R1(config-router)# neighbor 10.0.12.2 remote-as _______________
R1(config-router)# network 192.168.1.0 mask _______________
```

### Sur R2 (AS 200) — routeur de transit

**2.2** — R2 n'a pas de LAN propre mais relaie les routes entre AS 100 et AS 300 :

```cisco
R2(config)# router bgp ___
R2(config-router)# bgp router-id 2.2.2.2
R2(config-router)# neighbor _______________ remote-as 100   ← vers R1
R2(config-router)# neighbor _______________ remote-as 300   ← vers R3
```

### Sur R3 (AS 300)

**2.3** — Configure R3 symétriquement :

```cisco
R3(config)# router bgp _______________
R3(config-router)# bgp router-id _______________
R3(config-router)# neighbor _______________ remote-as _______________
R3(config-router)# network 192.168.3.0 mask 255.255.255.0
```

### Vérification des sessions

**2.4** — Sur R2 (point central), vérifie les sessions BGP :

```cisco
R2# show bgp summary
```

```
Recopie la sortie :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**2.5** — Analyse la sortie :

```
Voisin R1 (10.0.12.1) : AS = ___  State/PfxRcd = ___  Session : ☐ OK ☐ KO
Voisin R3 (10.0.23.2) : AS = ___  State/PfxRcd = ___  Session : ☐ OK ☐ KO
```

**2.6** — Attends ~30 secondes puis reteste. Si un voisin est encore en "Active" :

```
Vérifier la config remote-as de l'autre côté :
  R1# show run | include remote-as → ___________________________________
  R2# show run | include remote-as → ___________________________________
Cause la plus fréquente : ________________________________________________
```

---

## 🟠 NIVEAU 3 — Observer la table BGP et l'AS-path (20 min)

**3.1** — Sur R1, affiche la table BGP complète :

```cisco
R1# show bgp ipv4 unicast
```

```
Recopie les lignes de routes apprises :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**3.2** — R1 voit-il le réseau de R3 (192.168.3.0/24) ?

```
Route 192.168.3.0/24 présente ? ☐ Oui ☐ Non
Next-hop = _______________   AS-path = _______________
```

**3.3** — Analyse l'AS-path de la route vers 192.168.3.0/24 vue depuis R1 :

```
AS-path = "___  ___"
Cela signifie : le préfixe a traversé AS ___ (R2) puis vient d'AS ___ (R3)
Nombre d'AS traversés : ___
R1 vérifie que son propre AS (100) n'est pas dans le path → ☐ Boucle ☐ Pas de boucle
```

**3.4** — Sur R3, l'AS-path de 192.168.1.0/24 (LAN de R1) est-il différent ?

```cisco
R3# show bgp ipv4 unicast 192.168.1.0
```

```
AS-path vu par R3 = "___  ___"
Différence avec la vue de R1 : _______________________________________________
Règle : l'AS-path est toujours lu depuis la _____________ vers la source
```

**3.5** — Teste la connectivité end-to-end :

```
ping 192.168.3.10 depuis PC_A → ☐ Succès ☐ Échec
ping 192.168.1.10 depuis PC_C → ☐ Succès ☐ Échec
```

---

## 🔵 NIVEAU 4 — Manipuler Local-Pref pour forcer un chemin (15 min)

> **Scénario** : On ajoute un second lien entre R1 et R3 directement (AS 100 → AS 300).
> R1 peut maintenant atteindre 192.168.3.0/24 par deux chemins :
>   - Via R2 (AS 200) : AS-path = "200 300" (2 AS)
>   - Via le lien direct R1-R3 : AS-path = "300" (1 AS)
>
> Sans manipulation d'attributs, BGP choisirait le chemin direct (AS-path plus court).
> **Mission** : Forcer BGP à préférer le chemin via R2 malgré l'AS-path plus long.

**4.1** — Sur R1, applique un Local-Pref de 200 aux routes reçues via R2 (chemin à favoriser) :

```cisco
R1(config)# ip prefix-list VIA_R2 permit 192.168.3.0/24
R1(config)# route-map PREFER_R2 permit 10
R1(config-route-map)# match ip address prefix-list VIA_R2
R1(config-route-map)# set local-preference 200
R1(config-route-map)# exit
R1(config)# router bgp 100
R1(config-router)# neighbor 10.0.12.2 route-map PREFER_R2 in
R1(config-router)# end
R1# clear ip bgp * soft
```

**4.2** — Vérifie la table BGP de R1 après la modification :

```cisco
R1# show bgp ipv4 unicast 192.168.3.0
```

```
Chemin via R2 : LocPrf = ___  AS-path = ___________  Marqué > (best) ? ☐ Oui ☐ Non
Chemin direct : LocPrf = ___  AS-path = ___________  Marqué > (best) ? ☐ Oui ☐ Non

BGP a choisi le chemin via R2 malgré l'AS-path plus long ? ☐ Oui ☐ Non
Raison : Local-Pref ____ > ____ → Local-Pref est évalué AVANT l'AS-path dans l'algorithme
```

---

## 🔴 NIVEAU 5 — Diagnostiquer un problème de session BGP (10 min)

> L'enseignant a injecté une panne dans le fichier `.pkt` de dépannage.
> (Ouvrir `S3_E31_BGP_PANNES.pkt`)

**5.1** — Sur R2, `show bgp summary` montre R1 en état "Active" depuis longtemps. Diagnostique :

```cisco
R2# show bgp summary
R2# show run | section bgp
```

```
Remote-AS configuré sur R2 pour R1 : _______
Remote-AS configuré sur R1 pour R2 : _______
Correspondent-ils ? ☐ Oui ☐ Non
Panne identifiée : ___________________________________________________________
```

**5.2** — Correction :

```cisco
R___(config)# router bgp ___
R___(config-router)# neighbor _______________ remote-as _______________
```

**5.3** — Après correction, R2 affiche "Active" pour R3 maintenant. Regarder la connectivité IP :

```cisco
R2# ping 10.0.23.2
```

```
Résultat : ☐ Succès ☐ Échec
Si échec : vérifier _______________________________________________________
Commande de vérification : _________________________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Configurer eBGP (router bgp + neighbor + network) | ☐ | ☐ | ☐ |
| Lire `show bgp summary` et interpréter les états | ☐ | ☐ | ☐ |
| Identifier l'AS-path dans `show bgp ipv4 unicast` | ☐ | ☐ | ☐ |
| Expliquer pourquoi AS-path plus court = préféré | ☐ | ☐ | ☐ |
| Appliquer Local-Pref via route-map pour forcer un chemin | ☐ | ☐ | ☐ |
| Diagnostiquer une session BGP en état "Active" | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.2 — Sessions eBGP Established sur les 3 routeurs | /7 |
| Niv.3 — Table BGP lue et AS-path interprété correctement | /8 |
| Niv.3 — Ping E2E PC_A → PC_C | /3 |
| Niv.4 — Local-Pref appliqué, best path forcé | /4 |
| Niv.5 — Panne diagnostiquée et corrigée | /3 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 2

```cisco
! R1
router bgp 100
 bgp router-id 1.1.1.1
 neighbor 10.0.12.2 remote-as 200
 network 192.168.1.0 mask 255.255.255.0

! R2
router bgp 200
 bgp router-id 2.2.2.2
 neighbor 10.0.12.1 remote-as 100
 neighbor 10.0.23.2 remote-as 300

! R3
router bgp 300
 bgp router-id 3.3.3.3
 neighbor 10.0.23.1 remote-as 200
 network 192.168.3.0 mask 255.255.255.0
```

## Correction Niveau 3

```
Sur R1 : show bgp ipv4 unicast
*> 192.168.1.0/24  0.0.0.0       32768 i          ← réseau local
*> 192.168.3.0/24  10.0.12.2   0   200 300 i      ← via R2 puis R3

AS-path "200 300" : R2 (AS200) est le prochain saut, R3 (AS300) est l'origine
Sur R3 : AS-path de 192.168.1.0/24 = "200 100" (R2 puis R1)
Règle : lire l'AS-path de gauche (plus proche) à droite (origine)
```

## Correction Niveau 4

```
Avec Local-Pref 200 sur le chemin via R2 :
  Chemin via R2 : LocPrf=200 AS-path="200 300" → BEST (LocPrf 200 > 100)
  Chemin direct : LocPrf=100 AS-path="300"     → non best
BGP préfère LocPrf=200 car Local-Pref est évalué AVANT AS-path dans l'algorithme
```

## Correction Niveau 5

```
Panne typique : remote-as incorrect
  R2 a : neighbor 10.0.12.1 remote-as 100  ← correct
  R1 a : neighbor 10.0.12.2 remote-as 300  ← FAUX (devrait être 200)
→ Les deux côtés doivent déclarer l'AS DE L'AUTRE comme remote-as
Fix : R1(config-router)# neighbor 10.0.12.2 remote-as 200

Panne R2-R3 : vérifier connectivité IP d'abord (ping 10.0.23.2)
  Si ping KO → problème L1/L2/L3 sur le lien WAN avant même BGP
```

---

*TP BGP + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S3*
*Document Portfolio E31 — Compétences S2.4 · S2.5 · C2.2 · C2.3*
