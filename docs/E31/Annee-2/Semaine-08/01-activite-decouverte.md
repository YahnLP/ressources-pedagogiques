# 🎲 ACTIVITÉ DÉCOUVERTE – S8 ANNÉE 2 – E31
## « Le Wi-Fi du Café » : Quand le Réseau Gratuit Coûte Cher

---

## 🎯 OBJECTIFS

- ✅ Faire émerger les **risques concrets** d'un Wi-Fi non sécurisé ou mal sécurisé
- ✅ Comprendre l'attaque **Evil Twin** par l'exemple
- ✅ Identifier pourquoi une simple PSK partagée est insuffisante en entreprise
- ✅ Poser la question : "comment authentifier **individuellement** chaque utilisateur ?"

---

## ⏱️ DURÉE : 30 min

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur pose la question d'accroche :**

> *"Levez la main si vous vous êtes déjà connecté au Wi-Fi d'un café, d'un hôtel ou d'un aéroport. Maintenant : qui a vérifié que c'était le vrai réseau de l'établissement, et pas un point d'accès pirate qui imitait le nom ?"*

---

## 🔬 PHASE 1 – Scénario Evil Twin (10 min)

**Le formateur décrit le scénario pas à pas :**

```
Situation réelle :
─────────────────
Café "La Tasse" → SSID : "LaTasse_WiFi" (mot de passe : "latte2024")
Votre téléphone se connecte automatiquement (réseau déjà connu).

L'attaquant :
─────────────
Assis à la table d'à côté avec un laptop.
Il crée un AP avec le même SSID : "LaTasse_WiFi"
Il émet plus fort que l'AP légitime.
Votre téléphone bascule automatiquement sur l'AP pirate.
Toutes vos connexions HTTP passent par son laptop.
```

**Questions au groupe :**

| **Question** | **Réponse attendue** |
|---|---|
| "Comment l'attaquant peut-il lire vos données ?" | Il est en MITM (Man-in-the-Middle) — tout le trafic passe par lui |
| "HTTPS vous protège-t-il ?" | Partiellement — le contenu des échanges HTTPS est chiffré, mais les DNS, les headers HTTP, les certificats peuvent fuiter |
| "Votre téléphone peut-il détecter qu'il s'est connecté à un mauvais AP ?" | Non si le SSID est identique et que l'attaquant répond aux requêtes normalement |
| "Que pourrait voir l'attaquant en pratique ?" | Identifiants sur sites non-HTTPS, mots de passe POP3/IMAP, contenu des mails non chiffrés, DNS queries |

---

## 🏢 PHASE 2 – Le Problème de l'Entreprise (8 min)

**Le formateur change de contexte :**

> *"Maintenant vous êtes responsable réseau d'une PME de 50 employés. Vous déployez le Wi-Fi avec le mot de passe 'Entreprise2026!' pour tous. Listez les problèmes."*

**Groupes de 4 — Identifiez les risques :**

| **Risque** | **Explication** |
|---|---|
| Un employé quitte l'entreprise | Il connaît encore le mot de passe — accès indéfini |
| Un stagiaire partage le mot de passe | 10 inconnus ont accès au réseau de l'entreprise |
| On ne sait pas qui s'est connecté quand | Impossible de faire un audit de connexion (qui ? quand ? quelle IP ?) |
| Un visiteur demande le Wi-Fi | Même accès qu'un employé si un seul SSID |
| L'employé rejoint le mauvais AP "Entreprise-WiFi" | Pas de vérification d'identité de l'AP |

**Conclusion du formateur :**

> *"PSK partagée = une seule clé pour tout le monde = aucune traçabilité, aucune révocation individuelle. C'est le problème que 802.1X résout : chaque utilisateur a SON identifiant et SON mot de passe — on peut le désactiver, l'auditer, lui attribuer un VLAN spécifique."*

---

## 🛡️ PHASE 3 – L'Évolution des Protections (8 min)

**Le formateur présente le "mur de la honte" et les corrections :**

| **Époque** | **Protocole** | **Problème** | **Ce qui a été fait** |
|---|---|---|---|
| 1997 | WEP | Chiffrement RC4 avec IV de 24 bits → cassé en 3 min avec Aircrack-ng | Abandonné |
| 2003 | WPA | TKIP = patch d'urgence sur WEP, vulnérabilités TKIP | Déprécié |
| 2004 | WPA2 | AES-CCMP solide, mais PSK = attaque dictionnaire possible ; 4-way handshake capturable | Encore standard |
| 2018 | WPA3 | SAE = plus de capture de handshake, Forward Secrecy, Protection des trames de gestion | Recommandé |

**Questions finales :**

**Q1.** Pourquoi capturer le 4-way handshake WPA2 permet-il une attaque offline ?

_________________________________________________________________________
_________________________________________________________________________

**Q2.** Qu'est-ce que le "Forward Secrecy" apporté par WPA3 SAE ? Pourquoi est-ce important ?

_________________________________________________________________________
_________________________________________________________________________

---

## ✍️ PHASE 4 – Synthèse (2 min)

**À noter :**

```
┌─────────────────────────────────────────────────────────────────────┐
│  SÉCURITÉ WI-FI EN RÉSUMÉ                                           │
│                                                                     │
│  WEP  → ❌ Cassé en minutes (ne jamais utiliser)                    │
│  WPA  → ⚠️  Déprécié                                                │
│  WPA2 → ✅ Standard actuel (AES) — vulnérable si PSK faible         │
│  WPA3 → ✅✅ Recommandé (SAE, Forward Secrecy)                      │
│                                                                     │
│  Personal (PSK/SAE) → clé unique partagée → PME/particuliers       │
│  Enterprise (802.1X) → login individuel → recommandé en entreprise │
│                                                                     │
│  Evil Twin = AP pirate avec même SSID → contre-mesure : MFP, WPA3  │
└─────────────────────────────────────────────────────────────────────┘
```

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
