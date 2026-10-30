# 🗂️ AIDE-MÉMOIRE COMPOSANTS + KICAD — À PLASTIFIER
## Symboles · Code Couleur · Calculs · KiCad · BAC PRO CIEL · E2 · 2ᵉ année S1

---

> *Référence pour les TP et évaluations E2*

---

## 🔌 Composants — Symboles et rôles

```
R  Résistance     → limite le courant · [Ω]
C  Condensateur   → stocke/filtre · [F] · polarisé (+/−) ou non
L  Inductance     → filtre/stocke énergie magnétique · [H]
D  Diode          → sens unique · A→K (anode → cathode)
LED               → diode lumineuse · Vf≈2V rouge/jaune, 3V bleu/blanc
DZ Zener          → régule une tension · VZ fixe
Q  Transistor     → NPN (B·C·E) · commutateur ou amplificateur
AO Ampli op       → 2 entrées (+/−) · 1 sortie · comparateur/ampli
NE555             → timer · monostable ou astable · 8 broches
7805              → régulateur +5V fixe · VIN · GND · VOUT
```

---

## 🎨 Code couleur résistances (4 bandes)

```
N O R O  J  V  B  V  G  B   Or    Argent
0 1 2 3  4  5  6  7  8  9  ±5%   ±10%
        ×1 ×10 ×100 ×1k ×10k ×100k ×1M

Mémo : Ne Mange Rien Ou Je Vais Vite Chez McDonald's
       Noir Marron Rouge Orange Jaune Vert Violet Gris Blanc

Exemple : Marron(1) Noir(0) Orange(×1000) Or(±5%) = 10 000 Ω = 10 kΩ ±5%
```

---

## ⚡ Calculs essentiels

```
Loi d'Ohm    : U = R × I
Puissance    : P = U × I = R × I²
Résistances  : Série → Req = R1+R2+R3
               Parallèle → 1/Req = 1/R1+1/R2 (Req < plus petite R)
Pont diviseur: Vm = VCC × R2/(R1+R2)
LED          : R = (VCC − Vf) / If  (Vf=2V rouge · If=20mA standard)
Condensateur : E = ½×C×V²  ·  Uc = Q/C
Période/Fréq : T = 1/f
```

---

## 🖥️ KiCad — Raccourcis essentiels

```
A    → Ajouter un symbole (composant)
P    → Ajouter alimentation (+5V, GND...)
W    → Tracer un fil
E    → Éditer les propriétés
R    → Rotation
G    → Déplacer avec les fils connectés
DEL  → Supprimer
Ctrl+Z → Annuler
Ctrl+S → Sauvegarder (SOUVENT !)
I/F9 → ERC (vérification erreurs)
Molette → Zoom
```

---

## 📋 Bibliothèques KiCad importantes

```
Device:R              Résistance
Device:C_Polarized    Condensateur polarisé
Device:LED            LED
Device:D_Zener        Diode Zener
Device:Q_NPN_BCE      Transistor NPN
power:+5V +12V +3V3   Alimentations
power:GND             Masse
power:PWR_FLAG        ← Obligatoire sur chaque net d'alim !
Timer:NE555           NE555
```

---

## ✅ Checklist schéma KiCad

```
☐ Tous les composants annotés (R? → R1 via Annotate)
☐ Valeurs saisies (150Ω, BC547...)
☐ PWR_FLAG sur chaque net d'alimentation
☐ Tous les fils bien connectés (pas de carré vert)
☐ ERC → 0 erreur
☐ Ctrl+S sauvegardé
```

---

## ⚠️ Erreurs classiques

```
LED inversée     → A(anode) en haut · K(cathode) en bas → GND
Fil déconnecté   → Zoom et recoller le fil sur la broche
PWR_FLAG oublié  → "Net has no driver" dans ERC
Masque R         → Masque (/24) ≠ wildcard OSPF (erreur E31, pas E2 !)
Transistor sens  → Émetteur (E) toujours vers GND pour NPN
```

---

*Aide-Mémoire Composants + KiCad — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S1*
*Compétences S3.1 · S3.2 · S3.3 · C4.1*
