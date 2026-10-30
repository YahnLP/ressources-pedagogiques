# 🔌 Commander une charge : transistor, MOSFET, relais

## 🤔 À ton avis ?

Une broche d'Arduino ne peut fournir qu'environ **20 mA**. Un petit moteur ou un relais demande **70 mA ou plus**. Comment le piloter quand même ?

??? question "Réponse"
    Avec un **interrupteur commandé** : un composant qui laisse passer un gros courant quand un petit signal le commande. Ce composant est un **transistor**, un **MOSFET** ou un **relais**.

## 1. Le transistor bipolaire en commutation

Un transistor NPN (BC547, BC337) a trois broches : **B** (base), **C** (collecteur), **E** (émetteur). Un **petit courant de base** permet un **gros courant de collecteur**.

> [!TIP] 💡 En clair
> En commutation, on veut que le transistor soit **soit bloqué** (interrupteur ouvert), **soit saturé** (interrupteur fermé, $V_{CE} \approx 0{,}2\,\mathrm{V}$). Pour être sûr de saturer, on applique la règle du **gain forcé** : $I_{B} = \dfrac{I_C}{10}$ (et non $\dfrac{I_C}{h_{FE}}$, trop optimiste).

$$R_{b} = \frac{V_{\text{commande}} - 0{,}7}{I_B}$$

### Vérifie

Un transistor doit piloter une charge de **50 mA**, commandée par une sortie à 5 V. Calcule $I_{B}$ puis $R_{b}$ (valeur normalisée).

??? success "Réponse"
    $I_{B} = \dfrac{50}{10} = 5\,\mathrm{mA}$ ; $R_{b} = \dfrac{5 - 0{,}7}{0{,}005} = 860\,\Omega$ → on prend **820 Ω** (valeur normalisée inférieure, pour saturer avec sûreté).

## 2. Le MOSFET : commandé par une tension

Un **MOSFET** (par exemple IRLZ44N, « logic level ») se commande par la **tension de grille** $V_{GS}$, **sans courant de commande** notable. Une fois passant, il se comporte comme une petite résistance $R_{DS(on)}$ (de l'ordre de 22 mΩ pour l'IRLZ44N à $V_{GS} = 5\,\mathrm{V}$ ; vérifie dans la datasheet).

| | Transistor bipolaire | MOSFET |
|---|---|---|
| Commandé par | un **courant** de base | une **tension** de grille |
| Pertes en conduction | $V_{CE(sat)} \times I_{C}$ | $R_{DS(on)} \times I^2$ |
| Usage typique | petites charges (< 500 mA) | charges plus fortes, PWM |

> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier la **résistance de rappel à la masse** (10 kΩ) sur la grille : le MOSFET peut s'ouvrir tout seul au démarrage.
> - Choisir un MOSFET qui n'est **pas « logic level »** : avec 5 V sur la grille, il ne conduit pas bien et chauffe.

### Vérifie

Un MOSFET avec $R_{DS(on)} = 22\,\mathrm{m\Omega}$ commande un moteur de 2 A. Quelle puissance dissipe-t-il ? Faut-il un radiateur ?

??? success "Réponse"
    $P = R_{DS(on)} \times I^2 = 0{,}022 \times 2^2 = 0{,}088\,\mathrm{W}$ : **pas de radiateur** nécessaire.

## 3. Le relais

Un **relais** est un interrupteur **mécanique** commandé par une **bobine**. Il isole complètement la commande du circuit commandé (par exemple pour des tensions plus élevées). Une bobine 5 V consomme typiquement **70 mA** : on ne la branche **pas** directement à une broche, on utilise un transistor.

> [!WARNING] ⚠️ Diode de roue libre
> Quand on coupe le courant dans une bobine, elle produit un **pic de tension** qui peut détruire le transistor. On place une **diode** (1N4007) en **parallèle inverse** de la bobine : elle absorbe ce pic.

### Vérifie

1. Une bobine de relais consomme 70 mA sous 5 V. Quel transistor choisir : BC547 (100 mA max) ou BC337 (800 mA max) ? Pourquoi ?
2. Calcule $R_{b}$ pour une commande à 5 V (gain forcé de 10).
3. Pourquoi la diode est-elle indispensable ?

??? success "Réponses"

    1. **BC337** : 70 mA est trop proche des 100 mA maximum du BC547, sans marge.
    2. $I_{B} = \dfrac{70}{10} = 7\,\mathrm{mA}$ ; $R_{b} = \dfrac{4{,}3}{0{,}007} \approx 614\,\Omega$ → **560 Ω**.
    3. La diode **absorbe le pic de tension** produit à l'ouverture de la bobine, qui détruirait sinon le transistor.

> [!SUCCESS] 🧠 À retenir
> - Transistor : $R_{b} = \dfrac{V - 0{,}7}{I_C / 10}$, avec une marge sur $I_{C}$ maximum.
> - MOSFET : prendre un modèle « logic level », mettre une résistance de rappel sur la grille.
> - Charge inductive (relais, moteur) : **toujours** une diode de roue libre.
