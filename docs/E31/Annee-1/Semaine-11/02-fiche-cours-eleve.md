# 📖 FICHE COURS - S11 E31
## Active Directory - Domaine - OUs

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Comprendre Active Directory
- ✅ Installer contrôleur de domaine
- ✅ Créer OUs et utilisateurs AD
- ✅ Joindre PC au domaine

---

## 1️⃣ WORKGROUP vs DOMAINE

| **Critère** | **Workgroup** | **Domaine AD** |
|-------------|--------------|---------------|
| **Gestion** | Locale (chaque PC) | Centralisée (DC) |
| **Users** | Créés sur chaque PC | Créés 1× dans AD |
| **Échelle** | < 10 PC | 1 à 10 000+ PC |
| **Sécurité** | Faible | Forte (Kerberos) |
| **Usage** | Maison, TPE | Entreprise |

---

## 2️⃣ ACTIVE DIRECTORY

### **Définition**

> **Active Directory (AD)** = Annuaire centralisé qui stocke et gère informations sur utilisateurs, ordinateurs et ressources.

**Créé par :** Microsoft (1999)  
**Protocole :** LDAP (port 389)  
**Sécurité :** Kerberos (port 88)

### **Analogie**

> AD = Organigramme entreprise informatisé

---

## 3️⃣ CONCEPTS CLÉS

### **Domaine**

> Ensemble d'ordinateurs et users gérés par AD.

**Format :** `entreprise.local`  
**Exemple :** `globaltech.local`

**⚠️ Important :** `.local` pour test (pas `.com`)

---

### **DC (Domain Controller)**

> Serveur Windows qui héberge base AD.

**Rôle :**
- Stocke base AD (NTDS.DIT)
- Authentifie users
- Réplique avec autres DC

---

### **OU (Organizational Unit)**

> Conteneur logique pour organiser users/ordinateurs.

**Analogie :** Services entreprise

**Exemples :**
- OU Direction
- OU RH
- OU IT

**Avantages :**
- Organisation claire
- Permissions par OU
- GPO par OU (S12)

---

## 4️⃣ INSTALLER AD

### **Prérequis**

1. Windows Server 2019/2022
2. IP fixe (ex: 192.168.10.1)
3. DNS configuré (127.0.0.1)
4. Nom serveur (ex: SRV-DC01)

### **Procédure**

**Étape 1 : Ajouter rôle AD DS**

1. Gestionnaire de serveur
2. Gérer → Ajouter rôles
3. Cocher **Services AD DS**
4. Installer

**Étape 2 : Promouvoir en DC**

1. Clic 🔔 → Promouvoir ce serveur
2. Ajouter nouvelle forêt
3. Nom domaine : `globaltech.local`
4. Mot de passe DSRM
5. Installer

**Étape 3 : Redémarrage (5-10 min)**

---

## 5️⃣ GÉRER AD

### **Console**

**Ouvrir :** `dsa.msc`

### **Créer OU**

1. Clic droit domaine
2. Nouveau → Unité d'organisation
3. Nom : `IT`
4. OK

### **Créer utilisateur**

1. Clic droit OU → Nouveau → Utilisateur
2. Prénom : Alice
3. Nom : Martin
4. Ouverture session : `alice.martin`
5. Mot de passe
6. Terminer

---

## 6️⃣ JOINDRE PC AU DOMAINE

**Étape 1 : DNS**

DNS client = IP du DC

**Étape 2 : Joindre**

1. Ce PC → Propriétés
2. Nom ordinateur → Modifier
3. Domaine : `globaltech.local`
4. OK
5. Identifiants admin domaine
6. Redémarrer

---

## 📚 VOCABULAIRE

| **Terme** | **Définition** |
|-----------|----------------|
| **AD** | Active Directory |
| **DC** | Domain Controller |
| **OU** | Organizational Unit |
| **LDAP** | Protocole annuaire |
| **Kerberos** | Protocole auth AD |
| **UPN** | user@domaine |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je différencie workgroup/domaine
- [ ] Je sais installer AD DS
- [ ] Je peux créer OUs
- [ ] Je sais joindre PC au domaine

---

## 📌 POINTS-CLÉS

1. **AD** = Centralisation (vs workgroup local)
2. **DC** = Serveur avec AD DS
3. **OU** = Organisation logique
4. **Domaine** = `entreprise.local`

---

**Document - Version 1.0 - Février 2026**
