# 🎲 ACTIVITÉ - S12 E31
## "Le Bouclier Automatique" : Puissance des GPO

---

## 🎯 OBJECTIFS

- ✅ Visualiser impact GPO (avant/après)
- ✅ Comprendre application automatique
- ✅ Tester politiques mots de passe

---

## ⏱️ DURÉE : 45 min

---

## 📋 CONTEXTE

**Entreprise GLOBALTECH (S11)**

**Problème :** Service Commercial créé en S11, MAIS :
- Users choisissent mots de passe faibles ("123456")
- Risque piratage élevé
- 50 users = 50 fois expliquer "mot de passe fort"

**Solution :** GPO appliquée à OU Commercial

---

## 🎮 DÉROULEMENT

### **PHASE 1 : AVANT GPO - Chaos (10 min)**

**Démonstration formateur :**

**Créer user test :**
1. Console AD (dsa.msc)
2. OU Commercial → Nouveau user
3. Nom : "test.commercial"
4. Mot de passe : `123456`
5. ✅ **ACCEPTÉ** (pas de politique)

**Problème visible :**
> "N'importe qui peut mettre mot de passe faible !"

---

### **PHASE 2 : CRÉER GPO Sécurité (20 min)**

**TP guidé (formateur + élèves) :**

**Étape 1 : Ouvrir GPMC**

Console : `gpmc.msc`

**Étape 2 : Créer GPO**

1. Clic droit "Group Policy Objects"
2. Nouveau
3. Nom : **"Politique MDP Stricte"**
4. OK

**Étape 3 : Configurer GPO**

1. Clic droit GPO → Modifier
2. Configuration ordinateur → Stratégies → Paramètres Windows
3. Paramètres de sécurité → Stratégies de compte → **Stratégie de mot de passe**

**Configurer :**

| **Paramètre** | **Valeur** |
|--------------|-----------|
| Longueur minimale | **12 caractères** |
| Complexité activée | **Oui** |
| Historique | 5 anciens MDP |
| Durée de vie max | 90 jours |

4. Fermer

**Étape 4 : Lier GPO à OU**

1. Clic droit OU **"Commercial"**
2. Lier objet GPO existant
3. Sélectionner "Politique MDP Stricte"
4. OK

**Étape 5 : Forcer MAJ (client)**

Sur PC client Commercial :
```cmd
gpupdate /force
```

---

### **PHASE 3 : APRÈS GPO - Protection (10 min)**

**Tester sur même user :**

**Tentative 1 : Mot de passe faible**

1. Console AD
2. OU Commercial → Nouveau user
3. Nom : "test2.commercial"
4. Mot de passe : `123456`
5. ❌ **REFUSÉ** !

**Message erreur :**
> "Le mot de passe ne respecte pas les exigences de complexité"

**Tentative 2 : Mot de passe fort**

Mot de passe : `Commercial@2026!`
- ✅ 16 caractères
- ✅ Majuscule + minuscule
- ✅ Chiffre + symbole
- ✅ **ACCEPTÉ**

---

### **PHASE 4 : Magie de l'automatisation (5 min)**

**Démonstration finale :**

**Ajouter 10 nouveaux users dans OU Commercial**

**Résultat :**
- TOUS soumis à politique stricte
- Pas besoin de reconfigurer
- **Automatique !**

**Message :**
> "1 GPO = Protection de 1 à 10 000 users !"

---

## 📊 DÉBRIEFING

**Lien S11 → S12 :**

| **S11** | **S12** |
|---------|---------|
| Créer OUs | Appliquer GPO aux OUs |
| Structure entreprise | Automatisation règles |
| OU Commercial (conteneur) | GPO "MDP Stricte" (politique) |

**Avantages GPO :**

1. ✅ **Automatique** : Nouveau user = règles appliquées
2. ✅ **Centralisé** : 1 modif GPO = tous users
3. ✅ **Sécurité** : Impossible contourner
4. ✅ **Économie temps** : 1× configurer vs 1000× expliquer

---

## ✅ VALIDATION

- 100% observent démo
- 80% comprennent automatisation
- 70% créent GPO sécurité

---

**Document - Version 1.0 - Février 2026**
