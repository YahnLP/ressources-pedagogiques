# Semaine 4 : L'alimentation : bilan de puissance et thermique

> **Durée** : 4 h · **Compétences E2 travaillées** : C07 · C11

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Faire un bilan de puissance (courant de pointe et courant moyen).
- Calculer la puissance dissipée par un régulateur linéaire et sa température de jonction.
- Estimer l'autonomie d'une batterie.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Bilan de puissance : tableau et marge de 25 % |
| 1 h | Régulateur linéaire : $P_{diss}$ et rendement |
| 1 h | Température de jonction, radiateur, autonomie |
| 1 h | Auto-test et correction |

## 📚 Ressources à utiliser

- [Terminale S03 – dimensionnement d'alimentation](../S03-dimensionnement-d-alimentation-bilan-de/01-cours.md)

## ✅ Auto-test

1. Pic de 400 mA : quelle source minimale avec 25 % de marge ?
2. Un 7805 passe de 9 V à 5 V pour 300 mA. Quelle puissance dissipe-t-il ?
3. Avec $R_{\theta ja} = 65\,°\mathrm{C/W}$ et 25 °C ambiants, quelle est $T_j$ ?
4. Batterie 1000 mAh, 50 mA : autonomie réelle ?
5. Pourquoi un régulateur linéaire chauffe-t-il ?

??? success "Réponses"
    1. $400 \times 1{,}25 = 500\,\mathrm{mA}$.
    2. $(9 - 5) \times 0{,}3 = 1{,}2\,\mathrm{W}$.
    3. $25 + 1{,}2 \times 65 = 103\,°\mathrm{C}$ : radiateur recommandé.
    4. $\dfrac{1000}{50} \times 0{,}8 = 16\,\mathrm{h}$.
    5. Il **dissipe en chaleur** la différence $V_{in} - V_{out}$.

## 📦 Livrable

Bilan de puissance complet d'un petit montage (tableau + conclusion sur le régulateur).
