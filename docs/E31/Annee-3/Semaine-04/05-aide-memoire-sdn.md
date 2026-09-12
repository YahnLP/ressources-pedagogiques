# 🗂️ AIDE-MÉMOIRE SDN / NFV — À PLASTIFIER
## Plan Contrôle/Données · OpenFlow · NFV · Mininet · BAC PRO CIEL · E31 · 3ᵉ année S4

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 🧠 SDN en une ligne

```
SDN = séparer le PLAN DE CONTRÔLE (qui décide)
      du PLAN DE DONNÉES (qui transmet)
      → Contrôle centralisé sur un serveur logiciel
```

---

## 🏛️ Architecture SDN — 3 couches + 2 interfaces

```
┌──────────────────────────────────────┐
│  APPLICATIONS (monitoring, scripts)  │
└──────────────────┬───────────────────┘
                   │ Northbound API (REST/JSON)
┌──────────────────▼───────────────────┐
│  CONTRÔLEUR (ONOS, OpenDaylight)     │
│  Vue globale · Politiques · Chemins  │
└──────────────────┬───────────────────┘
                   │ Southbound API (OpenFlow TCP 6633)
┌──────────────────▼───────────────────┐
│  SWITCHES / DONNÉES (Open vSwitch)   │
│  Transmettent selon les Flow Tables  │
└──────────────────────────────────────┘
```

---

## ⚡ OpenFlow — cycle de vie d'un flux

```
1. Paquet reçu → switch consulte Flow Table
2. TABLE MISS → Packet-In envoyé au contrôleur
3. Contrôleur décide → Flow-Mod installé sur le switch
4. Paquets suivants → traités localement (rapide)
5. Règle expirée (idle/hard timeout) → supprimée
```

---

## 📋 Lire une flow entry

```
priority=200, ip, nw_src=10.0.1.0/24, nw_dst=10.0.2.0/24,
  actions=output:3

priority  = ordre d'évaluation (plus haut = évalué en premier)
ip        = type de paquet correspondant
nw_src    = IP source
nw_dst    = IP destination
output:3  = action : envoyer sur le port 3
drop      = action : jeter le paquet
controller = action : envoyer au contrôleur
```

---

## 🖥️ NFV — Virtualiser les fonctions réseau

```
Physique → VNF
Pare-feu ASA → Cisco CSRv (VM)
Load Balancer F5 → F5 BIG-IP VE (VM)
IDS Sourcefire → Snort/Suricata (VM)
Routeur ISR → Cisco vRouter (VM)

Avantages : coût réduit · déploiement rapide · élasticité
Risque : performances limitées · SPOF si hyperviseur tombe
```

---

## 💻 Commandes Mininet essentielles

```bash
sudo mn                      # Topologie simple (1 sw, 2 hôtes)
sudo mn --topo linear,3      # 3 switches en ligne
sudo mn --topo tree,2,2      # Arbre (4 hôtes)
sudo mn --controller none    # Sans contrôleur

# Dans le CLI Mininet :
mininet> pingall              # Ping all → vérifie connectivité
mininet> h1 ping -c 3 h2     # Ping h1→h2
mininet> dump                 # Infos sur tous les nœuds
mininet> sh ovs-ofctl dump-flows s1  # Flow table de s1

# Installer une règle manuellement :
mininet> sh ovs-ofctl add-flow s1 in_port=1,actions=output:2
mininet> sh ovs-ofctl add-flow s1 priority=200,in_port=1,actions=drop
```

---

## ✅ Comparatif SDN vs Réseau traditionnel

```
               Traditionnel      SDN
Config          Par équipement    Centralisée
Vue réseau      Partielle         Globale
Politique       Manuelle          API REST
Automatisation  Difficile (CLI)   Native (Python)
Résilience      OSPF distribué    Dépend contrôleur (SPOF !)
```

---

## ⚠️ Points clés à ne pas confondre

```
Northbound = vers le HAUT (applications) → REST/JSON
Southbound = vers le BAS (switches) → OpenFlow

Plan contrôle = décide COMMENT acheminer
Plan données  = transmet PHYSIQUEMENT les paquets

NFV ≠ SDN :
  SDN = séparation contrôle/données
  NFV = virtualiser les fonctions réseau
  Ils sont complémentaires mais indépendants
```

---

*Aide-Mémoire SDN/NFV — À plastifier*
*BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S4*
*Compétences S6.1 · S6.2 · S6.3 · C2.2 · C3.1*
