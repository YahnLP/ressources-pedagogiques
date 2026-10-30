# 📘 FICHE DE COURS — S11 · 2ᵉ ANNÉE · E2
## Fiabilité des Composants : MTBF · MTTR · Loi Exponentielle · Systèmes Série/Parallèle

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences travaillées** : S6.1 · S6.2 · S6.3 · S6.4 · S6.5 · C6.1

---

## 🔑 Vocabulaire clé

| Terme | Symbole | Définition | Unité |
|---|---|---|---|
| **Fiabilité** | R(t) | Probabilité qu'un composant fonctionne encore à l'instant t | Adimensionnel [0;1] |
| **Taux de panne** | λ (lambda) | Nombre moyen de pannes par unité de temps | pannes/heure |
| **MTBF** | — | Mean Time Between Failures — temps moyen entre deux pannes | heures |
| **MTTF** | — | Mean Time To Failure — temps moyen avant la 1ère panne (non réparable) | heures |
| **MTTR** | — | Mean Time To Repair — temps moyen de réparation | heures |
| **Disponibilité** | D | Fraction du temps où le système est opérationnel | % |
| **Indisponibilité** | Q | Fraction du temps où le système est en panne (Q = 1 − D) | % |
| **Durée de vie** | — | Durée pendant laquelle un composant est garanti fonctionnel | heures |
| **Redondance** | — | Duplication de composants pour améliorer la fiabilité | — |

---

## 1️⃣ — MTBF, MTTR et disponibilité

### MTBF : Mean Time Between Failures

```
MTBF = Temps total de fonctionnement (TO)
       ────────────────────────────────────
          Nombre de pannes (n)

Exemple :
  Un disque dur fonctionne 87 600 heures (10 ans) et tombe en panne 3 fois.
  MTBF = 87 600 / 3 = 29 200 heures ≈ 3,3 ans entre deux pannes

Interprétation :
  MTBF = 50 000 h → en fonctionnement 24h/24 → panne probable dans 5,7 ans
  MTBF = 500 000 h → panne probable dans 57 ans (quasi immortel !)
  
  ⚠️ MTBF ≠ durée de vie garantie
     C'est un indicateur STATISTIQUE : 50% des composants tomberont en panne
     AVANT le MTBF, et 50% APRÈS.
```

### MTTR : Mean Time To Repair

```
MTTR = Temps total d'arrêt (TA)
       ──────────────────────────
         Nombre de pannes (n)

MTTR inclut :
  → Temps de détection de la panne
  → Temps d'attente de l'intervention
  → Temps de diagnostic
  → Temps de réparation proprement dit
  → Temps de test et remise en service

Pour réduire le MTTR :
  ✓ Avoir des pièces de rechange en stock (gestion de stock)
  ✓ Former les techniciens aux procédures
  ✓ Systèmes de diagnostic automatique (alertes, logs)
  ✓ Modules facilement remplaçables (hot-swap)
```

### Disponibilité

```
           MTBF                  TO
D = ──────────────────  =  ──────────────
       MTBF + MTTR             TO + TA


Exemple numérique :
  MTBF = 2 500 h · MTTR = 3,6 h
  D = 2 500 / (2 500 + 3,6) = 2 500 / 2 503,6 = 0,9986 = 99,86%

Classes de disponibilité industrielle :
  99%       → 3,65 jours d'arrêt / an  (industrie non critique)
  99,9%     → 8,76 heures / an         ("three nines")
  99,99%    → 52,6 minutes / an        ("four nines")
  99,999%   → 5,26 minutes / an        ("five nines" — datacenter Tier IV)
```

---

**🖼️ ILLUSTRATION 1 — Chronologie MTBF / MTTR**
> *Légende* : Frise chronologique horizontale. Le temps s'écoule de gauche à droite. Alternance de zones vertes (fonctionnement = TO) et rouges (arrêt = TA). Les zones vertes sont larges, les rouges sont étroites. Des flèches doubles annotent : "MTBF = temps moyen entre pannes" entre deux zones rouges, "MTTR = durée moyenne de réparation" sur une zone rouge. En dessous, une formule : D = MTBF / (MTBF + MTTR). Les valeurs numériques 2500h et 3,6h sont indiquées.
>
> **Prompt illustration** : *"MTBF MTTR availability timeline diagram in French. Horizontal timeline with alternating green zones 'Fonctionnement (TO)' and thin red zones 'Arrêt (TA)'. Double-headed arrow between two red zones labeled 'MTBF = temps moyen entre pannes (ex: 2500h)'. Double-headed arrow on single red zone labeled 'MTTR = temps moyen réparation (ex: 3.6h)'. Formula below: 'D = MTBF / (MTBF + MTTR) = 99,86%'. Green=functioning, red=failure. French labels, technical timeline diagram"*

---

## 2️⃣ — Taux de panne λ et loi exponentielle

### Le taux de panne λ (lambda)

```
λ (lambda) = taux de panne = nombre de pannes par unité de temps

           1
λ = ──────────
       MTBF

Exemples :
  DHT22 (MTBF = 50 000 h)     → λ = 1/50 000 = 2×10⁻⁵ pannes/heure
  Disque dur (MTBF = 300 000 h)→ λ = 1/300 000 = 3,3×10⁻⁶ pannes/heure
  LED (MTBF = 25 000 h)       → λ = 1/25 000 = 4×10⁻⁵ pannes/heure

Unités alternatives :
  FIT (Failure In Time) = λ × 10⁹ (pannes pour 10⁹ heures)
  Ex : λ = 2×10⁻⁵ /h → 20 000 FIT (courant pour composants électroniques)
```

### La loi exponentielle de fiabilité

```
Pour la période de vie utile (taux de panne constant) :

R(t) = e^(−λt)    ← Probabilité de fonctionner encore à l'instant t

F(t) = 1 − R(t) = 1 − e^(−λt)  ← Probabilité d'être tombé en panne avant t

Où :
  e ≈ 2,718 (base de l'exponentielle naturelle)
  λ = taux de panne (1/MTBF)
  t = durée de fonctionnement
```

### Calcul pratique avec la calculatrice

Pour calculer e^(−λt) :  
Méthode 1 : touche [e^x] → entrer (−λt)  
Méthode 2 : touche [e] × [x] → EXP puis le nombre  

Exemple :  
MTBF = 50 000 h · λ = 1/50 000 = 2×10⁻⁵ h⁻¹  
Quelle est la fiabilité après 1 an (8 760 h) ?  

$$R(8760) = e^(-2 \times 10⁻⁵ \times 8760)$$

$$= e^(-0{,}1752)$$

$$= 0{,}839$$

$$= 83{,}9\,\mathrm{\%}$$

Probabilité de panne dans l'année : F = 1 − 0,839 = 16,1%  

### Vérification : à t = MTBF, R = ?

```
R(MTBF) = e^(−λ × MTBF) = e^(−1/MTBF × MTBF) = e^(−1) ≈ 0,368

À t = MTBF : il reste 36,8% de chances que le composant fonctionne encore.
Autrement dit : 63,2% des composants sont tombés en panne avant d'atteindre le MTBF.

C'est pourquoi MTBF ≠ durée de vie garantie !
```

---

**🖼️ ILLUSTRATION 2 — Courbe R(t) = e^(−λt)**
> *Légende* : Graphe de la fonction R(t) en fonction du temps. L'axe Y va de 0 à 1 (ou 0 à 100%). L'axe X représente le temps en multiples de MTBF (0 à 3×MTBF). La courbe exponentielle décroissante part de R(0)=1 et diminue. Trois points sont annotés : à t=MTBF → R=0,368 (36,8%), à t=2×MTBF → R=0,135 (13,5%), à t=3×MTBF → R=0,050 (5%). Une ligne horizontale en pointillés indique R=0,368. La zone sous la courbe est colorée en vert (fonctionnement probable) et au-dessus de F(t)=1-R(t) en rouge (probabilité de panne). La formule R(t)=e^-λt est inscrite.
>
> **Prompt illustration** : *"Exponential reliability curve R(t) in French. X-axis labeled 'Temps (multiple du MTBF)' with values 0, MTBF, 2×MTBF, 3×MTBF. Y-axis labeled 'Fiabilité R(t)' from 0 to 1 (or 0% to 100%). Decreasing exponential curve from R(0)=1. Three annotated points: (MTBF, 0.368) labeled '36,8% encore opérationnels', (2×MTBF, 0.135), (3×MTBF, 0.050). Dashed horizontal line at R=0.368. Formula 'R(t) = e^(-λt)' in top right. Green shading under curve, red above for F(t)=1-R(t). French labels, mathematical plot style"*

---

## 3️⃣ — La courbe en baignoire

```
La durée de vie d'un composant se découpe en 3 phases :

λ (taux de panne)
│
│  \               
│   \  Pannes       ___________  Pannes     /
│    \  jeunesses  |             d'usure   /
│     \___________|   Vie utile           /
│                  (λ constant)          
└──────────────────────────────────────────→ Temps

PHASE 1 — Mortalité infantile (λ décroissant) :
  Pannes dues aux défauts de fabrication
  → Se manifeste lors du "rodage" ou des tests en usine
  → C'est pourquoi les constructeurs font du "burn-in"

PHASE 2 — Vie utile (λ constant) :
  → Pannes aléatoires, indépendantes du temps
  → La loi exponentielle s'applique ici
  → C'est la phase normale de fonctionnement
  → MTBF est valable dans cette phase

PHASE 3 — Vieillissement (λ croissant) :
  → Usure normale des matériaux
  → Les condensateurs électrolytiques vieillissent (ESR augmente)
  → Les LED perdent de la luminosité
  → Préconisation : remplacement préventif avant cette phase
```

---

## 4️⃣ — Fiabilité des systèmes série

### Schéma série : tous les composants doivent fonctionner

```
[C1] ──── [C2] ──── [C3] ──── ... ──── [Cn]

Si un seul composant tombe en panne → tout le système est en panne

Fiabilité du système série :
Rs = R1 × R2 × R3 × ... × Rn

MTBF du système série :
λs = λ1 + λ2 + λ3 + ... + λn  →  MTBFs = 1/λs
```

### Exemple : carte ESP32 avec 4 composants critiques

Composant       | MTBF (h)    | λ (pannes/h)  
ESP32 module    | 100 000     | 10⁻⁵  
DHT22           | 50 000      | 2×10⁻⁵  
Alimentation    | 80 000      | 1,25×10⁻⁵  
Condensateur    | 60 000      | 1,67×10⁻⁵  

λsystème = 10⁻⁵ + 2×10⁻⁵ + 1,25×10⁻⁵ + 1,67×10⁻⁵  

$$= (1 + 2 + 1{,}25 + 1{,}67) \times 10⁻⁵$$

= 5,92 × 10⁻⁵ pannes/heure  

MTBFsystème = 1 / 5,92×10⁻⁵ = 16 892 heures ≈ 1,9 ans  

Vérification avec R(t) après 8 760 h (1 an) :  

$$R_{1}(8760) = e^(-10⁻⁵ \times 8760) = e^(-0{,}0876) = 0{,}916$$

$$R_{2}(8760) = e^(-2 \times 10⁻⁵ \times 8760) = e^(-0{,}1752) = 0{,}839$$

$$R_{3}(8760) = e^(-1{,}25 \times 10⁻⁵ \times 8760) = e^(-0{,}1095) = 0{,}896$$

$$R_{4}(8760) = e^(-1{,}67 \times 10⁻⁵ \times 8760) = e^(-0{,}1463) = 0{,}864$$

$$Rs(8760) = 0{,}916 \times 0{,}839 \times 0{,}896 \times 0{,}864 = 0{,}594$$

= 59,4% de chances de fonctionner encore après 1 an  

Observation : en série, plus on ajoute de composants, PLUS le système est fragile.  

---

**🖼️ ILLUSTRATION 3 — Fiabilité série vs parallèle**
> *Légende* : Deux diagrammes côte à côte avec des niveaux de fiabilité. Gauche "Série" : 3 blocs en ligne [R=0,9]-[R=0,9]-[R=0,9], flèche vers "Rs = 0,9³ = 0,729" en rouge (72,9%). Droite "Parallèle" : 3 blocs verticaux [R=0,9] en parallèle, flèche vers "Rs = 1-(0,1)³ = 0,999" en vert (99,9%). Un curseur montre visuellement la différence. En bas : "Série = plus fragile · Parallèle = plus fiable".
>
> **Prompt illustration** : *"Series vs parallel reliability diagram in French. Left panel 'Système Série': three blocks in a row labeled R₁=0.9, R₂=0.9, R₃=0.9 connected by lines, result arrow showing 'Rs = 0.9 × 0.9 × 0.9 = 0.729' in red box, label '72.9% - Moins fiable qu'un seul composant!'. Right panel 'Système Parallèle': three blocks stacked vertically labeled R₁=0.9, R₂=0.9, R₃=0.9 with branching connections, result arrow showing 'Rs = 1-(0.1)³ = 0.999' in green box, label '99.9% - Très fiable!'. Bottom comparison bar. French labels, reliability engineering diagram style"*

---

## 5️⃣ — Fiabilité des systèmes parallèle

### Schéma parallèle : un seul composant suffit

┌── [C1] ──┐
│           │
────►├── [C2] ──┼────►
│           │
└── [C3] ──┘

Le système tombe en panne seulement si TOUS les composants tombent en panne

Fiabilité du système parallèle :
Rs = 1 − (1−R1) × (1−R2) × (1−R3) × ... × (1−Rn)

MTBF approximatif pour 2 composants identiques (R1 = R2 = R) :
MTBFs ≈ MTBF × (1 + 1/2) = 1,5 × MTBF  (approximation)

### Exemple : deux alimentations redondantes

Alimentation A : MTBF = 80 000 h · R(8760) = e^(−8760/80000) = e^(−0,1095) = 0,896  
Alimentation B : MTBF = 80 000 h · même fiabilité  

$$Rs(8760) = 1 - (1 - 0{,}896) \times (1 - 0{,}896)$$

$$= 1 - 0{,}104 \times 0{,}104$$

$$= 1 - 0{,}0108$$

$$= 0{,}9892 = 98{,}92\,\mathrm{\%}$$

Comparaison :  
1 alimentation → R = 89,6%  
2 alimentations en parallèle → R = 98,9%  
Gain en fiabilité : +9,3 points !  

---

## 6️⃣ — Systèmes complexes (série + parallèle)

### Méthode de décomposition

```
ÉTAPE 1 : Identifier les blocs en parallèle → Calculer leur fiabilité équivalente
ÉTAPE 2 : Les remplacer par un seul bloc équivalent
ÉTAPE 3 : Calculer la fiabilité du système série résultant
```

### Exemple : système IoT industriel

```
Architecture :
  [Capteur 1 (R=0,90)] ─┐
  [Capteur 2 (R=0,90)] ─┴→ [CPU (R=0,95)] → [Réseau (R=0,98)] → [Serveur (R=0,99)]

ÉTAPE 1 : Fiabilité des 2 capteurs en parallèle
  R_capteurs = 1 − (1−0,90)(1−0,90)
             = 1 − 0,10 × 0,10
             = 1 − 0,01
             = 0,99

ÉTAPE 2 : Système réduit (tout en série)
  [0,99] → [0,95] → [0,98] → [0,99]

ÉTAPE 3 : Fiabilité totale
  Rs = 0,99 × 0,95 × 0,98 × 0,99
     = 0,99 × 0,95 × 0,98 × 0,99
     = 0,911
     = 91,1%
```

---

## 📌 Récapitulatif des formules

> [!NOTE] λ = 1/MTBF                   (taux de panne)
> MTBF = TO / n                (temps moyen entre pannes)  
> MTTR = TA / n                (temps moyen de réparation)  
> D = MTBF / (MTBF + MTTR)     (disponibilité)  
> R(t) = e^(−λt)               (fiabilité à l'instant t)  
> F(t) = 1 − R(t)              (probabilité de panne avant t)  
>
> SÉRIE   : Rs = R1 × R2 × R3    λs = λ1 + λ2 + λ3  
> PARALLÈLE : Rs = 1−(1−R1)(1−R2)  

---

## 📌 Les essentiels à retenir pour l'examen

> ✅ **MTBF** = TO / n → temps MOYEN entre pannes (pas durée de vie garantie !)
> ✅ **MTTR** = TA / n → plus court = meilleure maintenabilité
> ✅ **D = MTBF / (MTBF + MTTR)** → proche de 1 = très disponible
> ✅ **λ = 1/MTBF** → plus λ est petit, plus le composant est fiable
> ✅ **R(t) = e^(−λt)** → à t=MTBF : R = e^(−1) ≈ **36,8%**
> ✅ **Série** : Rs = R1 × R2 → PLUS fragile (Rs < Rmin)
> ✅ **Parallèle** : Rs = 1−(1−R1)(1−R2) → PLUS fiable (Rs > Rmax)
> ✅ La **courbe en baignoire** montre les 3 phases : mortalité infantile, vie utile, usure
> ✅ FIT = λ × 10⁹ (unité industrielle du taux de panne)

---

*Fiche de Cours Fiabilité — BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S11*
*Compétences : S6.1 · S6.2 · S6.3 · S6.4 · S6.5 · C6.1*
