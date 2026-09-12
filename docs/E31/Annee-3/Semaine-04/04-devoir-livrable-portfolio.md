# 📝 DEVOIR & LIVRABLE PORTFOLIO — S4 · 3ᵉ ANNÉE · E31
## SDN · OpenFlow · NFV · Plan Contrôle/Données

---

> **Module** : E31 – Administration Systèmes — SDN et NFV
> **Épreuve visée** : **E31** – Épreuve pratique · CCNA Automation (domaine 6)
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S6.1** | SDN : architecture, 3 plans, contrôleur | /30 |
| **S6.2** | OpenFlow : flow tables, Packet-In, Flow-Mod | /25 |
| **S6.3** | NFV : VNF, avantages, cas d'usage | /20 |
| **C3.1** | Schéma d'architecture SDN annoté | /25 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation

> **Tu es consultant réseau** pour une chaîne hôtelière qui veut moderniser son infrastructure.
> Elle gère 50 hôtels avec chacun 20 switches et 3 routeurs. Actuellement tout est configuré manuellement, ce qui prend des semaines lors d'un déploiement. Le DSI te demande d'évaluer et de présenter l'approche SDN.

---

## 🅰️ PARTIE A — En classe (45 min)

### 🧠 Exercice 1 — Architecture SDN (/30)

**1.a** — Explique en 4 lignes le problème fondamental des réseaux traditionnels que SDN cherche à résoudre : *(6 pts)*

```
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**1.b** — Complète le schéma d'architecture SDN en ajoutant les éléments manquants : *(10 pts)*

```
┌─────────────────────────────────────────────────┐
│               COUCHE _______                    │  ← Nom de la couche
│     Monitoring / Orchestrateur / Scripts        │
└──────────────────────┬──────────────────────────┘
                       │
         ┌─────────────▼──────────────┐
         │  Interface : _____________  │  ← Nom de l'interface
         └─────────────┬──────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│               COUCHE _______                    │  ← Nom de la couche
│     OpenDaylight / ONOS / Cisco ACI             │
│     [ Vue globale · Politiques · Chemins ]      │
└──────────────────────┬──────────────────────────┘
                       │
         ┌─────────────▼──────────────┐
         │  Interface : _____________  │  ← Nom et protocole
         └─────────────┬──────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│               COUCHE _______                    │  ← Nom de la couche
│     Switches · Open vSwitch · Flow Tables       │
└─────────────────────────────────────────────────┘
```

**1.c** — Dans le contexte de la chaîne hôtelière (50 hôtels, 20 switches chacun = 1 000 switches), donne 2 avantages concrets de SDN et 1 inconvénient ou risque : *(9 pts)*

```
Avantage 1 : _________________________________________________________________
_______________________________________________________________________________

Avantage 2 : _________________________________________________________________
_______________________________________________________________________________

Inconvénient / risque : _______________________________________________________
_______________________________________________________________________________
```

**1.d** — Quelle est la différence entre le plan de contrôle et le plan de données ? Donne un exemple pour chacun : *(5 pts)*

```
Plan de contrôle : ___________________________________________________________
  Exemple concret : __________________________________________________________

Plan de données : ____________________________________________________________
  Exemple concret : __________________________________________________________
```

---

### ⚡ Exercice 2 — OpenFlow et flow tables (/25)

**2.a** — Voici une flow entry d'un switch SDN. Décode chaque champ : *(12 pts)*

```
priority=200, ip, nw_src=10.0.1.0/24, nw_dst=10.0.2.0/24,
  actions=output:3
```

| Champ | Valeur | Signification |
|---|---|---|
| priority | 200 | |
| ip | ip | |
| nw_src | 10.0.1.0/24 | |
| nw_dst | 10.0.2.0/24 | |
| actions | output:3 | |

**2.b** — Décris en 4 étapes ce qui se passe quand un switch SDN reçoit un paquet ne correspondant à aucune règle (Table Miss) : *(8 pts)*

```
Étape 1 : ___________________________________________________________________
Étape 2 : ___________________________________________________________________
Étape 3 : ___________________________________________________________________
Étape 4 : ___________________________________________________________________
```

**2.c** — Un switch SDN a 3 règles :

```
Règle 1 : priority=100, in_port=1, actions=output:2
Règle 2 : priority=200, in_port=1, ip, nw_dst=192.168.5.5, actions=drop
Règle 3 : priority=50,  ip, actions=controller
```

Un paquet arrive sur le port 1, destination IP = `192.168.5.5`. Quelle règle s'applique et pourquoi ? *(5 pts)*

```
Règle appliquée : Règle n° ___
Raison : ____________________________________________________________________
Action résultante : __________________________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/50)

### 🖥️ Exercice 3 — NFV dans l'hôtel (/20)

> La chaîne hôtelière possède actuellement 50 × 3 boîtiers physiques dans chaque hôtel :
> un pare-feu Cisco ASA, un contrôleur WiFi physique, et un optimiseur WAN.
>
> Elle envisage de passer à NFV sur des serveurs standard.

**3.a** — Pour chaque appliance, donne son équivalent VNF et explique la différence : *(9 pts)*

| Appliance physique | VNF équivalente (exemple) | Différence principale |
|---|---|---|
| Cisco ASA (pare-feu) | | |
| Contrôleur WiFi physique | | |
| Optimiseur WAN physique | | |

**3.b** — Calcule l'impact du passage à NFV pour la chaîne hôtelière : *(6 pts)*

```
Situation actuelle :
  50 hôtels × 3 boîtiers × 3 000 € moyen = _________ € de matériel
  + délai de livraison : 3 semaines par hôtel
  + maintenance physique par technicien déplacé

Avec NFV :
  50 hôtels × 1 serveur × 4 000 € = _________ €
  + licences logicielles : 50 × 2 000 €/an = _________ €/an
  Économie sur le matériel initiale : _________ €
  Déploiement d'un nouvel hôtel : _____ heures au lieu de _____ semaines
```

**3.c** — Cite 2 risques à considérer avant de migrer vers NFV dans un contexte hôtelier : *(5 pts)*

```
Risque 1 : __________________________________________________________________
Risque 2 : __________________________________________________________________
```

---

### 📐 Exercice 4 — Concevoir l'architecture SDN de l'hôtel (/25)

> L'hôtel ALPHA décide d'adopter SDN + NFV.
> Infrastructure : 20 switches (Open vSwitch), 1 serveur contrôleur (ONOS),
> 1 serveur NFV (hyperviseur KVM avec VMs pare-feu, LB, IDS).
> 3 VLANs : VLAN 10 Chambre, VLAN 20 Personnel, VLAN 30 Gestion.

**4.a** — Dessine le schéma d'architecture complet de l'hôtel ALPHA en incluant : *(15 pts)*
- Les 3 couches SDN avec leurs noms
- Le contrôleur ONOS et les interfaces northbound/southbound
- Les 20 switches (représentés par 3-4 symboles pour la lisibilité)
- Le serveur NFV avec ses 3 VNFs
- Les 3 VLANs avec leurs appareils
- La connexion Internet avec le pare-feu VNF en coupure

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**4.b** — Écris la règle OpenFlow (en syntaxe OVS) qui permettrait de bloquer tout trafic du VLAN 10 (Chambre) vers le VLAN 20 (Personnel) : *(5 pts)*

```
# Supposons : VLAN 10 = 192.168.10.0/24, VLAN 20 = 192.168.20.0/24
# Règle à installer sur le switch de cœur :

ovs-ofctl add-flow s_core ___________________________________________________
```

**4.c** — Si le contrôleur ONOS tombe en panne, quel est l'impact sur les VLANs ? Propose une solution de résilience : *(5 pts)*

```
Impact immédiat : ___________________________________________________________
Impact différé : ____________________________________________________________
Solution de résilience : _____________________________________________________
Terme technique pour ce type de solution : ___________________________________
```

---

## 🏅 Barème global

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Architecture SDN | S6.1 | /30 | ≥ 17 |
| Ex. 2 — OpenFlow flow tables | S6.2 | /25 | ≥ 14 |
| Ex. 3 — NFV analyse | S6.3 | /20 | ≥ 11 |
| Ex. 4 — Schéma + règle + résilience | C3.1 | /25 | ≥ 14 |
| **TOTAL** | | **/100** | **≥ 55** |

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** : Réseau traditionnel = intelligence distribuée sur chaque équipement → configuration répétée × N équipements, pas de vue globale, changement de politique = intervention sur chaque switch, propriétaire constructeur

**1.b** :
```
Couche du haut : Application / Plan d'Application
Interface haute : Northbound API (REST/JSON)
Couche du milieu : Contrôle / Plan de Contrôle
Interface basse : Southbound API (OpenFlow TCP 6633)
Couche du bas : Infrastructure / Plan de Données
```

**1.c** :
- Avantage 1 : déploiement d'un VLAN sur 1 000 switches en 1 commande vs 1 000 sessions SSH
- Avantage 2 : vue globale permet l'optimisation automatique des chemins / QoS centralisée
- Risque : contrôleur = SPOF (point de défaillance unique) — si le contrôleur tombe, nouveaux flux bloqués

## Correction Exercice 2

**2.a** :

| Champ | Signification |
|---|---|
| priority=200 | Priorité 200 (évaluée avant les règles de priorité inférieure) |
| ip | Filtre les paquets IP uniquement (pas ARP, etc.) |
| nw_src | Source IP : tout le réseau 10.0.1.0/24 |
| nw_dst | Destination IP : tout le réseau 10.0.2.0/24 |
| output:3 | Envoyer le paquet sur le port physique numéro 3 |

**2.b** : Table Miss → Switch envoie Packet-In au contrôleur → Contrôleur analyse (src, dst, politique) → Contrôleur envoie Flow-Mod au switch → Switch installe la règle et forwarde le paquet original

**2.c** : Règle 2 (priority=200) s'applique car 200 > 100 > 50 → Action = DROP

## Correction Exercice 3

**3.b** :
- Actuel : 50 × 3 × 3000 = 450 000 € matériel
- NFV : 50 × 4000 = 200 000 € + 50 × 2000 = 100 000 €/an licences
- Économie initiale : 250 000 € · Déploiement : 2h vs 3 semaines

**3.c** : Risque 1 = performances : les VNFs en logiciel sont moins performantes que les ASICs matériels (débit maximal réduit) · Risque 2 = point de défaillance du serveur hyperviseur (concentre plusieurs fonctions critiques)

## Correction Exercice 4

**4.b** :
```
ovs-ofctl add-flow s_core priority=200,ip,nw_src=192.168.10.0/24,nw_dst=192.168.20.0/24,actions=drop
```
(+ règle symétrique pour le trafic de retour si nécessaire)

**4.c** : Impact immédiat = flux déjà établis (règles dans les flow tables) continuent de fonctionner · Impact différé = nouveaux flux inconnus ne peuvent pas être autorisés → blocage progressif du réseau · Solution = contrôleur en haute disponibilité (cluster ONOS à 3 nœuds, ou ONOS actif/passif) · Terme : HA (High Availability) / active-standby clustering

---

*Devoir + Correction — BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S4*
*Épreuve E31 | Compétences S6.1 · S6.2 · S6.3 · C3.1*
