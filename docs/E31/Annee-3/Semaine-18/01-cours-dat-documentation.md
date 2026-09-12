# 📘 COURS EXPRESS — S18 · 3ᵉ ANNÉE · E31
## Le Document d'Architecture Technique (DAT) : Structure, Normes, Exemples

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences** : C3.1 · C3.2 · C2.3

---

## 🔑 Vocabulaire clé

| Terme | Définition |
|---|---|
| **DAT** | Document d'Architecture Technique — document de référence décrivant une infrastructure IT dans sa totalité |
| **Schéma logique** | Vue fonctionnelle du réseau : adresses IP, VLANs, areas OSPF, flux — sans les détails physiques |
| **Schéma physique** | Vue matérielle : équipements, ports, types de câbles, emplacements rack |
| **Procédure d'exploitation** | Suite d'étapes numérotées pour réaliser une opération de maintenance |
| **PRA** | Plan de Reprise d'Activité — procédures pour rétablir le service après un incident |
| **RTO** | Recovery Time Objective — délai maximal acceptable pour rétablir le service |
| **RPO** | Recovery Point Objective — perte de données maximale tolérée |
| **Baseline** | Configuration de référence — état "normal" de l'infrastructure auquel on revient |
| **Changelog** | Journal des modifications — historique de toutes les évolutions de l'infrastructure |

---

## 1️⃣ — Qu'est-ce qu'un DAT et à quoi sert-il ?

### Le DAT en entreprise

```
SANS DAT :
  → L'admin réseau est irremplaçable (tout est dans sa tête)
  → Chaque intervention prend 2× plus de temps (redécouverte)
  → La moindre modification peut casser ce qu'on ne comprend pas
  → Impossible d'auditer ou de certifier l'infrastructure (ISO 27001, etc.)

AVEC DAT :
  → N'importe quel technicien qualifié peut intervenir
  → Les évolutions sont planifiées et documentées
  → Les incidents sont résolus plus vite (schémas disponibles)
  → Le client ou la direction peut voir ce pour quoi elle paie
```

### Quand est-il produit ?

```
1. LORS D'UN DÉPLOIEMENT : documentation de la nouvelle infrastructure
2. LORS D'UNE MIGRATION : avant/après l'évolution
3. EN COURS D'EXPLOITATION : mis à jour à chaque modification significative
4. LORS D'UN AUDIT : fourni à l'auditeur externe

Dans le cadre de l'E31 : le DAT est le livrable documentaire principal.
Il accompagne le fichier PT et constitue la preuve de C3.1.
```

---

## 2️⃣ — Structure standard d'un DAT

### Les 8 sections d'un DAT professionnel

```
SECTION 1 — Page de garde et informations générales
SECTION 2 — Contexte et objectifs du projet
SECTION 3 — Architecture globale (schémas)
SECTION 4 — Plan d'adressage IP
SECTION 5 — Configuration des équipements (extraits commentés)
SECTION 6 — Tableau de tests de validation
SECTION 7 — Procédures d'exploitation
SECTION 8 — Plan de Reprise d'Activité (PRA)
[ANNEXES]  — Configurations complètes, glossaire, changelog
```

### Section 1 — Page de garde

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│          DOCUMENT D'ARCHITECTURE TECHNIQUE              │
│                                                         │
│    Projet : Infrastructure NEXALINK Multi-sites         │
│                                                         │
│    Client  : NEXALINK SA                                │
│    Version : 1.0                                        │
│    Date    : [JJ/MM/AAAA]                               │
│    Auteur  : [Nom Prénom]                               │
│    Statut  : ☐ Brouillon  ☐ En révision  ☑ Validé      │
│                                                         │
│    Référence : DAT-NEXALINK-001-v1.0                    │
│                                                         │
│    Historique des révisions :                           │
│    v1.0 [date] : Création initiale                      │
│    v1.1 [date] : Ajout procédure PRA                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Section 2 — Contexte et objectifs (exemple rédigé)

```
EXEMPLE DE RÉDACTION PROFESSIONNELLE :

"NEXALINK SA est une entreprise de conseil informatique dont la fusion
avec ALPHATECH a nécessité l'interconnexion de deux sites géographiques :
le siège social de Lyon (80 collaborateurs) et l'agence de Marseille
(35 collaborateurs).

L'infrastructure précédente, basée sur des liaisons WAN non redondantes
et une gestion des VLANs inexistante, ne permettait plus de garantir les
niveaux de service attendus par les équipes métier.

Objectifs du projet :
  — Segmenter le réseau par usage (postes, VoIP, management)
  — Assurer la continuité de service sur le lien inter-sites
  — Prioriser le trafic VoIP pour maintenir la qualité des appels
  — Documenter l'infrastructure pour en faciliter l'exploitation"

CE QU'IL NE FAUT PAS ÉCRIRE :
  "On a fait des VLANs et OSPF pour relier les deux sites."
  → Trop vague, pas de contexte client, pas de justification
```

### Section 4 — Plan d'adressage (format tableau)

```
Mauvaise version (texte libre) :
  "R_LYON a l'adresse 10.20.1.1 sur son interface vers le LAN
  et l'adresse 10.20.100.1 sur son WAN."

Bonne version (tableau) :

| Équipement    | Interface      | Adresse IP         | Masque              | VLAN/Rôle          |
|---------------|----------------|--------------------|---------------------|--------------------|
| R_LYON        | Gi0/0.100      | 10.20.1.1          | 255.255.255.128 /25 | Passerelle VLAN 100|
| R_LYON        | Gi0/0.300      | 10.20.3.1          | 255.255.255.192 /26 | Passerelle VLAN 300|
| R_LYON        | Gi0/0.400      | 10.20.4.1          | 255.255.255.240 /28 | Passerelle VLAN 400|
| R_LYON        | Gi0/1          | 10.20.100.1        | 255.255.255.252 /30 | WAN → Marseille    |
| R_LYON        | Loopback0      | 10.20.255.1        | 255.255.255.255 /32 | Router-ID OSPF     |
| R_MARSEILLE   | Gi0/0          | 10.20.2.1          | 255.255.255.192 /26 | LAN Marseille      |
| PC_Direction  | eth0           | 10.20.1.10         | 255.255.255.128 /25 | VLAN 100           |
...
```

### Section 5 — Configurations commentées (exemple)

```
MAUVAIS EXEMPLE (copier-coller brut) :
  router ospf 1
  router-id 10.20.255.1
  network 10.20.1.0 0.0.0.127 area 0
  network 10.20.3.0 0.0.0.63 area 0

BON EXEMPLE (extraits commentés) :

! ========================================
! CONFIGURATION OSPF — R_LYON
! Rôle : Routeur ABR (Area Border Router)
!   - Area 0 : contient les réseaux Lyon
!   - Area 1 : contient le lien WAN + Marseille
! ========================================
router ospf 1
 ! Identifiant unique stable (Loopback garantit la stabilité)
 router-id 10.20.255.1
 
 ! Annonces Area 0 — réseaux locaux Lyon
 ! Wildcard /25 = 0.0.0.127 (255.255.255.128 inversé)
 network 10.20.1.0 0.0.0.127 area 0   ! VLAN 100 — Direction
 network 10.20.3.0 0.0.0.63 area 0    ! VLAN 300 — VoIP
 
 ! Pas de Hello OSPF vers les équipements utilisateurs finaux
 passive-interface GigabitEthernet0/0.100
 passive-interface GigabitEthernet0/0.300
```

---

## 3️⃣ — Les schémas : logique vs physique

### Schéma logique — ce qu'il doit contenir

```
Éléments OBLIGATOIRES :
  ✓ Tous les équipements réseau (avec leur nom)
  ✓ Les VLANs (numéro + nom + couleur différente par VLAN)
  ✓ Les areas OSPF (délimitées par des zones colorées ou en pointillés)
  ✓ Les adresses IP de chaque interface
  ✓ Les protocoles sur chaque lien (OSPF area X, LACP, trunk...)
  ✓ Les réseaux avec leur notation CIDR
  ✓ Une légende des symboles utilisés

Éléments APPRÉCIÉS :
  ○ Couleurs distinctes pour chaque VLAN
  ○ Icônes standard Cisco (routeur, switch, PC, téléphone IP)
  ○ Annotation des bandes passantes (1G, 10G)
  ○ Flèches directionnelles pour les flux critiques (VoIP, WAN)
```

### Schéma physique — ce qu'il doit contenir

```
Éléments OBLIGATOIRES :
  ✓ Équipements avec modèle (ex: Cisco 2960, Cisco 2901)
  ✓ Numéros de ports (Gi0/0, Gi0/1...)
  ✓ Types de câbles (cuivre, fibre, série)
  ✓ Emplacement physique (salle, rack, étage)

Structure recommandée (vue en rack) :
  ┌─────────────────────────────────────────────┐
  │  RACK LYON — Salle Informatique R.D.C       │
  │  U1  [Patch Panel 24 ports]                 │
  │  U2  [SW_CORE_LYON — Cisco Catalyst 3560]   │
  │  U3  [SW_ACC_LYON — Cisco Catalyst 2960]    │
  │  U4  [R_LYON — Cisco ISR 2901]              │
  │  U5  [Serveur NAS — Backup]                 │
  └─────────────────────────────────────────────┘
```

---

**🖼️ ILLUSTRATION 1 — Schéma logique type**
> *Légende* : Exemple de schéma logique professionnel pour une infrastructure 2 sites. R_LYON et R_MARSEILLE reliés par un lien WAN. Côté Lyon : SW_CORE et SW_ACC avec EtherChannel représenté par un double lien épais. Les VLANs sont représentés par des zones colorées (bleu VLAN 100, rouge VLAN 300, vert VLAN 400). Chaque interface est annotée avec son IP. Les areas OSPF sont délimitées par des contours pointillés (Area 0 englobe Lyon, Area 1 englobe le WAN + Marseille). Légende en bas à gauche.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 4️⃣ — Rédiger des procédures professionnelles

### Structure d'une procédure (rappel S18-2A)

```
┌──────────────────────────────────────────────────────────────┐
│  TITRE : Procédure de [action]                               │
│  Référence : PROC-[CODE]-[NUMÉRO]                            │
│  Version : X.Y · Date : JJ/MM/AAAA · Auteur : [Nom]         │
│  Validé par : [Responsable]                                  │
├──────────────────────────────────────────────────────────────┤
│  1. OBJECTIF                                                 │
│     Décrire en 2-3 lignes ce que fait la procédure           │
├──────────────────────────────────────────────────────────────┤
│  2. PRÉREQUIS                                                │
│     → Qui peut l'exécuter                                   │
│     → Outils nécessaires                                    │
│     → Fenêtre de maintenance requise (oui/non)              │
│     → Sauvegardes préalables (OBLIGATOIRE si config)        │
├──────────────────────────────────────────────────────────────┤
│  3. ÉTAPES D'EXÉCUTION                                       │
│     Chaque étape = 1 action précise + commande + résultat    │
├──────────────────────────────────────────────────────────────┤
│  4. VALIDATION                                               │
│     Tests à effectuer + résultats attendus                   │
├──────────────────────────────────────────────────────────────┤
│  5. ROLLBACK                                                 │
│     Que faire si ça ne fonctionne pas                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 5️⃣ — Le PRA : ce que le jury veut voir

```
Un PRA professionnel répond à 3 questions :
  1. QUE SE PASSE-T-IL si X tombe ?
  2. COMMENT LE DÉTECTE-T-ON ?
  3. QUELLES ACTIONS pour rétablir ? (avec délai RTO)

DEUX SCÉNARIOS MINIMUM pour l'E31 :
  Scénario A : Panne du lien WAN principal
  Scénario B : Corruption de configuration d'un équipement

TABLEAUX RTO/RPO :
  L'examinateur apprécie que ces valeurs soient chiffrées :
  "RTO = 30 minutes" est meilleur que "RTO = rapide"
```

---

## 📌 Les essentiels pour un dossier E31 qui impressionne

> ✅ Page de garde avec référence document, version, statut
> ✅ Table des matières générée automatiquement
> ✅ Schéma logique avec VLANs colorés, areas OSPF, adresses IP
> ✅ Plan d'adressage en **tableau** (jamais en texte libre)
> ✅ Configurations avec **commentaires** (pas juste copier-coller)
> ✅ Justifications précises avec termes techniques
> ✅ 2 procédures minimum + PRA avec 2 scénarios
> ✅ Tableau de tests avec résultats réels (pas "supposés réussis")
> ✅ Pagination + en-tête avec nom du projet et version
> ✅ Glossaire des acronymes si usage de termes techniques

---

*Cours Express DAT — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S18*
*Compétences : C3.1 · C3.2 · C2.3*
