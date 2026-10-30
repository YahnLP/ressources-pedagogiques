# Semaine 7 : Du cahier des charges au schéma et au PCB

> **Durée** : 4 h · **Compétences E2 travaillées** : C07

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Saisir un schéma dans KiCad (bibliothèques, alimentation, PWR_FLAG).
- Annoter, renseigner les valeurs, lancer et corriger l'ERC.
- Associer une empreinte à chaque composant.
- Placer et router un PCB selon des règles.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | TP virtuel ElectroLab : valider le clignoteur avant de le dessiner |
| 1 h | Schéma KiCad, ERC, empreintes |
| 1 h | Contour, règles, placement |
| 1 h | Routage et auto-test |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾**, puis fais ces TP **avant** de toucher au matériel :

- **NE555 en multivibrateur astable (4 fréquences)** (1 h 30, niveau première / terminale)

**Sujets à ouvrir dans ElectroLab** (bouton **Ouvrir**, puis choisis le fichier `.json`) :

- [`clignoteur.json`](tp/clignoteur.json) : le clignoteur NE555 complet (alimentation 5 V, fusible, NE555, LED, oscilloscope) ; relève la période T (attendu environ 1,01 s), la fréquence (environ 0,99 Hz), le rapport cyclique (environ 55 %) et la tension de sortie à l'état haut (environ 3,1 V)

> [!TIP] 🖥️ Pourquoi d'abord le simulateur ?
> On peut se tromper sans rien casser, répéter autant de fois que nécessaire et obtenir une correction automatique. Le TP réel sert ensuite à **confirmer** et à manipuler le vrai matériel.

## 📖 Le cours en bref

**🤔 À ton avis ?** Pourquoi dessiner le schéma **dans un logiciel** plutôt que sur papier, alors qu'on va ensuite faire le circuit imprimé ?

??? question "Réponse"
    Parce que le logiciel (KiCad) **garde en mémoire les liaisons** : c'est ce qu'il transmet ensuite au circuit imprimé (**netlist**). Une erreur de schéma se répercute partout : on la contrôle donc avant.

### 1. Le flux de travail

**Schéma → ERC → empreintes → PCB → DRC → fichiers de fabrication.** Chaque étape se **vérifie** avant la suivante.

### 2. Saisir un schéma dans KiCad (Eeschema)

1. **A** : ajouter un composant (cherche par nom : `R`, `LED`, `NE555`, `BC547`).
2. **P** : ajouter une alimentation (+5 V, GND).
3. **W** : tracer les fils.
4. **L** : poser une étiquette de réseau (net label) pour relier sans tracer.
5. **Annoter** (R1, R2…) et **saisir les valeurs**.
6. **ERC** : contrôle électrique.

### 3. L'ERC et ses erreurs classiques

| Erreur | Cause | Solution |
|---|---|---|
| `power_pin_not_driven` | KiCad ne sait pas qu'une source alimente le rail | poser un **PWR_FLAG** |
| `pin_not_connected` | broche en l'air | la relier, ou poser un **No Connect** (Q) |
| `duplicate_reference` | deux composants avec le même repère | annoter à nouveau |

### 4. Les empreintes (footprints)

L'**empreinte** est le dessin des **pastilles** sur le circuit imprimé. Elle doit correspondre au **boîtier réel** :

- **THT** (traversant) : pattes qui traversent la carte ; facile à souder à la main.
- **CMS** (monté en surface) : composant posé sur les pistes ; plus petit.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Choisir une empreinte **sans vérifier la datasheet** : le composant ne rentre pas.
> - Oublier les **PWR_FLAG** ou la **valeur** des composants.
> - Passer au PCB avec des erreurs d'ERC.

### 5. Les règles de conception

| Règle | Valeur courante | Pourquoi |
|---|---|---|
| **Clearance** (espace entre deux pistes) | 0,2 à 0,25 mm | éviter les courts-circuits |
| Piste de **signal** | 0,25 à 0,35 mm | faible courant |
| Piste d'**alimentation** | 0,5 à 0,8 mm | plus de courant |
| **Via** | Ø 0,8 mm, perçage 0,4 mm | passer d'une face à l'autre |

### 6. Placement et routage

1. **Contour** de la carte (Edge.Cuts).
2. Placer les **connecteurs au bord**, puis l'**alimentation**, puis le circuit principal, puis les passifs **près des circuits** qu'ils servent.
3. Le **condensateur de découplage** (100 nF) se place **au plus près** des broches d'alimentation du circuit intégré.
4. **Router l'alimentation en premier**, puis les signaux. Une masse **continue** (pas coupée par une piste) limite les perturbations.


## 🛠️ Atelier guidé : on construit, on mesure, on valide

**Fil rouge** : tu dessines le **schéma KiCad** du clignoteur.

1. Crée le projet `clignoteur`.
2. Place : connecteur 2 broches (J1, +12 V / GND), **7805** avec ses condensateurs (100 nF entrée, 10 µF sortie), **NE555**, $R_a$, $R_b$, $C_3$ (10 µF), **100 nF** sur la broche 5, $R_3$ (150 Ω) et la LED.
3. Câble : broche 4 et 8 au +5 V, broche 1 à la masse, 2 et 6 reliées entre elles et à $C_3$, 7 entre $R_a$ et $R_b$, sortie 3 vers $R_3$ puis LED vers la masse.
4. Ajoute 2 **PWR_FLAG** (+5 V et GND). **Annote**, renseigne les **valeurs**.
5. Lance l'**ERC** et corrige jusqu'à **0 erreur**.
6. Associe les **empreintes**.

??? success "Résultats attendus"
    - ERC : **0 erreur**.
    - Empreintes : R → `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal` ; LED → `LED_THT:LED_D5.0mm` ; NE555 → `Package_DIP:DIP-8_W7.62mm` ; 7805 → `Package_TO_SOT_THT:TO-220-3_Vertical` ; condensateur chimique → `Capacitor_THT:CP_Radial_D5.0mm_P2.50mm` ; connecteur → `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`.

## ✍️ Exercices d'application

1. L'ERC affiche `power_pin_not_driven` sur +5 V. Que faire ?
2. Deux composants portent le repère R1. Quelle erreur et quelle action ?
3. La broche 5 du NE555 n'est pas utilisée en astable : doit-elle rester non connectée ?
4. Où place-t-on le condensateur de découplage du NE555 ?

??? success "Corrigés"
    1. Poser un **PWR_FLAG** sur le net +5 V.
    2. `duplicate_reference` : **annoter à nouveau** le schéma.
    3. On la relie à la masse **par un condensateur de 100 nF** (stabilité) ; si on la laisse en l'air, l'ERC la signale (`pin_not_connected`) et le montage est plus sensible au bruit.
    4. **Au plus près** des broches 8 (VCC) et 1 (GND).

## 📚 Pour approfondir : les séances à consulter

- [Première S01 – interface et premiers schémas](../premiere/S01-interface-bibliotheques-schemas/01-cours.md)
- [Première S02 – saisie de schéma](../premiere/S02-kicad-saisie-de-schema-bibliotheques/01-cours.md)
- [Terminale S06 – flux KiCad complet](../terminale/S06-flux-kicad-complet-schema-erc-pcb-drc/01-cours.md)

## ✅ Auto-test

1. À quoi sert un PWR_FLAG ?
2. Que contrôle l'ERC ? Le DRC ?
3. Que se passe-t-il si une empreinte est mal choisie ?
4. Comment lever une erreur « pin not connected » voulue ?
5. Pourquoi corriger l'ERC avant le PCB ?
6. Quelle largeur pour une piste d'alimentation, quelle clearance ?

??? success "Réponses"
    1. À indiquer à KiCad qu'un rail d'alimentation est **bien alimenté** (évite l'erreur « power pin not driven »).
    2. L'ERC contrôle les **règles électriques du schéma** ; le DRC les **règles géométriques du PCB**.
    3. Le composant **ne rentre pas** sur la carte fabriquée.
    4. Poser un **No Connect** (touche Q).
    5. Une erreur de schéma se répercute sur **tout le PCB**.
    6. Piste d'alimentation **0,5 mm à 0,8 mm** ; clearance minimale **0,2 à 0,25 mm**.

## 📦 Livrable

Schéma complet NE555 + LED, ERC à 0 erreur, empreintes associées.
