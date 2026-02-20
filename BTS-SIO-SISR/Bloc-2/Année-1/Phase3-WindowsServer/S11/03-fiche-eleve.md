# Semaine 11 (S11) - BLOC 2
## "Windows Server, Active Directory et Structure d'Annuaire"

---

## 📚 FICHE DE COURS ÉLÈVE
### "Windows Server, Active Directory et Structure d'Annuaire"

*Version 1.0 – BTS SIO SISR – Semestre 1 – Semaine 11*

---

### I. Windows Server : Vue d'Ensemble

#### A. Rôle d'un Serveur Windows

Un **serveur** est un ordinateur (physique ou virtuel) qui fournit des **services** à d'autres machines (les clients). Windows Server est le système d'exploitation de Microsoft conçu pour ce rôle.

**Services typiques d'un Windows Server :**

| **Service** | **Rôle Windows Server** | **Fonction** |
|-------------|------------------------|--------------|
| Annuaire réseau | Active Directory Domain Services (AD DS) | Centralise les comptes, authentification |
| Attribution d'IP | DHCP Server | Distribue les configurations réseau |
| Résolution de noms | DNS Server | Traduit noms ↔ IP |
| Partage de fichiers | File and Storage Services | Partages réseau |
| Impression réseau | Print and Document Services | Imprimantes partagées |
| Web intranet | IIS (Internet Information Services) | Sites web internes |
| VPN | Routing and Remote Access | Accès distant sécurisé |
| Mises à jour | WSUS | Distribution des MAJ Windows en interne |

---

#### B. Éditions de Windows Server

| **Édition** | **Cible** | **Particularité** |
|-------------|-----------|-------------------|
| **Essentials** | TPE (≤25 utilisateurs, ≤50 appareils) | AD intégré, pas de CAL requises |
| **Standard** | PME, environnements non intensifs | 2 VMs incluses avec virtualisation |
| **Datacenter** | Grandes entreprises, cloud, virtualisation intensive | VMs illimitées, toutes fonctionnalités |
| **Azure Edition** | Cloud hybride Microsoft Azure | Fonctionnalités cloud-native |

**Pour les TP BTS SIO :** Windows Server 2022 **Evaluation** (180 jours, gratuit, fonctionnellement identique à Standard).

---

#### C. Modes d'Installation : Core vs Desktop Experience

| **Mode** | **Interface** | **RAM** | **Usage** |
|----------|---------------|---------|-----------|
| **Server Core** | CLI uniquement (pas de bureau) | ~1 Go | Production (sécurité renforcée) |
| **Desktop Experience** | Avec interface graphique (bureau classique) | ~2 Go | Apprentissage, administration visuelle |

**En TP : Desktop Experience** — interface graphique, plus accessible.

---

#### D. Post-Installation Indispensable

Après installation, **avant** tout rôle, configurer :

1. **Nom d'hôte** : `SRV-AD-TECHPRO` (descriptif, court, sans espaces)
   - *Paramètres* → *Système* → *Renommer ce PC*

2. **Adresse IP fixe** : Obligatoire pour un serveur (AD, DNS, DHCP ne fonctionnent pas bien avec DHCP)
   - IPv4 statique, masque, passerelle, **DNS pointant sur lui-même**

3. **Mises à jour Windows** : Effectuer les MAJ critiques avant la promotion DC

4. **Paramètres régionaux** : Langue, fuseau horaire, clavier (souvent en QWERTY par défaut)

---

#### E. Le Gestionnaire de Serveur (Server Manager)

L'interface centrale d'administration de Windows Server. Lancé automatiquement au démarrage.

**Onglets principaux :**
- **Tableau de bord** : Vue d'ensemble de l'état des rôles
- **Serveur local** : Paramètres du serveur (nom, IP, pare-feu, WER…)
- **Tous les serveurs** : Gérer plusieurs serveurs depuis une seule console
- **Gérer → Ajouter des rôles et fonctionnalités** : Installer les rôles

---

### II. Active Directory : Concepts Fondamentaux

#### A. Pourquoi Active Directory ?

**Sans AD (groupe de travail / workgroup) :**
- Chaque PC a ses propres comptes locaux
- 50 PCs = 50 × comptes à créer/gérer
- Mot de passe changé sur un PC ≠ changé sur les autres
- Pas de politique centralisée (longueur MDP, verrouillage…)

**Avec AD (domaine) :**
- Un serveur centralisé gère **tous** les comptes
- Un compte unique pour tous les PCs du domaine
- Administration centralisée des politiques de sécurité
- Authentification unique (SSO – Single Sign-On)

---

#### B. La Hiérarchie AD : Forêt, Arbre, Domaine

```
╔══════════════════════════════════════════════════════════╗
║  FORÊT (Forest)                                          ║
║  = Ensemble de domaines partageant le même schéma AD     ║
║  = Périmètre de sécurité ultime                          ║
║                                                          ║
║  ┌──────────────────────────────────────────────────┐    ║
║  │  ARBRE (Tree)                                    │    ║
║  │  = Ensemble de domaines partageant un espace DNS │    ║
║  │                                                  │    ║
║  │  ┌────────────────────┐                          │    ║
║  │  │  DOMAINE RACINE    │ techpro.local            │    ║
║  │  │  (Root Domain)     │                          │    ║
║  │  └─────────┬──────────┘                          │    ║
║  │            │                                     │    ║
║  │  ┌─────────┴──────────┐                          │    ║
║  │  │  DOMAINE ENFANT    │ paris.techpro.local       │    ║
║  │  └────────────────────┘                          │    ║
║  └──────────────────────────────────────────────────┘    ║
║                                                          ║
║  + Autre arbre : filiale2.com (même forêt, DNS différent)║
╚══════════════════════════════════════════════════════════╝
```

**Pour 99% des PME : 1 forêt = 1 arbre = 1 domaine.** La complexité multi-domaines concerne les grandes organisations.

---

#### C. Les Unités Organisationnelles (OU)

Une **OU** (Organizational Unit) est un **conteneur** dans un domaine AD. Elle sert à :
- **Organiser** les objets (utilisateurs, ordinateurs, groupes) selon la structure de l'entreprise
- **Déléguer** l'administration (ex : le responsable RH administre l'OU RH)
- **Appliquer des GPO** (stratégies de groupe) à un périmètre précis

**Analogie :** Une OU est un **dossier** dans l'explorateur Windows. On peut imbriquer des OU dans des OU (sous-dossiers).

**Ce qu'une OU N'EST PAS :**
- Une OU n'est **pas** un groupe de sécurité : les membres d'une OU n'héritent pas automatiquement des mêmes droits
- Une OU ne peut **pas** être utilisée directement pour les permissions NTFS (seuls les groupes le peuvent)

**Structure OU recommandée :**

```
techpro.local
│
├── OU_UTILISATEURS
│   ├── OU Direction
│   ├── OU Informatique
│   │   ├── OU Réseau
│   │   └── OU Développement
│   ├── OU Commercial
│   └── OU RH
│
├── OU_ORDINATEURS
│   ├── OU Postes-Direction
│   ├── OU Postes-Informatique
│   └── OU Postes-Commercial
│
└── OU_GROUPES
    ├── GRP_Direction
    ├── GRP_Informatique
    └── GRP_Commercial
```

**Bonne pratique :** Séparer les utilisateurs, les ordinateurs et les groupes dans des OU distinctes, même si c'est plus verbeux. Cela facilite l'application des GPO.

---

#### D. Les Objets Active Directory

| **Objet** | **Icône MMC** | **Description** | **Attributs principaux** |
|-----------|---------------|-----------------|--------------------------|
| **Utilisateur** (User) | 👤 | Compte d'une personne | SAMAccountName, UPN, mot de passe, service, email… |
| **Ordinateur** (Computer) | 🖥️ | Poste ou serveur joint au domaine | Nom, OS, date de dernière connexion |
| **Groupe** (Group) | 👥 | Regroupement d'utilisateurs et/ou d'ordinateurs | Type (sécurité/distribution), étendue (global/domain local/universel) |
| **OU** | 📁 | Conteneur pour organiser les objets | Nom, GPO liées |
| **Contact** | 📇 | Personne externe (pas de compte) | Email, téléphone |
| **Imprimante partagée** | 🖨️ | Imprimante publiée dans l'annuaire | Nom, localisation |

---

#### E. Le Compte Utilisateur AD

Le compte AD d'un utilisateur contient :

```
Objet Utilisateur : Jean Martin
├── Identité
│   ├── Prénom : Jean
│   ├── Nom : Martin
│   ├── Nom complet : Jean Martin
│   ├── SAMAccountName : j.martin           ← Login réseau (TECHPRO\j.martin)
│   └── UPN : j.martin@techpro.local        ← Login format email
│
├── Authentification
│   ├── Mot de passe (hashé, jamais en clair)
│   ├── Expiration du mot de passe : 90 jours
│   └── Compte activé/désactivé/verrouillé
│
├── Profil
│   ├── Chemin du profil : \\SRV-AD\Profiles\j.martin
│   ├── Script de connexion : logon.bat
│   └── Lecteur réseau : H: → \\SRV-AD\Users\j.martin
│
└── Appartenance aux groupes
    ├── GRP_Informatique
    └── GRP_All_Users
```

**SAMAccountName :** Limité à 20 caractères. Convention courante : `p.nom` (première lettre prénom + point + nom). Doit être unique dans le domaine.

**UPN (User Principal Name) :** Format email (`login@domaine`). Utilisé pour l'authentification dans les applications modernes.

---

#### F. Les Groupes Active Directory

Les groupes AD servent à **regrouper des utilisateurs** pour leur attribuer des droits collectivement.

##### Type de Groupe

| **Type** | **Usage** |
|----------|-----------|
| **Sécurité** | Attribuer des droits/permissions (NTFS, partages, GPO) |
| **Distribution** | Listes de diffusion email (Exchange/Outlook) uniquement |

**→ En BTS SIO SISR : presque toujours des groupes de sécurité.**

##### Étendue du Groupe

| **Étendue** | **Membres possibles** | **Peut être utilisé pour les droits dans…** | **Cas d'usage** |
|-------------|----------------------|----------------------------------------------|-----------------|
| **Domaine Local** | Utilisateurs, groupes globaux, groupes universels du domaine ou d'autres domaines | Le domaine local uniquement | Attribuer des droits sur des ressources locales |
| **Global** | Utilisateurs du même domaine uniquement | N'importe quel domaine de la forêt | Regrouper des utilisateurs par rôle/service |
| **Universel** | Utilisateurs et groupes de n'importe quel domaine | N'importe quel domaine de la forêt | Multi-domaines (grandes organisations) |

**Règle simple pour un domaine unique (99% des cas PME) :**
- Créer des **groupes de sécurité globaux** (`GRP_Informatique`, `GRP_Commercial`…)
- Ajouter les utilisateurs dans ces groupes
- Attribuer les droits aux groupes (et non aux utilisateurs directement)

---

#### G. Nommer les Objets AD : Conventions

Une bonne convention de nommage évite les confusions et facilite l'administration.

**Conventions courantes :**

| **Type d'objet** | **Préfixe** | **Exemple** |
|-----------------|-------------|-------------|
| OU Utilisateurs | `OU_` | `OU_Informatique` |
| OU Ordinateurs | `PC_` | `PC_Informatique` |
| Groupes de sécurité | `GRP_` | `GRP_Informatique` |
| Groupes de distribution | `DL_` | `DL_Commercial` |
| SAMAccountName utilisateur | `p.nom` | `j.martin`, `e.petit` |
| Nom d'hôte serveur | `SRV-` | `SRV-AD-01`, `SRV-FICHIER` |
| Nom d'hôte poste client | `PC-` | `PC-COM-01`, `PC-INFO-05` |

---

#### H. La Console ADUC (Active Directory Users and Computers)

La console MMC principale pour administrer AD.

**Accès :**
- `Démarrer` → `Outils d'administration Windows` → `Utilisateurs et ordinateurs Active Directory`
- Ou `dsa.msc` dans Exécuter

**Actions principales (clic droit dans ADUC) :**

| **Action** | **Clic droit sur…** | **Menu** |
|------------|---------------------|----------|
| Créer une OU | Le domaine ou une OU | Nouveau → Unité d'organisation |
| Créer un utilisateur | Une OU | Nouveau → Utilisateur |
| Créer un groupe | Une OU | Nouveau → Groupe |
| Déplacer un objet | L'objet | Déplacer… |
| Réinitialiser MDP | Un utilisateur | Réinitialiser le mot de passe |
| Désactiver un compte | Un utilisateur | Désactiver le compte |
| Ajouter au groupe | Un utilisateur | Ajouter à un groupe |
| Propriétés complètes | N'importe quel objet | Propriétés |

---

### III. Tableau de Correspondance Complet

| **Concept entreprise** | **Objet AD** | **Commande / Console** |
|------------------------|--------------|------------------------|
| Entreprise | Domaine | `dcpromo` / Server Manager |
| Service/Département | OU | ADUC → Nouveau → OU |
| Employé | Utilisateur | ADUC → Nouveau → Utilisateur |
| PC professionnel | Ordinateur | Joint au domaine depuis le PC |
| Équipe/rôle | Groupe (global, sécurité) | ADUC → Nouveau → Groupe |
| Règle de sécurité | GPO (Group Policy Object) | GPMC – S12 |
| Administrateur délégué | Délégation de contrôle | ADUC → Déléguer le contrôle |

---

### IV. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|----------------|
| **Active Directory (AD)** | Service d'annuaire de Microsoft – centralise l'authentification et la gestion des ressources réseau |
| **Contrôleur de domaine (DC)** | Serveur Windows hébergeant la base de données AD et gérant l'authentification |
| **Domaine** | Unité administrative AD identifiée par un nom DNS (ex: techpro.local) |
| **Forêt (Forest)** | Ensemble de domaines partageant un schéma AD commun – périmètre de sécurité ultime |
| **Arbre (Tree)** | Ensemble de domaines partageant un espace de noms DNS continu |
| **OU** | Unité Organisationnelle – conteneur AD pour organiser les objets et appliquer des GPO |
| **Utilisateur (User)** | Objet AD représentant le compte d'une personne |
| **Ordinateur (Computer)** | Objet AD représentant un PC ou serveur joint au domaine |
| **Groupe (Group)** | Objet AD regroupant des utilisateurs/ordinateurs pour leur attribuer des droits collectivement |
| **GPO** | Group Policy Object – stratégie de groupe appliquée à une OU (S12) |
| **SAMAccountName** | Identifiant court de connexion réseau (ex: j.martin) – max 20 caractères |
| **UPN** | User Principal Name – identifiant format email (j.martin@techpro.local) |
| **DSRM** | Directory Services Restore Mode – mode de récupération du DC, protégé par un mot de passe spécifique |
| **Domaine local** | Étendue de groupe : droits applicables dans le domaine local uniquement |
| **Groupe global** | Étendue de groupe : membres du domaine local, droits dans toute la forêt |
| **Promotion DC** | Opération qui transforme un Windows Server en contrôleur de domaine |
| **AD DS** | Active Directory Domain Services – rôle Windows Server hébergeant l'annuaire |
| **ADUC** | Active Directory Users and Computers – console MMC principale d'administration AD |
| **dsa.msc** | Commande pour ouvrir la console ADUC |
| **Niveau fonctionnel** | Version des fonctionnalités AD disponibles (lié à la version des DC du domaine) |

---

### V. Exercices d'Entraînement

#### Exercice 1 : Identifier les Objets AD

Pour chaque élément, dire s'il s'agit d'un Utilisateur, Ordinateur, Groupe, OU ou Domaine :

1. `GRP_Comptabilité` → ?
2. `PC-FIN-08` (machine jointe au domaine) → ?
3. `Service Financier` (conteneur dans AD) → ?
4. `marie.dupont` (login réseau) → ?
5. `finance.entreprise.local` → ?
6. `DL_Newsletter_Clients` → ?
7. `SRV-FILE-01` (serveur de fichiers joint) → ?

---

#### Exercice 2 : Concevoir une Structure OU

L'entreprise **BioMed SARL** (cabinet médical) a la structure suivante :

```
BioMed SARL (50 personnes)
├── Direction Médicale
│   ├── Dr. Lefebvre (médecin généraliste)
│   └── Dr. Rousseau (cardiologue)
├── Administration
│   ├── Claire (secrétariat)
│   └── Marc (comptabilité)
├── Infirmerie
│   ├── Anne (infirmière)
│   └── Pierre (infirmier)
└── Informatique
    └── Thomas (informaticien)
```

1. Proposer la structure OU complète pour ce domaine
2. Proposer les SAMAccountName pour chaque utilisateur
3. Proposer 3 groupes pertinents avec leur type et étendue
4. Quel nom de domaine suggérer ? (justifier)

---

#### Exercice 3 : Questions de Cours

1. Quelle est la différence entre un groupe de sécurité et un groupe de distribution ?
2. Pourquoi faut-il une IP fixe sur le serveur AVANT la promotion DC ?
3. Peut-on appliquer une GPO directement sur un groupe de sécurité ? Et sur une OU ?
4. Quelle est la différence entre SAMAccountName et UPN ?
5. Qu'est-ce que le mot de passe DSRM et à quoi sert-il ?

---

### VI. Auto-évaluation : Suis-je Prêt ?

- [ ] Nommer les 3 éditions principales de Windows Server et leur cible
- [ ] Expliquer la différence Server Core vs Desktop Experience
- [ ] Lister les 4 paramètres à configurer après installation (nom, IP, MAJ, région)
- [ ] Expliquer la hiérarchie Forêt → Arbre → Domaine → OU
- [ ] Différencier OU et Groupe (rôle de chacun)
- [ ] Expliquer SAMAccountName vs UPN
- [ ] Différencier groupe de sécurité vs groupe de distribution
- [ ] Différencier groupe global vs domaine local
- [ ] Installer Windows Server 2022 dans une VM
- [ ] Configurer IP fixe + nom d'hôte post-installation
- [ ] Promouvoir le serveur en contrôleur de domaine (AD DS)
- [ ] Créer des OU dans ADUC
- [ ] Créer des utilisateurs dans une OU avec mot de passe
- [ ] Créer des groupes et y ajouter des utilisateurs

