# 🔬 TRAVAUX PRATIQUES — S8 · 3ᵉ ANNÉE · E31
## WLC Enterprise : SSIDs · QoS WMM · WPA3 · Fast Roaming · Détection Rogue AP

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée**
> **Environnement** : ☐ WLC physique  ☐ Cisco Meraki Demo  ☐ Cisco Packet Tracer  ☐ GNS3 vWLC
> **Épreuve ciblée** : **E31** – Infrastructure réseau · **E32** (sécurité WPA3)

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S4.5** | Architecture WLC — CAPWAP, modes AP |
| **S4.6** | WiFi 6 — identifier les fonctionnalités sur le WLC |
| **S4.7** | Fast Roaming — configurer 802.11r/k/v |
| **S4.8** | QoS WMM — configurer les files de priorité |
| **S4.9** | WPA3 — créer et sécuriser un SSID WPA3 |
| **C2.2** | Naviguer dans l'interface WLC et configurer |
| **C3.1** | Documenter le schéma d'architecture WLAN |

---

## 🗺️ Objectif du TP

> Tu dois configurer l'infrastructure WiFi de l'entreprise TECHPRO avec :
> - 3 SSIDs distincts pour 3 populations d'utilisateurs
> - QoS WMM pour prioriser la VoIP
> - WPA3 sur le réseau corporate
> - Fast roaming pour les utilisateurs mobiles
> - Détection des APs non autorisés

```
Infrastructure cible TECHPRO :
  WLC IP : 192.168.100.10
  AP1     : Salle de réunion (IP: 192.168.100.21)
  AP2     : Open space (IP: 192.168.100.22)
  AP3     : Couloir/Hall (IP: 192.168.100.23)

SSIDs à créer :
  "TECHPRO-Corp"  → VLAN 10, WPA3-Enterprise ou WPA3-Personal, WMM activé, VoIP prioritaire
  "TECHPRO-Guest" → VLAN 20, WPA3-Personal (SAE), portail captif, 5 Mbps/client max
  "TECHPRO-IoT"   → VLAN 30, WPA2-PSK, isolation client, débit limité
```

---

## 🟢 NIVEAU 1 — Explorer l'interface WLC et les APs (10 min)

> Selon ton environnement, connecte-toi à l'interface de gestion WLC.

**1.1** — Accède au tableau de bord principal. Note les informations globales :

```
Nombre d'APs enregistrés : _______
Nombre de clients connectés : _______
Bande passante globale utilisée : _______
```

**1.2** — Navigue vers la section **Wireless** ou **Access Points**. Pour chaque AP, note :

| AP | Nom | Mode actuel | Canal 2.4G | Canal 5G | Clients |
|---|---|---|---|---|---|
| AP1 | | | | | |
| AP2 | | | | | |
| AP3 | | | | | |

**1.3** — Identifie quel protocole est utilisé entre le WLC et les APs :

```
Protocole WLC ↔ APs : _______________________
Port UDP contrôle : _______   Port UDP données : _______
```

**1.4** — Cherche si un AP est en mode "Monitor" ou "Rogue Detector". Qu'est-ce que cela signifie ?

```
Mode Monitor signifie : _________________________________________________________
```

---

## 🟡 NIVEAU 2 — Créer les 3 SSIDs (20 min)

### SSID 1 — TECHPRO-Corp (réseau corporate)

**2.1** — Dans **WLANs** ou **SSIDs**, crée un nouveau SSID :

```
Nom (SSID) : TECHPRO-Corp
VLAN/Interface : VLAN 10 (ou interface Management si PT)
Sécurité : WPA3-Personal (SAE) ou WPA2-Enterprise si RADIUS disponible
  Mot de passe PSK (si Personnel) : TechPro2024!
  Méthode EAP (si Enterprise) : PEAP
Statut : Enabled
```

Note les paramètres configurés :

```
SSID créé ? ☐ Oui ☐ Non
VLAN associé : _______
Méthode sécurité : _______________________
```

### SSID 2 — TECHPRO-Guest

**2.2** — Crée le SSID invité :

```
Nom (SSID) : TECHPRO-Guest
VLAN/Interface : VLAN 20
Sécurité : WPA3-Personal (SAE) ou WPA2-PSK
  Mot de passe : Guest2024
Portail captif (si disponible) : Enabled
Isolation client : ☐ Enabled (les clients invités ne se voient pas entre eux)
```

### SSID 3 — TECHPRO-IoT

**2.3** — Crée le SSID IoT :

```
Nom (SSID) : TECHPRO-IoT
VLAN/Interface : VLAN 30
Sécurité : WPA2-PSK (les capteurs IoT ne supportent pas WPA3 souvent)
  Mot de passe : IoTSecret2024
Isolation client : ☐ Enabled (capteurs ne se parlent pas entre eux)
Débit maximum par client : 5 Mbps (si disponible sur le WLC)
```

**2.4** — Vérifie que les 3 SSIDs sont actifs :

```
TECHPRO-Corp   : ☐ Enabled ☐ Disabled
TECHPRO-Guest  : ☐ Enabled ☐ Disabled
TECHPRO-IoT    : ☐ Enabled ☐ Disabled
```

---

## 🟠 NIVEAU 3 — Configurer la QoS WMM (15 min)

### Activer WMM sur TECHPRO-Corp

**3.1** — Dans les paramètres du SSID TECHPRO-Corp, cherche la section **QoS** ou **Advanced** :

```
WMM Policy : ☐ Disabled ☐ Allowed ☐ Required
Configurer sur : Required (obligatoire — tous les clients doivent supporter WMM)
```

**3.2** — Identifie les 4 files de priorité WMM dans l'interface :

```
File 1 (priorité la plus haute) : _______________  → Pour : ___________________
File 2 : _______________  → Pour : ___________________
File 3 : _______________  → Pour : ___________________
File 4 (priorité la plus basse) : _______________  → Pour : ___________________
```

**3.3** — Configure la priorité QoS du SSID TECHPRO-Corp sur **Platinum** ou **Voice** :

```
QoS Level/Priority : _______________________
Cela signifie que tout le trafic sur ce SSID est traité comme : ________________
```

**3.4** — Pour TECHPRO-IoT, configure la priorité sur **Silver** ou **Background** :

```
Justification : les capteurs IoT ont des données non urgentes → ________________
```

**3.5** — Complète le tableau de mapping QoS :

| SSID | Priorité QoS WLC | File WMM | Cas d'usage |
|---|---|---|---|
| TECHPRO-Corp | Platinum/Gold | Voice/Video | VoIP, vidéoconférence |
| TECHPRO-Guest | Silver | Best Effort | Navigation web |
| TECHPRO-IoT | Bronze/Background | Background | Capteurs IoT |

---

## 🔵 NIVEAU 4 — Fast Roaming et sécurité avancée (20 min)

### Configurer Fast Roaming 802.11r

**4.1** — Dans la configuration du SSID TECHPRO-Corp (section **Security** → **Advanced** ou **Layer 2**) :

```
802.11r (Fast BSS Transition) : ☐ Enabled ☐ Disabled
Configurer sur : Enabled

FT Roaming (Over-the-Air vs Over-the-DS) :
  Over-the-Air : le client contacte directement le nouvel AP → plus rapide
  Over-the-DS  : le client passe par le WLC → plus compatible
Choix recommandé : _______________
```

**4.2** — Cherche également 802.11k et 802.11v :

```
802.11k (Neighbor Reports) : ☐ Enabled ☐ Non disponible
802.11v (BSS Transition)   : ☐ Enabled ☐ Non disponible
```

**4.3** — Explique l'impact de 802.11v dans le contexte TECHPRO :

```
Avec 802.11v activé, si AP1 (salle de réunion) est surchargé et qu'AP2 (open space)
est libre, le WLC peut : __________________________________________________
Ce mécanisme s'appelle : _______________________________________________
```

### Vérifier WPA3 et PMF

**4.4** — Dans la configuration de sécurité de TECHPRO-Corp, cherche PMF :

```
PMF (Protected Management Frames) :
  ☐ Disabled ☐ Optional ☐ Required
WPA3 force PMF à : _______________________

Sans PMF, un attaquant peut envoyer des trames Deauth falsifiées pour : ________
Avec PMF activé : _____________________________________________________________
```

---

## 🔴 NIVEAU 5 — Détection Rogue AP et documentation (15 min)

### Détection des APs non autorisés

**5.1** — Dans la section **Wireless** ou **Security** → **Rogue AP** du WLC :

```
Rogue AP Detection : ☐ Enabled ☐ Disabled
Nombre de Rogue APs détectés actuellement : _______
```

**5.2** — Explore la liste des Rogue APs (si des APs sont détectés) :

```
Un Rogue AP est classé comme :
  ☐ Friendly : AP connu mais non géré par ce WLC (ex : AP d'un autre département)
  ☐ Malicious : AP suspect (même SSID que le réseau corp → evil twin possible)
  ☐ Unclassified : AP inconnu, pas encore qualifié

Action sur un Rogue AP malveillant : _________________________________________
```

**5.3** — Documente l'architecture WLAN complète de TECHPRO en dessinant le schéma :

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Dessine :                                                                   │
│  - Le WLC au centre                                                          │
│  - Les 3 APs avec leurs modes et localisations                              │
│  - Les 3 SSIDs avec leurs VLANs et méthodes de sécurité                     │
│  - Les clients par type (laptop Corp, smartphone Guest, capteur IoT)         │
│  - Les liens CAPWAP (avec les ports UDP)                                     │
│  - Le fast roaming entre AP1 et AP2                                          │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**5.4** — Questions de synthèse :

```
Pourquoi l'isolation client est-elle importante sur TECHPRO-Guest ?
___________________________________________________________________________

Quel est l'avantage de WPA3-Personal (SAE) vs WPA2-PSK pour TECHPRO-Corp ?
___________________________________________________________________________

Si l'hôpital du contexte initial (activité découverte) ne dispose que d'un accès
internet instable vers le WLC dans le bâtiment B, quel mode AP recommanderais-tu ?
Mode : _____________________  Raison : _________________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Créer un SSID sur WLC avec VLAN et sécurité | ☐ | ☐ | ☐ |
| Configurer WMM et les priorités QoS | ☐ | ☐ | ☐ |
| Activer 802.11r pour le fast roaming | ☐ | ☐ | ☐ |
| Distinguer WPA3-Personal, Enterprise, OWE | ☐ | ☐ | ☐ |
| Expliquer PMF et son rôle | ☐ | ☐ | ☐ |
| Décrire les 4 modes AP (Local/Flex/Mesh/Monitor) | ☐ | ☐ | ☐ |
| Dessiner le schéma WLAN enterprise annoté | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.1-2 — 3 SSIDs créés avec sécurité et VLANs corrects | /8 |
| Niv.3 — QoS WMM configurée et tableau de mapping complété | /5 |
| Niv.4 — Fast Roaming et PMF expliqués et configurés | /7 |
| Niv.5 — Schéma annoté + questions de synthèse | /5 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Niv.1 — Protocole

```
CAPWAP · UDP 5246 (contrôle) · UDP 5247 (données)
Mode Monitor = AP qui scanne le spectre RF sans accepter de clients
              → Détecte les Rogue APs et mesure la qualité RF
```

## Niv.3 — QoS WMM

```
4 files WMM (de haute à basse priorité) :
  VO (Voice)      → VoIP, appels temps réel
  VI (Video)      → Streaming, vidéoconférence
  BE (Best Effort)→ Navigation web, email
  BK (Background) → Sauvegardes, mises à jour

TECHPRO-Corp → Platinum = tout le trafic classé en Voice par défaut (cas VoIP)
TECHPRO-IoT  → Background = trafic non urgent, ne perturbe pas les autres SSIDs
```

## Niv.4 — Fast Roaming

```
802.11v (BSS Transition Management) + 802.11k (Neighbor Reports) permettent
le "client steering" = WLC suggère à un client de migrer vers un AP moins chargé

PMF Required = obligatoire pour WPA3 · protège contre Deauth flooding
```

## Niv.5 — Questions synthèse

```
Isolation client Guest : les visiteurs ne doivent pas accéder aux appareils
d'autres visiteurs (RGPD, sécurité, impression impromptue…)

SAE vs PSK : SAE résiste aux attaques offline (pas de capture+brute force)
             PFS : sessions passées sécurisées même si clé compromise

Mode FlexConnect : trafic local si WLC inaccessible via WAN défaillant
```

---

*TP WiFi Avancé + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S8*
*Document Portfolio E31 — Compétences S4.5 · S4.6 · S4.7 · S4.8 · S4.9 · C2.2 · C3.1*
