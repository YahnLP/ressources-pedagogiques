# 🗂️ AIDE-MÉMOIRE WIRELESS AVANCÉ — À PLASTIFIER
## WLC · WiFi 6 · Roaming · QoS WMM · WPA3 · BAC PRO CIEL · E31 · 3ᵉ année S8

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 🏛️ Architecture WLC — L'essentiel

```
WLC centralise : Auth, QoS, Sécurité, Config, Détection Rogue AP
APs Lightweight : aucune config locale, tout vient du WLC
CAPWAP          : UDP 5246 (contrôle) · UDP 5247 (données)

Modes AP :
  Local      → tunnel complet vers WLC (standard)
  FlexConnect → trafic local si WLC inaccessible (agences)
  Mesh       → backhaul radio sans câble (extérieur/entrepôt)
  Monitor    → surveillance RF + détection Rogue AP
```

---

## 📶 WiFi 6 (802.11ax) — 4 technologies clés

```
OFDMA    → plusieurs clients simultanés sur le MÊME canal
           (subdivise en Resource Units)
           Idéal : haute densité, IoT, petits paquets

MU-MIMO  → 8 clients TX/RX simultanément (vs 4 DL seulement en WiFi 5)
           Idéal : bureaux denses, salles de réunion

BSS Coloring → réutilisation spatiale des canaux entre cellules proches
               Réduit les interférences sans changer de fréquence

TWT      → réveil programmé des appareils IoT → batterie ×10
           Réduit les interférences (moins d'appareils actifs en même temps)
```

---

## 🔄 Roaming — 802.11r/k/v

```
Sans fast roaming : 4-14 secondes → VoIP coupée

802.11r  Fast BSS Transition  : clés pré-partagées → handoff < 50ms
802.11k  Neighbor Reports     : liste APs voisins → scan réduit
802.11v  BSS Transition Mgmt  : WLC suggère migration → load balancing

Activés ensemble → roaming transparent pour VoIP
```

---

## 🎵 QoS WMM — 4 files de priorité

```
VO (Voice)      → VoIP, appels ← DSCP EF (46)
VI (Video)      → Streaming    ← DSCP AF41 (34)
BE (Best Effort)→ Web, email   ← DSCP CS0 (0)
BK (Background) → Sauvegardes  ← arrière-plan

EDCA : VO attend moins, BK attend plus
       → VoIP passe statistiquement avant les téléchargements

Config WLC : SSID → QoS → WMM Required
             Corp = Platinum (Voice) · IoT = Background
```

---

## 🔒 WPA3 — Avantages clés

```
WPA3-Personal (SAE) :
  Remplace WPA2-PSK 4-way handshake
  Perfect Forward Secrecy (PFS)
  Résistant aux attaques offline (brute force impossible sans tentatives live)

PMF (Protected Management Frames) :
  OBLIGATOIRE dans WPA3
  Protège les trames Deauth → fin des attaques par déauthentification

OWE (Opportunistic Wireless Encryption) :
  Chiffrement automatique sur réseaux OUVERTS (sans mot de passe)
  Transparent pour l'utilisateur · remplace "WPA2 ouvert"

WPA3-Enterprise :
  Même EAP (PEAP, EAP-TLS) que WPA2-Enterprise
  + Suite cryptographique 192 bits pour haute sécurité
```

---

## 🔍 Rogue AP

```
Rogue AP = AP non autorisé dans l'environnement radio
  Friendly   = AP connu mais non géré par ce WLC
  Malicious  = evil twin (copie le SSID) → DANGEREUX
  Unclassified = inconnu, à qualifier

Détection : AP en mode Monitor ou Rogue Detector (WLC)
Action possible : containment (envoi Deauth vers le Rogue AP)
```

---

## ✅ Comparatif rapide

```
WPA2-PSK   → mdp partagé, brute force offline possible ✗
WPA3 SAE   → PFS, brute force offline impossible ✓
WPA2 Ouvert → trafic en clair ✗
WPA3 OWE   → chiffrement auto sans mdp ✓
PMF Off    → Deauth flooding possible ✗
PMF On     → Trames gestion protégées ✓
AP Standalone → config manuelle x45 ✗
AP + WLC     → config centralisée ✓
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| CAPWAP UDP 6633 | UDP 5246 (ctrl) + 5247 (data) |
| WPA3 n'a pas besoin de PMF | PMF est OBLIGATOIRE dans WPA3 |
| OFDMA = plus de bande passante | OFDMA = plusieurs clients SIMULTANÉS |
| 802.11r seul suffit | Activer aussi 802.11k + 802.11v pour optimal |
| Isolation client = partout | Corp OFF (partage imprimantes) · Guest ON (sécurité) |

---

*Aide-Mémoire WiFi Avancé — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S8*
*Compétences S4.5 · S4.6 · S4.7 · S4.8 · S4.9*
