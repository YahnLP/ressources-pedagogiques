# ★ EXAMEN BLANC E31 — SUJET OFFICIEL
## Infrastructure Multi-sites : NEXALINK · Simulation CCF 3h

---

> **⏱️ DURÉE : 3 HEURES**
> **Début : ___________ · Fin : ___________**
> **Autorisé** : calculatrice · Cisco Packet Tracer
> **Interdit** : fiches, notes, Internet, aide d'autrui
> **Fichier PT** : `S16_E31_Examen_Blanc_DEPART.pkt`

---

**Nom** : ___________________________ **Prénom** : ___________________________
**Groupe** : ___________________________ **Date** : ___________________________

---

## 🏢 Contexte professionnel

> **NEXALINK** est une entreprise de conseil informatique qui fusionne ses deux sites historiques.
>
> **Site LYON** (siège social) : 80 collaborateurs · services Direction, Commercial, IT
> **Site MARSEILLE** (agence) : 35 collaborateurs · services Technique, Support
>
> Vous êtes chargé(e) du déploiement complet de la nouvelle infrastructure réseau
> répondant aux exigences du cahier des charges ci-dessous.
>
> **Livrable attendu** : infrastructure PT fonctionnelle + dossier technique

---

## PARTIE A — Analyse et conception (/30 pts · 45 min conseillés)

### A1 — Plan d'adressage IP (/18 pts)

> NEXALINK dispose du bloc **10.20.0.0/16**. Le responsable technique impose :

| Réseau | Utilisation | Capacité requise |
|---|---|---|
| VLAN 100 — Direction/Commercial | Postes utilisateurs Lyon | ≥ 80 hôtes |
| VLAN 200 — Technique/Support | Postes utilisateurs Marseille | ≥ 35 hôtes |
| VLAN 300 — VoIP Lyon | Téléphones IP Lyon | ≥ 60 hôtes |
| VLAN 400 — Management | Administration réseau | ≥ 14 hôtes |
| Serveur — DMZ | Serveur web + SFTP | ≥ 6 hôtes |
| WAN Lyon↔Marseille | Lien inter-sites | 2 hôtes exactement |
| Loopback R_LYON | Router-ID OSPF | Hôte unique |
| Loopback R_MARSEILLE | Router-ID OSPF | Hôte unique |

**A1.a** — Propose pour chaque réseau le sous-réseau le plus économique issu de 10.20.0.0/16.
Complète le tableau intégralement :

| Réseau | Sous-réseau | Masque CIDR | Masque | 1ère IP hôte | Dernière IP hôte | Broadcast |
|---|---|---|---|---|---|---|
| VLAN 100 | | | | | | |
| VLAN 200 | | | | | | |
| VLAN 300 | | | | | | |
| VLAN 400 | | | | | | |
| DMZ | | | | | | |
| WAN | | | | | | |
| Lo R_LYON | 10.20.255.1 | /32 | 255.255.255.255 | 10.20.255.1 | 10.20.255.1 | — |
| Lo R_MARSEILLE | 10.20.255.2 | /32 | 255.255.255.255 | 10.20.255.2 | 10.20.255.2 | — |

**A1.b** — Complète le tableau d'équipements avec les adresses IP retenues :

| Équipement | Interface | Adresse IP | Rôle |
|---|---|---|---|
| R_LYON | Gi0/0.100 | | Passerelle VLAN 100 |
| R_LYON | Gi0/0.200 | | Passerelle VLAN 200 *(si applicable)* |
| R_LYON | Gi0/0.300 | | Passerelle VLAN 300 |
| R_LYON | Gi0/0.400 | | Passerelle VLAN 400 |
| R_LYON | Gi0/1 | | WAN vers Marseille |
| R_LYON | Loopback0 | 10.20.255.1/32 | Router-ID |
| R_MARSEILLE | Gi0/0 | | LAN Marseille |
| R_MARSEILLE | Gi0/1 | | WAN vers Lyon |
| R_MARSEILLE | Loopback0 | 10.20.255.2/32 | Router-ID |
| PC_Direction | NIC | | GW : .1 du VLAN 100 |
| PC_Technique | NIC | | GW : .1 du VLAN 200 |
| IP_Phone_1 | | | GW : .1 du VLAN 300 |
| SRV_Web | NIC | | DMZ |

### A2 — Schéma d'architecture (12 pts)

> **Sur les feuilles de brouillon fournies**, dessine le schéma logique de l'infrastructure.

**Éléments obligatoires dans le schéma** :

```
☐ Tous les équipements nommés (R_LYON, R_MARSEILLE, SW_CORE_LYON, SW_ACC_LYON, SW_MARSEILLE)
☐ Les 4 VLANs avec numéros et noms
☐ Les areas OSPF clairement délimitées (Area 0 et Area 1)
☐ Les adresses IP de chaque interface (selon A1)
☐ Le lien WAN avec réseau /30
☐ L'EtherChannel indiqué (entre SW_CORE_LYON et SW_ACC_LYON)
☐ Les connexions des PCs et téléphones IP aux bons ports/VLANs
☐ La DMZ avec le serveur web
```

---

## PARTIE B — Configuration Packet Tracer (/60 pts · 1h45 conseillées)

> Ouvrir `S16_E31_Examen_Blanc_DEPART.pkt`
> La topologie est **pré-câblée** — tous les câbles sont en place.
> Seuls les **hostnames** sont pré-configurés.

### Rappel topologie PT

```
        LYON (Siège)                               MARSEILLE (Agence)

PC_DIR   (VLAN 100) ──┐                            ┌── PC_TECH
IP_Phone (VLAN 300) ──┤                            │
PC_MGMT  (VLAN 400) ──┤                            │
                      [SW_ACC_LYON]                │
                          │ EC (2×Gi)               │
                      [SW_CORE_LYON] ──Gi0/24──Gi0/0──[R_LYON]──WAN──[R_MARSEILLE]──[SW_MARSEILLE]
                          │
                       [R_LYON]
                          │
                       [SRV_Web] (DMZ)
```

---

### Mission B1 — VLANs et infrastructure L2 (/14 pts)

```
Tâche B1.1 — Créer les VLANs sur SW_CORE_LYON et SW_ACC_LYON :
  ☐ VLAN 100 (nom : DIRECTION)
  ☐ VLAN 200 (nom : TECHNIQUE) — même si non utilisé côté Lyon
  ☐ VLAN 300 (nom : VOIP)
  ☐ VLAN 400 (nom : MANAGEMENT)

Tâche B1.2 — Configurer les ports access :
  ☐ PC_Direction → VLAN 100 (sur SW_ACC_LYON)
  ☐ IP_Phone → VLAN 300 (sur SW_ACC_LYON)
  ☐ PC_MGMT → VLAN 400 (sur SW_ACC_LYON)

Tâche B1.3 — Configurer les trunks :
  ☐ SW_ACC_LYON → SW_CORE_LYON : trunk VLANs 100, 200, 300, 400
  ☐ SW_CORE_LYON → R_LYON (Gi0/0) : trunk VLANs 100, 300, 400
```

### Mission B2 — EtherChannel LACP (/8 pts)

```
Tâche B2.1 — EtherChannel entre SW_CORE_LYON et SW_ACC_LYON :
  ☐ 2 liens Gigabit (Gi0/1 et Gi0/2 sur chaque switch)
  ☐ Protocole LACP · Mode active des deux côtés
  ☐ Port-channel 1 configuré en mode trunk · VLANs 100/200/300/400

Vérification obligatoire :
  ☐ show etherchannel summary → Po1(SU), Gi0/1(P), Gi0/2(P)
```

### Mission B3 — Routeurs : adressage et sous-interfaces (/14 pts)

```
Tâche B3.1 — R_LYON :
  ☐ Interface Gi0/0 parente : no shutdown
  ☐ Sous-interface Gi0/0.100 : encapsulation dot1Q 100 · IP selon A1
  ☐ Sous-interface Gi0/0.300 : encapsulation dot1Q 300 · IP selon A1
  ☐ Sous-interface Gi0/0.400 : encapsulation dot1Q 400 · IP selon A1
  ☐ Interface Gi0/1 (WAN) : IP selon A1
  ☐ Interface Loopback0 : 10.20.255.1/32

Tâche B3.2 — R_MARSEILLE :
  ☐ Interface Gi0/0 (LAN Marseille) : IP selon A1
  ☐ Interface Gi0/1 (WAN) : IP selon A1
  ☐ Interface Loopback0 : 10.20.255.2/32

Tâche B3.3 — Vérification :
  ☐ show ip interface brief → toutes les interfaces UP/UP
```

### Mission B4 — OSPF Multi-aires (/16 pts)

```
Architecture OSPF attendue :
  Area 0 (backbone) : R_LYON — VLANs 100/300/400 + Loopback
  Area 1 : R_LYON ↔ R_MARSEILLE (lien WAN) + LAN Marseille

Tâche B4.1 — R_LYON (ABR) :
  ☐ Process OSPF 1 · Router-ID 10.20.255.1
  ☐ VLAN 100 en Area 0 (wildcard correcte !)
  ☐ VLAN 300 en Area 0
  ☐ VLAN 400 en Area 0
  ☐ Loopback0 en Area 0
  ☐ Lien WAN en Area 1
  ☐ passive-interface sur toutes les sous-interfaces LAN
  ☐ passive-interface sur Loopback0

Tâche B4.2 — R_MARSEILLE :
  ☐ Process OSPF 1 · Router-ID 10.20.255.2
  ☐ LAN Marseille en Area 1
  ☐ Lien WAN en Area 1
  ☐ Loopback en Area 1
  ☐ passive-interface LAN

Vérifications :
  ☐ show ip ospf neighbor → R_MARSEILLE en FULL sur R_LYON
  ☐ show ip route sur R_MARSEILLE → routes O IA vers VLAN 100, 300, 400
```

### Mission B5 — QoS VoIP (/8 pts)

```
Tâche B5.1 — Policy-map LLQ sur R_LYON :
  ☐ class-map VOIX : match dscp ef
  ☐ policy-map QOS_WAN : class VOIX → priority percent 30 · class-default → fair-queue
  ☐ Appliquer en sortie sur l'interface WAN (Gi0/1)

Tâche B5.2 — Marquage DSCP sur SW_CORE_LYON :
  ☐ mls qos
  ☐ Port IP_Phone : mls qos trust dscp + switchport voice vlan 300
```

---

## PARTIE C — Tests et documentation (/30 pts · 30 min conseillées)

### C1 — Tableau de tests de validation (/15 pts)

> Complète ce tableau avec les résultats réels obtenus dans PT.

| # | Test | Commande / Action | Résultat attendu | Résultat obtenu | ✓/✗ |
|---|---|---|---|---|---|
| T1 | PC_Direction → PC_Technique | ping 10.20.___.___ | Succès | | |
| T2 | Inter-VLAN : PC_Direction (V100) → IP_Phone (V300) | ping 10.20.___.___ | Succès | | |
| T3 | OSPF adj. R_LYON | show ip ospf neighbor | FULL | | |
| T4 | Routes sur R_MARSEILLE | show ip route | O IA VLAN 100/300/400 | | |
| T5 | EtherChannel opérationnel | show etherchannel summary | Po1(SU), (P) | | |
| T6 | VLAN 300 séparé | show vlan brief | VLAN 300 sur bon port | | |
| T7 | QoS appliquée | show policy-map int Gi0/1 | Classe VOIX visible | | |
| T8 | Sauvegarde | copy run start (tous) | OK | | |

**Score validation : _____ / 8 tests réussis**

### C2 — Justifications techniques (/15 pts)

> Réponds aux 5 questions suivantes (5-8 lignes chacune, en langage professionnel) :

```
Question 1 — Pourquoi OSPF multi-aires plutôt qu'OSPF single-area pour NEXALINK ?
(3 pts)
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

Question 2 — Expliquez le rôle de `passive-interface` dans votre configuration OSPF.
(3 pts)
___________________________________________________________________________
___________________________________________________________________________

Question 3 — Pourquoi l'EtherChannel améliore-t-il la disponibilité entre les switches Lyon ?
(3 pts)
___________________________________________________________________________
___________________________________________________________________________

Question 4 — Justifiez la politique QoS LLQ pour la téléphonie IP.
(3 pts)
___________________________________________________________________________
___________________________________________________________________________

Question 5 — Que faudrait-il ajouter pour sécuriser ce réseau en production ?
(3 pts — réponse libre, attendu : ACL, VPN, WPA3, etc.)
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

---

## 📊 Barème récapitulatif

| Partie | Mission | Points |
|---|---|---|
| **A — Analyse** | A1 Plan adressage | /18 |
| | A2 Schéma | /12 |
| **B — Configuration** | B1 VLANs / L2 | /14 |
| | B2 EtherChannel | /8 |
| | B3 Adressage routeurs | /14 |
| | B4 OSPF | /16 |
| | B5 QoS VoIP | /8 |
| **C — Tests + Doc** | C1 Tableau de tests | /15 |
| | C2 Justifications | /15 |
| **TOTAL PRATIQUE** | | **/120** |
| **ORAL** | Soutenance + questions | **/20** |
| **TOTAL GLOBAL** | (/140 → /20) | **/20** |

---

*Sujet Examen Blanc E31 — CONFIDENTIEL jusqu'à la distribution*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S16*
*Simulation CCF · Durée : 3 heures*
