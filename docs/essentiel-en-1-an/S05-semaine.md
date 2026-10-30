# Semaine 5 : Alimentation et commande de charges

> **Durée** : 4 h · **Compétences E2** : C07, C11

## 🎯 À la fin de la semaine, je sais…

- faire un **bilan de puissance** et prévoir une marge ;
- calculer la **puissance dissipée** et la **température** d'un régulateur linéaire ;
- estimer **l'autonomie** d'une batterie ;
- **commander une charge** avec un transistor, un MOSFET ou un relais ;
- protéger une charge inductive avec une **diode de roue libre**.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | TP virtuels ElectroLab (régulation 7805, transistor, relais, MOSFET) |
| 1 h 15 | Cours : alimentation et thermique |
| 1 h | Cours : commande de charges |
| 45 min | Exercices et auto-test |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾** :

- **Régulation linéaire avec un 7805** (1 h 30)
- **Transistor bipolaire en commutation** (1 h 30)
- **Relais commandé par transistor : la diode de roue libre** (1 h 30)
- **MOSFET de puissance : commande d'une lampe 12 V par une sortie logique** (1 h 15)

---

## 📖 Le cours

**🤔 À ton avis ?** Un régulateur 7805 alimenté en 12 V pour fournir 5 V à 500 mA devient brûlant. Où va l'énergie « en trop » ?

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

On prévoit une **marge de 25 %** : $I_{source} \geq 1{,}25 \times I_{total}$, soit ici 115 mA minimum.

### 2. Le régulateur linéaire et la chaleur

![Régulateur linéaire et régulateur à découpage](images/lineaire-decoupage.png)

Un régulateur linéaire « mange » l'excès de tension **en chaleur** :

$$P_{diss} = (V_{in} - V_{out}) \times I_{out} \qquad \eta \approx \frac{V_{out}}{V_{in}}$$

**Exemple** : 12 V → 5 V à 500 mA : $P = 7 \times 0{,}5 = 3{,}5\,\mathrm{W}$ et $\eta \approx 42\,\%$ : plus de la moitié de l'énergie part en chaleur. Si l'écart est grand ou le courant fort, on utilise un **convertisseur à découpage** (rendement 85 à 90 %).

![Chaîne d'alimentation avec condensateurs de découplage](images/chaine-alimentation-decouplage.png)

### 3. La température du composant

![Modèle thermique d'un régulateur](images/modele-thermique.png)

$$T_j = T_{amb} + P_{diss} \times R_{\theta ja}$$

Pour un 7805 sans radiateur, $R_{\theta ja} \approx 65\,°\mathrm{C/W}$. On vise **moins de 105 °C** (125 °C maximum moins 20 °C de marge).

**Exemple** : $P = 1{,}2\,\mathrm{W}$ à 25 °C ambiants : $T_j = 25 + 1{,}2 \times 65 = 103\,°\mathrm{C}$ : à la limite, il faut un **radiateur**. Avec 3,5 W, $T_j$ dépasserait 250 °C : destruction.

### 4. L'autonomie sur batterie

$$t = \frac{\text{capacité (mAh)}}{I_{moy}\,(\mathrm{mA})} \times 0{,}8$$

Le 0,8 tient compte du fait qu'on n'utilise pas toute la capacité. **Exemple** : 1000 mAh à 50 mA : $t = 20 \times 0{,}8 = 16\,\mathrm{h}$.

Avec une **mise en veille** : 150 mA pendant 5 s puis 0,1 mA pendant 55 s :

$$I_{moy} = \frac{150 \times 5 + 0{,}1 \times 55}{60} \approx 12{,}6\,\mathrm{mA}$$

### 5. Commander une charge : le transistor en interrupteur

Une sortie de microcontrôleur fournit environ **20 mA**. Une charge plus gourmande se commande avec un **transistor** : un petit courant de **base** autorise un grand courant de **collecteur** à l'**émetteur**.

![Transistors NPN, PNP et MOSFET : symboles et rôles](images/transistors.png)

- **Bloqué** : pas de courant de base → interrupteur **ouvert**.
- **Saturé** : courant de base suffisant → interrupteur **fermé** ($V_{CE} \approx 0{,}2\,\mathrm{V}$).

$$I_B = \frac{I_C}{10} \qquad R_b = \frac{V_{commande} - 0{,}7}{I_B}$$

On prend $I_C/10$ (et non $I_C/h_{FE}$) pour être **sûr de saturer**.

![Une LED pilotée par un transistor NPN](images/schema-transistor-led.png)

**Exemple** : charge de 50 mA, commande à 5 V : $I_B = 5\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}005} = 860\,\Omega$ → **820 Ω**.

### 6. Le relais et la diode de roue libre

![Commander un relais avec un transistor : diode de roue libre](images/ess_relais_transistor.png)

Un **relais** est un interrupteur à **bobine** : il isole la commande de la charge. Sa bobine consomme environ 70 mA : on la commande par un **transistor** (BC337 : 800 mA maximum). À la coupure, la bobine produit un **pic de tension** : une **diode de roue libre** (1N4007) en parallèle inverse l'absorbe.

> [!TIP] 💡 Le MOSFET
> Un MOSFET « logic level » se commande par la **tension** de grille (sans courant de commande notable). Une fois passant, il se comporte comme une petite résistance $R_{DS(on)}$ (quelques dizaines de mΩ). Pertes : $P = R_{DS(on)} \times I^2$ (0,2 W pour 22 mΩ et 3 A). On ajoute une résistance de rappel à la masse sur la grille.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Utiliser le courant de **pointe** au lieu du courant **moyen** pour l'autonomie.
> - Oublier la **diode** sur une bobine : le transistor est détruit.
> - Calculer $R_b$ avec le gain maximal : le transistor ne sature pas.

---

## 🛠️ Atelier réel

**Fil rouge 1 : alimentation du clignoteur.**

1. **Bilan** : NE555 ≈ 10 mA, LED = 20 mA : total ?
2. **7805 sous 12 V** : puissance dissipée, puis $T_j$ ($R_{\theta ja} = 65\,°\mathrm{C/W}$, 25 °C ambiants).
3. Même calcul sous **9 V** : que gagne-t-on ?
4. **Autonomie** sur une pile 9 V de 500 mAh.
5. Faut-il un **radiateur** ? Justifie.
6. **Relais** : bobine 5 V / 70 mA commandée à 5 V. Choisis le transistor et calcule $R_b$.

??? success "Résultats attendus"
    1. $I_{total} = 30\,\mathrm{mA}$ ; avec 25 % de marge : 37,5 mA minimum côté source.
    2. $P = (12 - 5) \times 0{,}03 = 0{,}21\,\mathrm{W}$ ; $T_j = 25 + 0{,}21 \times 65 \approx 38{,}7\,°\mathrm{C}$.
    3. $P = 4 \times 0{,}03 = 0{,}12\,\mathrm{W}$ : moins de chaleur.
    4. $t = \dfrac{500}{30} \times 0{,}8 \approx 13\,\mathrm{h}$.
    5. **Non** : 38,7 °C est très inférieur aux 105 °C exploitables.
    6. **BC337** ; $I_B = 7\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}007} \approx 614\,\Omega$ → **560 Ω**.

## ✍️ Exercices

1. Un 7805 alimenté en 24 V débite 100 mA. Que se passe-t-il ?
2. Un convertisseur à découpage de rendement 90 % délivre 5 V sous 100 mA. Quelle puissance prélève-t-il ?
3. Pic de consommation de 220 mA : quelle source minimale ?
4. Courant moyen d'un système à 150 mA pendant 5 s puis 0,1 mA pendant 55 s ?
5. Charge de 30 mA, commande à 5 V : valeur de $R_b$ (règle $I_C/10$) ?

??? success "Corrigés"
    1. $P = 19 \times 0{,}1 = 1{,}9\,\mathrm{W}$ ; $T_j = 25 + 1{,}9 \times 65 \approx 148{,}5\,°\mathrm{C}$ : **supérieur à 125 °C**, le composant est détruit. Il faut un découpage ou un radiateur.
    2. $P_{in} = \dfrac{5 \times 0{,}1}{0{,}9} \approx 0{,}556\,\mathrm{W}$ (pertes ≈ 0,056 W).
    3. $220 \times 1{,}25 = 275\,\mathrm{mA}$.
    4. $\dfrac{750 + 5{,}5}{60} \approx 12{,}6\,\mathrm{mA}$.
    5. $I_B = 3\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}003} \approx 1{,}4\,\mathrm{kΩ}$ → **1,2 kΩ** (E12 inférieure).

## ✅ Auto-test

1. Quelle formule donne la puissance dissipée par un régulateur linéaire ?
2. Pourquoi une diode en parallèle sur la bobine d'un relais ?
3. À quoi sert la marge de 25 % ?
4. Pourquoi un régulateur linéaire chauffe-t-il ?

??? success "Réponses"
    1. $P_{diss} = (V_{in} - V_{out}) \times I_{out}$.
    2. Elle absorbe le **pic de tension** à la coupure.
    3. À absorber les **pointes** de consommation et le vieillissement.
    4. Il **dissipe en chaleur** la différence $V_{in} - V_{out}$.

## 📦 Livrable

Bilan de puissance du clignoteur (tableau, $P_{diss}$, $T_j$, autonomie) et schéma commenté d'une commande de relais.

> [!NOTE] 📚 Pour approfondir (facultatif)
> Ce parcours se suffit à lui-même. Pour aller plus loin : Terminale S03 (dimensionnement d'alimentation), Première S12 (transistor, MOSFET, relais) et Seconde S10 (moteur, PWM, pont en H).
