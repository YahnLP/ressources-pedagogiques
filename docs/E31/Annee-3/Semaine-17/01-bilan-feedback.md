# 📊 BILAN COLLECTIF POST-ÉPREUVE BLANCHE — S17-A3 E31
## Analyse des Résultats + Stratégie Finale + Plan d'Action

---

> **Ce document est distribué en S18, après correction des copies.** Il ne nomme aucun candidat individuellement — l'objectif est de transformer les erreurs collectives en leviers de progression pour les deux dernières semaines.

---

## 1. RÉSULTATS AGRÉGÉS PAR COMPÉTENCE

> Le formateur remplit ce tableau avant la restitution en S18.

| **Compétence** | **Moy. groupe** | **% ≥ 70%** | **% < 50%** | **Tendance** |
|---|---|---|---|---|
| Adressage VLSM | ___/10 | ___% | ___% | |
| OSPF multi-area | ___/8 | ___% | ___% | |
| HSRP calcul + config | ___/10 | ___% | ___% | |
| VPN IPsec | ___/8 | ___% | ___% | |
| ACL étendues | ___/6 | ___% | ___% | |
| Nagios | ___/10 | ___% | ___% | |
| Troubleshooting | ___/8 | ___% | ___% | |
| **Oral — Présentation** | ___/8 | ___% | ___% | |
| **Oral — Démo** | ___/12 | ___% | ___% | |
| **Oral — Troubleshooting** | ___/8 | ___% | ___% | |

---

## 2. LES 5 QUESTIONS LES PLUS RATÉES

> À analyser collectivement — sans identifier les candidats.

### Erreur collective N°1 — [À compléter par le formateur]

```
Question : ________________________________________
Erreur type : _____________________________________
Explication correcte :
```

---

### Erreur collective N°2

```
Question : ________________________________________
Erreur type : _____________________________________
Explication correcte :
```

---

### Erreur collective N°3

```
Question : ________________________________________
Erreur type : _____________________________________
Explication correcte :
```

---

## 3. LES PIÈGES QUI ONT FAIT CHUTER LE PLUS DE CANDIDATS

> Voici les pièges statistiquement les plus dangereux, identifiés sur cette promotion :

| **Piège** | **Nbre victimes** | **La règle simple** |
|---|---|---|
| Délai bascule = **Hold Timer** (pas Hello) | ___/16 | Bascule ≈ Hold Timer (défaut 10s) |
| ACL crypto **non-miroir** → VPN Phase 2 à 0 pkts | ___/16 | Miroir = source ↔ destination inversées |
| `exit 1` = **WARNING** (pas CRITICAL) | ___/16 | 0=OK, 1=WARN, 2=CRIT, 3=UNKN |
| Preempt **absent** → P absent dans show standby | ___/16 | P = preempt configuré |
| OSPFv3 sans **router-id IPv4** | ___/16 | Obligatoire même en réseau IPv6-only |
| `permit ip any any` final **oublié** → tout bloqué | ___/16 | Deny implicite = toujours présent |
| DHCPv6 **stateful** pour traçabilité (pas SLAAC) | ___/16 | Traçabilité = binding table = stateful |

---

## 4. ANALYSE DE L'ORAL

### Ce qui différencie les meilleurs oraux

> Basé sur les grilles de jury de cette session :

**Les 3 comportements observés chez les candidats avec oral > 32/40 :**

1. **Ils testent avant de regarder la config.** Quand une panne est injectée, leur premier réflexe est `ping` et `show ip route` — pas `show run`. Cela montre une méthode, pas de la chance.

2. **Ils nomment les protocoles avec précision.** Ils disent "le Hold Timer expire, R-BDX-B envoie un message Coup et passe Active" plutôt que "le routeur de secours prend le relais". Le vocabulaire technique signale la maîtrise.

3. **Ils verbalisent leur incertitude proprement.** "Je pense que le problème est dans l'ACL crypto — je vais vérifier en regardant les compteurs pkts sur les deux routeurs" vaut bien plus qu'un silence de 3 minutes.

### Les 3 erreurs les plus fréquentes à l'oral

1. **Présenter le schéma réseau sans parler des choix** — "voilà mes adresses" sans expliquer pourquoi ces adresses → jury sans matière pour évaluer la compréhension
2. **Réaliser les tests dans un ordre non logique** — faire T7 (VPN) avant T3 (OSPF) alors que le VPN dépend du routage
3. **Se figer sur la panne** sans utiliser les commandes de diagnostic — rester à regarder la topologie PT sans taper de commandes

---

## 5. PROJECTIONS NOTE FINALE

> Basé sur la corrélation statistique entre l'épreuve blanche et l'épreuve réelle.

| **Résultat blanc** | **Projection épreuve réelle** | **Action recommandée** |
|---|---|---|
| ≥ 70/100 | 🟢 Bien positionné(e) | Consolider les derniers points ; travailler l'expression orale |
| 55–69/100 | 🟡 Passable | 2 semaines de révision ciblée sur les lacunes identifiées |
| 40–54/100 | 🟠 Risqué | Révision intensive + simulation oral supplémentaire |
| < 40/100 | 🔴 Danger | Plan d'urgence : refaire P1–P5 du parcours remédiation + 2 oraux blancs |

---

## 6. PLAN D'ACTION INDIVIDUEL — LES 2 DERNIÈRES SEMAINES

> Chaque apprenti complète ce plan personnellement.

```
═══════════════════════════════════════════════════════════
PLAN D'ACTION — [Votre Nom]
Score épreuve pratique : ___/60
Score oral : ___/40
Total blanc : ___/100
═══════════════════════════════════════════════════════════

MON POINT LE PLUS FAIBLE (à travailler EN PRIORITÉ) :
  Domaine : ______________________________________________
  Action concrète : ______________________________________
  Temps estimé : _____ heures

MON DEUXIÈME POINT FAIBLE :
  Domaine : ______________________________________________
  Action concrète : ______________________________________

POUR L'ORAL, JE DOIS TRAVAILLER :
  ☐ Structurer ma présentation (schéma + protocoles + HA)
  ☐ Mémoriser les tests de démo dans le bon ordre
  ☐ Pratiquer la méthode de troubleshooting à voix haute
  ☐ Apprendre le vocabulaire précis de : ________________

PENDANT L'ÉPREUVE RÉELLE, JE RETIENDRAI :
  → Gestion du temps : _________________________________
  → Piège que je ne ferai plus : _______________________
  → Ma force à valoriser : _____________________________
═══════════════════════════════════════════════════════════
```

---

## 7. CONSEILS PRATIQUES POUR LE JOUR J

### Épreuve pratique (2h30–3h)

```
□ Lire l'intégralité du sujet AVANT de commencer (5 min)
  → Repérer les dépendances (VLSM → OSPF → HSRP → VPN)
  → Calculer le temps par partie

□ Commencer par le VLSM — c'est le socle de tout le reste
  → Une erreur de plan d'adressage cascade sur 5 parties

□ Si bloqué sur une question, passer à la suivante
  → Mieux vaut 8 parties à 70% que 3 parties à 100% et 5 à 0%

□ Les 20 dernières minutes : relecture exclusive
  → Vérifier les wildcards, les IPs, les directions ACL
```

### Oral jury

```
□ Préparer un schéma réseau papier avec TOUTES les infos
  → IPs, masques, protocoles, priorités HSRP, PSK VPN (masquée)

□ Mémoriser l'ordre des 10 tests (T1 à T10)
  → Les exécuter dans l'ordre sans hésitation

□ Pour le troubleshooting : TOUJOURS tester avant de regarder la config
  → "ping → show ip route → show ip ospf neighbor → etc."

□ Si vous ne savez pas répondre à une question jury :
  → "Je pense que la réponse est X parce que Y — mais je ne suis pas
     certain(e), je vérifierais avec la commande Z"
  → Vaut mieux que le silence
```

---

## 8. RESSOURCES DE DERNIÈRE MINUTE

| **Sujet** | **Document à retravailler** |
|---|---|
| VLSM | Parcours P1 — section A et B |
| OSPF + OSPFv3 | Fiche cours S1-A3 + Parcours P2 |
| HSRP | Fiche cours S12-A2 + TD-HA1 de S13 |
| VPN IPsec | Fiche cours S7-A2 + Parcours P4 |
| Nagios | Fiche cours S10-A2 + Annale 1 de S13 |
| Troubleshooting | Correction Lab S11-A3 |
| Oral | Sujet soutenance S19-A2 + grille jury |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
