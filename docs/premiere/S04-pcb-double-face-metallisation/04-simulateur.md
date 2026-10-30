# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans ElectroLab, clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## NE555 en multivibrateur astable (4 fréquences)

*Bac Pro CIEL (première / terminale) · durée indicative : 1 h 30*

Le NE555 est câblé en <b>astable</b> : la sortie OUT oscille entre 0 et Vcc. La fréquence dépend de R1, R2 et C : f ≈ 1,44 / ((R1 + 2·R2)·C). Calculez R2 pour obtenir la fréquence demandée, puis vérifiez à l'oscilloscope.

### 🎯 Objectifs

- Identifier les broches du NE555 (TRIG, THR, DIS, OUT, RESET, CTRL)
- Dimensionner R2 à partir d'une fréquence cible
- Mesurer période, fréquence et rapport cyclique à l'oscilloscope
- Comprendre pourquoi le rapport cyclique est toujours supérieur à 50 %

### 🛠️ Marche à suivre

1. Lisez dans l'énoncé la fréquence cible (variante affichée dans la question 1) et relevez R1 et C sur le schéma.
2. Calculez R2 = (1,44 / (f·C) − R1) / 2, puis réglez R2 (double-clic sur le composant).
3. Reliez la voie CH1 de l'oscilloscope à la sortie <b>OUT</b> (GND de l'oscilloscope à la masse) et ajustez la base de temps.
4. Mesurez période, fréquence et rapport cyclique. Comparez au calcul.
5. Observez aussi la tension aux bornes de C (CH2 sur THR) : entre quelles valeurs oscille-t-elle ?

### ❓ Questions

1. c => 'Fréquence cible de cette variante : ' + T5[c.tp.variant % 4].lab + '. Valeur calculée de R2 (en Ω, tolérance large : valeur normalisée acceptée)'
2. Fréquence mesurée de la sortie (en Hz)
3. Période mesurée (en ms)
4. Rapport cyclique de la sortie (en %)
5. Entre quelles valeurs oscille la tension aux bornes du condensateur ?  
    - ☐ 0 et Vcc  
    - ☐ Vcc/3 et 2·Vcc/3  
    - ☐ 0 et Vcc/3  
    - ☐ 2·Vcc/3 et Vcc
6. Pourquoi le rapport cyclique est-il toujours > 50 % avec ce montage ?  
    - ☐ Parce que le NE555 est asymétrique  
    - ☐ Parce que C se charge par R1 + R2 mais se décharge seulement par R2  
    - ☐ Parce que R1 est toujours plus grande que R2  
    - ☐ Parce que la tension d'alimentation n'est pas stable

### 📥 Fichiers à ouvrir dans ElectroLab

- [`ne555-v1.json`](tp/ne555-v1.json) — Autre fréquence n° 1
- [`ne555-v2.json`](tp/ne555-v2.json) — Autre fréquence n° 2

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *NE555 en multivibrateur astable (4 fréquences)*.
