# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans ElectroLab, clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## Filtre RC passe-bas : gain et fréquence de coupure

*Bac Pro CIEL (terminale) · durée indicative : 1 h 30*

Un signal sinusoïdal de 1 V crête traverse un filtre RC (R = 1,6 kΩ, C = 100 nF). Relevez le gain G = $V_{s}$/$V_{e}$ pour plusieurs fréquences et déterminez la fréquence de coupure à −3 dB.

### 🎯 Objectifs

- Mesurer l'amplitude d'entrée et de sortie à l'oscilloscope
- Tracer (ou noter) le gain en fonction de la fréquence
- Trouver $f_{c}$ (gain = 0,707) et la comparer à 1/(2πRC)

### 🛠️ Marche à suivre

1. Câblez CH1 sur l'entrée (sortie GBF), CH2 sur la sortie (aux bornes de C1), GND à la masse.
2. Pour f = 100 Hz, 500 Hz, 1 kHz, 2 kHz, 5 kHz, 10 kHz : réglez le GBF (double-clic), relevez $V_{e}$ et $V_{s}$ (crête à crête) et calculez G = $V_{s}$/$V_{e}$.
3. Trouvez par essais la fréquence où G = 0,707 : c'est $f_{c}$.
4. Observez le déphasage entre les deux voies à $f_{c}$ (≈ 45°, sortie en retard).

### ❓ Questions

1. Fréquence de coupure théorique 1/(2πRC) (en Hz)
2. Gain mesuré à f = 100 Hz (en valeur, sans unité)
3. Gain à f = 10 kHz (sans unité)
4. Ce filtre laisse passer…  
    - ☐ Les basses fréquences (passe-bas)  
    - ☐ Les hautes fréquences (passe-haut)  
    - ☐ Une bande étroite (passe-bande)  
    - ☐ Toutes les fréquences
5. Au-delà de $f_{c}$, chaque fois que la fréquence est multipliée par 10, le gain est divisé par environ…  
    - ☐ 2  
    - ☐ 10  
    - ☐ 100  
    - ☐ 1,4

### 📥 Fichiers à ouvrir dans ElectroLab

- [`filtre.json`](tp/filtre.json)

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Filtre RC passe-bas : gain et fréquence de coupure*.
