# 🎲 ACTIVITÉ DÉCOUVERTE – S12 ANNÉE 2 – E31
## « Le Routeur Qui Tombe » : Quand Votre Passerelle Devient un Point de Défaillance Unique

---

## 🎯 OBJECTIFS

- ✅ Faire émerger le **problème du SPOF** (Single Point of Failure) sur la passerelle par défaut
- ✅ Quantifier l'impact d'une panne de passerelle (durée, périmètre, conséquences)
- ✅ Explorer les solutions possibles avant d'arriver à HSRP
- ✅ Comprendre pourquoi une adresse IP **virtuelle** partagée est la solution élégante

---

## ⏱️ DURÉE : 30 min

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur dessine la topologie standard au tableau :**

```
       INTERNET
           │
       [R-PRINCIPAL]
       IP: 192.168.1.1
           │
       [SWITCH]
      /    │    \
  PC1     PC2    PC3
  GW: 192.168.1.1
```

**Question d'accroche :**

> *"Les trois PCs ont leur passerelle configurée sur 192.168.1.1. C'est le seul chemin vers Internet. Que se passe-t-il si R-PRINCIPAL tombe ?"*

---

## 💥 PHASE 1 – Le Calcul de l'Impact (8 min)

**Groupes de 4 — Quantifiez les conséquences :**

**Scénario A — PME de 50 employés, 9h00 un lundi matin :**

| **Question** | **Votre estimation** |
|---|---|
| Combien d'employés sont affectés ? | |
| Quels services sont coupés ? (e-mail, ERP, Internet, VPN…) | |
| Combien de temps avant que quelqu'un signale le problème ? | |
| Combien de temps pour remplacer/redémarrer le routeur en panne ? | |
| Coût estimé de l'interruption (€/heure) ? | |

**Scénario B — Hôpital, salle d'urgences :**

| **Question** | **Votre estimation** |
|---|---|
| Quels services réseau sont vitaux ? | |
| RTO (Recovery Time Objective) maximum acceptable ? | |
| Une coupure de 30 min est-elle acceptable ? | |

> **Message du formateur :** *"Dans les deux cas, un seul routeur = un seul point de défaillance = SPOF (Single Point of Failure). C'est une faiblesse architecturale inacceptable dans un réseau professionnel."*

---

## 🤔 PHASE 2 – Les Tentatives de Solution (8 min)

**Le formateur présente et le groupe évalue chaque solution :**

---

**Solution 1 : Deux routeurs, deux passerelles**

```
       INTERNET
      /         \
  [R1]          [R2]
  .1             .2
  GW-PC1: .1  GW-PC2: .2
```

> *"La moitié des PCs use R1, l'autre moitié use R2. Si R1 tombe, les PCs de R1 sont coupés mais pas les autres."*

| **Avantage** | **Problème** |
|---|---|
| Simple à configurer | Si R1 tombe, les 50% de PCs sur R1 ne basculent PAS sur R2 automatiquement |
| | Les admins doivent changer manuellement la passerelle sur chaque PC |
| | Non-transparent pour les utilisateurs |

**Verdict :** ⚠️ Partiel — réduit l'impact mais ne l'élimine pas.

---

**Solution 2 : Script sur chaque PC qui détecte la panne et change la GW**

> *"Un script ping R1 toutes les 30 secondes et modifie la route par défaut si R1 ne répond pas."*

| **Avantage** | **Problème** |
|---|---|
| Automatique | Script sur 200 PCs = cauchemar de maintenance |
| | Délai de détection : jusqu'à 30 s + temps de modification |
| | N'est pas standard, fragile |

**Verdict :** ❌ Impraticable en production.

---

**Solution 3 : Une adresse IP virtuelle, partagée par deux routeurs**

```
       INTERNET
      /         \
  [R1]          [R2]
  .1  \        / .2
       [IP VIRTUELLE : .254]
              │
          [SWITCH]
  GW de TOUS les PCs : .254
```

> *"Les deux routeurs "possèdent" la même IP virtuelle .254. Le premier qui répond aux ARP l'utilise. Si l'un tombe, l'autre prend automatiquement l'IP virtuelle."*

**Questions :**

**Q1.** Les PCs ont besoin d'être reconfigurés lors d'une bascule ? ___________

**Q2.** Comment les deux routeurs se coordonnent-ils pour décider lequel répond ? ___________

**Q3.** Quel protocole s'en charge ? ___________

> **Réponse formateur :** *"C'est exactement ce que fait HSRP (Hot Standby Router Protocol) chez Cisco, et VRRP (Virtual Router Redundancy Protocol) en standard ouvert. Un routeur est Active (répond aux ARP de la .254), l'autre est Standby (prêt à prendre le relais). Transparent pour tous les PCs."*

---

## 📊 PHASE 3 – Tableau Comparatif Final (8 min)

**À remplir collectivement :**

| **Critère** | **1 seul routeur** | **2 routeurs / 2 GW** | **HSRP / VRRP** |
|---|---|---|---|
| Redondance | ❌ | ⚠️ Partielle | ✅ Complète |
| Transparence pour les PCs | ✅ | ❌ | ✅ |
| Bascule automatique | — | ❌ | ✅ |
| Délai de bascule | — | Très long | **Quelques secondes** |
| Complexité de config | Nulle | Faible | Modérée |
| Standard professionnel | Non | Non | **OUI** |

---

## ✍️ SYNTHÈSE (2 min)

```
┌─────────────────────────────────────────────────────────────────────┐
│  HSRP / VRRP = Redondance de Passerelle (First Hop Redundancy)     │
│                                                                     │
│  Principe :                                                         │
│  • Un groupe de routeurs partage une adresse IP virtuelle           │
│  • Les PCs utilisent l'IP virtuelle comme passerelle                │
│  • Un routeur est "Active" (traite le trafic)                       │
│  • Un routeur est "Standby" (prêt à prendre le relais)             │
│  • En cas de panne de l'Active → Standby prend le relais           │
│    automatiquement, en quelques secondes, de façon transparente     │
│                                                                     │
│  HSRP : Cisco propriétaire  |  VRRP : standard ouvert (RFC 5798)   │
└─────────────────────────────────────────────────────────────────────┘
```

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
