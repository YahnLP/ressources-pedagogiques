# 📅 PLAN FINAL 10 JOURS + LOGISTIQUE EXAM — S6 · 3ᵉ ANNÉE · E31
## CCNA 200-301 : Les 10 jours qui séparent de la certification

---

> **Nom** : ___________________________
> **Score examen blanc** : _______ / 100 → _______ / 1000 estimé
> **Date visée pour l'examen** : ___________________________

---

## 🎯 Objectif de ce document

Tu sors de l'examen blanc avec un score et une liste de domaines à améliorer.
Ce plan transforme ce diagnostic en **actions concrètes jour par jour** pour les 10 jours restants.

---

## 📊 Analyse post-examen blanc

### Scores par domaine

```
D1 Fundamentals    : ___/20  →  ___% → ☐ Acquis (≥75%) ☐ À retravailler
D2 Network Access  : ___/20  →  ___% → ☐ Acquis ☐ À retravailler
D3 IP Connectivity : ___/20  →  ___% → ☐ Acquis ☐ À retravailler
D4 IP Services     : ___/12  →  ___% → ☐ Acquis ☐ À retravailler
D5 Security        : ___/14  →  ___% → ☐ Acquis ☐ À retravailler
D6 Automation      : ___/14  →  ___% → ☐ Acquis ☐ À retravailler
```

### Questions manquées — à analyser

```
Questions ratées : ___________________________________
Thèmes des erreurs : ________________________________
Erreurs bêtes (inattention) vs lacunes réelles : ____
```

---

## 🗓️ Plan jour par jour

### JOURS 1-2 — Attaque du domaine le plus faible

```
Mon domaine le plus faible : _______________________________________
Séance(s) à relire : _______________________________________________
Labs PT à refaire :
  □ _______________________________________________________________
  □ _______________________________________________________________
Aide-mémoires à relire : ___________________________________________
Objectif en fin de J2 : score de ___% sur ce domaine
```

### JOURS 3-4 — Deuxième domaine faible + sous-réseau

```
Mon 2ème domaine faible : __________________________________________
Séance(s) à relire : _______________________________________________

Exercices de sous-réseautage (indispensable) :
  □ /24 : trouver broadcast, hôtes utilisables
  □ /26, /28, /30 : même exercice
  □ VLSM : 3 sous-réseaux de tailles différentes
  □ Identifier à quel sous-réseau appartient une IP

Objectif J4 : calcul de masques sous 30 secondes
```

### JOURS 5-6 — Configuration IOS de mémoire

> Sans fiche, sur Packet Tracer vierge, configurer de A à Z :

```
□ J5 : Lab "VLANs + EtherChannel + Trunk" en 25 min
  → 2 switches, VLAN 10 et 20, EC LACP, trunk, ping E2E

□ J6 : Lab "OSPF multi-aire + inter-VLAN" en 35 min
  → 2 routeurs, R-on-a-stick, OSPF Area 0 + Area 1, vérif neighbors

Critère de réussite : 0 faute de syntaxe, pingall = 100%
```

### JOURS 7-8 — Révision rapide + pièges

```
□ Relire l'aide-mémoire final E31 (S20-2A doc 06)
□ Refaire les 30 questions QCM de S14-2A
□ Refaire les 40 questions CCNA Readiness de S20-2A

Pièges à revoir en priorité :
  □ ACL standard vs étendue (filtre src seul vs src+dst+port)
  □ Longest prefix match (pas la DA, pas la métrique)
  □ LACP modes (passive+passive ✗ · active+on ✗)
  □ show etherchannel summary → codes P/I/D/s
  □ DHCP excluded-address (pas "exclude")
  □ copy run start vs copy run tftp:
```

### JOUR 9 — Simulation chronométrée finale

```
□ Matin : refaire l'examen blanc S6 en 80 min CHRONO
  Objectif : ≥ 38/50 (760/1000 × facteur de correction ≈ 825)

□ Après-midi : corriger et noter les erreurs restantes
  □ J'ai encore raté : ___________________________________________
  □ Action pour demain : _________________________________________

□ Soir : lire "conseils du jour J" (voir page suivante)
  ARRÊTER de réviser après 22h
```

### JOUR 10 — JOUR DE L'EXAMEN

```
□ Réveil normal (pas de réveil 5h du matin)
□ Petit-déjeuner complet
□ Relire les 10 commandes incontournables (5 min max)
□ Partir avec 30 min d'avance au centre
□ Documents à emporter : Pièce d'identité + carte bancaire
□ Sur place : NE PAS réviser dans la salle d'attente
□ Pendant l'examen : appliquer la stratégie (voir ci-dessous)
```

---

## 🧠 Stratégie pendant les 120 minutes de l'examen réel

### La règle des 3 passages

```
PASSAGE 1 — Questions faciles (0-60 min) :
  → Répondre à toutes les questions dont tu es certain(e) en < 60s
  → Marquer les questions douteuses
  → Objectif : traiter 60-70% des questions

PASSAGE 2 — Questions difficiles (60-100 min) :
  → Revenir sur les questions marquées
  → Prendre 2-3 min max par question
  → Éliminer les mauvaises réponses

PASSAGE 3 — Dernière vérification (100-120 min) :
  → Scanner toutes les questions une dernière fois
  → Ne PAS changer une réponse sans raison solide
  → Questions sans réponse → OBLIGATOIRE de répondre (pas de pénalité)
```

### Pièges à éviter dans la salle

```
❌ Passer 10 min sur une question difficile → passer, revenir après
❌ Changer une réponse par doute sans raison → souvent faux
❌ Lire les réponses avant la question → risque de biais
❌ Négliger les simulations PT → elles valent souvent plus de points
❌ Paniquer sur les drag-and-drop → respirer, lire les instructions
```

### Types de questions spécifiques

```
QCM classique (1 réponse) :
  → Chercher la "MOST correct" ou "BEST" réponse
  → Souvent 2 réponses proches dont une est légèrement plus précise

QCM multiple (plusieurs réponses indiquées) :
  → L'énoncé dit "choose TWO" ou "choose THREE"
  → Ne pas cocher plus que demandé

Drag-and-drop :
  → Correspondance entre termes ou mise en ordre
  → Lire TOUS les éléments avant de placer

Simlet (lire des sorties de commandes) :
  → Prendre 2 min pour analyser la topologie/sortie
  → Les questions portent sur les sorties fournies, pas sur d'autres

Simulation Packet Tracer :
  → Configuration guidée → se concentrer sur ce qui est demandé
  → Ne pas reconfigurer ce qui n'est pas dans les missions
  → Vérifier avec ping avant de passer à la suivante
```

---

## 📋 Checklist logistique — Inscription et jour J

### Étapes d'inscription

```
□ 1. Créer un compte Cisco (cisco.com/login)
□ 2. Aller sur pearsonvue.com
□ 3. Chercher "Cisco" dans la liste des fournisseurs
□ 4. Sélectionner l'examen "200-301 CCNA"
□ 5. Choisir le mode : Centre d'examen OU Online (OnVUE)
□ 6. Sélectionner la date et l'heure
□ 7. Payer (~330 € — vérifier tarif actuel)
□ 8. Confirmation par email → numéro de confirmation à conserver

Ma date d'inscription : ___________________________
Mon numéro de confirmation : ___________________________
Adresse du centre : ___________________________
```

### Mode Online (OnVUE) — conditions

```
☐ Pièce d'identité prête (photographiée)
☐ Ordinateur avec webcam fonctionnelle
☐ Pièce fermée, seul(e), bureau dégagé
☐ Connexion Internet stable (filaire recommandé)
☐ Pas de moniteur supplémentaire
☐ Test système effectué sur le site Pearson avant le J
```

### Mode Centre d'examen

```
☐ Adresse vérifiée + trajet testé
☐ Arrivée 30 min avant l'heure
☐ Pièce d'identité photo + un second document
☐ Casiers disponibles pour affaires personnelles
☐ Fournitures : stylo et papier fournis par le centre
```

---

## 🔄 En cas d'échec — Plan B

```
Résultat : _______/1000 (seuil = 825)
Si échec (score < 825) :
  → Délai avant nouvelle tentative : 5 jours civils minimum
  → Débrief : noter toutes les questions dont on se souvient
  → Analyser les catégories signalées dans le rapport de résultat
  → 2 semaines de révision ciblée sur les domaines faibles

Le passage d'un examen de certification est normal à retenter.
La plupart des certifications Cisco nécessitent 1-2 tentatives.
```

---

## 🎯 Mon engagement personnel

```
Je m'engage à :
□ Réviser _____ heures par jour pendant 10 jours
□ Refaire au minimum _____ labs Packet Tracer
□ Passer l'examen avant le : ___________________________

Mon objectif de score : _______ / 1000
(Seuil minimum : 825 · Mon objectif réaliste : +50 pts tampon)

Signature : ___________________________  Date : ___________________________
```

---

*Plan de 10 Jours + Logistique Exam — BAC PRO CIEL | E31 | 3ᵉ année S6*
*CCNA 200-301 — Cisco · Pearson VUE*
