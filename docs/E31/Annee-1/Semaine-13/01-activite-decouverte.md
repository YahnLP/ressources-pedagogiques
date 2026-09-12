# 🎲 ACTIVITÉ - S13 E31
## "L'Immeuble Cloisonné" : Comprendre les VLANs

---

## 🎯 OBJECTIFS

- ✅ Visualiser isolation VLANs
- ✅ Comprendre broadcast confinés
- ✅ Tester communication inter/intra VLAN

---

## ⏱️ DURÉE : 40 min

---

## 🧩 MATÉRIEL

- Badges 3 couleurs (16)
- Schéma immeuble 3 étages
- Tableau "Switch virtuel"

---

## 📋 CONTEXTE

**Immeuble TECHCORP (3 étages isolés)**

**Étages = VLANs :**
- 🔴 Étage 1 = VLAN 10 (Direction)
- 🔵 Étage 2 = VLAN 20 (Administration)
- 🟢 Étage 3 = VLAN 30 (IT)

**Switch = Immeuble physique**

---

## 🎮 DÉROULEMENT

### **PHASE 1 : Distribution étages (5 min)**

**Formateur distribue badges :**
- 5 apprentis → Badge 🔴 (VLAN 10 Direction)
- 5 apprentis → Badge 🔵 (VLAN 20 Admin)
- 5 apprentis → Badge 🟢 (VLAN 30 IT)

**Disposition spatiale :**

```
[Direction 🔴]     [Admin 🔵]     [IT 🟢]
   (5 pers)         (5 pers)      (5 pers)
    Zone 1           Zone 2        Zone 3
```

---

### **PHASE 2 : Test isolation (15 min)**

**Situation 1 : Communication intra-VLAN**

🔴 **Alice (Direction) veut parler à Bob (Direction)**
- Même VLAN 10
- ✅ **Communication OK**

**Observation :** "Dans même étage = on se parle"

---

**Situation 2 : Communication inter-VLAN**

🔴 **Alice (Direction) veut parler à Charlie (IT)**
- VLANs différents (10 vs 30)
- ❌ **Communication BLOQUÉE**

**Formateur annonce :** "Pas de communication entre étages !"

**Observation :** "Étages isolés = sécurité"

---

**Situation 3 : Broadcast**

🔴 **Alice (Direction) crie : "Réunion !"**
- Broadcast dans VLAN 10
- 🔴 Bob, David (Direction) → ✅ Entendent
- 🔵 🟢 Admin, IT → ❌ N'entendent PAS

**Message :**
> "Broadcast confiné au VLAN = Pas de pollution réseau"

---

### **PHASE 3 : Trunk = Ascenseur (10 min)**

**Problème :** Comment relier 2 immeubles (2 switches) ?

**Solution :** **Port TRUNK** (ascenseur inter-immeubles)

**Démonstration :**

**Formateur = Câble trunk entre 2 switches**

**Tag 802.1Q = Badge étage :**
- 🔴 Personne Direction traverse trunk → Tag VLAN 10
- 🔵 Personne Admin traverse trunk → Tag VLAN 20

**Résultat :**
- Direction Immeuble A ↔ Direction Immeuble B ✅
- Direction Immeuble A ↔ Admin Immeuble B ❌

---

### **PHASE 4 : Segmentation entreprise (10 min)**

**Cas réel : Entreprise sécurisée**

**3 zones :**

**🔴 VLAN 10 : DMZ (Demilitarized Zone)**
- Serveurs publics (web)
- Accès Internet

**🔵 VLAN 20 : Production**
- PC employés
- Applications métier

**🟢 VLAN 30 : Administration**
- Serveurs critiques
- Comptes admin

**Sécurité :**
- DMZ isolée (si piratée, production protégée)
- Admin isolée (accès restreint)

---

## 📊 DÉBRIEFING

**Lien jeu ↔ VLANs :**

| **Jeu** | **VLAN réel** |
|---------|--------------|
| Immeuble | Switch physique |
| Étages | VLANs logiques |
| Badges couleurs | Tags 802.1Q |
| Ascenseur | Port trunk |
| Isolation étages | Isolation VLANs |

**Avantages VLANs :**

1. ✅ **Sécurité** : Isolation services
2. ✅ **Performance** : Broadcast confinés
3. ✅ **Flexibilité** : 1 switch = N réseaux
4. ✅ **Économie** : Pas besoin N switches

---

## ✅ VALIDATION

- 100% participent
- 80% comprennent isolation
- 70% expliquent trunk vs access

---

**Document - Version 1.0 - Février 2026**
