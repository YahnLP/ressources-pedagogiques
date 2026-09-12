# 🔬 TP PACKET TRACER – S4 ANNÉE 2 – E31
## OSPF : Network Statements, DR/BDR, Adjacences — Topologie 4 Routeurs

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Configurer OSPF complet (network statements + wildcard) sur une topologie 4 routeurs
- ✅ Observer et analyser l'élection DR/BDR sur un segment LAN partagé
- ✅ Lire et interpréter `show ip ospf neighbor` en détail
- ✅ Manipuler `ip ospf priority` et observer l'impact
- ✅ Diagnostiquer une adjacence bloquée et la corriger

---

## ⏱️ DURÉE : 70 min

---

## 📋 TOPOLOGIE

```
                    ┌──────────────────────────────────────┐
                    │           LAN OSPF                   │
                    │         10.0.0.0/24                  │
                    │  Switch central (192.168.100.x)      │
                    └──┬──────────┬──────────┬──────────┬──┘
                       │          │          │          │
                   [R1]Gi0/1  [R2]Gi0/1  [R3]Gi0/1  [R4]Gi0/1
                   10.0.0.1  10.0.0.2  10.0.0.3   10.0.0.4
                   R-ID:      R-ID:      R-ID:      R-ID:
                   1.1.1.1    2.2.2.2    3.3.3.3    4.4.4.4

                   [R1]Gi0/0       [R3]Gi0/0       [R4]Gi0/0
                   192.168.1.1/24  192.168.3.1/24  192.168.4.1/24
                       │               │               │
                   [LAN-A]         [LAN-C]         [LAN-D]
               192.168.1.0/24  192.168.3.0/24  192.168.4.0/24
```

---

## 📋 PLAN D'ADRESSAGE COMPLET

| **Équipement** | **Interface** | **Adresse IP** | **Masque** | **Rôle** |
|---|---|---|---|---|
| R1 | Gi0/0 | 192.168.1.1 | /24 | Passerelle LAN-A |
| R1 | Gi0/1 | 10.0.0.1 | /24 | LAN OSPF partagé |
| R2 | Gi0/1 | 10.0.0.2 | /24 | LAN OSPF partagé |
| R3 | Gi0/0 | 192.168.3.1 | /24 | Passerelle LAN-C |
| R3 | Gi0/1 | 10.0.0.3 | /24 | LAN OSPF partagé |
| R4 | Gi0/0 | 192.168.4.1 | /24 | Passerelle LAN-D |
| R4 | Gi0/1 | 10.0.0.4 | /24 | LAN OSPF partagé |
| PC-A | — | 192.168.1.10 | /24 | GW 192.168.1.1 |
| PC-C | — | 192.168.3.10 | /24 | GW 192.168.3.1 |
| PC-D | — | 192.168.4.10 | /24 | GW 192.168.4.1 |

> **Router-IDs :** R1=1.1.1.1 ; R2=2.2.2.2 ; R3=3.3.3.3 ; R4=4.4.4.4 (tous configurés manuellement)

---

## ⚠️ CONSIGNES

> - Construire ou charger la topologie dans Cisco Packet Tracer
> - Configurer les IP des interfaces **avant** OSPF
> - Tester chaque étape avec les commandes `show` indiquées
> - **Ne pas modifier les priorités avant la Partie 2** — laisser la valeur par défaut (1)

---

## 🧪 PARTIE 1 – Configuration OSPF de base (20 min)

### 1.1 – Calcul des wildcards (avant de configurer)

> Calculez les wildcards nécessaires :

| **Réseau** | **Masque** | **Wildcard (255.255.255.255 − masque)** |
|---|---|---|
| 192.168.1.0 | 255.255.255.0 | |
| 192.168.3.0 | 255.255.255.0 | |
| 192.168.4.0 | 255.255.255.0 | |
| 10.0.0.0 | 255.255.255.0 | |

---

### 1.2 – Configuration des routeurs

**Sur R1 :**

```ios
R1(config)# router ospf 1
R1(config-router)# router-id _____________
R1(config-router)# network _____________ _____________ area 0
R1(config-router)# network _____________ _____________ area 0
R1(config-router)# passive-interface _____________
```

*Indication : R1 doit annoncer son LAN (192.168.1.0/24) et sa liaison OSPF (10.0.0.0/24). Son interface vers LAN-A doit être passive.*

---

**Sur R2 :**

```ios
R2(config)# router ospf 1
R2(config-router)# router-id _____________
R2(config-router)# network _____________ _____________ area 0
```

*Indication : R2 n'a qu'une interface dans ce TP — la liaison OSPF.*

---

**Sur R3 :**

```ios
R3(config)# router ospf 1
R3(config-router)# router-id _____________
R3(config-router)# network _____________ _____________ area 0
R3(config-router)# network _____________ _____________ area 0
R3(config-router)# passive-interface _____________
```

---

**Sur R4 :**

```ios
R4(config)# router ospf 1
R4(config-router)# router-id _____________
R4(config-router)# network _____________ _____________ area 0
R4(config-router)# network _____________ _____________ area 0
R4(config-router)# passive-interface _____________
```

---

### 1.3 – Vérification initiale

**Après configuration des 4 routeurs, relevez sur R1 :**

```ios
R1# show ip ospf neighbor
```

**Copiez ou dessinez la sortie ici :**

```
Neighbor ID    Pri  State       Dead Time  Address    Interface
____________   ___  ________    _________  _________  ________
____________   ___  ________    _________  _________  ________
____________   ___  ________    _________  _________  ________
```

**Q1.** Combien de voisins R1 voit-il ? ___________

**Q2.** Quel état indique une adjacence complète ? ___________

**Q3.** Qui est le DR sur le segment 10.0.0.0/24 ? (regarder la colonne State) ___________

**Q4.** Qui est le BDR ? ___________

**Q5.** Pourquoi ce routeur est-il devenu DR ? (justifiez avec les router-id) :

_________________________________________________________________________

---

### 1.4 – Test de connectivité

```
PC-A# ping 192.168.3.10   → résultat : _______
PC-A# ping 192.168.4.10   → résultat : _______
PC-C# ping 192.168.4.10   → résultat : _______
```

---

## 🔬 PARTIE 2 – Manipulation de l'élection DR/BDR (20 min)

### 2.1 – Observation de l'état actuel

```ios
R1# show ip ospf interface Gi0/1
```

**Relevez :**

- Network Type : ___________
- DR : ___________ (adresse IP et router-id)
- BDR : ___________ (adresse IP et router-id)
- Priorité de R1 sur Gi0/1 : ___________

---

### 2.2 – Forcer R1 comme DR

**Objectif :** Configurer R1 avec la priorité la plus haute pour qu'il soit élu DR.

```ios
R1(config)# interface GigabitEthernet0/1
R1(config-if)# ip ospf priority 200
```

Puis forcer la re-élection sur **TOUS** les routeurs :

```ios
R1# clear ip ospf process       → yes
R2# clear ip ospf process       → yes
R3# clear ip ospf process       → yes
R4# clear ip ospf process       → yes
```

> ⚠️ Attendre 30–60 secondes que les adjacences se rétablissent.

**Après re-convergence, vérifiez sur R1 :**

```ios
R1# show ip ospf neighbor
R1# show ip ospf interface Gi0/1
```

**Q6.** R1 est-il maintenant DR ? Justifiez :

_________________________________________________________________________

**Q7.** Qui est devenu BDR ? Pourquoi (critère de sélection utilisé) ?

_________________________________________________________________________

---

### 2.3 – Exclure R2 de l'élection

**Objectif :** R2 ne doit jamais être DR ni BDR.

```ios
R2(config)# interface GigabitEthernet0/1
R2(config-if)# ip ospf priority 0
```

Puis `clear ip ospf process` sur tous.

**Q8.** Après re-convergence, quel état affiche R2 dans `show ip ospf neighbor` sur R1 ?

_________________________________________________________________________

**Q9.** Quelle est la priorité de R2 visible dans `show ip ospf neighbor` ?

_________________________________________________________________________

---

### 2.4 – Observation des multicast OSPF (optionnel si temps disponible)

```ios
R1# debug ip ospf hello
! Observer les messages hello envoyés vers 224.0.0.5
R1# undebug all
```

**Notez l'adresse multicast destination observée :**

_________________________________________________________________________

---

## 🛠️ PARTIE 3 – Débogage d'adjacences (15 min)

### Mise en situation

> Le formateur introduit volontairement une erreur de configuration sur R3. Les apprentis doivent identifier et corriger le problème.

**Configuration incorrecte injectée sur R3 :**

```ios
! Le formateur a saisi (sans le dire aux apprentis) :
R3(config-router)# network 10.0.0.0 0.0.0.3 area 0
! au lieu de :
R3(config-router)# network 10.0.0.0 0.0.0.255 area 0
```

---

### 3.1 – Symptôme observé

```ios
R1# show ip ospf neighbor
```

**Q10.** R3 apparaît-il dans la liste des voisins de R1 ? ___________

**Q11.** Quelle est votre hypothèse sur la cause ? (expliquez pourquoi ce réseau n'est pas annoncé)

_________________________________________________________________________
_________________________________________________________________________

---

### 3.2 – Diagnostic

```ios
R3# show ip ospf
R3# show ip ospf interface Gi0/1
```

**Q12.** L'interface Gi0/1 de R3 est-elle activée pour OSPF ? Comment le vérifier ?

_________________________________________________________________________

---

### 3.3 – Correction

**Écrivez les commandes de correction sur R3 :**

```ios
R3(config)# router ospf 1
R3(config-router)# _____________________________________________
R3(config-router)# _____________________________________________
```

**Q13.** Après correction, R3 réapparaît-il dans `show ip ospf neighbor` de R1 ? ___________

---

## 📊 PARTIE 4 – Synthèse et questions d'analyse (15 min)

### 4.1 – Tableau récapitulatif final

> Après toutes les manipulations (R1 priority=200, R2 priority=0), remplissez :

| **Routeur** | **Router-ID** | **Priorité Gi0/1** | **Rôle sur le LAN** | **État dans show ip ospf neighbor (vu depuis R1)** |
|---|---|---|---|---|
| R1 | 1.1.1.1 | 200 | | — (c'est nous) |
| R2 | 2.2.2.2 | 0 | | |
| R3 | 3.3.3.3 | 1 | | |
| R4 | 4.4.4.4 | 1 | | |

---

### 4.2 – Questions d'analyse

**Q14.** Sur ce LAN 10.0.0.0/24 avec 4 routeurs, combien d'adjacences Full existent au total ? Justifiez.

```
Adjacences Full :
- R1 (DR) ↔ R2 : ✅/❌  (R2 priority=0, mais peut-il quand même avoir une adj. Full avec le DR ?)
- R1 (DR) ↔ R3 : _______
- R1 (DR) ↔ R4 : _______
- R? (BDR) ↔ R2 : _______
- R? (BDR) ↔ R3 : _______
- R? (BDR) ↔ R4 : _______

Total adjacences Full : _______
```

> *Note : priority=0 empêche d'être DR/BDR, mais n'empêche pas d'avoir une adjacence Full avec le DR et le BDR.*

---

**Q15.** Que se passe-t-il côté routage si R1 (le DR actuel) tombe en panne ? Décrivez la séquence en 3 étapes :

1. _______________________________________________________________________

2. _______________________________________________________________________

3. _______________________________________________________________________

---

**Q16.** Un réseau LAN a 6 routeurs OSPF. Comparez :
- Nombre d'adjacences Full **sans** DR/BDR : _______
- Nombre d'adjacences Full **avec** DR/BDR : _______

Quel gain en termes d'échanges de LSA cela représente-t-il ?

_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 – Wildcards | Tableau de calcul correct | /2 |
| Partie 1 – Config | 4 routeurs configurés correctement | /4 |
| Partie 1 – Vérif | show ip ospf neighbor relevé + Q1-Q5 | /4 |
| Partie 1 – Ping | 3 tests de connectivité | /2 |
| Partie 2 – Election | Manipulation priority + Q6-Q9 | /4 |
| Partie 3 – Debug | Identification + correction erreur + Q10-Q13 | /4 |
| Partie 4 – Synthèse | Tableau + Q14-Q16 | /4 |
| **Présentation / Soin** | Clarté des relevés, étapes suivies | /1 |
| **TOTAL** | | **/25** |

> *Barème ramené à /20 : score × 0,8*

---

## 📸 PORTFOLIO

**À rendre :**
- ✅ Ce document complété avec tous les relevés et réponses
- ✅ Capture(s) de `show ip ospf neighbor` à chaque étape clé

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
