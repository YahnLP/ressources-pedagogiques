# 📝 DEVOIR & LIVRABLE PORTFOLIO — S8 · 3ᵉ ANNÉE · E31
## Wireless Avancé : WLC · WiFi 6 · Roaming · QoS WMM · WPA3

---

> **Module** : E31 – Infrastructure Réseau — WiFi enterprise avancé
> **Épreuve visée** : **E31** · **E32** (sécurité WPA3)
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 50 min)

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S4.5** | Architecture WLC, CAPWAP, modes AP | /20 |
| **S4.6** | WiFi 6 — technologies OFDMA, MU-MIMO, BSS Coloring | /20 |
| **S4.7** | Roaming — 802.11r/k/v, délais, mécanismes | /20 |
| **S4.8** | QoS WMM — 4 files, mapping DSCP | /15 |
| **S4.9** | WPA3 — SAE, PMF, OWE, avantages | /25 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation professionnelle

> **Tu es ingénieur réseau** pour une entreprise agroalimentaire qui construit un nouveau
> siège social "connecté" de 800 employés répartis sur 3 étages.
> Chaque étage aura 15 APs WiFi 6. 200 appareils IoT (capteurs qualité, robots entrepôt).
> VoIP sur WiFi pour tous les téléphones.
> Le DSI te demande une proposition d'architecture complète.

---

## 🅰️ PARTIE A — En classe (45 min)

### 🏛️ Exercice 1 — Architecture WLC (/20)

**1.a** — Explique en 4 lignes pourquoi une architecture à APs standalone est inadaptée pour 45 APs sur 3 étages : *(6 pts)*

```
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**1.b** — Complète le schéma simplifié de l'architecture WLAN centralisée : *(8 pts)*

```
┌─────────────────────────────────────────────────────────┐
│  Switch Cœur ─── [ _______ ] ← Nom de l'équipement    │
│                       │                                  │
│          Protocole : _______ (UDP ____ / ____)          │
│                  ↓ ↓ ↓                                  │
│           [ APs ________ ]  ← Adjectif des APs          │
│           Étage 1 : AP1-AP15                            │
│           Étage 2 : AP16-AP30                           │
│           Étage 3 : AP31-AP45                           │
└─────────────────────────────────────────────────────────┘
```

**1.c** — Pour les 200 robots d'entrepôt qui se déplacent dans une grande halle sans câblage possible, quel mode AP recommandes-tu ? Justifie. *(6 pts)*

```
Mode AP recommandé : ___________________________
Justification : _________________________________________________________________
Comment le trafic circule-t-il dans ce mode ? ___________________________________
Inconvénient principal : ________________________________________________________
```

---

### 📡 Exercice 2 — WiFi 6 (/20)

**2.a** — L'entrepôt a 200 capteurs IoT sur le même canal WiFi. Quelle technologie WiFi 6 résout spécifiquement ce problème de congestion ? Explique son fonctionnement. *(8 pts)*

```
Technologie : ___________________________
Fonctionnement :
___________________________________________________________________________
___________________________________________________________________________
Avantage vs WiFi 5 pour ce scénario : __________________________________________
```

**2.b** — Pour les téléphones VoIP qui se déplacent entre bureaux, cite 2 technologies WiFi 6 bénéfiques et explique pourquoi : *(8 pts)*

```
Technologie 1 : _______________________________________________________________
  Bénéfice pour VoIP : _________________________________________________________

Technologie 2 : _______________________________________________________________
  Bénéfice pour VoIP : _________________________________________________________
```

**2.c** — Quel est le débit théorique maximum de WiFi 6 ? Pourquoi ce débit ne sera-t-il jamais atteint en pratique ? *(4 pts)*

```
Débit max théorique : _______________________
Raisons pratiques (2 minimum) :
  1. __________________________________________________________________________
  2. __________________________________________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/60)

### 🔄 Exercice 3 — Roaming (/20)

> Le scénario : une commerciale se déplace avec son téléphone VoIP WiFi du bureau 1 (AP_Bureau, étage 1) vers la salle de réunion (AP_Meeting, étage 2) pendant un appel.

**3.a** — Décris en 5 étapes ce qui se passe SANS fast roaming : *(8 pts)*

```
Étape 1 : ___________________________________________________________________
Étape 2 : ___________________________________________________________________
Étape 3 : ___________________________________________________________________
Étape 4 : ___________________________________________________________________
Étape 5 : ___________________________________________________________________
Durée totale estimée : _____________    Impact sur l'appel VoIP : _____________
```

**3.b** — Complète le tableau des protocoles fast roaming : *(9 pts)*

| Protocole | Problème résolu | Mécanisme (1-2 lignes) | Bénéfice mesuré |
|---|---|---|---|
| 802.11r | | | < 50ms handoff |
| 802.11k | | | Scan réduit |
| 802.11v | | | Load balancing |

**3.c** — 802.11r, k et v sont souvent activés ensemble. Quel est l'impact combiné sur l'expérience VoIP ? *(3 pts)*

```
___________________________________________________________________________
___________________________________________________________________________
```

---

### 🛡️ Exercice 4 — WPA3 (/25)

**4.a** — L'entreprise utilise actuellement WPA2-PSK "AgroConnect2019" pour tout le WiFi.
Identifie 3 problèmes de sécurité et propose la solution WPA3 correspondante : *(15 pts)*

| Problème WPA2-PSK | Solution WPA3 |
|---|---|
| Attaque offline dictionary : capturer le handshake 4-way et cracker hors ligne | |
| Trame de déauthentification falsifiée : attaquant peut chasser les clients | |
| Réseau invité ouvert (portail captif) : trafic en clair, écoutable | |

**4.b** — Compare WPA3-Personal (SAE) et WPA3-Enterprise pour le réseau corporate : *(6 pts)*

```
WPA3-Personal (SAE) :
  Authentification basée sur : _________________________________________________
  Avantage clé vs WPA2-PSK : __________________________________________________
  Limite : ____________________________________________________________________

WPA3-Enterprise :
  Authentification basée sur : _________________________________________________
  Avantage supplémentaire : ____________________________________________________
  Infrastructure requise : _____________________________________________________

Pour une entreprise de 800 employés, lequel recommandes-tu et pourquoi ?
Choix : ________________  Raison : ____________________________________________
```

**4.c** — Un ingénieur IT propose de laisser le SSID invité en "WPA2 ouvert" pour la compatibilité des vieux appareils. Quelle est ton objection et ta proposition de compromis ? *(4 pts)*

```
Objection : __________________________________________________________________
Proposition WPA3 pour résoudre ce problème tout en gardant la compatibilité :
___________________________________________________________________________
```

---

### 📐 Exercice 5 — Architecture complète et QoS (/15)

**5.a** — Propose le plan des 3 SSIDs pour le siège social agroalimentaire : *(9 pts)*

| SSID | VLAN | Sécurité | QoS WMM | Isolation client | Utilisateurs |
|---|---|---|---|---|---|
| | 10 | WPA3-Enterprise | Platinum (Voice) | Non | Employés |
| | 20 | WPA3-Personal SAE | Silver (BE) | Oui | Invités |
| | 30 | WPA2-PSK | Background | Oui | IoT/Robots |

**5.b** — Explique pourquoi l'isolation client est nécessaire sur le SSID invité mais pas sur le SSID employé : *(6 pts)*

```
Sur SSID invité (isolation ON) :
  → Les visiteurs ne peuvent pas : ____________________________________________
  → Risques évités : ___________________________________________________________

Sur SSID employé (isolation OFF) :
  → Les employés peuvent : ___________________________________________________
  → Ce qui est nécessaire pour : _______________________________________________
```

---

## 🏅 Barème global

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Architecture WLC | S4.5 | /20 | ≥ 11 |
| Ex. 2 — WiFi 6 | S4.6 | /20 | ≥ 11 |
| Ex. 3 — Roaming | S4.7 | /20 | ≥ 11 |
| Ex. 4 — WPA3 | S4.9 | /25 | ≥ 14 |
| Ex. 5 — Architecture + QoS | S4.8 + C3.1 | /15 | ≥ 8 |
| **TOTAL** | | **/100** | **≥ 55** |

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** : 45 APs autonomes = 45 configurations manuelles indépendantes, pas de vue centralisée, roaming lent (réauthentification complète entre APs), pas de QoS cohérente ni de détection rogue AP

**1.b** : WLC · CAPWAP · UDP 5246/5247 · Lightweight (thin)

**1.c** : **Mesh** · Les robots n'ont pas de câble Ethernet dans l'entrepôt · Le trafic remonte par backhaul radio de maille en maille jusqu'au Root AP câblé · Inconvénient : chaque saut radio ajoute de la latence (2-5ms) et réduit le débit disponible

## Correction Exercice 2

**2.a** : **OFDMA** (Orthogonal Frequency Division Multiple Access) · Subdivise le canal WiFi en Resource Units (RUs) de différentes tailles · 200 capteurs peuvent transmettre simultanément sur des RUs dédiés au lieu d'attendre leur tour → x4 efficacité en haute densité

**2.b** :
- MU-MIMO 8×8 : 8 téléphones peuvent recevoir/émettre simultanément sans attendre leur tour → réduit la latence
- 802.11r (Fast BSS Transition) : roaming < 50ms entre APs → l'appel VoIP ne se coupe pas lors des déplacements

**2.c** : 9,6 Gbps · Conditions idéales = 8 clients parfaitement positionnés, canal de 160 MHz, 1024-QAM · En pratique : interférences, obstacles, clients lointains → débit réel 20-30% du max théorique

## Correction Exercice 3

**3.a** : 1. Téléphone détecte signal AP_Bureau trop faible · 2. Scan tous les canaux pour trouver APs (2-8s) · 3. Désassociation d'AP_Bureau · 4. Association à AP_Meeting + ré-authentification RADIUS (500ms-2s) · 5. Potentiellement nouveau bail DHCP (1-3s) · Total 4-14s · Impact : appel coupé

**3.b** :
- 802.11r : réauthentification lente / pré-partager clés FT via WLC / < 50ms
- 802.11k : le client ne sait pas vers quel AP aller / liste APs voisins avec RSSI / scan réduit
- 802.11v : AP surchargé avec meilleur AP disponible / WLC envoie suggestion de migration / équilibrage de charge

**3.c** : Les 3 protocoles combinés permettent un roaming transparent (< 50ms) : k identifie le meilleur AP cible avant que le signal baisse, r permet la transition sans réauthentification complète, v assure l'équilibrage → VoIP continue sans interruption perceptible

## Correction Exercice 4

**4.a** :

| Problème WPA2 | Solution WPA3 |
|---|---|
| Offline dictionary attack | WPA3-SAE (Dragonfly) + Perfect Forward Secrecy |
| Déauth falsifiée | PMF (Protected Management Frames) obligatoire |
| Réseau invité ouvert | OWE (Opportunistic Wireless Encryption) |

**4.b** : Personal = mot de passe partagé avec SAE / résistance brute force / limite = 1 seul secret partagé pour tous · Enterprise = identités individuelles 802.1X/RADIUS / révocation individuelle / nécessite RADIUS + PKI · Pour 800 employés → Enterprise (révocation employé qui part, traçabilité, politiques par groupe)

**4.c** : WPA2 ouvert = trafic en clair, écoutable par n'importe qui sur le réseau · Proposition : **WPA3-OWE** (Enhanced Open) — aucun mot de passe mais chiffrement automatique Diffie-Hellman → compatible avec les appareils récents + peut coexister avec SSID WPA2 pour les très vieux appareils

---

*Devoir + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S8*
*Épreuves E31 + E32 | Compétences S4.5 · S4.6 · S4.7 · S4.8 · S4.9 · C2.2 · C3.1*
