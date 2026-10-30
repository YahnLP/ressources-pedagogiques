# 📈 Amplificateur opérationnel, filtre RC et portes logiques

## 🤔 À ton avis ?

Un capteur délivre **10 mV**. L'entrée de l'Arduino mesure de 0 à 5 V. Comment **agrandir** un petit signal ? Et comment **supprimer le bruit** qui s'y ajoute ?

??? question "Réponse"
    On **amplifie** avec un amplificateur opérationnel (AOP) et on **filtre** le bruit avec un filtre RC.

## 1. L'amplificateur opérationnel (AOP)

Un AOP (par exemple LM358) a **deux entrées** : **+** (non inverseuse) et **−** (inverseuse), et une sortie. Il amplifie la **différence** entre ses entrées.

### En montage « non inverseur »

Avec deux résistances $R_{f}$ (de la sortie vers l'entrée −) et $R_{g}$ (de l'entrée − vers la masse) :

$$G = 1 + \frac{R_f}{R_g}$$

> [!TIP] 💡 En clair
> Le gain ne dépend **que des deux résistances**, pas de l'AOP lui-même. Et la sortie ne peut pas dépasser la tension d'alimentation : un gain de 100 sur 100 mV donnerait 10 V en théorie, mais la sortie sera **écrêtée** à environ 5 V si l'AOP est alimenté en 5 V.

### Vérifie

1. $R_{f} = 10\,\mathrm{k\Omega}$ et $R_{g} = 1\,\mathrm{k\Omega}$. Quel est le gain ?
2. Quelle tension de sortie pour une entrée de 100 mV ?
3. Un AOP alimenté en 5 V peut-il fournir 8 V en sortie ?

??? success "Réponses"

    1. $G = 1 + \dfrac{10}{1} = 11$.
    2. $11 \times 0{,}1 = 1{,}1\,\mathrm{V}$.
    3. **Non** : la sortie reste inférieure à l'alimentation (elle est écrêtée).

## 2. Le filtre RC passe-bas

Une résistance et un condensateur laissent passer les **basses fréquences** et atténuent les **hautes**. La **fréquence de coupure** vaut :

$$f_{c} = \frac{1}{2\pi R C}$$

À $f_{c}$, le signal est réduit à environ **70 %** de sa valeur ($-3\,\mathrm{dB}$).

### Vérifie

1. $R = 10\,\mathrm{k\Omega}$ et $C = 100\,\mathrm{nF}$ : calcule $f_{c}$.
2. Un bruit à 5 kHz est-il bien filtré ? Et un signal utile à 10 Hz ?
3. On veut $f_{c} = 159\,\mathrm{\mathrm{\mathrm{Hz}}}$ avec $C = 1\,\mathrm{\mu F}$ : quelle résistance ?

??? success "Réponses"

    1. $f_{c} = \dfrac{1}{2\pi \times 10\,000 \times 100 \times 10^{-9}} \approx 159\,\mathrm{\mathrm{\mathrm{Hz}}}$.
    2. Le bruit à 5 kHz est **très atténué** (bien au-dessus de $f_{c}$) ; le signal à 10 Hz **passe** (bien en dessous de $f_{c}$).
    3. $R = \dfrac{1}{2\pi \times 159 \times 10^{-6}} \approx 1\,\mathrm{k\Omega}$.

## 3. Les portes logiques

Les circuits numériques ne connaissent que **0** (≈ 0 V) et **1** (≈ 5 V ou 3,3 V).

| A | B | ET (AND) | OU (OR) | NON-ET (NAND) |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

La porte **NON** (NOT) inverse : $0 \to 1$ et $1 \to 0$.

### Vérifie

Un système doit allumer un voyant d'alarme si **la température est trop élevée (T = 1) ET le capteur de porte indique « ouvert » (P = 1)**. Quelle porte utiliser ? Que vaut la sortie si T = 1 et P = 0 ?

??? success "Réponse"
    Une porte **ET** (AND). Avec T = 1 et P = 0, la sortie vaut **0** : le voyant reste éteint.

> [!SUCCESS] 🧠 À retenir
> - Non inverseur : $G = 1 + \dfrac{R_f}{R_g}$ ; la sortie est limitée par l'alimentation.
> - Filtre RC : $f_{c} = \dfrac{1}{2\pi RC}$.
> - Une porte logique se décrit par sa **table de vérité**.
