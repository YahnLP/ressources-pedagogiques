# 🗂️ AIDE-MÉMOIRE PCB DOUBLE FACE · GERBER — À PLASTIFIER
## Métallisation · Sérigraphie · THT/SMD · Gerber · BAC PRO CIEL · E2 · 2ᵉ année S4

---

> *Conserver à côté du clavier pendant les TP KiCad*

---

## 🔄 Flux double face

```
Schéma (ERC=0) → Empreintes THT+SMD → Update PCB
→ Contour Edge.Cuts → Placement (F.Cu + flip B.Cu)
→ Routage F.Cu + B.Cu (vias avec V)
→ Plan GND B.Cu (B pour remplir)
→ DRC 0 erreur → Gerber ZIP → GerbView
```

---

## 📚 Calques et rôles

```
F.Cu  → Pistes cuivre avant (rouge)
B.Cu  → Pistes cuivre arrière + plan GND (bleu)
F.Mask → Vernis sauf sur les pads (rose) — ouvertures = soudure
F.Silkscreen → Textes/références (blanc) — NE PAS sur les pads !
Edge.Cuts → Contour découpe (jaune) — OBLIGATOIRE
Fichier .drl → Perçages (vias + THT)
```

---

## 🔩 SMD — Formats courants

```
0402 : 1,0 × 0,5 mm  → Très petit (usine)
0603 : 1,6 × 0,8 mm  → Petit
0805 : 2,0 × 1,25 mm → ★ RECOMMANDÉ (soudable à la main)
1206 : 3,2 × 1,6 mm  → Grand, composants puissants
SOT-23 : transistors, régulateurs simples
```

---

## ⚡ Via traversant standard

```
Diamètre extérieur : 0,80 mm
Perçage           : 0,40 mm
Anneau cuivre     : 0,20 mm ← ≥ 0,15 mm requis
Raccourci KiCad   : V (pendant le routage)
```

---

## 📏 Largeurs pistes double face

```
Signal     : 0,35 mm    < 0,5 A
Alim 5-9V  : 0,80 mm    < 2 A
GND        : Plan de masse B.Cu (Fill Zone)
Clearance  : 0,20 mm minimum
```

---

## 🟢 Plan de masse GND — procédure

```
1. Sélectionner B.Cu
2. Place → Add Rule Area
3. Dessiner rectangle sur tout le PCB
4. Net = GND · Fill = Solid · Clearance 0,3mm
5. Appuyer B → remplir
6. Ctrl+B → vider · B → remplir après modifications
```

---

## 📦 Export Gerber — checklist

```
File → Fabrication Outputs → Gerbers :
  ☐ F.Cu       ☐ B.Cu       ☐ Edge.Cuts
  ☐ F.Silkscreen ☐ F.Mask   ☐ B.Mask
  ☐ Protel extensions ✓

File → Fabrication Outputs → Drill Files :
  ☐ Excellon format ✓

→ Créer un ZIP de tous les fichiers gerber/
```

---

## 🔍 Vérification GerbView

```
F.Cu    → Toutes pistes face avant ?
B.Cu    → Plan GND + pistes arrière ?
Edge.Cuts → Contour fermé ?
F.Mask  → Zones noires = pads exposés (correct !)
Drill   → Tous les trous (vias + THT) ?
```

---

## ⚠️ Erreurs fréquentes

```
❌ Sérigraphie sur pad → DRC "Silkscreen clipped" → déplacer le texte
❌ Plan GND non rempli → pas de cuivre → appuyer B
❌ Edge.Cuts absent du ZIP → fabricant ne sait pas où couper
❌ Via 0,1mm perçage → impossible à fabriquer (min 0,3mm)
❌ C2 découplage loin du CI → bruit alimentation → < 3mm du CI
❌ Piste alim 0,35mm → trop fine → 0,8mm minimum
```

---

## 💰 Fabricants PCB (5 PCB 100×100mm)

```
JLCPCB  : ~2$ + port ~4$ (7-14 jours)
PCBWay  : ~5$ + port
Aisler  : ~15€ Europe (livraison rapide)
OSH Park: ~3$/inch² (violet, US)
```

---

*Aide-Mémoire PCB Double Face + Gerber — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S4*
*Compétences S3.3 · C4.1 · C4.2 · C4.3*
