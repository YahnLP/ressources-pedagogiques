# 📝 DEVOIR – S4 ANNÉE 2 – E31
## OSPF : Network Statements, DR/BDR, Adjacences, show ip ospf neighbor

**Nom : ________________  Prénom : ________________  Date : ________________**

---

## 📋 INFORMATIONS

| **Durée** | 45 minutes |
|---|---|
| **Documents autorisés** | Aucun |
| **Barème** | /20 points |

---

## PARTIE A – Connaissances OSPF (5 pts)

### A1 – Questions courtes (3 pts)

**a) *(0,5 pt)*** Quelle est la formule pour calculer un wildcard mask à partir d'un masque réseau ?

_________________________________________________________________________

**b) *(0,5 pt)*** Donnez le wildcard mask correspondant au préfixe /27.

_________________________________________________________________________

**c) *(0,5 pt)*** Que signifie configurer `ip ospf priority 0` sur une interface ? Quel est l'effet sur l'élection DR/BDR ?

_________________________________________________________________________
_________________________________________________________________________

**d) *(0,5 pt)*** Quelle est la différence entre l'état **Full** et l'état **2-Way** dans OSPF ? Lequel est l'état final normal entre deux DROthers ?

_________________________________________________________________________
_________________________________________________________________________

**e) *(0,5 pt)*** À quoi sert la commande `passive-interface` dans la configuration OSPF ? Donne un exemple de cas d'usage.

_________________________________________________________________________
_________________________________________________________________________

**f) *(0,5 pt)*** Quelle est l'adresse multicast utilisée par un DROther pour envoyer ses LSA au DR et BDR ?

_________________________________________________________________________

---

### A2 – Vrai ou Faux (2 pts)

| **Affirmation** | **V/F** | **Correction si fausse** |
|---|---|---|
| Le wildcard mask /26 est 0.0.0.192 | | |
| Un routeur avec priority=0 peut tout de même former une adjacence Full avec le DR | | |
| L'élection DR/BDR est préemptive : si un routeur avec une priorité plus élevée arrive, il devient DR immédiatement | | |
| Sur un lien point-à-point entre deux routeurs, il n'y a pas d'élection DR/BDR | | |

---

## PARTIE B – Lecture et analyse de `show ip ospf neighbor` (5 pts)

### Sortie collectée sur R-CORE d'une infrastructure d'entreprise

```
R-CORE# show ip ospf neighbor

Neighbor ID    Pri   State             Dead Time   Address         Interface
10.1.1.1         1   FULL/DR           00:00:37    172.16.0.1      Gi0/0
10.1.1.2         1   FULL/BDR          00:00:34    172.16.0.2      Gi0/0
10.1.1.3         1   2WAY/DROTHER      00:00:38    172.16.0.3      Gi0/0
10.1.1.4         0   FULL/DROTHER      00:00:32    172.16.0.4      Gi0/0
20.1.1.1         1   FULL/ -           00:00:35    192.168.10.1    Gi0/1
```

**B1 *(1 pt)* :** Quel est le Router-ID de R-CORE ? Comment en êtes-vous sûr sans voir `show ip ospf` ?

_________________________________________________________________________
_________________________________________________________________________

**B2 *(0,5 pt)* :** Combien de réseaux différents R-CORE est-il connecté via OSPF ?

_________________________________________________________________________

**B3 *(1 pt)* :** Sur l'interface Gi0/0, qui est le DR ? Qui est le BDR ? Justifiez pourquoi 10.1.1.1 est DR et non 10.1.1.4 (dont la priorité est 0).

_________________________________________________________________________
_________________________________________________________________________

**B4 *(0,5 pt)* :** Que signifie l'état `FULL/ -` pour le voisin 20.1.1.1 sur Gi0/1 ? Quel type de lien relie R-CORE à ce voisin ?

_________________________________________________________________________

**B5 *(1 pt)* :** Le Dead Time de 10.1.1.2 arrive à 0 s. Décrivez ce qui se passe (en 3 étapes) :

1. _______________________________________________________________________
2. _______________________________________________________________________
3. _______________________________________________________________________

**B6 *(1 pt)* :** Quelle est la différence entre l'état `2WAY/DROTHER` de 10.1.1.3 et l'état `FULL/DROTHER` de 10.1.1.4 ? Y a-t-il un problème ? Justifiez.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

## PARTIE C – Calcul et configuration (5 pts)

### C1 – Network statements (3 pts)

> Un routeur R-BRANCH a les interfaces suivantes :

| **Interface** | **Adresse IP** | **Masque** | **Rôle** |
|---|---|---|---|
| Gi0/0 | 10.50.1.1 | /27 | LAN utilisateurs (passerelle) |
| Gi0/1 | 10.50.0.1 | /30 | Liaison vers R-CORE |
| Gi0/2 | 10.50.0.5 | /30 | Liaison vers R-BACKUP |

**C1.a *(0,5 pt)* :** Calculez les wildcards pour les trois réseaux :

| **Réseau** | **Masque** | **Wildcard** |
|---|---|---|
| 10.50.1.0 | /27 | |
| 10.50.0.0 | /30 | |
| 10.50.0.4 | /30 | |

**C1.b *(2 pts)* :** Écrivez la configuration OSPF complète de R-BRANCH (router-id = 5.5.5.5, area 0, interface LAN passive) :

```ios
R-BRANCH(config)# router ospf _____
R-BRANCH(config-router)# router-id _____________________
R-BRANCH(config-router)# network _____________ _____________ area ___
R-BRANCH(config-router)# network _____________ _____________ area ___
R-BRANCH(config-router)# network _____________ _____________ area ___
R-BRANCH(config-router)# passive-interface _____________________
```

**C1.c *(0,5 pt)* :** Pourquoi est-il important de rendre Gi0/0 passive ?

_________________________________________________________________________

---

### C2 – Élection DR/BDR (2 pts)

> Quatre routeurs sont connectés au même segment LAN (172.16.1.0/24). Leurs paramètres sont :

| **Routeur** | **Router-ID** | **ip ospf priority (Gi0/0)** |
|---|---|---|
| Ra | 10.10.10.10 | 1 |
| Rb | 192.168.1.1 | 50 |
| Rc | 172.16.5.5 | 50 |
| Rd | 10.0.0.1 | 0 |

**C2.a *(1 pt)* :** Quel routeur sera élu **DR** ? Quel routeur sera élu **BDR** ? Justifiez précisément.

```
DR  = _______ car _________________________________________________
BDR = _______ car _________________________________________________
```

**C2.b *(0,5 pt)* :** Rd peut-il être élu DR ou BDR dans cette situation ? Pourquoi ?

_________________________________________________________________________

**C2.c *(0,5 pt)* :** L'admin veut forcer Ra comme DR. Quelle commande doit-il saisir sur Ra, et quelle action supplémentaire est nécessaire pour que le changement prenne effet ?

```ios
Ra(config-if)# _____________________________________________________
```
Action supplémentaire : _____________________________________________

---

## PARTIE D – Cas professionnel (5 pts)

### Mise en situation

> *Vous êtes technicien réseau dans une entreprise industrielle. Un collègue a configuré OSPF sur 3 routeurs pour relier 3 ateliers. Il vous appelle : "Ça ne marche pas, les routeurs ne se voient pas." Vous accédez à R-ATELIER2 à distance.*

**Sortie `show ip ospf neighbor` sur R-ATELIER2 :**

```
R-ATELIER2# show ip ospf neighbor
[Aucune sortie — liste vide]
```

**Sortie `show ip ospf` sur R-ATELIER2 :**

```
R-ATELIER2# show ip ospf
 Routing Process "ospf 1" with ID 192.168.2.1
 ...
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
   Area BACKBONE(0)
       Number of interfaces in this area is 1
       Area has no authentication
```

**Sortie `show ip ospf interface Gi0/0` sur R-ATELIER2 :**

```
GigabitEthernet0/0 is up, line protocol is up
  Internet Address 10.1.0.2/30, Area 0
  Process ID 1, Router ID 192.168.2.1, Network Type POINT_TO_POINT, Cost: 1
  Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
  Neighbor Count is 0, Adjacent neighbor count is 0
```

**Sortie `show ip ospf interface Gi0/1` sur R-ATELIER2 :**

```
GigabitEthernet0/1 is up, line protocol is up
  Internet Address 192.168.2.1/24, Area 0
  Process ID 1, Router ID 192.168.2.1, Network Type BROADCAST, Cost: 1
  Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
  Neighbor Count is 0, Adjacent neighbor count is 0
```

**Configuration OSPF de R-ATELIER1 (fournie pour comparaison) :**

```ios
router ospf 1
 router-id 192.168.1.1
 network 10.1.0.0 0.0.0.3 area 0
 network 192.168.1.0 0.0.0.255 area 0
```

**Configuration OSPF de R-ATELIER2 (à analyser) :**

```ios
router ospf 1
 router-id 192.168.2.1
 network 192.168.2.0 0.0.0.255 area 0
 passive-interface GigabitEthernet0/0
```

---

**D1 *(2 pts)* :** Identifiez **les deux erreurs** dans la configuration de R-ATELIER2. Pour chacune, expliquez précisément pourquoi c'est une erreur et quel est l'impact sur OSPF.

**Erreur 1 :**

_________________________________________________________________________
_________________________________________________________________________

**Erreur 2 :**

_________________________________________________________________________
_________________________________________________________________________

---

**D2 *(2 pts)* :** Écrivez la configuration OSPF **corrigée** complète de R-ATELIER2 :

```ios
R-ATELIER2(config)# router ospf _____
R-ATELIER2(config-router)# router-id _____________________
R-ATELIER2(config-router)# _________________________________________
R-ATELIER2(config-router)# _________________________________________
R-ATELIER2(config-router)# _________________________________________
```

---

**D3 *(1 pt)* :** Après correction, la liaison entre R-ATELIER1 et R-ATELIER2 est un /30 (réseau 10.1.0.0/30). Quel état d'adjacence attendez-vous dans `show ip ospf neighbor` sur ce lien ? Pourquoi n'y a-t-il pas d'élection DR/BDR sur ce type de liaison ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME RÉCAPITULATIF

| **Partie** | **Thème** | **Points** | **Note** |
|---|---|---|---|
| A1 | Questions courtes OSPF | /3 | |
| A2 | Vrai / Faux | /2 | |
| B1 à B6 | Lecture show ip ospf neighbor | /5 | |
| C1 | Network statements + wildcard | /3 | |
| C2 | Élection DR/BDR | /2 | |
| D1 | Identifier les 2 erreurs | /2 | |
| D2 | Configuration corrigée | /2 | |
| D3 | Type de lien et état adjacence | /1 | |
| **TOTAL** | | **/20** | |

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
