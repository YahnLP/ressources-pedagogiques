# 🔍 ACTIVITÉ DE DÉCOUVERTE — S13 · 2ᵉ ANNÉE · E31
## « Le mystère des ports bloqués » — Diagnostiquer EtherChannel sans cours préalable

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement
> **Principe** : On te présente des sorties de commandes Cisco IOS. Tu dois comprendre ce qui fonctionne, ce qui ne fonctionne pas, et pourquoi — sans avoir vu le cours.

---

## 🎯 Mise en situation

> Tu es **technicien réseau** dans un datacenter.
> Le réseau entre les deux switches principaux (SW1 et SW2) est censé utiliser **4 câbles** pour maximiser la bande passante.
> Mais les utilisateurs se plaignent de lenteurs. Un collègue a laissé ces sorties de commandes.
> **Ta mission** : comprendre l'état actuel et identifier les problèmes.

---

## 🗺️ Topologie déclarée

```
  ┌──────────┐  Gi0/1 ════ Gi0/1  ┌──────────┐
  │          │  Gi0/2 ════ Gi0/2  │          │
  │   SW1    │  Gi0/3 ════ Gi0/3  │   SW2    │
  │          │  Gi0/4 ════ Gi0/4  │          │
  └──────────┘                    └──────────┘
  4 liens physiques déclarés entre SW1 et SW2
  Objectif : 4 Gbps agrégés + redondance
```

---

## 📋 Sorties de commandes — SW1

### `SW1# show etherchannel summary`

```
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in-use      M - not in use, minimum links not met
        u - unsuitable for bundling

Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------
1      Po1(SU)         LACP      Gi0/1(P)   Gi0/2(P)
                                 Gi0/3(D)   Gi0/4(I)
```

### `SW1# show interfaces Po1 status`

```
Port      Name     Status       Vlan  Duplex Speed Type
Po1                connected    1     a-full  a-2G  -
```

### `SW1# show interfaces Gi0/3`

```
GigabitEthernet0/3 is down, line protocol is down (notconnect)
```

### `SW1# show interfaces Gi0/4`

```
GigabitEthernet0/4 is up, line protocol is up
  Hardware is iGbE, address is aabb.cc00.0014
  Full-duplex, 100Mb/s
```

---

## 📋 Sorties de commandes — SW2

### `SW2# show etherchannel summary`

```
Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------
1      Po1(SU)         LACP      Gi0/1(P)   Gi0/2(P)
                                 Gi0/3(D)   Gi0/4(I)
```

### `SW2# show interfaces Gi0/4`

```
GigabitEthernet0/4 is up, line protocol is up
  Hardware is iGbE, address is aabb.cc00.0024
  Full-duplex, Auto-speed, 1000Mb/s
```

---

## 🔍 PARTIE 1 — Décoder les états (10 min)

**Question 1.1** — Dans la sortie de `show etherchannel summary`, 4 codes apparaissent dans la colonne Ports : `P`, `D`, `I`. Que signifie chacun selon toi ?

```
(P) → ________________________________________________________________________
(D) → ________________________________________________________________________
(I) → ________________________________________________________________________
```

**Question 1.2** — Combien de ports sont actuellement ACTIFS dans le port-channel Po1 ?

```
Ports actifs (code P) : Gi_____ et Gi_____
Bande passante actuelle : _______ Gbps (sur les _______ Gbps théoriques)
```

**Question 1.3** — Le port-channel est noté `Po1(SU)`. Que signifient les lettres S et U ?

```
S → ________________________________________________________________________
U → ________________________________________________________________________
```

---

## 🔍 PARTIE 2 — Identifier les problèmes (15 min)

**Problème 1 — Interface Gi0/3 (code D)**

**Question 2.1** — `show interfaces Gi0/3` indique `down, line protocol is down (notconnect)`.
Quelle est la cause probable ? Que faut-il vérifier en premier ?

```
Cause probable : _______________________________________________________________
Première vérification physique : ______________________________________________
Commande IOS à taper ensuite : ________________________________________________
```

---

**Problème 2 — Interface Gi0/4 (code I = stand-alone)**

**Question 2.2** — Compare les deux sorties de `show interfaces Gi0/4` entre SW1 et SW2 :

```
SW1 Gi0/4 : ________ Mb/s, Full-duplex
SW2 Gi0/4 : ________ Mb/s, Full-duplex, Auto

Les vitesses sont-elles identiques ? ☐ Oui ☐ Non
```

**Question 2.3** — Gi0/4 est UP des deux côtés et le câble fonctionne. Pourtant ce port est en mode `I` (stand-alone = pas dans le port-channel). Quelle est l'explication la plus probable ?

```
☐ Le câble est défectueux
☐ Les vitesses des deux interfaces ne correspondent pas
☐ Le VLAN est différent
☐ LACP n'est pas activé

Justification depuis les sorties de commandes : ________________________________
______________________________________________________________________________
```

**Question 2.4** — Un port EtherChannel doit respecter des conditions pour être accepté dans le bundle. En déduisant depuis ce que tu observes, cite les conditions :

```
Condition 1 : _________________________________________________________________
Condition 2 : _________________________________________________________________
Condition 3 (déduite de la Panne 2) : ________________________________________
```

---

## 🔍 PARTIE 3 — Proposer les corrections (10 min)

**Question 3.1** — Pour corriger le problème de Gi0/3 (câble déconnecté — supposons qu'on ne peut pas intervenir physiquement), que peut-on faire pour les 4 Gbps prévus ?

```
Action possible sans intervention physique : ___________________________________
Bande passante maximale atteignable avec 2 ports actifs : _______ Gbps
```

**Question 3.2** — Pour corriger Gi0/4 sur SW1 (forcé à 100 Mbps), quelle commande IOS taper ? Où la taper ?

```
SW1(config)# interface GigabitEthernet0/4
SW1(config-if)# _______________________________________________________________
                ← que faut-il changer pour que ce port rejoigne le port-channel ?
```

**Question 3.3** — Après correction de Gi0/4, à quoi ressemblerait le `show etherchannel summary` idéal ?

```
Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------
1      Po1(SU)         LACP      Gi0/1(___)   Gi0/2(___)
                                 Gi0/3(___)   Gi0/4(___)
                                         ↑
                     Quel code voudrait-on voir sur tous les ports ?
```

---

## 🏁 Bilan

```
EtherChannel permet de :
1. _______________________________________________________________ (bande passante)
2. _______________________________________________________________ (redondance)
3. _______________________________________________________________ (vs STP)

Pour qu'un port rejoigne un port-channel, il faut :
→ ____________________________________
→ ____________________________________
→ ____________________________________

La commande de vérification essentielle est : ________________________________
```

> ✅ Tu viens d'analyser une vraie sortie `show etherchannel summary` et d'identifier
> des pannes réelles sans avoir vu le cours. Le cours va maintenant te donner
> les commandes pour configurer et corriger tout ça.

---

## 📎 Pour l'enseignant — Réponses

**1.1** : P = bundled/actif dans le port-channel · D = down (interface physique DOWN) · I = stand-alone (interface UP mais pas dans le bundle — incompatibilité)

**2.3** : Les vitesses ne correspondent pas : SW1 Gi0/4 est forcé à 100 Mbps, SW2 est en auto-1000 Mbps → LACP rejette ce port car un membre doit avoir la même vitesse que les autres (1 Gbps)

**3.2** : `speed auto` ou `no speed 100` pour revenir à l'auto-négociation 1 Gbps

**3.3** : Tous les ports devraient avoir le code **(P)** — bundled and active

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S13*
*Compétences : S2.1 · C2.3*
