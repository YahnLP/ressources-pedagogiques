# 📖 FICHE COURS - S12 E31
## GPO Sécurité - Stratégies de Groupes

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Créer GPO de sécurité
- ✅ Configurer politiques mots de passe
- ✅ Paramétrer verrouillage compte
- ✅ Comprendre héritage GPO

---

## 1️⃣ QU'EST-CE QU'UNE GPO ?

### **Définition**

> **GPO** (Group Policy Object) = Objet qui définit des **règles de configuration** appliquées automatiquement aux users et ordinateurs.

**Créé par :** Microsoft (Windows 2000)  
**Console :** GPMC (gpmc.msc)

### **Analogie**

> GPO = Règlement intérieur entreprise automatique

---

## 2️⃣ LIEN S11 → S12

| **S11** | **S12** |
|---------|---------|
| Créer OUs (structure) | Appliquer GPO (automatisation) |
| OU Commercial | GPO "Politique Commercial" |
| Users dans OU | Règles appliquées AUTO |

**Exemple :**

```
OU Commercial (S11)
   ↓ GPO liée (S12)
GPO "Mots de passe stricts"
   ↓ Appliquée à
TOUS users OU Commercial
```

---

## 3️⃣ TYPES DE GPO

| **Type** | **Cible** | **Exemples** |
|---------|----------|-------------|
| **Configuration ordinateur** | PC | Papier peint, verrouillage écran |
| **Configuration utilisateur** | User | Fond d'écran, restrictions |

**⚠️ S12 focus :** Configuration ordinateur (sécurité)

---

## 4️⃣ POLITIQUES MOTS DE PASSE

### **Recommandations ANSSI**

| **Paramètre** | **ANSSI** | **S12 appliqué** |
|--------------|----------|----------------|
| **Longueur min** | 12 caractères | ✅ 12 |
| **Complexité** | Oui (Maj+min+chiffre+symbole) | ✅ Oui |
| **Historique** | 5 anciens MDP | ✅ 5 |
| **Durée vie max** | 90 jours | ✅ 90 |
| **Durée vie min** | 1 jour | ✅ 1 |

### **Complexité = 3 sur 4**

- Majuscules (A-Z)
- Minuscules (a-z)
- Chiffres (0-9)
- Symboles (@#$%...)

**Exemple valide :** `Commercial@2026!`

---

## 5️⃣ VERROUILLAGE COMPTE

### **Protection brute-force**

| **Paramètre** | **Valeur S12** | **Pourquoi ?** |
|--------------|---------------|---------------|
| **Seuil verrouillage** | 3 essais | Bloquer après 3 échecs |
| **Durée verrouillage** | 30 minutes | Temporise attaques |
| **Réinitialisation compteur** | 30 minutes | Reset après inactivité |

**Scénario attaque :**
1. Pirate tente 3 mots de passe
2. Compte **verrouillé** 30 min
3. Attaque ralentie drastiquement

---

## 6️⃣ CRÉER GPO (Procédure)

### **Étape 1 : Ouvrir GPMC**

Console : `gpmc.msc`

### **Étape 2 : Créer GPO**

1. Clic droit "Group Policy Objects"
2. Nouveau
3. Nom : "Politique MDP Stricte"
4. OK

### **Étape 3 : Configurer**

1. Clic droit GPO → Modifier
2. Ordinateur → Stratégies → Paramètres Windows
3. Sécurité → Stratégies compte → **Stratégie mot de passe**

**Paramétrer :**
- Longueur min : 12
- Complexité : Activée
- Historique : 5

### **Étape 4 : Lier à OU**

1. Clic droit OU "Commercial"
2. Lier objet GPO existant
3. Sélectionner GPO
4. OK

### **Étape 5 : Forcer MAJ**

Sur PC client :
```cmd
gpupdate /force
```

---

## 7️⃣ HÉRITAGE GPO

### **Ordre application (LSDOU)**

```
1. Local (GPO locale PC)
2. Site
3. Domaine
4. OU (niveau 1, 2, 3...)
```

**Règle :** Dernière GPO l'emporte (OU > Domaine)

**Exemple :**

```
Domaine : MDP 8 caractères
   ↓
OU Direction : MDP 12 caractères
   ↓
User Direction : MDP = 12 (OU gagne)
```

---

## 8️⃣ COMMANDES UTILES

### **Forcer MAJ GPO (client)**

```cmd
gpupdate /force
```

### **Vérifier GPO appliquées**

```cmd
gpresult /r
```

**OU rapport HTML :**
```cmd
gpresult /h C:\rapport_gpo.html
```

---

## 9️⃣ DÉLÉGATION

### **Principe**

> Autoriser DRH à gérer OU RH (sans être admin domaine)

**Procédure :**

1. Console AD (dsa.msc)
2. Clic droit OU "RH"
3. Déléguer le contrôle
4. Ajouter user "drh"
5. Permissions : Créer users, modifier

**Avantage :** Admin décentralisé, sécurité renforcée

---

## 📚 VOCABULAIRE

| **Terme** | **Définition** |
|-----------|----------------|
| **GPO** | Group Policy Object |
| **GPMC** | Console gestion GPO |
| **LSDOU** | Ordre héritage (Local-Site-Domaine-OU) |
| **gpupdate** | Forcer MAJ GPO |
| **gpresult** | Vérifier GPO appliquées |
| **ANSSI** | Agence sécurité France |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je crée GPO sécurité
- [ ] Je lie GPO à OU
- [ ] Je force gpupdate
- [ ] Je comprends héritage LSDOU

---

## 📌 POINTS-CLÉS

1. **GPO** = Automatisation règles (S11 OUs)
2. **MDP** : 12 car, complexité, 90 jours
3. **Verrouillage** : 3 essais, 30 min
4. **Héritage** : OU > Domaine > Site > Local
5. **Délégation** : DRH gère OU RH

---

**Document - Version 1.0 - Février 2026**
