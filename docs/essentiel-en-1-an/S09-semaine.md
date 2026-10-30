# Semaine 9 : Tester, valider et dépanner

> **Durée** : 4 h · **Compétences E2 travaillées** : C11 · C03

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Suivre un protocole de test et noter attendu / mesuré / verdict.
- Comparer une mesure et sa marge à une tolérance.
- Rédiger un PV clair (identification, instruments, résultats, conclusion).
- Appliquer la méthode : décrire, mesurer, comparer, isoler, réparer, tester.
- Construire un tableau de tensions attendues / mesurées.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Tolérance, marge de mesure et PV (carte clignoteur) |
| 1 h | Méthode de dépannage : tableau de tensions |
| 1 h | TP virtuels ElectroLab : dépannage (alimentation, transistor, clignoteur) |
| 1 h | Dépannage réel, fiche d'intervention, auto-test |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾**, puis fais ces TP **avant** de toucher au matériel :

- **Dépannage d'une alimentation 5 V (7 pannes)** (2 h, niveau terminale)
- **Dépannage d'une platine transistor + LED (6 pannes)** (1 h 30, niveau première / terminale)
- **Dépannage d'un amplificateur inverseur à AOP (4 pannes)** (1 h 30, niveau terminale)
- **Dépannage d'une platine logique NAND + inverseur (5 pannes)** (1 h 30, niveau terminale)

**Sujets à ouvrir dans ElectroLab** (bouton **Ouvrir**, puis choisis le fichier `.json`) :

- [`clignoteur.json`](tp/clignoteur.json) : la carte saine de référence
- [`clignoteur-panne-A.json`](tp/clignoteur-panne-A.json) : panne A : rien ne s'allume
- [`clignoteur-panne-B.json`](tp/clignoteur-panne-B.json) : panne B : LED toujours allumée
- [`clignoteur-panne-C.json`](tp/clignoteur-panne-C.json) : panne C : même symptôme que B, autre cause

> [!TIP] 🖥️ Pourquoi d'abord le simulateur ?
> On peut se tromper sans rien casser, répéter autant de fois que nécessaire et obtenir une correction automatique. Le TP réel sert ensuite à **confirmer** et à manipuler le vrai matériel.

## 📖 Le cours en bref

**🤔 À ton avis ?** Tu mesures 4,80 V sur une sortie censée être 5 V ± 5 %. Conforme ?

??? question "Réponse"
    Oui, **4,80 V est dans la plage [4,75 V ; 5,25 V]**. Mais si l'incertitude de ta mesure est de ± 0,1 V, la vraie valeur pourrait être 4,70 V : **hors tolérance**. On doit donc tenir compte de la **marge de mesure**.

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

### 5. La méthode en 6 étapes

1. **Décrire** le symptôme (qu'est-ce qui marche ? qu'est-ce qui ne marche pas ?).
2. **Sécuriser** (tension, chaleur, odeur de brûlé).
3. **Vérifier l'alimentation** sur la carte.
4. **Dresser un tableau de tensions** : point de mesure, valeur attendue, valeur mesurée, verdict.
5. **Isoler** : couper le circuit en deux pour savoir de quel côté est la panne (dichotomie).
6. **Réparer** (un seul changement), **retester**, **tracer** (fiche d'intervention).

### 6. Trouver la panne avec les tensions

La panne est à la **première valeur** qui ne correspond pas à l'attendu, en partant de l'alimentation.

**Exemple** (LED pilotée par un transistor, 5 V) : base ≈ 0,7 V, collecteur ≈ 0,2 V quand tout va bien.

| Symptôme mesuré | Cause probable |
|---|---|
| signal d'entrée 5 V, base à 0 V | résistance de base coupée |
| signal d'entrée 0 V | problème **en amont** du circuit |
| collecteur à 0 V même sans commande | transistor en court-circuit |
| base normale mais collecteur à 1,8 V | transistor qui ne sature pas (résistance de base trop grande) |

### 7. Les mesures hors tension

- **Résistance** : retirée du circuit.
- **Transistor / diode** : test diode (≈ 0,6 V dans un sens, rien dans l'autre).
- **Continuité** : pistes et fils (bip).

### 8. Sécurité

- **Très basse tension** (≤ 50 V AC / 120 V DC) : pas de risque d'électrisation, mais attention à la chaleur et aux courts-circuits.
- Au-delà : **habilitation** (BR) obligatoire.
- **ESD** : bracelet, tapis, sachets antistatiques.


## 🛠️ Atelier guidé : on construit, on mesure, on valide

**Fil rouge 1 : valider puis dépanner la carte clignoteur.**

1. **Valide** la carte : tension d'alimentation (5 V ± 5 %), fréquence (1 Hz ± 10 %), rapport cyclique, courant dans la LED. Rédige le PV (attendu / mesuré / marge / verdict).
2. Dans **ElectroLab**, ouvre `clignoteur.json` puis les sujets de panne `clignoteur-panne-A.json`, `-B.json`, `-C.json`. Pour chacun : **décris** le symptôme, **mesure** (tensions, puis résistances hors tension), **conclus**.
3. Remplis une **fiche d'intervention** pour chaque panne.

??? success "Résultats attendus"
    - **Carte saine** : $V_{CC} \approx 5\,\mathrm{V}$ ; période ≈ 1,01 s ($f \approx 0{,}99\,\mathrm{Hz}$, conforme à 0,9–1,1 Hz) ; rapport cyclique ≈ 55 % ; sortie à l'état haut ≈ 3,1 V, donc courant LED ≈ 9 mA avec 150 Ω (inférieur au calcul simplifié : le NE555 bipolaire « perd » environ 1,9 V en sortie).
    - **Panne A** : aucune tension sur la carte : le **fusible F1** est grillé (mesure de la tension avant et après le fusible).
    - **Pannes B et C** : LED **toujours allumée**, broches 2 et 6 à environ 0 V : le condensateur **ne peut plus se charger**. Même symptôme, deux causes : on **départage hors tension** en mesurant la résistance. **B** : $R_b$ coupée ; **C** : $R_a$ coupée.

## ✍️ Exercices d'application

1. Mesure $(5{,}20 \pm 0{,}08)\,\mathrm{V}$ pour 5 V ± 5 % : verdict ?
2. Mesure $(0{,}93 \pm 0{,}02)\,\mathrm{Hz}$ pour 1 Hz ± 10 % : verdict ?
3. La sortie du 7805 est à 0 V, l'entrée à 12 V. Hypothèses ?
4. Pourquoi mesure-t-on une résistance retirée du circuit ?

??? success "Corrigés"
    1. Plage 5,12 à 5,28 V, qui **dépasse** 5,25 V : **non garanti**, à justifier ou refaire avec un meilleur instrument.
    2. Plage 0,91 à 0,95 Hz, dans [0,90 ; 1,10] : **conforme**.
    3. Régulateur défectueux, ou court-circuit en aval qui l'écrase (limite thermique), ou masse du régulateur coupée.
    4. Pour ne pas mesurer les autres composants en parallèle.

## 📚 Pour approfondir : les séances à consulter

- [Terminale S02 – rapport de mesures et PV](../terminale/S02-rapport-de-mesures-pv-professionnel/01-cours.md)
- [Terminale S07 – validation et conformité](../terminale/S07-validation-conformite-pv-professionnel/01-cours.md)
- [Terminale S11 – TP carte NE555 / 7805](../terminale/S11-interpreter-document-mesures-carte/02-tp.md)
- [Terminale S12 – dépanner un circuit simple](../terminale/S12-reussir-un-tp-de-mesure-en-45-minutes/03-depannage-circuit-simple.md)

## ✅ Auto-test

1. Sortie 5 V ± 5 % : quelle plage est acceptable ?
2. Mesure $(5{,}02 \pm 0{,}05)\,\mathrm{V}$ : conforme ?
3. Mesure $(5{,}20 \pm 0{,}08)\,\mathrm{V}$ : conforme ?
4. Par quoi commence-t-on un dépannage ?
5. Où se cache la panne dans un tableau de tensions ?
6. Pourquoi mesure-t-on une résistance hors tension ?

??? success "Réponses"
    1. De **4,75 V à 5,25 V**.
    2. **Oui** : la plage 4,97 à 5,07 V est dans la tolérance.
    3. **Non garanti** : la plage dépasse 5,25 V.
    4. Par **décrire** le symptôme et **vérifier l'alimentation**, pas par changer des composants.
    5. À la **première** valeur mesurée qui ne correspond pas à la valeur attendue.
    6. Sous tension, la mesure est **fausse** et peut endommager l'appareil.

## 📦 Livrable

PV de la carte clignoteur et fiche d'intervention d'une panne diagnostiquée.
