"""Mini-cours de chaque semaine du parcours « L'essentiel en 1 an » (texte pour élèves de Bac Pro)."""

COURS = {}

COURS[1] = r"""
??? question "🤔 À ton avis ?"
    Pourquoi une LED branchée directement sur une pile de 9 V grille-t-elle en un éclair ?

    **Réponse** : parce que rien ne **limite le courant**. Il faut une résistance en série. Toute la semaine sert à comprendre pourquoi et à savoir la calculer.

### 1. Tension, courant, résistance : l'analogie de l'eau

| Grandeur | Symbole | Unité | Analogie du tuyau |
|---|---|---|---|
| **Tension** | $U$ | volt (V) | la **pression** de l'eau |
| **Courant** | $I$ | ampère (A) | le **débit** |
| **Résistance** | $R$ | ohm (Ω) | un **rétrécissement** du tuyau |

> [!TIP] 💡 La loi d'Ohm
> $U = R \times I$, donc $I = \dfrac{U}{R}$ et $R = \dfrac{U}{I}$. Plus la résistance est grande, plus le courant est petit.

**Exemple** : 5 V aux bornes de 330 Ω donnent $I = \dfrac{5}{330} \approx 15{,}2\,\mathrm{mA}$.

### 2. La puissance

$P = U \times I$ (en watts). Une résistance classique supporte **0,25 W** : au-delà, elle chauffe et grille. **Exemple** : 5 V × 0,1 A = 0,5 W → trop pour une résistance de 0,25 W.

### 3. Lire une résistance : le code couleurs

Les anneaux se lisent depuis celui qui est **le plus proche d'une extrémité** :

- **noir** 0 · **marron** 1 · **rouge** 2 · **orange** 3 · **jaune** 4
- **vert** 5 · **bleu** 6 · **violet** 7 · **gris** 8 · **blanc** 9

Anneau 1 et 2 = deux chiffres ; anneau 3 = **multiplicateur** (nombre de zéros) ; anneau 4 = **tolérance** (or ± 5 %, argent ± 10 %).

**Exemple** : marron – noir – orange – or = 1, 0, ×1000 → **10 kΩ ± 5 %**.

Les valeurs vendues suivent une **série** (E12) : 10 · 12 · 15 · 18 · 22 · 27 · 33 · 39 · 47 · 56 · 68 · 82, puis × 10, × 100…

### 4. Associer des résistances

- **En série** : $R_{eq} = R_1 + R_2$ (même courant).
- **En parallèle** : $\dfrac{1}{R_{eq}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$ (même tension).
- **Pont diviseur** : $V_s = V_{cc} \times \dfrac{R_2}{R_1 + R_2}$.

### 5. Les composants à connaître

| Composant | Rôle | À retenir |
|---|---|---|
| **Diode** | laisse passer le courant dans **un seul sens** | seuil ≈ 0,7 V |
| **LED** | diode qui éclaire | seuil ≈ 2 V ; **toujours** une résistance en série |
| **Condensateur** | stocke de l'énergie, lisse les tensions | en farads ; les « chimiques » sont **polarisés** (+ et −) |
| **Transistor** | interrupteur commandé par un petit courant | B, C, E (voir semaine 7) |
| **Régulateur (7805)** | fournit une tension fixe de 5 V | voir semaine 4 |

> [!WARNING] ⚠️ Erreurs fréquentes
> - Brancher une LED **sans** résistance ; la brancher **à l'envers** (la patte longue est l'**anode +**).
> - Brancher un condensateur chimique **à l'envers** : il chauffe et peut éclater.
> - Oublier que 330 kΩ n'est pas 330 Ω (**préfixes** : k = 1000, M = 1 000 000).

### Exercice guidé : la résistance d'une LED

LED rouge (tension 2 V, courant voulu 20 mA) sur une alimentation de 5 V.

$$R = \frac{V_{cc} - V_{LED}}{I} = \frac{5 - 2}{0{,}020} = 150\,\Omega$$

C'est une valeur de la série E12 : on prend **150 Ω**. Le courant réel est alors exactement 20 mA.
"""

COURS[2] = r"""
??? question "🤔 À ton avis ?"
    Tu mesures 5,0 V sur une pin de ton microcontrôleur qui devrait envoyer un signal clignotant. Le multimètre dit « 5 V » : tout va bien ?

    **Réponse** : pas forcément ! Le multimètre donne une **valeur moyenne** : il ne voit pas que le signal est **figé**. Pour vérifier qu'un signal **varie**, il faut l'oscilloscope.

### 1. Le multimètre : quel mode, comment brancher

| Je mesure | Position | Branchement | Circuit |
|---|---|---|---|
| **Tension** (V) | V⎓ | en **parallèle** (aux bornes du composant) | sous tension |
| **Courant** (A) | A⎓ ou mA | en **série** (on **ouvre** le circuit pour insérer l'appareil) | sous tension |
| **Résistance** (Ω) | Ω | aux bornes du composant | **hors tension**, composant isolé |
| **Continuité** | symbole « bip » | aux deux extrémités d'un fil ou d'une piste | **hors tension** |
| **Diode** | symbole diode | LED ou diode | **hors tension** |

> [!WARNING] ⚠️ Le piège classique
> Mesurer une **tension** avec le multimètre en position **ampèremètre** crée un **court-circuit** et fait griller le fusible de l'appareil. Toujours vérifier la position **et** les bornes avant de brancher.

### 2. Lire l'écran de l'oscilloscope

L'écran est un **quadrillage** de carreaux (divisions).

$$U_{pp} = \text{carreaux (hauteur)} \times \text{V/DIV} \qquad T = \text{carreaux (largeur)} \times \text{s/DIV} \qquad f = \frac{1}{T}$$

**Exemple** : un signal carré occupe 3 carreaux en hauteur à 2 V/DIV et une période de 4 carreaux à 5 ms/DIV : $U_{pp} = 6\,\mathrm{V}$, $T = 20\,\mathrm{ms}$, $f = 50\,\mathrm{Hz}$.

### 3. Le rapport cyclique

Pour un signal carré (par exemple PWM) :

$$\text{rapport cyclique} = \frac{t_{haut}}{T} \times 100\,\%$$

**Exemple** : état haut pendant 5 ms sur une période de 20 ms → 25 %.

### 4. L'alimentation de laboratoire et le générateur de fonctions

- **Alimentation de labo** : on règle la **tension** et la **limite de courant** (un fusible réglable) **avant** de brancher. Si le voyant **CC** s'allume, le courant a atteint la limite : **il y a une anomalie** (court-circuit, composant à l'envers).
- **Générateur de fonctions (GBF)** : il **produit** un signal (sinus, carré) dont on règle la **fréquence**, l'**amplitude** et le décalage (offset). On l'observe à l'oscilloscope. On ne le branche **jamais** sur une tension.

**Exemple** : GBF réglé sur un sinus de 1 kHz et 2 V crête à crête : on doit lire à l'oscilloscope $T = 1\,\mathrm{ms}$ et $U_{pp} = 2\,\mathrm{V}$.

### 5. Les réglages à ne pas oublier

1. **Sonde ×10** déclarée sur la voie.
2. **Masse** de la sonde sur la masse du circuit.
3. **Couplage** : DC pour tout voir, AC pour supprimer la composante continue.
4. **Déclenchement** (trigger) réglé pour avoir une image stable.

### Exercice guidé

On observe une période de 5 carreaux à 2 ms/DIV et un signal de 4 carreaux de haut à 1 V/DIV.

$T = 5 \times 2 = 10\,\mathrm{ms}$ ; $f = \dfrac{1}{0{,}010} = 100\,\mathrm{Hz}$ ; $U_{pp} = 4 \times 1 = 4\,\mathrm{V}$.
"""

COURS[3] = r"""
??? question "🤔 À ton avis ?"
    On te donne une carte inconnue avec un composant marqué « LM7805 ». Comment savoir comment le brancher sans rien griller ?

    **Réponse** : on lit sa **datasheet** et le **schéma**. Cette semaine, tu apprends à lire ces deux documents, qui sont ta « notice » en électronique.

### 1. Lire un schéma

Un schéma est un **plan** : il montre **comment les composants sont reliés**, pas où ils sont posés.

- Chaque composant a un **repère** : **R**1 (résistance), **C**1 (condensateur), **D**1 (diode), **Q**1 (transistor), **U**1 (circuit intégré), **J**1 (connecteur).
- Les **traits** sont des fils ; un **point plein** à un croisement veut dire « relié », **sans point** = pas relié.
- Le **+** est en **haut**, la **masse (GND)** en bas, le signal de **gauche à droite**.

> [!TIP] 💡 En clair
> Pour comprendre un schéma, **découpe-le en blocs** : alimentation → traitement → sortie. Puis lis bloc par bloc.

### 2. Lire une datasheet

Une datasheet contient toujours les mêmes parties : description, **brochage**, **limites absolues**, **caractéristiques électriques** (min / typ / max), courbes, boîtier.

| À chercher | Pourquoi |
|---|---|
| **Brochage** | brancher chaque broche au bon endroit |
| **Absolute maximum ratings** | limites à **ne jamais dépasser** |
| **Electrical characteristics** | valeurs **garanties** pour calculer |
| **Package** | choisir l'empreinte du PCB |

On calcule toujours avec le **cas le plus défavorable** (min ou max), jamais avec la valeur « typique ».

### 3. Exemple : le régulateur 7805

- **Brochage** (boîtier TO-220) : 1 = entrée, 2 = masse, 3 = sortie.
- **Sortie** : 5 V (garantie de 4,8 à 5,2 V).
- **Entrée** : de 7 V à 35 V maximum.
- **Montage type** : un condensateur de 100 nF côté entrée et de 10 µF côté sortie.

### 4. Exemple : le transistor BC547

- Limites : $V_{CE}$ max = 45 V ; $I_C$ max = 100 mA.
- Gain $h_{FE}$ de 110 à 800 (très dispersé).
- Saturé : $V_{CE(sat)} \approx 0{,}2\,\mathrm{V}$.

### 5. Exemple : le NE555 en astable

$$f = \frac{1{,}44}{(R_a + 2R_b) \times C} \qquad DC = \frac{R_a + R_b}{R_a + 2R_b}$$

Avec $R_a = 10\,\mathrm{k\Omega}$, $R_b = 68\,\mathrm{k\Omega}$, $C = 10\,\mathrm{\mu F}$ : $f \approx 0{,}99\,\mathrm{Hz}$ et $DC \approx 53\,\%$.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Utiliser une datasheet du **mauvais composant** (vérifie la référence exacte et le fabricant).
> - Confondre **limite absolue** et **valeur de fonctionnement**.
> - Lire le brochage **vu du dessous** au lieu de vu du dessus (le dessin précise le sens).
"""

COURS[4] = r"""
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
"""

COURS[5] = r"""
??? question "🤔 À ton avis ?"
    Pourquoi dessiner le schéma **dans un logiciel** plutôt que sur papier, alors qu'on va ensuite faire le circuit imprimé ?

    **Réponse** : parce que le logiciel (KiCad) **garde en mémoire les liaisons** : c'est ce qu'il transmet ensuite au circuit imprimé (**netlist**). Une erreur de schéma se répercute partout : on la contrôle donc avant.

### 1. Le flux de travail

**Schéma → ERC → empreintes → PCB → DRC → fichiers de fabrication.** Chaque étape se **vérifie** avant la suivante.

### 2. Saisir un schéma dans KiCad (Eeschema)

1. **A** : ajouter un composant (cherche par nom : `R`, `LED`, `NE555`, `BC547`).
2. **P** : ajouter une alimentation (+5 V, GND).
3. **W** : tracer les fils.
4. **L** : poser une étiquette de réseau (net label) pour relier sans tracer.
5. **Annoter** (R1, R2…) et **saisir les valeurs**.
6. **ERC** : contrôle électrique.

### 3. L'ERC et ses erreurs classiques

| Erreur | Cause | Solution |
|---|---|---|
| `power_pin_not_driven` | KiCad ne sait pas qu'une source alimente le rail | poser un **PWR_FLAG** |
| `pin_not_connected` | broche en l'air | la relier, ou poser un **No Connect** (Q) |
| `duplicate_reference` | deux composants avec le même repère | annoter à nouveau |

### 4. Les empreintes (footprints)

L'**empreinte** est le dessin des **pastilles** sur le circuit imprimé. Elle doit correspondre au **boîtier réel** :

- **THT** (traversant) : pattes qui traversent la carte ; facile à souder à la main.
- **CMS** (monté en surface) : composant posé sur les pistes ; plus petit.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Choisir une empreinte **sans vérifier la datasheet** : le composant ne rentre pas.
> - Oublier les **PWR_FLAG** ou la **valeur** des composants.
> - Passer au PCB avec des erreurs d'ERC.

### Exercice guidé

Dessine : un connecteur 2 broches (+12 V, GND), un 7805 avec condensateurs 100 nF et 10 µF, puis une LED avec sa résistance de 150 Ω. Ajoute 2 PWR_FLAG (sur +5 V et GND). L'ERC doit afficher **0 erreur**.
"""

COURS[6] = r"""
??? question "🤔 À ton avis ?"
    Pourquoi les pistes d'alimentation sont-elles plus larges que les pistes de signal ?

    **Réponse** : une piste est un **fil de cuivre** : trop fine pour le courant, elle **chauffe**. On la dimensionne en fonction du courant qu'elle transporte.

### 1. Les règles de conception

| Règle | Valeur courante | Pourquoi |
|---|---|---|
| **Clearance** (espace entre deux pistes) | 0,2 à 0,25 mm | éviter les courts-circuits |
| Piste de **signal** | 0,25 à 0,35 mm | faible courant |
| Piste d'**alimentation** | 0,5 à 0,8 mm | plus de courant |
| **Via** | Ø 0,8 mm, perçage 0,4 mm | passer d'une face à l'autre |

### 2. Placement et routage

1. **Contour** de la carte (Edge.Cuts).
2. Placer les **connecteurs au bord**, puis l'**alimentation**, puis le circuit principal, puis les passifs **près des circuits** qu'ils servent.
3. Le **condensateur de découplage** (100 nF) se place **au plus près** des broches d'alimentation du circuit intégré.
4. **Router l'alimentation en premier**, puis les signaux. Une masse **continue** (pas coupée par une piste) limite les perturbations.

### 3. Contrôler : le DRC

Le DRC vérifie que **rien ne viole les règles** (pistes trop proches, trop fines, pastilles qui se touchent). Objectif : **0 erreur**.

### 4. Les fichiers de fabrication

Le fabricant reçoit :

- les **Gerber** : un fichier par couche (cuivre, masque de soudure, sérigraphie, contour) ;
- le fichier de **perçage** (.drl) ;
- la **BOM** (liste des composants) pour l'assemblage.

> [!TIP] 💡 En clair
> Un fichier Gerber est une **image vectorielle** d'une couche. On l'ouvre dans un **visualiseur** pour voir **exactement** ce qui sera fabriqué.

### 5. Souder et contrôler (IPC-A-610)

Pour un composant traversant (classe 2) : soudure **brillante**, forme de **cône**, trou **rempli à 75 % au moins**. Défauts : **pont de soudure** (court-circuit), soudure **froide** (terne, craquelée), **manque de soudure**.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Ne pas ouvrir les Gerber avant l'envoi.
> - Router une piste de signal **sous** un composant sans y penser (risque de court-circuit).
> - Oublier le **perçage** (fichier .drl) dans l'envoi.
"""

COURS[7] = r"""
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
"""

COURS[8] = r"""
??? question "🤔 À ton avis ?"
    Tu mesures 4,80 V sur une sortie censée être 5 V ± 5 %. Conforme ?

    **Réponse** : oui, **4,80 V est dans la plage [4,75 V ; 5,25 V]**. Mais si l'incertitude de ta mesure est de ± 0,1 V, la vraie valeur pourrait être 4,70 V : **hors tolérance**. On doit donc tenir compte de la **marge de mesure**.

### 1. La tolérance et la plage

« 5 V ± 5 % » signifie : **5 × 0,95 = 4,75 V** à **5 × 1,05 = 5,25 V**. Tout ce qui est dans cette plage est **conforme**.

### 2. La marge de mesure (version essentielle)

Aucun instrument n'est parfait. On estime la marge avec la **précision du constructeur**, par exemple « ± (0,5 % de la lecture + 2 chiffres) » pour un multimètre.

**Exemple** : lecture 5,02 V (résolution 0,01 V) : $0{,}5\,\% \times 5{,}02 = 0{,}025\,\mathrm{V}$ ; 2 chiffres = 0,02 V ; marge ≈ 0,05 V. Résultat : **(5,02 ± 0,05) V**.

> [!TIP] 💡 Règle de conclusion
> On compare **toute la plage** « valeur ± marge » à la tolérance :
> - toute la plage dedans → **conforme** ;
> - une partie dehors → **non garanti / à justifier** ;
> - toute la plage dehors → **non conforme**.

### 3. Le procès-verbal (PV)

Un PV est la **preuve écrite** d'un contrôle. Il contient :

1. **Identification** : carte, date, opérateur ;
2. **Instruments** utilisés (modèle, numéro de série, **étalonnage valide**) ;
3. **Méthode** (comment on a mesuré) ;
4. **Résultats** : attendu, mesuré, marge, verdict pour chaque test ;
5. **Conclusion** : conforme ou non, avec le critère ;
6. **Signature**.

### 4. La traçabilité

Un instrument est **comparé régulièrement** à une référence (étalonnage). Si son étalonnage est **périmé**, ses mesures ne sont plus valables dans un PV.

### Exercice guidé

Carte alimentée en 12 V : sortie 7805 mesurée à $(4{,}99 \pm 0{,}03)\,\mathrm{V}$, tolérance 5 V ± 5 %. Plage mesurée : 4,96 à 5,02 V, dans [4,75 ; 5,25] → **conforme**.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier l'**unité** ou la **tolérance** dans le PV.
> - Conclure « conforme » en comparant **seulement la valeur** et pas la plage avec sa marge.
> - Utiliser un instrument **hors étalonnage**.
"""

COURS[9] = r"""
??? question "🤔 À ton avis ?"
    Un circuit ne marche plus. Tu as un fer à souder et un multimètre. Que fais-tu **en premier** ?

    **Réponse** : tu **observes** et tu **mesures l'alimentation**. Remplacer des composants au hasard fait perdre du temps et risque d'abîmer le circuit.

### 1. La méthode en 6 étapes

1. **Décrire** le symptôme (qu'est-ce qui marche ? qu'est-ce qui ne marche pas ?).
2. **Sécuriser** (tension, chaleur, odeur de brûlé).
3. **Vérifier l'alimentation** sur la carte.
4. **Dresser un tableau de tensions** : point de mesure, valeur attendue, valeur mesurée, verdict.
5. **Isoler** : couper le circuit en deux pour savoir de quel côté est la panne (dichotomie).
6. **Réparer** (un seul changement), **retester**, **tracer** (fiche d'intervention).

### 2. Trouver la panne avec les tensions

La panne est à la **première valeur** qui ne correspond pas à l'attendu, en partant de l'alimentation.

**Exemple** (LED pilotée par un transistor, 5 V) : base ≈ 0,7 V, collecteur ≈ 0,2 V quand tout va bien.

| Symptôme mesuré | Cause probable |
|---|---|
| signal d'entrée 5 V, base à 0 V | résistance de base coupée |
| signal d'entrée 0 V | problème **en amont** du circuit |
| collecteur à 0 V même sans commande | transistor en court-circuit |
| base normale mais collecteur à 1,8 V | transistor qui ne sature pas (résistance de base trop grande) |

### 3. Les mesures hors tension

- **Résistance** : retirée du circuit.
- **Transistor / diode** : test diode (≈ 0,6 V dans un sens, rien dans l'autre).
- **Continuité** : pistes et fils (bip).

### 4. Sécurité

- **Très basse tension** (≤ 50 V AC / 120 V DC) : pas de risque d'électrisation, mais attention à la chaleur et aux courts-circuits.
- Au-delà : **habilitation** (BR) obligatoire.
- **ESD** : bracelet, tapis, sachets antistatiques.

### 5. La fiche d'intervention

Équipement, date, intervenant · symptôme · mesures (attendu / mesuré) · cause · action · test après réparation · préconisation.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Mesurer une résistance **sous tension**.
> - Changer **plusieurs** composants à la fois.
> - Oublier de **retester** (la panne a-t-elle disparu ? autre chose est-il en panne ?).
"""

COURS[10] = r"""
??? question "🤔 À ton avis ?"
    Tu as 3 heures pour mesurer, calculer et rédiger un PV. Comment ne pas perdre de points ?

    **Réponse** : en **suivant un plan** et en vérifiant les points qui rapportent le plus : unités, tolérances, conclusions.

### 1. Le plan de l'épreuve (3 h)

| Phase | Durée | Je fais |
|---|---|---|
| **Lire** | 15 min | tout le sujet, les documents, les consignes |
| **Préparer** | 30 min | calculs préalables : valeurs attendues et plages |
| **Mesurer** | 1 h 15 | mesures **dans l'ordre du sujet** ; je note attendu / mesuré |
| **Analyser** | 30 min | verdicts, calcul de marge, comparaison aux tolérances |
| **Rédiger** | 30 min | PV propre, conclusion argumentée |

### 2. La liste de contrôle avant de rendre

- [ ] Toutes les valeurs ont leur **unité**.
- [ ] Chaque mesure est comparée à une **tolérance** chiffrée.
- [ ] Chaque verdict (**conforme / non conforme**) est **justifié**.
- [ ] Les **instruments** et leur étalonnage sont indiqués.
- [ ] Le PV est **daté, signé**, propre.
- [ ] Les **calculs** sont montrés (formule, application numérique, résultat).

### 3. Les compétences évaluées

- **C03 – Participer à un projet** : respecter le planning, documenter, travailler en équipe.
- **C07 – Réaliser des maquettes et prototypes** : monter, souder, tester.
- **C11 – Maintenir un système électronique** : diagnostiquer, réparer, tracer.

### 4. En cas de blocage

- Une mesure **incohérente** : vérifier le **branchement**, le **calibre**, l'**instrument**, puis refaire.
- Un calcul **bloqué** : passer à la suite et y revenir (ne jamais laisser une partie vide).
- Un doute sur une **formule** : elle est dans les documents autorisés.

### Bilan personnel

Après l'épreuve blanche, classe tes erreurs : **oublis** (unités, tolérance), **calculs**, **manipulations**, **rédaction**. Révise **d'abord** la catégorie où tu perds le plus de points.
"""
