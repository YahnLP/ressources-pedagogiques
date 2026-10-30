# Semaine 4 : Alimentation et commande de charges

> **Durée** : 4 h · **Compétences E2 travaillées** : C07 · C11

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Faire un bilan de puissance (courant de pointe et courant moyen).
- Calculer la puissance dissipée par un régulateur linéaire et sa température de jonction.
- Estimer l'autonomie d'une batterie.
- Commander une charge avec un transistor, un MOSFET ou un relais.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | TP virtuels ElectroLab : régulation 7805, transistor |
| 1 h | Bilan de puissance et thermique |
| 1 h | Transistor, MOSFET, relais, diode de roue libre |
| 1 h | Atelier réel et auto-test |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾**, puis fais ces TP **avant** de toucher au matériel :

- **Régulation linéaire avec un 7805** (1 h 30, niveau terminale)
- **Transistor bipolaire en commutation** (1 h 30, niveau première)
- **Relais commandé par transistor : la diode de roue libre** (1 h 30, niveau terminale)
- **MOSFET de puissance : commande d'une lampe 12 V par une sortie logique** (1 h 15, niveau terminale)

> [!TIP] 🖥️ Pourquoi d'abord le simulateur ?
> On peut se tromper sans rien casser, répéter autant de fois que nécessaire et obtenir une correction automatique. Le TP réel sert ensuite à **confirmer** et à manipuler le vrai matériel.

## 📖 Le cours en bref

**🤔 À ton avis ?** Un régulateur 7805 alimenté en 12 V pour fournir 5 V à 500 mA devient **brûlant**. Pourquoi ? Où va l'énergie « en trop » ?

??? question "Réponse"
    Elle est **transformée en chaleur** dans le régulateur. On va apprendre à la calculer.

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

### 5. Le transistor en interrupteur

Un transistor NPN (BC547, BC337) : un petit courant dans la **base (B)** autorise un grand courant entre **collecteur (C)** et **émetteur (E)**.

- **Bloqué** : pas de courant de base → interrupteur **ouvert**.
- **Saturé** : courant de base suffisant → interrupteur **fermé** ($V_{CE} \approx 0{,}2\,\mathrm{V}$).

$$I_B = \frac{I_C}{10} \qquad R_b = \frac{V_{commande} - 0{,}7}{I_B}$$

**Exemple** : charge de 50 mA, commande à 5 V : $I_B = 5\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}005} = 860\,\Omega$ → **820 Ω**.

### 6. MOSFET et relais

- **MOSFET** « logic level » : se commande par la **tension** de grille ; très faibles pertes ; ajouter une résistance de rappel à la masse sur la grille.
- **Relais** : interrupteur à **bobine**. Toujours une **diode de roue libre** en parallèle inverse de la bobine, sinon le **pic de tension** détruit le transistor.


## 🛠️ Atelier guidé : on construit, on mesure, on valide

**Fil rouge** : tu dimensionnes l'**alimentation du clignoteur** (12 V → 5 V).

1. **Bilan** : NE555 ≈ 10 mA, LED = 20 mA. Total ?
2. **Régulateur** : puissance dissipée par le 7805 sous 12 V, puis température de jonction ($R_{\theta ja} = 65\,°\mathrm{C/W}$, 25 °C ambiants).
3. Même calcul sous **9 V** (pile) : que gagne-t-on ?
4. **Autonomie** sur une pile 9 V de 500 mAh.
5. Faut-il un **radiateur** ? Justifie.

??? success "Résultats attendus"
    1. $I_{total} = 30\,\mathrm{mA}$ ; avec 25 % de marge : 37,5 mA minimum côté source.
    2. $P = (12 - 5) \times 0{,}03 = 0{,}21\,\mathrm{W}$ ; $T_j = 25 + 0{,}21 \times 65 \approx 38{,}7\,°\mathrm{C}$.
    3. $P = 4 \times 0{,}03 = 0{,}12\,\mathrm{W}$ : moins de chaleur, meilleur rendement.
    4. $t = \dfrac{500}{30} \times 0{,}8 \approx 13\,\mathrm{h}$.
    5. **Non** : 38,7 °C est très inférieur aux 105 °C exploitables.

## ✍️ Exercices d'application

1. Un 7805 alimenté en 24 V débite 100 mA. Que se passe-t-il ?
2. Un convertisseur à découpage de rendement 90 % délivre 5 V sous 100 mA. Quelle puissance prélève-t-il ? Quelles pertes ?
3. Pic de consommation de 220 mA : quelle source minimale ?
4. $R_f = 22\,\mathrm{k\Omega}$, $R_g = 2{,}2\,\mathrm{k\Omega}$ sur un AOP non inverseur : gain ?

??? success "Corrigés"
    1. $P = 19 \times 0{,}1 = 1{,}9\,\mathrm{W}$ ; $T_j = 25 + 1{,}9 \times 65 \approx 148{,}5\,°\mathrm{C}$ : **supérieur à 125 °C**, le composant est détruit. Il faut un convertisseur à découpage ou un radiateur.
    2. $P_{in} = \dfrac{5 \times 0{,}1}{0{,}9} \approx 0{,}556\,\mathrm{W}$ ; pertes ≈ **0,056 W**.
    3. $220 \times 1{,}25 = 275\,\mathrm{mA}$.
    4. $G = 1 + 10 = 11$.

## 📚 Pour approfondir : les séances à consulter

- [Terminale S03 – dimensionnement d'alimentation](../terminale/S03-dimensionnement-d-alimentation-bilan-de/01-cours.md)
- [Première S12 – transistor, MOSFET, relais](../premiere/S12-prototypes-avances-integration/03-transistor-mosfet-relais.md)

## ✅ Auto-test

1. Pic de 400 mA : quelle source minimale avec 25 % de marge ?
2. Un 7805 passe de 9 V à 5 V pour 300 mA. Quelle puissance dissipe-t-il ?
3. Avec $R_{\theta ja} = 65\,°\mathrm{C/W}$ et 25 °C ambiants, quelle est $T_j$ ?
4. Charge de 50 mA, commande à 5 V : valeur de $R_b$ ?
5. Pourquoi une diode sur une bobine de relais ?

??? success "Réponses"
    1. $400 \times 1{,}25 = 500\,\mathrm{mA}$.
    2. $(9 - 5) \times 0{,}3 = 1{,}2\,\mathrm{W}$.
    3. $25 + 1{,}2 \times 65 = 103\,°\mathrm{C}$ : radiateur recommandé.
    4. $I_B = 5\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}005} = 860\,\Omega$ → **820 Ω**.
    5. Elle absorbe le **pic de tension** à la coupure.

## 📦 Livrable

Bilan de puissance complet d'un petit montage (tableau + conclusion sur le régulateur).
