# Semaine 2 : Mesurer : multimètre et oscilloscope

> **Durée** : 4 h · **Compétences E2 travaillées** : C07 · C11

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Mesurer une tension, un courant, une résistance, une continuité.
- Régler un oscilloscope (VOLT/DIV, SEC/DIV, déclenchement) et lire amplitude, période, fréquence.
- Choisir le bon instrument selon la grandeur.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Multimètre : tension, courant, résistance, continuité |
| 1 h | Prise en main de l'oscilloscope (signal de test, sonde ×10) |
| 1 h | Mesurer un signal PWM et une LED qui clignote |
| 1 h | Auto-test et correction |

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

### 4. Les réglages à ne pas oublier

1. **Sonde ×10** déclarée sur la voie.
2. **Masse** de la sonde sur la masse du circuit.
3. **Couplage** : DC pour tout voir, AC pour supprimer la composante continue.
4. **Déclenchement** (trigger) réglé pour avoir une image stable.

### Exercice guidé

On observe une période de 5 carreaux à 2 ms/DIV et un signal de 4 carreaux de haut à 1 V/DIV.

$T = 5 \times 2 = 10\,\mathrm{ms}$ ; $f = \dfrac{1}{0{,}010} = 100\,\mathrm{Hz}$ ; $U_{pp} = 4 \times 1 = 4\,\mathrm{V}$.

## 📚 Pour approfondir : les séances à consulter

- [Seconde S12 – tests au multimètre](../../seconde/S12-tests-au-multimetre-et-controle-qualite/01-cours.md)
- [Seconde S12 – prise en main de l'oscilloscope](../../seconde/S12-tests-au-multimetre-et-controle-qualite/05-prise-en-main-oscilloscope.md)
- [Terminale S01 – circuit fourni](../S01-circuit-fourni-multimetre-oscilloscope/README.md)

## ✅ Auto-test

1. Comment branche-t-on un ampèremètre ? Un voltmètre ?
2. Une période occupe 4 carreaux à 5 ms/DIV. Quelle fréquence ?
3. Dans quelles conditions mesure-t-on une résistance ?
4. Que fait le couplage AC ?
5. Que vérifier avant de brancher la sonde ?

??? success "Réponses"
    1. L'ampèremètre en **série**, le voltmètre en **parallèle**.
    2. $T = 20\,\mathrm{ms}$ ; $f = 50\,\mathrm{Hz}$.
    3. **Hors tension** et, si possible, **hors circuit**.
    4. Il supprime la **composante continue** pour voir la variation.
    5. Qu'elle est déclarée en **×10** et que la masse est sur la **masse du circuit**.

## 📦 Livrable

Relevé de 5 mesures (valeur, unité, instrument, réglage utilisé).
