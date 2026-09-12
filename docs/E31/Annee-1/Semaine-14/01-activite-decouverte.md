# 🎲 ACTIVITÉ - S14 E31
## "Audit WiFi MFR" : Scanner et Sécuriser

---

## 🎯 OBJECTIFS

- ✅ Scanner réseaux WiFi environnants
- ✅ Identifier failles sécurité
- ✅ Évaluer niveau protection

---

## ⏱️ DURÉE : 50 min

---

## 🧩 MATÉRIEL

- Smartphones (WiFi Analyzer app)
- PC Windows (NetSpot ou WifiInfoView)
- Fiche audit (à compléter)

---

## 📋 CONTEXTE

**Mission :** Auditer WiFi de la MFR

**⚠️ LÉGAL :** Audit sur WiFi MFR uniquement (pas voisins)

---

## 🎮 DÉROULEMENT

### **PHASE 1 : Installation outils (15 min)**

**Option 1 : Smartphone Android**

App : **WiFi Analyzer** (gratuit)

**Option 2 : PC Windows**

Logiciel : **WifiInfoView** (Nirsoft, gratuit)

**Données visibles :**
- SSID (nom réseau)
- BSSID (MAC AP)
- Canal
- Puissance signal
- **Sécurité** (WEP/WPA/WPA2)
- SSID caché ou visible

---

### **PHASE 2 : Scan WiFi MFR (20 min)**

**Tableau à compléter :**

| **SSID** | **Sécurité** | **Canal** | **Caché ?** | **Failles** |
|---------|-------------|----------|------------|------------|
| MFR-ADMIN | WPA2-PSK | 6 | Non | ✅ Sécurisé |
| MFR-ELEVES | WPA2-PSK | 11 | Non | ⚠️ MDP faible ? |
| MFR-INVITES | Ouvert | 1 | Non | ❌ Aucune sécu ! |

**Analyser :**

**1. Type sécurité**
- ❌ **Ouvert** (aucune sécu) = Très dangereux
- ❌ **WEP** = Obsolète, cassé en 1 min
- ⚠️ **WPA** = Ancien, vulnérable
- ✅ **WPA2-PSK** = OK si MDP fort
- ✅✅ **WPA3** = Meilleur (récent)

**2. SSID visible**
- Visible = Normal (pas une faille)
- Caché = Faux sentiment sécurité

**3. Canal**
- Vérifier : Pas trop de réseaux sur même canal

---

### **PHASE 3 : Rapport audit (10 min)**

**Fiche synthèse :**

```
┌────────────────────────────────────┐
│   RAPPORT AUDIT WiFi MFR           │
├────────────────────────────────────┤
│ Date : ____ / ____ / 2026          │
│                                    │
│ Réseaux détectés : ____            │
│                                    │
│ ✅ Sécurisés (WPA2+) : ____        │
│ ⚠️  Faibles (WPA/WEP) : ____       │
│ ❌ Ouverts : ____                  │
│                                    │
│ FAILLES CRITIQUES :                │
│ - WiFi invité ouvert               │
│ - Mot de passe faible détecté      │
│                                    │
│ RECOMMANDATIONS :                  │
│ 1. Activer WPA2 sur WiFi invité    │
│ 2. Changer MDP WiFi élèves         │
│ 3. Isoler WiFi invité (VLAN)       │
└────────────────────────────────────┘
```

---

### **PHASE 4 : Débriefing (5 min)**

**Failles communes WiFi :**

**1. WiFi ouvert (0% sécu)**
- Tout le monde se connecte
- Trafic visible (man-in-the-middle)
- **Solution** : WPA2 minimum

**2. WEP (cassé)**
- Cassé en < 5 minutes (aircrack-ng)
- **Solution** : WPA2 obligatoire

**3. WPA2 MDP faible**
- "12345678" = Dictionnaire
- **Solution** : 20+ caractères ANSSI

**4. SSID = "Nom entreprise"**
- Cible évidente
- **Solution** : SSID neutre

**5. Pas d'isolation invité**
- Invité accède réseau interne
- **Solution** : VLAN invité (S13)

---

## 📊 STATISTIQUES ATTENDUES

**WiFi MFR typique :**
- 60% WPA2 correct
- 30% WPA2 MDP faible
- 10% Ouvert ou WEP

**WiFi domicile élèves :**
- 40% WPA2 correct
- 40% WPA2 MDP faible ("box12345")
- 20% Ouvert

---

## ✅ VALIDATION

- 100% scannent WiFi
- 80% identifient failles
- 70% proposent corrections

---

## ⚠️ ÉTHIQUE

**INTERDIT :**
- ❌ Scanner WiFi voisins (vie privée)
- ❌ Tenter connexion WiFi tiers
- ❌ Casser WEP/WPA (illégal)

**AUTORISÉ :**
- ✅ Audit WiFi MFR (autorisation)
- ✅ Scan passif (réception)
- ✅ Analyse sécurité

---

**Document - Version 1.0 - Février 2026**
