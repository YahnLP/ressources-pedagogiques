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

## 📚 Ressources à utiliser

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
