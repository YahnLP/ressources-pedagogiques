# 📋 CAHIER DES CHARGES — PROJET A2
## Infrastructure Multi-sites : OSPF · VPN · Haute Disponibilité · QoS VoIP

---

> **Document client à distribuer aux équipes en début de S16**
> **Projet** : Infra-Corp 2024 — Mise en production du réseau multi-sites de l'entreprise DIGITEC
> **Équipe** : ___________________________ · ___________________________
> **Date de remise du dossier** : ___________________________

---

## 🏢 Présentation du client

> **DIGITEC SAS** est une PME spécialisée dans la maintenance industrielle.
> Elle dispose de **3 sites géographiques** :
>
> - **Siège social** (Lyon) : 40 salariés · services administratif, commercial, IT
> - **Agence B** (Grenoble) : 15 salariés · techniciens terrain
> - **Datacenter** (Lyon, bâtiment B) : 2 serveurs physiques, accès interne uniquement
>
> DIGITEC vient de décider de **moderniser son infrastructure réseau** qui date de 2015.
> Elle vous mandate pour concevoir et déployer la nouvelle architecture.

---

## 🎯 Exigences client (non négociables)

### Exigence 1 — Routage dynamique OSPF multi-aires

> *"Nous voulons un routage qui se répare tout seul si un lien tombe."*

- Configurer **OSPF** sur tous les routeurs
- Area 0 (backbone) : Siège + Datacenter
- Area 1 : Agence B (site distant)
- Le Siège doit voir les réseaux du Datacenter et de l'Agence B via OSPF
- Les tables de routage doivent être complètes sur chaque routeur

### Exigence 2 — Haute disponibilité du WAN Agence B

> *"L'Agence B ne peut pas se permettre d'être coupée du Siège."*

- Deux liaisons WAN entre le Siège et l'Agence B : une principale, une de secours
- **Basculement automatique** sur la liaison de secours si la principale tombe
- Temps de basculement inférieur à 1 minute
- Pas d'intervention manuelle requise pour le basculement

### Exigence 3 — Sécurisation du lien Siège ↔ Agence B

> *"Nos données commerciales qui transitent vers l'Agence B doivent être protégées."*

- Configurer un **tunnel VPN** (GRE over IPsec ou tunnel GRE) entre le Siège et l'Agence B
- Le trafic sensible doit transiter par ce tunnel

### Exigence 4 — Téléphonie IP (VoIP) prioritaire

> *"Nos techniciens de l'Agence B appellent le Siège par Teams/VoIP toute la journée.
> Quand Internet est chargé, les appels se coupent. C'est inacceptable."*

- Déployer une politique **QoS** sur le lien WAN principal (Siège → Agence B)
- Le trafic VoIP doit être priorisé en **Low Latency Queue (LLQ)**
- Bande passante réservée pour la VoIP : **30%** du débit WAN
- Marquage DSCP : VoIP = **EF (DSCP 46)**
- Tester avec des téléphones IP simulés sous Packet Tracer

### Exigence 5 — Redondance en cœur de réseau au Siège

> *"On ne veut plus qu'un seul câble entre nos switches principaux soit un point de défaillance."*

- **EtherChannel LACP** entre les switches de cœur du Siège (min. 2 liens agrégés)
- Configuration en trunk pour tous les VLANs
- Tester la résistance à la panne d'un lien membre

### Exigence 6 — Segmentation réseau par VLAN

> *"Les téléphones ne doivent pas partager le même réseau que les ordinateurs."*

| VLAN | Nom | Réseau suggéré |
|---|---|---|
| VLAN 10 | Data | 192.168.10.0/24 |
| VLAN 20 | VoIP | 192.168.20.0/24 |
| VLAN 30 | Management | 192.168.30.0/24 |
| VLAN 40 | Datacenter | 192.168.200.0/24 |
| VLAN 50 | Agence B | 192.168.50.0/24 |

---

## 📐 Contraintes techniques imposées

### Plan d'adressage WAN

| Lien | Réseau | Équipements |
|---|---|---|
| WAN Principal (Siège↔Agence B) | 10.1.2.0/30 | R_SIEGE .1 / R_AGENCE_B .2 |
| WAN Secours (Siège↔Agence B) | 10.1.3.0/30 | R_SIEGE_BACKUP .1 / R_AGENCE_B .2 |
| Lien Siège↔DC | 10.1.4.0/30 | R_SIEGE .1 / R_DC .2 |
| Tunnel GRE | 172.16.0.0/30 | R_SIEGE .1 / R_AGENCE_B .2 |

### Équipements fournis dans le .pkt

```
SIÈGE :
  R_SIEGE            Routeur Cisco 2901
  R_SIEGE_BACKUP     Routeur Cisco 2901 (lien secours)
  SW_CORE_A          Switch Cisco 3560 (cœur)
  SW_DIST_A1         Switch Cisco 2960 (distribution 1)
  SW_DIST_A2         Switch Cisco 2960 (distribution 2)
  IP_PHONES × 4      Téléphones IP Cisco (VLAN 20)
  PCs × 4            Postes utilisateur (VLAN 10)

AGENCE B :
  R_AGENCE_B         Routeur Cisco 2901
  SW_B               Switch Cisco 2960
  PC_B1, PC_B2       Postes (VLAN 50)
  IP_PHONE_B         Téléphone IP (VLAN 20)

DATACENTER :
  R_DC               Routeur Cisco 2901
  SW_DC              Switch Cisco 2960
  SRV_Web            Serveur (192.168.200.10)
  SRV_VoIP           Serveur Asterisk (192.168.200.20)
```

---

## 📦 Livrables attendus

### Livrable 1 — Fichier Packet Tracer (`.pkt`)

```
✓ Infrastructure complète et fonctionnelle
✓ Tous les pings du tableau de tests réussis
✓ Nommé : A2_DIGITEC_[NomEquipe].pkt
```

### Livrable 2 — Dossier technique (PDF ou DOCX, 10-15 pages)

```
PAGE 1  : Page de garde (projet, équipe, date)
PAGES 2-3 : Présentation de l'architecture choisie
  → Schéma logique annoté (avec VLANs, OSPF areas, tunnel VPN)
  → Schéma physique annoté (équipements, ports, câblage)
PAGES 4-5 : Plan d'adressage IP complet (tableau)
PAGES 6-8 : Documentation des configurations clés
  → Extraits commentés : OSPF, EtherChannel, QoS, VPN
PAGES 9-10 : Tableau de tests de validation
  → Pour chaque test : description, commande utilisée, résultat
PAGE 11 : Plan de reprise d'activité (PRA)
  → Que se passe-t-il si le WAN principal tombe ?
  → Que se passe-t-il si SW_CORE_A tombe ?
PAGE 12 : Synthèse et bilan
  → Ce qui fonctionne, ce qui reste à améliorer
```

### Livrable 3 — Présentation orale (10 min + 5 min questions) — si demandé

```
Slide 1 : Architecture globale (schéma)
Slide 2 : Choix techniques justifiés (pourquoi OSPF ? pourquoi LLQ ?)
Slide 3 : Démonstration live (ping, show ip ospf neighbor, show etherchannel summary)
Slide 4 : Scénario de panne simulée + rétablissement
Slide 5 : Ce qu'on ferait en plus avec plus de temps
```

---

## ✅ Tableau de tests de validation obligatoires

> À compléter dans le dossier technique avec les résultats réels.

| # | Test | Commande | Résultat attendu | Résultat obtenu |
|---|---|---|---|---|
| T1 | PC Siège (VLAN 10) → PC Agence B | `ping 192.168.50.10` | Succès | |
| T2 | PC Siège → Serveur Web DC | `ping 192.168.200.10` | Succès | |
| T3 | IP_Phone Siège → SRV_VoIP | `ping 192.168.200.20` | Succès | |
| T4 | OSPF : adjacences R_SIEGE | `show ip ospf neighbor` | FULL avec R_DC et R_AGENCE_B | |
| T5 | OSPF : table R_AGENCE_B complète | `show ip route` | O et O IA pour tous les réseaux | |
| T6 | EtherChannel : tous ports actifs | `show etherchannel summary` | Po1(SU), ports (P) | |
| T7 | EtherChannel : résilience | Shutdown Gi0/1, re-ping | Ping continue (quelques ms de perte) | |
| T8 | Haute dispo : basculement WAN | Shutdown WAN principal R_SIEGE | Ping reprend via WAN secours | |
| T9 | QoS : policy-map appliquée | `show policy-map interface Se0/0/0` | Classe VOIX avec priority | |
| T10 | Tunnel VPN : tunnel opérationnel | `show interfaces Tunnel0` | Tunnel0 is up, line protocol is up | |
| T11 | PC Agence B → PC VLAN 10 Siège | `ping 192.168.10.10` depuis PC_B1 | Succès via tunnel/OSPF | |
| T12 | Sauvegarde config | `copy run start` sur chaque équipement | OK (message "Building configuration") | |

---

## 📅 Planning du projet

| Phase | Contenu | Durée estimée |
|---|---|---|
| **Conception** (en S16) | Plan d'adressage · schéma · choix technos | 40 min |
| **Config de base** (en S16) | Adressage IP · VLANs · EtherChannel · OSPF | 80 min |
| **Config avancée** (en S16) | VPN · Haute dispo · QoS | 50 min |
| **Tests + Doc** (en S16 + hors présentiel) | Tableau de tests · rédaction dossier | 3h |
| **Finalisation** (hors présentiel) | Mise en page · schémas · relecture | 2h |

---

*Cahier des charges Projet A2 — DIGITEC*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S16*
*Document à distribuer aux équipes*
