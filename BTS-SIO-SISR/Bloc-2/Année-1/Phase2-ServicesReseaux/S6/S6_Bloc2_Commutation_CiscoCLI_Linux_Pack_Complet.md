# Pack de Formation - Semaine 6 (S6) - BLOC 2
## "Commutation, Cisco CLI et Linux : Commandes de Base"

---

## 📋 FICHE ENSEIGNANT

### Informations Générales

| **Élément** | **Détails** |
|-------------|-------------|
| **Semaine** | S6 - Année 1 |
| **Bloc** | Bloc 2 - Infrastructure, Systèmes & Réseaux |
| **Durée** | 4 heures (1 séance) |
| **Phase** | Phase 2 - Services réseau, administration & RGPD |
| **Public** | Apprentis BTS SIO SISR (hétérogène : Bac Pro CIEL + débutants) |
| **Prérequis** | S4 (modèle OSI, LAN/WAN, câblage RJ45) - S5 (IPv4, ARP, ICMP, Debian installé) |

### Compétences RNCP Visées

| **Code Compétence** | **Libellé** | **Niveau de Maîtrise** |
|---------------------|-------------|------------------------|
| **B2.2** | Installer, tester et déployer une solution d'infrastructure réseau - Configurer un switch | **Application** |
| **B2.3** | Exploiter, dépanner et superviser - Commandes show et diagnostic | Application |
| **B2.1** | Administrer les services d'un système d'exploitation - Commandes Linux | Application |

### Objectifs Pédagogiques

**À l'issue de cette séance, l'apprenant sera capable de :**

1. **Expliquer** le fonctionnement d'un switch (apprentissage table MAC, forwarding, flooding)
2. **Différencier** domaine de collision et domaine de diffusion (broadcast)
3. **Comparer** switch et hub (performances, sécurité, domaines)
4. **Accéder** à la CLI d'un équipement Cisco via câble console (PuTTY / Packet Tracer)
5. **Naviguer** entre les 3 modes CLI Cisco (User EXEC, Privileged EXEC, Global Config)
6. **Configurer** les éléments de base d'un switch Cisco (hostname, banner, passwords, save)
7. **Utiliser** les commandes `show` pour vérifier une configuration
8. **Maîtriser** les commandes Linux fondamentales (ls, cd, cp, mv, rm, mkdir, cat, nano)

---

### Planning de Séance (4h)

| **Horaire** | **Durée** | **Activité** | **Modalité** | **Objectif** |
|-------------|-----------|--------------|--------------|--------------|
| **00:00 - 00:10** | 10 min | Rappel S5 (ARP, ping, config IP) + annonce | Collectif | Réactiver |
| **00:10 - 00:40** | 30 min | **Activité Découverte** : "Le Central Téléphonique" (simulation table MAC) | Groupes de 5 | Comprendre la commutation |
| **00:40 - 01:15** | 35 min | Apport théorique : Commutation (table MAC, flooding, forwarding, domaines) | Collectif | Structurer |
| **01:15 - 01:45** | 30 min | Apport théorique : Cisco CLI (modes, commandes show) | Collectif + démo Packet Tracer | Découvrir la CLI |
| **01:45 - 02:00** | 15 min | **Pause** | - | - |
| **02:00 - 02:55** | 55 min | **TP Cisco Packet Tracer** : Configurer un switch (hostname, banner, passwords, save) | Individuel encadré | Pratiquer la CLI |
| **02:55 - 04:00** | 65 min | **TP Linux** : Commandes de base (ls, cd, cp, mv, rm, mkdir, cat, nano) - sur VM Debian S5 | Individuel encadré | Maîtriser le terminal |

---

### Matériel Nécessaire

| **Type** | **Quantité** | **Description** |
|----------|--------------|-----------------|
| **PC Windows 10/11** | 1 par apprenant | Pour Packet Tracer + VM Debian |
| **Packet Tracer 8.x** | Installé | Voir S5 pour installation |
| **VM Debian 12** | 1 par apprenant | Installée en S5, déjà fonctionnelle |
| **Cartes de rôles** | 1 jeu par groupe | Pour l'activité découverte (5 rôles imprimés) |
| **Fiche aide-mémoire CLI Cisco** | 1 par apprenant | Modes + commandes de base (imprimée) |
| **Fiche aide-mémoire Linux** | 1 par apprenant | Commandes fondamentales (imprimée) |

**Vérification avant la séance :**
- ✅ Packet Tracer fonctionnel sur tous les PC
- ✅ VM Debian démarre correctement sur tous les PC
- ✅ Fiches aide-mémoire imprimées en quantité

---

### Conseils de Différenciation Pédagogique

#### Pour les apprenants **Bac Pro CIEL** (déjà familiers)

- **Commutation** : Expliquer Spanning Tree Protocol (STP) et pourquoi il est nécessaire (boucles). Observer le STP avec `show spanning-tree` dans Packet Tracer.
- **Cisco CLI avancé** :
  - Configurer les lignes VTY (accès Telnet/SSH)
  - Configurer une adresse IP sur le VLAN de gestion
  - Explorer `show mac address-table` sur un switch avec trafic
- **Linux avancé** : Permissions (`chmod`, `chown`), redirections (`>`, `>>`, `|`), recherche (`grep`, `find`)
- **Mission complémentaire** : Script bash qui crée une arborescence de dossiers automatiquement

#### Pour les apprenants **débutants**

- **Activité découverte** : Enseignant joue le rôle du switch pour guider la simulation
- **CLI Cisco** : Fiche procédure illustrée avec captures Packet Tracer à chaque étape. Validation enseignant après chaque mode de navigation.
- **Linux** : Se limiter aux 6 commandes essentielles (ls, cd, mkdir, cp, mv, rm) avant nano et cat. Binômage avec Bac Pro CIEL.
- **Astuce** : Rappeler régulièrement `Tab` pour la complétion automatique (Cisco ET Linux)

---

### Points de Vigilance

⚠️ **Table MAC - Durée de vie (aging) :**
- Les entrées expirent par défaut après **300 secondes** (5 minutes) sur Cisco
- Commande : `show mac address-table aging-time`
- Si une machine est inactive, son entrée disparaît → flooding au prochain paquet

⚠️ **CLI Cisco - Erreurs fréquentes :**
- `%Invalid input detected at '^' marker` : Commande tapée dans le mauvais mode
- Oubli de `no shutdown` sur une interface → reste down
- Oubli de `copy run start` → configuration perdue au redémarrage
- `enable` ne demande pas de mot de passe **si pas configuré** (pas d'erreur = normal au début)

⚠️ **Banner MOTD - Syntaxe :**
- Le **délimiteur** doit être un caractère qui N'APPARAÎT PAS dans le message
- Convention : `#` ou `$`
- Syntaxe : `banner motd #<Entrée>Message<Entrée>#`
- ⚠️ Si le délimiteur est dans le message → le banner s'arrête prématurément

⚠️ **`enable secret` vs `enable password` :**
- `enable password` : mot de passe en **clair** dans la config (déconseillé)
- `enable secret` : mot de passe **chiffré MD5** (à privilégier toujours)
- Si les deux sont configurés : `enable secret` **prend le dessus**

⚠️ **Linux - Commandes destructives :**
- `rm -rf` sans chemin peut être catastrophique (supprimer des fichiers système)
- Insister : **vérifier deux fois le chemin avant de supprimer**
- Sur VM de TP : risque limité, mais prendre l'habitude

⚠️ **Linux - Distinction `cat` et `nano` :**
- `cat` = **lire** le contenu (affichage dans le terminal)
- `nano` = **éditer** le contenu (mode interactif)

---

### Évaluation et Traces d'Apprentissage

| **Type d'évaluation** | **Modalité** | **Critères** |
|-----------------------|--------------|--------------|
| **Diagnostique** | Rappel oral S5 (ARP, ping) | Compréhension adressage/connectivité |
| **Formative (activité)** | Observation simulation | Compréhension flooding/forwarding |
| **Formative (TP Cisco)** | Validation enseignant + `show run` | Switch configuré, passwords actifs, sauvegardé |
| **Formative (TP Linux)** | Validation enseignant + arborescence | Commandes maîtrisées, arborescence créée |
| **Livrable Portfolio** | Devoir maison (voir section) | Configuration switch complète + guide Linux |

---

### Lien avec le Référentiel Qualiopi

- ✅ **Objectifs mesurables** (8 objectifs, tous vérifiables en TP)
- ✅ **Adaptation hétérogène** (STP/VTY pour CIEL, procédure guidée débutants)
- ✅ **Évaluations formalisées** (diagnostique + formative + portfolio)
- ✅ **Traçabilité** (fichier Packet Tracer + arborescence Linux comme preuves)
- ✅ **Lien RNCP** (B2.2, B2.3, B2.1)
- ✅ **Progression logique** : S5 câblage/ARP/IPv4 → S6 équipement d'interconnexion + CLI

---

### Ressources Complémentaires pour l'Enseignant

**Commandes Cisco IOS essentielles pour cette séance :**

```cisco
! === NAVIGATION MODES ===
enable                              ! User EXEC → Privileged EXEC
configure terminal                  ! Privileged EXEC → Global Config
exit                                ! Remonter d'un niveau
end                                 ! Revenir directement en Privileged EXEC
Ctrl+Z                              ! Équivalent de "end"

! === CONFIG DE BASE SWITCH ===
hostname MonSwitch                  ! Renommer l'équipement
banner motd #                       ! Configurer le message du jour
  Acces autorise uniquement
  au personnel habilite !
#
enable secret Cisco123              ! Mot de passe mode privileged (chiffré)
no enable password                  ! Supprimer l'ancien password si existant
service password-encryption         ! Chiffrer tous les mots de passe en clair

line console 0                      ! Configurer la ligne console
  password Console1                 ! Mot de passe console
  login                             ! Activer l'authentification
  exec-timeout 5 0                  ! Déconnexion auto après 5 min d'inactivité
  exit

line vty 0 15                       ! Configurer les 16 lignes virtuelles (Telnet/SSH)
  password Telnet1
  login
  exec-timeout 5 0
  exit

! === SAUVEGARDE ===
copy running-config startup-config  ! Sauvegarder (RAM → Flash)
copy run start                      ! Version courte
write memory                        ! Autre syntaxe (ancienne, toujours valide)
erase startup-config                ! Effacer la config sauvegardée (reset)
reload                              ! Redémarrer l'équipement

! === COMMANDES SHOW ===
show running-config                 ! Config active en RAM
show startup-config                 ! Config au démarrage en Flash
show version                        ! Version IOS, uptime, RAM/Flash
show interfaces                     ! Détails de toutes les interfaces
show ip interface brief             ! Résumé IP + état des interfaces
show mac address-table              ! Table MAC apprise
show mac address-table aging-time   ! Durée de vie des entrées MAC
show flash                          ! Contenu de la mémoire Flash
show history                        ! Historique des commandes

! === UTILES ===
no ip domain-lookup                 ! Désactiver la résolution DNS (évite les pauses)
?                                   ! Aide contextuelle
Tab                                 ! Complétion automatique
Ctrl+C                              ! Interrompre une opération
```

**Commandes Linux essentielles (rappel + nouvelles S6) :**

```bash
# Navigation (S5 - rappel)
pwd              # Répertoire courant
ls -la           # Lister avec détails et fichiers cachés
cd /chemin       # Changer de répertoire
cd ..            # Remonter d'un niveau

# Gestion fichiers et dossiers (S5 + S6 approfondissement)
mkdir -p a/b/c   # Créer arborescence complète
touch fichier    # Créer fichier vide
cp -r src/ dest/ # Copier récursif
mv ancien nouveau # Déplacer/renommer
rm -i fichier    # Supprimer avec confirmation (-i = interactive)
rm -rf dossier/  # Supprimer dossier récursivement (prudence !)

# Lire/éditer des fichiers
cat fichier      # Afficher contenu complet
cat -n fichier   # Afficher avec numéros de lignes
less fichier     # Afficher page par page (q=quitter, /=rechercher)
head -10 fichier # 10 premières lignes
tail -5 fichier  # 5 dernières lignes
nano fichier     # Éditeur interactif

# Infos système
uname -a         # Info noyau
df -h            # Espace disque
free -h          # Mémoire utilisée
history          # Historique des commandes
clear            # Effacer l'écran (ou Ctrl+L)

# Astuces productivité
Tab              # Complétion automatique
Ctrl+C           # Interrompre la commande en cours
Ctrl+L           # Effacer l'écran
Flèche haut/bas  # Naviguer dans l'historique
!!               # Répéter la dernière commande
sudo !!          # Répéter la dernière commande avec sudo
```

---

## 🎯 ACTIVITÉ DE DÉCOUVERTE
### "Le Central Téléphonique" - Simulation de la Table MAC

### Objectif

Comprendre **concrètement** comment un switch apprend les adresses MAC et prend ses décisions de forwarding/flooding, par une simulation en groupe.

---

### Mise en Situation (5 min - Collectif)

> *"Imaginez un **standard téléphonique** d'entreprise des années 1990. Les employés ont des postes internes (numéro 101, 102, 103...) mais la standardiste ne connaît pas encore les noms. Quand quelqu'un appelle le 102 pour la première fois, elle doit chercher qui répond sur quelle ligne.*
>
> *Un **switch réseau**, c'est exactement pareil. Il gère des ports physiques (port 1, 2, 3...) et doit apprendre quelle **adresse MAC** (identifiant unique de carte réseau) se trouve sur quel port. Il ne le sait pas d'avance — il **apprend au fur et à mesure** des trames qui passent."*

---

### Déroulé (30 minutes)

#### **Phase 1 : Mise en Place (5 min)**

Former des **groupes de 5** (4 machines + 1 switch).

**Distribution des rôles + cartes :**

| **Joueur** | **Rôle** | **Adresse MAC** | **Port Switch** |
|------------|----------|-----------------|-----------------|
| Apprenant 1 | **PC-Alice** | `AA:AA:AA:00:01` | Port 1 |
| Apprenant 2 | **PC-Bob** | `BB:BB:BB:00:02` | Port 2 |
| Apprenant 3 | **PC-Clara** | `CC:CC:CC:00:03` | Port 3 |
| Apprenant 4 | **PC-David** | `DD:DD:DD:00:04` | Port 4 |
| Apprenant 5 | **LE SWITCH** | - | Gère les 4 ports |

**Matériel du Switch :**
- Une feuille vierge = **Table MAC** (vide au début)
- Un crayon

**Matériel des PC :**
- Leur carte d'identité (MAC + Port)
- Des billets (= trames) à remettre au Switch

---

#### **Phase 2 : Simulation (15 min)**

**Format d'un billet (trame) :**
```
┌─────────────────────────────────────┐
│ TRAME Ethernet                      │
│ MAC Source      : [SA MAC]          │
│ MAC Destination : [DA MAC]          │
│ Données         : "Bonjour Bob !"   │
└─────────────────────────────────────┘
```

---

**Tour 1 : PC-Alice envoie à PC-Bob (Table MAC vide)**

1. **PC-Alice** remplit un billet :
   - Source : `AA:AA:AA:00:01`
   - Destination : `BB:BB:BB:00:02`
   - Et le tend au **Switch** (via port 1)

2. **Le Switch** reçoit la trame sur le **Port 1** :
   - *"Je lis la MAC Source : `AA:AA:AA:00:01`"*
   - *"Je note dans ma Table MAC : `AA:AA:AA:00:01` → Port 1"* ✍️
   - *"Je cherche `BB:BB:BB:00:02` dans ma table... Inconnue !"*
   - **FLOODING** : Il donne des copies du billet à PC-Bob (port 2), PC-Clara (port 3) ET PC-David (port 4)

3. **PC-Bob** lit la destination : *"C'est pour moi !"* → Il répond.
   **PC-Clara** et **PC-David** lisent : *"Pas pour moi"* → Ils ignorent (jettent le billet).

---

**Tour 2 : PC-Bob répond à PC-Alice**

1. **PC-Bob** remplit un billet :
   - Source : `BB:BB:BB:00:02`
   - Destination : `AA:AA:AA:00:01`

2. **Le Switch** reçoit sur **Port 2** :
   - Note : `BB:BB:BB:00:02` → Port 2 ✍️
   - Cherche `AA:AA:AA:00:01`... **TROUVÉ ! Port 1**
   - **FORWARDING** : Donne le billet **uniquement** à PC-Alice (port 1)

3. PC-Clara et PC-David ne reçoivent **rien** cette fois ! 🎉

---

**Tour 3 : PC-Alice envoie de nouveau à PC-Bob**

- Le Switch connaît maintenant les deux MAC.
- **FORWARDING direct** : Port 1 → Port 2. Clara et David non sollicités.

---

**Tour 4 : PC-Clara envoie un Broadcast (`FF:FF:FF:FF:FF:FF`)**

1. PC-Clara remplit un billet :
   - Source : `CC:CC:CC:00:03`
   - Destination : `FF:FF:FF:FF:FF:FF`

2. Switch reçoit sur Port 3 :
   - Note : `CC:CC:CC:00:03` → Port 3 ✍️
   - Cherche `FF:FF:FF:FF:FF:FF`... *"C'est un broadcast !"*
   - **FLOODING OBLIGATOIRE** : Envoie à TOUS les ports (1, 2, 4) — même si les MAC sont connues !

3. **Tous les PC** reçoivent et lisent la trame.

---

**État final de la Table MAC :**

| **MAC Adresse** | **Port** | **Type** |
|-----------------|----------|----------|
| AA:AA:AA:00:01 | Port 1 | Dynamique |
| BB:BB:BB:00:02 | Port 2 | Dynamique |
| CC:CC:CC:00:03 | Port 3 | Dynamique |
| DD:DD:DD:00:04 | ? | Pas encore appris (David n'a rien envoyé) |

---

#### **Phase 3 : Débriefing (10 min)**

**Questions de l'enseignant :**

1. *"Qu'est-ce qui déclenche le flooding ? Et le forwarding ?"*
   - Flooding : destination inconnue dans la table, OU broadcast
   - Forwarding : destination connue dans la table

2. *"Quelle est la différence entre un switch et un hub ?"*
   - Hub : **toujours** flooding (répète tout sur tous les ports, comme une loudspeaker)
   - Switch : **forwarding** quand la MAC est connue (économise bande passante, sécurité)

3. *"PC-David n'a rien envoyé. Est-il coupé du réseau ?"*
   - Non, il peut recevoir des trames. Mais le switch ne connaît pas encore son port. Si quelqu'un lui envoie quelque chose, il y aura flooding (jusqu'à ce que David réponde et apprenne sa MAC au switch).

4. *"Que se passe-t-il si on branche 2 switches entre eux sans précaution ?"*
   - Risque de **boucle** : un broadcast tourne en rond indéfiniment → saturation → réseau mort.
   - Solution : **Spanning Tree Protocol (STP)** — à voir en S9 !

---

**Transition vers l'apport théorique :**

> *"Vous venez de simuler le cerveau d'un switch ! Maintenant on va voir comment lire cette table MAC sur un VRAI switch Cisco, et comment configurer un switch pour qu'il soit prêt à l'emploi dans une entreprise."*

---

## 📚 FICHE DE COURS ÉLÈVE
### "Commutation, Cisco CLI et Linux : Commandes de Base"

*Version 1.0 - BTS SIO SISR - Semestre 1 - Semaine 6*

---

### 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|----------------|
| **B2.2** | Installer, tester et déployer une solution d'infrastructure réseau - Configurer un switch Cisco |
| **B2.3** | Exploiter, dépanner et superviser - Commandes show, diagnostic commutation |
| **B2.1** | Administrer un système d'exploitation - Commandes Linux fondamentales |

---

### I. La Commutation : Fonctionnement d'un Switch

#### A. Rôle du Switch (Rappel S4)

**Switch (Commutateur)** = Équipement de couche **2** (Liaison de données) du modèle OSI.

**Rôle :** Interconnecter des machines dans un **même réseau local (LAN)** en utilisant les **adresses MAC**.

**Analogie :** Un switch est comme un **central téléphonique intelligent** d'entreprise. Il sait sur quelle ligne se trouve chaque poste (MAC → Port) et établit des connexions directes, sans déranger les autres.

---

#### B. La Table MAC (CAM Table)

**Définition :** Table interne du switch qui **associe chaque adresse MAC au port physique** sur lequel elle a été détectée.

**Caractéristiques :**
- Construite **automatiquement** (self-learning = apprentissage automatique)
- Stockée en mémoire RAM (volatile)
- Chaque entrée a une **durée de vie** (aging time, défaut Cisco = 300 secondes)

**Commande Cisco pour l'afficher :**
```
Switch# show mac address-table
```

**Exemple de résultat :**
```
          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    aaaa.aa00.0001    DYNAMIC     Fa0/1
   1    bbbb.bb00.0002    DYNAMIC     Fa0/2
   1    cccc.cc00.0003    DYNAMIC     Fa0/3
Total Mac Addresses for this criterion: 3
```

**Colonnes :**
- **Vlan** : VLAN auquel appartient l'entrée (VLAN 1 = défaut)
- **Mac Address** : Adresse MAC de la machine
- **Type** : DYNAMIC (apprise automatiquement) ou STATIC (configurée manuellement)
- **Ports** : Port physique du switch (Fa0/1 = FastEthernet port 1)

---

#### C. Processus d'Apprentissage et de Décision

Le switch traite chaque trame en **2 étapes systématiques** :

##### **Étape 1 : Apprentissage (Source MAC)**

1. Le switch reçoit une trame sur le **Port X**
2. Il lit l'**adresse MAC Source** de la trame
3. Il enregistre (ou met à jour) dans sa Table MAC :
   → *"MAC Source est joignable via Port X"*

##### **Étape 2 : Décision (Destination MAC)**

Le switch lit l'**adresse MAC Destination** et prend l'une de 3 décisions :

| **Situation** | **Décision** | **Description** |
|---------------|--------------|-----------------|
| MAC Destination **connue** dans la table | **FORWARDING** | Envoie la trame **uniquement** sur le port correspondant |
| MAC Destination **inconnue** dans la table | **FLOODING** | Envoie la trame sur **tous les ports** sauf celui de réception |
| MAC Destination = `FF:FF:FF:FF:FF:FF` (broadcast) | **FLOODING** | Envoie sur **tous les ports** sans exception (toujours) |

---

**Schéma du processus complet :**

```
Trame reçue sur Port 3
        │
        ▼
┌───────────────────────────────────────────────┐
│  APPRENTISSAGE                                │
│  Note MAC Source → Port 3 dans la table       │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
              MAC Destination =
              FF:FF:FF:FF:FF:FF ?
                /         \
              OUI          NON
               │             │
               │      MAC Destination
               │       connue dans table ?
               │          /      \
               │        OUI      NON
               │         │        │
               ▼         ▼        ▼
            FLOOD     FORWARD   FLOOD
          (tous ports)(1 port) (tous ports)
```

---

#### D. Évolution : Hub → Switch

**Hub (Concentrateur) - Obsolète :**

Le hub est un équipement de **couche 1** (physique). Il n'a aucune intelligence : il **répète le signal électrique sur tous les ports** sans exception, quelles que soient les adresses.

```
Hub - PC1 envoie à PC3 :
Port 1 [PC1] → Signal répété → Port 2 [PC2] ⚠️ (reçoit inutilement)
                             → Port 3 [PC3] ✅
                             → Port 4 [PC4] ⚠️ (reçoit inutilement)
```

**Switch - Moderne :**

```
Switch - PC1 envoie à PC3 (MAC connue) :
Port 1 [PC1] → FORWARDING → Port 3 [PC3] ✅
               (Port 2 et 4 ne reçoivent rien)
```

| **Critère** | **HUB** | **SWITCH** |
|-------------|---------|------------|
| Couche OSI | 1 (Physique) | 2 (Liaison) |
| Intelligence | ❌ Aucune | ✅ Table MAC |
| Sécurité | ❌ Toutes les trames visibles par tous | ✅ Forwarding ciblé |
| Performances | ❌ Dégradées avec le trafic | ✅ Débit dédié par port |
| Usage actuel | ❌ **Obsolète** | ✅ **Standard** |

---

#### E. Domaines de Collision et de Diffusion

##### 🔹 **Domaine de Collision (Collision Domain)**

**Définition :** Zone où deux transmissions simultanées provoquent une **collision** (corruption des signaux).

**Avec un Hub :**
```
[PC1]─┬─[PC2]─┬─[PC3]─┬─[PC4]
      └───── HUB ───────┘
→ 1 seul domaine de collision (tous les PC)
→ Si PC1 et PC2 émettent en même temps : COLLISION
→ Les deux doivent attendre un délai aléatoire et réémettre (CSMA/CD)
```

**Avec un Switch :**
```
[PC1]─Fa0/1─┐
[PC2]─Fa0/2─┤
[PC3]─Fa0/3─┤  [SWITCH]
[PC4]─Fa0/4─┘
→ 1 domaine de collision PAR PORT (full-duplex)
→ PC1 et PC2 peuvent émettre simultanément sans collision
```

💡 **Résumé :** Un switch avec **N ports** = **N domaines de collision** (1 par port).

---

##### 🔹 **Domaine de Diffusion (Broadcast Domain)**

**Définition :** Zone où une trame de diffusion (`FF:FF:FF:FF:FF:FF`) est **propagée et reçue par tous**.

**Avec un Switch seul :**
```
[PC1]─[PC2]─[SWITCH]─[PC3]─[PC4]
→ 1 seul domaine de diffusion
→ Un broadcast de PC1 est reçu par PC2, PC3, PC4
```

**Avec un Routeur :**
```
Réseau A: [PC1]─[PC2]─[SW1]─[ROUTEUR]─[SW2]─[PC3]─[PC4]
→ 2 domaines de diffusion séparés par le routeur
→ Broadcast de PC1 reste dans Réseau A (PC2 uniquement)
→ PC3 et PC4 ne reçoivent pas le broadcast
```

💡 **Règle à retenir :**
- **Switch** : Sépare les domaines de **collision** mais **PAS** les domaines de diffusion
- **Routeur** : Sépare les domaines de **diffusion** (et de collision)

| **Équipement** | **Sépare collisions ?** | **Sépare broadcasts ?** |
|----------------|-------------------------|-------------------------|
| Hub | ❌ Non | ❌ Non |
| Switch | ✅ Oui (1 par port) | ❌ Non |
| Routeur | ✅ Oui | ✅ Oui |

---

### II. La CLI Cisco IOS : Prise en Main

#### A. Accéder à un Équipement Cisco

##### 🔹 **Méthode 1 : Câble Console (accès physique - premier accès)**

**Matériel :**
- **Câble console** : RJ45 → USB (ou ancien DB9/RS-232)
- Logiciel terminal : **PuTTY**, Tera Term, SecureCRT

**Paramètres de connexion PuTTY :**

| **Paramètre** | **Valeur** |
|---------------|------------|
| Type de connexion | **Serial** |
| Port COM | COM3, COM4... (Gestionnaire de périphériques Windows) |
| Vitesse (baud rate) | **9600** |
| Bits de données | 8 |
| Parité | Aucune |
| Bits d'arrêt | 1 |
| Contrôle de flux | Aucun |

**Procédure :**
1. Brancher câble console PC ↔ Switch
2. Ouvrir PuTTY → Serial → COM3 → 9600
3. Appuyer sur **Entrée** → Prompt du switch apparaît

##### 🔹 **Méthode 2 : Packet Tracer (simulation)**

1. Clic sur le switch dans la topologie
2. Onglet **CLI**
3. Appuyer sur **Entrée**
4. Répondre **No** à "Initial configuration dialog?"

---

#### B. Les Modes de la CLI Cisco IOS

La CLI Cisco est organisée en **hiérarchie de modes**. Chaque mode a un **prompt** (invite) distinctif et permet des commandes spécifiques.

```
Switch>                     ← Mode User EXEC
    │  enable
    ▼
Switch#                     ← Mode Privileged EXEC (Enable Mode)
    │  configure terminal (ou conf t)
    ▼
Switch(config)#             ← Mode Global Configuration
    │  interface FastEthernet0/1
    ▼
Switch(config-if)#          ← Mode Interface Configuration
    │  exit (revenir d'un niveau)
    │  end (revenir directement en Privileged)
```

---

| **Mode** | **Prompt** | **Accès** | **Ce qu'on peut faire** |
|----------|------------|-----------|-------------------------|
| **User EXEC** | `Switch>` | Automatique à la connexion | `ping`, `show` limités, `enable` |
| **Privileged EXEC** | `Switch#` | `enable` (+ mot de passe si configuré) | Tous les `show`, `debug`, `copy`, `reload` |
| **Global Config** | `Switch(config)#` | `configure terminal` depuis Privileged | Modifier la config globale (hostname, passwords, banner...) |
| **Interface Config** | `Switch(config-if)#` | `interface <nom>` depuis Global Config | Configurer une interface spécifique |
| **Line Config** | `Switch(config-line)#` | `line console 0` ou `line vty 0 4` | Configurer les accès console et réseau |

---

**Commandes de navigation entre modes :**

```cisco
Switch> enable                ! User → Privileged
Switch# disable               ! Revenir en User EXEC
Switch# configure terminal    ! Privileged → Global Config
Switch(config)# exit          ! Remonter d'UN niveau
Switch(config)# end           ! Retour direct en Privileged (ou Ctrl+Z)
Switch(config-if)# exit       ! Interface Config → Global Config
Switch(config-if)# end        ! Interface Config → Privileged (sauter tous niveaux)
```

---

#### C. Astuces de Productivité CLI

| **Astuce** | **Usage** |
|------------|-----------|
| **`?`** | Aide contextuelle (affiche les commandes disponibles dans ce mode) |
| **`Tab`** | Complétion automatique de la commande |
| **`sh run`** au lieu de `show running-config` | Abréviation (fonctionne tant qu'unique) |
| **`conf t`** au lieu de `configure terminal` | Abréviation |
| **Flèche Haut** | Rappeler la commande précédente |
| **Ctrl+C** | Interrompre une opération |
| **Ctrl+Z** | Équivalent de `end` (retour Privileged) |
| **`no <commande>`** | Annuler/supprimer une configuration |
| **`show history`** | Afficher les dernières commandes tapées |

---

#### D. Les Commandes `show` Essentielles

Les commandes `show` s'utilisent en **mode Privileged EXEC** (ou User EXEC pour certaines).

```cisco
Switch# show running-config       ! Config active en RAM (tout ce qui est configuré)
Switch# show startup-config       ! Config sauvegardée en Flash (au démarrage)
Switch# show version              ! Version IOS, temps de fonctionnement, RAM, Flash
Switch# show interfaces           ! Détails de toutes les interfaces (compteurs d'erreurs...)
Switch# show ip interface brief   ! Résumé rapide : interface, IP, état (up/down)
Switch# show mac address-table    ! Table MAC apprise
Switch# show flash                ! Fichiers stockés en mémoire Flash
Switch# show history              ! 10 dernières commandes tapées
```

**Exemple de `show ip interface brief` :**
```
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/1        unassigned      YES unset  up                    up
FastEthernet0/2        unassigned      YES unset  down                  down
...
Vlan1                  unassigned      YES unset  administratively down down
```

**Lecture :**
- **up/up** : Interface active (câble connecté + activée)
- **down/down** : Pas de câble ou problème physique
- **administratively down** : Désactivée volontairement (`shutdown`)

---

### III. Configurer un Switch Cisco : Séquence Complète

#### A. Logique de la Configuration Initiale

Quand on reçoit un switch neuf ou réinitialisé, il faut :

1. **Nommer** l'équipement (`hostname`)
2. **Afficher un message d'avertissement** (`banner motd`)
3. **Sécuriser** l'accès mode privilégié (`enable secret`)
4. **Sécuriser** l'accès console (`line console 0`)
5. **Sécuriser** l'accès réseau / Telnet (`line vty 0 15`)
6. **Chiffrer** tous les mots de passe (`service password-encryption`)
7. **Sauvegarder** la configuration (`copy run start`)

---

#### B. Séquence de Configuration Complète (Avec Explications)

```cisco
! ============================================================
! ÉTAPE 0 : Accès en mode privilégié
! ============================================================
Switch> enable                   ! Pas de mot de passe au 1er accès
Switch#

! ============================================================
! ÉTAPE 1 : Entrer en mode configuration globale
! ============================================================
Switch# configure terminal
Switch(config)#

! ============================================================
! ÉTAPE 2 : Nommer le switch
! ============================================================
Switch(config)# hostname SW_BUREAU_01
SW_BUREAU_01(config)#            ! Le prompt change immédiatement !

! ============================================================
! ÉTAPE 3 : Désactiver la résolution DNS (astuce de confort)
! Évite que les fautes de frappe soient interprétées comme
! des noms d'hôtes à résoudre (pauses de 30 secondes !)
! ============================================================
SW_BUREAU_01(config)# no ip domain-lookup

! ============================================================
! ÉTAPE 4 : Configurer le message du jour (Banner MOTD)
! Le '#' est le délimiteur (doit être absent du message)
! ============================================================
SW_BUREAU_01(config)# banner motd #
Entrer le message du jour :
*****************************************************
* Acces INTERDIT aux personnes non autorisees.      *
* Toute connexion est enregistree et tracee.        *
* Contacter le DSI : dsi@entreprise.fr              *
*****************************************************
#

! ============================================================
! ÉTAPE 5 : Sécuriser le mode privilégié
! "enable secret" = chiffrement MD5 (toujours préférer à
! "enable password" qui stocke en clair)
! ============================================================
SW_BUREAU_01(config)# enable secret Cisco@2024

! ============================================================
! ÉTAPE 6 : Sécuriser la ligne console (accès physique)
! ============================================================
SW_BUREAU_01(config)# line console 0
SW_BUREAU_01(config-line)# password Console@2024
SW_BUREAU_01(config-line)# login
SW_BUREAU_01(config-line)# exec-timeout 5 0    ! Déconnexion après 5min inactivité
SW_BUREAU_01(config-line)# exit

! ============================================================
! ÉTAPE 7 : Sécuriser les lignes VTY (accès Telnet/SSH)
! vty 0 15 = 16 sessions simultanées possibles
! ============================================================
SW_BUREAU_01(config)# line vty 0 15
SW_BUREAU_01(config-line)# password Vty@2024
SW_BUREAU_01(config-line)# login
SW_BUREAU_01(config-line)# exec-timeout 5 0
SW_BUREAU_01(config-line)# exit

! ============================================================
! ÉTAPE 8 : Chiffrer TOUS les mots de passe en clair
! (line console, line vty sont en clair sans ça !)
! ============================================================
SW_BUREAU_01(config)# service password-encryption

! ============================================================
! ÉTAPE 9 : Revenir en mode privilégié
! ============================================================
SW_BUREAU_01(config)# end
SW_BUREAU_01#

! ============================================================
! ÉTAPE 10 : Vérifier la configuration
! ============================================================
SW_BUREAU_01# show running-config

! ============================================================
! ÉTAPE 11 : SAUVEGARDER ! (CRITIQUE - sinon perdu au reboot)
! ============================================================
SW_BUREAU_01# copy running-config startup-config
Destination filename [startup-config]?     ! Appuyer sur Entrée
Building configuration...
[OK]
```

---

#### C. Vérifier la Configuration : `show running-config`

Après configuration, taper `show running-config` permet de **vérifier** tout ce qui a été fait.

**Extrait typique :**
```
SW_BUREAU_01# show running-config
Building configuration...

Current configuration : 1024 bytes
!
version 15.0
...
!
hostname SW_BUREAU_01
!
no ip domain-lookup
!
enable secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0   ← Mot de passe chiffré MD5
!
banner motd ^C
*****************************************************
* Acces INTERDIT aux personnes non autorisees.      *
*****************************************************
^C
!
...
line con 0
 password 7 0822455D0A16                            ← Chiffré par service pwd-enc
 login
 exec-timeout 5 0
!
line vty 0 4
 password 7 0822455D0A16
 login
 exec-timeout 5 0
!
end
```

💡 **`enable secret 5 $1$...`** : Le `5` indique chiffrement MD5. Impossible de retrouver le mot de passe à partir de ce hash.

💡 **`password 7 ...`** : Service password-encryption → chiffrement faible (type 7), déchiffrable en ligne, mais dissuasif.

---

#### D. Différence Running-Config vs Startup-Config

```
Mémoire RAM                      Mémoire Flash (NVRAM)
┌─────────────────────┐           ┌─────────────────────┐
│   running-config    │           │   startup-config    │
│   (config active)   │  copy     │   (config sauvegardée)│
│   Modifiée en temps │──run───→  │   Chargée au         │
│   réel              │  start    │   démarrage          │
│   PERDUE au reboot  │           │   Persistante        │
└─────────────────────┘           └─────────────────────┘
```

⚠️ **Règle d'or :** Toujours `copy run start` après modification !

**Autres commandes de sauvegarde :**
```cisco
Switch# write memory             ! Équivalent de "copy run start" (ancienne syntaxe)
Switch# write                    ! Version abrégée (valide sur certains IOS)
Switch# erase startup-config     ! Effacer la config sauvegardée (reset usine)
Switch# reload                   ! Redémarrer (attention : sans save = config perdue !)
```

---

### IV. Linux : Commandes de Base (Suite S5)

**Rappel S5 :** Navigation (pwd, ls, cd), création (mkdir, touch), lecture (cat, less), édition (nano), suppression (rm), copie (cp), déplacement (mv).

Cette séance approfondit et consolide ces commandes avec plus d'options et de cas pratiques.

---

#### A. Navigation et Exploration

```bash
# Connaître son emplacement
pwd                         # /home/etudiant

# Lister le contenu
ls                          # Liste simple
ls -l                       # Liste longue (permissions, taille, date)
ls -a                       # Inclut les fichiers cachés (commençant par .)
ls -la                      # Longue + cachés (le plus utilisé)
ls -lh                      # Tailles lisibles (Ko, Mo, Go)
ls -lt                      # Triés par date (plus récent en premier)
ls /etc                     # Lister un répertoire sans s'y déplacer

# Se déplacer
cd /home/etudiant            # Chemin absolu (depuis la racine /)
cd BTS_SIO                   # Chemin relatif (depuis le répertoire courant)
cd ..                        # Remonter d'un niveau
cd ../..                     # Remonter de 2 niveaux
cd ~                         # Aller dans son répertoire home
cd -                         # Revenir au répertoire précédent
```

**Comprendre la sortie de `ls -l` :**
```
-rw-r--r--  1  etudiant  etudiant  1024  nov  15 10:30  fichier.txt
│           │  │          │         │     │              │
│           │  │          │         │     │              └─ Nom du fichier
│           │  │          │         │     └─ Date dernière modification
│           │  │          │         └─ Taille en octets
│           │  │          └─ Groupe propriétaire
│           │  └─ Utilisateur propriétaire
│           └─ Nombre de liens physiques
└─ Permissions (type + rwx propriétaire + rwx groupe + rwx autres)
```

---

#### B. Gestion des Répertoires et Fichiers

```bash
# Créer des répertoires
mkdir MonDossier                    # Créer un dossier
mkdir -p Projet/Reseau/Config       # Créer toute l'arborescence d'un coup
                                    # (-p = parents, crée chaque niveau manquant)

# Créer des fichiers
touch fichier.txt                   # Créer un fichier vide
touch a.txt b.txt c.txt             # Créer plusieurs fichiers d'un coup

# Copier
cp source.txt destination.txt       # Copier un fichier (renomme à la destination)
cp source.txt /tmp/                  # Copier dans un répertoire (garde le nom)
cp -r DossierSource/ DossierDest/   # Copier un dossier entier (-r = récursif)
cp -p source.txt dest.txt           # Copier en préservant les métadonnées (date, permissions)

# Déplacer / Renommer
mv ancien.txt nouveau.txt           # Renommer un fichier
mv fichier.txt /tmp/                # Déplacer dans /tmp
mv DossierA/ /home/etudiant/        # Déplacer un dossier

# Supprimer
rm fichier.txt                      # Supprimer un fichier
rm -i fichier.txt                   # Supprimer avec confirmation (-i = interactif)
rm -f fichier.txt                   # Forcer la suppression sans confirmation
rm -r MonDossier/                   # Supprimer un dossier et son contenu
rm -rf MonDossier/                  # Forcer la suppression récursive (DANGEREUX)
```

⚠️ **AVERTISSEMENT `rm -rf` :**
- Il n'y a **pas de corbeille** dans un terminal Linux : la suppression est **définitive**
- TOUJOURS vérifier le chemin avant `rm -rf`
- En TP : préférer `rm -ri` (confirmation pour chaque fichier) pour s'entraîner

---

#### C. Lecture et Affichage du Contenu

```bash
# Afficher le contenu d'un fichier
cat fichier.txt                     # Afficher tout le fichier d'un coup
cat -n fichier.txt                  # Avec numéros de lignes
cat fichier1.txt fichier2.txt       # Afficher plusieurs fichiers à la suite

# Navigation dans les fichiers longs
less fichier.txt                    # Affichage page par page
                                    # (Espace = page suivante, q = quitter,
                                    # / = rechercher, n = occurrence suivante)
more fichier.txt                    # Similaire à less (moins de fonctions)

# Extraits
head fichier.txt                    # 10 premières lignes (défaut)
head -20 fichier.txt                # 20 premières lignes
tail fichier.txt                    # 10 dernières lignes (défaut)
tail -5 fichier.txt                 # 5 dernières lignes
tail -f /var/log/syslog             # Suivi en temps réel (pratique pour logs)
```

---

#### D. Édition avec Nano

**Nano** est l'éditeur de texte en ligne de commande le plus accessible pour les débutants.

**Ouvrir/créer un fichier :**
```bash
nano monFichier.txt         # Ouvrir ou créer
nano /etc/hosts             # Ouvrir un fichier système (ajouter sudo si besoin)
sudo nano /etc/hosts        # Avec droits admin
```

**Interface Nano :**
```
  GNU nano 5.4                 monFichier.txt

Voici le contenu du fichier.
On peut taper ici librement.
_

^G Aide    ^O Enreg.  ^W Chercher ^K Couper  ^T Vérif.
^X Quitter ^R Insérer ^\ Remplacer ^U Coller  ^J Justifier
```

**Raccourcis clavier essentiels (`^` = touche Ctrl) :**

| **Raccourci** | **Action** |
|---------------|------------|
| `Ctrl+O` puis `Entrée` | **Enregistrer** le fichier (O comme ecrirO) |
| `Ctrl+X` | **Quitter** (demande de sauvegarder si modifications) |
| `Ctrl+K` | **Couper** la ligne courante (dans un presse-papiers) |
| `Ctrl+U` | **Coller** la ligne coupée |
| `Ctrl+W` | **Chercher** un texte dans le fichier |
| `Ctrl+G` | **Aide** complète |
| `Ctrl+\` | **Remplacer** texte |
| `Ctrl+C` | Afficher le **numéro de ligne** actuel |
| `Flèches` | Déplacer le curseur |

**Procédure typique :**
1. `nano monfichier.txt` → Le fichier s'ouvre
2. Taper le contenu souhaité
3. `Ctrl+O` → Appuyer sur `Entrée` pour confirmer le nom
4. `Ctrl+X` pour quitter

---

#### E. Exercices Pratiques Linux

##### **Exercice 1 : Créer une Arborescence de Projet**

Créer **entièrement depuis le terminal** la structure suivante :

```
/home/etudiant/
└── BTS_SIO_SISR/
    ├── Bloc2_Reseau/
    │   ├── Semaine5/
    │   │   └── config_ip.txt     → contenu : "IP: 192.168.5.20 - Masque: 255.255.255.0"
    │   └── Semaine6/
    │       └── commutation.txt   → contenu : "Switch = couche 2 - Table MAC"
    ├── Bloc2_Linux/
    │   ├── commandes.txt         → contenu : "ls, cd, cp, mv, rm, mkdir, cat, nano"
    │   └── notes.txt             → contenu vide (juste créer le fichier)
    └── README.txt                → contenu : "Portfolio BTS SIO SISR - Année 1"
```

**Commandes à utiliser :** `mkdir -p`, `nano`, `touch`, `cat`

---

##### **Exercice 2 : Manipulation de Fichiers**

À partir de l'arborescence créée :

1. **Copier** `commandes.txt` dans `/tmp/sauvegarde_commandes.txt`
2. **Déplacer** `notes.txt` dans `Semaine6/` (et le renommer `notes_s6.txt`)
3. **Afficher** le contenu de `config_ip.txt` avec numéros de lignes
4. **Ouvrir** `README.txt` avec nano et ajouter la ligne : "Semaine 6 - Commutation et CLI Cisco"
5. **Lister** le contenu de `BTS_SIO_SISR/` avec les tailles lisibles (`-lh`)

---

##### **Exercice 3 : Comprendre `ls -l`**

Taper `ls -la /home/etudiant/` et répondre :
1. Quels fichiers commencent par un `.` ? À quoi servent-ils ?
2. Quel est le propriétaire du répertoire `BTS_SIO_SISR` ?
3. Quelle est la taille du fichier `commandes.txt` ?
4. Quelle est la date de dernière modification de `README.txt` ?

---

### V. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|----------------|
| **Commutation** | Processus de transfert de trames entre ports d'un switch selon la table MAC |
| **Table MAC (CAM)** | Table d'un switch associant adresses MAC aux ports physiques |
| **Forwarding** | Switch envoie la trame uniquement sur le port du destinataire connu |
| **Flooding** | Switch envoie la trame sur tous les ports (MAC inconnue ou broadcast) |
| **Self-Learning** | Apprentissage automatique des MAC par le switch à partir des trames |
| **Aging Time** | Durée de vie d'une entrée dans la table MAC (défaut 300s sur Cisco) |
| **Domaine de collision** | Zone où deux émissions simultanées causent une collision |
| **Domaine de diffusion** | Zone où un broadcast est propagé |
| **Hub** | Équipement couche 1, répète le signal sur tous les ports (obsolète) |
| **IOS** | Internetwork Operating System - Système d'exploitation des équipements Cisco |
| **CLI** | Command Line Interface - Interface en ligne de commande Cisco |
| **User EXEC** | Mode CLI initial (prompt `>`) - accès limité |
| **Privileged EXEC** | Mode CLI administrateur (prompt `#`) - accès complet |
| **Global Config** | Mode configuration globale (prompt `(config)#`) |
| **hostname** | Commande Cisco changeant le nom de l'équipement |
| **banner motd** | Message affiché à chaque connexion à l'équipement |
| **enable secret** | Mot de passe chiffré MD5 pour le mode privilégié |
| **service password-encryption** | Chiffre tous les mots de passe en clair dans la config |
| **running-config** | Configuration active en RAM (perdue au redémarrage) |
| **startup-config** | Configuration sauvegardée en Flash (chargée au démarrage) |
| **copy run start** | Commande Cisco sauvegardant la config RAM → Flash |
| **exec-timeout** | Délai d'inactivité avant déconnexion automatique |
| **Chemin absolu** | Chemin depuis la racine `/` (ex: `/home/etudiant/fichier.txt`) |
| **Chemin relatif** | Chemin depuis le répertoire courant (ex: `../fichier.txt`) |
| **`cat`** | Afficher le contenu d'un fichier dans le terminal |
| **`nano`** | Éditeur de texte interactif dans le terminal |
| **`less`** | Afficher un fichier long page par page |

---

### VI. Exercices d'Entraînement

#### Exercice 1 : Simulation Table MAC

Un switch démarre à vide (table MAC vide). Il possède 4 ports avec :
- Port 1 : PC-A (MAC : `AAAA.0001`)
- Port 2 : PC-B (MAC : `BBBB.0002`)
- Port 3 : PC-C (MAC : `CCCC.0003`)
- Port 4 : PC-D (MAC : `DDDD.0004`)

Voici les trames reçues dans l'ordre :
1. PC-A envoie à PC-C
2. PC-C répond à PC-A
3. PC-B envoie à PC-D
4. PC-D répond à PC-B
5. PC-A envoie un broadcast

Pour chaque trame, indiquer :
- L'action du switch (FLOODING ou FORWARDING)
- Le contenu de la table MAC après chaque trame
- Sur quels ports la trame est envoyée

---

#### Exercice 2 : Navigation CLI

Répondre sans Packet Tracer (à partir du cours) :

1. On est en `Switch>`. On tape `show running-config`. Que se passe-t-il ?
2. On est en `Switch(config-if)#`. On veut aller directement en Privileged EXEC. Quelle commande ?
3. On tape `hostname MonSwitch` en mode User EXEC. Que se passe-t-il ?
4. Quelle est la différence entre `enable password` et `enable secret` ?
5. On a configuré le switch mais pas tapé `copy run start`. On redémarre. Qu'arrive-t-il ?

---

#### Exercice 3 : Domaines

Pour le réseau suivant :
```
[PC1]─[PC2]─[HUB_A]─[SWITCH]─[HUB_B]─[PC3]─[PC4]
```

1. Combien de domaines de collision ?
2. Combien de domaines de diffusion ?
3. Si PC1 envoie un ping à PC3, qui reçoit la trame au niveau du HUB_A ?
4. Si on remplace HUB_A par un switch, que change-t-il ?

---

#### Exercice 4 : Commandes Linux

Écrire la commande Linux pour :

1. Créer l'arborescence `/opt/apache/config/sites/` en une seule commande
2. Copier tous les fichiers `.txt` du répertoire courant dans `/tmp/sauvegarde/`
3. Afficher les 20 dernières lignes du fichier `/var/log/syslog`
4. Renommer le fichier `config_old.conf` en `config.conf`
5. Supprimer le dossier `/tmp/test/` et tout son contenu sans confirmation

---

### VII. Auto-évaluation : Suis-je Prêt ?

- [ ] Expliquer le processus d'apprentissage d'un switch (self-learning, table MAC)
- [ ] Distinguer forwarding et flooding (quand et pourquoi chaque cas)
- [ ] Définir domaine de collision et domaine de diffusion
- [ ] Indiquer quel équipement sépare les domaines de diffusion (routeur !)
- [ ] Naviguer entre les 3 modes CLI Cisco (User, Privileged, Global Config)
- [ ] Configurer le hostname, banner, enable secret d'un switch
- [ ] Configurer les mots de passe console et vty
- [ ] Utiliser `show running-config` pour vérifier la config
- [ ] Sauvegarder une config avec `copy run start`
- [ ] Expliquer la différence running-config / startup-config
- [ ] Naviguer dans l'arborescence Linux (pwd, ls -la, cd)
- [ ] Créer une arborescence de dossiers avec `mkdir -p`
- [ ] Copier, déplacer, renommer des fichiers (cp, mv)
- [ ] Afficher le contenu d'un fichier (cat, less, head, tail)
- [ ] Créer et éditer un fichier avec nano (Ctrl+O, Ctrl+X)

---

*Fin de la Fiche de Cours Élève - S6 Bloc 2*

---

## 🖥️ TP GUIDÉ CISCO PACKET TRACER
### "Configuration de Base d'un Switch SW_BUREAU_01"

---

### Objectif

Créer une topologie simple, accéder à la CLI d'un switch, le configurer entièrement (hostname, banner, passwords, save) et vérifier la configuration.

---

### Topologie à Réaliser

```
PC-Alice (192.168.10.10/24)─Fa0/1─┐
                                  │
PC-Bob   (192.168.10.20/24)─Fa0/2─┤  [SW_BUREAU_01]
                                  │
PC-Clara (192.168.10.30/24)─Fa0/3─┘
```

---

### Étape 1 : Créer la Topologie (5 min)

1. Ouvrir **Packet Tracer** → Nouveau fichier
2. Ajouter :
   - 1 **Switch Cisco 2960** (dans Network Devices → Switches)
   - 3 **PC** (dans End Devices)
3. Câbler : PC-Alice → Fa0/1, PC-Bob → Fa0/2, PC-Clara → Fa0/3 (câbles droits)
4. Configurer les IP des PC (onglet Desktop → IP Configuration) :
   - PC-Alice : `192.168.10.10` / `255.255.255.0`
   - PC-Bob : `192.168.10.20` / `255.255.255.0`
   - PC-Clara : `192.168.10.30` / `255.255.255.0`

✅ **Validation :** Les voyants des ports passent au vert (après quelques secondes).

---

### Étape 2 : Accéder à la CLI du Switch (2 min)

1. **Clic sur SW_BUREAU_01**
2. Onglet **CLI**
3. Appuyer sur **Entrée**
4. Si demande "Initial configuration dialog?" → taper **`no`** puis Entrée

```
Would you like to enter the initial configuration dialog? [yes/no]: no
Press RETURN to get started!
Switch>
```

✅ **Vous êtes en mode User EXEC (prompt `Switch>`)**

---

### Étape 3 : Explorer les Modes (5 min)

```cisco
Switch> ?                        ! Afficher les commandes disponibles en User EXEC

Switch> show version             ! Afficher les informations système

Switch> enable                   ! Passer en mode Privileged EXEC
Switch# ?                        ! Plus de commandes disponibles

Switch# show running-config      ! Afficher la config actuelle (vide pour l'instant)

Switch# configure terminal       ! Passer en mode Global Config
Switch(config)# ?                ! Commandes de configuration

Switch(config)# exit             ! Revenir en Privileged EXEC
Switch#
```

📝 **À noter :** Quelles nouvelles commandes apparaissent en mode Privileged par rapport à User ?

---

### Étape 4 : Configurer le Hostname (3 min)

```cisco
Switch# configure terminal
Switch(config)# hostname SW_BUREAU_01
SW_BUREAU_01(config)#            ! Le prompt a changé !
```

✅ **Validation :** Le prompt affiche maintenant `SW_BUREAU_01`.

---

### Étape 5 : Désactiver la Résolution DNS (1 min)

```cisco
SW_BUREAU_01(config)# no ip domain-lookup
```

💡 **Pourquoi ?** Sans cette commande, si vous faites une faute de frappe, Cisco essaie de résoudre le mot comme un nom DNS → attente de 30 secondes à chaque erreur !

---

### Étape 6 : Configurer le Banner MOTD (5 min)

```cisco
SW_BUREAU_01(config)# banner motd #
Entrez votre message. Terminez avec le caractère '#'.

=========================================
 ACCÈS RÉSERVÉ AU PERSONNEL AUTORISÉ
 Cabinet TechPro SARL - Service Informatique
 Toute connexion non autorisée est illégale.
 Contact DSI : +33 01 23 45 67 89
=========================================
#
SW_BUREAU_01(config)#
```

✅ **Validation :** Taper `end` puis `exit` pour se déconnecter, puis reconnecter → Le banner apparaît.

---

### Étape 7 : Sécuriser le Mode Privilégié (2 min)

```cisco
SW_BUREAU_01(config)# enable secret Cisco@2024
```

✅ **Validation :**
- Taper `end` pour revenir en Privileged
- Taper `disable` pour revenir en User EXEC
- Taper `enable` → le mot de passe est maintenant demandé !

```
SW_BUREAU_01> enable
Password: [taper Cisco@2024 - ne s'affiche pas]
SW_BUREAU_01#
```

---

### Étape 8 : Sécuriser la Ligne Console (5 min)

```cisco
SW_BUREAU_01# configure terminal
SW_BUREAU_01(config)# line console 0
SW_BUREAU_01(config-line)# password Console@2024
SW_BUREAU_01(config-line)# login
SW_BUREAU_01(config-line)# exec-timeout 5 0
SW_BUREAU_01(config-line)# exit
```

---

### Étape 9 : Sécuriser les Lignes VTY (5 min)

```cisco
SW_BUREAU_01(config)# line vty 0 15
SW_BUREAU_01(config-line)# password Vty@2024
SW_BUREAU_01(config-line)# login
SW_BUREAU_01(config-line)# exec-timeout 5 0
SW_BUREAU_01(config-line)# exit
```

---

### Étape 10 : Chiffrer Tous les Mots de Passe (2 min)

```cisco
SW_BUREAU_01(config)# service password-encryption
SW_BUREAU_01(config)# end
```

---

### Étape 11 : Vérification Complète (10 min)

```cisco
SW_BUREAU_01# show running-config
```

**Vérifier ligne par ligne :**

| **Ce qu'on doit voir** | **Trouvé ? ✅/❌** |
|------------------------|-------------------|
| `hostname SW_BUREAU_01` | |
| `no ip domain-lookup` | |
| Message du banner (entre `^C`) | |
| `enable secret 5 $1$...` (hash MD5) | |
| `line con 0` avec `password 7 ...` et `login` | |
| `line vty 0 4` avec `password 7 ...` et `login` | |
| `exec-timeout 5 0` sur con et vty | |

---

### Étape 12 : Observer la Table MAC (5 min)

```cisco
SW_BUREAU_01# show mac address-table
```

📝 La table est peut-être vide. Pour la remplir :

1. Aller sur **PC-Alice** → Desktop → Command Prompt
2. Taper : `ping 192.168.10.20` (vers PC-Bob)
3. Revenir sur le switch, retaper : `show mac address-table`

**Résultat attendu :**
```
          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    0001.xxxx.xxxx    DYNAMIC     Fa0/1
   1    0002.xxxx.xxxx    DYNAMIC     Fa0/2
Total Mac Addresses for this criterion: 2
```

📝 **Questions :**
- Combien d'entrées ? Pourquoi pas PC-Clara ?
- Quel type (DYNAMIC/STATIC) ?
- Après quel délai les entrées disparaîtront-elles ?

---

### Étape 13 : SAUVEGARDER ! (2 min)

```cisco
SW_BUREAU_01# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

**Vérification :**
```cisco
SW_BUREAU_01# show startup-config
```
→ La configuration doit être identique à `show running-config`.

---

### Étape 14 : Sauvegarde du Fichier Packet Tracer

1. Menu **File** → **Save As**
2. Nom : `NOM_Prenom_S6_TP_Switch_Config.pkt`
3. Sauvegarder dans votre dossier de travail.

✅ **TP Cisco terminé !**

---

## 📝 DEVOIR & LIVRABLE PORTFOLIO

### Titre du Devoir

**"Configuration Complète d'une Infrastructure Switch : TechPro SARL"**

---

### Contexte Professionnel

Vous êtes **technicien réseau** chez **InfoSys**, société de services informatiques. Votre client, **TechPro SARL** (cabinet d'ingénierie, 18 personnes), vient de recevoir ses équipements réseau neufs :

- 2 switchs Cisco 2960 (SWITCH_RDC et SWITCH_ETAGE)
- 18 PC répartis sur 2 étages
- Connexion Internet via une box (IP : `192.168.15.1`)

> *"Bonjour ! Les switchs sont arrivés, ils sont à l'état usine. Je veux que tu les configures correctement avec les conventions de notre entreprise InfoSys, que tu documentes ce que tu as fait, et que tu vérifies que le réseau fonctionne. Pour le reste, explique-moi comment un switch fonctionne pour que je puisse former mes équipes."*

---

### Consignes du Devoir

#### Partie 1 : Théorie - Fonctionnement d'un Switch (5 points)

**1.1 - Expliquer la table MAC** (2 pts)

Dans vos propres mots (pas de copier-coller du cours), expliquer :
- Comment un switch construit sa table MAC
- Ce qu'il se passe quand la MAC de destination est connue / inconnue
- Pourquoi un switch est meilleur qu'un hub (avec 1 exemple concret)

**1.2 - Exercice Domaines** (3 pts)

Pour le réseau suivant :
```
[PC1]─[PC2]─[SW1]─[SW2]─[PC3]─[PC4]─[PC5]
```

a) Combien de domaines de collision ?
b) Combien de domaines de diffusion ?
c) PC1 envoie un broadcast. Qui reçoit la trame ?
d) Pour séparer PC1/PC2 et PC3/PC4/PC5 en 2 domaines de diffusion, quel équipement ajouter et où ?

---

#### Partie 2 : Réalisation Packet Tracer (10 points)

**Topologie à créer :**

```
Réseau : 192.168.15.0/24
Passerelle : 192.168.15.1 (box - non simulée)

RDC (9 PC) :
PC-RDC-01 (192.168.15.11) ─Fa0/1─┐
PC-RDC-02 (192.168.15.12) ─Fa0/2─┤
...                                ┤  [SWITCH_RDC]
PC-RDC-09 (192.168.15.19) ─Fa0/9─┘

ÉTAGE (9 PC) :
PC-ETG-01 (192.168.15.21) ─Fa0/1─┐
...                                ┤  [SWITCH_ETAGE]
PC-ETG-09 (192.168.15.29) ─Fa0/9─┘

Liaison entre switchs :
SWITCH_RDC (Fa0/24) ─────── SWITCH_ETAGE (Fa0/24)
```

---

**2.1 - Topologie et câblage** (2 pts)

Créer la topologie dans Packet Tracer :
- 2 switchs Cisco 2960
- 6 PC minimum (3 par switch, représentant les 9)
- Interconnexion switch-switch
- Configuration IP de chaque PC (passerelle : `192.168.15.1`)

---

**2.2 - Configuration SWITCH_RDC** (4 pts)

Appliquer la **convention InfoSys** :

| **Élément** | **Convention InfoSys** |
|-------------|------------------------|
| Hostname | `SW-RDC-TECHPRO` |
| Banner | "TECHPRO SARL - Switch RDC - Acces reserve" |
| Enable Secret | `InfoSys@RDC2024` |
| Password Console | `Console@RDC` |
| Password VTY | `Vty@RDC` |
| Exec-timeout | 10 minutes |
| Chiffrement | Activé (`service password-encryption`) |
| Sauvegarde | `copy run start` |

---

**2.3 - Configuration SWITCH_ETAGE** (2 pts)

Même configuration en adaptant :
- Hostname : `SW-ETG-TECHPRO`
- Banner : "TECHPRO SARL - Switch ETAGE - Acces reserve"
- Passwords : même niveau, adapter les noms si souhaité

---

**2.4 - Tests et captures** (2 pts)

Réaliser et capturer (screenshots) :

| **Test** | **Depuis** | **Commande** | **Résultat attendu** |
|----------|------------|--------------|----------------------|
| Ping local | PC-RDC-01 | `ping 192.168.15.12` | ✅ 4 réponses |
| Ping inter-switch | PC-RDC-01 | `ping 192.168.15.21` | ✅ 4 réponses |
| Table MAC RDC | SW-RDC-TECHPRO | `show mac address-table` | Entrées visibles |
| Config sauvegardée | SW-RDC-TECHPRO | `show startup-config` | Config complète |

---

#### Partie 3 : Exercice Linux (5 points)

Sur votre **VM Debian** (installée en S5), réaliser et documenter (captures d'écran) :

**3.1 - Arborescence InfoSys** (2 pts)

Créer la structure suivante depuis le terminal :
```
/home/etudiant/InfoSys/
├── Clients/
│   ├── TechPro_SARL/
│   │   ├── config_switch_rdc.txt   → contenu : config complète du switch RDC
│   │   └── config_switch_etage.txt → contenu : config du switch ÉTAGE
│   └── README.txt                  → contenu : "Dossier clients InfoSys"
├── Scripts/
│   └── todo.txt                    → contenu : "TODO: ajouter scripts automatisation"
└── journal.txt                     → contenu : date du jour + "S6 : Configuration switches TechPro"
```

**3.2 - Manipulations de fichiers** (2 pts)

1. Copier `config_switch_rdc.txt` dans `/tmp/backup_rdc.txt`
2. Afficher `config_switch_rdc.txt` avec numéros de lignes
3. Ouvrir `journal.txt` avec nano, ajouter une ligne "Tests réussis : ping OK inter-switches", sauvegarder
4. Afficher les 5 dernières lignes de `journal.txt`
5. Lister le contenu de `/home/etudiant/InfoSys/` avec détails (`ls -lh`)

Fournir une **capture d'écran** pour chaque action.

**3.3 - Analyse `ls -l`** (1 pt)

À partir de la sortie de `ls -la /home/etudiant/InfoSys/`, répondre :
1. Qui est le propriétaire du dossier `Clients` ?
2. Que signifient les permissions `drwxr-xr-x` ?
3. Quelle est la taille de `journal.txt` ?

---

### Critères d'Évaluation (Barème Qualiopi)

| **Critère** | **Points** | **Indicateurs de Réussite** |
|-------------|------------|-----------------------------|
| **Théorie table MAC (1.1)** | /2 | Explication personnelle, forwarding/flooding corrects, comparaison hub pertinente |
| **Exercice domaines (1.2)** | /3 | 4 réponses correctes (collisions, diffusion, broadcast, équipement) |
| **Topologie Packet Tracer (2.1)** | /2 | 2 switchs + 6 PC + interconnexion, IP correctes |
| **Config SWITCH_RDC (2.2)** | /4 | 7 éléments configurés, sauvegardé, convention respectée |
| **Config SWITCH_ETAGE (2.3)** | /2 | Config complète, sauvegardée |
| **Tests + captures (2.4)** | /2 | 4 captures probantes, résultats positifs |
| **Arborescence Linux (3.1)** | /2 | Structure complète, contenu correct dans les fichiers |
| **Manipulations Linux (3.2)** | /2 | 5 actions réalisées avec captures |
| **Analyse ls -l (3.3)** | /1 | 3 réponses correctes |
| **Présentation et orthographe** | /2 | Document structuré, sans fautes majeures |
| **TOTAL** | **/20** | |

**Bonus (+2 pts max) :**
- Configuration SSH sur les switchs (clés RSA, `login local`) : +1 pt
- `show spanning-tree` commenté et analysé sur la liaison inter-switches : +1 pt
- Script bash créant l'arborescence Linux automatiquement : +1 pt
*(Maximum +2 pts)*

---

### Modalités de Rendu

- **Format :** Word/PDF (parties 1 et 3) + fichier Packet Tracer `.pkt`
- **Nom :** `NOM_Prenom_S6_Devoir_Switch_Linux.zip`
- **Deadline :** Avant la séance **S7**
- **Dépôt :** ENT / Moodle

---

### Lien Portfolio (E4/E5)

Situation professionnelle exploitable :
- **Contexte :** Déploiement et configuration de 2 switchs pour cabinet d'ingénierie (TechPro SARL)
- **Production :** Topologie Packet Tracer + configs CLI documentées + procédure Linux
- **Compétences :** B2.2 (config équipements), B2.3 (tests/diagnostic), B2.1 (Linux)
- **E5 (Pratique) :** Configuration CLI switch = compétence systématiquement évaluée

---

## ✅ CORRECTION ATTENDUE DU DEVOIR

*(Réservée à l'enseignant)*

### Partie 1.2 - Exercice Domaines

```
[PC1]─[PC2]─[SW1]─[SW2]─[PC3]─[PC4]─[PC5]
```

**a) Domaines de collision :**
- SW1 : 2 ports utilisés → 2 domaines (Port PC1 + Port PC2 + port vers SW2 = 3 domaines)
- SW2 : 3 ports utilisés → 3 domaines
- **Total : 5 domaines de collision** (1 par port de switch actif)
- *(Remarque : si SW1 a un port vers PC1, un vers PC2, un vers SW2 → 3 domaines sur SW1. SW2 : Port vers SW1, vers PC3, vers PC4, vers PC5 → 4 domaines. Total = **7** selon le schéma exact)*

**b) Domaines de diffusion :**
- **1 seul domaine de diffusion** (pas de routeur = tout le réseau est dans 1 domaine)

**c) Broadcast de PC1 :**
- Reçu par : **PC2, PC3, PC4, PC5** (tout le monde sauf l'émetteur)

**d) Pour séparer en 2 domaines de diffusion :**
- Ajouter un **routeur** entre SW1 et SW2

---

### Partie 2 : Configuration Switch complète

```cisco
! === SWITCH_RDC ===
enable
configure terminal
hostname SW-RDC-TECHPRO
no ip domain-lookup
banner motd #
TECHPRO SARL - Switch RDC - Acces reserve
#
enable secret InfoSys@RDC2024
line console 0
 password Console@RDC
 login
 exec-timeout 10 0
 exit
line vty 0 15
 password Vty@RDC
 login
 exec-timeout 10 0
 exit
service password-encryption
end
copy running-config startup-config

! === SWITCH_ETAGE ===
enable
configure terminal
hostname SW-ETG-TECHPRO
no ip domain-lookup
banner motd #
TECHPRO SARL - Switch ETAGE - Acces reserve
#
enable secret InfoSys@ETG2024
line console 0
 password Console@ETG
 login
 exec-timeout 10 0
 exit
line vty 0 15
 password Vty@ETG
 login
 exec-timeout 10 0
 exit
service password-encryption
end
copy running-config startup-config
```

---

### Partie 3.3 : Analyse `ls -la`

1. **Propriétaire de `Clients/`** : `etudiant` (l'utilisateur qui l'a créé)
2. **Permissions `drwxr-xr-x`** :
   - `d` = c'est un répertoire
   - `rwx` = propriétaire peut lire (r), écrire (w), exécuter/traverser (x)
   - `r-x` = groupe peut lire et traverser mais pas écrire
   - `r-x` = autres peuvent lire et traverser mais pas écrire
3. **Taille de `journal.txt`** : Dépend du contenu ajouté par l'étudiant (typiquement quelques dizaines à centaines d'octets)

---

### Grille de Correction Détaillée (Enseignant)

| **Critère** | **0 pt** | **1 pt** | **2-4 pts** |
|-------------|----------|----------|-------------|
| **Théorie table MAC** | Confused, inexact | Explication partielle | Forwarding/flooding clair, exemple hub pertinent |
| **Exercice domaines** | <2 bonnes | 2-3 bonnes | 4/4 correctes avec justifications |
| **Config switch (x2)** | <4 éléments | 5-6 éléments | 7 éléments + convention + sauvegardé |
| **Tests** | Pas de captures | Captures peu claires | 4 captures probantes, résultats positifs |
| **Arborescence Linux** | Structure manquante | Structure partielle | Complète + contenus corrects |
| **Manipulations** | <3 actions | 3-4 avec captures | 5/5 avec captures lisibles |

---

*Fin du Pack Semaine 6 - Bloc 2*

---

**🎉 Pack S6 - Bloc 2 "Commutation, Cisco CLI et Linux" terminé !**

Conforme au plan de formation :
- ✅ Commutation : switch, table MAC, domaines collision/diffusion
- ✅ Cisco CLI : accès console, modes (user/privileged/config), commandes show
- ✅ TP Cisco : configurer un switch (hostname, banner, passwords, save)
- ✅ Linux (suite) : commandes de base (ls, cd, cp, mv, rm, mkdir, cat, nano)
