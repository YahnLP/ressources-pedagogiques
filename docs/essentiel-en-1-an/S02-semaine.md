# Semaine 2 : Mesurer : multimètre, alimentation, générateur et oscilloscope

> **Durée** : 4 h · **Compétences E2 travaillées** : C07 · C11

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Mesurer une tension, un courant, une résistance, une continuité.
- Régler une alimentation de labo (tension et limite de courant).
- Régler un générateur de fonctions (forme, fréquence, amplitude).
- Régler un oscilloscope (VOLT/DIV, SEC/DIV, déclenchement) et lire amplitude, période, fréquence.
- Choisir le bon instrument selon la grandeur.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Multimètre : tension, courant, résistance, continuité |
| 1 h | Alimentation de labo et générateur de fonctions |
| 1 h | Oscilloscope : signal de test, sonde ×10, PWM, LED qui clignote |
| 1 h | Atelier chronométré et auto-test (passeport instruments) |

## 📖 Le cours en bref

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

## 🛠️ Atelier guidé : on construit ensemble le clignoteur

**Fil rouge** : tu réutilises ton montage LED, et tu apprends à **l'alimenter et le mesurer proprement**.

1. **Alimentation de labo** : règle **5,0 V** et une **limite de courant de 30 mA**, sortie coupée. Mesure la tension à vide au multimètre.
2. **Branche** le montage LED. Lis le courant affiché par l'alimentation, puis **vérifie-le** avec le multimètre en série.
3. **Générateur** : règle un signal **carré, 1 kHz, 3 V crête à crête**. Branche-le à l'oscilloscope (sonde ×10 compensée).
4. **Relève** période, fréquence, $U_{pp}$.
5. Règle un **rapport cyclique de 25 %** et relève $t_{haut}$ sur l'écran.
6. Ajoute un **offset** de 1,5 V, puis passe l'oscilloscope en couplage **AC** : que se passe-t-il ?

??? success "Résultats attendus"
    1. Environ 5,00 V à vide.
    2. Environ 20 mA, mode **CV** (le voyant CC ne s'allume pas).
    3. et 4. $T = 1\,\mathrm{ms}$, $f = 1\,\mathrm{kHz}$, $U_{pp} = 3\,\mathrm{V}$.
    5. $t_{haut} = 0{,}25 \times 1\,\mathrm{ms} = 0{,}25\,\mathrm{ms}$.
    6. L'offset décale tout le signal vers le haut ; en **AC**, le signal **se recentre sur zéro** (la composante continue est supprimée).

## ✍️ Exercices d'application

1. Période de 8 carreaux à 0,5 ms/DIV : quelle fréquence ?
2. Une sonde ×10 est utilisée, mais la voie est restée réglée sur ×1. L'écran indique 1,2 V crête à crête : quelle est la vraie valeur ?
3. Un signal est à l'état haut 3 ms sur une période de 12 ms. Rapport cyclique ?
4. Multimètre ±(0,5 % + 2 chiffres), lecture 12,00 V (résolution 0,01 V). Quelle marge ?

??? success "Corrigés"
    1. $T = 4\,\mathrm{ms}$ ; $f = 250\,\mathrm{Hz}$.
    2. Le signal est atténué 10 fois : la vraie valeur est **12 V**.
    3. $\dfrac{3}{12} = 25\,\%$.
    4. $0{,}5\,\% \times 12 = 0{,}06$ ; 2 chiffres = 0,02 ; marge = **0,08 V** → $(12{,}00 \pm 0{,}08)\,\mathrm{V}$.

## 📚 Pour approfondir : les séances à consulter

- [Seconde S12 – tests au multimètre](../seconde/S12-tests-au-multimetre-et-controle-qualite/01-cours.md)
- [Seconde S12 – prise en main de l'oscilloscope](../seconde/S12-tests-au-multimetre-et-controle-qualite/05-prise-en-main-oscilloscope.md)
- [Seconde S12 – alimentation de labo et générateur](../seconde/S12-tests-au-multimetre-et-controle-qualite/06-alimentation-labo-et-generateur.md)
- [Première S05 – TP instruments avancés](../premiere/S05-tests-mesures-avances-oscilloscope/05-tp-instruments-avances.md)
- [Terminale S01 – circuit fourni](../terminale/S01-circuit-fourni-multimetre-oscilloscope/README.md)
- [Passeport instruments](passeport-instruments.md)

## ✅ Auto-test

1. Comment branche-t-on un ampèremètre ? Un voltmètre ?
2. Une période occupe 4 carreaux à 5 ms/DIV. Quelle fréquence ?
3. Dans quelles conditions mesure-t-on une résistance ?
4. Que fait le couplage AC ?
5. Que vérifier avant de brancher la sonde ?
6. Que règle-t-on sur une alimentation de labo avant de brancher le montage ?
7. Le voyant CC est allumé : que signifie-t-il ?

??? success "Réponses"
    1. L'ampèremètre en **série**, le voltmètre en **parallèle**.
    2. $T = 20\,\mathrm{ms}$ ; $f = 50\,\mathrm{Hz}$.
    3. **Hors tension** et, si possible, **hors circuit**.
    4. Il supprime la **composante continue** pour voir la variation.
    5. Qu'elle est déclarée en **×10** et que la masse est sur la **masse du circuit**.
    6. La **tension** et la **limite de courant**.
    7. Le courant a atteint la **limite** : il y a une **anomalie** (court-circuit, consommation trop forte).

## 📦 Livrable

Relevé de 5 mesures (valeur, unité, instrument, réglage utilisé).
