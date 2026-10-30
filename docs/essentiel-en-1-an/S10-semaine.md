# Semaine 10 : Tester, valider et dépanner

> **Durée** : 4 h · **Compétences E2** : C11, C03

## 🎯 À la fin de la semaine, je sais…

- comparer une mesure à une **tolérance** en tenant compte de sa **marge** ;
- rédiger un **procès-verbal (PV)** de validation ;
- appliquer une **méthode de dépannage** et trouver une panne avec un **tableau de tensions** ;
- remplir une **fiche d'intervention** ;
- appliquer les règles de **sécurité** pendant un dépannage.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | TP virtuels ElectroLab : dépannage |
| 1 h | Cours : tolérance, marge, PV, traçabilité |
| 1 h | Cours : méthode de dépannage, tableau de tensions |
| 1 h | Atelier réel : valider puis dépanner la carte clignoteur |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾** :

- **Dépannage d'une platine transistor + LED (6 pannes)** (1 h 30)
- **Dépannage d'une alimentation 5 V (7 pannes)** (2 h)
- **Dépannage d'un amplificateur inverseur à AOP (4 pannes)** (1 h 30)
- **Dépannage d'une platine logique NAND + inverseur (5 pannes)** (1 h 30)

Puis, pour ta carte, ouvre ces sujets (bouton **Ouvrir**) :

- [`clignoteur.json`](tp/clignoteur.json) : la carte saine de référence ;
- [`clignoteur-panne-A.json`](tp/clignoteur-panne-A.json) : panne A, rien ne s'allume ;
- [`clignoteur-panne-B.json`](tp/clignoteur-panne-B.json) : panne B, LED toujours allumée ;
- [`clignoteur-panne-C.json`](tp/clignoteur-panne-C.json) : panne C, même symptôme que B, autre cause.

---

## 📖 Le cours

**🤔 À ton avis ?** Tu mesures 4,80 V sur une sortie censée être 5 V ± 5 %. Est-ce conforme ?

??? question "Réponse"
    Oui : 4,80 V est dans la plage de 4,75 V à 5,25 V. **Mais** si ta mesure a une marge de ± 0,1 V, la vraie valeur pourrait être 4,70 V : **hors tolérance**. On doit donc tenir compte de la **marge de mesure**.

### 1. La tolérance et la plage

« 5 V ± 5 % » signifie de $5 \times 0{,}95 = 4{,}75\,\mathrm{V}$ à $5 \times 1{,}05 = 5{,}25\,\mathrm{V}$. Tout ce qui est dans cette plage est **conforme**.

### 2. La marge de mesure et la conclusion

La marge se calcule avec la **précision du constructeur** (voir semaine 2) : $(5{,}02 \pm 0{,}05)\,\mathrm{V}$. On compare **toute la plage** « valeur ± marge » à la tolérance :

![Conformité : on compare la plage valeur ± marge à la tolérance](images/ess_marges.png)

- toute la plage dedans → **conforme** ;
- une partie dehors → **non garanti** (à justifier ou à refaire avec un meilleur instrument) ;
- toute la plage dehors → **non conforme**.

### 3. Le procès-verbal (PV)

Un PV est la **preuve écrite** d'un contrôle.

![Structure d'un procès-verbal de validation](images/pv-validation.png)

Il contient : **identification** (carte, date, opérateur) ; **instruments** (modèle, numéro de série, **étalonnage valide**) ; **méthode** ; **résultats** (attendu, mesuré, marge, verdict) ; **conclusion** avec le critère ; **signature**.

> [!TIP] 💡 La traçabilité
> Un instrument est **comparé régulièrement** à une référence (étalonnage). Si son étalonnage est **périmé**, ses mesures ne sont plus valables dans un PV.

### 4. La méthode de dépannage

![La démarche DECA : décrire, éliminer, cibler, agir](images/deca-entonnoir.png)

1. **Décrire** le symptôme : ce qui marche, ce qui ne marche pas.
2. **Sécuriser** : tension, chaleur, odeur de brûlé.
3. **Vérifier l'alimentation** sur la carte.
4. **Dresser un tableau de tensions** : point de mesure, valeur attendue, valeur mesurée, verdict.
5. **Isoler** : couper le circuit en deux pour savoir de quel côté est la panne (dichotomie).
6. **Réparer** (un seul changement), **retester**, **tracer** (fiche d'intervention).

### 5. Trouver la panne avec les tensions

![Tableau de tensions : la première valeur anormale désigne la panne](images/ess_tension_panne.png)

La panne est à la **première valeur** qui ne correspond pas à l'attendu, en partant de l'alimentation.

| Symptôme mesuré | Cause probable |
|---|---|
| entrée de $R_b$ à 5 V, base à 0 V | résistance de base coupée |
| signal d'entrée à 0 V | problème **en amont** du circuit |
| collecteur à 0 V même sans commande | transistor en court-circuit |
| base normale mais collecteur à 1,8 V | transistor qui ne sature pas ($R_b$ trop grande) |

**Hors tension** : mesurer les résistances **retirées du circuit** ; tester les transistors et diodes avec le **test diode** (≈ 0,6 V dans un sens, rien dans l'autre) ; vérifier les pistes à la **continuité**.

### 6. Maintenance et fiche d'intervention

![Maintenance préventive et corrective](images/preventive-corrective.png)

La **maintenance corrective** répare une panne ; la **préventive** l'évite. On trace l'intervention sur une **fiche** : équipement, date, intervenant · symptôme · mesures (attendu / mesuré) · cause · action · test après réparation · préconisation.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Mesurer une résistance **sous tension**.
> - Changer **plusieurs** composants à la fois.
> - Oublier de **retester** (la panne a-t-elle disparu ? autre chose est-il en panne ?).
> - Intervenir seul sur une installation **au-dessus de 50 V AC / 120 V DC** sans habilitation.

---

## 🛠️ Atelier réel : valider puis dépanner le clignoteur

1. **Valide** ta carte : tension d'alimentation (5 V ± 5 %), fréquence (1 Hz ± 10 %), rapport cyclique, courant dans la LED. Rédige le **PV** (attendu / mesuré / marge / verdict).
2. Dans **ElectroLab**, ouvre `clignoteur.json` puis les trois pannes. Pour chacune : **décris**, **mesure** (tensions, puis résistances hors tension), **conclus**.
3. Remplis une **fiche d'intervention** pour chaque panne.

??? success "Résultats attendus"
    - **Carte saine** : $V_{CC} \approx 5\,\mathrm{V}$ ; période ≈ 1,01 s ($f \approx 0{,}99\,\mathrm{Hz}$, conforme à 0,9–1,1 Hz) ; rapport cyclique ≈ 55 %. La sortie du NE555 bipolaire n'atteint qu'environ **3,1 V** à l'état haut : le courant LED est d'environ **9 mA** avec 150 Ω (pour 20 mA, il faudrait environ 56 Ω).
    - **Panne A** : aucune tension sur la carte : le **fusible F1** est grillé (mesure de la tension avant et après le fusible).
    - **Pannes B et C** : LED **toujours allumée**, broches 2 et 6 à environ 0 V : le condensateur **ne peut plus se charger**. Même symptôme, deux causes : on **départage hors tension** en mesurant la résistance. **B** : $R_b$ coupée ; **C** : $R_a$ coupée.

## ✍️ Exercices

1. Mesure $(5{,}20 \pm 0{,}08)\,\mathrm{V}$ pour 5 V ± 5 % : verdict ?
2. Mesure $(0{,}93 \pm 0{,}02)\,\mathrm{Hz}$ pour 1 Hz ± 10 % : verdict ?
3. Citez trois éléments obligatoires d'un PV.
4. La sortie d'un 7805 est à 0 V alors que l'entrée est à 12 V. Hypothèses ?
5. Une panne disparaît quand on touche la carte : quelle famille de défauts ?

??? success "Corrigés"
    1. Plage 5,12 à 5,28 V, qui **dépasse** 5,25 V : **non garanti**.
    2. Plage 0,91 à 0,95 Hz, dans [0,90 ; 1,10] : **conforme**.
    3. Par exemple : **identification**, **instruments avec étalonnage**, **résultats avec verdict**, **conclusion**, **signature**.
    4. Régulateur défectueux, court-circuit en aval, ou masse du régulateur coupée.
    5. Un défaut **intermittent** : soudure froide ou mauvais contact.

## ✅ Auto-test

1. Que veut dire « non garanti » dans un verdict ?
2. Quelle est la première étape d'un dépannage ?
3. Combien de composants change-t-on à la fois ?
4. Pourquoi un instrument hors étalonnage invalide-t-il un PV ?

??? success "Réponses"
    1. La plage « valeur ± marge » **dépasse en partie** la tolérance.
    2. **Décrire** le symptôme (puis vérifier l'alimentation).
    3. **Un seul**, puis on reteste.
    4. Sa mesure n'est plus **garantie** ni **traçable**.

## 📦 Livrable

PV complet de la carte clignoteur et fiche d'intervention d'une panne diagnostiquée.

> [!NOTE] 📚 Pour approfondir (facultatif)
> Ce parcours se suffit à lui-même. Pour aller plus loin : Terminale S02, S07, S11 et S12 (PV, validation, dépannage), Première S14 (maintenance corrective) et Seconde S05 et S17.
