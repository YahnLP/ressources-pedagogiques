# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans [ElectroLab](https://yahnlp.github.io/ElectroLab/), clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## Tester les composants hors tension (ohmmètre, diode, continuité)

*Bac Pro CIEL (seconde) · durée indicative : 1 h*

Sur la paillasse : une résistance, une diode 1N4007, une LED, un transistor NPN et un fusible. Aucun n'est alimenté. Avec le multimètre seul, vérifiez l'état de chaque composant. <b>On mesure toujours hors tension !</b>

### 🎯 Objectifs

- Mesurer une résistance à l'ohmmètre et la comparer à sa valeur nominale (tolérance)
- Tester une diode dans les deux sens : tension de seuil et blocage
- Contrôler un fusible à l'aide du mode « continuité » (bip)
- Vérifier les jonctions base-émetteur et base-collecteur d'un transistor

### 🛠️ Marche à suivre

1. Mesurez R1 à l'ohmmètre. Est-elle dans sa tolérance ?
2. Mode « Test diode » : placez le « + » (V/Ω/A) sur l'anode de D1, le COM sur la cathode : relevez $V_{F}$. Inversez : que lit-on (« OL » = circuit ouvert) ?
3. Même test pour la LED D2 : la LED s'allume-t-elle faiblement ?
4. Contrôlez le fusible F1 en continuité : bip ou pas de bip ?
5. Transistor Q1 : testez les jonctions B–E et B–C (comme deux diodes) puis C–E (bloqué dans les deux sens).

### ❓ Questions

1. Valeur de R1 mesurée à l'ohmmètre (en Ω)
2. Tension de seuil de D1 au testeur de diode, sens passant (en V)
3. Tension de seuil de la LED D2 au testeur de diode (en V)
4. Le fusible F1 est…  
    - ☐ En bon état  
    - ☐ Grillé (coupé)
5. Tension $V_{BE}$ du transistor au testeur de diode (B vers E, en V)
6. Au testeur de diode, une diode saine dans le sens bloqué affiche…  
    - ☐ 0,6 V  
    - ☐ 0 V  
    - ☐ « OL » (circuit ouvert)  
    - ☐ Un bip continu

### 📥 Fichiers à ouvrir dans ElectroLab

- [`test-v1.json`](tp/test-v1.json) — Autre fusible n° 1

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Tester les composants hors tension (ohmmètre, diode, continuité)*.
