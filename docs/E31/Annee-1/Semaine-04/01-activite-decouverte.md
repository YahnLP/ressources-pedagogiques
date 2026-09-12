# 🎲 ACTIVITÉ - S4 E31
## "Plan d'Adressage MFR" : Concevoir un Réseau Réel

---

## 🎯 OBJECTIFS

- ✅ Appliquer classes IPv4 (A/B/C)
- ✅ Choisir plage IP adaptée
- ✅ Attribuer adresses par service
- ✅ Créer plan d'adressage documenté

---

## ⏱️ DURÉE : 55 min

---

## 📋 CONTEXTE

**Maison Familiale Rurale (MFR) TECHCIEL**

**Situation :**
- 150 apprenants + 20 formateurs + 10 administratifs
- 4 services à connecter :
  - **Direction** (10 PC)
  - **Administration** (15 PC)
  - **Salle info 1** (30 PC)
  - **Salle info 2** (30 PC)
- Besoin : Plan d'adressage IPv4

---

## 🎮 DÉROULEMENT

### **PHASE 1 : Choix Classe (10 min)**

**Groupes de 4 apprentis**

**Mission :**
Choisir classe IP adaptée (A, B ou C)

**Réflexion guidée :**

**Classe A (10.0.0.0/8) ?**
- Nb hôtes : 16 millions
- Adapté ? ❌ **Surdimensionné** (MFR = 85 PC)

**Classe B (172.16.0.0/16) ?**
- Nb hôtes : 65 534
- Adapté ? ⚠️ Possible mais surdimensionné

**Classe C (192.168.X.0/24) ?**
- Nb hôtes : 254 par réseau
- Adapté ? ✅ **OPTIMAL** (85 PC < 254)

**Choix recommandé :** Classe C privée  
**Réseau choisi :** `192.168.1.0/24`

---

### **PHASE 2 : Répartition Adresses (25 min)**

**Tableau à compléter :**

| **Service** | **Nb PC** | **Plage IP** | **Passerelle** | **Remarques** |
|------------|----------|-------------|---------------|---------------|
| **Direction** | 10 | 192.168.1.10 - .19 | 192.168.1.1 | Début réseau |
| **Administration** | 15 | 192.168.1.20 - .34 | 192.168.1.1 | Après Direction |
| **Salle Info 1** | 30 | 192.168.1.40 - .69 | 192.168.1.1 | Bloc 30 |
| **Salle Info 2** | 30 | 192.168.1.70 - .99 | 192.168.1.1 | Bloc 30 |
| **Serveurs** | 3 | 192.168.1.5 - .7 | 192.168.1.1 | Réservé début |
| **Imprimantes** | 5 | 192.168.1.100 - .104 | 192.168.1.1 | Fin réseau |

**Adresses spéciales :**
- **Passerelle (routeur)** : `192.168.1.1`
- **Réseau** : `192.168.1.0`
- **Broadcast** : `192.168.1.255`

**Total utilisé :** ~95 adresses sur 254 disponibles

---

### **PHASE 3 : Schéma Réseau (15 min)**

**Dessiner schéma réseau :**

```
                Internet
                   |
              [Routeur]
            192.168.1.1
                   |
              [Switch Central]
                   |
      ┌────────────┼───────────┬────────────┐
      |            |           |            |
  [Direction]  [Admin]   [Salle 1]    [Salle 2]
   .10-.19     .20-.34    .40-.69      .70-.99
    (10 PC)    (15 PC)    (30 PC)      (30 PC)
```

---

### **PHASE 4 : Documentation (5 min)**

**Créer fiche récapitulative :**

```
┌─────────────────────────────────────┐
│  PLAN ADRESSAGE MFR TECHCIEL        │
├─────────────────────────────────────┤
│  Réseau : 192.168.1.0/24            │
│  Masque : 255.255.255.0             │
│  Passerelle : 192.168.1.1           │
│  DNS : 192.168.1.2                  │
│                                     │
│  Services :                         │
│  - Direction : .10-.19              │
│  - Admin : .20-.34                  │
│  - Salle 1 : .40-.69                │
│  - Salle 2 : .70-.99                │
│  - Serveurs : .5-.7                 │
│  - Imprimantes : .100-.104          │
│                                     │
│  Total : 95 hôtes / 254 disponibles │
└─────────────────────────────────────┘
```

---

## 📊 DÉBRIEFING (10 min)

**Questions guidées :**

**1. Pourquoi classe C ?**

**Réponse :**
- MFR = 85 PC
- Classe C = 254 hôtes
- Classe B (65k) = surdimensionné
- ✅ Classe C adaptée

---

**2. Pourquoi 192.168.x.x ?**

**Réponse :**
- Adresse **privée** (RFC 1918)
- Pas routée sur Internet
- Sécurité + économie IP publiques

---

**3. Lien avec OSI**

**C3 Réseau (S3) :**
- Adresse IP = Couche 3
- Routage entre réseaux

---

**4. Bonnes pratiques**

✅ **Réserver début** : Serveurs, équipements critiques  
✅ **Bloquer par service** : Facilite gestion  
✅ **Laisser marge** : Évolution future  
✅ **Documenter** : Plan écrit obligatoire  

---

## ✅ VALIDATION ACTIVITÉ

**Réussie si :**
- ✅ Classe adaptée choisie
- ✅ Plages IP cohérentes (pas de chevauchement)
- ✅ Schéma réseau lisible
- ✅ Documentation complète

---

## 📸 PORTFOLIO

**À conserver :**
- Plan d'adressage MFR complété
- Schéma réseau
- Fiche récapitulative

---

## 📝 VARIANTE : ENTREPRISE

**Adapter pour entreprise d'alternance :**

**Services différents :**
- Production
- Bureau études
- Administration
- Logistique

**Classe B si grande entreprise (> 254 PC)**

---

**Document - Version 1.0 - Février 2026**
