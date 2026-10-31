# Semaine 4 : Lire un schéma et une datasheet, monter sur plaque d'essai

> **Durée** : 4 h · **Compétence E2** : C07

## 🎯 À la fin de la semaine, je sais…

- **lire un schéma** normalisé et le découper en blocs ;
- **trouver dans une datasheet** le brochage, les limites et les valeurs utiles, et les utiliser dans un calcul ;
- **monter un circuit** sur plaque d'essai à partir d'un schéma, puis le **vérifier** avant de l'alimenter ;
- **tester des composants** hors tension avec le multimètre.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | TP virtuels ElectroLab (test des composants, NE555 en astable) |
| 1 h | Cours : lire un schéma, lire une datasheet |
| 1 h | Cours : trois composants clés ; de la datasheet au calcul |
| 1 h | Atelier réel : monter sur plaque d'essai et vérifier |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾** :

- **Tester les composants hors tension (ohmmètre, diode, continuité)** (1 h) : tu apprends à reconnaître un composant en panne.
- **NE555 en multivibrateur astable (4 fréquences)** (1 h 30) : tu vérifies la formule de la fréquence.

---

## 📖 Le cours

**🤔 À ton avis ?** On te donne une carte inconnue avec un composant marqué « LM7805 ». Comment savoir comment le brancher sans rien griller ?

??? question "Réponse"
    On lit sa **datasheet** (la notice du fabricant) et le **schéma** de la carte. Cette semaine, tu apprends à lire ces deux documents.

### 1. Lire un schéma

Un schéma est un **plan** : il montre **comment les composants sont reliés**, pas où ils sont posés.

![Symboles normalisés des composants courants](images/symboles-de-base.png)

- Chaque composant a un **repère** : **R**1 (résistance), **C**1 (condensateur), **D**1 (diode), **Q**1 (transistor), **U**1 (circuit intégré), **J**1 (connecteur).
- Les **traits** sont des fils. Un **point plein** à un croisement veut dire « relié » ; **sans point**, les fils ne sont pas reliés.
- Par convention : le **+** en haut, la **masse (GND)** en bas, le signal de **gauche à droite**.

![Schéma électrique et montage sur plaque d'essai : un même circuit, deux représentations](images/schema-vs-montage.png)

> [!TIP] 💡 Méthode : lire un schéma en 4 temps
> 1. **Repérer l'alimentation** (d'où vient le +, où est la masse).
> 2. **Découper en blocs** (alimentation, traitement, sortie).
> 3. **Suivre le signal** de gauche à droite, bloc par bloc.
> 4. **Chercher le rôle de chaque composant** (limiter un courant, filtrer, protéger).

**Exemple** : sur un schéma « pile 9 V → 7805 → LED + résistance », le bloc 1 abaisse la tension à 5 V, le bloc 2 limite le courant à environ 20 mA, le bloc 3 est la LED qui éclaire.

### 2. Lire une datasheet

Une datasheet contient toujours les mêmes parties.

![Datasheet annotée : où trouver quoi](images/datasheet-annotee.png)

| À chercher | Pourquoi |
|---|---|
| **Brochage** (*pin configuration*) | brancher chaque broche au bon endroit |
| **Absolute maximum ratings** | limites à **ne jamais dépasser** |
| **Electrical characteristics** (min / typ / max) | valeurs **garanties**, pour calculer |
| **Package** | choisir l'empreinte du circuit imprimé |

> [!TIP] 💡 Min, typ, max
> Les valeurs **garanties** sont **min** et **max**. La valeur « typique » est ce qu'on mesure en général, **sans garantie**. Pour un calcul de sécurité, on prend **le cas le plus défavorable**.

![Limites absolues du transistor BC547](images/ratings-bc547.png)

**Exemple de lecture** : pour le BC547, la datasheet donne $h_{FE}$ entre **110 et 800**. Pour être sûr que le transistor sature, on calcule le courant de base avec une règle **prudente** ($I_B = I_C/10$) et non avec la valeur typique.

### 3. Trois composants à connaître

**Le régulateur 7805** : sortie **5 V** (garantie de 4,8 à 5,2 V), entrée de **7 V à 35 V maximum**.

![Brochage du régulateur 7805](images/brochage-7805.png)

**Le transistor BC547** : $V_{CE}$ max = 45 V ; $I_C$ max = 100 mA ; gain $h_{FE}$ de 110 à 800 (très dispersé) ; saturé : $V_{CE(sat)} \approx 0{,}2\,\mathrm{V}$.

**Le NE555** en astable :

$$f = \frac{1{,}44}{(R_a + 2R_b) \times C} \qquad DC = \frac{R_a + R_b}{R_a + 2R_b}$$

![Brochage du NE555](images/brochage-ne555.png)

Avec $R_a = 10\,\mathrm{kΩ}$, $R_b = 68\,\mathrm{kΩ}$, $C = 10\,\mathrm{\mu F}$ : $f \approx 0{,}99\,\mathrm{Hz}$ et $DC \approx 53\,\%$. C'est le **clignoteur** que tu vas construire pendant le parcours.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Utiliser la datasheet du **mauvais composant** (vérifie la référence exacte et le fabricant).
> - Confondre **limite absolue** et **valeur de fonctionnement**.
> - Lire le brochage **vu du dessous** au lieu de vu du dessus.

**Exercice guidé : de la datasheet au calcul.** On veut alimenter une LED rouge (tension directe $V_F \approx 2\,\mathrm{V}$, courant 15 mA) depuis la sortie 5 V du 7805.

1. Tension aux bornes de la résistance : $5 - 2 = 3\,\mathrm{V}$.
2. $R = \dfrac{3}{0{,}015} = 200\,\Omega$ → on choisit **220 Ω** (valeur normalisée supérieure).
3. Courant réel : $I = \dfrac{3}{220} \approx 13{,}6\,\mathrm{mA}$, très en dessous de la limite de la LED (20 mA).
4. Puissance dans la résistance : $P = R I^2 = 220 \times 0{,}0136^2 \approx 0{,}04\,\mathrm{W}$, donc une résistance **1/4 W** suffit largement.

### 4. La plaque d'essai

Sur une plaque d'essai (*breadboard*), les trous d'une **même colonne de 5** sont reliés ; les **rails** (lignes + et −) courent sur toute la longueur. On monte un circuit **sans souder**, pour le tester.

![Plaque d'essai : colonnes reliées et rails d'alimentation](images/breadboard.png)

![Câblage correct et câblage erroné sur une plaque d'essai](images/cablage-ok-ko.png)

> [!TIP] 💡 Méthode de montage
> 1. Relier les rails +5 V et GND. 2. Poser les composants **dans l'ordre du schéma**. 3. **Vérifier avant d'alimenter** : sens des LED, polarité des condensateurs, absence de court-circuit entre + et −.

### 5. Vérifier un montage avant de l'alimenter

Avant de brancher l'alimentation, on fait **trois contrôles** au multimètre, **hors tension** :

| Contrôle | Réglage | Résultat attendu |
|---|---|---|
| Absence de court-circuit entre + et − | **continuité** | **aucun bip** (circuit ouvert) |
| Une liaison prévue | **continuité** | **bip** |
| Une résistance en place | **ohmmètre** | valeur proche du marquage (± tolérance) |

![Test de continuité au multimètre](images/continuite-multimetre.png)

> [!WARNING] ⚠️ Un bip entre + et − avant d'alimenter
> Il y a un **court-circuit** : on **n'alimente pas**. On cherche d'abord un fil mal placé ou un composant monté à l'envers.

### 6. Reconnaître un composant défectueux

| Composant | Test hors tension | Valeur d'un composant **bon** | Signe d'un composant **mauvais** |
|---|---|---|---|
| Résistance | ohmmètre | marquage ± tolérance | valeur très supérieure (coupée) ou nulle |
| Diode / LED | test diode | 0,5 à 0,7 V dans un sens (LED : environ 1,8 V), **OL** dans l'autre | **OL** dans les deux sens (coupée) ou **bip** dans les deux (court-circuit) |
| Condensateur | ohmmètre | la valeur monte puis se stabilise (charge) | **0 Ω** durable (en court-circuit) |

---

## 🛠️ Atelier réel

**Matériel** : plaque d'essai, alimentation 5 V, LED, résistance 220 Ω, 3 résistances, multimètre, datasheet du 7805.

1. Ouvre la datasheet du **7805** : note la tension d'entrée maximale, la sortie, et le brochage.
2. Mesure les **3 résistances** à l'ohmmètre et indique leur écart avec le marquage.
3. Monte sur la plaque : alimentation 5 V → résistance 220 Ω → LED → masse. **Vérifie hors tension** (continuité), puis alimente.
4. Mesure la **tension aux bornes de la résistance** et calcule le courant.
5. **Dessine** le schéma de ce que tu viens de monter, avec les repères et les valeurs.
6. Provoque une panne volontaire (LED à l'envers) : que constates-tu ? Comment la diagnostiques-tu ?

??? success "Résultats attendus"
    1. Entrée maximale **35 V**, sortie **5 V** ; broches : 1 entrée, 2 masse, 3 sortie.
    2. Les trois valeurs sont dans la tolérance du marquage (± 5 % pour la bande or).
    3. La LED s'allume.
    4. Environ **3 V** aux bornes de la résistance ; $I \approx 13{,}6\,\mathrm{mA}$.
    5. Schéma : source 5 V, R1 = 220 Ω, D1, masse.
    6. **La LED reste éteinte** : en inverse, elle est bloquée. Au test diode, on lit **OL** dans le sens où elle devrait conduire. On la retourne.

## ✍️ Exercices

1. Un 7805 est alimenté en 7,5 V. Peut-il réguler à 5 V ? Et en 6 V ? (chute minimale d'environ 2 V)
2. NE555 : $R_a = 4{,}7\,\mathrm{kΩ}$, $R_b = 33\,\mathrm{kΩ}$, $C = 10\,\mathrm{\mu F}$. Quelle fréquence ?
3. Pourquoi calcule-t-on avec les limites de la datasheet plutôt qu'avec les valeurs typiques ?
4. Deux fils se croisent sur un schéma, sans point : sont-ils reliés ?
5. Une LED rouge ($V_F = 2\,\mathrm{V}$) doit recevoir 10 mA depuis 5 V. Quelle résistance normalisée choisis-tu ?
6. Au test de continuité, tu entends un bip entre le + et le − du montage. Que fais-tu ?

??? success "Corrigés"
    1. À 7,5 V : **oui** (7,5 − 5 = 2,5 V ≥ 2 V). À 6 V : **non** (1 V < 2 V).
    2. $f = \dfrac{1{,}44}{(4{,}7 + 66) \times 10^{3} \times 10^{-5}} \approx 2{,}04\,\mathrm{Hz}$.
    3. Pour que le montage fonctionne dans le **cas le plus défavorable** (composant le moins favorable, température extrême).
    4. **Non** : seul un **point plein** indique une liaison.
    5. $R = \dfrac{3}{0{,}01} = 300\,\Omega$ → **330 Ω** (valeur normalisée supérieure).
    6. **Je n'alimente pas** : il y a un court-circuit. Je repère le fil ou le composant en cause.

## ✅ Auto-test

1. Que signifie « absolute maximum ratings » ?
2. Quelle est la tension d'entrée maximale d'un 7805 ?
3. Combien de trous sont reliés dans une colonne d'une plaque d'essai ?
4. Quel contrôle fait-on avant d'alimenter un montage ?

??? success "Réponses"
    1. Les limites à **ne jamais dépasser** : au-delà, le composant peut être détruit.
    2. **35 V**.
    3. **5 trous**.
    4. Un test de **continuité** : aucun bip entre + et −.

## 📦 Livrable

Fiche de synthèse d'une datasheet (brochage, limites, valeurs utiles) et schéma du montage réalisé avec ses mesures.

> [!NOTE] 📚 Pour approfondir (facultatif)
> Ce parcours se suffit à lui-même. Pour aller plus loin : Seconde S03 (breadboard, schémas) et S06 (lecture de datasheet) ; Première S01 (« Lire une datasheet »).
