# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans [ElectroLab](https://yahnlp.github.io/ElectroLab/), clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## Le transformateur : rapport de transformation

*Bac Pro CIEL (première) · durée indicative : 1 h*

Un transformateur 230 V / 12 V est alimenté par le secteur à vide. Mesurez les tensions primaire et secondaire au multimètre (V∿) et à l'oscilloscope, puis déterminez le rapport de transformation.<p><b>⚠ Sécurité :</b> le secteur 230 V est <b>mortel</b>. Dans ce simulateur on s'entraîne sans danger, mais dans la réalité on ne touche jamais à un circuit relié au secteur : on débranche, on attend la décharge des condensateurs, on vérifie l'absence de tension, <i>puis</i> on intervient.</p>

### 🎯 Objectifs

- Mesurer une tension alternative (valeur efficace) au multimètre en mode V∿
- Relever la valeur maximale et la période à l'oscilloscope
- Calculer le rapport de transformation m = $U_{s}$/$U_{p}$
- Distinguer valeur efficace et valeur maximale : $U_{max}$ = $U_{eff}$·√2

### 🛠️ Marche à suivre

1. Placez MM1 (mode <b>V∿</b>) aux bornes du primaire (P1–P2) et relevez $U_{p}$.
2. Déplacez MM1 aux bornes du secondaire (S1–S2) et relevez $U_{s}$ (à vide, le secondaire délivre un peu plus que 12 V).
3. Câblez l'oscilloscope : CH1 sur S1, GND sur S2 (<i>le secondaire est isolé du secteur</i>). Mesurez $U_{max}$ et la période T.
4. Calculez m, $U_{max}$/$U_{eff}$ et la fréquence.

### ❓ Questions

1. Tension efficace primaire $U_{p}$ (en V)
2. Tension efficace secondaire à vide $U_{s}$ (en V)
3. Rapport de transformation m = $U_{s}$ / $U_{p}$ (sans unité, 3 décimales)
4. Valeur maximale du secondaire $U_{max}$ relevée à l'oscilloscope (en V)
5. Période du signal (en ms)
6. Le transformateur d'isolement…  
    - ☐ Transforme le courant alternatif en courant continu  
    - ☐ Abaisse (ou élève) la tension alternative et isole galvaniquement le secondaire du secteur  
    - ☐ Modifie la fréquence du réseau  
    - ☐ Stocke l'énergie électrique

### 📥 Fichiers à ouvrir dans ElectroLab

- [`transfo.json`](tp/transfo.json)

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Le transformateur : rapport de transformation*.

## Redressement simple et double alternance

*Bac Pro CIEL (première) · durée indicative : 1 h 15*

Un transformateur alimente une résistance de charge à travers un redresseur. Visualisez la tension aux bornes de la charge, mesurez sa valeur moyenne (V⎓) et sa fréquence, et comparez le redressement <b>simple alternance</b> (1 diode) au <b>double alternance</b> (pont de 4 diodes).

### 🎯 Objectifs

- Reconnaître le rôle d'une diode (conduction dans un seul sens)
- Observer la tension redressée à l'oscilloscope
- Mesurer la valeur moyenne avec un multimètre en V⎓
- Comparer fréquence et valeur moyenne des deux montages

### 🛠️ Marche à suivre

1. Câblez l'oscilloscope : CH1 sur le secondaire (S1), CH2 sur la charge RL, masses reliées ; affichez les deux voies (5 V/div, 5 ms/div).
2. Observez et décrivez la tension $u_{RL}$ : combien de « bosses » par période du secteur ?
3. Mesurez la valeur moyenne de $u_{RL}$ avec MM1 en V⎓ et la valeur maximale à l'oscilloscope. Comparez avec $U_{smax}$ − 0,7 V (simple) ou − 1,4 V (pont).
4. Cliquez « ↻ Montage suivant » pour étudier l'autre redresseur.

### ❓ Questions

1. Valeur maximale de la tension sur la charge (en V)
2. Valeur moyenne de la tension sur la charge, mesurée en V⎓ (en V)
3. Fréquence de la tension redressée (en Hz)
4. Dans le montage observé, combien de diodes conduisent en même temps ?  
    - ☐ Une seule (dans les deux cas)  
    - ☐ Une seule  
    - ☐ Deux (une sur chaque branche du pont)  
    - ☐ Quatre
5. Pour le même transformateur, quel montage donne la valeur moyenne la plus grande ?  
    - ☐ Simple alternance  
    - ☐ Double alternance (pont)  
    - ☐ Identique  
    - ☐ Impossible à dire

### 📥 Fichiers à ouvrir dans ElectroLab

- [`redress-v1.json`](tp/redress-v1.json) — Montage suivant n° 1

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Redressement simple et double alternance*.

## Filtrage par condensateur : choix de C

*Bac Pro CIEL (première) · durée indicative : 1 h 15*

Un pont redresseur alimente une charge de 100 Ω. Un condensateur de filtrage de seulement 100 µF laisse une ondulation inacceptable. Mesurez l'ondulation, calculez la capacité nécessaire pour qu'elle reste inférieure à 1 V et corrigez le montage.

### 🎯 Objectifs

- Mesurer l'ondulation crête à crête à l'oscilloscope (couplage AC)
- Utiliser ΔV ≈ I / (2·f·C) pour le redressement double alternance
- Choisir la capacité et la tension de service d'un électrolytique
- Vérifier le résultat

### 🛠️ Marche à suivre

1. Câblez CH1 de l'oscilloscope sur la charge RL et passez la voie en couplage <b>AC</b> avec 1 V/div pour voir l'ondulation.
2. Mesurez la tension moyenne (MM1 en V⎓) et l'ondulation ΔV pp. Calculez le courant dans la charge I = U/R.
3. Calculez la capacité C minimale pour ΔV ≤ 1 V : C = I / (2·f·ΔV). Choisissez la valeur normalisée supérieure.
4. Remplacez C1 dans l'inspecteur (attention à la tension de service ≥ 1,5 × $U_{max}$). Vérifiez à l'oscilloscope.

### ❓ Questions

1. Tension moyenne sur la charge avec C = 100 µF (en V)
2. Courant dans la charge I ≈ $U_{moy}$/R (en mA), pour $U_{moy}$ ≈ 14 V
3. Capacité minimale pour ΔV ≤ 1 V : C = I/(2·f·ΔV) (en µF), I = 0,14 A, f = 50 Hz
4. Valeur E12 à choisir (en µF)
5. La tension de service du condensateur doit être…  
    - ☐ Inférieure à $U_{max}$  
    - ☐ Égale à $U_{max}$  
    - ☐ Supérieure à $U_{max}$ (marge ≥ 30 %)  
    - ☐ Sans importance

### 📥 Fichiers à ouvrir dans ElectroLab

- [`filtrage.json`](tp/filtrage.json)

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Filtrage par condensateur : choix de C*.

## Régulation linéaire avec un 7805

*Bac Pro CIEL (terminale) · durée indicative : 1 h 30*

Une alimentation complète (transformateur, pont, filtrage, régulateur 7805) alimente une charge de 5 V / 330 mA. Étudiez le rôle du régulateur : tension de sortie constante, ondulation, tension de déchet (dropout) et échauffement.

### 🎯 Objectifs

- Mesurer la tension avant et après régulation
- Calculer la puissance dissipée par le régulateur P = ($U_{e}$ − $U_{s}$)·I
- Comprendre la tension de déchet minimale (≈ 2 V)
- Savoir quand un dissipateur thermique est nécessaire

### 🛠️ Marche à suivre

1. Mesurez la tension d'entrée du régulateur (aux bornes de C1) à l'oscilloscope et au multimètre, puis la tension de sortie.
2. Calculez la puissance dissipée par U1 : P = ($U_{e}$ − $U_{s}$)·$I_{s}$. Quelle température atteint le boîtier sans dissipateur ? Observez le comportement dans l'inspecteur de U1 (protection thermique).
3. Si nécessaire, ajoutez un dissipateur thermique (case dans l'inspecteur) ou changez de transformateur.
4. Variante : avec le transformateur 6 V, mesurez l'ondulation en sortie. Pourquoi la sortie n'est-elle plus régulée ?

### ❓ Questions

1. Tension moyenne en entrée du régulateur $U_{e}$ (en V)
2. Tension de sortie $U_{s}$ (en V)
3. Courant de charge $I_{s}$ (en mA)
4. Puissance dissipée par le régulateur (en W)
5. Quelle est la condition pour que le 7805 régule correctement ?  
    - ☐ $U_{e}$ doit toujours rester au-dessus de ≈ 7 V (5 V + tension de déchet)  
    - ☐ $U_{e}$ doit être égale à 5 V  
    - ☐ Il faut une charge nulle  
    - ☐ Il faut une fréquence supérieure à 1 kHz

### 📥 Fichiers à ouvrir dans ElectroLab

- [`regul-v1.json`](tp/regul-v1.json) — Autre transformateur n° 1

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Régulation linéaire avec un 7805*.
