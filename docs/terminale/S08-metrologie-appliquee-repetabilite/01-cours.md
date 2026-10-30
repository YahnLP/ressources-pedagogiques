# 📘 FICHE DE COURS — S8 · 3ᵉ ANNÉE · E2
## Métrologie Appliquée : Répétabilité · Reproductibilité · Gauge R&R · Limite de Détection

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences** : S8.1 · S8.2 · S8.3 · S8.4 · C8.1

---

## 🔑 Vocabulaire clé

| Terme | Définition | Symbole |
|---|---|---|
| **Répétabilité** | Variabilité d'un même opérateur faisant plusieurs mesures dans les mêmes conditions | σ_EV ou σ_r |
| **Reproductibilité** | Variabilité entre opérateurs différents mesurant le même objet | σ_AV ou σ_R |
| **Gauge R&R** | Gage Repeatability & Reproducibility — méthode industrielle d'analyse des MSE | %GRR |
| **MSA** | Measurement System Analysis — analyse du système de mesure (norme IATF) | — |
| **EV** | Equipment Variation — variation due à l'équipement (= répétabilité) | — |
| **AV** | Appraiser Variation — variation due à l'opérateur (= reproductibilité) | — |
| **GRR** | Gauge Repeatability & Reproducibility — combinaison de EV et AV | σ_GRR |
| **%GRR** | Pourcentage de la tolérance consommé par le système de mesure | % |
| **Étendue R** | max − min d'une série de mesures | Ω, °C... |
| **LDD** | Limite de Décision de Détection — seuil à 95% de détection | — |
| **LD** | Limite de Détection — seuil pratique de détectabilité | — |
| **NDC** | Number of Distinct Categories — nombre de catégories distinctes que peut discerner l'instrument | — |

---

## 1️⃣ — Répétabilité et Reproductibilité

### Répétabilité (Equipment Variation — EV)

DÉFINITION :  
Variabilité observée quand UN SEUL opérateur mesure le MÊME objet  
PLUSIEURS FOIS avec le MÊME instrument dans les MÊMES conditions.  

CAUSES de la non-répétabilité :  
→ Résolution limitée de l'instrument (arrondi au dernier chiffre)  
→ Bruit électronique de l'instrument  
→ Instabilité de l'objet mesuré (température qui dérive)  
→ Vibrations mécaniques  
→ Variations de l'interface pièce/instrument (contact sondes)  

CALCUL :  
Effectuer n mesures → calculer σ_EV (écart-type des n mesures)  

$$σ_EV = \sqrt(Σ(xi - x̄)^2 / (n-1))$$

Ou méthode des étendues (plus rapide) :  

$$σ_EV = R̄ / d2$$

avec R̄ = étendue moyenne des groupes de mesures  
et d2 = constante statistique (d2 = 1,128 pour n=2 · 1,693 pour n=3 · 2,059 pour n=5)  

### Reproductibilité (Appraiser Variation — AV)

```
DÉFINITION :
  Variabilité observée quand DIFFÉRENTS opérateurs mesurent le MÊME objet
  avec le MÊME instrument.

CAUSES de la non-reproductibilité :
  → Formation insuffisante des opérateurs
  → Différences dans la façon de positionner l'instrument
  → Interprétation différente des modes opératoires
  → Fatigue, conditions physiques différentes

CALCUL :
  Comparer les MOYENNES de chaque opérateur :
  AV = x̄_max − x̄_min   (étendue des moyennes inter-opérateurs)
  
  σ_AV = √max(AV²/n − σ_EV²/(n×p) ; 0)
    avec n = nombre de mesures par opérateur par pièce
    et p = nombre de pièces mesurées
    (si le terme sous la racine est négatif → σ_AV = 0 par convention)
```

---

**🖼️ ILLUSTRATION 1 — Répétabilité vs Reproductibilité**
> *Légende* : Quatre cibles de tir côte à côte illustrant les 4 combinaisons possibles. Cible 1 "Bonne répétabilité + bonne reproductibilité" : 3 groupes de points serrés, chaque groupe proche du centre (idéal). Cible 2 "Bonne répétabilité + mauvaise reproductibilité" : 3 groupes de points serrés, mais les groupes sont dispersés loin les uns des autres. Cible 3 "Mauvaise répétabilité + bonne reproductibilité" : 3 groupes dispersés mais centrés au même endroit. Cible 4 "Mauvaise répétabilité + mauvaise reproductibilité" : chaos total. Chaque groupe de points a une couleur différente (opérateur A=bleu, B=rouge, C=vert).
>
> **Prompt illustration** : *"Repeatability vs Reproducibility target diagram in French. Four archery targets side by side. Target 1 'Bonne répétabilité + Reproductibilité': 3 tight clusters of dots near center, each cluster labeled Op.A (blue), Op.B (red), Op.C (green) - ideal. Target 2 'Bonne répétabilité, mauvaise reproductibilité': 3 tight clusters but spread far apart. Target 3 'Mauvaise répétabilité, bonne reproductibilité': 3 spread-out clusters near same center area. Target 4 'Les deux mauvaises': chaotic dots everywhere. French labels under each target. Archery target diagram style with concentric circles"*

---

## 2️⃣ — Le Gauge R&R : méthode industrielle

### Pourquoi le Gauge R&R ?

```
En industrie (automobile, aéronautique, médical) :
  → Avant d'utiliser un système de mesure en production, il faut PROUVER qu'il est capable.
  → La norme IATF 16949 (automobile) et ISO 9001 exigent une étude MSA.
  → Un instrument défaillant prend de bonnes pièces pour des mauvaises (faux rebut)
    ou des mauvaises pièces pour des bonnes (risque qualité grave).

Pour un système IoT industriel :
  → Un capteur "malade" peut déclencher de fausses alertes (coût d'intervention)
  → Ou rater une vraie alerte (risque sécurité)
  → Le %GRR permet de décider si le capteur est apte à la surveillance.
```

### Protocole Gauge R&R simplifié

PROTOCOLE (version cours BAC PRO) :  
k = 2 opérateurs (A et B)  
n = 5 mesures par opérateur  
p = 1 pièce (pour simplifier)  

ÉTAPE 1 — Mesures :  
Opérateur A : effectue n mesures → calcule x̄_A et σ_A (ou R_A)  
Opérateur B : effectue n mesures → calcule x̄_B et σ_B (ou R_B)  

ÉTAPE 2 — Répétabilité (EV) :  
σ_EV = (σ_A + σ_B) / 2   (moyenne des écarts-types des opérateurs)  

Ou avec les étendues :  
σ_EV = R̄ / d2   avec R̄ = (R_A + R_B)/2 · d2 = 1,693 (pour n=5)  

ÉTAPE 3 — Reproductibilité (AV) :  
AV_brut = |x̄_A − x̄_B|   (différence entre les moyennes)  
σ_AV = √max( AV_brut²/n − σ_EV²/(n×p) ; 0 )  

Simplification fréquente si 1 seule pièce (p=1) :  
σ_AV ≈ |x̄_A − x̄_B| / √n   (approximation acceptable)  

ÉTAPE 4 — GRR total :  

$$σ_GRR = \sqrt(σ_EV^2 + σ_AV^2)$$

ÉTAPE 5 — %GRR :  
%GRR = (5,15 × σ_GRR / Tolérance) × 100  

Le facteur 5,15 = 2 × 2,575 = couvre 99% de la distribution normale  

### Interprétation du %GRR

```
%GRR < 10%       → ✓✓ EXCELLENT
                    Le système de mesure est accepté sans restriction.

10% ≤ %GRR ≤ 30% → ✓ ACCEPTABLE (conditionnel)
                    Accepté selon l'importance de l'application.
                    Action possible : former les opérateurs, améliorer la procédure.

%GRR > 30%       → ✗ INACCEPTABLE
                    Le système de mesure doit être amélioré ou remplacé.
                    On "gaspille" plus de 30% de la tolérance juste en incertitude de mesure.

NDC (Number of Distinct Categories) :
  NDC = 1,41 × (σ_pièce / σ_GRR)
  NDC ≥ 5 → instrument capable de distinguer les pièces conformes des non-conformes.
```

---

**🖼️ ILLUSTRATION 2 — Interprétation graphique du %GRR**
> *Légende* : Barre horizontale représentant l'intervalle de tolérance total (de −Tol à +Tol). Une zone hachurée rouge à gauche représente la "part de la tolérance consommée par le GRR" (5,15 × σ_GRR). Trois cas superposés : cas 1 (%GRR=8%, zone rouge petite = vert "EXCELLENT"), cas 2 (%GRR=20%, zone rouge plus grande = jaune "ACCEPTABLE"), cas 3 (%GRR=40%, zone rouge occupe presque tout l'intervalle = rouge "INACCEPTABLE"). La zone bleue restante représente "ce qu'il reste pour distinguer les pièces".
>
> **Prompt illustration** : *"GRR percentage interpretation diagram in French. Horizontal tolerance bar showing total tolerance range. Three stacked scenarios: Case 1 '%GRR=8%': small red hatched zone on left labeled 'Incertitude de mesure' green label 'EXCELLENT ✓✓'. Case 2 '%GRR=20%': medium red zone yellow label 'ACCEPTABLE ✓'. Case 3 '%GRR=40%': large red zone covering most of bar red label 'INACCEPTABLE ✗'. Blue zone labeled 'Marge pour distinguer les pièces'. Threshold lines at 10% and 30%. French labels, quality engineering diagram style"*

---

## 3️⃣ — Limite de détection d'un instrument

### Pourquoi une limite de détection ?

```
PROBLÈME :
  Un capteur de température DHT22 a un bruit de ±0,3°C (σ_répétabilité).
  Un ingénieur veut détecter une variation de 0,1°C dans une serre.
  Est-ce possible ?

RÉPONSE : NON — la variation de 0,1°C est noyée dans le bruit de 0,3°C.
  On ne peut pas distinguer une vraie variation d'un artefact de mesure.
  
LA LIMITE DE DÉTECTION :
  = La plus petite variation qu'un instrument peut détecter avec fiabilité.
```

### Formules de la limite de détection

À PARTIR DU BRUIT DE FOND σ_bruit = σ_répétabilité (quand on mesure une valeur fixe) :  

LDD (Limite de Décision de Détection) :  
LDD = 1,65 × σ_bruit  
→ Signal au-dessus de LDD : 95% de chance que ce soit un vrai signal  

LD (Limite de Détection) :  
LD  = 3,3 × σ_bruit  
→ Signal au-dessus de LD : erreur < 5% sur la décision de détection  

RÈGLE PRATIQUE SIMPLIFIÉE :  
LD ≈ 3 × σ_bruit   (règle "3-sigma", très utilisée en pratique)  

Un signal n'est détectable de façon fiable que si sa valeur > LD.  

APPLICATION AU DHT22 (σ_répétabilité = 0,3°C) :  

$$LDD = 1{,}65 \times 0{,}3 = 0{,}50\,\mathrm{°C}$$

$$LD = 3{,}3 \times 0{,}3 = 0{,}99\,\mathrm{°C} \approx 1\,\mathrm{°C}$$

→ Le DHT22 peut détecter de façon fiable des variations ≥ 1°C.  
→ Une variation de 0,1°C est INDÉTECTABLE avec ce capteur.  

### Lien entre σ, résolution et LD

```
RÉSOLUTION ≠ PRÉCISION ≠ LIMITE DE DÉTECTION :

  Résolution = plus petit incrément affiché (ex: 0,1°C pour le DHT22)
  Précision   = erreur max par rapport à la vraie valeur (ex: ±0,5°C spéc.)
  LD          = plus petite VARIATION détectable (dépend du bruit réel)

Exemple :
  Oscilloscope numérique 8 bits :
    Résolution verticale  : 1/256 de la pleine échelle = 3,9 mV pour 1V/div
    σ_bruit observé       : 5 mV
    LD                    : 3 × 5 = 15 mV
  → Le signal affiché semble avoir 4 mV de résolution, mais on ne peut détecter 
    de façon fiable que des signaux supérieurs à 15 mV.
```

---

## 4️⃣ — Choisir un instrument pour une application

### Ratio signal/bruit et critère de sélection

```
Pour qu'une mesure soit fiable :
  Variation à mesurer ≥ LD = 3 × σ_bruit

CRITÈRE DE SÉLECTION D'UN INSTRUMENT :
  σ_bruit ≤ (Variation à mesurer) / 3

EXEMPLE — Choisir entre 3 capteurs pour surveiller une variation de 0,5°C :

  Capteur A : σ_répétabilité = 0,1°C → LD = 0,3°C ≤ 0,5°C → ✓ ADAPTÉ
  Capteur B : σ_répétabilité = 0,2°C → LD = 0,6°C > 0,5°C → ✗ INSUFFISANT
  Capteur C : σ_répétabilité = 0,5°C → LD = 1,5°C >> 0,5°C → ✗✗ INADAPTÉ
```

### Application au Gauge R&R — Critère d'aptitude

```
Un système de mesure est apte si :
  (1) %GRR < 30%  (préférence : < 10%)
  (2) NDC ≥ 5
  (3) LD < (plus petite différence à détecter entre pièces)

Ces 3 conditions ENSEMBLE définissent un système de mesure CAPABLE.
```

---

## 📌 Les essentiels à retenir

> ✅ **Répétabilité** = variabilité d'un seul opérateur · calculer σ_EV
> ✅ **Reproductibilité** = variabilité entre opérateurs · calculer σ_AV
> ✅ **GRR** = √(σ_EV² + σ_AV²) · **%GRR** = 5,15 × σ_GRR / Tolérance × 100
> ✅ **%GRR < 10%** = excellent · **10-30%** = acceptable · **> 30%** = inacceptable
> ✅ **LD ≈ 3 × σ_bruit** (règle pratique des 3 sigma)
> ✅ Un signal n'est détectable que s'il est **> LD**
> ✅ **Résolution ≠ Précision ≠ Limite de détection** (3 concepts distincts !)
> ✅ NDC ≥ 5 → instrument peut distinguer les pièces entre elles
> ✅ Cause principale de mauvaise répétabilité : bruit de l'instrument
> ✅ Cause principale de mauvaise reproductibilité : formation insuffisante des opérateurs

---

*Fiche de Cours Métrologie R&R — BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S8*
*Compétences : S8.1 · S8.2 · S8.3 · S8.4 · C8.1*
