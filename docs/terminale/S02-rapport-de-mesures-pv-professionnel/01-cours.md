# 📖 FICHE COURS – S2 ANNÉE 3 – E2
## Rapport de Mesures : PV Professionnel, Traçabilité, Incertitudes, Norme IPC

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Rédiger un PV de mesure professionnel (structure, champs, signature)
- ✅ Expliquer la traçabilité métrologique et l'étalonnage
- ✅ Calculer une incertitude de mesure (type A, type B, combinée, élargie)
- ✅ Connaître les critères d'acceptabilité IPC-A-610 par classe
- ✅ Rédiger un rapport de conformité (conforme / non conforme)

---

## 1️⃣ DE LA MESURE AU PROCÈS-VERBAL

### La limite d'une mesure brute

> Vous lisez `22,4°C` sur votre sonde. Cette valeur seule ne prouve rien :
> - Est-ce que l'instrument est fiable ?
> - Est-ce que vous l'avez lu correctement ?
> - Est-ce que ce chiffre tient compte de l'erreur de l'instrument ?
> - Qui peut confirmer que cette mesure a bien été réalisée ?

> Un **Procès-Verbal (PV) de mesure** transforme une lecture en preuve documentée, opposable, traçable.

### La valeur légale d'un PV

| **Mesure brute** | **PV de mesure professionnel** |
|---|---|
| Valeur lue à l'écran | Valeur + incertitude + unité |
| Instrument inconnu | Instrument identifié (marque, modèle, N° de série) |
| Conditions non précisées | Conditions (T°, hygrométrie, date, lieu) |
| Aucune traçabilité | Certificat d'étalonnage référencé |
| Non signé | Signé par le mesureur et le responsable qualité |
| Non daté | Daté et numéroté |

---

## 2️⃣ STRUCTURE D'UN PV DE MESURE PROFESSIONNEL

### Les 10 sections d'un PV complet

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PROCÈS-VERBAL DE MESURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. EN-TÊTE ET IDENTIFICATION
   Référence PV    : PV-2026-ESP32-001
   Date            : 2026-03-20
   Lieu            : Labo électronique – CFA [Ville]
   Donneur d'ordre : INDUSTECH SAS – M. DUBOIS

2. OBJET DE LA MESURE
   Vérification des résistances de pull-up I2C sur carte ESP32

3. ÉQUIPEMENT SOUS TEST (EUT)
   Désignation     : Carte ESP32 IoT AGROSMART
   Référence       : ASM-001-REV2
   N° de série     : SN20260320-03

4. INSTRUMENTS UTILISÉS
   ┌───────────────────────────────────────────────────────┐
   │  Appareil    : Multimètre numérique Fluke 87V        │
   │  N° de série : 7435280                               │
   │  Calibration : 2026-01-15 – Cert. N° LAB-2026-0047  │
   │  Classe      : 0,5                                   │
   │  Validité    : 2027-01-14                            │
   └───────────────────────────────────────────────────────┘

5. CONDITIONS DE MESURE
   Température ambiante : 22°C ± 2°C
   Hygrométrie          : 45% HR ± 10%
   Réseau électrique    : Mesure hors tension (Ω)

6. RÉSULTATS DE MESURE
   (voir tableau section suivante)

7. INCERTITUDES
   (voir calcul section suivante)

8. CONCLUSION / CONFORMITÉ
   ☐ Conforme    ☐ Non conforme    ☐ Sous réserve

9. REMARQUES ET OBSERVATIONS

10. SIGNATURES
    Mesureur : ________________    Responsable qualité : ________________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3️⃣ TRAÇABILITÉ MÉTROLOGIQUE

### La chaîne de raccordement

> La **traçabilité métrologique** garantit qu'une mesure peut être reliée, par une chaîne ininterrompue de comparaisons, aux étalons nationaux et internationaux.

```
BIPM (Bureau International des Poids et Mesures — Sèvres)
  ↓ Définition SI (le métre, l'ampère, le kelvin...)
LNE (Laboratoire National de Métrologie et d'Essais — France)
  ↓ Étalons primaires nationaux
Laboratoire accrédité COFRAC
  ↓ Certificat d'étalonnage ISO/CEI 17025
Votre multimètre étalonné
  ↓ Mesure avec incertitude connue
VOTRE PV DE MESURE
```

> **Sans cette chaîne**, votre mesure ne peut pas être opposée à une norme, un contrat ou un tribunal.

### L'étalonnage d'un instrument

> **Étalonner** un instrument = le comparer à un étalon de référence de niveau supérieur et déterminer son erreur systématique.

> **Certificat d'étalonnage** : document émis par un laboratoire accrédité attestant que l'instrument a été comparé à des étalons raccordés, à une date précise, dans des conditions définies, avec les incertitudes mesurées.

```
Ce que contient un certificat d'étalonnage :
  ✅ Identification de l'instrument (modèle, N° de série)
  ✅ Date d'étalonnage
  ✅ Organisme étalonnant (COFRAC ou équivalent)
  ✅ Résultats : erreur constatée par gamme de mesure
  ✅ Incertitude de mesure de l'étalonnage
  ✅ Validité (durée avant prochain étalonnage)
```

> ⚠️ Un instrument non étalonné ou avec un étalonnage périmé ne peut pas servir à produire un PV opposable.

---

📷 **[ILLUSTRATION 1]**
*Diagramme pyramidal de la chaîne de raccordement métrologique. Sommet : BIPM (icône globe, "Définitions SI"). Niveau 2 : LNE France (icône bâtiment officiel, "Étalons primaires nationaux"). Niveau 3 : Laboratoire accrédité COFRAC (icône microscope, "Certificats ISO/CEI 17025"). Niveau 4 : Instrument étalonné (icône multimètre, "Erreur et incertitude connues"). Base : Mesure sur le terrain (icône technicien, "PV de mesure traçable"). Flèches descendantes annotées "Raccordement par comparaison". Style diagramme métrologique industriel, fond blanc, couleurs hiérarchiques du bleu foncé au vert clair.*

> **Légende :** La chaîne de traçabilité métrologique. Chaque niveau est raccordé au niveau supérieur par une comparaison documentée avec incertitude connue. Un PV de mesure réalisé avec un instrument Fluke étalonné COFRAC en 2026 est raccordé au BIPM via cette chaîne — c'est la garantie de sa valeur légale.

---

## 4️⃣ INCERTITUDES DE MESURE

### Pourquoi aucune mesure n'est parfaite

> Toute mesure est affectée d'une incertitude — un doute sur la valeur "vraie". Cette incertitude a deux origines :
> - Les **variations aléatoires** (bruit, instabilité) → Incertitude de **type A**
> - Les **limites connues de l'instrument** (résolution, classe, étalonnage) → Incertitude de **type B**

---

### Incertitude de type A — Statistique

> Calculée par répétition de la mesure. Pour n mesures de même grandeur :

$$u_A = \frac{s}{\sqrt{n}} \quad \text{où} \quad s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

**Exemple (n=5 mesures de résistance) :**

```
Mesures : 4 701 Ω / 4 698 Ω / 4 705 Ω / 4 702 Ω / 4 699 Ω
Moyenne x̄ = 4 701 Ω
Écart-type s = 2,7 Ω
u_A = 2,7 / √5 = 1,2 Ω
```

---

### Incertitude de type B — Instruments

**Source 1 : résolution de l'affichage numérique**

> L'affichage numérique ne peut donner que des valeurs discrètes. L'erreur maximale est ±½ du dernier chiffre.

$$u_{B,rés} = \frac{\text{résolution}}{2\sqrt{3}}$$

**Exemple :** Multimètre affiche `4 703 Ω`, résolution = 1 Ω
$$u_{B,rés} = \frac{1}{2\sqrt{3}} = \frac{1}{3,46} \approx 0,29 \text{ Ω}$$

**Source 2 : classe de l'instrument**

> La classe est l'erreur maximale exprimée en % de la valeur mesurée.

$$u_{B,classe} = \frac{\text{classe\%} \times \text{valeur lue}}{100 \times \sqrt{3}}$$

**Exemple :** Fluke 87V, classe 0,5%, mesure 4 703 Ω
$$u_{B,classe} = \frac{0,5 \times 4703}{100 \times 1,73} = \frac{23,5}{173} \approx 13,6 \text{ Ω}$$

---

### Incertitude combinée et élargie

$$\boxed{u_c = \sqrt{u_A^2 + u_{B,rés}^2 + u_{B,classe}^2}}$$

$$\boxed{U = k \cdot u_c \quad \text{avec } k=2 \text{ pour 95\% de confiance}}$$

**Exemple complet :**

```
u_A         = 1,2 Ω
u_B,rés     = 0,3 Ω
u_B,classe  = 13,6 Ω

u_c = √(1,2² + 0,3² + 13,6²) = √(1,44 + 0,09 + 184,96) = √186,49 = 13,7 Ω

U = 2 × 13,7 = 27,4 Ω  → arrondi à 30 Ω (règle : 1 chiffre significatif sur U)

Résultat : R = (4 703 ± 30) Ω  [niveau de confiance 95%]
```

> **Règle d'arrondi :** L'incertitude élargie s'arrondit **par excès à 1 chiffre significatif** (sauf si commence par 1 ou 2 → 2 chiffres). La valeur mesurée s'arrondit ensuite au même rang décimal que U.

---

📷 **[ILLUSTRATION 2]**
*Diagramme en bâtons montrant la composition de l'incertitude. Sur l'axe X : les 3 sources (u_A statistique en bleu flair, u_B résolution en orange clair, u_B classe en rouge). Sur l'axe Y : les valeurs en Ω. Une 4ème barre montre u_c combinée (plus grande). Une 5ème barre montre U élargie (le double). Annotation centrale : "La classe de l'instrument domine souvent l'incertitude totale". Style graphique bâtons pédagogique, fond blanc, axes annotés.*

> **Légende :** Composition de l'incertitude de mesure. Dans cet exemple, la classe de l'instrument (13,6 Ω) domine largement l'incertitude combinée. L'incertitude statistique (u_A = 1,2 Ω) et la résolution (u_B = 0,3 Ω) sont négligeables face à l'incertitude intrinsèque de l'instrument. Cela montre qu'améliorer le nombre de mesures (réduire u_A) ne sert à rien si l'instrument est de mauvaise classe.

---

## 5️⃣ NORME IPC-A-610 — ACCEPTABILITÉ DES ASSEMBLAGES

### Qu'est-ce que la norme IPC-A-610 ?

> La norme **IPC-A-610** (Acceptability of Electronic Assemblies) est le standard international le plus utilisé dans l'industrie électronique pour définir les critères d'acceptabilité des brasures, du placement des composants et des défauts d'assemblage.

### Les 3 classes IPC

| **Classe** | **Usage** | **Exemples** |
|---|---|---|
| **Classe 1** | Produits grand public, tolérance haute aux défauts | Jouets électroniques, appareils ménagers bas de gamme |
| **Classe 2** | Produits industriels et commerciaux | Équipement IoT industriel, automates, systèmes embarqués |
| **Classe 3** | Applications critiques, défaillance inacceptable | Médical, aérospatial, militaire, nucléaire |

> **En BAC PRO CIEL** : votre projet IoT industriel est typiquement **Classe 2**.

---

### Critères d'acceptabilité des brasures (CMS)

| **Critère** | **Conforme** (Target) | **Acceptable** | **Non conforme** |
|---|---|---|---|
| **Mouillage** | Soudure lisse, brillante, bonne extension | Légèrement terne, mouillage partiel | Perle de soudure, non-mouillage |
| **Angle de contact** | < 90° | 90°–120° | > 120° (beurk) |
| **Hauteur de brasure** | 25–75% de la hauteur du composant | ≥ 25% | < 25% |
| **Excès de soudure (bridging)** | Absent | Absent (Cl.1: acceptable) | Non conforme Cl.2/3 |
| **Composant déplacé CMS** | < 25% de la largeur | 25–50% | > 50% |

### Critères pour les trous traversants (PTH)

| **Critère** | **Cl.1** | **Cl.2** | **Cl.3** |
|---|---|---|---|
| Remplissage du trou | ≥ 50% | ≥ 75% | ≥ 75% |
| Void dans la brasure | ≤ 25% | ≤ 10% | ≤ 10% |
| Pointe de soudure (icicle) | Acceptable | Non conforme | Non conforme |

---

## 6️⃣ RAPPORT DE CONFORMITÉ

### Les 3 conclusions possibles

| **Conclusion** | **Définition** | **Formulation** |
|---|---|---|
| **Conforme** | Toutes les exigences sont satisfaites | "L'assemblage est déclaré conforme à la norme IPC-A-610 Classe 2" |
| **Non conforme** | Au moins une exigence n'est pas satisfaite | "L'assemblage présente X défauts non conformes — rejeté" |
| **Sous réserve** | Conforme avec une observation ou une restriction | "Conforme sous réserve de correction du pont de soudure en C3-C4" |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais nommer les 10 sections d'un PV de mesure professionnel
- [ ] Je comprends la chaîne de traçabilité (BIPM → LNE → COFRAC → instrument)
- [ ] Je sais calculer u_A (statistique), u_B résolution et u_B classe
- [ ] Je sais calculer u_c (combinée) et U (élargie avec k=2)
- [ ] Je sais exprimer un résultat : valeur ± U unité [confiance 95%]
- [ ] Je connais les 3 classes IPC et leurs applications
- [ ] Je distingue "conforme", "acceptable" et "non conforme" IPC
- [ ] Je sais rédiger une conclusion de conformité en 1 phrase

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **PV de mesure** | Procès-Verbal — document officiel attestant d'une mesure avec traçabilité |
| **Traçabilité** | Propriété d'une mesure reliée aux étalons nationaux/internationaux |
| **Étalonnage** | Comparaison d'un instrument à un étalon de référence plus précis |
| **COFRAC** | Comité Français d'Accréditation — organisme qui accrédite les laboratoires d'étalonnage |
| **LNE** | Laboratoire National de Métrologie et d'Essais — référence nationale française |
| **BIPM** | Bureau International des Poids et Mesures — référence internationale des unités SI |
| **Incertitude type A** | Incertitude évaluée statistiquement par répétition des mesures |
| **Incertitude type B** | Incertitude évaluée à partir de données instruments (résolution, classe) |
| **Incertitude combinée** | $u_c = \sqrt{u_A^2 + u_B^2}$ |
| **Incertitude élargie** | $U = k \cdot u_c$ avec k=2 (~95% confiance) |
| **Classe d'instrument** | Erreur maximale en % de la pleine échelle ou de la valeur lue |
| **Résolution** | Plus petit écart affichable par l'instrument (ex: 0,1°C, 1 Ω) |
| **IPC-A-610** | Norme internationale d'acceptabilité des assemblages électroniques |
| **Classe 2 IPC** | Niveau industriel standard — critères de qualité élevés |
| **Brasure conforme** | Brasure satisfaisant tous les critères IPC (mouillage, angle, hauteur) |

---

## 📌 POINTS-CLÉS À RETENIR

1. Un PV sans date, sans instrument identifié et sans signature est **sans valeur légale**
2. La traçabilité = chaîne **BIPM → LNE → COFRAC → instrument étalonné → PV**
3. `u_A = s/√n` (répétitions) ; `u_B = résolution/(2√3)` ; `u_B = (classe%×valeur)/(100√3)`
4. `U = 2 × u_c` → confiance 95% — **k=2 est la valeur standard**
5. Expression : `R = (4 703 ± 30) Ω [95%]` — **toujours arrondir U par excès à 1 chiffre sig.**
6. IPC Classe 2 = standard IoT industriel — pont de soudure = **non conforme**
7. Rapport de conformité : **conforme / non conforme / sous réserve** — jamais juste "OK" ou "KO"

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Version 1.0 – 2026**
