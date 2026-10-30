# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans ElectroLab, clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## Diviseur de tension et influence du voltmètre

*Bac Pro CIEL (première) · durée indicative : 1 h*

Un diviseur 1 MΩ / 1 MΩ alimenté en 10 V devrait délivrer 5 V. Mais le voltmètre n'est pas parfait : son impédance d'entrée (10 MΩ) perturbe la mesure. Étudiez aussi l'effet d'une charge et d'un potentiomètre.

### 🎯 Objectifs

- Calculer la tension de sortie d'un diviseur $U_{s}$ = E·R2/(R1+R2)
- Mettre en évidence l'erreur de méthode due à la résistance interne du voltmètre
- Observer l'effet d'une charge sur la sortie du diviseur

### 🛠️ Marche à suivre

1. Câblez MM1 (V⎓) entre le point milieu S (R1/R2) et la masse. Relevez $U_{s}$. Comparez à la valeur théorique 5 V : quel écart observez-vous ?
2. Calculez la résistance équivalente de R2 en parallèle avec l'entrée du voltmètre (10 MΩ) et expliquez l'écart.
3. Remplacez le diviseur par R1 = R2 = 10 kΩ (modifiez les valeurs) : l'erreur est-elle toujours visible ? Pourquoi ?
4. Ajoutez une charge $R_{L}$ = 10 kΩ entre S et la masse (c'est R3 déjà placée en bas, à relier) et mesurez $U_{s}$.

### ❓ Questions

1. Tension de sortie théorique du diviseur à vide, valeurs nominales (en V)
2. Tension relevée au voltmètre sur le diviseur 1 MΩ / 1 MΩ (en V)
3. Résistance équivalente de R2 ∥ 10 MΩ (en kΩ)
4. Avec R1 = R2 = 10 kΩ, la valeur lue est…  
    - ☐ Très différente de 5 V  
    - ☐ Quasiment 5 V (erreur &lt; 0,1 %)  
    - ☐ Égale à 10 V

### 📥 Fichiers à ouvrir dans ElectroLab

- [`diviseur.json`](tp/diviseur.json)

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Diviseur de tension et influence du voltmètre*.
