# 📘 FICHE DE COURS ÉLÈVE - U2 ÉLECTRONIQUE - SEMAINE 1

## ⚡ CODE COULEURS DES RÉSISTANCES ET LOI D'OHM

---

## 📋 INFORMATIONS

| **Élément** | **Détail** |
|-------------|------------|
| **Bloc** | U2 - Réalisation et maintenance de systèmes électroniques |
| **Semaine** | S1 / Année 1 |
| **Thématique** | Diagnostic prérequis, Code couleurs, Loi d'Ohm |
| **Durée cours** | 50 minutes |

---

## 🎯 OBJECTIFS D'APPRENTISSAGE

À la fin de ce cours, je serai capable de :

✅ Décoder le code couleurs des résistances  
✅ Comprendre les 3 grandeurs électriques : U, I, R  
✅ Appliquer la loi d'Ohm (U = R × I)  
✅ Convertir les unités (Ω, kΩ, MΩ / A, mA, µA)  
✅ Identifier les principaux composants électroniques  
✅ Calculer une valeur manquante dans un circuit  

---

## 1️⃣ LES 3 GRANDEURS ÉLECTRIQUES FONDAMENTALES

### 📖 Définitions

| **Grandeur** | **Symbole** | **Unité** | **Définition** | **Analogie hydraulique** |
|-------------|------------|-----------|----------------|--------------------------|
| **Tension** | **U** | Volt (V) | Différence de potentiel électrique | Pression de l'eau |
| **Intensité** | **I** | Ampère (A) | Quantité de charges qui circulent | Débit de l'eau |
| **Résistance** | **R** | Ohm (Ω) | Opposition au passage du courant | Étroitesse du tuyau |

### 🌊 L'analogie de l'eau

**Comprendre l'électricité comme un circuit d'eau :**

```
┌────────────────────────────────────────┐
│      CHÂTEAU D'EAU (Tension U)         │
│         ↓ Haute pression               │
│         │                              │
│    ┌────▼────┐                         │
│    │  POMPE  │ ← Générateur            │
│    └────┬────┘                         │
│         │                              │
│    ┌────▼──────────┐                   │
│    │ TUYAU ÉTROIT  │ ← Résistance      │
│    │  (Résistance) │                   │
│    └────┬──────────┘                   │
│         │                              │
│         ▼ Débit (Intensité I)          │
│                                        │
│    ┌─────────┐                         │
│    │ TURBINE │ ← Charge (LED, moteur)  │
│    └─────────┘                         │
└────────────────────────────────────────┘
```

**Points clés de l'analogie :**

| **Électricité** | **Eau** |
|----------------|---------|
| Générateur (pile) | Pompe / Château d'eau |
| Tension (V) | Pression de l'eau |
| Intensité (A) | Débit de l'eau |
| Résistance (Ω) | Étroitesse du tuyau |
| Charge (LED, moteur) | Turbine / Roue à eau |

![Illustration : Deux schémas côte à côte. À gauche : circuit électrique simple avec pile, résistance et LED. À droite : circuit d'eau avec réservoir en hauteur, tuyau étroit et roue à eau. Des flèches relient les éléments équivalents. Style : schéma pédagogique clair avec annotations.]

**Prompt image :** "Illustration comparative électricité vs eau. Côté gauche : circuit électrique simple avec pile rectangulaire, résistance (zigzag), LED (triangle), fil connectant le tout. Côté droit : circuit hydraulique avec château d'eau en hauteur, tuyau étroit descendant, roue à eau en bas. Flèches colorées reliant : pile↔château d'eau, résistance↔tuyau étroit, LED↔roue. Labels clairs. Style : diagramme pédagogique coloré sur fond blanc."

---

## 2️⃣ LA LOI D'OHM

### 📖 Définition

La **loi d'Ohm** est la relation mathématique fondamentale qui lie tension, intensité et résistance :

```
╔═══════════════════╗
║   U = R × I       ║
╚═══════════════════╝

U = Tension (Volt)
R = Résistance (Ohm)
I = Intensité (Ampère)
```

### 🔺 Le triangle mnémotechnique

**Pour retrouver facilement les 3 formules :**

```
        U
       ───
      │   │
      R   I
```

**Comment utiliser le triangle :**

1. **Cacher ce que vous cherchez** avec le doigt
2. **Lire ce qui reste** :

| **Je cherche** | **Je cache** | **Formule** | **Calcul** |
|---------------|--------------|-------------|------------|
| **U** (Tension) | U | R et I côte à côte | **U = R × I** |
| **R** (Résistance) | R | U au-dessus de I | **R = U / I** |
| **I** (Intensité) | I | U au-dessus de R | **I = U / R** |

### 📝 Exemples d'application

#### Exemple 1 : Calculer la tension U

**Données :**
- Résistance : R = 1000 Ω
- Intensité : I = 0,01 A

**Calcul :**
```
U = R × I
U = 1000 × 0,01
U = 10 V
```

**Réponse :** La tension est de **10 Volts**.

---

#### Exemple 2 : Calculer la résistance R

**Données :**
- Tension : U = 12 V
- Intensité : I = 0,02 A

**Calcul :**
```
R = U / I
R = 12 / 0,02
R = 600 Ω
```

**Réponse :** La résistance est de **600 Ohms**.

---

#### Exemple 3 : Calculer l'intensité I

**Données :**
- Tension : U = 5 V
- Résistance : R = 500 Ω

**Calcul :**
```
I = U / R
I = 5 / 500
I = 0,01 A = 10 mA
```

**Réponse :** L'intensité est de **0,01 Ampère** ou **10 milliampères**.

---

## 3️⃣ LES UNITÉS ET CONVERSIONS

### 📊 Les multiples et sous-multiples

#### Pour la RÉSISTANCE (Ohm)

| **Unité** | **Symbole** | **Conversion** | **Exemple** |
|-----------|------------|----------------|-------------|
| Ohm | Ω | 1 Ω | Résistance faible |
| Kilo-ohm | kΩ | 1 kΩ = 1 000 Ω | **Résistance standard** |
| Méga-ohm | MΩ | 1 MΩ = 1 000 000 Ω | Résistance élevée |

**Conversions utiles :**
- 100 Ω = 0,1 kΩ
- 1 000 Ω = 1 kΩ
- 10 000 Ω = 10 kΩ
- 1 000 000 Ω = 1 000 kΩ = 1 MΩ

---

#### Pour l'INTENSITÉ (Ampère)

| **Unité** | **Symbole** | **Conversion** | **Exemple** |
|-----------|------------|----------------|-------------|
| Ampère | A | 1 A | Moteur électrique |
| Milliampère | mA | 1 mA = 0,001 A | **LED standard** |
| Microampère | µA | 1 µA = 0,000001 A | Composants très faibles |

**Conversions utiles :**
- 1 A = 1 000 mA
- 0,01 A = 10 mA
- 20 mA = 0,02 A
- 500 mA = 0,5 A

---

#### Pour la TENSION (Volt)

| **Unité** | **Symbole** | **Conversion** | **Exemple** |
|-----------|------------|----------------|-------------|
| Volt | V | 1 V | Pile |
| Millivolt | mV | 1 mV = 0,001 V | Signaux faibles |
| Kilovolt | kV | 1 kV = 1 000 V | Haute tension |

**Tensions courantes :**
- Pile AA : 1,5 V
- Pile 9V : 9 V
- USB : 5 V
- Batterie voiture : 12 V
- Secteur France : 230 V

---

### 🔄 Tableau de conversion rapide

**Méthode :** Pour convertir, déplacer la virgule !

```
MΩ ← ← ← kΩ ← ← ← Ω
   × 1000   × 1000

Exemple : 2,5 kΩ = 2 500 Ω
```

```
A → → → mA → → → µA
   ÷ 1000   ÷ 1000

Exemple : 0,02 A = 20 mA
```

---

## 4️⃣ LE CODE COULEURS DES RÉSISTANCES

### 📖 Principe

Les **résistances** utilisent un système de **bagues colorées** pour indiquer leur valeur en Ohms.

**Pourquoi des couleurs ?**  
→ Les résistances sont petites, impossible d'écrire "1000 Ω" dessus !

### 🎨 Le tableau des couleurs

| **Couleur** | **Chiffre** | **Multiplicateur** | **Moyen mnémotechnique** |
|------------|------------|-------------------|-------------------------|
| ⚫ **Noir** | 0 | × 1 | **N**e **0** mettez rien |
| 🟤 **Marron** | 1 | × 10 | **M**arron = **1** |
| 🔴 **Rouge** | 2 | × 100 | **R**ouge = **2** |
| 🟠 **Orange** | 3 | × 1 000 | **O**range = **3** |
| 🟡 **Jaune** | 4 | × 10 000 | **J**aune = **4** |
| 🟢 **Vert** | 5 | × 100 000 | **V**ert = **5** |
| 🔵 **Bleu** | 6 | × 1 000 000 | **B**leu = **6** |
| 🟣 **Violet** | 7 | - | **V**iolet = **7** |
| ⚪ **Gris** | 8 | - | **G**ris = **8** |
| ⚪ **Blanc** | 9 | - | **B**lanc = **9** |

### 🔢 Comment décoder une résistance ?

**Une résistance à 4 bagues :**

```
┌──────────────────────────────────┐
│    RÉSISTANCE 4 BAGUES           │
│                                  │
│   ██  ██  ██  ██                │
│   │   │   │   │                 │
│   1   2   3   4                 │
│                                  │
│  Bague 1 : Chiffre des dizaines │
│  Bague 2 : Chiffre des unités   │
│  Bague 3 : Multiplicateur       │
│  Bague 4 : Tolérance (optionnel)│
└──────────────────────────────────┘
```

**Formule :**

```
Valeur = (Bague1 × 10 + Bague2) × Multiplicateur
```

---

### 📝 Exemples de décodage

#### Exemple 1 : Marron - Noir - Rouge

| **Bague** | **Couleur** | **Valeur** |
|-----------|------------|------------|
| Bague 1 | 🟤 Marron | 1 |
| Bague 2 | ⚫ Noir | 0 |
| Bague 3 | 🔴 Rouge | × 100 |

**Calcul :**
```
(1 × 10 + 0) × 100 = 10 × 100 = 1 000 Ω = 1 kΩ
```

**Réponse :** **1 000 Ω** ou **1 kΩ**

---

#### Exemple 2 : Jaune - Violet - Orange

| **Bague** | **Couleur** | **Valeur** |
|-----------|------------|------------|
| Bague 1 | 🟡 Jaune | 4 |
| Bague 2 | 🟣 Violet | 7 |
| Bague 3 | 🟠 Orange | × 1 000 |

**Calcul :**
```
(4 × 10 + 7) × 1 000 = 47 × 1 000 = 47 000 Ω = 47 kΩ
```

**Réponse :** **47 000 Ω** ou **47 kΩ**

---

#### Exemple 3 : Marron - Noir - Jaune

| **Bague** | **Couleur** | **Valeur** |
|-----------|------------|------------|
| Bague 1 | 🟤 Marron | 1 |
| Bague 2 | ⚫ Noir | 0 |
| Bague 3 | 🟡 Jaune | × 10 000 |

**Calcul :**
```
(1 × 10 + 0) × 10 000 = 10 × 10 000 = 100 000 Ω = 100 kΩ
```

**Réponse :** **100 000 Ω** ou **100 kΩ**

---

### 🎨 La 4e bague : la tolérance

| **Couleur** | **Tolérance** | **Signification** |
|------------|--------------|------------------|
| 🟡 **Or** | ± 5% | Précision standard |
| ⚪ **Argent** | ± 10% | Précision normale |
| 🔴 **Rouge** | ± 2% | Précision élevée |
| 🟤 **Marron** | ± 1% | Très haute précision |

**Exemple :**  
Une résistance de 1 kΩ ± 5% peut avoir une valeur réelle entre **950 Ω et 1 050 Ω**.

---

## 5️⃣ LES COMPOSANTS ÉLECTRONIQUES DE BASE

### 📦 Tableau récapitulatif

| **Composant** | **Symbole** | **Rôle** | **Caractéristique** | **Polarité** |
|--------------|------------|----------|---------------------|--------------|
| 🟤 **Résistance** | ──▭── | Limiter le courant | Valeur en Ω (code couleurs) | Non |
| 🔴 **LED** | ──▷\|── | Émettre de la lumière | Tension ~2V, Courant ~20mA | Oui (+ = patte longue) |
| ⚫ **Diode** | ──▷\|── | Laisser passer le courant dans un seul sens | Bague = cathode (-) | Oui |
| 🟡 **Condensateur** | ──\|\|── | Stocker de l'énergie électrique | Valeur en F (Farad) | Parfois (électrolytique) |
| 🔵 **Transistor** | ─┤├─ | Amplifier ou commuter un signal | 3 pattes : B, C, E | Oui |
| 🔋 **Pile** | ─\|+─ | Fournir une tension | Tension en V | Oui (+ et -) |

---

### 🔍 Focus : La LED (Light Emitting Diode)

**Caractéristiques principales :**

| **Paramètre** | **Valeur typique** |
|--------------|-------------------|
| Tension directe (Vf) | 1,8 V (rouge) à 3,3 V (bleu/blanc) |
| Courant nominal | 20 mA (0,02 A) |
| Polarité | Oui : patte longue = anode (+) |

**⚠️ IMPORTANT :** Une LED doit **toujours** être protégée par une **résistance de limitation** !

**Calcul de la résistance de limitation :**

```
           Vcc (Tension alimentation)
Rled = ─────────────────────────────
              Iled (0,02 A)
```

**Exemple :**  
Alimenter une LED rouge (Vf = 2V) avec une pile de 9V :

```
Rled = (9V - 2V) / 0,02A = 7V / 0,02A = 350 Ω

→ On choisira une résistance de 330 Ω ou 470 Ω (valeur standard)
```

![Illustration : Schéma électrique d'un circuit LED avec pile 9V, résistance de protection et LED. Annotations montrant le sens du courant et les valeurs. Style : schéma technique clair et coloré.]

**Prompt image :** "Schéma électrique simple d'un circuit LED. De gauche à droite : pile 9V (rectangle avec + et -), fil, résistance 330Ω (zigzag avec couleurs marron-orange-marron), fil, LED rouge (triangle avec barre). Flèche rouge indiquant le sens du courant. Annotations : '9V', '330Ω', 'LED 2V 20mA'. Style : schéma technique clair sur fond blanc."

---

## 6️⃣ EXERCICES D'APPLICATION

### 🧮 Exercice 1 : Décodage de résistances

**Décodez les résistances suivantes :**

1. 🟤 Marron - 🔴 Rouge - 🟠 Orange = _______ Ω = _______ kΩ
2. 🟡 Jaune - 🟣 Violet - 🔴 Rouge = _______ Ω = _______ kΩ
3. 🟢 Vert - 🔵 Bleu - 🟤 Marron = _______ Ω = _______ kΩ

---

### 🧮 Exercice 2 : Loi d'Ohm

**Calculez la valeur manquante :**

1. U = 12V, R = 600Ω → I = _______ A = _______ mA
2. I = 0,05A, R = 200Ω → U = _______ V
3. U = 9V, I = 0,003A → R = _______ Ω = _______ kΩ

---

### 🧮 Exercice 3 : Conversions

**Convertissez les valeurs suivantes :**

1. 4 700 Ω = _______ kΩ
2. 0,025 A = _______ mA
3. 2,2 MΩ = _______ Ω
4. 150 mA = _______ A

---

## 📝 VOCABULAIRE CLÉ À MAÎTRISER

| **Terme** | **Définition** |
|-----------|----------------|
| **Tension (U)** | Différence de potentiel électrique (Volt) |
| **Intensité (I)** | Quantité de courant qui circule (Ampère) |
| **Résistance (R)** | Opposition au passage du courant (Ohm) |
| **Loi d'Ohm** | Relation U = R × I |
| **Code couleurs** | Système de bagues colorées sur les résistances |
| **LED** | Diode électroluminescente qui émet de la lumière |
| **Polarité** | Sens de branchement d'un composant (+ et -) |
| **Anode** | Borne positive (+) d'une LED ou diode |
| **Cathode** | Borne négative (-) d'une LED ou diode |
| **Multimètre** | Appareil de mesure (tension, intensité, résistance) |
| **Circuit série** | Composants branchés les uns après les autres |
| **Circuit parallèle** | Composants branchés sur des branches différentes |

---

## ✅ AUTO-ÉVALUATION : AI-JE COMPRIS ?

Cochez les affirmations vraies :

- [ ] La tension se mesure en Ampères
- [ ] La formule de la loi d'Ohm est U = R × I
- [ ] Une résistance Marron-Noir-Orange vaut 10 kΩ
- [ ] Une LED peut se brancher directement sur une pile sans résistance
- [ ] 1 kΩ = 1 000 Ω
- [ ] La patte longue d'une LED est la cathode (-)
- [ ] L'intensité se mesure en Volts
- [ ] 20 mA = 0,02 A

**Réponses :**
✅ Vrai : 2 (U = R × I), 3 (Marron=1, Noir=0, Orange=×1000 → 10 000 Ω = 10 kΩ), 5 (1 kΩ = 1 000 Ω), 8 (20 mA = 0,02 A)  
❌ Faux : 1 (tension = Volt), 4 (il faut TOUJOURS une résistance de limitation), 6 (patte longue = anode +), 7 (intensité = Ampère)

---

## 🔗 POUR ALLER PLUS LOIN

### 📚 Ressources complémentaires

- 🎥 **Vidéo** : "La loi d'Ohm expliquée" - e-penser (YouTube)
- 🎥 **Vidéo** : "Code couleurs résistances" - Électronique Passion (YouTube)
- 📱 **App mobile** : "Resistor Color Code" (calculateur de résistances)
- 🛠️ **Simulateur** : [https://www.falstad.com/circuit/](https://www.falstad.com/circuit/)
- 📖 **Livre** : "L'électronique pour les débutants" - Jean-Pierre Oehmichen

### 🎯 Exercices supplémentaires

1. Décodez 10 résistances trouvées chez vous (vieux appareils)
2. Calculez la résistance de limitation pour une LED verte (Vf = 2,2V) avec une pile de 12V
3. Convertissez 50 valeurs entre Ω, kΩ, MΩ et mA, A

---

## 🏢 APPLICATION EN ENTREPRISE

**Situations professionnelles où vous utiliserez ces notions :**

✅ **Identifier une résistance** sur une carte électronique défectueuse  
✅ **Calculer la résistance de limitation** pour remplacer une LED grillée  
✅ **Mesurer avec un multimètre** les tensions et intensités d'un circuit  
✅ **Lire un schéma électrique** pour comprendre un montage  
✅ **Diagnostiquer une panne** en vérifiant les valeurs de résistances  

**Missions possibles en entreprise cette semaine :**
- Observer les cartes électroniques et identifier les composants
- Demander au tuteur de montrer un schéma électrique
- Photographier une carte et annoter les composants

---

## 🔧 FORMULES À RETENIR (MÉMO)

### Triangle de la loi d'Ohm

```
    U
   ───
  R │ I

U = R × I
R = U / I
I = U / R
```

### Conversions rapides

```
1 kΩ = 1 000 Ω
1 MΩ = 1 000 000 Ω
1 A = 1 000 mA
1 mA = 0,001 A
```

### Résistance de limitation LED

```
Rled = (Vcc - Vf) / Iled
```

---

**📅 Fiche rédigée le :** 26/02/2026  
**✍️ Auteur :** Équipe pédagogique CFA  
**📧 Questions :** formation@cfa-exemple.fr  
**🔄 Prochaine mise à jour :** Juin 2026

---

**💡 ASTUCE RÉVISION :** Imprimez cette fiche et gardez-la toujours avec vous ! Le code couleurs et la loi d'Ohm sont LA BASE de toute l'électronique. Vous les utiliserez tous les jours pendant 3 ans ! ⚡**
