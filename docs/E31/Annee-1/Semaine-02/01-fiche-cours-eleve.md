# 📖 FICHE DE COURS - S2 E31
## Câblage RJ45 - Normes T568A/B

**Nom : ________________  Prénom : ________________  Classe : BAC PRO CIEL Année 1**

---

## 🎯 OBJECTIFS

À la fin de S2, je serai capable de :
- ✅ **Sertir** un connecteur RJ45 sur un câble
- ✅ **Respecter** la norme T568B
- ✅ **Tester** mon câble avec un testeur
- ✅ **Identifier** et corriger un défaut

---

## 1️⃣ LE CÂBLE ETHERNET RJ45

### 📝 Définition

> Un **câble Ethernet** permet de connecter des équipements réseau (PC, switch, routeur...).  
> Le connecteur s'appelle **RJ45** (prise transparente 8 broches).

### 🔌 Structure d'un câble Ethernet

**Composants :**

```
┌─────────────────────────────────────┐
│  Gaine externe (PVC)                │
│  ┌─────────────────────────────┐   │
│  │ 4 paires torsadées (8 fils) │   │
│  │ - Paire 1: Bleu             │   │
│  │ - Paire 2: Orange           │   │
│  │ - Paire 3: Vert             │   │
│  │ - Paire 4: Brun             │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
         ↓
    Connecteur RJ45
    (8 broches cuivre)
```

**UTP** = **U**nshielded **T**wisted **P**air (paire torsadée non blindée)

---

## 2️⃣ NORMES T568A et T568B

### 📊 Les 2 normes de câblage

Il existe **2 normes** pour ordonner les 8 fils dans le connecteur RJ45 :

- **T568A** : Ancienne norme (moins utilisée)
- **T568B** : **Norme actuelle** (standard) ⭐

**⚠️ Important :** Il faut utiliser la **MÊME norme aux 2 extrémités** du câble (sauf câble croisé).

---

### 🟠 NORME T568B (À CONNAÎTRE)

**Ordre des 8 fils (de gauche à droite, connecteur face à soi, languette en haut) :**

| **Pin** | **Couleur** | **Paire** |
|---------|-------------|-----------|
| **1** | **Blanc-Orange** | Paire 2 |
| **2** | **Orange** | Paire 2 |
| **3** | **Blanc-Vert** | Paire 3 |
| **4** | **Bleu** | Paire 1 |
| **5** | **Blanc-Bleu** | Paire 1 |
| **6** | **Vert** | Paire 3 |
| **7** | **Blanc-Brun** | Paire 4 |
| **8** | **Brun** | Paire 4 |

**💡 Moyen mnémotechnique :**

> **T568B** → **B**lanc-**O**range en premier  
> **O**range, **V**ert, **B**leu, **Br**un

**Schéma visuel :**

```
RJ45 vu de face (languette en haut)
┌─┬─┬─┬─┬─┬─┬─┬─┐
│1│2│3│4│5│6│7│8│
└─┴─┴─┴─┴─┴─┴─┴─┘
 │ │ │ │ │ │ │ │
 BO O BV B BB V BBr Br

BO = Blanc-Orange
O  = Orange
BV = Blanc-Vert
B  = Bleu
BB = Blanc-Bleu
V  = Vert
BBr= Blanc-Brun
Br = Brun
```

---

### 🟢 NORME T568A (Pour info)

| **Pin** | **Couleur** |
|---------|-------------|
| 1 | Blanc-Vert |
| 2 | Vert |
| 3 | Blanc-Orange |
| 4 | Bleu |
| 5 | Blanc-Bleu |
| 6 | Orange |
| 7 | Blanc-Brun |
| 8 | Brun |

**Différence T568A ↔ T568B :**  
Inversion des **paires 2 (Orange) et 3 (Vert)**

---

## 3️⃣ CÂBLE DROIT vs CÂBLE CROISÉ

### 📊 Types de câbles

| **Type** | **Normes** | **Usage** | **Exemple** |
|---------|-----------|----------|-------------|
| **Câble droit** | T568B ↔ T568B | **PC ↔ Switch** <br> **Switch ↔ Routeur** | 99% des cas |
| **Câble croisé** | T568A ↔ T568B | **PC ↔ PC** <br> **Switch ↔ Switch** | Rare (obsolète) |

**💡 Aujourd'hui :** Les équipements modernes ont **Auto-MDI/X** → Détectent automatiquement le type de câble.  
→ **Câble croisé n'est plus nécessaire** !

**On utilise donc :** Câble droit (T568B des 2 côtés) partout.

---

## 4️⃣ CATÉGORIES DE CÂBLES

### 📊 Cat5e, Cat6, Cat7...

| **Catégorie** | **Vitesse max** | **Fréquence** | **Usage** |
|--------------|----------------|--------------|-----------|
| **Cat5e** | 1 Gbps | 100 MHz | Réseau domestique, bureau |
| **Cat6** | 1-10 Gbps | 250 MHz | Réseau entreprise |
| **Cat6a** | 10 Gbps | 500 MHz | Data center |
| **Cat7** | 10 Gbps | 600 MHz | Infrastructure critique (blindé) |

**💡 En BAC PRO :** On utilise du **Cat5e** (suffisant, économique)

---

## 5️⃣ PROCÉDURE SERTISSAGE (10 ÉTAPES)

### 🔧 Matériel nécessaire

- Câble UTP (Cat5e)
- Connecteur RJ45 (transparent)
- Pince à sertir
- Cutter ou dénudeur
- Testeur de câble
- **(Optionnel)** Peigne à câble

---

### 📋 ÉTAPES PAS À PAS

#### **ÉTAPE 1 : Couper le câble**

Longueur voulue : 0,5m / 1m / 2m...

**Outil :** Cutter ou cisaille de la pince

---

#### **ÉTAPE 2 : Dénuder la gaine externe**

**Longueur :** 3-4 cm depuis l'extrémité

**⚠️ Attention :** Ne pas couper les fils à l'intérieur !

**Astuce :** Tourner légèrement le cutter autour du câble, puis tirer la gaine.

```
Avant :  ═══════════════════
Après :  ═══════════╗
                    ║ 3-4 cm
         Fils visibles
```

---

#### **ÉTAPE 3 : Détorsader les paires**

Séparer les 4 paires torsadées.

**⚠️ Attention :** Ne pas trop détorsader (fragilise).

---

#### **ÉTAPE 4 : Ordonner les fils (T568B)**

Placer les 8 fils dans l'ordre T568B (de gauche à droite) :

**BO - O - BV - B - BB - V - BBr - Br**

**💡 Astuce :** Utiliser un **peigne à câble** pour maintenir l'ordre.

---

#### **ÉTAPE 5 : Aplatir et aligner**

Fils côte à côte, bien alignés (tous à la même hauteur).

```
Incorrect :  ╱ ╲ ╱ ╲ ╱ ╲  (fils désalignés)
Correct :    ║ ║ ║ ║ ║ ║  (fils alignés)
```

---

#### **ÉTAPE 6 : Couper net**

**Longueur fils libres :** **1 cm maximum** après la gaine

**Outil :** Cisaille de la pince (coupe perpendiculaire)

**Résultat :** Tous les fils à la même longueur, coupe nette.

---

#### **ÉTAPE 7 : Insérer dans RJ45**

**Sens :** Languette RJ45 **vers le bas**, fils **vers le haut**

**Action :** Pousser fermement jusqu'à ce que :
- Les fils touchent le **fond** du connecteur
- La gaine externe entre **dans** le RJ45

```
     ┌────────┐
     │RJ45    │
     │ ╔╔╔╔╔╔ │ ← Fils au fond
     │ ║ Gaine│ ← Gaine rentrée
     └────────┘
```

---

#### **ÉTAPE 8 : Vérifier par transparence**

Regarder le RJ45 par **transparence** :

- ✅ 8 fils visibles au fond
- ✅ Ordre couleurs correct (BO, O, BV...)
- ✅ Gaine bien rentrée

**Si NON → Retirer et recommencer**

---

#### **ÉTAPE 9 : Sertir**

**Action :** Placer RJ45 dans pince à sertir, **appuyer fermement**.

**Résultat :** Les **broches cuivre** percent l'isolant des fils et créent le contact.

**⚠️ Important :** Serrer **fort** (jusqu'au clic de la pince).

---

#### **ÉTAPE 10 : Tester**

**Outil :** Testeur de câble

**Procédure :**
1. Brancher les 2 extrémités du câble dans le testeur
2. Allumer
3. Observer les LEDs

**Résultat attendu :** **8 LEDs s'allument** dans l'ordre (1 → 8)

```
Testeur OK :  ● ● ● ● ● ● ● ●  (8 LEDs vertes)
              1 2 3 4 5 6 7 8

Testeur KO :  ● ○ ● ● ○ ● ● ●  (LEDs manquantes)
              → Fils 2 et 5 problème
```

---

## 6️⃣ DIAGNOSTIC PANNES

### 🔍 Test échoué : Que faire ?

| **Symptôme** | **Cause probable** | **Solution** |
|-------------|-------------------|-------------|
| **Aucune LED** | Pas de contact électrique | Re-sertir plus fort |
| **1-2 LEDs manquantes** | Fil coupé ou mal inséré | Refaire le câble |
| **LEDs dans le désordre** | Inversion couleurs | Vérifier ordre T568B, refaire |
| **LED 1 et 2 inversées** | T568A au lieu de T568B | Refaire en T568B |

**Réflexe :** Comparer l'ordre des fils avec le schéma T568B

---

## ✅ AUTO-ÉVALUATION

- [ ] Je connais l'ordre T568B par cœur
- [ ] J'ai réussi à sertir au moins 2 câbles
- [ ] Mes câbles passent le test (8 LEDs)
- [ ] Je sais identifier un défaut

---

## 📚 VOCABULAIRE

| **Terme** | **Définition** |
|-----------|----------------|
| **RJ45** | Connecteur 8 broches pour câble Ethernet |
| **UTP** | Unshielded Twisted Pair (non blindé) |
| **T568A/B** | Normes d'ordre des fils |
| **Sertir** | Fixer le connecteur sur le câble |
| **Paire torsadée** | 2 fils torsadés ensemble (réduit interférences) |
| **Cat5e/6/7** | Catégories de câbles (vitesse) |
| **Auto-MDI/X** | Détection automatique câble droit/croisé |

---

## 📌 POINTS-CLÉS

1. **T568B** = norme standard (Blanc-Orange en 1er)
2. **Câble droit** = T568B des 2 côtés (99% des cas)
3. **Sertissage** = Ordre fils crucial + sertir FORT
4. **Test** = 8 LEDs = câble OK

---

## 📸 PORTFOLIO

**À conserver :**
- Photo de ton câble RJ45 terminé
- Résultat du test (8 LEDs allumées)
- Cette fiche annotée

---

## 🏠 POUR ALLER PLUS LOIN

**Chez toi :**
- Observe les câbles RJ45 (box, PC, TV)
- Identifie la catégorie (marquée sur le câble)
- Essaie de fabriquer un câble (si matériel)

---

**Document - BAC PRO CIEL - Version 1.0 - Février 2026**  
*Séance S2 E31 - TP Pratique*
