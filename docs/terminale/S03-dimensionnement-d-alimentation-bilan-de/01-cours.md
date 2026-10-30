# 📘 FICHE DE COURS — S3 · 3ᵉ ANNÉE · E2
## Dimensionnement d'Alimentation : Bilan de Puissance · Régulateurs · Calcul Thermique

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences** : S2.1 · S2.2 · S2.3 · C2.1

---

## 🔑 Vocabulaire clé

| Terme | Définition | Unité |
|---|---|---|
| **Bilan de puissance** | Tableau listant la puissance consommée par chaque composant | W |
| **Courant de pointe (peak)** | Courant maximal momentané (ex: démarrage WiFi) | A |
| **Courant moyen** | Courant moyen sur un cycle complet | A (mA) |
| **Régulateur linéaire** | Fait chuter la tension en dissipant l'excès en chaleur | — |
| **LDO** | Low Drop-Out : régulateur linéaire à faible chute de tension | — |
| **Régulateur à découpage (SMPS)** | Convertit la tension par commutation rapide · rendement élevé | — |
| **Buck (abaisseur)** | Convertisseur à découpage qui abaisse la tension (Vout < Vin) | — |
| **Boost (élévateur)** | Convertisseur à découpage qui élève la tension (Vout > Vin) | — |
| **Buck-Boost** | Peut abaisser et élever selon les conditions | — |
| **Rendement η** | Rapport puissance utile / puissance absorbée | % |
| **Pdiss** | Puissance dissipée en chaleur | W |
| **Rθja** | Résistance thermique jonction-air (sans radiateur) | °C/W |
| **Rθjc** | Résistance thermique jonction-boîtier | °C/W |
| **Rθsa** | Résistance thermique radiateur-air | °C/W |
| **Tj** | Température de jonction (interne au composant) | °C |
| **Tj max** | Température maximale tolérée par le composant | °C |
| **Marge thermique** | Tj max − Tj calculée | °C |

---

## 1️⃣ — Le bilan de puissance

### Pourquoi établir un bilan ?

```
AVANT de choisir l'alimentation d'un système, il faut savoir :
  → Quelle est la puissance TOTALE consommée ?
  → Quel est le COURANT de POINTE (pour dimensionner la source) ?
  → Quel est le COURANT MOYEN (pour calculer l'autonomie) ?

Un bilan mal fait → régulateur sous-dimensionné → surchauffe → panne
                 → batterie surestimée → autonomie insuffisante
```

### Méthode : tableau de bilan de puissance

```
Remplir pour chaque composant :

┌────────────────┬───────────┬──────────┬───────────┬──────────────┬──────────────┐
│ Composant      │ Vcc (V)   │ I_pic (mA)│ I_moy (mA)│ P_moy (mW)  │ Mode         │
├────────────────┼───────────┼──────────┼───────────┼──────────────┼──────────────┤
│ ESP32 WiFi TX  │ 3,3       │ 250       │ 80        │ 264          │ Actif WiFi   │
│ DHT22          │ 3,3       │ 2         │ 1         │ 3            │ Actif        │
│ MQ-2 (chauf.)  │ 5,0       │ 150       │ 150       │ 750          │ Toujours ON  │
│ LED rouge      │ 3,3       │ 20        │ 10        │ 33           │ 50% duty     │
├────────────────┼───────────┼──────────┼───────────┼──────────────┼──────────────┤
│ TOTAL @3,3V    │ —         │ 272       │ 91        │ 300          │ —            │
│ TOTAL @5V      │ —         │ 150       │ 150       │ 750          │ —            │
└────────────────┴───────────┴──────────┴───────────┴──────────────┴──────────────┘

Note : Le courant du régulateur 3,3V ≈ I_total_3,3V = 91 mA moyen, 272 mA de pointe
       Le courant du régulateur 5V  ≈ I_total_5V  = 150 mA
```

### Règle de dimensionnement de la source

```
COURANT DE LA SOURCE ≥ I_pic_total × 1,25   (marge de sécurité 25%)

Exemple : I_pic = 272 mA @ 3,3V + 150 mA @ 5V
          → Source 5V : I_requis = 272 mA + 150 mA + (Pdiss régulateur / 5V)
```

---

## 2️⃣ — Les régulateurs de tension

### Régulateur linéaire

```
PRINCIPE :
  Le composant de passage (transistor bipolaire ou MOS) est toujours conducteur.
  Il dissipe l'excès d'énergie sous forme de chaleur.
  
  Vin ────[Transistor passant]──── Vout (fixe)
                  │
               Chaleur ↓
  
FORMULE CLÉ :
  Pdiss = (Vin − Vout) × Iout

RENDEMENT :
  η = Vout × Iout / (Vin × Iin) ≈ Vout / Vin  (pour Iin ≈ Iout)

EXEMPLES :
  LM7805 : 9V → 5V, 1A, boîtier TO-220, Rθja = 65°C/W
  LM1117-3.3 : 5V → 3,3V, 0,8A, SOT-223, Rθja = 50°C/W
  AMS1117-3.3 : 5V → 3,3V, 1A, SOT-223, Rθja = 44°C/W

AVANTAGES :
  ✓ Simple (peu de composants externes)
  ✓ Tension de sortie très stable (pas de bruit HF)
  ✓ Très bon marché (< 0,50€)
  ✓ Pas d'émissions CEM

INCONVÉNIENTS :
  ✗ Faible rendement si Vin >> Vout
  ✗ Forte dissipation thermique → chauffe
  ✗ Gaspille de l'énergie → mauvais pour les batteries

LDO (Low Drop-Out) = variante du linéaire :
  Tension minimale Vin − Vout ≥ 0,3 à 1,5 V (selon le modèle)
  (vs 2,5V minimum pour un 78xx classique)
  → Utilisable avec batterie Li-ion en décharge
```

---

**🖼️ ILLUSTRATION 1 — Linéaire vs Découpage**
> *Légende* : Deux schémas côte à côte. Gauche "Régulateur linéaire" : source 9V → boîtier TO-220 avec flèche de chaleur rouge vers le bas · Vout=5V · rendement = 5/9 = 55%. Zone rouge = énergie perdue. Droite "Convertisseur à découpage (Buck)" : source 9V → bobine + condensateur + commutateur avec signal carré · Vout=5V · rendement ≈ 90%. Zone verte dominante = énergie utile. Graphes d'énergie en dessous montrant la différence visuellement.
>
> **Prompt illustration** : *"Linear regulator vs switching regulator comparison in French. Left panel 'Régulateur Linéaire': 9V source, TO-220 package with red downward arrow 'Chaleur (Pdiss)', output 5V, efficiency formula 'η = 5/9 = 55%', large red zone labeled 'Énergie perdue'. Right panel 'Convertisseur Buck': 9V source, inductor+capacitor+switch circuit with PWM signal, output 5V, efficiency 'η ≈ 90%', large green zone 'Énergie utile', small red zone '10% perdu'. Bar charts below comparing efficiency. French labels, power electronics diagram"*

---

### Régulateur à découpage (SMPS / Buck / Boost)

```
PRINCIPE :
  Un interrupteur (transistor MOS) commute à haute fréquence (100 kHz à 2 MHz).
  Un filtre LC lisse la tension de sortie.
  La bobine stocke et restitue l'énergie → pas de dissipation en chaleur.
  
RENDEMENT :
  η = 80 à 95% typique (vs 30-60% pour le linéaire)

EXEMPLES :
  LM2596 : réglable ou fixe (5V/3,3V), 3A, fréquence 150 kHz, boîtier TO-263
  MP2315 : buck compact, 3A, 500 kHz, SOT-23-8 (PCB très compact)
  TPS54360 : 60V input, 3,5A, 100 kHz-2,5 MHz, TI premium

COMPOSANTS EXTERNES NÉCESSAIRES :
  Bobine (inductance) · Condensateurs d'entrée et sortie · Diode ou synchrone
  → Plus de composants, mais efficacité bien supérieure

AVANTAGES :
  ✓ Rendement élevé → autonomie batterie × 2 à × 3
  ✓ Peu de dissipation thermique → pas ou peu de radiateur
  ✓ Efficace même avec Vin >> Vout

INCONVÉNIENTS :
  ✗ Génère du bruit HF (ripple de tension en sortie)
  ✗ Plus complexe à concevoir (bobine, condensateurs spécifiques)
  ✗ Plus cher (x3 à x10 vs linéaire)
  ✗ Émissions CEM ! → nécessite blindage et filtrage soigneux
```

### Tableau de choix

```
CHOISIR un RÉGULATEUR LINÉAIRE si :
  → Vin − Vout < 2V (faible écart → faible dissipation de toute façon)
  → Courant < 500 mA et alimentation sur secteur (pas sur batterie)
  → Signal analogique sensible à côté (ADC, audio) → pas de bruit HF
  → Contrainte CEM sévère
  → Budget très serré

CHOISIR un RÉGULATEUR À DÉCOUPAGE si :
  → Vin − Vout ≥ 2V ET courant ≥ 200 mA
  → Alimentation sur batterie → autonomie critique
  → Courant > 1A
  → La CEM peut être gérée (filtrage, blindage)
```

---

## 3️⃣ — Calcul thermique

### Le modèle thermique simple

```
Analogie électrique :
  Puissance P (W)     ↔  Courant électrique (A)
  Température T (°C)  ↔  Tension électrique (V)
  Résistance Rθ (°C/W)↔  Résistance électrique (Ω)
  
  ΔT = P × Rθ   (comme ΔV = I × R)
```

### Calcul de Tj sans radiateur

```
Tj = Tamb + Pdiss × Rθja

Tj max (datasheet) = 125°C pour la plupart des régulateurs courants
Tamb typique = 25°C (laboratoire) ou 50-70°C (boîtier industriel en été)

Exemple : LM7805, Vin=9V, Vout=5V, Iout=200mA, Tamb=25°C
  Pdiss = (9−5) × 0,200 = 0,8 W
  Rθja  = 65°C/W (TO-220 sans radiateur)
  Tj    = 25 + 0,8 × 65 = 25 + 52 = 77°C

Marge thermique = 125 − 77 = 48°C ← CORRECT (marge suffisante)

Règle pratique : Tj ne doit pas dépasser Tj_max − 20°C (marge de sécurité)
  → Tj max exploitable = 125 − 20 = 105°C
```

### Calcul de Tj avec radiateur

```
Quand utiliser un radiateur ?
  Si Tj calculé sans radiateur ≥ Tj_max − 20°C → radiateur nécessaire

Avec radiateur :
  Tj = Tamb + Pdiss × (Rθjc + Rθcs + Rθsa)
  
  Rθjc = résistance jonction-boîtier (extrait du datasheet, ex: 5°C/W pour TO-220)
  Rθcs = résistance boîtier-radiateur (avec graisse thermique ≈ 0,5°C/W)
  Rθsa = résistance radiateur-air (extrait du datasheet radiateur)
  
Exemple : Même LM7805, Pdiss=3W, Tamb=40°C
  Sans radiateur : Tj = 40 + 3 × 65 = 40 + 195 = 235°C → DESTRUCTION !
  
  Avec radiateur Rθsa = 15°C/W :
  Tj = 40 + 3 × (5 + 0,5 + 15) = 40 + 3 × 20,5 = 40 + 61,5 = 101,5°C ← OK !
```

---

**🖼️ ILLUSTRATION 2 — Modèle thermique d'un régulateur**
> *Légende* : Schéma thermique en circuit analogique. Gauche : source de chaleur Pdiss (W). Chaîne en série de droite à gauche : Rθjc (jonction vers boîtier) → Rθcs (boîtier vers radiateur, avec graisse) → Rθsa (radiateur vers air) → Tamb. Les températures T_jonction, T_boîtier, T_surface_radiateur, T_air sont annotées aux nœuds. Formule globale encadrée : Tj = Tamb + Pdiss × (Rθjc + Rθcs + Rθsa). Un thermomètre visuel montre la progression des températures.
>
> **Prompt illustration** : *"Thermal resistance model diagram for power regulator in French. Electrical circuit analogy with series resistances. Left to right: 'Pdiss (W)' as current source. Nodes labeled: 'Tj - Jonction', 'Tc - Boîtier', 'Ts - Radiateur', 'Tamb - Ambiant'. Between nodes: resistors labeled 'Rθjc (5°C/W)', 'Rθcs (0.5°C/W graisse)', 'Rθsa (15°C/W)'. Formula box: 'Tj = Tamb + Pdiss × (Rθjc + Rθcs + Rθsa)'. Temperature thermometer on right showing progression 25°C→40°C→60°C→100°C. French labels, thermal engineering diagram style"*

---

## 4️⃣ — Autonomie sur batterie

### Calcul d'autonomie

```
Autonomie brute :
  t (heures) = Capacité batterie (mAh) / Courant moyen système (mA)

Autonomie réelle (facteur de dégradation) :
  t_réelle = t_brute × 0,80   (80% de la capacité est utilisable en pratique)
  → Raisons : décharge non linéaire · vieillissement · température

Courant moyen si le système a plusieurs modes :
  I_moy = (I_mode1 × t1 + I_mode2 × t2 + ...) / (t1 + t2 + ...)
```

### Exemple : ESP32 en mode intermittent

```
Cycle : 5s de mesure WiFi + 55s de deep sleep, répété indéfiniment

Mode actif WiFi (5s) : I = 150 mA
Mode deep sleep (55s): I = 0,1 mA

I_moy = (150 × 5 + 0,1 × 55) / (5 + 55)
      = (750 + 5,5) / 60
      = 755,5 / 60
      = 12,6 mA

Batterie Li-ion 18650 (3000 mAh) :
  t = 3000 / 12,6 = 238 heures = 9,9 jours
  t_réelle ≈ 238 × 0,80 = 190 heures ≈ 8 jours
```

---

## 5️⃣ — Schéma d'alimentation type pour un projet ESP32

```
Source (batterie LiPo ou 5V USB)
   │
   ├── [Condensateur d'entrée 10µF (céramique)] ← filtre les transitoires d'entrée
   │
   ├── [Régulateur 3,3V (LDO AMS1117 ou buck MP2315)]
   │       │
   │       ├── [Condensateur sortie 10µF] ← stabilité du régulateur
   │       └── [Condensateur sortie 100nF] ← filtrage HF
   │
   └── [Alimentation 3,3V vers ESP32, capteurs...]

Protection optionnelle :
   [Diode Schottky SS14] en série en entrée → protection anti-inversion polarité
   [Fusible réarmable (PTC)] en série → protection surintensité
```

---

## 📌 Les essentiels à retenir

> ✅ **Bilan de puissance** = tableau Composant / Vcc / I_pic / I_moy / P_moy — AVANT de choisir l'alimentation
> ✅ **Régulateur linéaire** : Pdiss = **(Vin − Vout) × Iout** — simple mais peu efficace
> ✅ **Régulateur à découpage** : η = 80-95% — obligatoire sur batterie si Vin-Vout ≥ 2V et Iout ≥ 200mA
> ✅ **Calcul thermique** : **Tj = Tamb + Pdiss × Rθja** (sans radiateur)
> ✅ **Radiateur nécessaire** si Tj calculé > Tj_max − 20°C (≥ 105°C en général)
> ✅ **Avec radiateur** : Tj = Tamb + Pdiss × (Rθjc + Rθcs + Rθsa)
> ✅ **Autonomie** = Capacité (mAh) / I_moy (mA) × 0,80 (facteur pratique)
> ✅ **Deep sleep** ESP32 = 10-150 µA → multiplier l'autonomie par ×10 à ×100 !
> ✅ **LDO** = linéaire à faible chute · bon pour Li-ion · bon si signal analogique sensible à côté
> ✅ **Buck** = découpage abaisseur · excellent rendement · génère du bruit HF

---

*Fiche de Cours Alimentation — BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S3*
*Compétences : S2.1 · S2.2 · S2.3 · C2.1*
