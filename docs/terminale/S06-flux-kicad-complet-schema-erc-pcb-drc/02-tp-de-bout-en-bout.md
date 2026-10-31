# 🎯 TP de bout en bout : du cahier des charges à la carte testée

> **Durée** : 4 h · **Documents autorisés** : cours S06, datasheets · **Logiciel** : KiCad · **Matériel** : multimètre, oscilloscope

## 🤔 À ton avis ?

Tu reçois un cahier des charges. Il faut livrer **une carte qui fonctionne, avec ses fichiers de fabrication et la preuve qu'elle est conforme**. Dans quel ordre fais-tu les choses ?

??? question "Réponse"
    **Comprendre** (analyse, calculs) → **dessiner** (schéma, ERC) → **concevoir** (empreintes, PCB, DRC) → **sortir les fichiers** (Gerber, perçage, BOM) → **tester** (mesures, PV). Chaque étape est **vérifiée** avant la suivante.

## Cahier des charges

Réaliser un **clignoteur à LED** :

- alimentation d'entrée : **12 V** ; carte alimentée en **5 V** (régulateur 7805) ;
- LED qui clignote à **1 Hz ± 10 %** (NE555 en astable) ;
- courant dans la LED : **20 mA** ;
- carte de **60 mm × 40 mm** maximum, simple face, composants traversants.

## Étape 1 : analyse et calculs (30 min)

1. Dessine le **schéma bloc** (alimentation, oscillateur, indicateur).
2. Calcule $R_{3}$ (LED), puis $f$ et le rapport cyclique pour $R_{a} = 10\,\mathrm{k\Omega}$, $R_{b} = 68\,\mathrm{k\Omega}$, $C = 10\,\mathrm{\mu F}$.

??? success "Valeurs attendues"

    - $R_{3} = \dfrac{5 - 2}{0{,}020} = 150\,\Omega$.
    - $f = \dfrac{1{,}44}{(10\,000 + 2 \times 68\,000) \times 10 \times 10^{-6}} \approx 0{,}99\,\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{Hz}}}}}}}}}}}}$ : **conforme** à 1 Hz ± 10 %.
    - $DC = \dfrac{78}{146} \approx 53\,\%$.
    - Condensateurs du 7805 : 100 nF à l'entrée, 10 µF à la sortie.

## Étape 2 : schéma et ERC (45 min)

Saisis le schéma dans KiCad : connecteur d'entrée, 7805 et ses condensateurs, NE555 (avec 100 nF sur la broche 5), $R_{a}$, $R_{b}$, $C$, $R_{3}$, LED. Ajoute les **PWR_FLAG**, annote, renseigne les valeurs. Lance l'**ERC**.

✅ Critère : **0 erreur**.

## Étape 3 : empreintes (20 min)

Associe une empreinte à **chaque** composant (vérifie les dimensions avec la datasheet). Mets à jour le PCB.

✅ Critère : **aucun composant** sans empreinte.

## Étape 4 : placement et routage (60 min)

1. Contour de **60 × 40 mm** (Edge.Cuts).
2. Règles : clearance **0,25 mm**, pistes de signal **0,25 mm**, pistes d'alimentation **0,5 mm**, via 0,8/0,4 mm.
3. Place d'abord le connecteur (au bord), le 7805 et ses condensateurs, puis le NE555 et les passifs.
4. Route l'**alimentation en premier**, puis les signaux.

## Étape 5 : DRC et fichiers de fabrication (30 min)

1. Lance le **DRC** : 0 erreur.
2. Exporte les **Gerber** (cuivre, masque, sérigraphie, contour) et le fichier de **perçage**.
3. Génère la **BOM**.
4. **Ouvre les Gerber dans un visualiseur** et vérifie que tout est présent.

??? success "Fichiers attendus"
    Une couche cuivre (F.Cu ou B.Cu selon la face), masque de soudure, sérigraphie, contour (Edge.Cuts), le fichier de perçage (.drl) et la BOM (.csv).

## Étape 6 : mesures et procès-verbal (40 min)

Une fois la carte montée et alimentée en 12 V :

1. Mesure $U_{out}$ du 7805 : **4,75 V à 5,25 V** attendu.
2. Mesure la **fréquence** à l'oscilloscope : **0,9 Hz à 1,1 Hz** attendu.
3. Mesure le courant dans la LED : **≤ 30 mA** (cible 20 mA).
4. Rédige le **PV** : valeur attendue, valeur mesurée, verdict pour chaque test, conclusion.

## Grille d'évaluation (20 points)

| Critère | Points |
|---|---|
| Calculs justes et justifiés | 4 |
| Schéma propre, ERC à 0 erreur | 4 |
| PCB conforme au cahier des charges, DRC à 0 erreur | 4 |
| Fichiers de fabrication complets et vérifiés | 3 |
| Mesures et PV (verdicts justifiés) | 5 |

> [!SUCCESS] 🧠 À retenir
> - Chaque étape se **vérifie** (ERC, DRC, visualiseur) avant de passer à la suivante.
> - Un PV compare toujours **attendu** et **mesuré**, puis conclut.
