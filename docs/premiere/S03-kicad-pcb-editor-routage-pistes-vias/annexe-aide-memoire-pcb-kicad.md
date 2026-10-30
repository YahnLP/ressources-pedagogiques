# 🗂️ AIDE-MÉMOIRE PCB KICAD — À PLASTIFIER
## Routage · Clearance · DRC · Vue 3D · BAC PRO CIEL · E2 · 2ᵉ année S3

---

> *Conserver à côté du clavier pendant les TP KiCad*

---

## 🔄 Flux de conception

```
Schéma (ERC=0) → Empreintes → Update PCB
→ Contour Edge.Cuts → Placement → Routage → DRC → 3D
```

---

## 🎛️ Raccourcis PCB Editor

```
X    → Tracer une piste
V    → Insérer un via (changer de calque)
R    → Rotation composant
G    → Grab (déplacer avec les fils)
F    → Flip (face avant ↔ arrière)
E    → Éditer propriétés
DEL  → Supprimer
Alt+3 → Vue 3D
+/-  → Calque suivant/précédent
Ctrl+S → Sauvegarder
B    → Remplir les zones (Fill All Zones)
```

---

## 📏 Largeurs de pistes recommandées

```
Signal     : 0,30-0,50 mm    < 0,5 A
Alim 5V    : 0,80 mm          < 2 A
Alim 12V   : 1,50 mm          < 4 A
GND        : Plan de masse (B.Cu)
Clearance  : 0,20 mm minimum
```

---

## 🔩 Via standard

```
Diamètre extérieur : 0,80 mm
Perçage            : 0,40 mm
Anneau cuivre      : 0,20 mm
```

---

## 📚 Calques essentiels

```
F.Cu        → Cuivre face avant (rouge)
B.Cu        → Cuivre face arrière (bleu)
Edge.Cuts   → Contour PCB (jaune)
F.Silkscreen → Sérigraphie (blanc)
F.Mask      → Masque soudure (rose)
F.Courtyard → Zone réservée (magenta)
```

---

## 🔴 Erreurs DRC fréquentes

```
"Clearance violation"   → Pistes trop proches → redéfinir
"Unconnected items"     → Ratsnest restant → router
"Dangling end"          → Piste qui part dans le vide → prolonger
"Courtyard overlap"     → Composants qui se chevauchent → écarter
"Net has no driver"     → PWR_FLAG manquant dans le schéma
```

---

## ✅ Checklist avant fabrication

```
☐ Contour Edge.Cuts fermé et propre
☐ Tous les ratsnest routés (0 ratsnest visible)
☐ Pistes alimentation plus larges que signal
☐ DRC → 0 erreur, 0 avertissement
☐ Vue 3D vérifiée (pas de chevauchement)
☐ copy run start... non, c'est pour E31 !
☐ Fichier .kicad_pcb sauvegardé
```

---

## 🖥️ Vue 3D — navigation

```
Alt+3         → Ouvrir
Clic gauche   → Rotation
Clic droit    → Translation
Molette       → Zoom
Numpad 7      → Vue dessus
Numpad 1      → Vue face
Numpad 9      → Vue dessous
```

---

*Aide-Mémoire PCB KiCad — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S3*
*Compétences S3.3 · C4.1 · C4.2*
