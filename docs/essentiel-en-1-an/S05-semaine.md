# Semaine 5 : Microcontrôleur, capteurs et traitement du signal

> **Durée** : 4 h · **Compétences E2 travaillées** : C07 · C11

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Écrire et lire un programme Arduino simple (entrées, sorties, moniteur série).
- Lire un capteur analogique (LM35) et convertir en grandeur physique.
- Produire un signal PWM.
- Filtrer un signal (filtre RC), amplifier (AOP) et lire une table de vérité.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Programme Arduino : sorties, entrées, bouton |
| 1 h | Capteur LM35 : lecture et conversion |
| 1 h | TP virtuels ElectroLab : AOP, filtre RC, portes ; conditionnement du signal |
| 1 h | Exercices et auto-test |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾**, puis fais ces TP **avant** de toucher au matériel :

- **Amplificateur inverseur à AOP : gain et saturation** (1 h 30, niveau terminale)
- **Filtre RC passe-bas : gain et fréquence de coupure** (1 h 30, niveau terminale)
- **Portes logiques : tables de vérité, alimentation, CMOS / TTL** (1 h 15, niveau première)
- **Diviseur de tension et influence du voltmètre** (1 h, niveau première)

> [!TIP] 🖥️ Pourquoi d'abord le simulateur ?
> On peut se tromper sans rien casser, répéter autant de fois que nécessaire et obtenir une correction automatique. Le TP réel sert ensuite à **confirmer** et à manipuler le vrai matériel.

## 📖 Le cours en bref

**🤔 À ton avis ?** Un capteur délivre une tension de 0,25 V. Comment l'Arduino peut-il en faire « 25 °C » sur un écran ?

??? question "Réponse"
    Il **convertit** la tension en nombre (ADC), puis le programme applique une **formule**. On va apprendre chaque étape.

### 1. Programmer un microcontrôleur : Arduino / ESP32

Un **microcontrôleur** est un petit ordinateur sur une puce : il lit des **entrées**, exécute un **programme** et pilote des **sorties**. Un programme Arduino (« sketch ») a deux parties :

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
| `analogWrite(p, 0…255)` | signal **PWM** (rapport cyclique) |
| `Serial.println(x)` | afficher x sur le moniteur série |

> [!TIP] 💡 Bouton poussoir
> Avec `INPUT_PULLUP`, une résistance interne tire l'entrée à 5 V : le bouton relié à la masse donne **LOW quand on appuie**.

### 2. Lire un capteur : conversion analogique-numérique

Le convertisseur **ADC** de l'Arduino a **10 bits** : $2^{10} = 1\,024$ valeurs (0 à 1023) pour 0 à 5 V. Un pas vaut $\dfrac{5}{1023} \approx 4{,}9\,\mathrm{mV}$.

$$U = \text{valeur} \times \frac{5}{1023}$$

**Capteur de température LM35** : **10 mV par °C**, donc $T = U \times 100$.

```cpp
void loop() {
  int brut = analogRead(A0);
  float tension = brut * 5.0 / 1023.0;
  float temperature = tension * 100.0;
  Serial.println(temperature);
  delay(1000);
}
```

**Exemple** : `brut = 51` → $U \approx 0{,}249\,\mathrm{V}$ → $T \approx 24{,}9\,°\mathrm{C}$. Un pas de l'ADC (4,9 mV) correspond à environ 0,5 °C : c'est la **résolution** de la mesure.

**PWM** : `analogWrite(9, 64)` donne un rapport cyclique de $\dfrac{64}{255} \approx 25\,\%$ à environ 490 Hz.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier `Serial.begin(9600)` ou régler le moniteur sur une autre vitesse : texte illisible.
> - Diviser des entiers (`brut / 1023`) : le résultat est tronqué. Écrire `1023.0`.
> - Brancher le capteur sur une broche **numérique** au lieu d'une entrée **analogique** (A0…).

### 3. Traiter le signal : filtre, amplificateur, logique

Montage **non inverseur** : $G = 1 + \dfrac{R_f}{R_g}$. **Exemple** : $R_f = 10\,\mathrm{k\Omega}$, $R_g = 1\,\mathrm{k\Omega}$ → $G = 11$ : 100 mV en entrée donnent 1,1 V en sortie. La sortie ne dépasse jamais l'alimentation.

$$f_c = \frac{1}{2\pi R C}$$

Il laisse passer les **basses fréquences** et atténue les **hautes**. **Exemple** : 10 kΩ et 100 nF → $f_c \approx 159\,\mathrm{Hz}$.

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


## 🛠️ Atelier guidé : on construit, on mesure, on valide

**Fil rouge 2 : la station de mesure.** Matériel : Arduino (ou ESP32), capteur LM35, LED, bouton.

1. Câble la **LED** sur la broche 13 avec une résistance de 220 Ω. Téléverse le programme de clignotement (500 ms).
2. Câble le **bouton** entre la broche 2 et la masse (`INPUT_PULLUP`) : la LED s'allume tant qu'on appuie.
3. Câble le **LM35** (+5 V, A0, GND). Écris le programme de lecture et affiche la température sur le moniteur série (9600 bauds).
4. Change la fréquence de clignotement : combien de clignotements par seconde pour `delay(250)` ?
5. Pose la LED sur une broche PWM (9) et fais varier l'intensité avec `analogWrite`.

??? success "Résultats attendus"
    1. La LED clignote à **1 Hz** (500 ms allumée + 500 ms éteinte).
    2. LED allumée **quand on appuie** (le bouton relié à la masse donne LOW).
    3. Environ la **température ambiante** (par exemple 22 à 25 °C) ; elle monte si on touche le capteur.
    4. Période 500 ms → **2 clignotements par seconde**.
    5. Intensité proportionnelle au rapport cyclique ($64/255 \approx 25\,\%$ : faible ; 255 : maximale).

## ✍️ Exercices d'application

1. Combien de valeurs distinctes peut renvoyer `analogRead` ?
2. `brut = 102` sur un LM35 : température ?
3. Pourquoi écrire `1023.0` plutôt que `1023` ?
4. Un AOP non inverseur a $R_f = 10\,\mathrm{k\Omega}$, $R_g = 1\,\mathrm{k\Omega}$ : gain ?

??? success "Corrigés"
    1. $2^{10} = 1\,024$ valeurs (0 à 1023).
    2. $U \approx 0{,}50\,\mathrm{V}$ ; $T \approx 49{,}9\,°\mathrm{C}$.
    3. Pour forcer un calcul **décimal** ; avec des entiers le résultat est tronqué.
    4. $G = 1 + 10 = 11$.

## 📚 Pour approfondir : les séances à consulter

- [Seconde S07 – structure d'un sketch](../seconde/S07-arduino-ide-structure-du-sketch-led/01-cours.md)
- [Seconde S08 – entrées numériques](../seconde/S08-e-s-numeriques-bouton-led-pull-up-pull/01-cours.md)
- [Seconde S09 – capteur LM35](../seconde/S09-capteur-lm35-analogread-et-conversion/01-cours.md)
- [Première S12 – AOP, filtre RC, portes logiques](../premiere/S12-prototypes-avances-integration/04-aop-filtre-logique.md)

## ✅ Auto-test

1. Que fait `analogRead(A0)` ? Quelle plage de valeurs ?
2. `analogRead` renvoie 102 pour un LM35 : quelle température ?
3. Quel rapport cyclique donne `analogWrite(9, 128)` ?
4. Avec `INPUT_PULLUP`, que lit-on quand on appuie sur le bouton relié à la masse ?
5. Fréquence de coupure d'un filtre RC (10 kΩ, 100 nF) ?

??? success "Réponses"
    1. Il lit une tension de 0 à 5 V et renvoie un nombre de **0 à 1023**.
    2. $U = 102 \times \dfrac{5}{1023} \approx 0{,}50\,\mathrm{V}$ ; $T \approx 49{,}9\,°\mathrm{C}$.
    3. $\dfrac{128}{255} \approx 50\,\%$.
    4. **LOW** (0).
    5. $\dfrac{1}{2\pi RC} \approx 159\,\mathrm{Hz}$.

## 📦 Livrable

Programme commenté qui lit un capteur de température et affiche la valeur en °C sur le moniteur série.
