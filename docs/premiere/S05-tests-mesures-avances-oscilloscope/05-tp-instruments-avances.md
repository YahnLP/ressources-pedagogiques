# 🎛️ TP : maîtriser l'oscilloscope et le générateur de fonctions

> **Durée** : 2 h · **Matériel** : oscilloscope 2 voies (30 MHz), générateur de fonctions (GBF), résistance 10 kΩ, condensateur 100 nF, plaque d'essai

## 🤔 À ton avis ?

Un filtre laisse passer certains signaux et en bloque d'autres. Comment le **vérifier avec des mesures** plutôt qu'avec une formule ?

??? question "Réponse"
    On envoie un signal de **fréquence connue** (GBF) à l'entrée et on **mesure l'amplitude à la sortie** (oscilloscope). En répétant à plusieurs fréquences, on **trace la réponse** du filtre.

## 1. Les fonctions à maîtriser sur l'oscilloscope

| Fonction | À quoi ça sert |
|---|---|
| **Déclenchement** (trigger) : front montant ou descendant, niveau | figer l'image |
| Modes **Auto / Normal / Single** | observer un signal permanent, ou capturer un événement unique |
| **Mesures automatiques** : $U_{pp}$, $U_{moy}$, $U_{eff}$, fréquence, rapport cyclique | gagner du temps et comparer à la lecture manuelle |
| **Curseurs** | mesurer une durée ou une tension avec précision |
| **Deux voies** | comparer l'entrée et la sortie d'un montage |

> [!TIP] 💡 En clair
> Pour un signal sinusoïdal : $U_{eff} = \dfrac{U_{max}}{\sqrt{2}} = \dfrac{U_{pp}}{2\sqrt{2}}$. Un sinus de 2 V crête à crête a une valeur efficace d'environ **0,71 V**.

## 2. Manipulation A : mesures de base

1. GBF : sinus, 1 kHz, 2 $U_{pp}$. Branche sur la voie 1.
2. Relève **à la main** : $T$, $f$, $U_{pp}$. Compare avec les **mesures automatiques**.
3. Change le **déclenchement** : front montant puis descendant. Qu'observes-tu ?

??? success "Valeurs attendues"
    $T = 1\,\mathrm{ms}$, $f = 1\,\mathrm{\mathrm{\mathrm{\mathrm{kHz}}}}$, $U_{pp} = 2\,\mathrm{V}$, $U_{eff} \approx 0{,}71\,\mathrm{V}$. Le déclenchement montant ou descendant décale le **point de départ** du signal à l'écran (le sinus démarre en montée ou en descente).

## 3. Manipulation B : réponse d'un filtre RC

Monte un filtre : GBF → $R = 10\,\mathrm{k\Omega }$ → point de sortie ; $C = 100\,\mathrm{nF}$ entre le point de sortie et la masse. Voie 1 sur l'entrée du GBF, voie 2 sur la sortie.

**Calcul préalable** : $f_{c} = \dfrac{1}{2\pi R C} \approx 159\,\mathrm{\mathrm{\mathrm{\mathrm{Hz}}}}$.

1. Règle le GBF à une amplitude de 2 $U_{pp}$.
2. Pour chaque fréquence, relève l'amplitude **de sortie** et calcule le **rapport** $\dfrac{U_{sortie}}{U_{entrée}}$.

| Fréquence | $U_{sortie}$ mesuré | Rapport |
|---|---|---|
| 16 Hz | | |
| 159 Hz | | |
| 1 600 Hz | | |

??? success "Valeurs attendues (théoriques)"
    | Fréquence | Rapport attendu | $U_{sortie}$ pour 2 V$_{pp}$ |
    |---|---|---|
    | 16 Hz | ≈ 0,99 | ≈ 2,0 V |
    | 159 Hz | ≈ 0,71 | ≈ 1,41 V |
    | 1 600 Hz | ≈ 0,10 | ≈ 0,20 V |

    À $f_{c}$, la sortie est à 70,7 % de l'entrée. Au-dessus, le signal est de plus en plus atténué : c'est un **passe-bas**. On observe aussi un **retard** de la sortie sur l'entrée (déphasage de 45° à $f_{c}$).

## 4. Pour aller plus loin (si l'oscilloscope le permet)

- **Analyseur logique** (voies numériques) : visualiser plusieurs signaux numériques en même temps et **décoder** une liaison UART ou I2C.
- **Mesure du temps de montée** d'un signal carré avec les curseurs.

> [!SUCCESS] 🧠 À retenir
> - Mesure à la main **et** mesure automatique : on compare toujours.
> - À $f_{c}$, un filtre RC atténue à **70,7 %** ; $f_{c} = \dfrac{1}{2\pi RC}$.
> - Deux voies = on compare **entrée et sortie** d'un montage.
