# 📘 INTRODUCTION À KICAD — S1 · 2ᵉ ANNÉE · E2
## Interface · Bibliothèques · Schémas · Premiers pas en CAO électronique

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences** : S3.3 · C4.1

---

## 🔑 Vocabulaire clé

| Terme | Définition |
|---|---|
| **KiCad** | Suite logicielle open source de CAO électronique (EDA) — gratuit, professionnel, utilisé dans l'industrie |
| **EDA** | Electronic Design Automation — logiciel de conception électronique assistée par ordinateur |
| **Schématique (Schematic)** | Vue logique du circuit : symboles + connexions (ce que vous avez fait sur papier en 1A) |
| **Empreinte (Footprint)** | Vue physique d'un composant : dimensions exactes sur le circuit imprimé (PCB) |
| **Netlist** | Liste des connexions électriques — passerelle entre schéma et PCB |
| **PCB** | Printed Circuit Board — circuit imprimé · le KiCad PCB Editor design le PCB final |
| **BOM** | Bill Of Materials — nomenclature : liste de tous les composants du projet |
| **ERC** | Electrical Rules Check — vérification automatique des erreurs de schéma |
| **Bibliothèque de symboles** | Collection de symboles de composants (comme une liste de formes) |
| **Annotation** | Numérotation automatique des composants (R1, R2, C1, D1...) |
| **Net** | Connexion électrique nommée entre composants |
| **PWR_FLAG** | Symbole spécial indiquant au KiCad qu'un net d'alimentation est bien connecté à une source |

---

## 1️⃣ — Pourquoi KiCad ?

### Du papier au logiciel

```
1ère ANNÉE (dessin manuel) :
  ✓ Apprendre les symboles et les règles de schéma
  ✗ Difficile à modifier, pas de vérification automatique
  ✗ Impossible de générer un PCB directement

2ᵉ ANNÉE (KiCad) :
  ✓ Modification facile et rapide
  ✓ Vérification automatique des erreurs (ERC)
  ✓ Génération de la liste de composants (BOM)
  ✓ Passage direct au PCB pour fabrication
  ✓ Même outil que les ingénieurs en entreprise
```

### KiCad dans le monde réel

```
Projets open source conçus avec KiCad :
  Arduino Uno (depuis la version R3)
  Raspberry Pi Compute Module
  De nombreuses cartes de développement ESP32
  Équipements médicaux open source (OpenEEG, etc.)

Alternatives commerciales (pour info) :
  Altium Designer (> 8 000 €/an)
  Cadence OrCAD (> 5 000 €/an)
  Eagle (racheté par Autodesk)
  KiCad → 100% GRATUIT, même qualité professionnelle
```

---

## 2️⃣ — Interface KiCad : vue d'ensemble

### Le gestionnaire de projet (Project Manager)

```
Fenêtre principale de KiCad :
  ┌─────────────────────────────────────────────────────────┐
  │  File   View   Tools   Help                             │
  ├─────────────────────────────────────────────────────────┤
  │                    FICHIERS DU PROJET                    │
  │  ▶ mon_projet.kicad_pro      ← Fichier projet           │
  │  ▶ mon_schéma.kicad_sch      ← Schéma électronique      │
  │  ▶ mon_pcb.kicad_pcb         ← Circuit imprimé          │
  │  ▶ mon_symbole.kicad_sym     ← Symboles personnalisés   │
  ├─────────────────────────────────────────────────────────┤
  │  [Schematic Editor]  [PCB Editor]  [Symbol Editor]      │
  └─────────────────────────────────────────────────────────┘

WORKFLOW KiCad :
  1. Créer un projet (.kicad_pro)
  2. Dessiner le schéma (.kicad_sch) ← On commence ici en S1
  3. Associer les empreintes aux composants
  4. Mettre à jour le PCB
  5. Router les pistes sur le PCB
  6. Générer les fichiers Gerber pour fabrication
```

### Le Schematic Editor — zones clés

```
┌─────┬───────────────────────────────────────┬──────────┐
│     │  Barre d'outils horizontale             │          │
│  B  │─────────────────────────────────────────│  Barre  │
│  a  │                                         │  verti- │
│  r  │                                         │  cale   │
│  r  │         ZONE DE DESSIN                  │  (Pas-  │
│  e  │                                         │  ser)   │
│     │                                         │          │
│  g. │                                         │          │
└─────┴───────────────────────────────────────┴──────────┘

Raccourcis clavier essentiels :
  A → Ajouter un composant (Add Symbol)
  W → Ajouter un fil (Wire)
  P → Ajouter un symbole d'alimentation (Power)
  E → Éditer les propriétés d'un composant
  R → Faire pivoter
  X → Copier
  DEL → Supprimer
  Esc → Annuler l'outil en cours
  Ctrl+Z → Annuler
  Ctrl+S → Sauvegarder
  Molette → Zoom avant/arrière
  Clic droit → Menu contextuel
```

---

**🖼️ ILLUSTRATION 1 — Interface KiCad Schematic Editor**
> *Légende* : Capture annotée de l'interface KiCad Schematic Editor. La zone de dessin centrale est vide avec la grille visible. La barre d'outils de droite est annotée avec les 8 outils principaux (flèche sélection, fil, bus, label, symbole alimentation, add symbol, texte, ERC). En bas, la barre de coordonnées X/Y. Une infobulle montre le raccourci clavier de chaque outil. La palette de couleurs du schéma est indiquée (fond noir, fils verts, composants bleus).
>
> **Prompt illustration** : *"KiCad Schematic Editor interface screenshot in French with 8 annotation arrows. Dark background schematic canvas with grid. Right toolbar annotated: 'Sélectionner (S)', 'Fil (W)', 'Bus', 'Label net', 'Alimentation (P)', 'Symbole (A)', 'Texte', 'Vérif ERC'. Bottom status bar showing 'X: 0.00 Y: 0.00'. Keyboard shortcut labels next to each tool. Color scheme: black background, green wires, blue component symbols. French labels, UI screenshot style"*

---

## 3️⃣ — Les bibliothèques de symboles

### Accéder à la bibliothèque

```
Méthode 1 — Touche A (ou menu Place → Add Symbol) :
  → Ouvre le dialogue "Choose Symbol"
  → Barre de recherche en haut
  → Liste des bibliothèques à gauche
  → Aperçu du symbole à droite

Méthode 2 — Clic droit → Add Symbol
```

### Les bibliothèques principales

```
Device/        → Composants génériques (R, C, L, D, Q, LED...)
  Device:R            Résistance générique
  Device:C            Condensateur non polarisé
  Device:C_Polarized  Condensateur polarisé (électrolytique)
  Device:L            Inductance
  Device:LED          Diode LED
  Device:D            Diode standard
  Device:D_Zener      Diode Zener
  Device:Q_NPN_BCE    Transistor NPN
  Device:Q_PNP_BCE    Transistor PNP
  Device:Battery_Cell Pile
  Device:Conn_01x02   Connecteur 2 broches
  
power/         → Symboles d'alimentation
  power:+5V           Net +5V
  power:+3V3          Net +3,3V
  power:+12V          Net +12V
  power:GND           Masse
  power:VCC           Alimentation générique
  power:PWR_FLAG      Marqueur d'alimentation

Timer/         → Circuits intégrés de timing
  Timer:NE555         NE555

Amplifier/     → Amplificateurs
  Amplifier:LM741     Ampli op LM741

Regulator_Linear/ → Régulateurs de tension
  Regulator_Linear:LM7805 Régulateur 5V
```

### Chercher un composant efficacement

```
Dans la barre de recherche :
  "R"         → Affiche toutes les résistances
  "LED"       → Affiche toutes les LED
  "NPN"       → Tous les transistors NPN
  "555"       → Tous les circuits timers 555
  "LM74"      → LM741, LM747...

Astuce : utiliser le nom générique (Device:R) pour les composants courants
         plutôt que le modèle exact — l'empreinte sera associée plus tard
```

---

## 4️⃣ — Créer un schéma pas à pas

### Les 5 règles d'or du schéma KiCad

```
RÈGLE 1 : Toujours nommer et annoter les composants
  → Clic droit → Annotate Schematic → OK
  → R? devient R1, R2... · C? devient C1... automatiquement

RÈGLE 2 : Toujours connecter les fils jusqu'au bout des broches
  → Un fil qui s'arrête à 1 mm d'une broche = ERREUR
  → Le petit carré vert au bout d'une broche = broche libre = ERREUR potentielle

RÈGLE 3 : Ajouter PWR_FLAG sur chaque net d'alimentation
  → Sans PWR_FLAG → ERC signale "pin non connectée à une source"
  → Place → Add Power Port → PWR_FLAG

RÈGLE 4 : Nommer les signaux importants avec des labels nets
  → Menu Place → Net Label → nommer ex: "SIGNAL_A"
  → Deux broches avec le même label = connexion électrique (même fil)

RÈGLE 5 : Sauvegarder souvent (Ctrl+S)
  → KiCad peut crasher sur les vieux PC
```

### Exemple : circuit LED basique

```
OBJECTIF : LED rouge alimentée en 5V avec résistance de limitation

COMPOSANTS :
  R1 = Device:R, valeur "150Ω"
  D1 = Device:LED, valeur "LED rouge"
  +5V = power:+5V
  GND = power:GND
  2× PWR_FLAG

CÂBLAGE :
  +5V → fil → Pin 1 de R1 → fil → Pin 2 de R1 → fil → Anode (pin K+) de D1 → fil → Cathode → GND

VÉRIFICATION :
  1. Annotate Schematic (R? → R1, D? → D1)
  2. Run ERC (Electric Rules Check) → 0 erreur
  3. Ctrl+S pour sauvegarder
```

---

**🖼️ ILLUSTRATION 2 — Schéma LED dans KiCad annoté**
> *Légende* : Capture d'un schéma KiCad simple sur fond noir montrant : symbole +5V en haut (flèche vers le haut), fil vertical, résistance R1 "150Ω" au centre, fil, LED D1 avec ses flèches de lumière, fil, symbole GND en bas. Les broches sont annotées (Pin 1/Pin 2 de R1, A/K de D1). Des flèches colorées indiquent : la direction du courant conventionnel, où placer les PWR_FLAG, le sens de la LED (A=anode haut, K=cathode bas), la valeur et référence de chaque composant.
>
> **Prompt illustration** : *"KiCad schematic screenshot in French showing simple LED circuit on dark background. Components from top to bottom: +5V power symbol, wire, R1 resistor (150Ω label), wire, D1 LED (with light arrow symbols), wire, GND symbol. Two PWR_FLAG symbols on VCC and GND. Green wires connecting everything. Annotation arrows: red arrow 'Sens courant conventionnel', blue arrow 'PWR_FLAG obligatoire', orange arrow 'A=Anode (haut), K=Cathode (bas)', yellow arrows on component values '150Ω' and 'LED rouge'. French labels, KiCad dark theme UI style"*

---

## 5️⃣ — L'ERC : trouver et corriger les erreurs

### Ce que l'ERC détecte

```
ERREURS FRÉQUENTES EN DÉBUTANT :

Erreur "Pin not connected" :
  → Une broche de composant n'est connectée à rien
  → Solution : connecter la broche, ou marquer comme "no connect" (X)

Erreur "Net has no driver" :
  → Un net d'alimentation n'a pas de source (pas de PWR_FLAG)
  → Solution : ajouter PWR_FLAG sur le net VCC et GND

Erreur "Duplicate reference" :
  → Deux composants ont le même numéro (ex: deux R1)
  → Solution : Annotate Schematic pour renommer automatiquement

Erreur "Wire not connected" :
  → Un fil se termine dans le vide sans se connecter à une broche
  → Solution : étirer le fil jusqu'à la broche exacte

Avertissement "Simulation model issue" :
  → Composant sans modèle de simulation (ignorable en 2A)
```

### Lancer l'ERC

```
Menu : Inspect → Electrical Rules Checker (ERC)
Ou   : Touche I (Inspect)
Résultat :   0 erreurs, 0 avertissements = PARFAIT ✓
             Erreurs présentes = cliquer sur chaque pour voir l'emplacement
```

---

## 📌 Raccourcis KiCad à maîtriser en priorité

| Raccourci | Action | Usage |
|---|---|---|
| **A** | Ajouter un symbole | Placer une résistance, LED... |
| **P** | Ajouter un symbole d'alimentation | Ajouter +5V, GND... |
| **W** | Tracer un fil | Connecter les composants |
| **E** | Éditer les propriétés | Changer la valeur d'une résistance |
| **R** | Rotation | Orienter un composant |
| **G** | Drag (déplacer avec les fils) | Déplacer sans déconnecter |
| **M** | Move (déplacer sans les fils) | Attention : peut déconnecter |
| **DEL** | Supprimer | Effacer un composant ou un fil |
| **Ctrl+Z** | Annuler | Revenir en arrière |
| **Ctrl+S** | Sauvegarder | SOUVENT ! |
| **I** ou **F9** | ERC | Vérifier les erreurs |
| **Molette** | Zoom | Navigation |

---

## 📌 À retenir pour la suite

> ✅ KiCad = **gratuit** + **professionnel** + **utilisé dans l'industrie**
> ✅ Workflow : Schéma → Empreintes → PCB → Gerber (fabrication)
> ✅ En S1, on se concentre sur le **Schematic Editor**
> ✅ Raccourcis clés : A (symbole), P (alim.), W (fil), E (éditer), R (rotation)
> ✅ PWR_FLAG obligatoire sur chaque net d'alimentation
> ✅ Toujours finir par Annotate + ERC avant de sauvegarder

---

*Introduction KiCad — BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S1*
*Compétences : S3.3 · C4.1*
