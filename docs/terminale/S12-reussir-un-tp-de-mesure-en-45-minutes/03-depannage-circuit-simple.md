# 🛠️ Dépanner un circuit simple : méthode et cas pratique

## 🤔 À ton avis ?

Une LED commandée par un transistor **ne s'allume plus**. Tu as un multimètre. Par quoi commences-tu : **remplacer le transistor**, **changer la LED**… ou autre chose ?

??? question "Réponse"
    Ni l'un ni l'autre. Remplacer au hasard coûte du temps et peut masquer la vraie cause. On **observe**, on **mesure des tensions** à des points précis, on les **compare aux valeurs attendues** : la bonne mesure désigne la pièce en cause.

## 1. La méthode en 6 étapes

| Étape | Je fais | Je note |
|---|---|---|
| 1. **Décrire** | Je regarde sans toucher : que se passe-t-il, que devrait-il se passer ? | Le symptôme |
| 2. **Sécuriser** | Je vérifie qu'il n'y a pas de danger (tension, chaleur, odeur) | Les précautions |
| 3. **Alimentation** | Je mesure la tension d'alimentation **sur la carte** | $V_{CC}$ mesurée |
| 4. **Tableau de tensions** | Je mesure chaque nœud et je compare à la valeur attendue | Attendu / mesuré / verdict |
| 5. **Isoler** | Je coupe le circuit en deux (dichotomie) pour savoir de quel côté est la panne | La zone fautive |
| 6. **Réparer, tester, tracer** | Je remplace **une seule** chose, je reteste, je remplis la fiche | La fiche d'intervention |

> [!TIP] 💡 En clair
> La panne se cache là où **la tension mesurée ne correspond pas à la tension attendue**. On cherche donc d'abord la **première** valeur qui sort du lot, en partant de l'alimentation.

> [!WARNING] ⚠️ Sécurité
> Nos montages sont en **basse tension (5 V)** : pas de danger d'électrisation. Au-delà de **50 V alternatif ou 120 V continu**, il faut une **habilitation électrique** (BR) : on ne dépanne pas seul un circuit relié au secteur.

## 2. Cas pratique : LED pilotée par un transistor NPN

Le schéma est celui de la séance de Première S01 : $V_{CC} = 5\,\mathrm{V}$, $R_{c} = 150\,\Omega$ en série avec la LED côté collecteur, $R_{b} = 10\,\mathrm{k\Omega}$, signal d'entrée à 5 V (LED censée être allumée).

### Tableau de référence (circuit en bon état)

| Point de mesure | Valeur attendue | Pourquoi |
|---|---|---|
| Entrée de $R_{b}$ | 5 V | Signal appliqué |
| Base du transistor | ≈ 0,7 V | Tension $V_{BE}$ |
| Entre les bornes de $R_{c}$ | ≈ 2,8 V | $5 - 2\,(\text{LED}) - 0{,}2\,(V_{CE(sat)})$ |
| Courant dans la LED | ≈ 18,7 mA | $\dfrac{2{,}8}{150}$ |
| Collecteur | ≈ 0,2 V | Transistor saturé |

### Quatre pannes à diagnostiquer

Pour chaque relevé, trouve la **cause**.

| Panne | Entrée de $R_{b}$ | Base | Tension aux bornes de $R_{c}$ | Collecteur | LED |
|---|---|---|---|---|---|
| **A** | 5 V | 0 V | 0 V | 5 V | éteinte |
| **B** | 0 V | 0 V | 0 V | 5 V | éteinte |
| **C** | 5 V | 0,7 V | 1,3 V | 1,8 V | faible |
| **D** | 0 V | 0 V | 3 V | 0 V | allumée |

??? success "Diagnostic"

    - **A** : le signal arrive (5 V) mais la base est à 0 V : **$R_{b}$ coupée** (ou soudure coupée). Plus de courant de base, le transistor est bloqué.
    - **B** : **pas de signal en entrée** (0 V) : le problème est **en amont** (câble, générateur, microcontrôleur), pas dans ce circuit.
    - **C** : l'entrée et la base sont normales, mais le collecteur est à **1,8 V** au lieu de 0,2 V : le transistor **ne sature pas**, il fournit trop peu de courant (≈ 8,7 mA au lieu de 18,7 mA). La cause : un courant de base trop faible, donc **$R_b$ de valeur trop grande** (100 kΩ montée à la place de 10 kΩ). On le confirme en mesurant $R_b$ hors tension.
    - **D** : entrée à 0 V mais la LED reste allumée et le collecteur est à 0 V : le **transistor est en court-circuit collecteur-émetteur** (claqué) : à remplacer.

### Hors tension : confirmer avec le multimètre

- **Résistance** : mesurer $R_{b}$ et $R_{c}$ **retirées du circuit** (sinon les autres composants faussent la mesure).
- **Transistor** : le **test diode** doit donner environ 0,6 à 0,7 V entre base et émetteur, dans un sens seulement.
- **LED** : le test diode doit l'allumer faiblement dans un seul sens.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Mesurer une résistance **sous tension** : valeur fausse, risque pour le multimètre.
> - Changer **plusieurs** composants à la fois : on ne sait plus lequel était en cause.
> - Oublier de **retester** après la réparation (la panne a-t-elle disparu ? autre chose est-il tombé en panne ?).

## 3. La fiche d'intervention

| Champ | À remplir |
|---|---|
| Équipement, date, intervenant | |
| Symptôme observé | |
| Mesures réalisées (attendu / mesuré) | |
| Cause identifiée | |
| Action corrective | |
| Test après réparation | ☐ OK ☐ KO |
| Préconisation (maintenance préventive) | |

## 4. Entraîne-toi

Un montage identique mais avec **$R_{c} = 330\,\Omega$** et une alimentation de 5 V. Quel est le courant dans la LED en fonctionnement normal ? Une mesure de 0,5 V aux bornes de $R_{c}$ indique quelle panne ?

??? success "Réponses"

    - Normal : $\dfrac{5 - 2 - 0{,}2}{330} \approx 8{,}5\,\mathrm{mA}$ (tension aux bornes de $R_{c}$ : 2,8 V).
    - 0,5 V aux bornes de $R_c$ : courant $\dfrac{0{,}5}{330} \approx 1{,}5\,\mathrm{mA}$, très insuffisant. Le transistor ne sature pas : la cause la plus probable est un **courant de base trop faible** ($R_b$ de valeur trop grande). On confirme en mesurant $V_{CE}$ (bien supérieur à 0,2 V) puis $R_b$ hors tension.

> [!SUCCESS] 🧠 À retenir
> - Dépanner = **décrire, mesurer, comparer, isoler, réparer, tracer**.
> - On cherche la **première** tension anormale en partant de l'alimentation.
> - Une résistance se mesure **hors tension** et **hors circuit**.
> - Une seule modification à la fois, puis on **retest**e.
