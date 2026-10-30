# 📖 Rappel essentiel : lire un document, calculer, mesurer le NE555 et le 7805

> À lire **avant** le TP. Les valeurs de l'exemple sont **différentes** de celles du sujet.

## 🤔 À ton avis ?

Le cahier des charges demande un clignotement de 1 Hz. Tu mesures 1,3 Hz. Comment trouver quel composant est responsable ?

??? question "Voir une réponse possible"
    On **calcule** la fréquence théorique avec les valeurs **mesurées** de $R_a$, $R_b$ et $C$ : le composant dont la valeur mesurée s'éloigne de son nominal, et dont l'écart **explique** la différence, est le suspect.

## 1. Le NE555 en montage astable

Un **astable** produit un signal carré sans commande extérieure : le condensateur $C$ se charge à travers $R_a + R_b$ jusqu'à $\dfrac{2}{3}V_{CC}$, puis se décharge à travers $R_b$ jusqu'à $\dfrac{1}{3}V_{CC}$, et ainsi de suite.

$$f = \frac{1{,}44}{(R_a + 2R_b)\,C} \quad t_H = 0{,}693\,(R_a + R_b)\,C \quad t_L = 0{,}693\,R_b\,C \quad \text{rapport cyclique} = \frac{R_a + R_b}{R_a + 2R_b}$$

**Exemple** : $R_a = 1\,\mathrm{kΩ}$, $R_b = 47\,\mathrm{kΩ}$, $C = 10\,\mathrm{\mu F}$ → $f \approx 1{,}52\,\mathrm{Hz}$, $t_H \approx 0{,}33\,\mathrm{s}$, $t_L \approx 0{,}33\,\mathrm{s}$, rapport cyclique ≈ 50,5 %. Aux bornes de $C$ (avec $V_{CC} = 5\,\mathrm{V}$), la tension oscille entre environ **1,7 V et 3,3 V**.

## 2. Le régulateur 7805

Le **7805** abaisse une tension d'entrée (au moins ≈ 7 V) à **5 V**. La différence est **perdue en chaleur** : $P = (V_{in} - V_{out}) \times I$. Les condensateurs recommandés à l'entrée et à la sortie évitent les oscillations.

## 3. La méthode du TP

1. **Lire** le cahier des charges et repérer les valeurs attendues et leurs tolérances.
2. **Identifier les blocs** : entrée, alimentation, oscillateur, sortie.
3. **Calculer** avant de mesurer (fréquence, courant LED, puissance dissipée).
4. **Mesurer** en notant l'instrument, les conditions et l'unité.
5. **Comparer** chaque mesure à sa plage et **conclure**.
6. **Chercher l'anomalie** : écart le plus grand → composant suspect → impact chiffré → recommandation.

??? tip "💡 Aide : ordres de grandeur pour vérifier ton travail"
    - **Sortie du 7805** : à $V_{in} = 12\,\mathrm{V}$, attends **4,8 à 5,2 V**.
    - **Régulation** : en passant de 9 V à 15 V en entrée, la sortie varie de **quelques dizaines de mV**.
    - **Fréquence NE555** : la mesure s'écarte souvent de la théorie de **5 à 15 %** à cause des **tolérances** des composants ; au-delà, cherche un composant défectueux.
    - **Sortie du NE555 (broche 3)** : le niveau haut est **un peu en dessous** de $V_{CC}$ (environ 1 V de moins pour un NE555 bipolaire).
    - **Anomalie** : une valeur qui s'éloigne de **plus de 20 %** de son nominal est un **bon candidat**.

## ✅ Vérifie que tu as compris

**Q1.** Si on double la valeur de $C$, que devient la fréquence ?

??? success "Réponse"
    Elle est **divisée par deux** ($f$ est inversement proportionnelle à $C$).

**Q2.** Un 7805 reçoit 12 V et fournit 100 mA. Quelle puissance dissipe-t-il ?

??? success "Réponse"
    $P = (12 - 5) \times 0{,}1 = 0{,}7\,\mathrm{W}$.

**Q3.** Pourquoi le rapport cyclique d'un astable simple est-il toujours supérieur à 50 % ?

??? success "Réponse"
    Parce que la charge passe par $R_a + R_b$ et la décharge seulement par $R_b$ : $t_H > t_L$.
