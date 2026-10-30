# 🗂️ AIDE-MÉMOIRE CEM — À PLASTIFIER
## Compatibilité EM · Blindage · Filtrage · Masse · BAC PRO CIEL · E2 · 2ᵉ année S13

---

> *Conserver pour les TP, exercices et l'évaluation*

---

## 🔑 Définition et triangle CEM

```
CEM = Ne pas perturber + Ne pas être perturbé
      (Directive européenne 2014/30/UE → Marquage CE)

SOURCE ──→ COUPLAGE ──→ VICTIME

Agir sur le COUPLAGE = solution la plus simple
```

---

## ⚡ Les 4 types de couplage

```
Résistif   → masse partagée → courant commun
Capacitif  → pistes proches → couplage par C parasite
Inductif   → boucle courant → champ B → courant induit
Rayonné    → onde EM dans l'air → perturbation à distance
```

---

## 📡 Conduit vs Rayonné

```
CONDUIT  (< 30 MHz) → se propage par les câbles
RAYONNÉ  (> 30 MHz) → se propage dans l'air

Solutions :
  Conduit  → filtre, condensateur découplage, ferrite
  Rayonné  → blindage, câble blindé, plan de masse
```

---

## 🛡️ Blindage

Efficace si :  
✓ Continu (pas de fente)  
✓ Relié à la masse (1 point)  
✓ Faible impédance  

Règle fente :  
Fente < λ/20 (sinon → antenne !)  

$$λ = \dfrac{c}{f} = 3 \times 10⁸ / f$$

Ex : f = 2,4 GHz → λ = 12,5 cm  
Fente max = 12,5/20 = 6,25 mm  

---

## 🔌 Condensateurs de découplage

```
100 nF céramique → 1 MHz à 100 MHz  ← HF (commutations)
10 µF tantale    → 1 kHz à 1 MHz   ← MF
100 µF élec.     → 10 Hz à 100 kHz ← BF

RÈGLE D'OR :
  Placer au plus près des pins VCC/GND (<1mm idéalement)
  Via GND court directement vers le plan de masse
```

---

## 🧲 Ferrites

```
Absorbent (≠ réfléchissent) l'énergie HF
Transparentes en BF, résistives en HF

Applications :
  Sur câble USB, câble alimentation
  Ferrite bead en série sur VCC d'un CI
  Clip-on sur câble d'entrée/sortie
```

---

## 🟩 Filtre RC passe-bas

```
Signal ──[R]──┬── Sortie filtrée
              [C]
              GND

fc = 1 / (2π × R × C)

Ex : R=10kΩ · C=330nF → fc = 48 Hz
```

---

## 🌐 Plan de masse

```
✓ Plan CONTINU sur B.Cu
  → Courant de retour direct sous la piste
  → Petite boucle → peu de rayonnement

✗ Plan FENDU
  → Courant détourné → grande boucle
  → Forte antenne → INTERDIT

Règles :
  Vias de masse fréquents (stitching)
  Masse analogique séparée de masse numérique
  → Relier à 1 seul point commun (topologie étoile)
```

---

## ⚠️ 5 violations CEM fréquentes sur un PCB

```
1. Condensateur découplage loin du CI
2. Plan de masse avec fente (piste traverse)
3. Longue piste pour signal rapide (> λ/20)
4. Masse analogique et numérique communes
5. Câble signal non blindé près d'un câble puissance
```

---

## 🏷️ Classes CEM

```
Classe A → Industriel (limites moins strictes)
Classe B → Résidentiel (limites plus strictes)
```

---

*Aide-Mémoire CEM — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S13*
*Compétences S7.1 · S7.2 · S7.3 · S7.4 · S7.5 · S7.6 · C7.1*
