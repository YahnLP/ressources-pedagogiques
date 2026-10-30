# Semaine 6 : Microcontrôleur, capteurs et traitement du signal

> **Durée** : 4 h · **Compétences E2** : C07, C11

## 🎯 À la fin de la semaine, je sais…

- écrire et lire un **programme Arduino** simple (entrées, sorties, moniteur série) ;
- **lire un capteur analogique** (LM35) et convertir la valeur en grandeur physique ;
- produire un signal **PWM** ;
- **filtrer** un signal (filtre RC), l'**amplifier** (AOP) et lire une **table de vérité**.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | TP virtuels ElectroLab (AOP, filtre RC, portes, diviseur) |
| 1 h 15 | Cours : programme Arduino, entrées et sorties |
| 1 h | Cours : capteur LM35 et conversion ; filtre, AOP, logique |
| 45 min | Atelier réel et auto-test |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾** :

- **Amplificateur inverseur à AOP : gain et saturation** (1 h 30)
- **Filtre RC passe-bas : gain et fréquence de coupure** (1 h 30)
- **Portes logiques : tables de vérité, alimentation, CMOS / TTL** (1 h 15)
- **Diviseur de tension et influence du voltmètre** (1 h)

---

## 📖 Le cours

**🤔 À ton avis ?** Un capteur délivre une tension de 0,25 V. Comment l'Arduino peut-il en faire « 25 °C » sur un écran ?

??? question "Réponse"
    Il **convertit** la tension en un nombre (convertisseur ADC), puis le programme applique une **formule**. On apprend chaque étape.

### 1. Un microcontrôleur, c'est quoi ?

Un **microcontrôleur** est un petit ordinateur sur une puce : il lit des **entrées**, exécute un **programme** et pilote des **sorties**. Les cartes **Arduino Uno** (5 V) ou **ESP32** (3,3 V) en sont équipées.

![Carte Arduino Uno annotée : broches numériques, entrées analogiques, alimentation](images/arduino-uno-annote.png)

### 2. Le programme : `setup()` et `loop()`

![Structure d'un programme : setup une fois, loop en boucle](images/setup-loop.png)

```cpp
void setup() {            // exécuté UNE fois au démarrage
  pinMode(13, OUTPUT);    // broche 13 = sortie
  Serial.begin(9600);     // moniteur série à 9600 bauds
}
void loop() {             // répété en boucle
  digitalWrite(13, HIGH); // sortie à 5 V
  delay(500);             // attendre 500 ms
  digitalWrite(13, LOW);
  delay(500);
}
```

| Instruction | Rôle |
|---|---|
| `pinMode(p, OUTPUT / INPUT / INPUT_PULLUP)` | choisir le rôle d'une broche |
| `digitalWrite(p, HIGH / LOW)` | mettre une sortie à 5 V / 0 V |
| `digitalRead(p)` | lire une entrée (HIGH ou LOW) |
| `analogRead(A0)` | lire une tension de 0 à 5 V : nombre de **0 à 1023** |
| `analogWrite(p, 0…255)` | signal **PWM** |
| `Serial.println(x)` | afficher x sur le moniteur série |

![Montage d'une LED sur la broche 13 avec sa résistance](images/schema-led-d13.png)

**Bouton poussoir** : avec `INPUT_PULLUP`, une résistance interne tire l'entrée à 5 V. Le bouton relié à la masse donne **LOW quand on appuie**.

![Entrée avec résistance de rappel (pull-up / pull-down)](images/pulldown-pullup.png)

![Le moniteur série de l'environnement Arduino](images/serial-monitor-ide.png)

### 3. Lire un capteur : la conversion analogique-numérique

Le convertisseur **ADC** de l'Arduino a **10 bits** : $2^{10} = 1\,024$ valeurs (0 à 1023) pour 0 à 5 V. Un pas vaut $\dfrac{5}{1023} \approx 4{,}9\,\mathrm{mV}$.

![Conversion analogique-numérique : de la tension à la valeur](images/adc-conversion.png)

$$U = \text{valeur} \times \frac{5}{1023}$$

**Capteur de température LM35** : **10 mV par °C**, donc $T = U \times 100$.

![Brochage du capteur LM35](images/lm35-brochage.png)

![Câblage du LM35 sur l'Arduino](images/cablage-lm35.png)

```cpp
void loop() {
  int brut = analogRead(A0);
  float tension = brut * 5.0 / 1023.0;
  float temperature = tension * 100.0;
  Serial.println(temperature);
  delay(1000);
}
```

**Exemple** : `brut = 51` → $U \approx 0{,}249\,\mathrm{V}$ → $T \approx 24{,}9\,°\mathrm{C}$. Un pas de l'ADC correspond à environ 0,5 °C : c'est la **résolution** de la mesure.

**PWM** : `analogWrite(9, 64)` donne un rapport cyclique de $\dfrac{64}{255} \approx 25\,\%$ à environ 490 Hz.

### 4. Filtrer et amplifier un signal

**Le filtre RC passe-bas** laisse passer les basses fréquences et atténue les hautes :

$$f_c = \frac{1}{2\pi R C}$$

![Réponse d'un filtre RC passe-bas : gain en fonction de la fréquence](images/ess_rc_bode.png)

**L'amplificateur opérationnel** (AOP) amplifie un petit signal. En montage **non inverseur** : $G = 1 + \dfrac{R_f}{R_g}$.

![Montage non inverseur d'un amplificateur opérationnel](images/ess_aop.png)

### 5. La logique

Les circuits numériques ne connaissent que **0** (≈ 0 V) et **1** (≈ 5 V ou 3,3 V).

![Niveaux logiques et zone interdite](images/niveaux-logiques.png)

| A | B | ET | OU | NON-ET |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier `Serial.begin(9600)` ou régler le moniteur sur une autre vitesse : texte illisible.
> - Diviser des entiers (`brut / 1023`) : le résultat est tronqué. Écrire `1023.0`.
> - Brancher un capteur analogique sur une broche **numérique** au lieu de A0…
> - Alimenter un AOP en 5 V en attendant une sortie de 8 V.

---

## 🛠️ Atelier réel : la station de mesure

**Fil rouge 2.** Matériel : Arduino (ou ESP32), LM35, LED, bouton, résistance 220 Ω.

1. Câble la **LED** sur la broche 13 avec 220 Ω. Téléverse le programme de clignotement (500 ms).
2. Câble le **bouton** entre la broche 2 et la masse (`INPUT_PULLUP`) : la LED s'allume tant qu'on appuie.
3. Câble le **LM35** (+5 V, A0, GND). Écris le programme de lecture et affiche la température sur le moniteur série (9600 bauds).
4. Combien de clignotements par seconde avec `delay(250)` ?
5. Place la LED sur une broche PWM (9) et fais varier l'intensité avec `analogWrite`.

??? success "Résultats attendus"
    1. La LED clignote à **1 Hz**.
    2. LED allumée **quand on appuie** (bouton relié à la masse : LOW).
    3. La **température ambiante** (par exemple 22 à 25 °C), qui monte si on touche le capteur.
    4. Période 500 ms → **2 clignotements par seconde**.
    5. Intensité proportionnelle au rapport cyclique ($64/255 \approx 25\,\%$ : faible ; 255 : maximale).

## ✍️ Exercices

1. Combien de valeurs distinctes peut renvoyer `analogRead` ?
2. `analogRead` renvoie 102 pour un LM35 : quelle température ?
3. Quel rapport cyclique donne `analogWrite(9, 128)` ?
4. Avec `INPUT_PULLUP`, que lit-on quand le bouton relié à la masse est appuyé ?
5. Gain d'un AOP non inverseur avec $R_f = 10\,\mathrm{kΩ}$ et $R_g = 1\,\mathrm{kΩ}$ ? Fréquence de coupure d'un filtre RC (10 kΩ, 100 nF) ?

??? success "Corrigés"
    1. $2^{10} = 1\,024$ valeurs (0 à 1023).
    2. $U = 102 \times \dfrac{5}{1023} \approx 0{,}50\,\mathrm{V}$ ; $T \approx 49{,}9\,°\mathrm{C}$.
    3. $\dfrac{128}{255} \approx 50\,\%$.
    4. **LOW** (0).
    5. $G = 1 + 10 = 11$ ; $f_c = \dfrac{1}{2\pi \times 10^{4} \times 10^{-7}} \approx 159\,\mathrm{Hz}$.

## ✅ Auto-test

1. Que fait `analogRead(A0)` ?
2. Pourquoi écrire `5.0 / 1023.0` ?
3. Que font les basses fréquences dans un filtre RC passe-bas ?
4. Sortie d'une porte NON-ET avec A = 1 et B = 1 ?

??? success "Réponses"
    1. Il lit une tension de 0 à 5 V et renvoie un nombre de **0 à 1023**.
    2. Pour forcer un calcul **décimal**.
    3. Elles **passent** ; les hautes fréquences sont atténuées.
    4. **0**.

## 📦 Livrable

Programme commenté qui lit un capteur de température et affiche la valeur en °C sur le moniteur série.

> [!NOTE] 📚 Pour approfondir (facultatif)
> Ce parcours se suffit à lui-même. Pour aller plus loin : Seconde S07 à S09 (Arduino, entrées numériques, LM35) et Première S12 (AOP, filtre RC, portes logiques).
