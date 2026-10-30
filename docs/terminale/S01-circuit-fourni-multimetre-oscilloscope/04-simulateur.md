# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans ElectroLab, clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## Signaux périodiques : GBF, oscilloscope et multimètre

*Bac Pro CIEL (première) · durée indicative : 1 h 15*

Un générateur délivre un signal <b>inconnu</b> (réglages masqués). À l'aide de l'oscilloscope et du multimètre, caractérisez-le complètement : forme, période, fréquence, valeurs crête, moyenne et efficace.

### 🎯 Objectifs

- Régler correctement un oscilloscope (sensibilités, base de temps, déclenchement)
- Mesurer T, f, V<sub>max</sub>, V<sub>min</sub>, V<sub>pp</sub>
- Distinguer valeur moyenne (V⎓) et valeur efficace alternative (V∿)

### 🛠️ Marche à suivre

1. Câblez l'oscilloscope : CH1 aux bornes de R1 (sortie GBF), GND à la masse. Utilisez « Auto » pour obtenir une image stable puis affinez les réglages.
2. Relevez la forme du signal, sa période T et sa fréquence f = 1/T.
3. Relevez V<sub>max</sub>, V<sub>min</sub> et V<sub>pp</sub>. Déduisez l'amplitude et la valeur moyenne (composante continue).
4. Câblez MM1 (V⎓) puis MM2 (V∿) aux bornes de R1 et comparez avec l'oscilloscope.
5. Cliquez « ↻ Autre signal » pour recommencer avec un autre signal.

### ❓ Questions

1. Forme du signal  
    - ☐ Sinusoïdale  
    - ☐ Carrée  
    - ☐ Triangulaire
2. Période T (en ms)
3. Fréquence f (en Hz)
4. Tension maximale V<sub>max</sub> (en V)
5. Tension crête à crête V<sub>pp</sub> (en V)
6. Valeur moyenne du signal (en V) — lue en V⎓
7. Valeur efficace de la composante alternative, lue en V∿ (en V)

### 📥 Fichiers à ouvrir dans ElectroLab

- [`signaux-v1.json`](tp/signaux-v1.json) — Autre signal n° 1
- [`signaux-v2.json`](tp/signaux-v2.json) — Autre signal n° 2

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Signaux périodiques : GBF, oscilloscope et multimètre*.
