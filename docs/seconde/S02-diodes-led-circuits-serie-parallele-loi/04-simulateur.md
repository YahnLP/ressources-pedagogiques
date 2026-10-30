# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans ElectroLab, clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## LED : calcul de la résistance de limitation

*Bac Pro CIEL (seconde) · durée indicative : 1 h*

Une LED doit être alimentée en 5 V. Une LED n'est pas une résistance : sans limitation, le courant explose et elle est détruite. Calculez la résistance de protection, choisissez une valeur normalisée et vérifiez à l'ampèremètre.

### 🎯 Objectifs

- Relever la tension de seuil d'une LED
- Calculer R = (E − V<sub>F</sub>) / I<sub>F</sub> avec la loi des mailles
- Choisir une valeur de la série E12 et vérifier le courant

### 🛠️ Marche à suivre

1. Avec MM1 (mode V⎓) mesurez la tension V<sub>F</sub> aux bornes de la LED. La résistance R1 est pour l'instant de 1 kΩ : relevez le courant avec MM2 (mA, en série). La LED brille-t-elle fort ?
2. On veut I<sub>F</sub> = 15 mA. Calculez R avec la loi des mailles E = R·I + V<sub>F</sub>. Choisissez la valeur E12 la plus proche.
3. Modifiez R1 (inspecteur), vérifiez I<sub>F</sub> et la puissance dissipée par R1.
4. <i>Pour réfléchir :</i> que se passerait-il avec R1 = 0 Ω ? (ne le faites pas : la LED serait détruite !)

### ❓ Questions

1. Tension V<sub>F</sub> mesurée aux bornes de la LED (en V)
2. Résistance théorique pour I<sub>F</sub> = 15 mA : R = (5 − V<sub>F</sub>)/I<sub>F</sub> (en Ω)
3. Valeur normalisée E12 la plus proche (en Ω)
4. Courant mesuré avec cette résistance (en mA)
5. Puissance dissipée par R1 (en mW)
6. Si l'on inverse la LED, elle…  
    - ☐ Brille plus fort  
    - ☐ Reste éteinte (diode bloquée, I ≈ 0)  
    - ☐ Est détruite à coup sûr  
    - ☐ Change de couleur

### 📥 Fichiers à ouvrir dans ElectroLab

- [`led-v1.json`](tp/led-v1.json) — Autre couleur de LED n° 1
- [`led-v2.json`](tp/led-v2.json) — Autre couleur de LED n° 2
- [`led-v3.json`](tp/led-v3.json) — Autre couleur de LED n° 3

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *LED : calcul de la résistance de limitation*.

## Associations de résistances et diviseur de courant

*Bac Pro CIEL (seconde) · durée indicative : 1 h*

Trois résistances forment un montage mixte : R1 en série avec R2 ∥ R3. Mesures hors tension, puis sous tension : tensions et courants dans chaque branche.

### 🎯 Objectifs

- Calculer et mesurer une résistance équivalente
- Constater qu'une mesure « en circuit » mesure l'ensemble du réseau
- Appliquer la loi des nœuds (I = I2 + I3)

### 🛠️ Marche à suivre

1. <b>Sortie de l'alim sur OFF.</b> Mesurez avec l'ohmmètre la résistance vue entre les bornes + et − de l'alimentation. Comparez au calcul R1 + (R2 ∥ R3).
2. Mesurez aux bornes de R2 (toujours hors tension) : pourquoi ne lit-on pas la valeur de R2 seule ?
3. Réglez 12 V, sortie ON. Mesurez la tension aux bornes de l'association R2 ∥ R3.
4. Insérez l'ampèremètre successivement dans R1, R2 puis R3 et vérifiez I1 = I2 + I3.

### ❓ Questions

1. R2 ∥ R3 calculée avec les valeurs nominales (en Ω)
2. Résistance équivalente vue par l'alimentation (en Ω, mesurée à l'ohmmètre sortie OFF)
3. Sous 12 V : courant total fourni par l'alimentation (en mA)
4. Tension aux bornes de R2 ∥ R3 (en V)
5. Courant dans R3 (en mA)
6. La branche qui reçoit le plus de courant est celle de…  
    - ☐ R2 (2,2 kΩ)  
    - ☐ R3 (3,3 kΩ)  
    - ☐ Les deux reçoivent le même courant

### 📥 Fichiers à ouvrir dans ElectroLab

- [`assoc.json`](tp/assoc.json)

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Associations de résistances et diviseur de courant*.
