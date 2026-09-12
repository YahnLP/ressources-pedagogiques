# 🔍 ACTIVITÉ DE DÉCOUVERTE — S4 · 3ᵉ ANNÉE · E31
## « Réseau en kit » — Comprendre SDN par l'absurde

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement
> **Principe** : Avant tout cours sur SDN, tu vas analyser deux situations réseaux contrastées et déduire pourquoi l'une est révolutionnaire.

---

## 🎯 Mise en situation : deux datacenters, deux approches

> **Datacenter A — Traditionnel (2010)**
> 300 switches Cisco configurés un par un.
> Chaque switch décide lui-même comment acheminer les paquets.
> Chaque VLAN nécessite 300 commandes manuelles.
> Chaque switch a son propre firmware, sa propre table de routage, sa propre logique.
>
> **Datacenter B — SDN (2024)**
> 300 switches "stupides" sans configuration locale.
> Un serveur central reçoit les requêtes de flux et dit à chaque switch quoi faire.
> Un nouveau VLAN = 1 commande sur le serveur central → propagé en 2 secondes.
> Les switches sont interchangeables comme des disques durs.

---

## 📋 Document 1 — Architecture du Datacenter B (SDN)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   ┌───────────────────────────────────────────────────────────────┐    │
│   │            APPLICATION DE GESTION RÉSEAU                      │    │
│   │         (interface web, scripts Python, ERP)                  │    │
│   └─────────────────────┬─────────────────────────────────────────┘    │
│                         │                                               │
│                    REST API (JSON)                                      │
│                         │                                               │
│   ┌─────────────────────▼─────────────────────────────────────────┐    │
│   │                  CONTRÔLEUR SDN                                │    │
│   │            (serveur Linux, logiciel OpenDaylight)              │    │
│   │     ┌──────────────────────────────────────────────┐          │    │
│   │     │  Vue globale du réseau · Politiques centrales│          │    │
│   │     │  Calcul des chemins · Gestion des flux       │          │    │
│   │     └──────────────────────────────────────────────┘          │    │
│   └─────────┬─────────────────────────────┬───────────────────────┘    │
│             │                             │                             │
│       OpenFlow (TCP 6633)          OpenFlow (TCP 6633)                  │
│             │                             │                             │
│   ┌─────────▼──────┐           ┌──────────▼──────┐                    │
│   │  SWITCH SDN 1  │           │  SWITCH SDN 2   │     × 298          │
│   │  (Open vSwitch)│           │  (Open vSwitch) │                    │
│   │  Flow Table    │           │  Flow Table     │                    │
│   └────────────────┘           └─────────────────┘                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 PARTIE 1 — Analyser l'architecture SDN (12 min)

**Question 1.1** — L'architecture SDN montre 3 couches distinctes. Nomme-les et décris brièvement le rôle de chacune :

```
Couche du haut (Applications) :
Rôle : ______________________________________________________________________

Couche du milieu (Contrôleur) :
Rôle : ______________________________________________________________________

Couche du bas (Switches) :
Rôle : ______________________________________________________________________
```

**Question 1.2** — Dans le Datacenter A (traditionnel), chaque switch Cisco fait DEUX choses simultanément :
- Décider comment acheminer les paquets (calculer les routes, maintenir les tables)
- Physiquement transmettre les paquets d'un port à l'autre

Dans le Datacenter B (SDN), ces deux fonctions sont-elles encore dans le même équipement ?

```
Dans le Datacenter B :
  Qui décide comment acheminer les paquets ? ____________________________________
  Qui transmet physiquement les paquets ? ______________________________________
  Ces deux fonctions sont : ☐ toujours dans le même équipement ☐ séparées
```

**Question 1.3** — L'interface entre les applications et le contrôleur utilise "REST API (JSON)". L'interface entre le contrôleur et les switches utilise "OpenFlow".

Propose un nom pour chacune de ces interfaces selon leur direction :

```
Interface contrôleur → Applications (vers le haut) : ____________________________
Interface contrôleur → Switches (vers le bas)       : ____________________________

Indice : les mots "north" (nord) et "south" (sud) sont utilisés en SDN...
```

---

## 📋 Document 2 — Comparaison de flux réseau

> **Scénario** : H1 veut envoyer un paquet à H2.

```
RÉSEAU TRADITIONNEL :
  H1 envoie le paquet
  → Switch S1 consulte sa propre table MAC/ARP
  → S1 décide seul de forwarder vers S2
  → S2 consulte sa propre table, forwarde vers H2
  → Chaque switch a sa logique indépendante

RÉSEAU SDN :
  H1 envoie le paquet
  → Switch S1 reçoit le paquet
  → S1 consulte sa Flow Table : règle pour ce flux présente ?
      SI OUI  → applique la règle (forward, drop, modifier, etc.)
      SI NON  → envoie le paquet au CONTRÔLEUR (Packet-In message)
  → Contrôleur analyse : "Ce flux doit passer de H1 à H2 via S1→S2→H2"
  → Contrôleur installe les règles sur S1 ET S2 (Flow-Mod messages)
  → Les paquets suivants de ce flux sont traités directement par les switches
```

**Question 2.1** — Dans le réseau SDN, que se passe-t-il pour le PREMIER paquet d'un flux jamais vu ?

```
Le switch S1 consulte sa Flow Table et : ☐ trouve une règle ☐ ne trouve pas de règle
Il envoie alors le paquet au : _________________________ via un message de type ___
```

**Question 2.2** — Pour les paquets SUIVANTS du même flux, le contrôleur est-il encore consulté ?

```
☐ Oui — chaque paquet passe par le contrôleur
☐ Non — les règles sont installées sur les switches, les paquets sont traités localement
Avantage de ce fonctionnement : _______________________________________________
```

**Question 2.3** — Si le contrôleur tombe en panne, que se passe-t-il pour les flux déjà établis (règles déjà installées) vs les nouveaux flux jamais vus ?

```
Flux déjà établis (règles dans la Flow Table) : ___________________________________
Nouveaux flux inconnus : _______________________________________________________
Conclusion sur la criticité du contrôleur : _______________________________________
```

---

## 📋 Document 3 — NFV (Network Functions Virtualization)

> **Contexte** : En 2015, une entreprise veut sécuriser son réseau.
>
> **Approche traditionnelle :**
> Elle achète un pare-feu Cisco ASA physique (3 000 €), un load balancer F5 physique (8 000 €),
> un IDS Sourcefire physique (5 000 €). Total : 16 000 € de matériel.
> Délai de livraison : 3 semaines.
>
> **Approche NFV :**
> Elle installe un hyperviseur (VMware ESXi) sur un serveur standard.
> Elle déploie 3 VMs : Cisco CSRv (pare-feu virtuel), F5 BIG-IP VE (LB virtuel), Snort (IDS virtuel).
> Coût logiciel : abonnements. Délai : 2 heures.

**Question 3.1** — Quelle est la différence fondamentale entre une fonction réseau physique et une VNF (Virtual Network Function) ?

```
Physique : la fonction réseau est liée à ____________________________________
NFV      : la fonction réseau est _________________ sur un ________________
```

**Question 3.2** — Cite 2 avantages de NFV par rapport aux appliances physiques :

```
Avantage 1 : _________________________________________________________________
Avantage 2 : _________________________________________________________________
```

**Question 3.3** — Cite 1 inconvénient ou risque de NFV :

```
Inconvénient : _______________________________________________________________
```

---

## 🏁 Bilan

```
SDN (Software-Defined Networking) sépare :
  LE PLAN DE CONTRÔLE → qui décide : ________________________________________
  LE PLAN DE DONNÉES   → qui transmet : _____________________________________

Le composant central de SDN est le : _________________________________________
Il communique vers le bas (switches) via le protocole : ______________________
Il communique vers le haut (applications) via des : __________________________

NFV = virtualiser les ______________________ sur des serveurs standard
      au lieu d'utiliser des __________________ dédiées

Avantage commun à SDN et NFV : _____________________________________________
```

> ✅ Tu viens de comprendre l'essence de SDN et NFV par déduction.
> Le cours va maintenant préciser les concepts, les protocoles et les cas d'usage.

---

## 📎 Pour l'enseignant — Réponses

**1.2** : Plan de contrôle → Contrôleur (centralisé) · Plan de données → Switches (distribués) · Séparés

**1.3** : Northbound API (vers le haut) · Southbound API (vers le bas)

**2.1** : Ne trouve pas de règle → envoie au contrôleur via Packet-In

**2.2** : Non, les règles sont installées → traitement local. Avantage : performance (pas d'aller-retour contrôleur pour chaque paquet)

**2.3** : Flux établis → continuent (règles dans la flow table) · Nouveaux flux → bloqués ou traitement par défaut · Contrôleur est un point de défaillance unique (SPOF)

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S4*
*Compétences : S6.1 · S6.2 · S6.3*
