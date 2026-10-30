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

## 📚 Pour approfondir : les séances à consulter

- [Première S12 – transistor, MOSFET, relais](../../premiere/S12-prototypes-avances-integration/03-transistor-mosfet-relais.md)
- [Première S12 – AOP, filtre RC, portes logiques](../../premiere/S12-prototypes-avances-integration/04-aop-filtre-logique.md)

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
