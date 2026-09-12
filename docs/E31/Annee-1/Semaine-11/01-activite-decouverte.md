# 🎲 ACTIVITÉ - S11 E31
## "L'Organigramme Vivant" : Active Directory

---

## 🎯 OBJECTIFS

- ✅ Visualiser structure hiérarchique entreprise
- ✅ Comprendre concept **OUs**
- ✅ Expérimenter centralisation vs gestion dispersée

---

## ⏱️ DURÉE : 40 min

---

## 🧩 MATÉRIEL

- Badges 4 couleurs (16)
- Organigramme grand format
- Tableau "OUs"

---

## 📋 CONTEXTE

**Entreprise GLOBALTECH**

**4 services :**
- 🔴 Direction (2 personnes)
- 🔵 RH (4 personnes)
- 🟢 IT (5 personnes)
- 🟡 Commercial (5 personnes)

**+ Formateur = DC (Contrôleur de Domaine)**

---

## 🎮 DÉROULEMENT

### **PHASE 1 : CHAOS - Gestion dispersée (10 min)**

**Scénario :** Pas de centralisation

**Situation 1 : Nouvel employé**

🟢 **IT embauche Alice** :
- IT note "Alice" sur feuille locale
- RH ne sait pas
- Commercial ne sait pas
- **Problème** : Incohérence

**Situation 2 : Changement de service**

🟡 **Bob (Commercial) → RH** :
- Commercial supprime Bob
- RH ajoute Bob
- **Problème** : Bob perd accès dossiers
- IT ne sait pas → emails non transférés

**Observation :**
> "Sans centralisation = chaos, temps perdu"

---

### **PHASE 2 : Active Directory - Centralisation (15 min)**

**Nouvelle règle :** Toutes les infos dans le **DC** (formateur)

**Le DC a un tableau :**

```
┌──────────────────────────────────┐
│   BASE ACTIVE DIRECTORY          │
├──────────────────────────────────┤
│ OU: Direction                    │
│   - pdg@globaltech.local         │
│   - daf@globaltech.local         │
├──────────────────────────────────┤
│ OU: RH                           │
│   - drh@globaltech.local         │
│   - alice.rh@globaltech.local    │
├──────────────────────────────────┤
│ OU: IT                           │
│   - dsi@globaltech.local         │
│   - tech1@globaltech.local       │
├──────────────────────────────────┤
│ OU: Commercial                   │
│   - dircom@globaltech.local      │
│   - commercial1@globaltech.local │
└──────────────────────────────────┘
```

**Scénario 1 : Nouvel employé (avec AD)**

🟢 **IT embauche Charlie** :
- IT demande au **DC** : "Ajoute charlie@globaltech.local dans OU IT"
- DC note dans base centrale
- **Résultat** : Visible par TOUS instantanément

**Scénario 2 : Changement service (avec AD)**

🟡 **Bob Commercial → RH** :
- RH demande DC : "Déplace bob@globaltech.local vers OU RH"
- DC modifie
- **Résultat** : Bob garde historique

---

### **PHASE 3 : OUs = Structure logique (10 min)**

**OU** = Boîte qui regroupe utilisateurs d'un service

**Avantages OUs :**
1. **Organisation** : Users groupés logiquement
2. **Permissions** : Appliquer droits à toute l'OU
3. **GPO** (S12) : Configuration auto par OU
4. **Délégation** : DRH gère OU RH

---

## 📊 DÉBRIEFING (5 min)

**Lien jeu ↔ AD :**

| **Jeu** | **AD** |
|---------|--------|
| Formateur | **DC (Domain Controller)** |
| Tableau central | **Base AD** |
| Panneaux services | **OUs** |
| Badges employés | **Comptes users** |
| globaltech | **Nom domaine** |

**Workgroup vs Domaine :**

| **Critère** | **Workgroup (S10)** | **Domaine AD (S11)** |
|------------|--------------------|--------------------|
| Gestion | Locale (chaque PC) | Centralisée (DC) |
| Users | Créés sur chaque PC | Créés 1× dans AD |
| Échelle | <10 PC | 1 à 10 000+ PC |

---

## ✅ VALIDATION

- 100% participent
- 80% comprennent rôle DC
- 70% expliquent différence workgroup/domaine

---

**Document - Version 1.0 - Février 2026**
