# 🧪 TP « Passeport oscilloscope » : 13 missions

> **Durée** : 2 h à 3 h (en 2 séances) · **Matériel** : un oscilloscope (OWON SDS5032E ou RIGOL DS1054Z), une sonde ×1/×10, un générateur de fonctions (GBF), un circuit RC (10 kΩ et 100 nF), une alimentation, une clé USB.
> **Fiches à avoir sous la main** : [OWON](owon-sds5032e.md) ou [RIGOL](rigol-ds1104z.md).
>
> Fais ce TP **dans l'ordre**. Chaque mission a un **résultat à obtenir** : coche la case quand tu l'as **réussi seul(e)**.

## 🔬 Avant le TP réel : OscilloLab

Entraîne-toi d'abord sur le simulateur de **tes deux oscilloscopes** : [▶️ OscilloLab](https://yahnlp.github.io/OscilloLab/) ([mode d'emploi](../oscillolab.md)). Commence par **📖 Les bases de l'oscilloscope**, puis :

| Missions | TP OscilloLab |
|---|---|
| 1 · 2 · 3 · 4 | **1** Prise en main · **2** Compenser la sonde · **3** Piège ×1 / ×10 · **4** Lire sur la grille · **16** Pince de masse oubliée |
| 5 · 6 | **5** Couplage DC / AC / GND · **6** Le déclenchement |
| 7 · 8 · 9 | **7** Mesures automatiques · **8** Curseurs · **9** NE555 · **10** Pont de diodes (ondulation) · **15** Réduire le bruit |
| 10 · 11 | **12** Mesurer un déphasage · **13** Mode XY · **14** Capture unique (rebonds) · **11** Charge d'un condensateur |

## 🖥️ Avant le TP réel : ElectroLab

Dans [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾** : **Lire un signal à l'oscilloscope** (6 signaux), **Signal rectangulaire : rapport cyclique** (5 signaux), **Deux voies : gain et déphasage d'un filtre RC** (4 fréquences), **Couplage AC / DC** (3 signaux).

---

## 🟢 Niveau 1 : démarrer

### Mission 1 : remettre à zéro et régler la sonde

1. **Allume** l'oscilloscope.
2. **Rétablis les réglages d'usine**.
3. Mets l'interrupteur de la sonde sur **10X** et règle le **menu de la voie** sur **×10**.

**À obtenir** : la sonde est réglée **aux deux endroits** sur le même coefficient.

- [ ] Réussi

### Mission 2 : compenser la sonde

1. Branche la sonde sur la **sortie de compensation**.
2. Appuie sur **Autoset** (OWON) ou **AUTO** (RIGOL).
3. **Déforme volontairement** le carré (tourne le trimmer), puis **corrige**.

**À obtenir** : un carré **bien droit** de **1 kHz**.

- [ ] Réussi

??? tip "💡 Aides"
    - Un carré avec un **coin arrondi** : sonde **sous-compensée**. Un carré avec une **bosse** : **sur-compensée**.
    - Si tu ne vois rien, vérifie que la voie est **allumée** et que le couplage est **DC**.
    - OWON : le signal doit mesurer environ **5 V crête-à-crête**.

### Mission 3 : lire l'écran

Avec le carré de compensation :

1. Lis **V/div** et **s/div**.
2. Compte les **carreaux** de hauteur et d'une période.
3. Calcule $U_{pp}$, $T$ et $f$.

**À obtenir** : un tableau « lu / calculé / affiché par l'appareil ».

| Grandeur | Carreaux | Réglage | Calcul | Valeur de l'appareil |
|---|---|---|---|---|
| $U_{pp}$ | | | | |
| $T$ | | | | |
| $f$ | | | | |

- [ ] Réussi

??? tip "💡 Aides"
    - $U_{pp} = \text{carreaux} \times \text{V/div}$ ; $T = \text{carreaux} \times \text{s/div}$ ; $f = \dfrac{1}{T}$.
    - Ton calcul doit s'écarter de la valeur de l'appareil de **moins de 5 à 10 %** ; sinon, recompte les carreaux.

---

## 🟡 Niveau 2 : régler à la main

### Mission 4 : un sinus de 1 kHz sans Autoset

1. Règle le **GBF** : **sinus**, **1 kHz**, **2 V crête-à-crête**.
2. Branche-le sur **CH1**.
3. **Sans Autoset**, règle la sensibilité et la base de temps pour afficher **3 à 5 périodes** sur **au moins 4 carreaux de hauteur**.

**À obtenir** : un signal **stable, centré, lisible**.

- [ ] Réussi

??? tip "💡 Aides"
    - Sensibilité conseillée : **0,5 V/div** pour 2 V crête-à-crête (4 carreaux).
    - Base de temps conseillée : **0,5 ms/div** (1 période = 2 carreaux, 10 carreaux = 5 périodes).
    - Si l'image défile : **déclenchement** (source, niveau, pente) ; pense au bouton **50 %** (OWON).

### Mission 5 : le couplage DC et AC

1. Règle le GBF : **sinus 1 kHz, 1 V crête-à-crête, avec un décalage (offset) de +2 V**.
2. Observe en **DC**, puis en **AC**, puis en **GND**.

**À obtenir** : trois captures, et une explication en une phrase de chaque.

| Couplage | Ce que je vois | Pourquoi |
|---|---|---|
| **DC** | | |
| **AC** | | |
| **GND** | | |

- [ ] Réussi

??? tip "💡 Aides"
    - En **DC**, le tracé est **décalé** de 2 V (soit plusieurs carreaux selon la sensibilité).
    - En **AC**, il est **centré** : la composante continue est supprimée.
    - En **GND**, une **ligne plate** : c'est le **zéro** de la voie.

### Mission 6 : le déclenchement

1. Reprends le sinus de la mission 4.
2. Mets le niveau de déclenchement **au-dessus de l'amplitude du signal**. Que se passe-t-il en mode **Auto** ? En mode **Normal** ?
3. Reviens à un niveau correct. Passe de la pente **montante** à la pente **descendante** : que change le tracé ?

**À obtenir** : tu sais **expliquer** quand l'image défile, quand elle est figée, et pourquoi.

- [ ] Réussi

??? tip "💡 Aides"
    - **Auto** : l'écran défile (pas de déclenchement mais il affiche quand même).
    - **Normal** : l'écran **reste figé** sur l'ancien tracé.
    - Changer la **pente** décale le **début** du tracé d'un demi-période environ.

---

## 🟠 Niveau 3 : mesurer sérieusement

### Mission 7 : trois façons de mesurer

Pour le sinus de 1 kHz et 2 V crête-à-crête, mesure $U_{pp}$ et la **fréquence** de **trois manières** :

1. par **lecture des carreaux** ;
2. par les **mesures automatiques** ;
3. par les **curseurs**.

**À obtenir** : un tableau comparatif et le **commentaire** sur l'écart.

| Méthode | $U_{pp}$ | $f$ |
|---|---|---|
| Carreaux | | |
| Mesure automatique | | |
| Curseurs | | |

- [ ] Réussi

??? tip "💡 Aides"
    - La **mesure automatique** est la plus **fiable** (elle utilise tous les points) ; la lecture des carreaux la **moins précise**.
    - Les **trois valeurs** doivent s'accorder à **quelques pour cent**. Un écart de plus de **10 %** indique une erreur de lecture ou de **coefficient de sonde**.
    - Sur l'**OWON**, les curseurs se déplacent avec les boutons **VERTICAL POSITION** de CH1 et CH2.

### Mission 8 : un signal rectangulaire

1. GBF : **carré**, **1 kHz**, **0 à 5 V**, **rapport cyclique 25 %**.
2. Mesure le **temps haut**, la **période**, le **rapport cyclique** et la **valeur moyenne**.

**À obtenir** : $t_H = 250\,\mathrm{\mu s}$, $T = 1\,\mathrm{ms}$, rapport cyclique 25 %, valeur moyenne $\approx 1{,}25\,\mathrm{V}$.

- [ ] Réussi

??? tip "💡 Aides"
    - Rapport cyclique $= \dfrac{t_H}{T}$ ; valeur moyenne $= \text{rapport cyclique} \times U_{max}$.
    - Utilise les mesures automatiques **+Width**/**+Duty** (OWON) ou la mesure de **largeur** et de **rapport cyclique** (RIGOL), et **Vavg** pour la moyenne.

### Mission 9 : l'ondulation d'une alimentation

1. Alimente une charge (LED + résistance, ou une carte) avec une alimentation de labo **5 V**.
2. Mets la voie en couplage **AC**, sensibilité **20 mV/div**.
3. Mesure l'**ondulation** (crête-à-crête) et sa **fréquence** éventuelle.

**À obtenir** : une valeur d'ondulation en **mV crête-à-crête**.

- [ ] Réussi

??? tip "💡 Aides"
    - Une alimentation de labo propre donne **quelques millivolts** à **quelques dizaines de millivolts** de bruit.
    - Une alimentation **à découpage** donne des **pointes brèves** ; une alimentation **linéaire redressée** donne une **dent de scie à 100 Hz**.
    - Sans **couplage AC**, tu ne vois que la valeur moyenne.

---

## 🔴 Niveau 4 : analyser et capturer

### Mission 10 : deux voies, retard et déphasage

1. Monte le **filtre RC** ($R = 10\,\mathrm{kΩ}$, $C = 100\,\mathrm{nF}$) : GBF → CH1 (entrée), sortie du filtre → CH2.
2. Règle le GBF en **sinus 160 Hz**, 2 V crête-à-crête.
3. Mesure le **gain** $\dfrac{U_s}{U_e}$ et le **retard** entre les deux voies, puis le **déphasage** : $\varphi = 360° \times \dfrac{\Delta t}{T}$.

**À obtenir** : gain proche de **0,7** (−3 dB) et déphasage proche de **−45°** (la sortie est en retard).

- [ ] Réussi

??? tip "💡 Aides"
    - Fréquence de coupure $f_c = \dfrac{1}{2\pi R C} \approx 159\,\mathrm{Hz}$ : tu es **à $f_c$**.
    - Utilise les **curseurs de temps** ou la mesure de **retard** entre voies (*Delay* sur OWON).
    - Les **deux pinces de masse** sur la **même** masse.

### Mission 11 : capturer un événement unique

1. Monte un circuit RC avec un **bouton** et une alimentation (charge d'un condensateur de 100 µF à travers 10 kΩ, par exemple).
2. Règle le déclenchement en **front montant**, mode **Single**.
3. **Arme** l'oscilloscope, **appuie** sur le bouton, et **capture** la charge.

**À obtenir** : une courbe de charge exponentielle, avec **$\tau = RC$ lu à l'écran** (63 % de la valeur finale).

- [ ] Réussi

??? tip "💡 Aides"
    - $\tau = RC = 10\,\mathrm{kΩ} \times 100\,\mathrm{\mu F} = 1\,\mathrm{s}$ ; la charge dure environ **5 s**.
    - Base de temps conseillée : **500 ms/div**.
    - Niveau de déclenchement : **juste au-dessus du zéro**.
    - Si rien n'est capturé, vérifie que l'appareil est bien en **attente** (Ready / WAIT) avant d'appuyer.

### Mission 12 : sauvegarder une image

1. Insère une **clé USB**.
2. Enregistre l'**écran** d'une des missions précédentes.
3. Ouvre l'image sur l'ordinateur et **annote-la** (grandeurs lues, réglages).

**À obtenir** : un fichier image **nommé** (par exemple `mission8_carre25.bmp`) intégré à ton compte rendu.

??? tip "💡 Aides"
    - **OWON** : touche **Save** → *Type* **Image** → nom du fichier (**H4**) → le fichier est enregistré en **BMP**.
    - **RIGOL** : clé USB en **FAT32**, puis touche **Quick Print** (à côté de **Help**). Pour un **fond blanc** (idéal pour imprimer) : Utility → Print Set → palette **Gray Scale**, puis **Invert : ON**.

- [ ] Réussi

### Mission 13 : mini compte rendu de mesure

Rédige une **fiche** d'une page pour **un signal au choix** : schéma de montage, réglages de l'oscilloscope (V/div, s/div, couplage, déclenchement), capture annotée, **résultats avec unités**, et **incertitude estimée** (résolution de lecture et précision de l'instrument).

**À obtenir** : un document qu'un **autre élève peut reproduire**.

- [ ] Réussi

---

## 🏁 Mon bilan « Passeport oscilloscope »

| Compétence | Mission | Acquis |
|---|---|---|
| Régler et compenser la sonde | 1, 2 | ☐ |
| Lire l'écran | 3 | ☐ |
| Régler sensibilité, base de temps, centrage | 4 | ☐ |
| Choisir le couplage | 5 | ☐ |
| Maîtriser le déclenchement | 6 | ☐ |
| Mesurer (carreaux, automatique, curseurs) | 7, 8 | ☐ |
| Mesurer une ondulation | 9 | ☐ |
| Utiliser deux voies | 10 | ☐ |
| Capturer et sauvegarder | 11, 12 | ☐ |
| Rédiger un compte rendu de mesure | 13 | ☐ |

> [!TIP] 💡 Tu as tout validé ?
> Tu es **autonome** sur l'oscilloscope : tu peux l'utiliser pour **dépanner** une carte, **valider** un montage ou **rédiger un PV de mesure** (semaine 13 du parcours « L'essentiel en 1 an »).
