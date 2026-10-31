# 🔬 Utiliser OscilloLab

> [!NOTE] 🧪 Voir aussi : [tous les Labs](labs.md) · [🖥️ ElectroLab](electrolab.md) pour câbler et simuler des circuits.

**OscilloLab** est un simulateur des **deux oscilloscopes du laboratoire** : l'**OWON SDS5032E(V)** et le **RIGOL DS1054Z**. Il fonctionne **hors ligne** dans un navigateur. La face avant, les menus et les réactions de l'appareil sont reproduits : on apprend à **régler l'oscilloscope** sans risque pour le matériel.

▶️ **Ouvrir le simulateur : [OscilloLab — oscilloscopes OWON et RIGOL](https://yahnlp.github.io/OscilloLab/)**

📥 Pour travailler hors ligne, le fichier unique `dist/oscillolab.html` est disponible dans le [dépôt OscilloLab](https://github.com/YahnLP/OscilloLab).

## Commencer

1. Choisis **ton appareil** en haut de la page (OWON ou RIGOL) : les consignes s'adaptent.
2. Clique sur **📖 Les bases de l'oscilloscope** et lis le mini-cours (10 minutes) en manipulant l'appareil.
3. Choisis un **TP** dans la liste à droite : le banc d'essai est préparé pour toi.
4. Pour chaque étape : lis **💡 À savoir**, suis le **🛠 Pas à pas**, puis réponds aux questions.

> [!TIP] 👆 Le bouton « Montre-moi »
> Dans le pas à pas, le bouton **👆 Montre-moi** fait **clignoter la touche ou le bouton** dont on parle sur la face avant. Si tu hésites : **🆘 Un coup de pouce**.

## Manipuler

| Je veux… | Je fais… |
|---|---|
| Tourner un bouton | **molette de la souris** ou **glisser** sur le bouton |
| Appuyer sur un bouton | **un clic** (ex. appui sur POSITION : remise à zéro) |
| Brancher une sonde, régler la vis de compensation | menu **🔌 Branchements des sondes** (au-dessus de l'oscilloscope) |
| Régler le générateur de fonctions | menu **〰 Générateur de fonctions** |
| Changer de montage (pont de diodes, NE555, RC…) | menu **🧩 Montages en entrée** |
| Déplacer une fenêtre de menu | la **saisir par son titre** |
| Tirer d'autres valeurs | bouton **↻ Nouveau signal** |

> [!WARNING] ⚠️ Comme sur le vrai appareil
> Le simulateur reproduit aussi les **pièges** : sonde non compensée, interrupteur de la sonde ≠ menu *Probe* (tensions fausses d'un facteur 10), pince de masse oubliée (parasite à 50 Hz), niveau de déclenchement hors du signal…

## Quel TP pour quelle séance ?

| TP OscilloLab | Ce qu'on apprend | Mission du [Passeport](oscilloscopes/tp-passeport-oscilloscope.md) | Séances |
|---|---|---|---|
| **1** Prise en main | sonde, Autoset, lecture | 1 · 3 | Seconde S12 · Essentiel S3 |
| **2** Compenser la sonde | carré parfait | 2 | Seconde S12 · Essentiel S3 |
| **3** Le piège ×1 / ×10 | interrupteur ≠ menu | 1 | Seconde S12 · Essentiel S3 |
| **4** Lire sur la grille | V/div, s/div, Upp, T, f | 3 · 4 | Seconde S12 · Essentiel S3 |
| **5** Couplage DC, AC, GND | zéro, ondulation | 5 | Seconde S12 · Essentiel S3 |
| **6** Le déclenchement | niveau, pente, Auto / Normal | 6 | Seconde S12 · Première S05 |
| **7** Mesures automatiques | Freq, rapport cyclique, Upp | 7 · 8 | Première S05 |
| **8** Les curseurs | ΔU, ΔT, 1/ΔT | 7 | Première S05 |
| **9** Signal d'un NE555 | f et α, mesure et calcul | 8 | Première S05 · S14 (année 3) |
| **10** Pont de diodes | Umax, 100 Hz, ondulation | 9 | Essentiel S6 · Première S05 |
| **11** Charge d'un condensateur | τ = R·C | — | Première S05 |
| **12** Mesurer un déphasage | Δt, φ = 360° Δt / T | 10 | Première S05 · Terminale S01 |
| **13** Mode XY | ellipse, sin φ = Y₀ / Ymax | 10 | Première S05 · Terminale |
| **14** Capture unique : rebonds | Single, anti-rebond | 11 | Première S05 |
| **15** Réduire le bruit | sonde ×1, mode Average | 7 | Première S05 |
| **16** La pince de masse oubliée | parasite 50 Hz | 1 | Seconde S12 |
| **17** Le bruit : le reconnaître et l'atténuer | limite 20 MHz, rejet HF, moyennage, sensibilité | 7 · 9 | Première S05 · Essentiel S6 |
| **18** Décoder une liaison série UART / RS-232 *(RIGOL)* | vitesse, seuil, polarité, ASCII | — | Première S05 · Terminale |
| **19** Décoder un bus I²C *(RIGOL)* | Start, adresse, R/W, données, ACK | — | Première S05 · Terminale |
| **20** Décoder un bus SPI *(RIGOL)* | CS, SCLK, MOSI / MISO | — | Première S05 · Terminale |

> [!TIP] 🏁 La bonne méthode
> **1)** Réussis d'abord le TP virtuel (cases cochées et questions justes). **2)** Refais la manipulation sur **l'appareil réel**, avec la fiche : [OWON](oscilloscopes/owon-sds5032e.md) ou [RIGOL](oscilloscopes/rigol-ds1104z.md). **3)** Coche la mission du [Passeport oscilloscope](oscilloscopes/tp-passeport-oscilloscope.md).

> [!NOTE] 🔌 Décodeur série du RIGOL
> Les **TP 18 à 20** utilisent le décodeur de bus série du RIGOL DS1054Z (**MATH → Decode1**). C'est une **option logicielle** de l'appareil (SA-DS1000Z) : vérifie qu'elle est active sur ton oscilloscope. L'OWON n'a pas de décodeur.

## Limites
OscilloLab ne remplace pas le matériel : certains menus rarement utilisés ne sont pas simulés (déclenchements spéciaux, FFT, décodage série). Détail dans le [dépôt](https://github.com/YahnLP/OscilloLab).
