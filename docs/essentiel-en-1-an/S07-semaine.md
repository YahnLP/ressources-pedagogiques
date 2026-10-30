# Semaine 7 : Commander une charge, amplifier, filtrer

> **Durée** : 4 h · **Compétences E2 travaillées** : C07

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Dimensionner la résistance de base d'un transistor en commutation.
- Choisir transistor, MOSFET ou relais, et protéger une charge inductive.
- Calculer le gain d'un AOP non inverseur et la fréquence de coupure d'un filtre RC.
- Lire une table de vérité.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Transistor en commutation : $R_b$ |
| 1 h | MOSFET et relais, diode de roue libre |
| 1 h | AOP, filtre RC, portes logiques |
| 1 h | Auto-test et correction |

## 📖 Le cours en bref

??? question "🤔 À ton avis ?"
    Une sortie de microcontrôleur donne **20 mA**. Un relais demande **70 mA**. Comment le piloter ?

    **Réponse** : avec un **transistor** : un petit courant de commande permet un gros courant dans la charge.

### 1. Le transistor en interrupteur

Un transistor NPN (BC547, BC337) : un petit courant dans la **base (B)** autorise un grand courant entre **collecteur (C)** et **émetteur (E)**.

- **Bloqué** : pas de courant de base → interrupteur **ouvert**.
- **Saturé** : courant de base suffisant → interrupteur **fermé** ($V_{CE} \approx 0{,}2\,\mathrm{V}$).

$$I_B = \frac{I_C}{10} \qquad R_b = \frac{V_{commande} - 0{,}7}{I_B}$$

**Exemple** : charge de 50 mA, commande à 5 V : $I_B = 5\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}005} = 860\,\Omega$ → **820 Ω**.

### 2. MOSFET et relais

- **MOSFET** « logic level » : se commande par la **tension** de grille ; très faibles pertes ; ajouter une résistance de rappel à la masse sur la grille.
- **Relais** : interrupteur à **bobine**. Toujours une **diode de roue libre** en parallèle inverse de la bobine, sinon le **pic de tension** détruit le transistor.

### 3. L'amplificateur opérationnel (AOP)

Montage **non inverseur** : $G = 1 + \dfrac{R_f}{R_g}$. **Exemple** : $R_f = 10\,\mathrm{k\Omega}$, $R_g = 1\,\mathrm{k\Omega}$ → $G = 11$ : 100 mV en entrée donnent 1,1 V en sortie. La sortie ne dépasse jamais l'alimentation.

### 4. Le filtre RC passe-bas

$$f_c = \frac{1}{2\pi R C}$$

Il laisse passer les **basses fréquences** et atténue les **hautes**. **Exemple** : 10 kΩ et 100 nF → $f_c \approx 159\,\mathrm{Hz}$.

### 5. Les portes logiques

| A | B | ET | OU | NON-ET |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

> [!WARNING] ⚠️ Erreurs fréquentes
> - Calculer $R_b$ avec le gain maximal : on prend **$I_C/10$** pour être sûr de saturer.
> - Oublier la **diode** sur une bobine.
> - Alimenter un AOP en 5 V en attendant une sortie de 8 V.

## 🛠️ Atelier guidé : on construit ensemble le clignoteur

**Fil rouge** : tu **améliores** le clignoteur en lui faisant commander une charge plus puissante (un relais 5 V, 70 mA).

1. **Choisis** le transistor (BC547 ou BC337) et justifie.
2. **Calcule** $R_b$ (commande par la sortie du NE555 à environ 5 V, règle $I_C/10$).
3. **Dessine** le schéma : bobine du relais, diode de roue libre, transistor.
4. **Filtre** : place un filtre RC (10 kΩ, 100 nF) sur une tension bruitée et calcule sa fréquence de coupure.
5. **Logique** : écris la table de vérité d'une alarme « température haute ET porte ouverte ».

??? success "Résultats attendus"
    1. **BC337** (800 mA maximum) : le BC547 serait trop juste à 70 mA.
    2. $I_B = 7\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}007} \approx 614\,\Omega$ → **560 Ω**.
    3. Diode 1N4007 en parallèle inverse de la bobine.
    4. $f_c = \dfrac{1}{2\pi \times 10^{4} \times 10^{-7}} \approx 159\,\mathrm{Hz}$.
    5. Porte **ET** : la sortie vaut 1 seulement si les deux entrées valent 1.

## ✍️ Exercices d'application

1. $R_f = 22\,\mathrm{k\Omega}$, $R_g = 2{,}2\,\mathrm{k\Omega}$ sur un AOP non inverseur : gain ?
2. Filtre RC : $R = 4{,}7\,\mathrm{k\Omega}$, $C = 10\,\mathrm{nF}$. Fréquence de coupure ?
3. MOSFET de $R_{DS(on)} = 22\,\mathrm{m\Omega}$ et courant de 3 A : puissance dissipée ?
4. Sortie d'une porte NON-ET avec A = 1 et B = 1 ?

??? success "Corrigés"
    1. $G = 1 + 10 = 11$.
    2. $f_c = \dfrac{1}{2\pi \times 4700 \times 10^{-8}} \approx 3{,}4\,\mathrm{kHz}$.
    3. $P = 0{,}022 \times 9 \approx 0{,}2\,\mathrm{W}$ : pas de radiateur.
    4. **0**.

## 📚 Pour approfondir : les séances à consulter

- [Première S12 – transistor, MOSFET, relais](../premiere/S12-prototypes-avances-integration/03-transistor-mosfet-relais.md)
- [Première S12 – AOP, filtre RC, portes logiques](../premiere/S12-prototypes-avances-integration/04-aop-filtre-logique.md)

## ✅ Auto-test

1. Charge de 50 mA, commande à 5 V : valeur de $R_b$ ?
2. Pourquoi une diode sur une bobine de relais ?
3. AOP non inverseur, $R_f = 10\,\mathrm{k\Omega}$, $R_g = 1\,\mathrm{k\Omega}$ : gain ?
4. $R = 10\,\mathrm{k\Omega}$, $C = 100\,\mathrm{nF}$ : $f_c$ ?
5. Sortie d'une porte ET avec A = 1, B = 0 ?

??? success "Réponses"
    1. $I_B = 5\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}005} = 860\,\Omega$ → **820 Ω**.
    2. Elle absorbe le **pic de tension** à la coupure.
    3. $1 + 10 = 11$.
    4. $\dfrac{1}{2\pi RC} \approx 159\,\mathrm{Hz}$.
    5. **0**.

## 📦 Livrable

Schéma commenté d'une commande de relais par transistor, avec calcul de $R_b$.
