# 🔭 Prise en main de l'oscilloscope

> **Matériel visé** : oscilloscope numérique 2 voies de 30 MHz (type Owon SDS5032E-V). Le nom exact des menus peut varier d'un modèle à l'autre ; les touches principales (Autoset, Run/Stop, Trigger, Measure, Cursor) existent partout.

> [!TIP] 📘 Fiches détaillées de ton oscilloscope
> Pour voir **chaque bouton**, **chaque réglage** et **chaque menu**, avec captures d'écran : [🔭 Fiche OWON SDS5032E(V)](../../ressources/oscilloscopes/owon-sds5032e.md) · [🔭 Fiche RIGOL DS1104Z](../../ressources/oscilloscopes/rigol-ds1104z.md). Pour t'entraîner : [🧪 TP « Passeport oscilloscope »](../../ressources/oscilloscopes/tp-passeport-oscilloscope.md) (missions 1 à 8).

## 🤔 À ton avis ?

Le multimètre te donne **une** valeur. Mais comment savoir si une tension **clignote**, à quelle **vitesse**, et si elle est **propre** ?

??? question "Réponse"
    Le multimètre affiche une moyenne : il ne montre pas **l'évolution dans le temps**. L'oscilloscope trace la tension **en fonction du temps** : on voit la forme du signal, sa période, son amplitude.

## 1. Les trois réglages à connaître

| Réglage | Il règle... | Unité |
|---|---|---|
| **VOLT/DIV** | l'échelle **verticale** (tension) | V par carreau |
| **SEC/DIV** | l'échelle **horizontale** (temps) | s, ms ou µs par carreau |
| **Trigger** (déclenchement) | le point où le signal « se fige » à l'écran | niveau en V |

> [!TIP] 💡 En clair
> L'écran est un **quadrillage**. On compte les carreaux, puis on **multiplie** par le réglage.
> - **Amplitude crête à crête** : $U_{pp} = \text{nombre de carreaux} \times \text{VOLT/DIV}$.
> - **Période** : $T = \text{nombre de carreaux} \times \text{SEC/DIV}$, puis $f = \dfrac{1}{T}$.

### Vérifie

1. Un signal occupe **4 carreaux** en hauteur avec 2 V/DIV. Quelle est son amplitude crête à crête ?
2. Une période occupe **5 carreaux** avec 2 ms/DIV. Quelle est la fréquence ?
3. Pourquoi règle-t-on le niveau de déclenchement ?

??? success "Réponses"

    1. $U_{pp} = 4 \times 2 = 8\,\mathrm{V}$.
    2. $T = 5 \times 2\,\mathrm{ms} = 10\,\mathrm{ms}$ ; $f = \dfrac{1}{0{,}010} = 100\,\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{\mathrm{Hz}}}}}}}}}}}}$.
    3. Pour que l'image reste **stable** : sans déclenchement correct, le signal « défile » et on ne peut rien lire.

## 2. La sonde : ×1 ou ×10, et la compensation

La sonde est un **fil spécial**. Sur ×10, elle divise le signal par 10 : l'oscilloscope doit être réglé sur « ×10 » pour afficher la bonne valeur.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Sonde sur ×10 mais voie réglée sur ×1 : toutes les tensions affichées sont **10 fois trop petites**.
> - Pince de masse (crocodile) branchée **sur un point qui n'est pas la masse** du circuit : elle est reliée à la terre, c'est un **court-circuit**.

**Compensation** : branche la sonde sur la borne « signal de test » (carré de 1 kHz) de la façade. Le carré doit être **bien droit** : s'il est arrondi ou s'il a des pointes, tourne la vis de compensation de la sonde avec un petit tournevis.

## 3. Le couplage : DC, AC ou GND

- **DC** : on voit **tout** (la composante continue + les variations).
- **AC** : on **supprime** la partie continue : pratique pour voir une petite ondulation sur une grande tension.
- **GND** : on voit le **zéro** (référence).

## 4. TP : mesurer des signaux

### Manipulation 1 : le signal de test
1. Sonde sur ×10, voie CH1. Branche-la au signal de test de la façade.
2. Appuie sur **Autoset**. Compense la sonde.
3. Relève la fréquence et l'amplitude : fréquence = \_\_\_\_\_\_ Hz ; $U_{pp}$ = \_\_\_\_\_\_ V.

??? success "Valeurs attendues"
    Environ **1 kHz** et environ **3 V** crête à crête (selon le modèle ; voir la notice de l'appareil).

### Manipulation 2 : une LED qui clignote (Arduino)
Charge le programme **Blink** modifié avec `delay(500)` et place la sonde sur la broche de la LED (masse sur GND).

- Quelle est la période ? \_\_\_\_\_\_ La fréquence ? \_\_\_\_\_\_ Le niveau haut ? \_\_\_\_\_\_ V

??? success "Valeurs attendues"
    Période = 1 s (500 ms allumée + 500 ms éteinte) ; fréquence = 1 Hz ; niveau haut ≈ 5 V. Utilise 200 ms/DIV ou 500 ms/DIV.

### Manipulation 3 : un signal PWM
Programme `analogWrite(9, 128)` et observe la broche 9.

- Fréquence ≈ \_\_\_\_\_\_ Hz ; rapport cyclique ≈ \_\_\_\_\_\_ %.

??? success "Valeurs attendues"
    Environ **490 Hz** (broches 3, 9, 10, 11 de l'Arduino Uno) ; rapport cyclique $\dfrac{128}{255} \approx 50\,\%$. Avec `analogWrite(9, 64)`, le rapport cyclique tombe à environ 25 %.

### Manipulation 4 : mesures automatiques et curseurs
Utilise **Measure** pour afficher la fréquence, l'amplitude et le rapport cyclique, puis les **curseurs** pour mesurer à la main. Compare les deux méthodes.

> [!SUCCESS] 🧠 À retenir
> - $U = \text{carreaux} \times \text{VOLT/DIV}$ ; $T = \text{carreaux} \times \text{SEC/DIV}$ ; $f = \dfrac{1}{T}$.
> - Toujours : sonde ×10 déclarée, masse sur la masse du circuit, déclenchement réglé.

## 5. Pour aller plus loin : l'oscilloscope à 4 voies avec analyseur logique

Certains oscilloscopes ont **4 voies analogiques** et des **entrées logiques** (analyseur logique). On peut alors voir **plusieurs signaux numériques en même temps** et **décoder** un bus :

- **UART** (liaison série) : lire les lettres envoyées par l'Arduino (comme en Seconde S13) ;
- **I2C** (écran LCD, capteurs) : voir l'adresse (par exemple `0x27`) et les données.

??? question "Pourquoi décoder un bus plutôt que de lire les carrés à l'œil ?"
    Parce qu'un octet fait **8 bits** de 104 µs (à 9600 bauds) : les compter à la main est long et source d'erreurs. Le décodage affiche directement la **lettre** ou la **valeur**.
