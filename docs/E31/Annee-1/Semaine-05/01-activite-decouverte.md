# ACTIVITÉ DÉCOUVERTE - U31 Réseaux Informatiques
## Semaine 5 - "Le Facteur Intelligent" : Comprendre le Switch par Simulation

---

## 🎯 OBJECTIFS DE L'ACTIVITÉ

### Objectifs pédagogiques

- **Comprendre intuitivement** le fonctionnement d'un switch (apprentissage, forwarding, flooding)
- **Découvrir** la notion de table MAC (association adresse MAC ↔ port)
- **Différencier** domaine de collision et domaine de broadcast
- **Introduire** la segmentation par VLANs
- **Expérimenter** les 4 processus : learning, forwarding, flooding, filtering

### Compétences transversales

- Expression orale (jouer un rôle)
- Observation et analyse
- Travail collaboratif
- Prise de notes structurée

---

## ⏱️ DURÉE ET ORGANISATION

| **Élément** | **Détail** |
|-------------|------------|
| **Durée totale** | 25 minutes |
| **Modalité** | Jeu de rôle collectif + observation |
| **Effectif** | 12-16 apprentis |
| **Répartition** | 1 switch + 8 ordinateurs + 7 observateurs |
| **Lieu** | Salle de TP avec espace dégagé (ou en extérieur) |
| **Moment** | Début de séance (00:00 - 00:25) |

---

## 🛠️ MATÉRIEL NÉCESSAIRE

### Matériel à préparer par le formateur

| **Quantité** | **Matériel** | **Spécifications** |
|--------------|--------------|-------------------|
| 8 | Fiches "Adresse MAC" | Format A5, imprimées (ex: MAC-A, MAC-B, ..., MAC-H) |
| 8 | Badges numérotés "Port" | Numéros 1 à 8 pour les ports du switch |
| 1 | Grand tableau blanc ou paperboard | Pour noter la "table MAC" du switch |
| 1 | Badge "SWITCH" | Pour identifier le switch humain |
| 8 | Enveloppes colorées | Pour simuler les "trames réseau" |
| 1 | Chronomètre | Pour mesurer les temps de traitement |
| 7 | Fiches d'observation | Pour les apprentis observateurs |
| 1 | Scotch de couleur (2 couleurs) | Pour délimiter 2 zones (VLAN 1 et VLAN 2) |

### Préparation des fiches "Adresse MAC"

**Modèle de fiche (format A5) :**

```
┌─────────────────────────────────┐
│                                 │
│      ORDINATEUR A               │
│                                 │
│   Adresse MAC :                 │
│   00:1A:2B:3C:4D:5E             │
│                                 │
│   Adresse IP :                  │
│   192.168.1.10                  │
│                                 │
└─────────────────────────────────┘
```

**Liste des 8 ordinateurs :**

| **Ordinateur** | **Adresse MAC** | **Adresse IP** |
|---------------|----------------|---------------|
| A | 00:1A:2B:3C:4D:5E | 192.168.1.10 |
| B | 00:AA:BB:CC:DD:01 | 192.168.1.20 |
| C | 00:11:22:33:44:55 | 192.168.1.30 |
| D | 00:50:56:AB:CD:EF | 192.168.1.40 |
| E | 00:0C:29:5A:3B:1F | 192.168.1.50 |
| F | 00:1B:21:3A:4C:5D | 192.168.1.60 |
| G | 00:DE:AD:BE:EF:00 | 192.168.1.70 |
| H | 00:CA:FE:BA:BE:01 | 192.168.1.80 |

---

## 📋 DÉROULÉ DE L'ACTIVITÉ (25 min)

### Phase 1 : Mise en place et présentation (5 min)

#### Attribution des rôles

**Le formateur désigne :**

1. **1 Switch** (apprenti volontaire, organisé)
   - Rôle : Traiter les trames et gérer la table MAC
   - Matériel : Badge "SWITCH" + Tableau blanc + Marqueur

2. **8 Ordinateurs** (apprentis actifs)
   - Rôle : Envoyer et recevoir des trames
   - Matériel : 1 fiche MAC + 1 badge numéro de port
   - Répartition :
     - Ports 1-4 : Zone VLAN 1 (scotch bleu)
     - Ports 5-8 : Zone VLAN 2 (scotch rouge)

3. **7 Observateurs** (reste du groupe)
   - Rôle : Observer et noter le processus
   - Matériel : Fiche d'observation + stylo

---

#### Règles du jeu

**Le formateur explique :**

> "Vous allez simuler un réseau Ethernet avec un switch.
>
> **Les ordinateurs** veulent communiquer entre eux (s'envoyer des messages). Pour cela, ils donnent leurs **trames** (enveloppes) au **switch**.
>
> **Le switch** doit :
> 1. **Apprendre** quelle adresse MAC est sur quel port (remplir sa table)
> 2. **Décider** où envoyer chaque trame (bon port, ou tous les ports)
>
> **Observateurs** : Notez tout ce qui se passe. On fera le lien avec les vrais switches après."

---

#### Délimitation de l'espace

**Le formateur organise l'espace :**

```
         [SWITCH]
         (Centre)
            │
    ┌───────┴───────┐
    │               │
 VLAN 1          VLAN 2
(Bleu)          (Rouge)
    │               │
PC1 PC2         PC5 PC6
PC3 PC4         PC7 PC8
```

- Le **switch** se positionne au centre (avec son tableau)
- Les **8 ordinateurs** se placent en cercle autour du switch, chacun à son "port"
- Les **observateurs** se placent en périphérie avec vue sur la scène

---

### Phase 2 : Scénario 1 - Apprentissage de la table MAC (7 min)

#### 🎬 Situation initiale

**Le formateur annonce :**

> "Le switch vient d'être allumé. Sa **table MAC est vide**. Il ne sait pas encore qui est connecté sur quel port."

**Table MAC du switch (vide) :**

```
┌──────────────────────────────────┐
│      TABLE MAC DU SWITCH         │
├──────────────┬──────────┬────────┤
│ Adresse MAC  │   Port   │  VLAN  │
├──────────────┼──────────┼────────┤
│              │          │        │
│              │          │        │
└──────────────┴──────────┴────────┘
```

---

#### 🎬 Trame 1 : Ordinateur A envoie à Ordinateur B

**Action :**

1. **Ordinateur A** (port 1) prend une enveloppe et écrit dessus :
   - Source : 00:1A:2B:3C:4D:5E (MAC-A)
   - Destination : 00:AA:BB:CC:DD:01 (MAC-B)
   - Message : "Salut B !"

2. **Ordinateur A** donne l'enveloppe au **switch** et dit :
   > "Je suis sur le port 1, voici ma trame !"

3. **Le switch** lit la trame :
   - Lit l'adresse **source** : MAC-A
   - **Apprend** : "MAC-A est sur le port 1"
   - **Note dans sa table MAC** :

```
┌──────────────────────────────────┐
│      TABLE MAC DU SWITCH         │
├──────────────┬──────────┬────────┤
│ Adresse MAC  │   Port   │  VLAN  │
├──────────────┼──────────┼────────┤
│ MAC-A        │    1     │   1    │
└──────────────┴──────────┴────────┘
```

4. **Le switch** lit l'adresse **destination** : MAC-B
   - Consulte sa table → **MAC-B n'est pas dans la table !**
   - Décision : **FLOODING** (diffusion)

5. **Le switch** annonce :
   > "Je ne connais pas MAC-B. Je vais envoyer cette trame à **tous les ports** (sauf le port 1 d'où elle vient)."

6. **Le switch** donne l'enveloppe à tous les ordinateurs (ports 2-8)

7. Chaque ordinateur regarde l'adresse destination :
   - **Ordinateur B** : "C'est pour moi !" → **Accepte la trame**
   - **Ordinateurs C, D, E, F, G, H** : "Ce n'est pas pour moi" → **Ignorent**

---

**💡 Formateur explique aux observateurs :**

> "Processus **Learning** : Le switch a appris que MAC-A est sur le port 1.
>
> Processus **Flooding** : Comme il ne connaissait pas MAC-B, il a diffusé partout."

---

#### 🎬 Trame 2 : Ordinateur B répond à Ordinateur A

**Action :**

1. **Ordinateur B** (port 2) crée une enveloppe :
   - Source : MAC-B
   - Destination : MAC-A
   - Message : "Salut A, bien reçu !"

2. **Ordinateur B** donne l'enveloppe au **switch**

3. **Le switch** lit la trame :
   - Lit l'adresse **source** : MAC-B
   - **Apprend** : "MAC-B est sur le port 2"
   - **Note dans sa table** :

```
┌──────────────────────────────────┐
│      TABLE MAC DU SWITCH         │
├──────────────┬──────────┬────────┤
│ Adresse MAC  │   Port   │  VLAN  │
├──────────────┼──────────┼────────┤
│ MAC-A        │    1     │   1    │
│ MAC-B        │    2     │   1    │
└──────────────┴──────────┴────────┘
```

4. **Le switch** lit l'adresse **destination** : MAC-A
   - Consulte sa table → **MAC-A est sur le port 1 !**
   - Décision : **FORWARDING** (acheminement direct)

5. **Le switch** annonce :
   > "Je connais MAC-A ! Il est sur le port 1. J'envoie la trame **uniquement** sur ce port."

6. **Le switch** donne l'enveloppe **seulement à l'Ordinateur A**

7. **Ordinateur A** : "C'est pour moi !" → **Reçoit le message**

---

**💡 Formateur explique :**

> "Processus **Forwarding** : Le switch connaissait la destination, il a envoyé **directement** sur le bon port. Plus rapide et pas de trafic inutile !"

---

#### 🎬 Trames 3-4 : Remplissage progressif de la table

**Le formateur accélère :**

> "Maintenant, les ordinateurs C, D, E vont envoyer des messages. Le switch va apprendre leurs positions."

**Trames à simuler rapidement :**
- C → D : Switch apprend MAC-C (port 3), flooding pour D, puis apprend MAC-D (port 4)
- E → F : Switch apprend MAC-E (port 5), flooding pour F, puis apprend MAC-F (port 6)

**Table MAC après 6 trames :**

```
┌──────────────────────────────────┐
│      TABLE MAC DU SWITCH         │
├──────────────┬──────────┬────────┤
│ Adresse MAC  │   Port   │  VLAN  │
├──────────────┼──────────┼────────┤
│ MAC-A        │    1     │   1    │
│ MAC-B        │    2     │   1    │
│ MAC-C        │    3     │   1    │
│ MAC-D        │    4     │   1    │
│ MAC-E        │    5     │   2    │
│ MAC-F        │    6     │   2    │
└──────────────┴──────────┴────────┘
```

---

### Phase 3 : Scénario 2 - Domaines de collision et broadcast (5 min)

#### 🎬 Situation : Trame de broadcast

**Le formateur explique :**

> "L'ordinateur A veut annoncer quelque chose à **tout le monde** (exemple : découverte ARP). Il envoie une trame de **broadcast**."

**Action :**

1. **Ordinateur A** crée une enveloppe :
   - Source : MAC-A
   - Destination : **FF:FF:FF:FF:FF:FF** (broadcast)
   - Message : "Qui a l'IP 192.168.1.50 ?"

2. **Le switch** lit la destination :
   - Destination = Broadcast
   - Décision : **FLOODING** systématique (tous les ports de son VLAN)

3. **Le switch** annonce :
   > "C'est un broadcast ! J'envoie à **tous les ports du VLAN 1** (ports 1-4)."

4. **Ordinateurs A, B, C, D** reçoivent tous le message

5. **Ordinateurs E, F, G, H** (VLAN 2) **ne reçoivent PAS** le message

---

**💡 Formateur explique :**

> "**Domaine de broadcast** : Tous les équipements qui reçoivent les broadcasts.
>
> Sans VLAN : 1 seul domaine (tous les ports)
>
> Avec VLANs : 1 domaine par VLAN (isolation)"

---

#### Comparaison Hub vs Switch

**Le formateur fait une démonstration :**

**Avec un HUB (ancien) :**

> "Si c'était un hub, même pour une trame unicast (A → B), **tous les ordinateurs** recevraient la trame. Il y aurait **1 seul domaine de collision** → Collisions possibles."

**Avec un SWITCH (moderne) :**

> "Le switch crée **1 domaine de collision par port**. Aucune collision possible, même si plusieurs paires communiquent en même temps :
> - A ↔ B sur les ports 1-2
> - C ↔ D sur les ports 3-4
> - E ↔ F sur les ports 5-6
>
> Simultanément, sans problème !"

---

### Phase 4 : Scénario 3 - Segmentation par VLANs (5 min)

#### 🎬 Situation : Communication inter-VLAN impossible

**Le formateur annonce :**

> "L'ordinateur A (VLAN 1) veut parler à l'ordinateur E (VLAN 2)."

**Action :**

1. **Ordinateur A** (port 1, VLAN 1) crée une enveloppe :
   - Source : MAC-A
   - Destination : MAC-E
   - Message : "Salut E !"

2. **Le switch** lit la trame :
   - Source : MAC-A (VLAN 1)
   - Destination : MAC-E
   - Consulte la table → MAC-E est sur le port 5 (VLAN 2)

3. **Le switch** vérifie les VLANs :
   - Source VLAN : 1
   - Destination VLAN : 2
   - **VLANs différents !**

4. **Le switch** annonce :
   > "ATTENTION ! MAC-A est dans VLAN 1, MAC-E est dans VLAN 2. Je ne peux **pas** transférer cette trame entre VLANs. Je la **bloque**."

5. **Ordinateur E** ne reçoit **jamais** le message

6. **Ordinateur A** ne reçoit **pas de réponse**

---

**💡 Formateur explique :**

> "Les **VLANs** créent des **réseaux logiques séparés** sur le même switch physique.
>
> C'est comme si vous aviez **2 switches différents** :
> - Switch 1 : Ports 1-4 (VLAN 1)
> - Switch 2 : Ports 5-8 (VLAN 2)
>
> Pour faire communiquer VLAN 1 et VLAN 2, il faut un **routeur** (on verra ça plus tard)."

---

#### Question aux ordinateurs VLAN 2

**Le formateur demande aux ordinateurs E, F, G, H :**

> "Pourquoi vos ports sont dans un VLAN séparé ?"

**Réponses attendues :**
- "Pour la sécurité (isoler les départements)"
- "Pour réduire le trafic de broadcast"
- "Pour organiser logiquement le réseau"

---

### Phase 5 : Débriefing collectif (3 min)

**Le formateur fait revenir tous les apprentis en position assise.**

**Questions posées au groupe :**

1. **"Qu'est-ce que le switch a fait en premier ?"**
   - Réponse attendue : Apprendre les adresses MAC (learning)

2. **"Que fait le switch quand il ne connaît pas la destination ?"**
   - Réponse attendue : Flooding (envoie partout)

3. **"Quelle différence entre un hub et un switch ?"**
   - Réponse attendue : Le switch prend des décisions intelligentes, le hub répète bêtement

4. **"À quoi servent les VLANs ?"**
   - Réponses attendues : Sécurité, isolation, réduction du broadcast, organisation logique

5. **"Combien de domaines de collision dans un switch 8 ports ?"**
   - Réponse attendue : 8 (1 par port)

---

## 📄 FICHE D'OBSERVATION (Modèle pour les observateurs)

```
═══════════════════════════════════════════════════════════
     📝 FICHE D'OBSERVATION - SIMULATION SWITCH
═══════════════════════════════════════════════════════════

Nom : _____________________ Prénom : _____________________

Date : ___/___/___


┌─────────────────────────────────────────────────────────┐
│  APPRENTISSAGE DE LA TABLE MAC                           │
└─────────────────────────────────────────────────────────┘

Trame 1 : A → B

Que fait le switch avec l'adresse SOURCE (MAC-A) ?
_________________________________________________________________

Que fait le switch avec l'adresse DESTINATION (MAC-B) ?
_________________________________________________________________

Pourquoi le switch envoie-t-il la trame à TOUS les ports ?
_________________________________________________________________


Trame 2 : B → A

Que fait le switch avec l'adresse SOURCE (MAC-B) ?
_________________________________________________________________

Pourquoi le switch envoie-t-il la trame SEULEMENT au port 1 ?
_________________________________________________________________


┌─────────────────────────────────────────────────────────┐
│  TABLE MAC FINALE (après 6 trames)                       │
└─────────────────────────────────────────────────────────┘

Dessine la table MAC telle qu'elle apparaît sur le tableau :

┌──────────────┬──────────┬────────┐
│ Adresse MAC  │   Port   │  VLAN  │
├──────────────┼──────────┼────────┤
│              │          │        │
│              │          │        │
│              │          │        │
│              │          │        │
│              │          │        │
│              │          │        │
└──────────────┴──────────┴────────┘


┌─────────────────────────────────────────────────────────┐
│  DOMAINES DE COLLISION ET BROADCAST                      │
└─────────────────────────────────────────────────────────┘

Qu'est-ce qu'un domaine de collision ?
_________________________________________________________________
_________________________________________________________________

Combien de domaines de collision dans notre switch de 8 ports ?
_________________________________________________________________

Qu'est-ce qu'un domaine de broadcast ?
_________________________________________________________________

Combien de domaines de broadcast avec 2 VLANs ?
_________________________________________________________________


┌─────────────────────────────────────────────────────────┐
│  SEGMENTATION PAR VLANs                                  │
└─────────────────────────────────────────────────────────┘

Pourquoi l'ordinateur A (VLAN 1) ne peut pas parler à E (VLAN 2) ?
_________________________________________________________________
_________________________________________________________________

À quoi servent les VLANs selon toi ?
1. ___________________________________________________________
2. ___________________________________________________________
3. ___________________________________________________________


┌─────────────────────────────────────────────────────────┐
│  LES 4 PROCESSUS DU SWITCH                               │
└─────────────────────────────────────────────────────────┘

Complète :

1. **Learning** (Apprentissage) :
   Le switch apprend ____________________________________________

2. **Forwarding** (Acheminement) :
   Le switch envoie la trame ____________________________________

3. **Flooding** (Inondation) :
   Le switch diffuse la trame ___________________________________

4. **Filtering** (Filtrage) :
   Le switch bloque la trame ____________________________________


═══════════════════════════════════════════════════════════
```

---

## 🎓 APPRENTISSAGES ATTENDUS

### Ce que les apprentis vont découvrir intuitivement

| **Découverte** | **Lien avec le cours théorique** |
|----------------|----------------------------------|
| "Le switch note quelle MAC est sur quel port" | Table MAC (CAM table) |
| "Le switch envoie directement si il connaît" | Processus Forwarding |
| "Le switch diffuse partout si il ne sait pas" | Processus Flooding |
| "Chaque port a sa propre voie" | Domaine de collision par port |
| "Le broadcast va à tout le monde" | Domaine de broadcast |
| "Les VLANs empêchent de communiquer" | Segmentation logique |
| "La table se remplit au fur et à mesure" | Apprentissage dynamique |

---

## 💡 CONSEILS POUR LE FORMATEUR

### Gestion du jeu de rôle

**Si les apprentis sont timides :**
- Le formateur peut jouer le rôle du switch lui-même
- Simplifier les adresses MAC (MAC-A, MAC-B au lieu des valeurs hexadécimales)
- Réduire le nombre d'ordinateurs (4 au lieu de 8)

**Si les apprentis sont très à l'aise :**
- Introduire le concept de **vieillissement** (aging) : "Après 5 minutes, les entrées disparaissent"
- Simuler une **saturation de table MAC** (attaque)
- Ajouter un **routeur** pour faire communiquer les VLANs

**Si le temps manque :**
- Faire uniquement les scénarios 1 et 2 (apprentissage + domaines)
- Expliquer les VLANs théoriquement sans simulation

---

### Variantes pédagogiques

**Version simplifiée (15 min) :**
- 1 switch + 4 ordinateurs
- Scénario 1 uniquement (apprentissage)
- Pas de VLANs

**Version approfondie (35 min) :**
- Ajouter un 2ème switch connecté en trunk
- Simuler le protocole Spanning Tree (boucles réseau)
- Introduire le port mirroring (pour Wireshark)

**Version théâtralisée :**
- Costumes (le switch porte une casquette "Postier Intelligent")
- Décor (dessiner un switch géant au sol avec scotch)
- Musique de fond (son de datacenter)

---

## ✅ CRITÈRES DE RÉUSSITE DE L'ACTIVITÉ

L'activité est réussie si :

| **Indicateur** | **Critère** |
|----------------|-------------|
| **Engagement** | Au moins 90% des apprentis participent (rôles ou observations) |
| **Compréhension processus** | Les observateurs identifient learning et forwarding |
| **Découverte table MAC** | Les apprentis comprennent que le switch "note" les associations |
| **Différenciation domaines** | Les apprentis distinguent collision et broadcast |
| **Intérêt VLANs** | Au moins 2 avantages des VLANs cités spontanément |

---

## 🔗 TRANSITION VERS LE COURS

**Script de transition (à dire aux apprentis après l'activité) :**

> "Bravo pour cette simulation ! Vous venez de jouer le rôle d'un **switch Ethernet**, un équipement réseau intelligent de **couche 2**.
>
> Ce que vous avez découvert :
> - La **table MAC** (le tableau que le switch a rempli)
> - Les **4 processus** : Learning, Forwarding, Flooding, Filtering
> - Les **domaines** : 1 collision par port, 1 broadcast par VLAN
> - Les **VLANs** : segmentation logique pour isoler
>
> Maintenant, on va voir comment ça fonctionne **en vrai** :
> - Se connecter à un switch Cisco en CLI
> - Créer des VLANs avec des commandes
> - Analyser une vraie table MAC avec `show mac address-table`
> - Configurer des ports en mode access
>
> Sortez vos fiches de cours, on plonge dans le monde des switches !"

---

## 📊 GRILLE D'OBSERVATION FORMATEUR (pendant l'activité)

| **Critère** | **Observations** |
|-------------|------------------|
| **Apprentis très engagés** (noms) | |
| **Apprentis en retrait** (noms) | |
| **Questions pertinentes posées** | |
| **Incompréhensions détectées** | |
| **Points à reprendre dans le cours** | |

---

## 🎯 LIEN AVEC LE PORTFOLIO

Cette activité prépare la compétence C3.3 pour le portfolio :

> "J'ai participé à une simulation physique du fonctionnement d'un switch Ethernet. J'ai observé les processus d'apprentissage de la table MAC (learning), d'acheminement direct (forwarding) et de diffusion (flooding). J'ai compris la différence entre domaine de collision (1 par port) et domaine de broadcast (1 par VLAN). Cette expérience m'a permis de visualiser concrètement le rôle d'un switch avant de le configurer techniquement."

---

## 📸 PHOTO-SOUVENIR (optionnel)

**Idée bonus :** Prendre une photo de groupe avec :
- Le switch au centre (avec son tableau de table MAC rempli)
- Les 8 ordinateurs autour (brandissant leurs fiches MAC)
- Les observateurs en arrière-plan

**Légende :**
> "Promotion 2024-2027 - Simulation Switch - S5 Réseaux - 24/02/2026"

→ À afficher en salle de TP ou à intégrer dans le portfolio collectif

---

**Document créé le :** 24/02/2026  
**Auteur :** Équipe pédagogique CFA  
**Version :** 1.0  
**Durée de l'activité :** 25 minutes
