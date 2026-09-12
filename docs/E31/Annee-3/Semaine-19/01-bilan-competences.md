# 🗺️ BILAN DE COMPÉTENCES E31 — ANNÉE 2 & ANNÉE 3
## Auto-Évaluation Finale + Fiche Individuelle de Bilan

**Nom : ________________  Prénom : ________________  Date : ________________**

---

> *Ce document n'est pas noté. Il vous appartient entièrement. Soyez honnête — c'est le seul moyen d'en tirer de la valeur pour la suite.*

---

## PARTIE 1 — LE CHEMIN PARCOURU

### Il y a 2 ans, vous ne saviez pas (encore) faire ça…

> Cochez ce que vous maîtrisez aujourd'hui :

**Réseau de base**
- [ ] Calculer un plan d'adressage VLSM multi-sites depuis un bloc IP donné
- [ ] Écrire un network statement OSPF avec le wildcard exact
- [ ] Lire `show ip ospf neighbor` et identifier un problème d'adjacence
- [ ] Configurer OSPF multi-area avec un ABR

**Sécurité réseau**
- [ ] Rédiger une ACL étendue avec 5 règles ordonnées correctement
- [ ] Placer une ACL sur la bonne interface dans la bonne direction
- [ ] Configurer un VPN IPsec site-à-site en 5 étapes sur Cisco IOS
- [ ] Diagnostiquer un VPN asymétrique (`encaps=5, decaps=0`)

**Haute disponibilité**
- [ ] Configurer HSRP avec preempt, timers et tracking d'interface WAN
- [ ] Calculer si une bascule HSRP aura lieu (décrement vs prio Standby)
- [ ] Distinguer HSRP (Cisco) et VRRP (standard) — vocabulaire + interopérabilité
- [ ] Expliquer le rôle du Gratuitous ARP dans une bascule

**Supervision**
- [ ] Rédiger un `define host {}` et un `define service {}` valides
- [ ] Calculer l'heure exacte d'une alerte (Soft State → Hard State)
- [ ] Écrire un plugin bash avec exit 0/1/2/3 et perf data
- [ ] Identifier le point aveugle supervision/HA (Nagios OK ≠ infra OK)

**IPv6 et protocoles avancés**
- [ ] Simplifier et développer une adresse IPv6 (`::` + zéros non-significatifs)
- [ ] Calculer l'EUI-64 d'une adresse MAC en 3 étapes
- [ ] Distinguer SLAAC / DHCPv6 stateless / DHCPv6 stateful (flags M/O)
- [ ] Configurer OSPFv3 sur une interface Cisco (pas de `network` !)

**Cloud et WAN avancé**
- [ ] Concevoir un VPC AWS avec subnets publics/privés et Security Groups
- [ ] Distinguer Security Group (stateful) et NACL (stateless) en AWS
- [ ] Expliquer overlay vs underlay et leur rôle dans SD-WAN
- [ ] Configurer un spoke DMVPN et comprendre le rôle de NHRP

---

**Score auto-évalué :** _____ compétences sur 28 maîtrisées

---

## PARTIE 2 — MES POINTS FORTS TECHNIQUES

> Identifiez les 3 domaines où vous vous sentez le plus solide. Justifiez avec un exemple concret.

**Point fort 1 :**

Domaine : _________________________________

Exemple concret : __________________________
_________________________________________________________________________

**Point fort 2 :**

Domaine : _________________________________

Exemple concret : __________________________
_________________________________________________________________________

**Point fort 3 :**

Domaine : _________________________________

Exemple concret : __________________________
_________________________________________________________________________

---

## PARTIE 3 — MES AXES DE PROGRESSION

> Identifiez 2 domaines où vous avez encore des lacunes. Pour chacun, écrivez ce qui vous pose problème et ce que vous comptez faire.

**Lacune 1 :**

Domaine : _________________________________

Ce qui me pose problème : __________________
_________________________________________________________________________

Ce que je vais faire : ______________________
_________________________________________________________________________

**Lacune 2 :**

Domaine : _________________________________

Ce qui me pose problème : __________________
_________________________________________________________________________

Ce que je vais faire : ______________________
_________________________________________________________________________

---

## PARTIE 4 — CE QUE J'AI COMPRIS DE LA DÉMARCHE INGÉNIEUR

> Au-delà de la technique, E31 a développé des habitudes de pensée. Cochez celles que vous avez intégrées :

- [ ] **Tester avant de diagnostiquer** : ping d'abord, config ensuite
- [ ] **Méthode descendante** : couche 1 → couche 2 → couche 3 avant de chercher dans les protocoles
- [ ] **Documenter avant d'exécuter** : plan de test avec résultat attendu avant d'injecter une panne
- [ ] **Vérifier, pas supposer** : `show` après chaque commande de configuration
- [ ] **Penser en couches** : HSRP (passerelle LAN) ≠ OSPF (routage inter-sites) — chaque protocole a son périmètre
- [ ] **Anticiper les pannes** : si je configure ça, que se passe-t-il si ce lien tombe ?
- [ ] **Lire les logs** : la sortie de `show` contient toujours l'indice, il faut savoir où chercher

---

## PARTIE 5 — LE MOT DE LA FIN

> Une phrase pour résumer ce que vous retenez de E31 A2+A3 :

_________________________________________________________________________
_________________________________________________________________________

---

---
# ═══════════════════════════════════════════════════════════
# FICHE DE BILAN INDIVIDUEL — À REMPLIR PAR LE FORMATEUR
# (Remise à l'apprenti lors de l'entretien individuel)
# ═══════════════════════════════════════════════════════════

**Apprenti : ________________  Formateur : ________________**

---

## PROFIL DE COMPÉTENCES E31 (sur l'ensemble A2+A3)

| **Domaine** | **Niveau observé** | **Évolution sur l'année** |
|---|---|---|
| Adressage IPv4 / VLSM | 🟢 Maîtrisé / 🟡 Fragile / 🔴 Lacune | ↑ Progression / → Stable / ↓ Régression |
| OSPF v2 (single + multi-area) | | |
| ACL étendues | | |
| VPN IPsec site-à-site | | |
| HSRP / VRRP haute disponibilité | | |
| Nagios supervision | | |
| IPv6 (EUI-64, DHCPv6, OSPFv3) | | |
| Cloud networking (AWS/Azure) | | |
| WAN avancé (DMVPN, SD-WAN) | | |
| Troubleshooting méthode | | |
| **Expression orale (soutenance)** | | |
| **Rigueur / Méthode de travail** | | |

---

## 3 POINTS FORTS OBSERVÉS

1. _________________________________________________________________________

2. _________________________________________________________________________

3. _________________________________________________________________________

---

## 2 AXES D'AMÉLIORATION PRIORITAIRES

1. _________________________________________________________________________

2. _________________________________________________________________________

---

## RECOMMANDATION DE POURSUITE D'ÉTUDES

| | **BTS CIEL** | **BTS SIO SISR** | **BTS SIO SLAM** | **Autre** |
|---|---|---|---|---|
| **Recommandé** | ☐ | ☐ | ☐ | ☐ _______ |

**Justification :**

_________________________________________________________________________
_________________________________________________________________________

---

## MOT DU FORMATEUR

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

**Signature formateur : ________________  Date : ________________**

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
