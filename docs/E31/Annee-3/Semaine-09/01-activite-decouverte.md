# 🎲 ACTIVITÉ DÉCOUVERTE – S9 ANNÉE 3 – E31
## « L'Autoroute du Réseau » : Comprendre Pourquoi le WAN Classique a des Limites

---

## 🎯 OBJECTIFS

- ✅ Identifier les limites concrètes du WAN traditionnel (MPLS + VPN IPsec)
- ✅ Faire émerger le besoin de **dissociation** entre infrastructure physique et logique d'acheminement
- ✅ Construire l'analogie underlay/overlay depuis une situation familière
- ✅ Poser les questions auxquelles SD-WAN, DMVPN et VXLAN répondent

---

## ⏱️ DURÉE : 30 min

---

## 🚗 PHASE 1 — L'Analogie de l'Autoroute (8 min)

**Le formateur dessine au tableau :**

```
AUTOROUTE (Infrastructure physique)
══════════════════════════════════════════════════════
  ┌─────────────────────────────────────────────────┐
  │ Voie ordinaire      Voie Bus/Taxi      Voie bus  │
  │ (tout le monde)     (réservée)         (rapide)  │
  └─────────────────────────────────────────────────┘
        ▲                    ▲
        │                    │
   Usage libre          Usage prioritaire
                        (défini par le gestionnaire)
```

**Questions au groupe :**

> *"L'autoroute est la même pour tout le monde (c'est l'underlay). Mais les règles qui décident qui roule sur quelle voie, à quelle vitesse, avec quelle priorité — c'est le gestionnaire du réseau (c'est l'overlay). Si on change les règles de circulation, l'autoroute physique ne change pas."*

| **Autoroute** | **Réseau informatique** |
|---|---|
| Asphalte, béton, ponts | Fibres optiques, câbles, antennes 4G/5G, MPLS |
| Voies dédiées (covoiturage, bus) | Tunnels VPN, canaux QoS |
| Gestionnaire (panneaux, signalisation) | Contrôleur SD-WAN |
| GPS qui choisit l'itinéraire optimal | Politique SD-WAN (SLA, préférence) |
| Accident → déviation automatique | Panne lien → failover automatique |

---

## 💸 PHASE 2 — Le Problème du WAN Classique (10 min)

**Le formateur présente le réseau WAN d'une PME de 10 sites :**

```
Réseau WAN classique — 10 agences + 1 siège :
════════════════════════════════════════════════════
  [SIÈGE]──MPLS──[AGE-1]
         ──MPLS──[AGE-2]
         ──MPLS──[AGE-3]
         ... × 10 agences

Chaque lien MPLS :
  - Contrat opérateur : 500€/mois/agence = 5 000€/mois
  - Délai de changement : 3 à 6 mois (SLA opérateur)
  - Bande passante garantie (QoS) ✅
  - Flexibilité : ❌ très rigide
  - Si 1 lien tombe : 1 agence isolée jusqu'à réparation
════════════════════════════════════════════════════
```

**Groupes de 4 — Identifiez les problèmes :**

| **Problème posé** | **Impact sur l'entreprise** | **Votre solution intuitive** |
|---|---|---|
| Le DSI veut ajouter un lien de secours 4G pour chaque agence | | |
| Le trafic VoIP et Netflix du commercial prennent la même bande passante | | |
| Deux agences veulent communiquer directement (pas via le siège) | | |
| L'opérateur augmente les tarifs MPLS de 20% | | |
| Un lien MPLS tombe : l'agence est coupée 4h | | |

**Réponses attendues :**

| **Problème** | **Limite WAN classique** | **Ce que SD-WAN apporterait** |
|---|---|---|
| Lien 4G de secours | Config manuelle de tous les routeurs | Ajout automatique dans le plan de données |
| VoIP vs Netflix même lien | QoS manuelle par ACL sur chaque routeur | Politique applicative centralisée |
| Communication agence-to-agence | Tunnel IPsec supplémentaire à configurer | DMVPN ou SD-WAN direct path |
| Coût MPLS élevé | Remplacer = 6 mois de projet | SD-WAN mixe MPLS + Internet selon coût/qualité |
| Panne 4h | Pas de failover automatique | SLA monitoring BFD → failover en < 1 seconde |

---

## 🏗️ PHASE 3 — Formalisation Overlay / Underlay (8 min)

**Le formateur conclut avec le schéma fondamental :**

```
┌───────────────────────────────────────────────────────┐
│                    OVERLAY                             │
│  Tunnels IPsec, politiques QoS, routage logique,      │
│  segmentation des flux, sélection de chemin           │
│  → Invisible pour l'infrastructure physique           │
│  → Géré par le contrôleur SD-WAN                     │
├───────────────────────────────────────────────────────┤
│                    UNDERLAY                            │
│  Internet, MPLS, 4G/5G, fibre dédiée                 │
│  → Transport physique des paquets                     │
│  → Géré par les opérateurs télécom                   │
└───────────────────────────────────────────────────────┘

Clé de lecture :
  • L'underlay ne sait pas ce qu'il transporte (il voit des paquets UDP/IP)
  • L'overlay ne sait pas par quelle infrastructure il passe (il utilise la meilleure)
  • Cette séparation = liberté et flexibilité maximales
```

**Questions finales :**

**Q1.** En S7-A2, vous avez configuré un VPN IPsec site-à-site entre Paris et Lyon. Ce tunnel IPsec était-il un overlay ou un underlay ?

___________ car ___________________________________________________________

**Q2.** VXLAN (qu'on va voir dans ce cours) étend des VLANs sur un réseau IP. C'est un overlay ou un underlay ?

___________ car ___________________________________________________________

---

## ✍️ SYNTHÈSE (4 min)

```
┌───────────────────────────────────────────────────────────────────┐
│  Vocabulaire fondamental de la séance :                           │
│                                                                   │
│  UNDERLAY  = infrastructure physique de transport                 │
│              (MPLS, Internet, 4G, fibre)                         │
│                                                                   │
│  OVERLAY   = réseau logique au-dessus de l'underlay              │
│              (tunnels VPN, VXLAN, segmentation SD-WAN)           │
│                                                                   │
│  SD-WAN    = gestion centralisée de l'overlay multi-lien         │
│  DMVPN     = overlay dynamique hub-and-spoke sur GRE + IPsec     │
│  VXLAN     = overlay L2 sur réseau L3 (pour datacenter/cloud)    │
└───────────────────────────────────────────────────────────────────┘
```

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
