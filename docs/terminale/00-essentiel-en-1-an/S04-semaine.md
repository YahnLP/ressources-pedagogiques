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

## 📖 Le cours en bref

??? question "🤔 À ton avis ?"
    Un régulateur 7805 alimenté en 12 V pour fournir 5 V à 500 mA devient **brûlant**. Pourquoi ? Où va l'énergie « en trop » ?

    **Réponse** : elle est **transformée en chaleur** dans le régulateur. On va apprendre à la calculer.

### 1. Le bilan de puissance

Avant de choisir une alimentation, on **additionne les courants** de tous les composants :

| Composant | Tension | Courant |
|---|---|---|
| Microcontrôleur | 3,3 V | 80 mA |
| Capteur | 3,3 V | 2 mA |
| LED | 3,3 V | 10 mA |
| **Total** | | **92 mA** |

On prévoit une **marge de 25 %** : $I_{source} \geq 1{,}25 \times I_{total}$ → ici 115 mA minimum.

### 2. Le régulateur linéaire

Il « mange » l'excès de tension en chaleur :

$$P_{diss} = (V_{in} - V_{out}) \times I_{out} \qquad \eta \approx \frac{V_{out}}{V_{in}}$$

**Exemple** : 12 V → 5 V à 500 mA : $P = 7 \times 0{,}5 = 3{,}5\,\mathrm{W}$ et $\eta \approx 42\,\%$. Plus de la moitié de l'énergie part en chaleur.

> [!TIP] 💡 En clair
> Plus l'écart $V_{in} - V_{out}$ est grand, plus ça chauffe. Si l'écart est grand ou le courant fort, on utilise un **convertisseur à découpage** (rendement 85 à 90 %).

### 3. La température du composant

$$T_j = T_{amb} + P_{diss} \times R_{\theta ja}$$

Pour un 7805 sans radiateur, $R_{\theta ja} \approx 65\,°\mathrm{C/W}$.

**Exemple** : $P = 1{,}2\,\mathrm{W}$ et 25 °C ambiants : $T_j = 25 + 1{,}2 \times 65 = 103\,°\mathrm{C}$. On vise **moins de 105 °C** (125 °C maxi moins 20 °C de marge) : on est à la limite, **il faut un radiateur** ou un autre montage. Avec les 3,5 W de l'exemple 2, $T_j$ atteindrait plus de 250 °C : le composant serait détruit.

### 4. L'autonomie sur batterie

$$t = \frac{\text{capacité (mAh)}}{I_{moy}\,(\mathrm{mA})} \times 0{,}8$$

Le 0,8 tient compte du fait qu'on n'utilise pas toute la capacité.

**Exemple** : batterie 1000 mAh, consommation moyenne 50 mA : $t = \dfrac{1000}{50} \times 0{,}8 = 16\,\mathrm{h}$.

**Courant moyen avec mise en veille** : un système consomme 150 mA pendant 5 s, puis 0,1 mA pendant 55 s :

$$I_{moy} = \frac{150 \times 5 + 0{,}1 \times 55}{60} \approx 12{,}6\,\mathrm{mA}$$

> [!WARNING] ⚠️ Erreurs fréquentes
> - Utiliser le courant de **pointe** au lieu du courant **moyen** pour l'autonomie.
> - Oublier la **marge de 25 %**.
> - Oublier de convertir **mA ↔ A** dans $P = U \times I$.

## 📚 Pour approfondir : les séances à consulter

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
