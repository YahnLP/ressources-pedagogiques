# 📄 GABARIT DAT — À COMPLÉTER
## Document d'Architecture Technique · Infrastructure NEXALINK

---

> **Instructions** : Complète chaque section en utilisant ton infrastructure NEXALINK
> (examen blanc S16) ou ton projet A2. Remplace tous les `[...]` par tes vraies valeurs.
> Longueur cible : 8 à 12 pages une fois complété.

---

## ══════════════════════════════════════════════════
## PAGE DE GARDE
## ══════════════════════════════════════════════════

```
          DOCUMENT D'ARCHITECTURE TECHNIQUE

  Projet   : Infrastructure Réseau [Nom de l'entreprise]
  Référence : DAT-[SIGLE]-001-v1.0
  Version  : 1.0
  Date     : [JJ/MM/AAAA]
  Auteur   : [Nom Prénom]
  Statut   : ☐ Brouillon  ☐ En révision  ☐ Validé

  Historique des révisions :
  ┌─────────┬────────────┬──────────────────────────────────┐
  │ Version │    Date    │ Description                      │
  ├─────────┼────────────┼──────────────────────────────────┤
  │   1.0   │            │ Création initiale                │
  └─────────┴────────────┴──────────────────────────────────┘
```

---

## TABLE DES MATIÈRES

```
1. Contexte et objectifs ............................................. p.2
2. Architecture globale .............................................. p.3
   2.1 Schéma logique
   2.2 Schéma physique
   2.3 Topologie des équipements
3. Plan d'adressage IP ............................................... p.5
4. Configuration des équipements ..................................... p.6
   4.1 Switches
   4.2 Routeurs
   4.3 Services (OSPF, QoS, VPN)
5. Tableau de tests de validation .................................... p.8
6. Procédures d'exploitation ......................................... p.9
   6.1 Procédure de sauvegarde
   6.2 Procédure de modification de configuration
   6.3 Procédure en cas de panne WAN
7. Plan de Reprise d'Activité (PRA) .................................. p.11
Annexes ................................................................ p.13
Glossaire .............................................................. p.14
```

---

## SECTION 1 — CONTEXTE ET OBJECTIFS

### 1.1 Présentation du contexte

> *Décris ici l'entreprise cliente et la situation qui justifie le projet.
> 4-6 lignes. Utilise des termes professionnels.*

```
[L'entreprise ________ est une ________ qui dispose de __ site(s).
Elle a décidé de moderniser son infrastructure réseau afin de...]

[Les besoins identifiés sont :]
[  — ...]
[  — ...]
[  — ...]
```

### 1.2 Objectifs du projet

| Objectif | Priorité | Indicateur de réussite |
|---|---|---|
| Segmenter le réseau par usage (VLANs) | Haute | VLANs 100/300/400 actifs, isolation vérifiée |
| Assurer le routage inter-sites (OSPF) | Haute | Adjacences FULL, ping E2E fonctionnel |
| | | |
| | | |

### 1.3 Périmètre du document

```
Ce document couvre :
  ✓ L'infrastructure réseau du site [Lyon]
  ✓ L'infrastructure réseau du site [Marseille]
  ✓ L'interconnexion WAN entre les deux sites

Hors périmètre :
  ✗ L'infrastructure serveurs (traitée dans un document séparé)
  ✗ La téléphonie PABX legacy
```

---

## SECTION 2 — ARCHITECTURE GLOBALE

### 2.1 Schéma logique

> *Coller ici le schéma logique produit avec Draw.io ou équivalent.*
> *Le schéma doit inclure : équipements nommés, VLANs colorés, areas OSPF,
> adresses IP sur chaque interface, légende.*

```
[INSÉRER LE SCHÉMA LOGIQUE ICI]

Légende obligatoire :
  ■ Bleu    : VLAN 100 — Direction/Commercial
  ■ Rouge   : VLAN 300 — VoIP
  ■ Vert    : VLAN 400 — Management
  ─ ─ ─    : Frontière Area OSPF
  ══════   : Lien EtherChannel LACP
  ——————   : Lien trunk 802.1Q
```

### 2.2 Schéma physique

> *Coller ici le schéma physique ou la vue en rack.*
> *Doit inclure : modèles d'équipements, numéros de ports, types de câbles.*

```
[INSÉRER LE SCHÉMA PHYSIQUE ICI]

Vue rack — Site LYON :
  U1 : [Modèle switch cœur] — SW_CORE_LYON
  U2 : [Modèle switch accès] — SW_ACC_LYON
  U3 : [Modèle routeur] — R_LYON
  U4 : Serveur de sauvegarde TFTP (192.168.__.100)
```

### 2.3 Inventaire des équipements

| Nom | Modèle | Rôle | Site | IP Management |
|---|---|---|---|---|
| R_LYON | Cisco ISR 2901 | Routeur principal + ABR OSPF | Lyon | |
| R_MARSEILLE | Cisco ISR 2901 | Routeur agence | Marseille | |
| SW_CORE_LYON | Cisco Catalyst 3560 | Switch cœur | Lyon | VLAN 400 |
| SW_ACC_LYON | Cisco Catalyst 2960 | Switch accès | Lyon | VLAN 400 |
| SW_MARSEILLE | Cisco Catalyst 2960 | Switch agence | Marseille | |

---

## SECTION 3 — PLAN D'ADRESSAGE IP

### 3.1 Tableau des réseaux

| VLAN/Réseau | Nom | Sous-réseau | CIDR | Masque | Plage utilisables | Passerelle |
|---|---|---|---|---|---|---|
| VLAN 100 | Direction | | /25 | | | |
| VLAN 200 | Technique | | /26 | | | |
| VLAN 300 | VoIP | | /26 | | | |
| VLAN 400 | Management | | /28 | | | |
| DMZ | Serveurs | | /29 | | | |
| WAN | Lyon↔Marseille | | /30 | | | |

### 3.2 Tableau des interfaces

| Équipement | Interface | Adresse IP | Masque CIDR | Rôle |
|---|---|---|---|---|
| R_LYON | Gi0/0.100 | | /25 | Passerelle VLAN 100 |
| R_LYON | Gi0/0.300 | | /26 | Passerelle VLAN 300 |
| R_LYON | Gi0/0.400 | | /28 | Passerelle VLAN 400 |
| R_LYON | Gi0/1 | | /30 | WAN vers Marseille |
| R_LYON | Loopback0 | 10.20.255.1 | /32 | Router-ID OSPF |
| R_MARSEILLE | Gi0/0 | | /26 | LAN Marseille |
| R_MARSEILLE | Gi0/1 | | /30 | WAN vers Lyon |
| R_MARSEILLE | Loopback0 | 10.20.255.2 | /32 | Router-ID OSPF |
| PC_Direction | eth0 | | /25 | Poste utilisateur |
| IP_Phone | | | /26 | Téléphone VoIP |

---

## SECTION 4 — CONFIGURATION DES ÉQUIPEMENTS

> *Pour chaque section, coller les extraits de configuration IOS COMMENTÉS.
> Pas de copier-coller brut — chaque ligne ou bloc doit avoir une explication.*

### 4.1 Configuration switches — SW_CORE_LYON

```cisco
! =====================================================
! SW_CORE_LYON — Cisco Catalyst 3560
! Rôle : Switch de distribution, cœur de réseau Lyon
! =====================================================

! Création des VLANs avec noms significatifs
vlan 100
 name DIRECTION        ! Postes Direction et Commercial
vlan 300
 name VOIP             ! Téléphones IP et équipements VoIP
vlan 400
 name MANAGEMENT       ! Administration réseau (accès restreint)

! EtherChannel LACP vers SW_ACC_LYON
! Deux liens Gi agrégés pour redondance et performance
interface range GigabitEthernet0/1-2
 channel-group 1 mode active    ! Mode actif LACP : initie la négociation

! Configuration du Port-Channel (TOUJOURS sur Po, jamais sur les membres)
interface port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 100,200,300,400
 ! Note : on limite les VLANs autorisés → sécurité et efficacité

[COMPLÉTEZ AVEC VOS VRAIES COMMANDES ET COMMENTAIRES]
```

### 4.2 Configuration routeur — R_LYON

```cisco
! =====================================================
! R_LYON — Cisco ISR 2901
! Rôle : Routeur principal, ABR OSPF (Area 0 + Area 1)
! =====================================================

! Loopback pour le Router-ID — stable même si une interface tombe
interface Loopback0
 ip address 10.20.255.1 255.255.255.255

! Interface parent des sous-interfaces — doit être UP pour que tout fonctionne
interface GigabitEthernet0/0
 no shutdown    ! ← CRITIQUE : l'oublier bloque toutes les sous-interfaces

! Sous-interfaces — chacune porte un VLAN
interface GigabitEthernet0/0.100
 encapsulation dot1Q 100          ! Encapsulation 802.1Q pour VLAN 100
 ip address [VOTRE IP] [MASQUE]   ! Passerelle du VLAN 100

[COMPLÉTEZ AVEC VOS VRAIES COMMANDES ET COMMENTAIRES]

! OSPF — Configuration Multi-Aires
! Area 0 = backbone (réseaux Lyon)
! Area 1 = WAN + Marseille
router ospf 1
 router-id 10.20.255.1
 ! Wildcard = inverse du masque : /25 → 0.0.0.127
 network [RÉSEAU VLAN 100] [WILDCARD] area 0

[COMPLÉTEZ LA CONFIG OSPF AVEC WILDCARDS ET COMMENTAIRES]
```

### 4.3 Configuration QoS VoIP

```cisco
! =====================================================
! QoS LLQ — Priorisation de la téléphonie IP
! Objectif : garantir latence < 150ms et gigue < 30ms
! =====================================================

! Classe de trafic VoIP (DSCP EF = Expedited Forwarding = valeur 46)
class-map match-any VOIX
 match dscp ef    ! Identificaion par le marquage DSCP

! Politique QoS
policy-map QOS_WAN
 class VOIX
  priority percent 30   ! Réservation stricte 30% du débit WAN pour VoIP
 class class-default
  fair-queue            ! Partage équitable pour le reste

! Application en SORTIE sur le lien WAN (là où la congestion peut survenir)
interface GigabitEthernet0/1
 service-policy output QOS_WAN
```

---

## SECTION 5 — TABLEAU DE TESTS DE VALIDATION

| # | Objectif du test | Commande / Action | Résultat attendu | Résultat obtenu | ✓/✗ |
|---|---|---|---|---|---|
| T1 | Connectivité E2E inter-sites VLAN 100 | `ping [IP PC Marseille]` depuis PC_Direction | 5/5 paquets | | |
| T2 | Isolation inter-VLAN sans routeur | `ping [IP VLAN 300]` depuis PC sur VLAN 100 (port non router) | Échec (isolé) | | |
| T3 | Inter-VLAN routing | `ping [IP VLAN 300]` depuis PC_Direction via R_LYON | Succès | | |
| T4 | Adjacence OSPF | `show ip ospf neighbor` sur R_LYON | FULL avec R_MARSEILLE | | |
| T5 | Table de routage complète | `show ip route` sur R_MARSEILLE | O IA vers VLANs Lyon | | |
| T6 | EtherChannel opérationnel | `show etherchannel summary` sur SW_CORE | Po1(SU), (P) | | |
| T7 | Trunk VLANs autorisés | `show interfaces trunk` sur SW_CORE | VLANs 100/300/400 autorisés | | |
| T8 | QoS appliquée | `show policy-map interface Gi0/1` sur R_LYON | Classe VOIX visible + compteurs | | |
| T9 | Sauvegarde TFTP | `copy run tftp:` sur R_LYON | Fichier créé sur serveur | | |
| T10 | Sauvegarde permanente | `show startup-config` sur tous équipements | Config présente en NVRAM | | |

---

## SECTION 6 — PROCÉDURES D'EXPLOITATION

### Procédure 6.1 — Sauvegarde hebdomadaire des configurations

```
┌──────────────────────────────────────────────────────────────────────┐
│ TITRE    : Sauvegarde hebdomadaire — Infrastructure NEXALINK          │
│ Réf.     : PROC-NEXALINK-001                                         │
│ Version  : 1.0 · Date : ____________ · Auteur : _____________        │
│ Fréquence : Chaque vendredi, 22h (hors heures de bureau)             │
├──────────────────────────────────────────────────────────────────────┤
│ OBJECTIF :                                                           │
│   Sauvegarder les running-config de tous les équipements actifs      │
│   vers le serveur TFTP centralisé pour permettre un rollback rapide  │
├──────────────────────────────────────────────────────────────────────┤
│ PRÉREQUIS :                                                          │
│   → Serveur TFTP accessible : ping ____________ depuis chaque routeur│
│   → Fenêtre de maintenance : NON requise (non impactant)             │
│   → Connexion SSH à chaque équipement                                │
├──────────────────────────────────────────────────────────────────────┤
│ ÉTAPES D'EXÉCUTION :                                                 │
│                                                                      │
│   Étape 1 — Vérifier l'accessibilité du serveur TFTP :              │
│   R_LYON# ping ____________                                          │
│   Résultat attendu : 5/5 paquets reçus                               │
│                                                                      │
│   Étape 2 — Sauvegarder R_LYON :                                     │
│   R_LYON# copy running-config tftp:                                  │
│   Adresse serveur : ____________                                     │
│   Nom fichier : R_LYON_running_[AAAA-MM-JJ]_2200.cfg                │
│                                                                      │
│   Étape 3 — Sauvegarder R_MARSEILLE :                                │
│   [COMPLÉTER]                                                        │
│                                                                      │
│   Étape 4 — Vérifier la présence des fichiers sur le serveur TFTP   │
│   [COMPLÉTER]                                                        │
│                                                                      │
│   Étape 5 — Documenter dans le registre de maintenance :             │
│   Date, heure, opérateur, résultat                                   │
├──────────────────────────────────────────────────────────────────────┤
│ VALIDATION :                                                         │
│   ☐ Fichiers présents sur le serveur TFTP                            │
│   ☐ Taille des fichiers non nulle                                    │
│   ☐ Convention de nommage respectée                                  │
├──────────────────────────────────────────────────────────────────────┤
│ ROLLBACK : N/A — Opération non impactante (lecture seule)            │
│ DURÉE ESTIMÉE : 15 minutes · IMPACT : AUCUN                         │
└──────────────────────────────────────────────────────────────────────┘
```

### Procédure 6.2 — Modification d'une configuration en production

```
[À RÉDIGER EN AUTONOMIE selon le même format que 6.1]

Points obligatoires à inclure :
  ✓ Condition préalable : SAUVEGARDE avant toute modification
  ✓ Fenêtre de maintenance : OUI (samedi 22h-06h)
  ✓ Approbation du responsable
  ✓ Plan de rollback détaillé
  ✓ Tests de validation post-modification
```

### Procédure 6.3 — Rétablissement après panne WAN

```
[À RÉDIGER EN AUTONOMIE selon le même format que 6.1]

Points obligatoires à inclure :
  ✓ Symptômes observables (alertes, appels utilisateurs)
  ✓ Diagnostic (show ip route, ping, traceroute)
  ✓ Actions si route flottante active automatiquement
  ✓ Actions si intervention manuelle nécessaire
  ✓ Escalade si non résolu en 30 min
  ✓ RTO cible : _____ minutes
```

---

## SECTION 7 — PLAN DE REPRISE D'ACTIVITÉ (PRA)

### 7.1 Objectifs de reprise

| Composant | RTO (max) | RPO (max) | Criticité |
|---|---|---|---|
| Lien WAN Lyon↔Marseille | | 24h | Haute |
| Routeur R_LYON | | 24h | Critique |
| Switch SW_CORE_LYON | | 24h | Haute |
| Lien EtherChannel | | 24h | Moyenne |

### 7.2 Scénario A — Panne du lien WAN

```
SCÉNARIO : Le lien WAN entre Lyon et Marseille est coupé (panne opérateur)

DÉTECTION :
  → Alerte syslog : R_LYON perd l'adjacence OSPF avec R_MARSEILLE
  → Appels des utilisateurs de Marseille signalant la coupure
  → show ip ospf neighbor : R_MARSEILLE absent

IMPACT :
  → Site Marseille coupé du LAN Lyon et d'Internet
  → Appels VoIP inter-sites interrompus

ACTIONS (à compléter) :
  Minute 0-5  : [DIAGNOSTIC — commandes à exécuter]
  Minute 5-15 : [CONTOURNEMENT éventuel]
  Minute 15+  : [APPEL OPÉRATEUR — procédure escalade]

VALIDATION :
  → [TESTS pour confirmer le rétablissement]

RTO VISÉ : _____ minutes
```

### 7.3 Scénario B — Corruption de configuration d'un routeur

```
SCÉNARIO : R_LYON a une configuration corrompue suite à une modification erronée

SYMPTÔMES :
  → Plus d'accès Internet depuis Lyon
  → show ip route : routes OSPF absentes

ACTIONS :
  1. [DIAGNOSTIC]
  2. [RESTAURATION depuis TFTP]
     copy tftp: running-config
     Source : serveur TFTP ____________
     Fichier : R_LYON_running_[dernière date].cfg
  3. [VALIDATION]

RTO VISÉ : _____ minutes
```

---

## ANNEXES

### Annexe A — Configurations complètes

```
[Coller ici les running-config complets de chaque équipement]
[Sans commentaires — version brute pour référence technique]
```

### Annexe B — Glossaire

| Acronyme | Signification |
|---|---|
| ABR | Area Border Router — routeur OSPF à la frontière de deux aires |
| OSPF | Open Shortest Path First — protocole de routage à état de lien |
| LACP | Link Aggregation Control Protocol — agrégation de liens IEEE 802.3ad |
| QoS | Quality of Service — mécanisme de priorisation du trafic réseau |
| LLQ | Low Latency Queue — file d'attente prioritaire pour la VoIP |
| DSCP | Differentiated Services Code Point — marquage de priorité IP |
| PRA | Plan de Reprise d'Activité |
| RTO | Recovery Time Objective — délai maximum de rétablissement |
| RPO | Recovery Point Objective — perte de données maximale tolérée |
| DAT | Document d'Architecture Technique |
| | |

### Annexe C — Registre des modifications

| Date | Version | Nature de la modification | Auteur | Validé par |
|---|---|---|---|---|
| | 1.0 | Création du document | | |
| | | | | |

---

*Gabarit DAT — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S18*
*À compléter puis exporter en PDF pour le portfolio*
