# Pack de Formation - Semaine 3 (S3) - BLOC 2
## "Systèmes d'Exploitation : Windows, Comptes Utilisateurs & Permissions"

---

## 📋 FICHE ENSEIGNANT

### Informations Générales

| **Élément** | **Détails** |
|-------------|-------------|
| **Semaine** | S3 - Année 1 |
| **Bloc** | Bloc 2 - Infrastructure, Systèmes & Réseaux |
| **Durée** | 4 heures (1 séance) |
| **Phase** | Phase 1 - Découverte de la machine et fondamentaux absolus |
| **Public** | Apprentis BTS SIO SISR (hétérogène : Bac Pro CIEL + débutants) |
| **Prérequis** | S1 (composants PC), S2 (serveurs, BIOS, installation Windows en VM) |

### Compétences RNCP Visées

| **Code Compétence** | **Libellé** | **Niveau de Maîtrise** |
|---------------------|-------------|------------------------|
| **B1.2** | Mettre à disposition des utilisateurs un service informatique - Gérer des utilisateurs et des droits | **Application** |
| **B2.1** | Administrer les services d'un système d'exploitation serveur | Initiation |
| **B2.2** | Installer, tester et déployer une solution d'infrastructure réseau | Consolidation |
| **B3.1** | Protéger les données à caractère personnel - Gestion des droits d'accès | Initiation |

### Objectifs Pédagogiques

**À l'issue de cette séance, l'apprenant sera capable de :**

1. **Expliquer** le rôle d'un système d'exploitation et ses composants (noyau, interface, gestion des ressources)
2. **Différencier** les principaux OS (Windows, Linux, macOS) et leurs cas d'usage professionnels
3. **Créer et gérer** des comptes utilisateurs locaux dans Windows (création, modification, suppression)
4. **Distinguer** les types de comptes (Administrateur vs Utilisateur standard) et leurs privilèges
5. **Configurer** les permissions NTFS sur fichiers et dossiers (lecture, écriture, modification, contrôle total)
6. **Comprendre** la différence entre comptes locaux et comptes de domaine (introduction Active Directory)
7. **Appliquer** le principe du moindre privilège dans un contexte professionnel

### Prérequis

- Installation de Windows 10/11 en VM (acquis S2)
- Compréhension de la hiérarchie logicielle (Hardware → OS → Applications, vue en S1)
- Navigation dans l'interface Windows

---

### Planning de Séance (4h)

| **Horaire** | **Durée** | **Activité** | **Modalité** | **Objectif** |
|-------------|-----------|--------------|--------------|--------------|
| **00:00 - 00:10** | 10 min | Rappel S1-S2 + Quiz interactif | Collectif | Réactiver les acquis |
| **00:10 - 00:35** | 25 min | **Activité de Découverte** : "Qui peut faire quoi ?" (jeu de rôles) | Groupes de 3-4 | Comprendre la notion de droits |
| **00:35 - 01:05** | 30 min | Apport théorique : Rôle et fonctions d'un OS | Collectif avec projection | Structurer les connaissances |
| **01:05 - 01:35** | 30 min | Apport théorique : Comptes utilisateurs (local vs domaine) | Collectif avec démonstration | Comprendre l'authentification |
| **01:35 - 02:05** | 30 min | **TP Guidé Partie 1** : Création et gestion de comptes locaux Windows | Individuel encadré | Créer des utilisateurs |
| **02:05 - 02:20** | 15 min | **Pause** | - | - |
| **02:20 - 02:50** | 30 min | Apport théorique : Permissions NTFS (ACL, héritage, types de droits) | Collectif avec démonstration | Comprendre les permissions |
| **02:50 - 03:50** | 60 min | **TP Guidé Partie 2** : Configuration des permissions NTFS (scénario entreprise) | Individuel encadré | Appliquer les permissions |
| **03:50 - 04:00** | 10 min | Bilan de séance, QCM rapide, annonce du devoir | Collectif | Valider les acquis |

---

### Matériel Nécessaire

| **Type** | **Quantité** | **Description** |
|----------|--------------|-----------------|
| **VM Windows 10/11** | 1 par apprenant | VM créée en S2 (avec droits admin) |
| **VM Windows Server 2022** | 1 par apprenant | VM créée en S2 (pour comparaison comptes domaine - optionnel S3, obligatoire S4+) |
| **Fiches de rôles** | 1 kit par groupe | Pour l'activité découverte (4 rôles imprimés) |
| **Vidéoprojecteur** | 1 | Pour démonstrations collectives |
| **Documentation papier** | 1 par apprenant | Fiche récapitulative permissions NTFS (tableau synthèse) |

---

### Conseils de Différenciation Pédagogique

#### Pour les apprenants **Bac Pro CIEL** (déjà familiers)

- **Approfondissement** : 
  - Explorer les permissions NTFS avancées (Refuser explicite, propriétaire, audit)
  - Utiliser **PowerShell** pour créer des comptes (`New-LocalUser`, `Add-LocalGroupMember`)
  - Tester les permissions effectives avec `icacls` en ligne de commande
- **Mission complémentaire** : Créer un script PowerShell automatisant la création de 5 comptes utilisateurs d'un coup
- **Questionnement avancé** : 
  - "Comment gérer 200 utilisateurs sans les créer un par un ?"
  - "Pourquoi ne jamais utiliser le compte Administrateur au quotidien ?"

#### Pour les apprenants **débutants**

- **Fiche procédure illustrée** : Guide pas-à-pas avec captures d'écran pour chaque manipulation
- **Validation par étapes** : L'enseignant vérifie la création de chaque compte avant de passer au suivant
- **Binômage stratégique** : Associer avec un Bac Pro CIEL pour le TP permissions (plus complexe)
- **Simplification initiale** : Se concentrer sur les 3 permissions principales (Lecture, Écriture, Modification) avant d'aborder les 6 permissions complètes

#### Pour tous

- **Ancrage professionnel** : Scénario réaliste PME avec 4 services (Direction, Comptabilité, Commercial, Technique)
- **Lien sécurité** : Expliquer que mal gérer les droits = faille de sécurité majeure (principe du moindre privilège)
- **Lien RGPD** : Mentionner que la gestion des droits est une obligation légale (RGPD, Article 32 - mesures de sécurité)

---

### Points de Vigilance

⚠️ **Session Administrateur obligatoire :**
- Pour créer des comptes, l'apprenant doit être connecté en tant qu'**Administrateur** sur sa VM
- Vérifier avant le TP que tous les apprenants ont les droits admin sur leur VM

⚠️ **Mots de passe des comptes créés :**
- Imposer une convention : tous les comptes de TP utilisent le mot de passe **`Azerty123!`** (sauf admin)
- Rappeler que ce mot de passe faible est **uniquement pour le TP** (sensibilisation sécurité)

⚠️ **Permissions NTFS - Risque de se bloquer :**
- Si un apprenant retire ses propres droits sur un dossier, il ne pourra plus y accéder
- **Solution** : Se reconnecter en Administrateur pour reprendre la propriété du dossier
- **Prévention** : Toujours conserver un compte Administrateur accessible

⚠️ **Héritage des permissions :**
- Expliquer clairement que **par défaut, les permissions sont héritées** du dossier parent
- Montrer comment **désactiver l'héritage** si nécessaire (cas spécifiques)

⚠️ **Différence Partage vs NTFS :**
- Ne **PAS** aborder les permissions de partage réseau en S3 (ce sera vu en S5-S6)
- Se concentrer uniquement sur **NTFS local** pour éviter la confusion

---

### Évaluation et Traces d'Apprentissage

| **Type d'évaluation** | **Modalité** | **Critères** |
|-----------------------|--------------|--------------|
| **Diagnostique (Quiz début)** | Questions projetées, réponses levée de main | Vérifier prérequis S1-S2 |
| **Formative (activité découverte)** | Observation des échanges en groupes | Compréhension de la notion de droits |
| **Formative (TP comptes)** | Validation enseignant | 3 comptes créés avec types corrects |
| **Formative (TP permissions)** | Validation enseignant + tests | Permissions correctement configurées (tests d'accès réussis) |
| **Sommative (QCM fin)** | 5 questions rapides (Kahoot ou papier) | Vocabulaire et concepts clés maîtrisés |
| **Livrable Portfolio** | Devoir maison (voir section dédiée) | Documentation de gestion des utilisateurs |

---

### Lien avec le Référentiel Qualiopi

Cette séance répond aux exigences Qualiopi en matière de :

- ✅ **Objectifs pédagogiques clairs et mesurables** (7 objectifs explicites)
- ✅ **Adaptation au public hétérogène** (différenciation Bac Pro CIEL / débutants)
- ✅ **Modalités d'évaluation formalisées** (formative + sommative + portfolio)
- ✅ **Traçabilité des apprentissages** (comptes créés dans VM, captures d'écran)
- ✅ **Lien explicite avec le référentiel RNCP** (B1.2, B2.1, B2.2, B3.1)
- ✅ **Approche par compétences** (scénario professionnel réaliste PME)
- ✅ **Conformité RGPD** (mention du cadre légal de la gestion des droits)

---

### Ressources Complémentaires pour l'Enseignant

**Commandes PowerShell utiles (pour démonstrations) :**
```powershell
# Lister les comptes utilisateurs locaux
Get-LocalUser

# Créer un nouvel utilisateur
New-LocalUser -Name "jdupont" -Password (ConvertTo-SecureString "Azerty123!" -AsPlainText -Force) -FullName "Jean Dupont"

# Ajouter un utilisateur à un groupe
Add-LocalGroupMember -Group "Utilisateurs" -Member "jdupont"

# Voir les permissions NTFS d'un dossier
Get-Acl C:\Data | Format-List

# Afficher les permissions en ligne de commande
icacls C:\Data
```

**Documentation Microsoft :**
- [Gestion des comptes utilisateurs locaux](https://learn.microsoft.com/fr-fr/windows/security/identity-protection/access-control/local-accounts)
- [Permissions NTFS](https://learn.microsoft.com/fr-fr/windows-server/storage/file-server/ntfs-overview)
- [Principe du moindre privilège](https://learn.microsoft.com/fr-fr/windows-server/identity/ad-ds/plan/security-best-practices/implementing-least-privilege-administrative-models)

**Vidéos pédagogiques :**
- "Gestion des utilisateurs Windows 10" - Tutoriel complet (15 min)
- "Comprendre les permissions NTFS" - Explication claire (10 min)
- "Comptes locaux vs comptes de domaine" - Différences (8 min)

**Outils de démonstration :**
- Active Directory Users and Computers (ADUC) - pour montrer rapidement un AD (même non configuré)
- Process Monitor (Sysinternals) - pour montrer les tentatives d'accès refusés en temps réel

---

## 🎯 ACTIVITÉ DE DÉCOUVERTE
### "Qui Peut Faire Quoi ? Le Jeu des Rôles"

### Objectif

Faire comprendre concrètement la notion de **droits d'accès différenciés** et le **principe du moindre privilège** avant l'apport théorique sur les permissions.

---

### Mise en Situation (5 min - Collectif)

> *"Vous travaillez pour **TechPro SARL**, une PME de 20 personnes qui développe des applications mobiles. L'entreprise possède un serveur de fichiers centralisé où sont stockés tous les documents. Malheureusement, la gestion des droits est chaotique : tout le monde a accès à tout !*
>
> *Hier, un stagiaire a accidentellement supprimé le dossier contenant les contrats clients. Le directeur commercial était furieux. La direction vous demande de mettre de l'ordre dans tout ça."*

**Problème à résoudre :** Comment organiser les accès pour que chacun puisse faire son travail, mais **rien de plus** ?

---

### Déroulé (25 minutes)

#### **Phase 1 : Constitution des groupes et distribution des rôles (5 min)**

Former des **groupes de 4 apprenants** (ou 3 si nombre impair).

Chaque groupe représente l'entreprise **TechPro SARL** et reçoit **4 fiches de rôles** :

1. **Directeur Général (Mme Martin)**
2. **Comptable (M. Dubois)**
3. **Développeur (Mlle Leroux)**
4. **Stagiaire Commercial (M. Petit)**

---

#### **Phase 2 : Analyse des besoins par rôle (10 min - en groupes)**

**Consigne :** "Chaque membre du groupe prend un rôle et remplit le tableau suivant pour SON personnage."

**Support distribué : Fiche de travail (voir ci-dessous)**

---

### 📄 Fiche de Travail - "Analyse des Droits d'Accès"

**Dossiers disponibles sur le serveur de fichiers :**

- 📁 **Comptabilité** (factures, bilans, salaires)
- 📁 **Commercial** (contrats clients, devis, prospection)
- 📁 **Développement** (code source, documentations techniques)
- 📁 **Direction** (stratégie, CA, documents confidentiels)
- 📁 **Commun** (procédures internes, organigramme, planning des congés)

---

**Tableau à remplir (1 par apprenant) :**

| **Dossier** | **Accès nécessaire ?** | **Type d'accès** | **Justification** |
|-------------|------------------------|------------------|-------------------|
| **Comptabilité** | ☐ Oui ☐ Non | ☐ Lecture seule ☐ Lecture+Écriture ☐ Tout contrôler | |
| **Commercial** | ☐ Oui ☐ Non | ☐ Lecture seule ☐ Lecture+Écriture ☐ Tout contrôler | |
| **Développement** | ☐ Oui ☐ Non | ☐ Lecture seule ☐ Lecture+Écriture ☐ Tout contrôler | |
| **Direction** | ☐ Oui ☐ Non | ☐ Lecture seule ☐ Lecture+Écriture ☐ Tout contrôler | |
| **Commun** | ☐ Oui ☐ Non | ☐ Lecture seule ☐ Lecture+Écriture ☐ Tout contrôler | |

**Questions bonus à discuter en groupe :**
1. Qui devrait pouvoir **créer de nouveaux dossiers** sur le serveur ?
2. Qui devrait pouvoir **supprimer** des fichiers dans Comptabilité ?
3. Le stagiaire commercial doit-il avoir les mêmes droits que le Directeur Général ?

---

#### **Phase 3 : Mise en commun et débat (10 min - Collectif)**

L'enseignant projette une grille vierge et interroge les groupes :

**Exemple de déroulé :**

**Enseignant :** *"Mme Martin, Directeur Général : de quoi avez-vous besoin pour le dossier Comptabilité ?"*

**Groupe 1 (Directeur)** : *"Lecture seule, pour consulter les bilans et vérifier que tout va bien."*

**Enseignant :** *"Pourquoi pas Lecture+Écriture ?"*

**Groupe 1** : *"Parce que ce n'est pas mon métier, je ne dois pas modifier les fichiers comptables. C'est le comptable qui gère ça."*

✅ **Enseignant valide** : *"Excellent ! C'est exactement le principe du moindre privilège : on donne UNIQUEMENT ce qui est nécessaire pour la mission."*

---

**Enseignant :** *"M. Petit, Stagiaire Commercial : avez-vous besoin d'accès au dossier Direction ?"*

**Groupe 2 (Stagiaire)** : *"Non, ça ne me concerne pas."*

**Enseignant :** *"Et pourquoi c'est important qu'il n'y ait pas accès ?"*

**Groupe 3** : *"Parce qu'il y a des documents confidentiels, comme la stratégie ou les salaires."*

✅ **Enseignant valide** : *"Exactement. Donner trop de droits = risque de fuite d'informations sensibles, voire violation du RGPD !"*

---

**Synthèse collective attendue (grille projetée finale) :**

| **Dossier** | **Directeur** | **Comptable** | **Développeur** | **Stagiaire** |
|-------------|---------------|---------------|-----------------|---------------|
| **Comptabilité** | 👁️ Lecture seule | ✏️ Lecture+Écriture | ❌ Aucun accès | ❌ Aucun accès |
| **Commercial** | 👁️ Lecture seule | ❌ Aucun accès | ❌ Aucun accès | 👁️ Lecture seule |
| **Développement** | 👁️ Lecture seule | ❌ Aucun accès | ✏️ Lecture+Écriture | ❌ Aucun accès |
| **Direction** | ✏️ Lecture+Écriture | ❌ Aucun accès | ❌ Aucun accès | ❌ Aucun accès |
| **Commun** | ✏️ Lecture+Écriture | 👁️ Lecture seule | 👁️ Lecture seule | 👁️ Lecture seule |

*Légende : 👁️ = Lecture seule | ✏️ = Lecture+Écriture | ❌ = Aucun accès*

---

**Transition vers l'apport théorique :**

> *"Vous venez de définir une **politique de droits d'accès** ! Dans un système d'exploitation Windows, c'est exactement ce qu'on configure avec les **comptes utilisateurs** et les **permissions NTFS**. On va maintenant voir comment le mettre en pratique."*

➡️ **Passage à l'apport théorique.**

---

### Critères de Réussite de l'Activité

| **Critère** | **Indicateur Observable** |
|-------------|---------------------------|
| **Engagement** | Les groupes échangent activement et remplissent les fiches |
| **Pertinence** | Au moins 3 choix de droits corrects par rôle |
| **Argumentation** | Les groupes justifient leurs choix (besoins métier, sécurité) |
| **Compréhension du principe** | Identification du fait que "trop de droits = dangereux" |
| **Participation collective** | Chaque groupe propose au moins 2 réponses lors de la mise en commun |

---

## 📚 FICHE DE COURS ÉLÈVE
### "Systèmes d'Exploitation : Windows, Comptes Utilisateurs & Permissions"

*Version 1.0 - BTS SIO SISR - Semestre 1 - Semaine 3*

---

### 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|----------------|
| **B1.2** | Mettre à disposition des utilisateurs un service informatique - Gérer des utilisateurs et des droits |
| **B2.1** | Administrer les services d'un système d'exploitation serveur |
| **B3.1** | Protéger les données à caractère personnel - Gestion des droits d'accès |

---

### I. Le Système d'Exploitation : Chef d'Orchestre de l'Ordinateur

#### A. Définition et Rôle

**Définition :** Le **Système d'Exploitation** (Operating System / OS) est un ensemble de programmes qui assure la **liaison entre le matériel et les applications**, tout en fournissant une **interface utilisateur**.

**Analogie :** L'OS est comme le **chef d'orchestre** d'un concert :
- Les **musiciens** = composants matériels (CPU, RAM, disques...)
- La **partition** = les applications (Word, Chrome, Photoshop...)
- Le **chef d'orchestre** = l'OS qui coordonne tout et décide qui joue quand

Sans OS, un ordinateur est comme une voiture sans moteur : le matériel est là, mais rien ne fonctionne.

---

#### B. Les 5 Rôles Principaux d'un OS

##### 🔹 **1. Gestion du Matériel (Hardware Management)**

L'OS contrôle tous les composants matériels via des **pilotes (drivers)**.

**Exemples :**
- Envoyer les données à imprimer vers l'imprimante
- Lire et écrire des données sur le disque dur
- Gérer l'affichage sur l'écran via la carte graphique
- Détecter les clés USB branchées

💡 **Lien avec S1-S2 :** Rappelez-vous les composants (CPU, RAM, SSD) vus en S1 → c'est l'OS qui les pilote !

---

##### 🔹 **2. Gestion des Fichiers (File System Management)**

L'OS organise les données en **fichiers** et **dossiers** (hiérarchie arborescente).

**Concepts clés :**
- **Système de fichiers** : NTFS (Windows), ext4 (Linux), APFS (macOS)
- **Arborescence** : Racine C:\ → Dossiers → Sous-dossiers → Fichiers
- **Métadonnées** : Nom, taille, date de création, propriétaire, permissions

**Opérations gérées :**
- Créer, copier, déplacer, renommer, supprimer des fichiers
- Rechercher des fichiers
- Sauvegarder et restaurer des données

![Arborescence Windows](arborescence_windows.png)
*Légende : Arborescence typique Windows avec C:\ à la racine, puis dossiers systèmes (Windows, Program Files) et utilisateurs (Users).*

---

##### 🔹 **3. Gestion des Processus (Process Management)**

Un **processus** = un programme en cours d'exécution.

**Rôle de l'OS :**
- **Multitâche** : Exécuter plusieurs programmes simultanément (Chrome + Word + Spotify...)
- **Allocation du CPU** : Décider quel processus utilise le CPU et pendant combien de temps
- **Gestion de la RAM** : Allouer de la mémoire à chaque processus
- **Priorités** : Les processus système ont la priorité sur les applications

**Outil Windows :** **Gestionnaire des tâches** (Ctrl+Shift+Esc)
- Onglet "Processus" : voir tous les programmes en cours
- Onglet "Performances" : voir l'utilisation CPU, RAM, disque, réseau

![Gestionnaire Tâches](gestionnaire_taches.png)
*Légende : Gestionnaire des tâches Windows 10 montrant les processus actifs et la consommation des ressources (CPU 12%, RAM 45%).*

---

##### 🔹 **4. Gestion des Utilisateurs et des Droits (User Management & Security)**

⭐ **THÈME CENTRAL DE CETTE SÉANCE**

L'OS permet de créer des **comptes utilisateurs** avec des **droits différenciés**.

**Pourquoi ?**
- ✅ **Sécurité** : Empêcher les utilisateurs de modifier les fichiers système
- ✅ **Confidentialité** : Chacun a son espace personnel (Bureau, Documents...)
- ✅ **Traçabilité** : Savoir qui a fait quoi (logs, audits)
- ✅ **Conformité RGPD** : Article 32 impose des mesures de sécurité dont la gestion des droits

**Mécanismes :**
- **Authentification** : Vérifier l'identité (nom d'utilisateur + mot de passe)
- **Autorisation** : Déterminer ce que l'utilisateur peut faire (permissions)
- **Audit** : Enregistrer les actions (qui a accédé à quoi, quand)

➡️ Nous approfondirons ce point dans les sections II et III.

---

##### 🔹 **5. Interface Utilisateur (User Interface)**

L'OS fournit un moyen d'interagir avec l'ordinateur.

**Types d'interfaces :**

| **Type** | **Nom** | **Description** | **Exemple** |
|----------|---------|-----------------|-------------|
| **CLI** | Command Line Interface | Lignes de commande (texte uniquement) | CMD, PowerShell, Bash (Linux) |
| **GUI** | Graphical User Interface | Interface graphique (fenêtres, icônes, souris) | Windows 10/11, macOS, GNOME (Linux) |
| **TUI** | Text-based User Interface | Interface texte avancée (menus texte) | Nano (éditeur Linux), BIOS/UEFI |

![CLI vs GUI](cli_vs_gui.png)
*Légende : À gauche, PowerShell (CLI) avec commandes tapées. À droite, Explorateur Windows (GUI) avec icônes et fenêtres.*

**Avantages CLI (pour les techniciens) :**
- ✅ Plus rapide pour les tâches répétitives (scripts)
- ✅ Administration à distance (SSH)
- ✅ Automatisation (batch, PowerShell, Bash)

**Avantages GUI (pour les utilisateurs finaux) :**
- ✅ Intuitif et visuel
- ✅ Courbe d'apprentissage plus douce
- ✅ Découverte des fonctionnalités par exploration

💡 **Bon technicien SISR = maîtrise des deux interfaces !**

---

#### C. Les Principaux Systèmes d'Exploitation

##### 🔹 **Tableau Comparatif**

| **OS** | **Éditeur** | **Licence** | **Usage Principal** | **Parts de Marché** |
|--------|-------------|-------------|---------------------|---------------------|
| **Windows** | Microsoft | Propriétaire (payant) | Desktop (bureautique, jeux), Serveurs | ~73% desktop, ~70% serveurs (avec Linux) |
| **Linux** | Communauté / Red Hat / Canonical... | Open Source (gratuit) | Serveurs, embarqué, supercalculateurs | ~26% serveurs, ~3% desktop |
| **macOS** | Apple | Propriétaire (inclus avec Mac) | Desktop (création, développement) | ~15% desktop |
| **Android** | Google | Open Source (base Linux) | Smartphones, tablettes | ~70% mobile |
| **iOS** | Apple | Propriétaire | iPhone, iPad | ~27% mobile |

---

##### 🔹 **Windows : L'Incontournable en Entreprise**

**Versions :**
- **Client** : Windows 10, Windows 11 (postes de travail)
- **Serveur** : Windows Server 2016/2019/2022 (infrastructure)

**Points forts :**
- ✅ **Compatibilité** : Majorité des logiciels professionnels (Office, ERP, CRM...)
- ✅ **Active Directory** : Gestion centralisée des utilisateurs et machines
- ✅ **Support** : Assistance Microsoft, documentation abondante
- ✅ **Familiarité** : Interface connue par 90% des utilisateurs

**Points faibles :**
- ❌ **Coût** : Licences payantes (Windows + CAL + applications)
- ❌ **Sécurité** : Cible privilégiée des malwares (vulnérabilités fréquentes)
- ❌ **Lourdeur** : Consomme plus de ressources que Linux

**Cas d'usage typiques :**
- Postes de travail bureautiques dans PME/ETI/Grands Comptes
- Serveurs de fichiers (File Server)
- Serveurs d'applications métier (.NET, SQL Server)
- Contrôleurs de domaine (Active Directory)

---

##### 🔹 **Linux : Le Roi des Serveurs**

**Distributions principales :**
- **Debian** / **Ubuntu** : Serveurs web, cloud
- **Red Hat Enterprise Linux (RHEL)** / **CentOS** : Entreprises (support commercial)
- **Fedora** : Workstations développeurs
- **Arch Linux** : Utilisateurs avancés (personnalisation maximale)

**Points forts :**
- ✅ **Gratuit** : Pas de licence (économie majeure)
- ✅ **Stabilité** : Serveurs Linux avec uptimes de plusieurs années
- ✅ **Sécurité** : Moins de malwares, permissions strictes par défaut
- ✅ **Légèreté** : Fonctionne sur du matériel ancien
- ✅ **Flexibilité** : Personnalisable à l'extrême (choix GUI, services...)

**Points faibles :**
- ❌ **Courbe d'apprentissage** : CLI obligatoire pour administration
- ❌ **Compatibilité logicielle** : Certains logiciels métier Windows-only
- ❌ **Fragmentation** : Des dizaines de distributions différentes

**Cas d'usage typiques :**
- Serveurs web (Apache, Nginx)
- Serveurs de bases de données (MySQL, PostgreSQL)
- Infrastructure cloud (AWS, Azure, Google Cloud)
- Conteneurs (Docker, Kubernetes)
- Objets connectés (Raspberry Pi, routeurs, NAS...)

---

##### 🔹 **macOS : Créatif et Développeur**

**Points forts :**
- ✅ **Écosystème Apple** : Intégration iPhone/iPad/Mac
- ✅ **Création** : Applications pro (Final Cut, Logic Pro, Xcode)
- ✅ **Base Unix** : Terminal Bash/Zsh pour développeurs
- ✅ **Sécurité** : Gatekeeper, XProtect (antimalware intégré)

**Points faibles :**
- ❌ **Prix** : Matériel Apple très cher
- ❌ **Fermeture** : Impossible d'installer sur PC standard (hackintosh = violation licence)
- ❌ **Peu en entreprise** : Marginal en environnement corporate (sauf créa/dev)

**Cas d'usage typiques :**
- Studios de création graphique / vidéo / audio
- Agences de développement mobile (apps iOS)
- Startups tech (culture développeur)

---

#### D. Architecture d'un OS : Le Noyau (Kernel)

**Définition :** Le **noyau** (kernel) est le **cœur de l'OS**, programme qui s'exécute en **mode privilégié** (accès direct au matériel).

**Rôles du noyau :**
- Gestion des processus (scheduler)
- Gestion de la mémoire (RAM)
- Gestion des périphériques (drivers)
- Gestion des entrées/sorties (I/O)

**Types de noyaux :**

| **Type** | **Description** | **Exemple** |
|----------|-----------------|-------------|
| **Monolithique** | Tout dans un seul programme (performances max) | Linux, Unix |
| **Micro-noyau** | Noyau minimal + services séparés (stabilité max) | Minix, QNX |
| **Hybride** | Compromis (performance + modularité) | Windows NT, macOS (XNU) |

**Schéma en couches :**

```
┌────────────────────────────────────────┐
│     UTILISATEUR & APPLICATIONS         │  ← Couche 4 : Programmes (Word, Chrome...)
├────────────────────────────────────────┤
│     INTERFACE SYSTÈME (API)            │  ← Couche 3 : API Windows / POSIX
├────────────────────────────────────────┤
│     SERVICES SYSTÈMES                  │  ← Couche 2 : Gestionnaire fichiers, réseau...
├────────────────────────────────────────┤
│     NOYAU (KERNEL)                     │  ← Couche 1 : Cœur de l'OS
├────────────────────────────────────────┤
│     MATÉRIEL (HARDWARE)                │  ← Couche 0 : CPU, RAM, Disques, Cartes réseau
└────────────────────────────────────────┘
```

💡 **Privilèges :**
- **Mode noyau** (kernel mode) : Accès total au matériel (réservé à l'OS)
- **Mode utilisateur** (user mode) : Accès restreint via API (applications)

Cette séparation empêche une application malveillante de crasher tout le système ou d'accéder directement au matériel.

---

### II. Gestion des Comptes Utilisateurs dans Windows

#### A. Pourquoi Plusieurs Comptes Utilisateurs ?

**Scénario sans comptes séparés (ordinateur partagé avec 1 seul compte) :**

❌ **Problèmes :**
1. Pas de **confidentialité** : Tout le monde voit les documents de tout le monde
2. Pas de **personnalisation** : Fond d'écran, favoris, applications... partagés
3. **Sécurité catastrophique** : Si ce compte unique est Administrateur, n'importe qui peut installer des logiciels malveillants ou supprimer des fichiers système
4. **Aucune traçabilité** : Impossible de savoir qui a supprimé le fichier important

**Scénario avec comptes séparés :**

✅ **Avantages :**
1. **Confidentialité** : Chaque utilisateur a son dossier personnel (C:\Users\nomutilisateur\)
2. **Personnalisation** : Bureau, thème, paramètres propres à chacun
3. **Sécurité** : Comptes limités ne peuvent pas installer de logiciels ou modifier le système
4. **Traçabilité** : Les logs indiquent quel compte a effectué quelle action
5. **Conformité RGPD** : Séparation des accès = mesure de sécurité obligatoire

---

#### B. Types de Comptes dans Windows

##### 🔹 **1. Compte Administrateur (Administrator)**

**Privilèges :**
- ✅ **Contrôle total** du système
- ✅ Installer/désinstaller des programmes
- ✅ Modifier les paramètres système
- ✅ Créer/supprimer des comptes utilisateurs
- ✅ Modifier les permissions de fichiers
- ✅ Accéder aux fichiers de tous les utilisateurs
- ✅ Installer des pilotes matériels

**Icône :** Badge jaune/orange sur la photo de profil

**Danger ⚠️ :**
- Un malware exécuté avec des droits admin peut **tout infecter**
- Une fausse manipulation peut **rendre Windows instable**
- Accès non contrôlé aux **données sensibles**

**Bonnes pratiques :**
- ❌ **Ne JAMAIS utiliser un compte Administrateur au quotidien**
- ✅ Créer un compte Utilisateur standard pour l'usage quotidien
- ✅ Utiliser l'Administrateur uniquement pour les tâches d'administration
- ✅ Activer **UAC (User Account Control)** pour demander confirmation avant actions sensibles

---

##### 🔹 **2. Compte Utilisateur Standard (Standard User)**

**Privilèges :**
- ✅ Utiliser les programmes installés
- ✅ Modifier ses propres fichiers (dans C:\Users\sonnom\)
- ✅ Personnaliser son Bureau, thème, favoris
- ✅ Se connecter à Internet
- ❌ **Ne PEUT PAS** installer de logiciels
- ❌ **Ne PEUT PAS** modifier les paramètres système
- ❌ **Ne PEUT PAS** accéder aux fichiers des autres utilisateurs

**Icône :** Pas de badge spécial

**Avantages sécurité :**
- ✅ Un malware ne peut infecter que l'espace de cet utilisateur (pas tout le système)
- ✅ Impossible de casser Windows par erreur
- ✅ Principe du **moindre privilège** respecté

**Usage recommandé :**
- ✅ **Tous les employés** d'une entreprise doivent avoir des comptes Standard
- ✅ Même l'administrateur système doit avoir un compte Standard pour son travail quotidien (et un compte Admin séparé pour l'administration)

---

##### 🔹 **3. Compte Invité (Guest) - Obsolète Windows 10/11**

**Caractéristiques :**
- Compte temporaire pour visiteurs
- Aucun mot de passe requis
- Profil supprimé à chaque fermeture de session
- **Désactivé par défaut** depuis Windows 10 (raisons de sécurité)

💡 **Note :** Peu utilisé en entreprise. En BTS SIO, on ne le manipule généralement pas.

---

#### C. Comptes Locaux vs Comptes de Domaine

##### 🔹 **Compte Local**

**Définition :** Compte créé sur une **machine spécifique**, stocké dans la **base SAM** (Security Account Manager) locale de cette machine.

**Caractéristiques :**
- ✅ Fonctionne uniquement sur **cette machine**
- ✅ Pas besoin de réseau ou de serveur
- ✅ Idéal pour : PC personnels, petites structures (<5 PC), environnements de test

**Gestion :**
- Outil : **Gestion de l'ordinateur** → **Utilisateurs et groupes locaux**
- Emplacement base de données : `C:\Windows\System32\config\SAM`

**Limites :**
- ❌ Si 10 PC → il faut créer 10 fois le même compte (1 par PC) !
- ❌ Changement de mot de passe → à faire sur chaque machine
- ❌ Pas de gestion centralisée
- ❌ Pas de stratégies de groupe (GPO)

---

##### 🔹 **Compte de Domaine (Active Directory)**

**Définition :** Compte créé dans **Active Directory** (annuaire centralisé sur un serveur), valable sur **toutes les machines du domaine**.

**Caractéristiques :**
- ✅ **1 seul compte** utilisable sur tous les PC de l'entreprise
- ✅ Gestion **centralisée** (création, modification, suppression depuis le serveur)
- ✅ **Stratégies de groupe (GPO)** : paramètres appliqués automatiquement
- ✅ **Authentification unique (SSO)** : 1 mot de passe pour tous les services

**Gestion :**
- Outil : **Active Directory Users and Computers (ADUC)** sur le contrôleur de domaine
- Serveur : **Windows Server** avec rôle **AD DS (Active Directory Domain Services)**

**Avantages pour l'entreprise :**
- ✅ Employé arrive → 1 compte créé → accès immédiat à tous les PC et services
- ✅ Employé part → compte désactivé en 1 clic → plus aucun accès nulle part
- ✅ Changement de mot de passe → pris en compte partout instantanément
- ✅ Stratégies : forcer écran de veille, fond d'écran entreprise, logiciels installés...

**Exemple professionnel :**

| **Scénario** | **Compte Local** | **Compte Domaine (AD)** |
|--------------|------------------|-------------------------|
| Nouvel employé (Jean Dupont) | Créer manuellement "jdupont" sur ses 3 PC de travail | Créer 1 fois "jdupont" dans AD → fonctionne sur les 500 PC de l'entreprise |
| Jean oublie son mot de passe | Réinitialiser sur chaque PC (3 fois) | Réinitialiser 1 fois dans AD → synchronisé partout |
| Jean change de service | Modifier les droits sur chaque PC manuellement | Déplacer le compte dans une autre OU (Organizational Unit) → GPO appliquées automatiquement |
| Jean quitte l'entreprise | Supprimer le compte sur les 3 PC | Désactiver le compte dans AD → bloqué partout en 10 secondes |

💡 **En BTS SIO :**
- **S3-S4** : Manipulation de comptes **locaux** (Windows 10/11)
- **S5-S10+** : Mise en place d'**Active Directory** et gestion de comptes de domaine

---

#### D. Création de Comptes Utilisateurs Locaux (Windows 10/11)

##### 🔹 **Méthode Graphique (GUI)**

**Étapes :**

1. **Ouvrir les Paramètres**
   - Clic droit sur le bouton Démarrer → **Paramètres** (icône engrenage)
   - Ou touche Windows + I

2. **Accéder aux Comptes**
   - Clic sur **Comptes**
   - Dans le menu de gauche, clic sur **Famille et autres utilisateurs**

3. **Ajouter un Utilisateur**
   - Section "Autres utilisateurs" → **Ajouter un autre utilisateur sur ce PC**

4. **Créer un Compte Local** (pas de compte Microsoft)
   - Fenêtre "Comment cette personne va-t-elle se connecter ?"
   - Clic sur **Je ne dispose pas des informations de connexion de cette personne**
   - Puis clic sur **Ajouter un utilisateur sans compte Microsoft**

5. **Remplir les Informations**
   - **Nom d'utilisateur** : `jdupont` (convention : prenom.nom ou initiales)
   - **Mot de passe** : `Azerty123!` (respecter complexité : maj+min+chiffre+symbole)
   - **Confirmer le mot de passe** : `Azerty123!`
   - **Questions de sécurité** : Remplir les 3 questions (obligatoire)

6. **Créer**
   - Clic sur **Suivant**
   - ✅ Le compte est créé ! (Type : Utilisateur standard par défaut)

---

##### 🔹 **Modifier le Type de Compte (Standard → Administrateur)**

**Si besoin de promouvoir un compte en Administrateur :**

1. Paramètres → Comptes → Famille et autres utilisateurs
2. Clic sur le compte `jdupont`
3. Clic sur **Modifier le type de compte**
4. Dans le menu déroulant, sélectionner **Administrateur**
5. Clic sur **OK**

⚠️ **Attention :** Ne faire cela que si **vraiment nécessaire** (principe du moindre privilège) !

---

##### 🔹 **Méthode Ligne de Commande (PowerShell)**

**Pourquoi utiliser PowerShell ?**
- ✅ Plus **rapide** pour créer plusieurs comptes
- ✅ **Automatisation** via scripts
- ✅ Administration à **distance** (WinRM)
- ✅ **Traçabilité** (commandes enregistrées dans l'historique)

**Commandes :**

```powershell
# Ouvrir PowerShell en tant qu'Administrateur
# Clic droit sur Démarrer → Windows PowerShell (admin)

# Créer un utilisateur local
New-LocalUser -Name "jdupont" -Password (ConvertTo-SecureString "Azerty123!" -AsPlainText -Force) -FullName "Jean Dupont" -Description "Comptable"

# Ajouter l'utilisateur au groupe Administrateurs (si besoin)
Add-LocalGroupMember -Group "Administrateurs" -Member "jdupont"

# Ou au groupe Utilisateurs (par défaut)
Add-LocalGroupMember -Group "Utilisateurs" -Member "jdupont"

# Lister tous les comptes locaux
Get-LocalUser

# Désactiver un compte
Disable-LocalUser -Name "jdupont"

# Réactiver un compte
Enable-LocalUser -Name "jdupont"

# Supprimer un compte
Remove-LocalUser -Name "jdupont"

# Changer le mot de passe
Set-LocalUser -Name "jdupont" -Password (ConvertTo-SecureString "NouveauMDP2024!" -AsPlainText -Force)
```

💡 **Conseil :** Gardez ces commandes sous la main, elles reviendront souvent en BTS et en entreprise !

---

##### 🔹 **Méthode Outil Gestion de l'Ordinateur (Avancé)**

**Avantage :** Interface plus complète que les Paramètres, permet de gérer les groupes locaux.

**Étapes :**

1. Clic droit sur **Ce PC** → **Gérer**
   - Ou taper `compmgmt.msc` dans Exécuter (Windows + R)

2. **Outils système** → **Utilisateurs et groupes locaux** → **Utilisateurs**

3. Clic droit dans la zone vide → **Nouvel utilisateur...**

4. Remplir :
   - **Nom d'utilisateur** : `jdupont`
   - **Nom complet** : Jean Dupont
   - **Description** : Comptable
   - **Mot de passe** : `Azerty123!`
   - **Confirmer le mot de passe** : `Azerty123!`
   - Cocher **L'utilisateur ne peut pas changer de mot de passe** (optionnel, selon contexte)
   - Décocher **L'utilisateur doit changer le mot de passe à la prochaine ouverture de session** (pour simplifier le TP)

5. Clic sur **Créer** puis **Fermer**

**Ajouter l'utilisateur à un groupe :**

1. Toujours dans **Utilisateurs et groupes locaux** → **Groupes**
2. Double-clic sur **Administrateurs** (ou autre groupe)
3. Clic sur **Ajouter...**
4. Taper `jdupont` → Clic sur **Vérifier les noms** → OK
5. OK pour valider

✅ L'utilisateur est maintenant membre du groupe Administrateurs.

![Gestion Ordinateur Utilisateurs](gestion_ordinateur_utilisateurs.png)
*Légende : Fenêtre "Utilisateurs et groupes locaux" dans Gestion de l'ordinateur, montrant la liste des comptes locaux (Administrateur, Invité, et comptes créés).*

---

#### E. Groupes Locaux Prédéfinis

**Définition :** Un **groupe** est un ensemble d'utilisateurs partageant les **mêmes droits**. Au lieu de donner des droits individuellement, on les affecte au groupe.

**Groupes Windows locaux principaux :**

| **Groupe** | **Description** | **Privilèges** |
|------------|-----------------|----------------|
| **Administrateurs** | Contrôle total du système | Tout installer, tout modifier, accès à tous les fichiers |
| **Utilisateurs** | Groupe standard | Utiliser le PC, modifier ses propres fichiers, installer apps Modern (Microsoft Store) |
| **Utilisateurs avec pouvoir** | Privilèges limités avancés | Partager des dossiers, modifier l'horloge (ancien, peu utilisé) |
| **Opérateurs de sauvegarde** | Sauvegardes système | Lire tous les fichiers (même sans permission), pour logiciels de backup |
| **Invités** | Accès temporaire minimal | Très restreint, pas de personnalisation |

**Pourquoi utiliser des groupes ?**

**Exemple :** 10 employés du service Comptabilité doivent avoir accès au dossier `C:\Compta`.

❌ **Méthode individuelle** : Ajouter les 10 comptes un par un aux permissions du dossier.
- Si 11ème employé arrive → ajouter manuellement
- Si employé part → retirer manuellement
- Risque d'oubli et d'erreur

✅ **Méthode par groupe** : 
1. Créer un groupe local "Comptables"
2. Ajouter les 10 comptes au groupe
3. Donner les permissions au **groupe** (pas aux comptes individuels)
- Nouvel employé → l'ajouter au groupe (1 manipulation) → droits automatiques
- Employé part → le retirer du groupe → droits révoqués partout

➡️ **Gain de temps + sécurité + cohérence**

---

### III. Permissions NTFS : Contrôler l'Accès aux Fichiers

#### A. Qu'est-ce que NTFS ?

**NTFS = New Technology File System**

**Définition :** Système de fichiers de Windows (depuis Windows NT 1993), offrant des fonctionnalités avancées de sécurité, fiabilité et performance.

**Avantages de NTFS vs FAT32 :**

| **Fonctionnalité** | **FAT32** (ancien) | **NTFS** (moderne) |
|--------------------|--------------------|--------------------|
| **Taille fichier max** | 4 Go | 16 Exaoctets (= illimité en pratique) |
| **Taille partition max** | 2 To | 256 To |
| **Permissions fichiers** | ❌ Non (tous les fichiers accessibles par tous) | ✅ Oui (ACL - Access Control Lists) |
| **Chiffrement** | ❌ Non | ✅ Oui (EFS - Encrypting File System) |
| **Compression** | ❌ Non | ✅ Oui (transparente) |
| **Quotas disque** | ❌ Non | ✅ Oui (limiter l'espace par utilisateur) |
| **Journalisation** | ❌ Non | ✅ Oui (récupération après crash) |

💡 **À retenir :** NTFS est **obligatoire** pour utiliser les permissions de fichiers Windows. Une clé USB en FAT32 n'a **pas de permissions** (accessible en écriture par tous).

---

#### B. Les 6 Permissions NTFS Standard

Chaque fichier ou dossier NTFS possède une **ACL (Access Control List)** : liste des utilisateurs/groupes et leurs droits.

**Les 6 permissions de base :**

| **Permission** | **Symbole** | **Peut...** | **Exemples d'actions autorisées** |
|----------------|-------------|-------------|-----------------------------------|
| **Lecture** | 👁️ R (Read) | Lire le contenu | Ouvrir un fichier, voir le contenu d'un dossier, copier un fichier |
| **Écriture** | ✏️ W (Write) | Modifier le contenu | Modifier un fichier existant, créer de nouveaux fichiers dans un dossier |
| **Lecture et exécution** | 👁️▶️ RX (Read & Execute) | Lire + exécuter | Lancer un .exe, parcourir un dossier, lire un script |
| **Modification** | ✏️🗑️ M (Modify) | Lire + Écrire + Supprimer | Tout faire sauf changer les permissions ou prendre possession |
| **Contrôle total** | 🔑 F (Full Control) | **TOUT** | Modifier, supprimer, changer les permissions, changer le propriétaire |
| **Permissions spéciales** | ⚙️ | Combinaisons personnalisées | Paramètres très avancés (rarement utilisés) |

---

**Détail des permissions :**

##### 🔹 **1. Lecture (Read)**

**Permet de :**
- ✅ Ouvrir et **lire** un fichier
- ✅ Lister le contenu d'un dossier
- ✅ **Copier** un fichier (la copie = lecture + écriture ailleurs)

**Ne permet PAS de :**
- ❌ Modifier le fichier
- ❌ Supprimer le fichier
- ❌ Exécuter un programme (.exe, .bat)

**Cas d'usage :** Consulter des documents en lecture seule (procédures, rapports archivés).

---

##### 🔹 **2. Écriture (Write)**

**Permet de :**
- ✅ Modifier le **contenu** d'un fichier existant
- ✅ Créer de **nouveaux fichiers** dans un dossier

**Ne permet PAS (seule) de :**
- ❌ Lire le contenu (!)
- ❌ Supprimer le fichier

⚠️ **Bizarrerie :** Avoir uniquement "Écriture" sans "Lecture" est rare et peu utile (on peut modifier sans voir !).

**Cas d'usage (combinée avec Lecture) :** Modifier des fichiers partagés (dossier collaboratif).

---

##### 🔹 **3. Lecture et Exécution (Read & Execute)**

**Permet de :**
- ✅ Tout ce que "Lecture" permet
- ✅ **Exécuter** des programmes (.exe, .bat, .cmd, .ps1...)
- ✅ **Parcourir** les sous-dossiers (traverse folders)

**Cas d'usage :** Dossier d'applications partagées. Les utilisateurs peuvent lancer les programmes mais pas les modifier.

---

##### 🔹 **4. Modification (Modify)**

**Permet de :**
- ✅ Lecture
- ✅ Écriture
- ✅ Lecture et Exécution
- ✅ **Supprimer** des fichiers et sous-dossiers

**Ne permet PAS de :**
- ❌ Changer les **permissions** du fichier/dossier
- ❌ Prendre **possession** (changer le propriétaire)

**Cas d'usage :** Dossier collaboratif où chacun peut créer, modifier, supprimer ses fichiers (mais pas bloquer les autres en changeant les droits).

⭐ **Permission la plus courante en entreprise pour les utilisateurs standards.**

---

##### 🔹 **5. Contrôle Total (Full Control)**

**Permet de :**
- ✅ **TOUT** ce que "Modification" permet
- ✅ Changer les **permissions** du fichier/dossier (ACL)
- ✅ Prendre **possession** (devenir propriétaire)
- ✅ Supprimer le fichier/dossier **même sans permission de suppression sur le contenu** (force delete)

**Danger ⚠️ :**
- Un utilisateur avec Contrôle Total peut **bloquer tout le monde** (y compris les admins) en retirant tous les droits
- Il peut **supprimer** un dossier entier même si d'autres travaillent dessus

**Cas d'usage :** 
- Réservé aux **Administrateurs**
- Propriétaire du fichier (créateur)

💡 **Principe du moindre privilège :** Ne JAMAIS donner Contrôle Total à un utilisateur standard !

---

##### 🔹 **6. Permissions Spéciales (Advanced)**

Combinaisons personnalisées des 13 permissions atomiques NTFS.

**Exemples de permissions atomiques :**
- Créer des fichiers / Écrire des données
- Créer des dossiers / Ajouter des données
- Supprimer les sous-dossiers et fichiers
- Lire les attributs étendus
- Modifier les permissions
- ...

⚙️ **Usage :** Très rare, pour des besoins très spécifiques (audits de sécurité, restrictions fines).

💡 **En BTS SIO SISR :** On se limite aux 5 premières permissions dans 99% des cas.

---

#### C. Héritage des Permissions

**Définition :** Par défaut, un sous-dossier ou fichier **hérite** automatiquement des permissions de son dossier parent.

**Exemple :**

```
C:\Data (Permissions : Groupe "Comptables" = Modification)
  ├── Factures (Hérite : Groupe "Comptables" = Modification)
  │   └── Facture_2024.xlsx (Hérite : Groupe "Comptables" = Modification)
  └── Bilans (Hérite : Groupe "Comptables" = Modification)
```

➡️ Si je donne "Modification" au groupe "Comptables" sur `C:\Data`, tous les sous-dossiers et fichiers héritent automatiquement de cette permission.

**Avantages :**
- ✅ **Facilité de gestion** : 1 seule configuration au sommet de l'arborescence
- ✅ **Cohérence** : Pas de risque d'oublier un sous-dossier
- ✅ **Maintenance** : Modifier en haut = répercuté partout

**Désactiver l'héritage :**

Parfois, on veut qu'un sous-dossier ait des permissions **différentes** du parent.

**Exemple :** 
- `C:\Data\Salaires` → Seuls les RH doivent y accéder (pas tout le groupe "Comptables")

**Procédure :**
1. Clic droit sur `Salaires` → **Propriétés** → Onglet **Sécurité**
2. Clic sur **Avancé**
3. Clic sur **Désactiver l'héritage**
4. Choisir :
   - **Convertir les permissions héritées en permissions explicites** (garde les permissions actuelles mais les rend modifiables)
   - **Supprimer toutes les permissions héritées** (repart de zéro)
5. OK → Le dossier a maintenant ses propres permissions, indépendantes du parent

⚠️ **Attention :** Désactiver l'héritage partout = gestion cauchemar ! À utiliser avec parcimonie, uniquement pour des dossiers vraiment sensibles.

---

#### D. Principe du Refus Explicite (Deny)

**Deny (Refuser) vs Allow (Autoriser) :**

Chaque permission peut être **Autorisée** ou **Refusée**.

**Règle d'or :** **Deny l'emporte toujours sur Allow**.

**Exemple :**
- Utilisateur "jdupont" est membre de 2 groupes :
  - Groupe "Comptables" → **Autorise** Modification sur `C:\Data`
  - Groupe "Stagiaires" → **Refuse** Écriture sur `C:\Data`

➡️ Résultat : "jdupont" a **Lecture seule** (le Refus annule l'autorisation d'écriture).

**Cas d'usage du Deny :**
- ✅ Bloquer un utilisateur spécifique sans le retirer d'un groupe
- ✅ Exceptions dans une politique générale

**Piège :**
- ❌ Overuse de Deny = gestion complexe et bugs difficiles à déboguer
- ✅ **Bonne pratique :** Utiliser principalement Allow, et Deny **très rarement** (cas exceptionnels)

---

#### E. Permissions Effectives (Effective Permissions)

**Problème :** Un utilisateur est souvent membre de **plusieurs groupes**. Comment savoir quels sont ses droits réels ?

**Règle de cumul :**
1. Les permissions **Allow** de tous les groupes **s'additionnent** (cumul)
2. Le **Deny** de n'importe quel groupe **annule** tout

**Exemple :**

| **Groupe** | **Permission sur C:\Projets** |
|------------|-------------------------------|
| Développeurs | Lecture |
| Chefs de projet | Modification |
| Stagiaires | *Pas de permission* |

**Utilisateur "mleroux" est membre de :**
- Développeurs
- Chefs de projet

➡️ **Permissions effectives de mleroux** : **Modification** (la plus permissive entre Lecture et Modification)

---

**Outil Windows pour vérifier les permissions effectives :**

1. Clic droit sur le dossier → **Propriétés** → **Sécurité**
2. Clic sur **Avancé**
3. Onglet **Accès effectif**
4. Clic sur **Sélectionner un utilisateur**
5. Taper le nom d'utilisateur (ex: `jdupont`) → **OK**
6. Windows affiche la liste des permissions effectives (cochées ou non)

![Permissions Effectives](permissions_effectives.png)
*Légende : Fenêtre "Accès effectif" montrant les permissions réelles de l'utilisateur "jdupont" sur le dossier sélectionné, en tenant compte de tous ses groupes.*

---

#### F. Configurer les Permissions NTFS (Méthode Graphique)

##### 🔹 **Méthode Simple (Interface Sécurité)**

**Étapes :**

1. **Créer le dossier**
   - Exemple : `C:\Data\Comptabilite`

2. **Clic droit** sur le dossier → **Propriétés**

3. Onglet **Sécurité**
   - Affiche la liste des utilisateurs/groupes ayant des permissions
   - Affiche leurs permissions (cases cochées)

4. **Ajouter un utilisateur/groupe**
   - Clic sur **Modifier...**
   - Clic sur **Ajouter...**
   - Taper le nom (ex: `Comptables` ou `jdupont`)
   - Clic sur **Vérifier les noms** (souligne si trouvé)
   - Clic sur **OK**

5. **Définir les permissions**
   - Sélectionner l'utilisateur/groupe dans la liste
   - Cocher les permissions dans la section du bas :
     - ✅ **Contrôle total** (rarement, admins uniquement)
     - ✅ **Modification** (usage courant)
     - ✅ **Lecture et exécution** (consultations)
     - ✅ **Lecture** (lecture seule)
     - ✅ **Écriture** (rare seule)
   - Ou cocher **Refuser** pour bloquer (rare)

6. **Appliquer** → **OK**

✅ Les permissions sont configurées !

**Test des permissions :**
- Se déconnecter de Windows
- Se connecter avec le compte "jdupont"
- Essayer d'accéder au dossier `C:\Data\Comptabilite`
- Vérifier qu'on peut lire, écrire, ou que l'accès est refusé selon les permissions

---

##### 🔹 **Méthode Avancée (Permissions Avancées)**

Pour aller plus loin (désactiver héritage, permissions spéciales...) :

1. Clic droit sur le dossier → **Propriétés** → **Sécurité**
2. Clic sur **Avancé**
3. Fenêtre "Paramètres de sécurité avancés" :
   - Onglet **Permissions** : Liste complète avec héritage visible
   - Bouton **Désactiver l'héritage** : Casser la chaîne d'héritage
   - Bouton **Ajouter** : Ajouter une entrée de permission (ACE - Access Control Entry)
   - Double-clic sur une ligne : Voir les 13 permissions atomiques détaillées

---

#### G. Scénario Professionnel Complet (TP)

**Contexte :** PME **TechPro SARL** avec 4 services.

**Structure de dossiers à créer :**

```
C:\Data
  ├── Direction
  ├── Comptabilite
  ├── Commercial
  ├── Technique
  └── Commun
```

**Groupes à créer :**
- `GRP_Direction` (1 membre : Mme Martin)
- `GRP_Comptabilite` (2 membres : M. Dubois, Mme Leroy)
- `GRP_Commercial` (3 membres : M. Bernard, Mme Petit, M. Dupuis)
- `GRP_Technique` (2 membres : M. Garcia, Mme Roux)

**Matrice de permissions :**

| **Dossier** | **GRP_Direction** | **GRP_Comptabilite** | **GRP_Commercial** | **GRP_Technique** | **Utilisateurs** |
|-------------|-------------------|----------------------|--------------------|--------------------|------------------|
| **Direction** | Modification | ❌ Aucun | ❌ Aucun | ❌ Aucun | Lecture seule (pour organigramme) |
| **Comptabilite** | Lecture seule | Modification | ❌ Aucun | ❌ Aucun | ❌ Aucun |
| **Commercial** | Lecture seule | ❌ Aucun | Modification | ❌ Aucun | ❌ Aucun |
| **Technique** | Lecture seule | ❌ Aucun | ❌ Aucun | Modification | ❌ Aucun |
| **Commun** | Modification | Lecture | Lecture | Lecture | Lecture |

**Objectifs du TP :**
1. Créer les 5 dossiers
2. Créer les 4 groupes locaux
3. Créer 8 comptes utilisateurs (répartis dans les groupes)
4. Configurer les permissions NTFS selon la matrice
5. Tester avec chaque compte que les accès sont corrects

➡️ Détail complet dans la section **TP Guidé Partie 2** ci-dessous.

---

### IV. TP Guidé Partie 1 : Création et Gestion de Comptes Locaux (30 min)

#### Objectif

Créer 4 comptes utilisateurs locaux avec des rôles différents et comprendre les types de comptes.

---

#### Scénario

Vous êtes technicien chez **TechPro SARL**. On vous demande de créer les comptes pour 4 nouveaux employés :

1. **Marie MARTIN** - Directrice Générale (compte Administrateur)
2. **Paul DUBOIS** - Comptable (compte Utilisateur standard)
3. **Sophie LEROUX** - Développeuse (compte Utilisateur standard)
4. **Thomas PETIT** - Stagiaire Commercial (compte Utilisateur standard)

---

#### Étape 1 : Création des Comptes (Méthode Paramètres - 15 min)

**Pour chaque compte, suivre ces étapes :**

1. **Ouvrir les Paramètres** (Windows + I)
2. **Comptes** → **Famille et autres utilisateurs**
3. **Ajouter un autre utilisateur sur ce PC**
4. **Je ne dispose pas des informations de connexion** → **Ajouter un utilisateur sans compte Microsoft**
5. Remplir :
   - **Compte 1 :**
     - Nom : `mmartin`
     - Mot de passe : `Azerty123!`
     - Questions de sécurité : Au choix
   - **Compte 2 :**
     - Nom : `pdubois`
     - Mot de passe : `Azerty123!`
   - **Compte 3 :**
     - Nom : `sleroux`
     - Mot de passe : `Azerty123!`
   - **Compte 4 :**
     - Nom : `tpetit`
     - Mot de passe : `Azerty123!`
6. Clic sur **Suivant** pour chaque compte

✅ **Validation :** Les 4 comptes apparaissent dans la liste "Autres utilisateurs".

---

#### Étape 2 : Promouvoir mmartin en Administrateur (5 min)

1. Dans Paramètres → Comptes → Famille et autres utilisateurs
2. Clic sur **mmartin**
3. **Modifier le type de compte**
4. Sélectionner **Administrateur**
5. **OK**

✅ **Validation :** Badge "Administrateur" visible à côté de "mmartin".

---

#### Étape 3 : Vérification avec PowerShell (5 min)

1. Ouvrir **PowerShell** (Clic droit Démarrer → Windows PowerShell)
2. Taper :
   ```powershell
   Get-LocalUser
   ```
3. Vérifier que les 4 comptes apparaissent dans la liste

4. Voir les membres du groupe Administrateurs :
   ```powershell
   Get-LocalGroupMember -Group "Administrateurs"
   ```
   ✅ "mmartin" doit apparaître (+ votre compte initial)

5. Voir les membres du groupe Utilisateurs :
   ```powershell
   Get-LocalGroupMember -Group "Utilisateurs"
   ```
   ✅ "pdubois", "sleroux", "tpetit" doivent apparaître

---

#### Étape 4 : Test de Connexion (5 min)

1. **Déconnexion** (Ctrl+Alt+Suppr → Déconnexion)
2. **Se connecter avec "pdubois"** (mot de passe : `Azerty123!`)
3. Essayer d'ouvrir **Gestion de l'ordinateur** (compmgmt.msc)
   - ❌ Devrait demander un mot de passe administrateur (UAC)
4. **Déconnexion**
5. **Se connecter avec "mmartin"**
6. Ouvrir **Gestion de l'ordinateur**
   - ✅ Devrait s'ouvrir directement (ou avec simple confirmation UAC)

✅ **TP Partie 1 terminé !**

---

### V. TP Guidé Partie 2 : Configuration des Permissions NTFS (60 min)

#### Objectif

Mettre en place une structure de dossiers avec permissions NTFS pour séparer les accès selon les services de l'entreprise.

---

#### Scénario

**TechPro SARL** a 4 services (Direction, Comptabilité, Commercial, Technique). Vous devez créer une structure de dossiers partagés avec des droits d'accès différenciés.

---

#### Étape 1 : Création de la Structure de Dossiers (5 min)

1. **Se connecter en tant qu'Administrateur** (mmartin ou votre compte initial)

2. Ouvrir **Explorateur de fichiers**

3. Créer à la racine de C:\ un dossier **Data** :
   - Aller sur `C:\`
   - Clic droit → Nouveau → Dossier → Nommer `Data`

4. Dans `C:\Data\`, créer 5 sous-dossiers :
   - `Direction`
   - `Comptabilite`
   - `Commercial`
   - `Technique`
   - `Commun`

**Structure finale :**
```
C:\Data
  ├── Direction
  ├── Comptabilite
  ├── Commercial
  ├── Technique
  └── Commun
```

✅ **Validation :** Les 5 dossiers sont visibles dans `C:\Data\`

---

#### Étape 2 : Création des Groupes Locaux (10 min)

1. Ouvrir **Gestion de l'ordinateur** (compmgmt.msc)
2. **Outils système** → **Utilisateurs et groupes locaux** → **Groupes**
3. Clic droit zone vide → **Nouveau groupe...**

**Créer 4 groupes :**

| **Nom du groupe** | **Description** | **Membres à ajouter** |
|-------------------|-----------------|----------------------|
| `GRP_Direction` | Service Direction | mmartin |
| `GRP_Comptabilite` | Service Comptabilité | pdubois |
| `GRP_Commercial` | Service Commercial | tpetit |
| `GRP_Technique` | Service Technique | sleroux |

**Procédure pour chaque groupe :**
1. **Nom du groupe** : `GRP_Direction`
2. **Description** : `Service Direction`
3. Clic sur **Ajouter...**
4. Taper `mmartin` → **Vérifier les noms** → **OK**
5. Clic sur **Créer** → **Fermer**

Répéter pour les 3 autres groupes.

✅ **Validation :** 4 groupes créés et visibles dans "Groupes", chacun avec au moins 1 membre.

---

#### Étape 3 : Configuration des Permissions du Dossier "Direction" (10 min)

**Objectif :** Seul le groupe GRP_Direction a accès en Modification. Tous les autres : aucun accès.

1. Clic droit sur `C:\Data\Direction` → **Propriétés**
2. Onglet **Sécurité**
3. Clic sur **Avancé**
4. **Désactiver l'héritage** → **Supprimer toutes les permissions héritées**
   - ⚠️ Le dossier n'a maintenant PLUS AUCUNE permission (même pas pour vous !)
5. Clic sur **Ajouter**
6. **Sélectionner un principal** → Taper `Administrateurs` → OK
7. **Permissions de base** → Cocher **Contrôle total**
8. **OK**
9. Répéter l'ajout pour `GRP_Direction` :
   - **Ajouter** → `GRP_Direction` → **OK**
   - Cocher **Modification**
   - **OK**
10. **Appliquer** → **OK** → **OK**

✅ **Validation :** 
- Propriétés → Sécurité du dossier Direction affiche :
  - Administrateurs (Contrôle total)
  - GRP_Direction (Modification)

---

#### Étape 4 : Configuration des Autres Dossiers (20 min)

**Appliquer le même principe pour les 4 autres dossiers :**

##### **Dossier Comptabilite**
1. Désactiver l'héritage → Supprimer tout
2. Ajouter **Administrateurs** (Contrôle total)
3. Ajouter **GRP_Comptabilite** (Modification)
4. Ajouter **GRP_Direction** (Lecture seule)

##### **Dossier Commercial**
1. Désactiver l'héritage → Supprimer tout
2. Ajouter **Administrateurs** (Contrôle total)
3. Ajouter **GRP_Commercial** (Modification)
4. Ajouter **GRP_Direction** (Lecture seule)

##### **Dossier Technique**
1. Désactiver l'héritage → Supprimer tout
2. Ajouter **Administrateurs** (Contrôle total)
3. Ajouter **GRP_Technique** (Modification)
4. Ajouter **GRP_Direction** (Lecture seule)

##### **Dossier Commun**
1. Désactiver l'héritage → Supprimer tout
2. Ajouter **Administrateurs** (Contrôle total)
3. Ajouter **GRP_Direction** (Modification)
4. Ajouter **GRP_Comptabilite** (Lecture)
5. Ajouter **GRP_Commercial** (Lecture)
6. Ajouter **GRP_Technique** (Lecture)

---

#### Étape 5 : Tests des Permissions (15 min)

**Créer des fichiers de test dans chaque dossier (en tant qu'admin) :**

1. Dans `Direction` : Créer `StrategieConfidentielle.docx`
2. Dans `Comptabilite` : Créer `Bilan2024.xlsx`
3. Dans `Commercial` : Créer `Contrats.docx`
4. Dans `Technique` : Créer `Documentation.pdf`
5. Dans `Commun` : Créer `Procedures.txt`

---

**Test 1 : Connexion avec "pdubois" (Comptable)**

1. **Déconnexion** → **Se connecter avec pdubois**
2. Aller dans `C:\Data\`
3. Tester :
   - ✅ **Comptabilite** : Double-clic → Doit s'ouvrir, on peut ouvrir et modifier `Bilan2024.xlsx`
   - ❌ **Direction** : Double-clic → "Vous n'avez pas les autorisations..." (accès refusé)
   - ❌ **Commercial** : Accès refusé
   - ❌ **Technique** : Accès refusé
   - ✅ **Commun** : Doit s'ouvrir, on peut lire `Procedures.txt` mais pas le modifier (erreur si on essaie de sauvegarder)

✅ **Validation :** Comportement conforme à la matrice de permissions.

---

**Test 2 : Connexion avec "mmartin" (Directrice)**

1. **Déconnexion** → **Se connecter avec mmartin**
2. Tester :
   - ✅ **Direction** : Accès complet (lecture + modification)
   - ✅ **Comptabilite** : Lecture seule (peut ouvrir `Bilan2024.xlsx` mais erreur si modification)
   - ✅ **Commercial** : Lecture seule
   - ✅ **Technique** : Lecture seule
   - ✅ **Commun** : Accès complet (modification)

✅ **Validation :** La Directrice a accès partout (sauf modification des dossiers métiers, par respect du moindre privilège).

---

**Test 3 : Connexion avec "tpetit" (Stagiaire Commercial)**

1. **Déconnexion** → **Se connecter avec tpetit**
2. Tester :
   - ❌ **Direction** : Accès refusé
   - ❌ **Comptabilite** : Accès refusé
   - ✅ **Commercial** : Accès complet
   - ❌ **Technique** : Accès refusé
   - ✅ **Commun** : Lecture seule

✅ **TP Partie 2 terminé !**

---

### VI. Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|-----------|----------------|
| **Système d'exploitation (OS)** | Logiciel assurant la liaison entre matériel et applications, gérant ressources et utilisateurs |
| **Noyau (Kernel)** | Cœur de l'OS, s'exécutant en mode privilégié avec accès direct au matériel |
| **CLI (Command Line Interface)** | Interface en ligne de commande (texte uniquement) - Ex: PowerShell, Bash |
| **GUI (Graphical User Interface)** | Interface graphique (fenêtres, icônes, souris) - Ex: Windows 10, macOS |
| **Compte utilisateur** | Identité numérique permettant de s'authentifier et d'accéder à des ressources |
| **Compte local** | Compte créé sur une machine spécifique, valable uniquement sur cette machine |
| **Compte de domaine** | Compte créé dans Active Directory, valable sur toutes les machines du domaine |
| **Administrateur** | Compte avec droits complets sur le système (installation, modification, gestion utilisateurs...) |
| **Utilisateur standard** | Compte avec droits limités (usage normal, sans modification système) |
| **Groupe** | Ensemble d'utilisateurs partageant les mêmes droits (facilite la gestion) |
| **UAC (User Account Control)** | Mécanisme Windows demandant confirmation avant actions sensibles |
| **Active Directory (AD)** | Service d'annuaire Microsoft pour gestion centralisée des comptes, machines, stratégies |
| **NTFS** | New Technology File System, système de fichiers Windows avec permissions avancées |
| **ACL (Access Control List)** | Liste des permissions associées à un fichier/dossier (qui peut faire quoi) |
| **Permissions NTFS** | Droits d'accès sur fichiers/dossiers : Lecture, Écriture, Modification, Contrôle total... |
| **Héritage des permissions** | Mécanisme de transmission automatique des permissions du parent aux enfants |
| **Deny (Refuser)** | Permission de refus explicite (prioritaire sur Autoriser) |
| **Allow (Autoriser)** | Permission d'autorisation explicite |
| **Permissions effectives** | Droits réels d'un utilisateur tenant compte de tous ses groupes et héritages |
| **Principe du moindre privilège** | Donner uniquement les droits strictement nécessaires (sécurité maximale) |
| **SAM (Security Account Manager)** | Base de données locale Windows stockant les comptes et mots de passe (hashés) |
| **GPO (Group Policy Object)** | Stratégie de groupe permettant de configurer automatiquement des paramètres (domaine AD) |
| **RGPD** | Règlement Général sur la Protection des Données, impose gestion stricte des droits d'accès |

---

### VII. Questions de Réflexion (Pour aller plus loin)

1. **Pourquoi est-il dangereux d'utiliser un compte Administrateur au quotidien ?**
   - *Piste : Malwares, fausses manipulations, principe moindre privilège*

2. **Un employé quitte l'entreprise. Vaut-il mieux supprimer son compte ou le désactiver ?**
   - *Réponse : Désactiver d'abord (garder traçabilité, récupération fichiers), supprimer après 3-6 mois*

3. **Comment gérer 200 employés sans créer 200 comptes locaux ?**
   - *Réponse : Active Directory (comptes de domaine centralisés)*

4. **Pourquoi utiliser des groupes plutôt que donner des permissions individuellement ?**
   - *Réponse : Gain temps, cohérence, moins d'erreurs, scalabilité*

5. **Un utilisateur a Lecture via le groupe A, Modification via le groupe B, et Deny Écriture via le groupe C. Quel est son accès réel ?**
   - *Réponse : Lecture seule (Deny annule l'autorisation Modification)*

6. **Pourquoi NTFS est-il obligatoire pour les permissions Windows ?**
   - *Réponse : FAT32 ne supporte pas les ACL (permissions)*

7. **Comment un ransomware peut-il chiffrer tous les fichiers d'une entreprise si les utilisateurs sont en comptes standards ?**
   - *Réponse : Il chiffre les fichiers accessibles par l'utilisateur (ses documents + dossiers partagés avec Modification). D'où l'importance de sauvegardes offline !*

---

### VIII. Ressources pour Approfondir

**Documentation Microsoft :**
- [Gestion des comptes utilisateurs locaux](https://learn.microsoft.com/fr-fr/windows/security/identity-protection/access-control/local-accounts)
- [Comprendre les permissions NTFS](https://learn.microsoft.com/fr-fr/windows-server/storage/file-server/ntfs-overview)
- [Principe du moindre privilège](https://learn.microsoft.com/fr-fr/windows-server/identity/ad-ds/plan/security-best-practices/implementing-least-privilege-administrative-models)

**Vidéos YouTube :**
- "Créer des utilisateurs Windows 10" - Tutoriel complet
- "Permissions NTFS expliquées simplement" - Vulgarisation
- "Active Directory pour débutants" - Introduction

**Outils avancés (pour aller plus loin) :**
- **Process Monitor (Sysinternals)** : Voir les accès fichiers en temps réel (détection de permissions manquantes)
- **icacls** (CLI) : Gérer les permissions NTFS en ligne de commande
- **whoami /groups** : Voir tous les groupes dont on est membre

---

### ✅ Auto-évaluation : Suis-je Prêt ?

Après avoir terminé cette séance, je suis capable de :

- [ ] Expliquer les 5 rôles principaux d'un système d'exploitation
- [ ] Différencier Windows, Linux et macOS (avantages, inconvénients, usages)
- [ ] Créer un compte utilisateur local dans Windows (GUI et PowerShell)
- [ ] Expliquer la différence entre compte Administrateur et Utilisateur standard
- [ ] Distinguer compte local et compte de domaine
- [ ] Créer un groupe local et y ajouter des membres
- [ ] Expliquer les 6 permissions NTFS (Lecture, Écriture, Lecture et exécution, Modification, Contrôle total, Spéciales)
- [ ] Configurer des permissions NTFS sur un dossier
- [ ] Comprendre le principe d'héritage des permissions
- [ ] Tester les permissions en me connectant avec différents comptes
- [ ] Appliquer le principe du moindre privilège dans un scénario réel

---

*Fin de la Fiche de Cours Élève - S3 Bloc 2*

---

## 📝 DEVOIR & LIVRABLE PORTFOLIO

### Titre du Devoir

**"Audit et Sécurisation des Accès : Gestion des Utilisateurs et Permissions"**

---

### Contexte Professionnel (Mise en Situation)

Vous êtes **technicien systèmes junior** chez **SecureIT**, une ESN spécialisée dans la sécurité informatique. Votre responsable, M. Leclerc, vous confie une mission d'audit pour un nouveau client :

> *"On a signé un contrat avec **BioMed SARL**, une entreprise de 15 personnes dans le secteur médical (cabinet médical multi-spécialités). Ils ont un serveur Windows Server 2022 avec des dossiers partagés, mais la gestion des droits est catastrophique : tout le monde a accès à tout, y compris aux dossiers patients !*
>
> *C'est une violation du RGPD gravissime. Ils risquent une amende de 20 millions d'euros ou 4% du CA si la CNIL les contrôle.*
>
> *Je veux que tu audites leur situation actuelle, que tu proposes une nouvelle organisation des accès conforme au RGPD, et que tu la mettes en place dans une maquette (VM Windows Server de test). Documente tout, j'en aurai besoin pour justifier notre intervention auprès du client."*

**Informations sur BioMed SARL :**
- **15 employés** répartis en 4 services :
  - **Direction** : Dr Sophie Blanc (médecin directrice)
  - **Secrétariat médical** : Marie Dubois, Claire Martin (secrétaires)
  - **Médecins** : Dr Paul Leroux (généraliste), Dr Emma Garcia (pédiatre), Dr Lucas Bernard (cardiologue)
  - **Infirmiers** : Julie Petit, Thomas Roux
  - **Comptabilité** : Sarah Dupont (comptable)

- **Dossiers actuels sur le serveur** (tous accessibles par tous !) :
  - `\\Serveur\Dossiers_Patients` (fichiers médicaux sensibles - **données de santé**)
  - `\\Serveur\Comptabilite` (factures, salaires)
  - `\\Serveur\Administratif` (plannings, procédures, notes internes)
  - `\\Serveur\Direction` (stratégie, comptes rendus conseil administration)

---

### Consignes du Devoir

#### Partie 1 : Audit de la Situation Actuelle (6 points)

**Objectif :** Analyser les risques de la configuration actuelle.

**À fournir :**

1. **Tableau d'analyse des risques** (4 pts)

Remplir le tableau suivant pour CHAQUE dossier :

| **Dossier** | **Données contenues** | **Niveau de sensibilité (1-5)** | **Risque si accès non autorisé** | **Conformité RGPD ?** |
|-------------|----------------------|--------------------------------|----------------------------------|----------------------|
| Dossiers_Patients | Fichiers médicaux (pathologies, traitements...) | | | |
| Comptabilite | Factures, salaires | | | |
| Administratif | Plannings, procédures | | | |
| Direction | Stratégie, CA | | | |

**Légende niveau de sensibilité :**
- 1 = Public (pas de risque)
- 2 = Usage interne (faible risque)
- 3 = Confidentiel (risque moyen)
- 4 = Très confidentiel (risque élevé)
- 5 = Secret / Données de santé (risque critique)

2. **Identification des violations RGPD** (2 pts)

Lister **3 violations du RGPD** causées par la configuration actuelle (tous les droits à tout le monde).

**Exemple de formulation :**
- *"Violation de l'Article XX : [Nom de l'article]. Le secrétariat médical a accès aux salaires (dossier Comptabilité), ce qui viole le principe de..."*

---

#### Partie 2 : Proposition d'une Nouvelle Organisation (8 points)

**Objectif :** Concevoir une matrice de permissions conforme au RGPD et au principe du moindre privilège.

**À fournir :**

1. **Création de groupes utilisateurs** (2 pts)

Proposer une liste de groupes à créer (minimum 4 groupes).

**Tableau attendu :**

| **Nom du Groupe** | **Membres** | **Justification Métier** |
|-------------------|-------------|--------------------------|
| GRP_Medecins | Dr Blanc, Dr Leroux, Dr Garcia, Dr Bernard | Accès dossiers patients (secret médical) |
| ... | ... | ... |

2. **Matrice de permissions** (4 pts)

Remplir la matrice suivante :

| **Dossier** | **GRP_...** | **GRP_...** | **GRP_...** | **GRP_...** | **Justification** |
|-------------|-------------|-------------|-------------|-------------|-------------------|
| Dossiers_Patients | Modification | Lecture | Aucun | Aucun | Seuls médecins modifient, secrétariat consulte pour plannings |
| Comptabilite | | | | | |
| Administratif | | | | | |
| Direction | | | | | |

**Permissions possibles :**
- Contrôle total
- Modification
- Lecture
- Aucun accès

3. **Mesures de sécurité complémentaires** (2 pts)

Proposer **3 mesures supplémentaires** pour renforcer la sécurité :

Exemples :
- Activer l'audit des accès (logs NTFS)
- Imposer des mots de passe forts (12 caractères minimum)
- Chiffrer le dossier Dossiers_Patients (EFS)
- ...

---

#### Partie 3 : Mise en Pratique (Maquette VM) (6 points)

**Objectif :** Implémenter la solution proposée dans une VM Windows Server 2022.

**À réaliser dans la VM :**

1. **Création des comptes utilisateurs** (1 pt)
   - Créer 8 comptes (au moins 1 par service)
   - Convention : `prenom.nom` (ex: `sophie.blanc`)
   - Mot de passe : `BioMed2024!`

2. **Création des groupes locaux** (1 pt)
   - Créer les 4+ groupes proposés en Partie 2
   - Ajouter les membres correspondants

3. **Création de la structure de dossiers** (1 pt)
   - Créer `C:\Partages\` puis les 4 sous-dossiers

4. **Configuration des permissions NTFS** (2 pts)
   - Appliquer la matrice de permissions de la Partie 2
   - Désactiver l'héritage sur chaque dossier
   - Supprimer les permissions par défaut (sauf Administrateurs)

5. **Tests et captures d'écran** (1 pt)
   - Tester avec 2 comptes différents (1 médecin, 1 secrétaire)
   - Prendre 4 captures d'écran :
     - Connexion médecin → accès Dossiers_Patients ✅
     - Connexion médecin → refus Comptabilite ❌
     - Connexion secrétaire → lecture Dossiers_Patients ✅
     - Connexion secrétaire → refus Direction ❌

**Captures d'écran obligatoires :**
- Fenêtre Propriétés → Sécurité de chaque dossier (montrant les permissions)
- Tests d'accès (message d'erreur ou ouverture réussie)

---

### Critères d'Évaluation (Barème Qualiopi)

| **Critère** | **Points** | **Indicateurs de Réussite** |
|-------------|------------|------------------------------|
| **Analyse des risques (Partie 1.1)** | /4 | Tableau complet, niveaux cohérents, risques identifiés pertinents |
| **Violations RGPD (Partie 1.2)** | /2 | 3 violations correctement identifiées avec références articles RGPD |
| **Création groupes (Partie 2.1)** | /2 | Minimum 4 groupes, membres répartis logiquement, justifications métier claires |
| **Matrice permissions (Partie 2.2)** | /4 | 4 dossiers configurés, permissions cohérentes, principe moindre privilège respecté |
| **Mesures complémentaires (Partie 2.3)** | /2 | 3 mesures pertinentes et justifiées |
| **Maquette VM - Comptes (Partie 3.1)** | /1 | 8 comptes créés avec convention correcte |
| **Maquette VM - Groupes (Partie 3.2)** | /1 | Groupes créés avec bons membres |
| **Maquette VM - Structure (Partie 3.3)** | /1 | 4 dossiers créés dans C:\Partages\ |
| **Maquette VM - Permissions (Partie 3.4)** | /2 | Permissions appliquées conformément à la matrice, héritage désactivé |
| **Maquette VM - Tests (Partie 3.5)** | /1 | 4 captures d'écran probantes |
| **Présentation et orthographe** | /2 | Document professionnel, structuré, sans fautes majeures |
| **TOTAL** | **/20** | |

**Bonus (+2 pts max) :**
- Script PowerShell de création automatique des comptes et groupes (+1 pt)
- Activation de l'audit NTFS avec captures d'écran des logs (+1 pt)
- Chiffrement EFS sur Dossiers_Patients avec test (+1 pt)
*(Maximum +2 points au total)*

---

### Modalités de Rendu

- **Format :** 
  - Document Word (.docx) ou PDF pour les Parties 1 et 2
  - Dossier compressé (.zip) contenant :
    - Le document Word/PDF
    - Les captures d'écran (nommées explicitement : `capture1_medecin_acces_patients.png`, etc.)
    - (Optionnel) Script PowerShell si bonus
- **Nom du fichier :** `NOM_Prenom_S3_Devoir_Audit_Permissions.zip`
- **Taille maximale :** 20 Mo
- **Deadline :** Avant le début de la séance **S4**
- **Dépôt :** Via l'ENT / Plateforme Moodle

---

### Compétences RNCP Mobilisées

| **Code** | **Compétence** | **Niveau** |
|----------|----------------|------------|
| **B1.2** | Mettre à disposition des utilisateurs un service informatique - Gérer des utilisateurs et des droits | **Maîtrise** |
| **B2.1** | Administrer les services d'un système d'exploitation serveur | Application |
| **B3.1** | Protéger les données à caractère personnel - Gestion des droits d'accès | Application |
| **B1.6** | Organiser son développement professionnel - Audit et documentation | Application |

---

### Ressources Autorisées

✅ **Autorisé :**
- Votre fiche de cours S3
- Vos notes personnelles du TP
- Documentation Microsoft officielle
- Textes du RGPD (notamment Articles 5, 25, 32)
  - [RGPD.fr](https://www.cnil.fr/fr/reglement-europeen-protection-donnees)
- Recherches web sur les bonnes pratiques de gestion des droits

❌ **Interdit :**
- Copier-coller intégral de matrices de permissions trouvées en ligne
- Plagiat entre étudiants

---

### Lien avec le Portfolio (E4 / E5)

Ce devoir constitue une **situation professionnelle exploitable** pour vos **épreuves E4 et E5** :

- **E4 (Oral - Portefeuille de compétences)** :
  - **Contexte** : Mission d'audit sécurité pour un cabinet médical (secteur santé = sensible)
  - **Production** : Matrice de permissions + maquette fonctionnelle
  - **Compétences** : B1.2 (Gestion utilisateurs/droits), B3.1 (Protection données personnelles), conformité RGPD

- **E5 (Pratique)** :
  - Type de manipulation fréquemment demandée à l'épreuve pratique
  - Création comptes/groupes + permissions NTFS = compétence fondamentale SISR

💡 **Conseil :** 
- Conservez ce devoir dans votre **portfolio numérique**
- Rédigez une fiche récapitulative (1 page) :
  - Contexte de la mission
  - Problématique (non-conformité RGPD)
  - Solution apportée (matrice permissions)
  - Résultats (sécurité renforcée, conformité)
  - Difficultés rencontrées et solutions trouvées

---

## ✅ CORRECTION ATTENDUE DU DEVOIR

*(Fournie aux enseignants uniquement - À distribuer APRÈS la remise des copies)*

### Partie 1 : Audit de la Situation Actuelle

#### 1. Tableau d'Analyse des Risques

| **Dossier** | **Données contenues** | **Niveau de sensibilité** | **Risque si accès non autorisé** | **Conformité RGPD ?** |
|-------------|----------------------|---------------------------|----------------------------------|----------------------|
| **Dossiers_Patients** | Dossiers médicaux (pathologies, traitements, antécédents, résultats analyses) | **5 (Critique)** | Violation du **secret médical** (Code Santé Publique), fuite de **données de santé** (catégorie spéciale RGPD Art. 9), risque de **chantage**, discrimination, perte de **confiance patients** | ❌ **NON** - Violation Art. 9 (données sensibles), Art. 32 (mesures sécurité) |
| **Comptabilite** | Factures patients, salaires employés, charges, trésorerie | **4 (Très confidentiel)** | Connaissance des **salaires** (conflits internes), vol de **données bancaires patients**, détournement de fonds | ❌ **NON** - Violation Art. 32 (accès non restreint), Art. 5 (principe de limitation) |
| **Administratif** | Plannings consultations, procédures internes, notes service, organigramme | **2-3 (Usage interne)** | Risque faible : fuite de planning (perturbation organisation), mais pas de données personnelles critiques | ⚠️ **PARTIEL** - Acceptable si tous les employés, mais secrétariat devrait gérer |
| **Direction** | Stratégie entreprise, comptes rendus CA, projets confidentiels, décisions RH | **4 (Très confidentiel)** | Fuite de **stratégie** (avantage concurrence), connaissance de **décisions RH** avant annonce (démissions, licenciements) | ❌ **NON** - Violation principe "besoin d'en connaître" (Art. 5, 32) |

---

#### 2. Violations RGPD Identifiées

**Violation 1 : Article 9 - Traitement de catégories particulières de données**

> *"Les données de santé sont des **catégories particulières de données** nécessitant des mesures de protection renforcées. Actuellement, le dossier `Dossiers_Patients` est accessible par **tous les employés**, y compris la comptable Sarah Dupont qui n'a **aucun besoin professionnel** d'accéder aux pathologies des patients. Cela viole l'Article 9 qui interdit le traitement de données de santé sauf exceptions strictes (consentement, nécessité médicale). De plus, cela viole le **secret médical** (Code de la Santé Publique Article L1110-4)."*

**Sanction possible :** Amende jusqu'à **20 millions € ou 4% du CA** (sanction maximale RGPD).

---

**Violation 2 : Article 32 - Sécurité du traitement**

> *"L'Article 32 impose au responsable de traitement de mettre en œuvre des **mesures techniques et organisationnelles** pour garantir la sécurité des données personnelles. Donner un accès total à tous les employés (y compris aux salaires dans le dossier Comptabilité) constitue un **manque flagrant de mesures de sécurité**. Aucune authentification différenciée, aucun contrôle d'accès = vulnérabilité majeure."*

---

**Violation 3 : Article 5.1.c - Minimisation des données (Principe de limitation)**

> *"Le principe de minimisation impose de limiter l'accès aux données au **strict nécessaire**. Un infirmier n'a pas besoin d'accéder aux dossiers de comptabilité. Un secrétaire n'a pas besoin d'accéder à la stratégie de direction. La configuration actuelle viole ce principe en donnant un accès universel sans distinction de fonction."*

---

### Partie 2 : Proposition d'une Nouvelle Organisation

#### 1. Création de Groupes Utilisateurs

| **Nom du Groupe** | **Membres** | **Justification Métier** |
|-------------------|-------------|--------------------------|
| **GRP_Medecins** | Dr Sophie Blanc, Dr Paul Leroux, Dr Emma Garcia, Dr Lucas Bernard | Secret professionnel médical : seuls les médecins peuvent **consulter et modifier** les dossiers patients (diagnostic, prescription, notes médicales) |
| **GRP_Secretariat** | Marie Dubois, Claire Martin | Besoin de **consulter** les dossiers patients pour planification RDV, envoi de courriers, mais **pas de modification** du contenu médical (respect périmètre métier) |
| **GRP_Infirmiers** | Julie Petit, Thomas Roux | Besoin de **consulter** certaines informations patients (allergies, traitements en cours) pour administration soins, mais accès limité (pas tout le dossier médical complet - à affiner selon organisation réelle) |
| **GRP_Comptabilite** | Sarah Dupont | Accès exclusif au dossier Comptabilité (factures, salaires, trésorerie). **Aucun accès** aux dossiers médicaux (séparation stricte métiers) |
| **GRP_Direction** | Dr Sophie Blanc (en tant que directrice) | Accès stratégique aux documents de Direction. Accès en lecture aux autres dossiers pour supervision (sauf modification, respect métiers) |

💡 **Note :** Dr Sophie Blanc est membre de 2 groupes (Médecins + Direction) car elle a une double casquette.

---

#### 2. Matrice de Permissions

| **Dossier** | **GRP_Medecins** | **GRP_Secretariat** | **GRP_Infirmiers** | **GRP_Comptabilite** | **GRP_Direction** | **Justification** |
|-------------|------------------|---------------------|--------------------|--------------------|-------------------|-------------------|
| **Dossiers_Patients** | **Modification** | **Lecture** | **Lecture** | **Aucun** | **Lecture** | Médecins créent/modifient dossiers. Secrétariat consulte pour organisation. Comptabilité n'a pas besoin (facturation séparée). Direction supervise. |
| **Comptabilite** | **Aucun** | **Aucun** | **Aucun** | **Modification** | **Lecture** | Seule la comptable gère ce dossier (salaires = confidentiel). Direction consulte pour pilotage financier. Médecins/Infirmiers/Secrétariat n'ont pas besoin. |
| **Administratif** | **Lecture** | **Modification** | **Lecture** | **Lecture** | **Modification** | Secrétariat gère plannings et procédures (Modification). Tous les autres consultent (organisation commune). Direction modifie pour notes de service. |
| **Direction** | **Aucun** | **Aucun** | **Aucun** | **Aucun** | **Modification** | Exclusivement Direction (stratégie, CA, RH = très confidentiel). Principe besoin d'en connaître strict. |

**Commentaires importants :**

- 🔒 **Dossiers_Patients** : Accès le plus restreint (données de santé). Infirmiers en lecture car besoin pour administration soins, mais à **affiner** selon organisation (possibilité de créer sous-dossier "Soins infirmiers" avec permissions différentes).

- 🔒 **Comptabilite** : Isolation stricte (salaires = confidentiel RH). Seule la comptable + Direction.

- 📋 **Administratif** : Dossier "commun" où secrétariat a la main (organisation), tous les autres consultent.

- 🚫 **Direction** : "Need to know basis" strict. Seule la direction.

---

#### 3. Mesures de Sécurité Complémentaires

**Mesure 1 : Activer l'audit NTFS sur les dossiers sensibles**

- **Description** : Configurer Windows Server pour **enregistrer tous les accès** (lectures, modifications, suppressions) aux dossiers `Dossiers_Patients` et `Comptabilite`.
- **Objectif** : Traçabilité complète (qui a accédé à quel dossier, quand). En cas de fuite de données, possibilité d'identifier la source.
- **Mise en œuvre** : 
  - Activer l'audit via GPO (Stratégie Audit d'accès aux objets)
  - Configurer SACL (System Access Control List) sur les dossiers sensibles
  - Consulter les logs dans **Observateur d'événements** (Event Viewer) → Sécurité

---

**Mesure 2 : Chiffrement du dossier Dossiers_Patients (EFS ou BitLocker)**

- **Description** : Chiffrer le contenu du dossier `Dossiers_Patients` pour qu'en cas de vol physique du serveur ou du disque dur, les données restent **illisibles** sans la clé de déchiffrement.
- **Objectif** : Protection contre vol matériel, conformité RGPD Article 32 (chiffrement recommandé pour données sensibles).
- **Mise en œuvre** :
  - **EFS** (Encrypting File System) : Chiffrement au niveau fichier, automatique, transparent pour utilisateurs autorisés
  - **BitLocker** : Chiffrement de l'intégralité du disque (plus robuste)

---

**Mesure 3 : Politique de mots de passe forts et renouvellement obligatoire**

- **Description** : Imposer via GPO (ou politique locale si pas de domaine) :
  - Longueur minimum : **12 caractères**
  - Complexité obligatoire (majuscule + minuscule + chiffre + caractère spécial)
  - Durée de vie maximale : **90 jours** (renouvellement obligatoire)
  - Historique : **5 derniers mots de passe** non réutilisables
- **Objectif** : Empêcher les mots de passe faibles (ex: "123456") ou devinables (ex: "BioMed2024"). Réduire risque de compromission de comptes.
- **Mise en œuvre** : GPO → Configuration ordinateur → Paramètres Windows → Paramètres de sécurité → Stratégies de compte → Stratégie de mot de passe

---

**Mesure 4 (Bonus) : Authentification à deux facteurs (2FA) pour accès aux dossiers patients**

- **Description** : Exiger un second facteur d'authentification (SMS, application mobile, clé physique) pour accéder au dossier `Dossiers_Patients`.
- **Objectif** : Protection maximale contre usurpation d'identité (même si mot de passe volé, accès bloqué sans 2FA).

---

**Mesure 5 (Bonus) : Formation RGPD des employés**

- **Description** : Session de formation annuelle obligatoire pour tous les employés sur :
  - Principe du RGPD
  - Risques de fuite de données
  - Bonnes pratiques (verrouillage session, mots de passe, phishing...)
- **Objectif** : Sensibilisation (facteur humain = maillon faible de la sécurité). Conformité Article 32.4 (formation du personnel).

---

### Partie 3 : Mise en Pratique (Maquette VM)

#### Comptes Utilisateurs à Créer

**Commandes PowerShell (exemple de script) :**

```powershell
# Script de création automatique des comptes BioMed SARL
# À exécuter en tant qu'Administrateur sur Windows Server 2022

# Tableau des utilisateurs (Nom, Prénom, Service)
$utilisateurs = @(
    @{Nom="Blanc"; Prenom="Sophie"; Service="Direction"},
    @{Nom="Dubois"; Prenom="Marie"; Service="Secretariat"},
    @{Nom="Martin"; Prenom="Claire"; Service="Secretariat"},
    @{Nom="Leroux"; Prenom="Paul"; Service="Medecins"},
    @{Nom="Garcia"; Prenom="Emma"; Service="Medecins"},
    @{Nom="Bernard"; Prenom="Lucas"; Service="Medecins"},
    @{Nom="Petit"; Prenom="Julie"; Service="Infirmiers"},
    @{Nom="Roux"; Prenom="Thomas"; Service="Infirmiers"},
    @{Nom="Dupont"; Prenom="Sarah"; Service="Comptabilite"}
)

# Mot de passe commun (à changer à la première connexion en production)
$mdp = ConvertTo-SecureString "BioMed2024!" -AsPlainText -Force

# Création des comptes
foreach ($user in $utilisateurs) {
    $login = "$($user.Prenom.ToLower()).$($user.Nom.ToLower())"
    $nomComplet = "$($user.Prenom) $($user.Nom)"
    
    New-LocalUser -Name $login -Password $mdp -FullName $nomComplet -Description $user.Service
    Write-Host "Compte créé : $login ($nomComplet - $($user.Service))" -ForegroundColor Green
}

Write-Host "`nTous les comptes ont été créés avec succès !" -ForegroundColor Cyan
```

**Liste des 9 comptes créés :**
1. `sophie.blanc` - Dr Sophie Blanc (Direction + Médecin)
2. `marie.dubois` - Marie Dubois (Secrétariat)
3. `claire.martin` - Claire Martin (Secrétariat)
4. `paul.leroux` - Dr Paul Leroux (Médecin)
5. `emma.garcia` - Dr Emma Garcia (Médecin)
6. `lucas.bernard` - Dr Lucas Bernard (Médecin)
7. `julie.petit` - Julie Petit (Infirmier)
8. `thomas.roux` - Thomas Roux (Infirmier)
9. `sarah.dupont` - Sarah Dupont (Comptabilité)

---

#### Groupes Locaux à Créer

**Commandes PowerShell :**

```powershell
# Création des groupes
New-LocalGroup -Name "GRP_Medecins" -Description "Personnel médical avec accès dossiers patients"
New-LocalGroup -Name "GRP_Secretariat" -Description "Secrétariat médical"
New-LocalGroup -Name "GRP_Infirmiers" -Description "Personnel infirmier"
New-LocalGroup -Name "GRP_Comptabilite" -Description "Service comptabilité"
New-LocalGroup -Name "GRP_Direction" -Description "Direction de l'établissement"

# Ajout des membres aux groupes
# Groupe Médecins
Add-LocalGroupMember -Group "GRP_Medecins" -Member "sophie.blanc"
Add-LocalGroupMember -Group "GRP_Medecins" -Member "paul.leroux"
Add-LocalGroupMember -Group "GRP_Medecins" -Member "emma.garcia"
Add-LocalGroupMember -Group "GRP_Medecins" -Member "lucas.bernard"

# Groupe Secrétariat
Add-LocalGroupMember -Group "GRP_Secretariat" -Member "marie.dubois"
Add-LocalGroupMember -Group "GRP_Secretariat" -Member "claire.martin"

# Groupe Infirmiers
Add-LocalGroupMember -Group "GRP_Infirmiers" -Member "julie.petit"
Add-LocalGroupMember -Group "GRP_Infirmiers" -Member "thomas.roux"

# Groupe Comptabilité
Add-LocalGroupMember -Group "GRP_Comptabilite" -Member "sarah.dupont"

# Groupe Direction
Add-LocalGroupMember -Group "GRP_Direction" -Member "sophie.blanc"

Write-Host "Groupes créés et membres ajoutés !" -ForegroundColor Cyan
```

---

#### Structure de Dossiers

**Commandes PowerShell :**

```powershell
# Création de la structure
New-Item -Path "C:\Partages" -ItemType Directory
New-Item -Path "C:\Partages\Dossiers_Patients" -ItemType Directory
New-Item -Path "C:\Partages\Comptabilite" -ItemType Directory
New-Item -Path "C:\Partages\Administratif" -ItemType Directory
New-Item -Path "C:\Partages\Direction" -ItemType Directory

Write-Host "Structure de dossiers créée dans C:\Partages\" -ForegroundColor Green
```

---

#### Configuration Permissions NTFS (Exemple pour Dossiers_Patients)

**Méthode CLI (icacls) :**

```powershell
# Dossier Dossiers_Patients
$dossier = "C:\Partages\Dossiers_Patients"

# Désactiver l'héritage et supprimer les permissions héritées
icacls $dossier /inheritance:r

# Ajouter Administrateurs en Contrôle Total
icacls $dossier /grant "Administrateurs:(OI)(CI)F"

# Ajouter GRP_Medecins en Modification
icacls $dossier /grant "GRP_Medecins:(OI)(CI)M"

# Ajouter GRP_Secretariat en Lecture
icacls $dossier /grant "GRP_Secretariat:(OI)(CI)R"

# Ajouter GRP_Infirmiers en Lecture
icacls $dossier /grant "GRP_Infirmiers:(OI)(CI)R"

# Ajouter GRP_Direction en Lecture
icacls $dossier /grant "GRP_Direction:(OI)(CI)R"

Write-Host "Permissions configurées sur $dossier" -ForegroundColor Green
```

**Légende paramètres icacls :**
- `(OI)` = Object Inherit (héritage vers fichiers)
- `(CI)` = Container Inherit (héritage vers sous-dossiers)
- `F` = Full Control (Contrôle total)
- `M` = Modify (Modification)
- `R` = Read (Lecture)

---

**Répéter pour les 3 autres dossiers avec les permissions de la matrice.**

---

#### Tests Attendus (Captures d'Écran)

**Capture 1 : Connexion médecin → Accès Dossiers_Patients ✅**
- Se connecter avec `paul.leroux`
- Ouvrir `C:\Partages\Dossiers_Patients`
- Créer un fichier de test `Patient_Test.txt`
- ✅ Doit fonctionner (Modification autorisée)
- **Capture d'écran** : Fenêtre Explorateur montrant le fichier créé

---

**Capture 2 : Connexion médecin → Refus Comptabilite ❌**
- Toujours connecté avec `paul.leroux`
- Essayer d'ouvrir `C:\Partages\Comptabilite`
- ❌ Message d'erreur "Vous n'avez pas les autorisations nécessaires..."
- **Capture d'écran** : Message d'erreur Windows

---

**Capture 3 : Connexion secrétaire → Lecture Dossiers_Patients ✅**
- Se déconnecter → Se connecter avec `marie.dubois`
- Ouvrir `C:\Partages\Dossiers_Patients`
- Ouvrir le fichier `Patient_Test.txt` créé précédemment
- Essayer de le modifier et sauvegarder
- ❌ Message d'erreur à la sauvegarde (Lecture seule)
- **Capture d'écran** : Fichier ouvert + message d'erreur sauvegarde

---

**Capture 4 : Connexion secrétaire → Refus Direction ❌**
- Toujours connecté avec `marie.dubois`
- Essayer d'ouvrir `C:\Partages\Direction`
- ❌ Message d'erreur "Accès refusé"
- **Capture d'écran** : Message d'erreur

---

### Grille de Correction Détaillée (Enseignant)

| Critère | 0 pt | 1 pt | 2 pts | 3-4 pts |
|---------|------|------|-------|---------|
| **Analyse risques** | <2 dossiers | 2-3 dossiers incomplets | 4 dossiers, niveaux cohérents | 4 dossiers, analyse détaillée et pertinente |
| **Violations RGPD** | <2 violations ou incorrectes | 2 violations peu détaillées | 3 violations identifiées | 3 violations avec articles RGPD corrects |
| **Groupes** | <3 groupes | 3-4 groupes, justifications faibles | 4+ groupes, membres corrects | 4+ groupes, répartition logique, justifications métier claires |
| **Matrice permissions** | <2 dossiers configurés | 2-3 dossiers, permissions incohérentes | 4 dossiers, permissions globalement correctes | 4 dossiers, moindre privilège respecté, justifications |
| **Mesures complémentaires** | <2 mesures | 2 mesures peu pertinentes | 3 mesures pertinentes | 3 mesures justifiées et réalistes |
| **Maquette - Comptes/Groupes** | <4 comptes | 4-6 comptes, groupes partiels | 8 comptes, groupes créés | 8+ comptes, groupes avec bons membres |
| **Maquette - Permissions** | Permissions non configurées | 1-2 dossiers configurés | 3-4 dossiers, erreurs mineures | 4 dossiers, conformes à la matrice |
| **Tests captures** | <2 captures | 2-3 captures non probantes | 4 captures, certaines floues | 4 captures claires et pertinentes |

**Bonus :**
- Script PowerShell complet et fonctionnel (+1 pt)
- Audit NTFS activé avec logs (+1 pt)
- Chiffrement EFS démontré (+1 pt)

---

*Fin du Pack Semaine 3 - Bloc 2*

---

**🎉 Pack S3 - Bloc 2 terminé !**

Ce pack complet contient :
- ✅ **Fiche Enseignant** détaillée (planning 4h, différenciation, points vigilance, Qualiopi)
- ✅ **Activité Découverte** ludique et concrète (jeu de rôles "Qui peut faire quoi ?")
- ✅ **Fiche Cours Élève** exhaustive (OS, comptes, permissions NTFS, vocabulaire)
- ✅ **2 TP Guidés** pas-à-pas (création comptes 30min + permissions NTFS 60min)
- ✅ **Devoir Portfolio** contextualisé secteur médical (audit RGPD + maquette)
- ✅ **Correction Détaillée** avec scripts PowerShell et grille enseignant

**Souhaitez-vous que je continue avec :**
- **S3 - Bloc 1** (Introduction à la gestion de parc, inventaire) ?
- **S3 - Bloc 3** (Menaces : ransomware, phishing, ingénierie sociale) ?
- **S3 - CEJMA** (Métiers du numérique : DSI, RSSI, Chef de projet) ?
- **S3 - Maths Informatique** (Codage de l'information, ASCII, Unicode) ?
- **S4 - Bloc 2** (Active Directory : installation contrôleur domaine, gestion comptes/GPO) ?

Dites-moi ce qui vous serait le plus utile ! 🚀
