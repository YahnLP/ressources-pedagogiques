# 📘 FICHE DE COURS — S2 / Module E2
## Diodes LED · Circuits Série & Parallèle · Loi d'Ohm appliquée

---

## 🗝️ Vocabulaire clé à maîtriser pour l'examen

| Terme | Définition à retenir |
|---|---|
| **LED** | Light Emitting Diode — Diode électroluminescente qui émet de la lumière quand elle est traversée par un courant dans le bon sens |
| **Anode (+)** | Borne positive de la LED — broche la plus longue — sens d'entrée du courant conventionnel |
| **Cathode (−)** | Borne négative de la LED — broche la plus courte — côté méplat sur le boîtier |
| **Tension de seuil ($V_{F}$)** | Tension minimale pour que la LED s'allume (Forward Voltage) : ≈ 2 V rouge, ≈ 2,1 V vert, ≈ 3,3 V bleu |
| **Courant nominal ($I_{F}$)** | Courant de fonctionnement normal de la LED : généralement 20 mA = 0,02 A |
| **Résistance de limitation** | Résistance placée en série avec la LED pour protéger de l'excès de courant |
| **Loi d'Ohm** | U = R × I — Relation entre tension (V), résistance (Ω) et courant (A) |
| **Circuit série** | Les composants sont branchés les uns après les autres — même courant partout |
| **Circuit parallèle** | Les composants sont branchés côte à côte — même tension aux bornes de chacun |
| **Datasheet** | Document technique du fabricant donnant toutes les caractéristiques d'un composant |


### 🤔 À ton avis ?

Sur les anciennes guirlandes de Noël, quand **une seule ampoule grille**, **toute la guirlande s'éteint**. Sur les guirlandes LED modernes, les autres restent allumées. Pourquoi, à ton avis ?

??? question "Voir une réponse possible"
    Les anciennes ampoules sont branchées **les unes après les autres**, **en série** : un seul chemin pour le courant, donc une coupure arrête tout. Les montages modernes utilisent des **branches en parallèle** : chaque LED a son propre chemin.
    
    Dans cette séance, tu vas apprendre à **calculer** la résistance qui protège une LED et à comprendre ces deux façons de brancher des composants.

---

## 1. La diode LED : structure et fonctionnement

### 1.1 Qu'est-ce qu'une LED ?

Une LED est un composant **semiconducteur** qui transforme l'énergie électrique en lumière. Elle ne laisse passer le courant que **dans un seul sens** (du + vers le −, de l'anode vers la cathode).

> ⚠️ **Règle d'or** : Une LED sans résistance de protection grille immédiatement. Ne jamais brancher une LED directement sur une alimentation.

### 1.2 Symbole et identification physique

![Symbole IEC et aspect réel d'une LED](images/diode-led.png)

| Caractéristique | Rouge | Vert | Bleu | Blanc |
|---|---|---|---|---|
| Tension $V_{F}$ typique | 1,8 – 2,2 V | 2,0 – 2,5 V | 3,0 – 3,5 V | 3,0 – 3,5 V |
| Courant $I_{F}$ nominal | 20 mA | 20 mA | 20 mA | 20 mA |
| Courant $I_{F}$ maximum | 30 mA | 30 mA | 30 mA | 30 mA |


> [!TIP] 💡 En clair
> Une LED est une **diode** qui émet de la lumière. Elle laisse passer le courant **dans un seul sens** : de l'**anode (+)** vers la **cathode (−)**.
>
> Pour s'allumer, elle a besoin d'une tension minimale appelée **tension de seuil** ($V_F$, environ 2 V pour une LED rouge). Ensuite, **le courant augmente très vite** : si rien ne le limite, la LED est détruite. D'où la **résistance de limitation**.

### ✅ Vérifie que tu as compris

**Q1.** Une LED ne s'allume pas alors que le circuit est complet. Quelle est la première chose à vérifier ?

??? success "Réponse"
    Le **sens de branchement** : la patte longue (anode) doit aller vers le **+**.

**Q2.** Que signifie $V_F$ pour une LED ?

??? success "Réponse"
    La **tension de seuil** (« forward voltage ») : la tension qui apparaît aux bornes de la LED quand elle est allumée (environ 2 V pour une rouge).

**Q3.** Pourquoi une LED ne supporte-t-elle pas 9 V directement ?

??? success "Réponse"
    Elle laisse alors passer un courant **beaucoup trop fort** et elle est détruite. Il faut une résistance en série.

> [!SUCCESS] 🧠 À retenir
> - La LED est une diode : elle a un sens (anode +, cathode −).
> - Elle a une tension de seuil $V_F$ et un courant normal $I_F$ (≈ 20 mA).

---

## 2. La Loi d'Ohm — Rappel et application

### 2.1 La formule fondamentale

$$U = R \times I$$

| Symbole | Grandeur | Unité | Instrument |
|---|---|---|---|
| **U** | Tension (différence de potentiel) | Volt (V) | Voltmètre — en parallèle |
| **R** | Résistance | Ohm (Ω) | Ohmmètre — hors circuit |
| **I** | Intensité du courant | Ampère (A) — souvent mA | Ampèremètre — en série |

### 2.2 Le triangle mnémotechnique

![Cercle de la loi d'Ohm : U en haut, R à gauche, I à droite](images/loi-ohm-cercle.png)

### 2.3 Les trois formules à retenir

| Je cherche... | La formule | Exemple numérique |
|---|---|---|
| La tension U | $U = R \times I$ | R = 150 Ω, I = 20 mA → U = 150 × 0,02 = **3 V** |
| La résistance R | $R = \dfrac{U}{I}$ | U = 7 V, I = 20 mA → R = 7 / 0,02 = **350 Ω** |
| Le courant I | $I = \dfrac{U}{R}$ | U = 5 V, R = 250 Ω → I = 5 / 250 = $0{,}02\,\mathrm{A} = 20\,\mathrm{mA}$ |

> 💡 **Attention aux unités !** Les calculs se font avec des Ampères (A), pas des milliampères (mA).  
> Conversion : $20\,\mathrm{mA} = 0{,}020\,\mathrm{A}$ (diviser par 1000)


> [!TIP] 💡 En clair
> C'est la **même loi d'Ohm** que dans la séance S01 : $U = R \times I$. Ici, on l'utilise sur la résistance qui protège la LED.
>
> Trois réflexes : **écrire ce qu'on cherche**, **convertir en V, A, Ω**, puis **calculer** avec la bonne formule.

### ✅ Vérifie que tu as compris

**Q1.** Une résistance de 220 Ω est traversée par 15 mA. Quelle tension a-t-elle à ses bornes ?

??? success "Réponse"
    $U = R \times I = 220 \times 0{,}015 = 3{,}3\,\mathrm{V}$ (15 mA = 0,015 A).

**Q2.** Une tension de 6 V est appliquée à 300 Ω. Quel courant passe ?

??? success "Réponse"
    $I = \dfrac{U}{R} = \dfrac{6}{300} = 0{,}02\,\mathrm{A} = 20\,\mathrm{mA}$.

**Q3.** Pourquoi convertit-on les mA en A avant de calculer ?

??? success "Réponse"
    Parce que la loi d'Ohm donne un bon résultat avec les **unités de base** : volts, ampères et ohms.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Utiliser 20 au lieu de 0,02 pour 20 mA : le résultat est faux d'un facteur 1 000.

---

## 3. Calcul de la résistance de limitation d'une LED

### 3.1 La logique du calcul

![Circuit LED : pile 9 V, résistance et LED en série](images/circuit-led-9v.png)

Quand on branche une LED sur une alimentation, il faut "absorber" la tension en surplus avec une résistance.

### 3.2 La formule de calcul

$$R = \frac{V_{alim} - V_{F}}{I_F}$$

Où :

- **$V_{\mathrm{alim}}$** = tension de l'alimentation (en Volts)
- **$V_{F}$** = tension de seuil de la LED (en Volts, lue dans la datasheet)
- **$I_{F}$** = courant nominal de la LED (en **Ampères** — convertir les mA !)

### 3.3 Exemples de calcul pas à pas

**Exemple 1 — LED rouge sur alimentation 9 V**

> *Données : $V_{\mathrm{alim}}$ = 9 V | LED rouge : $V_{F}$ = 2 V, $I_{F}$ = 20 mA = 0,02 A*

| Étape | Calcul | Résultat |
|---|---|---|
| 1. Tension à absorber | $V_{\mathrm{R}} = V_{\mathrm{alim}} - V_{\mathrm{F}} = 9 - 2$ | $V_{\mathrm{R}} = 7\,\mathrm{V}$ |
| 2. Calcul R | $R = \dfrac{V_{\mathrm{R}}}{I_{\mathrm{F}}} = \dfrac{7}{0{,}02}$ | $R = 350\,\mathrm{\Omega }$ |
| 3. Valeur normalisée E24 | La valeur normalisée la plus proche ≥ 350 Ω | $R = 390\,\mathrm{\Omega }$ *(on choisit la valeur supérieure pour protéger la LED)* |

**Exemple 2 — LED bleue sur alimentation 5 V (Arduino)**

> *Données : $V_{\mathrm{alim}}$ = 5 V | LED bleue : $V_{F}$ = 3,3 V, $I_{F}$ = 20 mA = 0,02 A*

| Étape | Calcul | Résultat |
|---|---|---|
| 1. Tension à absorber | $V_{\mathrm{R}} = 5 - 3{,}3$ | $V_{\mathrm{R}} = 1{,}7\,\mathrm{V}$ |
| 2. Calcul R | $R = \dfrac{1{,}7}{0{,}02}$ | $R = 85\,\mathrm{\Omega }$ |
| 3. Valeur normalisée E24 | Valeur supérieure la plus proche | $R = 100\,\mathrm{\Omega }$ |


> [!TIP] 💡 En clair
> Une LED rouge « garde » environ 2 V pour elle. Si tu l'alimentes avec 9 V, il reste **7 V en trop**. C'est la **résistance** qui doit les absorber, tout en laissant passer 20 mA.
>
> **Méthode en 4 étapes :**
>
> 1. **Tension à absorber** : $V_R = V_{alim} - V_F$.
> 2. **Courant voulu** : $I_F = 20\,\mathrm{mA} = 0{,}02\,\mathrm{A}$.
> 3. **Calcul** : $R = \dfrac{V_R}{I_F}$.
> 4. **Choix** : on prend la valeur **normalisée** (série E24) **au-dessus** du résultat.

### ✅ Vérifie que tu as compris

**Q1.** Calcule la résistance pour une LED rouge (2 V, 20 mA) alimentée en 5 V.

??? success "Réponse"
    $V_R = 5 - 2 = 3\,\mathrm{V}$ ; $R = \dfrac{3}{0{,}02} = 150\,\Omega$. 150 Ω est une valeur normalisée.

**Q2.** Calcule la résistance pour une LED verte (2,1 V, 20 mA) alimentée en 12 V.

??? success "Réponse"
    $V_R = 12 - 2{,}1 = 9{,}9\,\mathrm{V}$ ; $R = \dfrac{9{,}9}{0{,}02} = 495\,\Omega$ ; valeur normalisée au-dessus : **510 Ω**.

**Q3.** Calcule la résistance pour une LED rouge (2 V, 20 mA) alimentée en 3,3 V.

??? success "Réponse"
    $V_R = 3{,}3 - 2 = 1{,}3\,\mathrm{V}$ ; $R = \dfrac{1{,}3}{0{,}02} = 65\,\Omega$ ; valeur normalisée au-dessus : **68 Ω**.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier de retirer $V_F$ : on calculerait $R = 9 / 0{,}02 = 450\,\Omega$, alors que la bonne valeur est 350 Ω.
> - Prendre une valeur **plus petite** que le résultat : la LED reçoit trop de courant.

> [!SUCCESS] 🧠 À retenir
> - $R = \dfrac{V_{alim} - V_F}{I_F}$, avec $I_F$ en ampères.
> - On choisit la valeur normalisée **juste au-dessus** du résultat.

---

## 4. Circuits série et circuits parallèle

### 4.1 Le circuit série

![Deux LED en série avec une résistance](images/led-serie.png)

**Règles du circuit série :**

| Paramètre | Comportement en série |
|---|---|
| **Courant I** | Identique partout : $I_{\mathrm{total}}$ = I_LED1 = I_LED2 |
| **Tension U** | Se répartit : $V_{\mathrm{alim}}$ = $V_{R}$ + V_F1 + V_F2 |
| **Si une LED grille** | Le circuit est coupé → toutes les LEDs s'éteignent |
| **Résistance R** | $R = \dfrac{V_{\mathrm{alim}} - V_{\mathrm{F1}} - V_{\mathrm{F2}}}{I_{\mathrm{F}}}$ |

**Exemple — 2 LEDs rouges en série sur 9 V :**

> R = (9 − 2 − 2) / 0,02 = 5 / 0,02 = **250 Ω → choisir 270 Ω**


> [!TIP] 💡 En clair
> **En série**, les composants forment **un seul chemin**, comme des personnes qui marchent en file indienne : **le même courant** traverse tout le monde, et **la tension se partage**. Si un maillon est coupé, **tout s'arrête**.
>
> **En parallèle**, le courant a **plusieurs chemins**, comme les voies d'une autoroute : **la tension est la même** sur chaque branche, et **le courant se partage**. Si une branche est coupée, **les autres continuent**.

### ✅ Vérifie que tu as compris

**Q1.** Deux LED rouges (2 V, 20 mA) sont en série sur 9 V. Calcule la résistance.

??? success "Réponse"
    $R = \dfrac{9 - 2 - 2}{0{,}02} = 250\,\Omega$ ; valeur normalisée : **270 Ω**.

**Q2.** Deux LED rouges sont en parallèle sur 9 V. Quel courant total faut-il ?

??? success "Réponse"
    $I_{total} = 2 \times 20 = 40\,\mathrm{mA}$ ; et $R = \dfrac{9 - 2}{0{,}04} = 175\,\Omega$ (valeur normalisée : 180 Ω).

**Q3.** Une LED grille. Dans quel montage les autres restent-elles allumées ?

??? success "Réponse"
    Dans le montage **en parallèle** : chaque LED a son propre chemin.

> [!SUCCESS] 🧠 À retenir
> - Série : **même courant**, la tension se partage, une panne coupe tout.
> - Parallèle : **même tension**, le courant se partage, les autres branches continuent.

---

### 4.2 Le circuit parallèle

![Deux LED en parallèle avec une résistance commune](images/led-parallele.png)

**Règles du circuit parallèle :**

| Paramètre | Comportement en parallèle |
|---|---|
| **Tension U** | Identique aux bornes de chaque LED : V_F1 = V_F2 |
| **Courant I** | Se divise : $I_{\mathrm{total}}$ = I_LED1 + I_LED2 |
| **Si une LED grille** | Les autres continuent à fonctionner |
| **Résistance R** | R = ($V_{\mathrm{alim}}$ − $V_{F}$) / $I_{\mathrm{total}}$ avec $I_{\mathrm{total}}$ = N × $I_{F}$ |

**Exemple — 2 LEDs rouges en parallèle sur 9 V :**

> $I_{\mathrm{total}}$ = 2 × 20 mA = 40 mA = 0,04 A  
> R = (9 − 2) / 0,04 = 7 / 0,04 = **175 Ω → choisir 180 Ω**

---

### 4.3 Tableau de comparaison série vs parallèle

| Critère | Série | Parallèle |
|---|---|---|
| Même courant partout | ✅ Oui | ❌ Non (se divise) |
| Même tension partout | ❌ Non (se divise) | ✅ Oui |
| Panne d'une LED | ⚠️ Tout s'éteint | ✅ Les autres restent allumées |
| Luminosité par LED | ✅ Identique si identiques | ✅ Identique si identiques |
| Exemple d'utilisation | Guirlandes anciennes | Éclairage LED moderne |

---

## 5. Lire une datasheet (fiche technique)

Une **datasheet** est le document officiel du fabricant. Elle contient toutes les valeurs limites à ne **jamais dépasser**.

### 5.1 Données essentielles à repérer

| Paramètre datasheet | Signification | Exemple LED rouge 5 mm |
|---|---|---|
| **$V_{F}$ (Forward Voltage)** | Tension de seuil en fonctionnement | 2,0 V typ. — 2,5 V max |
| **$I_{F}$ (Forward Current)** | Courant de fonctionnement normal | 20 mA |
| **$I_{\mathrm{FM}}$ (Peak Forward Current)** | Courant maximum instantané | 100 mA |
| **$V_{R}$ (Reverse Voltage)** | Tension inverse maximale tolérée | 5 V max |
| **$P_{D}$ (Power Dissipation)** | Puissance maximale dissipée | 65 mW |
| **λ (Wavelength)** | Longueur d'onde — couleur émise | 625 nm (rouge) |

> 📌 **Règle pratique** : On prend toujours la valeur **typique** (typ.) pour calculer, et on vérifie qu'on ne dépasse pas la valeur **maximale** (max).


> [!TIP] 💡 En clair
> Une **datasheet** est la « notice » du composant, écrite par le fabricant. Tu n'as pas besoin de tout lire : cherche **trois choses** :
>
> 1. la **tension directe** $V_F$ ;
> 2. le **courant normal** $I_F$ ;
> 3. les **valeurs maximales** à ne jamais dépasser.
>
> Pour calculer, on prend les valeurs **typiques** (« typ. ») ; on vérifie ensuite qu'on reste **sous les valeurs maximales** (« max »).

### ✅ Vérifie que tu as compris

**Q1.** Quelle valeur de la datasheet utilise-t-on pour calculer la résistance ?

??? success "Réponse"
    Les valeurs **typiques** de $V_F$ et de $I_F$.

**Q2.** Pourquoi ne prend-on pas $I_{FM} = 100\,\mathrm{mA}$ pour calculer ?

??? success "Réponse"
    C'est un courant **maximal instantané**, jamais un courant de fonctionnement normal : on utilise $I_F = 20\,\mathrm{mA}$.

---

## 6. Utilisation du multimètre

![Multimètre numérique annoté](images/multimetre.png)

| Mesure | Position sélecteur | Branchement | Unité lue |
|---|---|---|---|
| Tension continue | **DCV** (choisir calibre > U mesurée) | **En parallèle** avec l'élément | Volts (V) |
| Courant continu | **DCA** | **En série** dans le circuit | Ampères (A) ou mA |
| Résistance | **Ω** | **Hors circuit** (composant non alimenté) | Ohms (Ω) |
| Continuité | Symbole **))) ou 🔊** | En série | Bip si continuité |
| Test diode | Symbole **→|** | Anode sur rouge, cathode sur noir | Affiche $V_{F}$ |


> [!TIP] 💡 En clair
> Le multimètre se branche **différemment** selon ce qu'on mesure. Pour t'en souvenir :
>
> - **Tension** : en **parallèle** (on mesure « entre deux points »).
> - **Courant** : en **série** (le courant doit **traverser** l'appareil).
> - **Résistance** : **hors tension**, composant sorti du circuit.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Brancher l'ampèremètre **en parallèle** : on crée un court-circuit et on peut détruire l'appareil.
> - Mesurer une résistance alors que le circuit est alimenté : la mesure est fausse.

### ✅ Vérifie que tu as compris

**Q1.** Comment branche-t-on le multimètre pour mesurer la tension aux bornes d'une LED ?

??? success "Réponse"
    **En parallèle** de la LED, en mode tension continue (DCV).

**Q2.** Pour mesurer le courant dans le circuit, où place-t-on l'ampèremètre ?

??? success "Réponse"
    **En série** : on ouvre le circuit et on y intercale l'appareil.

**Q3.** Peut-on mesurer la valeur d'une résistance dans un circuit alimenté ?

??? success "Réponse"
    Non : il faut couper l'alimentation et, si possible, sortir la résistance du circuit.

> [!SUCCESS] 🧠 À retenir
> - V en parallèle, A en série, Ω hors tension.

---

## 📝 Fiche mémo — À garder dans le portfolio

| Je dois... | La formule / règle |
|---|---|
| Calculer R pour une LED | $R = \dfrac{V_{\mathrm{alim}} - V_{\mathrm{F}}}{I_{\mathrm{F}}}$ |
| Trouver I en circuit série | **I identique partout** |
| Trouver U en circuit série | **$V_{\mathrm{total}}$ = somme des tensions** |
| Trouver U en circuit parallèle | **V identique aux bornes de chaque branche** |
| Convertir 20 mA en A | **÷ 1000 → 0,02 A** |
| Reconnaître l'anode | **Broche la plus longue** |
| Choisir une valeur E24 | **Valeur normalisée supérieure la plus proche** |

---

## ✅ Compétences RNCP travaillées dans ce cours

| Code | Compétence | Niveau |
|---|---|---|
| C2.1 | Préparer les ressources matérielles à la réalisation | ⭐⭐ Application |
| C2.2 | Réaliser des câblages et montages à partir d'un schéma | ⭐⭐ Application |
| C3.1 | Rendre compte de son activité par écrit | ⭐ Découverte |
| S2 | Électricité — Loi d'Ohm, dipôles, circuits | ⭐⭐⭐ Maîtrise |
| S3 | Composants électroniques — diodes, LED | ⭐⭐ Application |

---

*BAC Pro CIEL — S2 Module E2 | MFR de Pontonx | © Yahn LE PRETTRE*
