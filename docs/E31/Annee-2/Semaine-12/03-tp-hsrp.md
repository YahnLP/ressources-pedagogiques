# 🔬 TP PACKET TRACER – S12 ANNÉE 2 – E31
## HSRP : Redondance de Passerelle, Préemption, Tracking, Simulation de Bascule

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Configurer HSRP sur deux routeurs Cisco (IP virtuelle, priorité, preempt, timers)
- ✅ Vérifier l'élection Active/Standby avec `show standby brief`
- ✅ Simuler une panne et observer la bascule automatique
- ✅ Configurer le tracking d'interface WAN et tester son déclenchement
- ✅ Observer l'impact de `preempt` lors du retour de l'Active

---

## ⏱️ DURÉE : 70 min

---

## 📋 TOPOLOGIE

```
          INTERNET (WAN)
         /              \
    Gi0/1             Gi0/1
  [R-PRINCIPAL]    [R-SECOURS]
  203.0.113.1      203.0.113.5
    Gi0/0             Gi0/0
  192.168.1.1      192.168.1.2
        \              /
         [SW-CORE]
         /    |    \
       PC1   PC2   PC3
  192.168.1.10  .20  .30
  GW : 192.168.1.254 (IP virtuelle HSRP)
```

---

## 📋 PLAN D'ADRESSAGE

| **Équipement** | **Interface** | **IP** | **Masque** | **Rôle** |
|---|---|---|---|---|
| R-PRINCIPAL | Gi0/0 (LAN) | 192.168.1.1 | /24 | Interface LAN |
| R-PRINCIPAL | Gi0/1 (WAN) | 203.0.113.1 | /30 | Liaison Internet |
| R-SECOURS | Gi0/0 (LAN) | 192.168.1.2 | /24 | Interface LAN |
| R-SECOURS | Gi0/1 (WAN) | 203.0.113.5 | /30 | Liaison Internet |
| PC1–PC3 | — | 192.168.1.10–.30 | /24 | GW : **192.168.1.254** |

> **IP virtuelle HSRP :** 192.168.1.254 (groupe 1)
> **Politique :** R-PRINCIPAL = Active (prio 110) ; R-SECOURS = Standby (prio 90)

---

## 🧪 PARTIE 1 – Vérification préliminaire SANS HSRP (5 min)

### 1.1 – Test de connectivité initial

```
PC1# ping 192.168.1.254    → _______  (IP virtuelle — n'existe pas encore)
PC1# ping 192.168.1.1      → _______  (interface LAN de R-PRINCIPAL)
PC1# ping 192.168.1.2      → _______  (interface LAN de R-SECOURS)
```

**Q1.** Avant HSRP, l'IP 192.168.1.254 répond-elle ? Pourquoi ?

_________________________________________________________________________

---

## 🔬 PARTIE 2 – Configuration HSRP de base (20 min)

### 2.1 – Configuration R-PRINCIPAL (Active)

```ios
R-PRINCIPAL(config)# interface GigabitEthernet0/0
R-PRINCIPAL(config-if)# standby _____ ip _____________
R-PRINCIPAL(config-if)# standby _____ priority _____
R-PRINCIPAL(config-if)# standby _____ preempt
R-PRINCIPAL(config-if)# standby _____ timers _____ _____
```

*Groupe = 1 ; IP virtuelle = 192.168.1.254 ; Priorité = 110 ; Hello=1s ; Hold=3s*

---

### 2.2 – Configuration R-SECOURS (Standby)

```ios
R-SECOURS(config)# interface GigabitEthernet0/0
R-SECOURS(config-if)# standby _____ ip _____________
R-SECOURS(config-if)# standby _____ priority _____
R-SECOURS(config-if)# standby _____ preempt
R-SECOURS(config-if)# standby _____ timers _____ _____
```

*Groupe = 1 ; IP virtuelle = 192.168.1.254 ; Priorité = 90 ; Mêmes timers*

---

### 2.3 – Vérification initiale

**Sur R-PRINCIPAL :**

```ios
R-PRINCIPAL# show standby brief
```

**Relevez la sortie :**

```
Interface   Grp  Pri P State   Active    Standby    Virtual IP
_________   ___  ___ _ _____   ______    ________   ___________
```

**Q2.** R-PRINCIPAL est-il bien en état Active ? ___________

**Q3.** L'IP 192.168.1.254 est-elle bien la Virtual IP ? ___________

---

**Sur R-SECOURS :**

```ios
R-SECOURS# show standby brief
```

```
Interface   Grp  Pri P State   Active    Standby    Virtual IP
_________   ___  ___ _ _____   ______    ________   ___________
```

**Q4.** Quel état affiche R-SECOURS ? ___________

---

### 2.4 – Test de connectivité AVEC HSRP

```
PC1# ping 192.168.1.254    → _______
PC1# ping 203.0.113.1      → _______  (Internet via R-PRINCIPAL)
```

---

## 💥 PARTIE 3 – Simulation de panne et bascule (20 min)

### 3.1 – Simuler la panne de R-PRINCIPAL

**Désactiver l'interface LAN de R-PRINCIPAL :**

```ios
R-PRINCIPAL(config)# interface GigabitEthernet0/0
R-PRINCIPAL(config-if)# shutdown
```

**Immédiatement, observer sur R-SECOURS :**

```ios
R-SECOURS# show standby brief
```

**Relevez l'état après la bascule :**

```
Interface   Grp  Pri P State   Active    Standby    Virtual IP
_________   ___  ___ _ _____   ______    ________   ___________
```

**Q5.** R-SECOURS est-il passé à l'état Active ? ___________

**Q6.** Combien de secondes la bascule a-t-elle pris (approximativement, selon les timers configurés) ?

_________________________________________________________________________

---

### 3.2 – Test de connectivité pendant la panne

```
PC1# ping 192.168.1.254    → _______
PC1# ping 203.0.113.1      → _______ (Internet doit passer via R-SECOURS maintenant)
```

**Q7.** Les PCs ont-ils besoin d'être reconfigurés pour continuer à fonctionner ? Pourquoi ?

_________________________________________________________________________

---

### 3.3 – Retour de R-PRINCIPAL (AVEC preempt)

**Réactiver l'interface LAN de R-PRINCIPAL :**

```ios
R-PRINCIPAL(config)# interface GigabitEthernet0/0
R-PRINCIPAL(config-if)# no shutdown
```

**Attendre ~5 secondes puis vérifier :**

```ios
R-PRINCIPAL# show standby brief
R-SECOURS# show standby brief
```

**Q8.** R-PRINCIPAL a-t-il repris le rôle Active ? Pourquoi (quelle commande a permis ça) ?

_________________________________________________________________________

---

### 3.4 – Retour SANS preempt (suppression de preempt)

**Sur R-PRINCIPAL, supprimer la préemption :**

```ios
R-PRINCIPAL(config)# interface GigabitEthernet0/0
R-PRINCIPAL(config-if)# no standby 1 preempt
```

**Simuler à nouveau la panne (shutdown Gi0/0 de R-PRINCIPAL) :**

→ R-SECOURS passe Active ✅

**Puis rétablir (no shutdown) :**

```ios
R-PRINCIPAL# show standby brief
```

**Q9.** R-PRINCIPAL reprend-il Active cette fois-ci ? Qu'est-ce qui a changé ?

_________________________________________________________________________
_________________________________________________________________________

**Remettre `preempt` sur R-PRINCIPAL avant de continuer.**

---

## 📡 PARTIE 4 – Tracking d'interface WAN (15 min)

### 4.1 – Configurer le tracking sur R-PRINCIPAL

> Objectif : si l'interface WAN (Gi0/1) de R-PRINCIPAL tombe, sa priorité HSRP doit baisser sous celle de R-SECOURS.

**Calcul préalable :**

```
Priorité R-PRINCIPAL = 110
Priorité R-SECOURS   = 90

Pour que la bascule se produise si WAN R-PRINCIPAL tombe :
  110 - décrement < 90
  décrement > 20
  → Choisir décrement = 30
  → Si WAN tombe : 110 - 30 = 80 < 90 ✅ → Bascule vers R-SECOURS
```

```ios
R-PRINCIPAL(config)# interface GigabitEthernet0/0
R-PRINCIPAL(config-if)# standby 1 track GigabitEthernet0/1 30
```

**Vérifier :**

```ios
R-PRINCIPAL# show standby
```

Cherchez la ligne : `Track interface GigabitEthernet0/1 state ___ decrement 30`

**État actuel du tracking :** ___________

---

### 4.2 – Simuler la panne WAN

**Désactiver le lien WAN de R-PRINCIPAL :**

```ios
R-PRINCIPAL(config)# interface GigabitEthernet0/1
R-PRINCIPAL(config-if)# shutdown
```

**Observer sur R-PRINCIPAL :**

```ios
R-PRINCIPAL# show standby
```

**Q10.** Quelle est maintenant la priorité de R-PRINCIPAL après la panne WAN ?

_________________________________________________________________________

**Q11.** R-SECOURS est-il devenu Active ? (Vérifier avec `show standby brief` sur R-SECOURS)

_________________________________________________________________________

---

### 4.3 – Test connectivité lors de la panne WAN

```
PC1# ping 203.0.113.1    → _______ (R-PRINCIPAL WAN down)
PC1# ping 203.0.113.5    → _______ (R-SECOURS WAN doit répondre)
```

**Q12.** La connectivité Internet est-elle maintenue via R-SECOURS ? ___________

---

## 📊 PARTIE 5 – Questions d'analyse et synthèse (10 min)

**Q13.** Si vous n'aviez pas configuré `preempt` sur R-SECOURS, et que la panne WAN de R-PRINCIPAL déclenche une bascule, que se passe-t-il quand le WAN de R-PRINCIPAL revient ?

_________________________________________________________________________
_________________________________________________________________________

**Q14.** Un collègue configure HSRP avec `timers 1 1`. Quel problème cela pose-t-il ? (Rappel : Hold ≥ 3 × Hello)

_________________________________________________________________________
_________________________________________________________________________

**Q15.** Complétez le tableau de synthèse final :

| **Scénario** | **R-PRINCIPAL état** | **R-SECOURS état** | **Trafic routé par** |
|---|---|---|---|
| État normal | | | |
| Panne LAN R-PRINCIPAL | | | |
| Retour LAN R-PRINCIPAL (avec preempt) | | | |
| Retour LAN R-PRINCIPAL (sans preempt) | | | |
| Panne WAN R-PRINCIPAL (avec tracking) | | | |

**Q16.** Quelle est la différence entre HSRP et VRRP en termes d'interopérabilité ? Dans quel contexte utiliseriez-vous VRRP plutôt qu'HSRP ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 | Test initial + Q1 | /1 |
| Partie 2 | Configuration HSRP sur 2 routeurs + show standby brief | /5 |
| Partie 2 | Q2–Q4 | /2 |
| Partie 3 | Simulation panne + bascule observée | /4 |
| Partie 3 | Q5–Q9 (preempt vs no preempt) | /4 |
| Partie 4 | Tracking configuré + simulation WAN + Q10–Q12 | /4 |
| Partie 5 | Q13–Q16 + tableau synthèse | /4 |
| Présentation / Clarté | — | /1 |
| **TOTAL** | | **/25** |

> *Ramené à /20 : score × 0,8*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
