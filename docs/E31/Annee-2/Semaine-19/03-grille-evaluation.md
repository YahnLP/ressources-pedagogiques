# 📊 GRILLE D'ÉVALUATION — SOUTENANCE U31 ANNÉE 2
## Infrastructure Multi-Sites CIEL-Corp

**Candidat : ________________  Prénom : ________________**
**Date : ________________  Jury : ________________**
**Heure de début : ________  Heure de fin : ________**

---

## CRITÈRE 1 — Présentation de la topologie (3 pts)

### 1.1 — Schéma réseau et plan d'adressage

| **Indicateur** | **0** | **0,5** | **1** |
|---|---|---|---|
| Schéma réseau présent et lisible | Absent | Incomplet / illisible | Complet, annoté, clair |
| Plan d'adressage cohérent (sous-réseaux valides, no overlap) | Erreurs bloquantes | Erreurs mineures | Cohérent et justifié |

**Score 1.1 : _____ / 2**

### 1.2 — Qualité de la présentation orale

| **Indicateur** | **0** | **0,5** | **1** |
|---|---|---|---|
| Capacité à expliquer le rôle de chaque composant sans lire | Lecture intégrale | Partiellement autonome | Explication fluide, vocabulaire technique correct |

**Score 1.2 : _____ / 1**

**Notes jury (Critère 1) :**

_________________________________________________________________________
_________________________________________________________________________

**TOTAL CRITÈRE 1 : _____ / 3**

---

## CRITÈRE 2 — Fonctionnalité de la topologie (4 pts)

### 2.1 — Technologies présentes et opérationnelles

| **Technologie** | **Absent** | **Présent mais non fonctionnel** | **Fonctionnel** | **Points** |
|---|---|---|---|---|
| OSPF (adjacences FULL, routes visibles) | 0 | 0,25 | **0,5** | / 0,5 |
| HSRP (Active/Standby correct, IP virtuelle) | 0 | 0,25 | **0,5** | / 0,5 |
| VPN IPsec (Phase 1 + Phase 2, pkts encrypt) | 0 | 0,25 | **0,5** | / 0,5 |
| ACL étendue (rédigée, appliquée, matches visibles) | 0 | 0,25 | **0,5** | / 0,5 |
| Nagios (au moins 2 checks, plugin testé) | 0 | 0,25 | **0,5** | / 0,5 |
| HSRP preempt + timers optimisés | 0 | 0,25 | **0,5** | / 0,5 |
| Tracking HSRP (interface WAN trackée) | 0 | 0,25 | **0,5** | / 0,5 |
| Connectivité totale Paris ↔ Lyon | 0 | 0,25 | **0,5** | / 0,5 |

**TOTAL CRITÈRE 2 : _____ / 4**

---

## CRITÈRE 3 — Démonstration fonctionnelle (5 pts)

### Tests obligatoires

| **Test** | **Non réalisé** | **Réalisé avec aide** | **Réalisé de façon autonome** | **Pts** |
|---|---|---|---|---|
| T1 — Ping LAN Paris | 0 | 0,25 | **0,5** | / 0,5 |
| T2 — Ping inter-sites Paris↔Lyon | 0 | 0,25 | **0,5** | / 0,5 |
| T3 — `show ip ospf neighbor` (FULL visible) | 0 | 0,25 | **0,5** | / 0,5 |
| T4 — `show standby brief` (Active/Standby) | 0 | 0,25 | **0,5** | / 0,5 |
| T5 — Bascule HSRP (shutdown + R-B passe Active) | 0 | 0,25 | **0,5** | / 0,5 |
| T6 — `show crypto ipsec sa` (pkts encrypt > 0) | 0 | 0,25 | **0,5** | / 0,5 |
| T7 — `show ip access-lists` (matches visibles) | 0 | 0,25 | **0,5** | / 0,5 |
| T8 — Test plugin Nagios CLI (résultat cohérent) | 0 | 0,25 | **0,5** | / 0,5 |

### Tests valorisants réalisés (bonus jusqu'à +1 pt)

- [ ] Retour preempt après bascule HSRP démontré (+0,25)
- [ ] Tracking WAN déclenche bascule démontré (+0,25)
- [ ] `show crypto isakmp sa` QM_IDLE démontré (+0,25)
- [ ] `show ip route ospf` routes distribuées visibles (+0,25)

**Bonus : _____ / 1**

**TOTAL CRITÈRE 3 : _____ / 5**

---

## CRITÈRE 4 — Défense des choix techniques (2 pts)

### Grille de notation des réponses aux questions jury

| **Question posée** | **Réponse** | **Score** |
|---|---|---|
| Question 1 : _________________________ | _________________________ | / 0,5 |
| Question 2 : _________________________ | _________________________ | / 0,5 |
| Question 3 : _________________________ | _________________________ | / 0,5 |
| Bonus (si pertinence/profondeur exceptionnelle) | | / 0,5 |

**Barème :**
- **0,5 pt** : réponse correcte, justifiée, vocabulaire technique approprié
- **0,25 pt** : réponse partiellement correcte ou justification incomplète
- **0 pt** : silence, réponse incorrecte, confusion avec un autre concept

**TOTAL CRITÈRE 4 : _____ / 2**

---

## CRITÈRE 5 — Troubleshooting Live (4 pts)

### Panne injectée par le jury

**Description de la panne injectée :** ___________________________________________

**Niveau de difficulté :** ☐ Facile ☐ Standard ☐ Expert

---

### Grille d'évaluation du troubleshooting

#### 5.1 — Méthode de diagnostic (2 pts)

| **Comportement observé** | **0** | **0,5** | **1** |
|---|---|---|---|
| **Identification du symptôme** : commence par tester la connectivité avant de regarder la config | Regarde directement la config sans tester | Teste puis config avec hésitation | Teste d'abord, puis remonte méthodiquement |
| **Commandes utilisées** : utilise les bons `show` pour chaque problème | Commandes aléatoires ou absentes | Commandes partiellement adaptées | Commandes précises, adaptées au symptôme observé |

**Score 5.1 : _____ / 2**

#### 5.2 — Résolution (2 pts)

| **Étape** | **Non réalisé** | **Partiellement** | **Complet** | **Pts** |
|---|---|---|---|---|
| **Identification correcte** de la panne | 0 | 0,5 | **1** | / 1 |
| **Correction et vérification** (la correction fonctionne) | 0 | 0,5 | **1** | / 1 |

**Score 5.2 : _____ / 2**

**Déroulement du troubleshooting (notes jury) :**

```
Symptôme identifié en premier : _____________________________________________
Commandes utilisées : _______________________________________________________
Hypothèse formulée : ________________________________________________________
Correction proposée : _______________________________________________________
Vérification effectuée : ____________________________________________________
Temps utilisé : _____ / 10 min
```

**TOTAL CRITÈRE 5 : _____ / 4**

---

## CRITÈRE 6 — Expression orale et posture professionnelle (2 pts)

| **Indicateur** | **0** | **0,5** | **1** |
|---|---|---|---|
| **Clarté et structure** : présentation logique, transitions claires entre les phases | Présentation désordonnée | Structure présente mais saccadée | Présentation fluide, bien structurée |
| **Vocabulaire technique** : utilise correctement les termes réseau | Vocabulaire approximatif ou incorrect | Vocabulaire correct mais hésitant | Vocabulaire précis, maîtrisé |

**TOTAL CRITÈRE 6 : _____ / 2**

---

## 📊 RÉCAPITULATIF ET NOTE FINALE

| **Critère** | **Points obtenus** | **Points max** |
|---|---|---|
| 1 — Présentation topologie | | /3 |
| 2 — Fonctionnalité topologie | | /4 |
| 3 — Démonstration fonctionnelle | | /5 |
| 4 — Défense des choix | | /2 |
| 5 — Troubleshooting live | | /4 |
| 6 — Expression orale + posture | | /2 |
| **TOTAL** | | **/20** |

---

## 🚦 DÉCISION

| **Note** | **Décision** | **Action** |
|---|---|---|
| **≥ 15/20** | ✅✅ Très bien | Compétences U31 A2 dépassant les attendus |
| **12–14/20** | ✅ Bien | Compétences U31 A2 maîtrisées |
| **10–11/20** | ✅ Validé | Compétences U31 A2 acquises |
| **8–9/20** | ⚠️ Insuffisant | Rappel possible (voir politique de l'établissement) |
| **< 8/20** | ❌ Non validé | Rattrapage obligatoire, plan de remédiation |

**Décision : ________________  Note finale : _____ / 20**

---

## 💬 FEEDBACK ORAL — POINTS À RESTITUER AU CANDIDAT

### Points forts observés

1. _________________________________________________________________________
2. _________________________________________________________________________
3. _________________________________________________________________________

### Points d'amélioration

1. _________________________________________________________________________
2. _________________________________________________________________________

### Conseil principal pour la progression A3

_________________________________________________________________________
_________________________________________________________________________

---

**Signature du jury : ________________  Date : ________________**

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
