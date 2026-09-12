# 🔧 FICHE TP - S2 E31
## Sertissage Câble RJ45 - Norme T568B

**Nom : ________________  Prénom : ________________  Binôme : ________________**

---

## 🎯 OBJECTIF TP

**Fabriquer et tester 3 câbles Ethernet RJ45 fonctionnels**

- **Norme** : T568B
- **Longueurs** : 0,5m / 1m / 2m
- **Critère réussite** : 8 LEDs testeur allumées

---

## 🧰 MATÉRIEL PAR BINÔME

- ☐ Câble UTP Cat5e (20m)
- ☐ Connecteurs RJ45 (× 30)
- ☐ Pince à sertir (× 1)
- ☐ Testeur de câble (× 1)
- ☐ Cutter (× 1)
- ☐ Peigne à câble (× 1, optionnel)
- ☐ Règle ou mètre
- ☐ Schéma T568B (affiché)

---

## ⚠️ CONSIGNES SÉCURITÉ

**AVANT de manipuler :**

- ✅ Cutter : Couper en **s'éloignant** du corps
- ✅ Pince : Ne pas pincer les doigts
- ✅ Fils : Attention bords coupants
- ✅ Déchets : Poubelle dédiée

**En cas de coupure :** Appeler le formateur

---

## 📋 PROCÉDURE DÉTAILLÉE

### **CÂBLE 1 : 1 mètre (guidé)**

---

#### **□ ÉTAPE 1 : Mesurer et couper**

**Action :** Dérouler 1,10m de câble (marge), couper net.

**Outil :** Cisaille pince ou cutter

**Vérification :** Longueur = 1m (± 5 cm)

---

#### **□ ÉTAPE 2 : Dénuder la gaine**

**Longueur à dénuder :** **3-4 cm**

**Procédure :**
1. Marquer au feutre la zone (3 cm depuis bout)
2. Inciser légèrement la gaine avec cutter (tourner)
3. Tirer la gaine coupée

**⚠️ Attention :** Ne PAS couper les fils internes !

**Résultat :**

```
Câble ═══════════╗
                 ║ 3-4 cm de fils visibles
      Gaine ←───┘
```

**☑ Vérification :** 8 fils visibles, aucun coupé

---

#### **□ ÉTAPE 3 : Détorsader les paires**

**Action :** Défaire les 4 paires torsadées.

**Paires :**
- 🔵 Bleu (Bleu + Blanc-Bleu)
- 🟠 Orange (Orange + Blanc-Orange)
- 🟢 Vert (Vert + Blanc-Vert)
- 🟤 Brun (Brun + Blanc-Brun)

**☑ Vérification :** 8 fils séparés

---

#### **□ ÉTAPE 4 : Ordonner selon T568B**

**Ordre (de gauche à droite) :**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| **BO** | **O** | **BV** | **B** | **BB** | **V** | **BBr** | **Br** |

**BO** = Blanc-Orange  
**O** = Orange  
**BV** = Blanc-Vert  
**B** = Bleu  
**BB** = Blanc-Bleu  
**V** = Vert  
**BBr** = Blanc-Brun  
**Br** = Brun

**💡 Astuce :** Poser les fils sur la table dans l'ordre, vérifier avec schéma.

**☑ Vérification :** Comparer avec affiche T568B au mur

---

#### **□ ÉTAPE 5 : Aplatir et aligner**

**Action :** 
1. Placer les 8 fils côte à côte
2. Les aplatir entre pouce et index
3. Aligner les extrémités

**Résultat attendu :**

```
Vue de profil :
═══════════════  (Tous à la même hauteur)

Vue de dessus :
║ ║ ║ ║ ║ ║ ║ ║  (Côte à côte, sans espace)
```

**☑ Vérification :** Pas d'écart entre fils, tous alignés

---

#### **□ ÉTAPE 6 : Couper à 1 cm**

**Longueur fils libres :** **1 cm** après la gaine

**Outil :** Cisaille de la pince (coupe perpendiculaire)

**Procédure :**
1. Tenir fils fermement (ordre maintenu)
2. Positionner cisaille à 1 cm
3. Couper net (un seul coup)

**☑ Vérification :** 
- Tous les fils même longueur
- Coupe nette (pas d'effilochage)

---

#### **□ ÉTAPE 7 : Insérer dans RJ45**

**Orientation RJ45 :**
- **Languette vers le BAS**
- **Broches cuivre vers le HAUT**
- **Ouverture face à toi**

```
     Broches cuivre
         ↓
    ┌─────────┐
    │  RJ45   │
    │ ║║║║║║║║│ ← Emplacement fils
    └─────────┘
         ↑
     Languette
```

**Action :**
1. Maintenir l'ordre des fils
2. Insérer doucement dans RJ45
3. Pousser jusqu'à ce que :
   - Fils touchent le **fond**
   - Gaine entre **dans** le RJ45 (3-5 mm)

**☑ Vérification :** 
- Par **transparence**, voir fils au fond
- Gaine bien rentrée

---

#### **□ ÉTAPE 8 : Vérifier ordre couleurs**

**Regarder RJ45 par transparence :**

```
Vue face avant RJ45 :
┌─┬─┬─┬─┬─┬─┬─┬─┐
│BO│O│BV│B│BB│V│BBr│Br│
└─┴─┴─┴─┴─┴─┴─┴─┘
 1 2 3 4 5 6 7 8
```

**☑ Vérification :** 
- Ordre correct T568B ?
- Si NON → **Retirer RJ45 et recommencer**

---

#### **□ ÉTAPE 9 : Sertir**

**Procédure :**
1. Placer RJ45 dans **emplacement pince** (clic)
2. Tenir câble fermement
3. Appuyer **FORT** sur poignées pince (jusqu'au bout)
4. Relâcher

**⚠️ Important :** Serrer **fermement** (clic audible)

**Résultat :** Les broches cuivre ont **percé** l'isolant des fils.

**☑ Vérification :** RJ45 bien fixé, ne bouge pas si on tire

---

#### **□ ÉTAPE 10 : Répéter pour 2e extrémité**

**Refaire TOUTES les étapes** pour l'autre bout du câble.

**⚠️ IMPORTANT :** **MÊME norme T568B** des 2 côtés !

---

#### **□ ÉTAPE 11 : TEST**

**Matériel :** Testeur de câble

**Procédure :**
1. Brancher extrémité 1 dans **port "TX"**
2. Brancher extrémité 2 dans **port "RX"**
3. Allumer testeur
4. Observer LEDs

**Résultat attendu :**

```
✅ CÂBLE OK :
Testeur ● ● ● ● ● ● ● ●
        1 2 3 4 5 6 7 8
(8 LEDs vertes allumées en séquence)

❌ CÂBLE KO :
Testeur ● ○ ● ● ○ ● ● ●
        1 2 3 4 5 6 7 8
(LEDs manquantes = problème)
```

**☑ Si OK :** Câble validé ! ✅  
**☑ Si KO :** Voir diagnostic pannes ci-dessous ⬇️

---

## 🔍 DIAGNOSTIC PANNES

### **Problème : Aucune LED**

**Causes possibles :**
- Broches non enfoncées (sertissage faible)
- Fils coupés
- RJ45 défectueux

**Solution :**
1. Re-sertir plus fort
2. Tester avec autre testeur
3. Refaire le câble

---

### **Problème : 1-2 LEDs manquantes**

**Causes possibles :**
- Fil(s) inversé(s)
- Fil(s) coupé(s)
- Mauvais contact broche

**Solution :**
1. Vérifier ordre T568B par transparence
2. Si ordre OK → Re-sertir
3. Si ordre KO → **Refaire le câble**

---

### **Problème : LEDs dans le désordre**

**Cause :**
- Inversion de couleurs

**Solution :**
- Comparer avec schéma T568B
- **Refaire le câble**

---

### **Problème : LED 1 et 2 inversées avec 3 et 6**

**Cause :**
- T568A au lieu de T568B

**Solution :**
- **Refaire en T568B** (Blanc-Orange en 1er)

---

## 📊 SUIVI FABRICATION

### **CÂBLE 1 : 1m**

| **Critère** | **OK** | **KO** | **Remarques** |
|------------|--------|--------|---------------|
| Longueur correcte (1m) | ☐ | ☐ | |
| Ordre T568B respecté | ☐ | ☐ | |
| Test réussi (8 LEDs) | ☐ | ☐ | |
| Nombre d'essais | _____ | | |

**Validation formateur : ☐**

---

### **CÂBLE 2 : 0,5m**

| **Critère** | **OK** | **KO** | **Remarques** |
|------------|--------|--------|---------------|
| Longueur correcte (0,5m) | ☐ | ☐ | |
| Ordre T568B respecté | ☐ | ☐ | |
| Test réussi (8 LEDs) | ☐ | ☐ | |
| Nombre d'essais | _____ | | |

**Validation formateur : ☐**

---

### **CÂBLE 3 : 2m**

| **Critère** | **OK** | **KO** | **Remarques** |
|------------|--------|--------|---------------|
| Longueur correcte (2m) | ☐ | ☐ | |
| Ordre T568B respecté | ☐ | ☐ | |
| Test réussi (8 LEDs) | ☐ | ☐ | |
| Nombre d'essais | _____ | | |

**Validation formateur : ☐**

---

## 🏆 DÉFI (Optionnel - Si temps)

### **CÂBLE CROISÉ (T568A ↔ T568B)**

**Extrémité 1 :** T568A (Blanc-Vert en 1er)  
**Extrémité 2 :** T568B (Blanc-Orange en 1er)

**Usage :** Connecter 2 PC directement (sans switch)

**Test :** 8 LEDs mais **dans le désordre** (normal)

---

## 📝 NOTES PERSONNELLES

**Difficultés rencontrées :**

___________________________________________________________________

___________________________________________________________________

**Astuces découvertes :**

___________________________________________________________________

___________________________________________________________________

**Temps par câble :**
- Câble 1 : _____ min
- Câble 2 : _____ min
- Câble 3 : _____ min

---

## ✅ VALIDATION FINALE

**☐ 3 câbles testés OK (minimum 2)**  
**☐ Poste rangé (outils, déchets)**  
**☐ Grille d'évaluation complétée**

**Signature formateur : __________________**

---

**Document - BAC PRO CIEL - Version 1.0 - Février 2026**  
*TP Pratique S2 E31*
