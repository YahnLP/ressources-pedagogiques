# 📊 FICHE DE TRAVAIL ÉQUIPE — S16 · 2ᵉ ANNÉE · E31
## Projet A2 DIGITEC : Suivi d'avancement · Planning · Validation

---

> **Équipe** : ___________________________ · ___________________________
> **Date de début** : ___________________________
> **Date de rendu** : ___________________________
> **Fichier .pkt** : A2_DIGITEC_[NomEquipe].pkt

---

## 🗓️ Planning de travail

### Phase 1 — Conception (40 min en S16)

**Objectif** : Plan d'adressage validé + schéma dessiné avant de toucher à Packet Tracer

```
☐ Plan d'adressage IP complet rédigé (tableau ci-dessous)
☐ Schéma logique dessiné (sur papier ou PT avant config)
☐ OSPF Areas déterminées (qui est dans Area 0 ? Area 1 ?)
☐ Checkpoint enseignant validé ← NE PAS COMMENCER LA CONFIG AVANT
```

### Phase 2 — Configuration de base (80 min en S16)

```
☐ Adressage IP sur tous les routeurs (interfaces + Loopback)
☐ VLANs créés sur tous les switches
☐ Trunks configurés
☐ EtherChannel LACP Po1 et Po2 au Siège
☐ OSPF configuré et convergé (show ip ospf neighbor → FULL)
☐ Inter-VLAN routing (sous-interfaces sur R_SIEGE)
```

### Phase 3 — Configuration avancée (50 min en S16 + hors présentiel)

```
☐ Tunnel GRE configuré (show interfaces Tunnel0 → up)
☐ Route flottante (haute dispo WAN Agence B)
☐ QoS LLQ VoIP (policy-map appliquée sur Se0/0/0)
☐ Tests de basculement WAN
```

### Phase 4 — Finalisation hors présentiel

```
☐ Tous les pings du tableau T1-T12 réussis
☐ copy running-config startup-config sur tous les équipements
☐ Dossier technique rédigé (10-15 pages)
☐ Schémas finaux (logique + physique)
☐ Plan de reprise d'activité rédigé
☐ Relecture + mise en page
```

---

## 📐 Plan d'adressage — À compléter en Phase 1

### Équipements et interfaces

| Équipement | Interface | Adresse IP | Masque | VLAN / Commentaire |
|---|---|---|---|---|
| R_SIEGE | Gi0/0.10 | | | VLAN 10 Data |
| R_SIEGE | Gi0/0.20 | | | VLAN 20 VoIP |
| R_SIEGE | Gi0/0.30 | | | VLAN 30 Mgmt |
| R_SIEGE | Se0/0/0 | | | WAN principal |
| R_SIEGE | Se0/0/1 | | | Lien vers R_DC |
| R_SIEGE | Loopback0 | | | Router-ID OSPF |
| R_SIEGE | Tunnel0 | | | Tunnel GRE |
| R_SIEGE_BACKUP | Se0/0/0 | | | WAN secours |
| R_AGENCE_B | Gi0/0 | | | LAN Agence B |
| R_AGENCE_B | Se0/0/0 | | | WAN principal |
| R_AGENCE_B | Se0/0/1 | | | WAN secours |
| R_AGENCE_B | Loopback0 | | | Router-ID OSPF |
| R_AGENCE_B | Tunnel0 | | | Tunnel GRE |
| R_DC | Gi0/0 | | | LAN DC |
| R_DC | Se0/0/0 | | | Lien vers R_SIEGE |
| R_DC | Loopback0 | | | Router-ID OSPF |
| PC_Siege_1 | NIC | | 192.168.10.0/24 | VLAN 10 |
| PC_Siege_2 | NIC | | 192.168.10.0/24 | VLAN 10 |
| IP_Phone_Siege | VoIP | | 192.168.20.0/24 | VLAN 20 |
| PC_B1 | NIC | | 192.168.50.0/24 | Agence B |
| SRV_Web | NIC | 192.168.200.10 | 255.255.255.0 | DC |
| SRV_VoIP | NIC | 192.168.200.20 | 255.255.255.0 | DC |

### Réseaux WAN et passerelles

| Lien | Réseau | Routeur A | Routeur B |
|---|---|---|---|
| WAN Principal | 10.1.2.0/30 | R_SIEGE .__ | R_AGENCE_B .__ |
| WAN Secours | 10.1.3.0/30 | R_SIEGE_BACKUP .__ | R_AGENCE_B .__ |
| Siège ↔ DC | 10.1.4.0/30 | R_SIEGE .__ | R_DC .__ |
| Tunnel GRE | 172.16.0.0/30 | R_SIEGE .__ | R_AGENCE_B .__ |

---

## 🏗️ Schéma logique — À dessiner ici

```
(Dessine l'architecture dans cet espace : équipements, liens, OSPF Areas, VLANs, tunnel)

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

---

## ✅ Tableau de tests de validation — À compléter au fil du projet

| # | Test | Commande | Résultat attendu | ✓/✗ | Notes |
|---|---|---|---|---|---|
| T1 | PC Siège VLAN 10 → PC Agence B | `ping 192.168.50.10` | 5/5 | | |
| T2 | PC Siège → SRV_Web DC | `ping 192.168.200.10` | 5/5 | | |
| T3 | IP_Phone → SRV_VoIP | `ping 192.168.200.20` | 5/5 | | |
| T4 | OSPF R_SIEGE voisins | `show ip ospf neighbor` | FULL ×2 | | |
| T5 | Table R_AGENCE_B complète | `show ip route` | O IA pour tous | | |
| T6 | EtherChannel Po1 actif | `show etherchannel summary` | Po1(SU), (P) | | |
| T7 | Résilience EC | Shutdown Gi0/1, ping | Continue | | |
| T8 | Basculement WAN | Shutdown WAN principal | Ping reprend | | |
| T9 | QoS appliquée | `show policy-map int Se0/0/0` | Classe VOIX visible | | |
| T10 | Tunnel GRE actif | `show interfaces Tunnel0` | up/up | | |
| T11 | PC Agence B → PC Siège VLAN 10 | `ping 192.168.10.10` | 5/5 | | |
| T12 | Sauvegarde configs | `copy run start` (tous) | OK | | |

**Score tests : _____ / 12 tests réussis**

---

## 📝 Journal de bord (à remplir pendant le projet)

### Problèmes rencontrés et solutions

```
Problème 1 : _________________________________________________________________
Solution appliquée : __________________________________________________________
Temps perdu : _________

Problème 2 : _________________________________________________________________
Solution : ___________________________________________________________________
Temps perdu : _________

Problème 3 (si applicable) : _________________________________________________
Solution : ___________________________________________________________________
```

### Répartition des tâches

```
[Nom Membre 1] : _____________________________________________________________

[Nom Membre 2] : _____________________________________________________________

[Nom Membre 3 si applicable] : _______________________________________________
```

---

## 🎯 Auto-évaluation finale (à remplir avant le rendu)

| Critère | Réalisé ✓ | Partiel ~ | Non réalisé ✗ |
|---|---|---|---|
| Plan d'adressage cohérent | | | |
| OSPF convergé (FULL neighbors) | | | |
| EtherChannel Po1 et Po2 fonctionnels | | | |
| Haute disponibilité WAN testée | | | |
| Tunnel GRE opérationnel | | | |
| QoS policy-map appliquée | | | |
| 12/12 tests de validation réussis | | | |
| Dossier technique complet (10+ pages) | | | |
| Schéma logique et physique présents | | | |
| Plan de reprise d'activité rédigé | | | |

**Commentaire d'équipe (ce qui a le mieux/moins bien fonctionné) :**

```
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

---

*Fiche de travail Projet A2 — BAC PRO CIEL | E31 | 2ᵉ année S16*
*Document équipe*
