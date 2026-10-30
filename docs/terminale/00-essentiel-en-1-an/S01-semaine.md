# Semaine 1 : Les composants et les lois de base

> **Durée** : 4 h · **Compétences E2 travaillées** : C07

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Reconnaître les composants courants (résistance, condensateur, diode/LED, transistor, régulateur, circuit intégré).
- Appliquer la loi d'Ohm et calculer une puissance.
- Lire le code couleurs d'une résistance.
- Calculer la résistance en série d'une LED.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Découvrir les familles de composants et leurs symboles |
| 1 h | Loi d'Ohm, puissance, code couleurs : exercices |
| 1 h | LED : calcul de la résistance, câblage sur plaque d'essai |
| 1 h | Auto-test et correction |

## 📖 Le cours en bref

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

## 📚 Pour approfondir : les séances à consulter

- [Seconde S01 – code couleurs et loi d'Ohm](../../seconde/S01-code-couleurs-des-resistances-et-loi-d/01-cours.md)
- [Seconde S01 – familles de composants](../../seconde/S01-code-couleurs-des-resistances-et-loi-d/02-familles-de-composants.md)
- [Seconde S02 – diodes et LED](../../seconde/S02-diodes-led-circuits-serie-parallele-loi/01-cours.md)

## ✅ Auto-test

1. Une résistance marron – noir – orange – or vaut combien ?
2. Quel courant dans une résistance de 330 Ω sous 5 V ?
3. Quelle résistance en série avec une LED (2 V, 20 mA) sous 5 V ?
4. Quelle patte d'une LED est l'anode (+) ?
5. Quelle puissance dissipe une résistance traversée par 100 mA sous 5 V ?

??? success "Réponses"
    1. **10 kΩ**, tolérance ± 5 %.
    2. $I = \dfrac{5}{330} \approx 15{,}2\,\mathrm{mA}$.
    3. $R = \dfrac{5 - 2}{0{,}020} = 150\,\Omega$.
    4. La **patte longue**.
    5. $P = 5 \times 0{,}1 = 0{,}5\,\mathrm{W}$.

## 📦 Livrable

Fiche « mes composants » : symbole, rôle et une valeur typique pour 8 composants.
