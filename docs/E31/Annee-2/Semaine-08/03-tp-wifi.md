# 🔬 TP PACKET TRACER – S8 ANNÉE 2 – E31
## Sécurité Wi-Fi : WPA2-Personal et WPA2-Enterprise (802.1X/RADIUS)

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Configurer un SSID Wi-Fi WPA2-Personal (PSK) et tester la connexion
- ✅ Configurer un SSID Wi-Fi WPA2-Enterprise avec serveur RADIUS (802.1X)
- ✅ Tester l'authentification individuelle par identifiant/mot de passe
- ✅ Observer le comportement lors d'une mauvaise PSK ou de mauvais credentials
- ✅ Analyser la politique de sécurité d'un réseau Wi-Fi existant

---

## ⏱️ DURÉE : 65 min

---

## 📋 TOPOLOGIE

```
                    ┌─────────────────────────────────────────────────────┐
                    │                                                     │
         [AP-CORP]  │  [AP-GUEST]                                        │
          (802.1X)  │  (WPA2-PSK)                                        │
             │      │      │                                              │
             └──────┴──────┘                                              │
                    │                                                     │
                  [SW-CORE]                                               │
                    │                                                     │
         ┌──────────┼──────────┐                                         │
         │          │          │                                         │
    [SRV-RADIUS]  [PC-FILAIRE]  [SERVEUR-WEB]                           │
    10.0.0.10     10.0.0.20     10.0.0.30                               │
                                                                         │
Clients Wi-Fi :                                                          │
  PC-EMPLOYE  (SSID: CORP-SECURE, 802.1X, user: alice/Alice2026!)       │
  PC-VISITEUR (SSID: GUEST-WIFI, PSK: Visiteur123!)                     │
  PC-PIRATE   (test connexion CORP avec mauvais credentials)            │
                    └─────────────────────────────────────────────────────┘
```

---

## 📋 PARAMÈTRES DE CONFIGURATION

### SSID 1 — Réseau Entreprise (WPA2-Enterprise / 802.1X)

| **Paramètre** | **Valeur** |
|---|---|
| SSID | `CORP-SECURE` |
| Sécurité | WPA2-Enterprise |
| Chiffrement | AES |
| Serveur RADIUS IP | 10.0.0.10 |
| RADIUS Secret | `RadSecret2026` |
| Utilisateurs | alice / `Alice2026!` ; bob / `Bob2026!` |

### SSID 2 — Réseau Invités (WPA2-Personal / PSK)

| **Paramètre** | **Valeur** |
|---|---|
| SSID | `GUEST-WIFI` |
| Sécurité | WPA2-PSK |
| Chiffrement | AES |
| Mot de passe PSK | `Visiteur123!` |

---

## 🧪 PARTIE 1 – Configuration du réseau invités WPA2-Personal (15 min)

### 1.1 – Configuration AP-GUEST

**Accédez à AP-GUEST → Config → Wireless :**

Configurez le premier SSID avec :

| **Champ** | **Valeur à saisir** |
|---|---|
| SSID Name | |
| Authentication | |
| Encryption | |
| PSK Pass Phrase | |

---

### 1.2 – Connexion PC-VISITEUR

**PC-VISITEUR → Config → Wireless :**

| **Champ** | **Valeur** |
|---|---|
| SSID | |
| Auth | |
| PSK | |

**Vérification :**

```
PC-VISITEUR# ping 10.0.0.30     → _______   (serveur web)
PC-VISITEUR# ping 10.0.0.10     → _______   (RADIUS — doit être accessible ?)
```

**Q1.** PC-VISITEUR peut-il accéder au serveur RADIUS (10.0.0.10) ? Est-ce souhaitable pour un réseau invité ?

_________________________________________________________________________
_________________________________________________________________________

---

### 1.3 – Test avec mauvaise PSK

Configurez PC-PIRATE avec SSID `GUEST-WIFI` mais PSK `MauvaisMotDePasse` :

**Résultat de connexion : _______ (connecté / non connecté)**

**Q2.** Le client est-il averti que la PSK est incorrecte ou simplement n'arrive-t-il pas à se connecter ? Que se passe-t-il réellement au niveau du 4-way handshake ?

_________________________________________________________________________
_________________________________________________________________________

---

## 🔬 PARTIE 2 – Configuration 802.1X WPA2-Enterprise (25 min)

### 2.1 – Configuration du serveur RADIUS

**SRV-RADIUS → Services → AAA :**

**Ajout du client AP (Authenticator) :**

| **Champ** | **Valeur** |
|---|---|
| Network Configuration → Client Name | AP-CORP |
| Client IP | (IP de AP-CORP) |
| Secret | `RadSecret2026` |

**Ajout des utilisateurs :**

| **Username** | **Password** |
|---|---|
| alice | Alice2026! |
| bob | Bob2026! |

---

### 2.2 – Configuration AP-CORP

**AP-CORP → Config → Wireless :**

| **Champ** | **Valeur** |
|---|---|
| SSID Name | `CORP-SECURE` |
| Authentication | WPA2-Enterprise |
| Encryption | AES |
| RADIUS Server IP | `10.0.0.10` |
| RADIUS Secret | `RadSecret2026` |

---

### 2.3 – Connexion PC-EMPLOYE (utilisateur légitime : alice)

**PC-EMPLOYE → Config → Wireless :**

| **Champ** | **Valeur** |
|---|---|
| SSID | `CORP-SECURE` |
| Auth | WPA2-Enterprise |
| Username | `alice` |
| Password | `Alice2026!` |

**Vérification :**

```
PC-EMPLOYE# ping 10.0.0.20     → _______   (PC filaire)
PC-EMPLOYE# ping 10.0.0.30     → _______   (serveur web)
```

**Q3.** PC-EMPLOYE est-il connecté ? ___________

---

### 2.4 – Test avec mauvais credentials

**PC-PIRATE → SSID `CORP-SECURE`, username : `hacker`, password : `test123` :**

**Résultat : _______**

**Q4.** Que répond le serveur RADIUS dans ce cas ? Qui prend la décision de refuser ? (Supplicant / Authenticator / RADIUS)

_________________________________________________________________________

---

### 2.5 – Révocation d'un utilisateur (simulation)

**Supprimez l'utilisateur `bob` du serveur RADIUS :**

Si un PC était connecté avec `bob`, que se passerait-il lors de sa prochaine tentative d'authentification ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 PARTIE 3 – Analyse comparative (15 min)

### 3.1 – Tableau comparatif de vos tests

| **Scénario** | **SSID** | **Résultat** | **Qui authentifie ?** |
|---|---|---|---|
| PC-VISITEUR + bonne PSK | GUEST-WIFI | | |
| PC-PIRATE + mauvaise PSK | GUEST-WIFI | | |
| PC-EMPLOYE (alice) + bons creds | CORP-SECURE | | |
| PC-PIRATE + mauvais creds | CORP-SECURE | | |

---

### 3.2 – Questions d'analyse

**Q5.** Sur le réseau GUEST-WIFI (WPA2-Personal), si un visiteur partage le mot de passe `Visiteur123!` avec un inconnu, que peut faire l'admin réseau pour résoudre le problème ?

_________________________________________________________________________
_________________________________________________________________________

**Q6.** Sur CORP-SECURE (WPA2-Enterprise), si un employé quitte l'entreprise, quelle action suffit pour lui retirer l'accès Wi-Fi ? Comparez avec la solution WPA2-Personal.

_________________________________________________________________________
_________________________________________________________________________

**Q7.** Un stagiaire vous dit : "Pour sécuriser encore plus GUEST-WIFI, je vais cacher le SSID." Quelle est votre réponse ?

_________________________________________________________________________
_________________________________________________________________________

**Q8.** Un attaquant crée un AP avec le SSID `CORP-SECURE`. Un PC-EMPLOYE se connecte à cet AP pirate. L'AP pirate ne connaît pas le secret RADIUS. Que se passe-t-il pour le PC-EMPLOYE ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 – Config AP-GUEST | SSID + WPA2-PSK configurés | /2 |
| Partie 1 – PC-VISITEUR | Connexion + ping réussis | /2 |
| Partie 1 – Q1 + Q2 | Questions d'analyse PSK | /2 |
| Partie 2 – RADIUS | Clients + utilisateurs configurés | /3 |
| Partie 2 – AP-CORP | SSID Enterprise + IP RADIUS | /2 |
| Partie 2 – PC-EMPLOYE | Connexion 802.1X réussie | /2 |
| Partie 2 – Q3 + Q4 | Analyse RADIUS | /2 |
| Partie 3 – Tableau | 4 scénarios renseignés | /2 |
| Partie 3 – Q5 à Q8 | Analyse comparative | /3 |
| **TOTAL** | | **/20** |

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
