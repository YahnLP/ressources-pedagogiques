# 🔍 ACTIVITÉ DE DÉCOUVERTE — S8 · 3ᵉ ANNÉE · E31
## « L'hôpital sans fil » — Diagnostiquer une architecture WLAN enterprise

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement
> **Principe** : Analyser une architecture WLAN d'entreprise réelle et identifier les problèmes avant tout cours sur WiFi avancé.

---

## 🎯 Mise en situation

> **Hôpital Saint-Antoine** — 400 lits, 5 bâtiments, 1 200 appareils WiFi.
> Tu es consultant réseau. L'infirmière coordinatrice se plaint :
>
> **Problème 1** : *"Quand je me déplace avec ma tablette entre le bâtiment A et B,
> mes applications se déconnectent 10-15 secondes. C'est inacceptable pendant un transfert de dossier patient."*
>
> **Problème 2** : *"Les appels VoIP sur les téléphones WiFi sont souvent de mauvaise qualité.
> On entend des coupures. Surtout quand les infirmières font leur ronde."*
>
> **Problème 3** : *"Nous avons installé 200 capteurs IoT pour la surveillance des équipements.
> Depuis, le WiFi des tablettes est plus lent."*
>
> **Problème 4** : *"Un visiteur a installé son propre routeur WiFi dans sa chambre.
> Maintenant certains patients se connectent dessus sans le savoir."*

---

## 📋 Document 1 — Architecture actuelle de l'hôpital

```
BÂTIMENT A                 BÂTIMENT B                BÂTIMENT C
                                                      
[Salle serveurs]           [Infirmeries]              [Chambres patients]
  │                          │                           │
[Switch] ─────── [AP01] [AP02]   [AP03] [AP04]   [AP05] [AP06] [AP07]
  │
[Switch Core]

Chaque AP est autonome (standalone).
Chaque AP a sa propre configuration.
SSID "Hospital-Staff" : WPA2-PSK mdp "hospital2019" — tous les personnels
SSID "Hospital-IoT"   : pas de sécurité (ouvert)
SSID "Hospital-Guest" : portail captif (WEP — vieux AP)

Pas de contrôleur WiFi centralisé.
```

---

## 🔍 PARTIE 1 — Diagnostiquer les problèmes (15 min)

**Question 1.1 — Problème 1 (déconnexion lors des déplacements)**

```
Ce phénomène s'appelle le : __________________________________________________
Dans l'architecture actuelle (APs autonomes), pourquoi la reconnexion prend-elle 10-15s ?
___________________________________________________________________________
___________________________________________________________________________

Dans une architecture moderne avec contrôleur centralisé, ce délai serait de :
  ☐ identique ☐ < 1 seconde ☐ supprimé totalement

La norme WiFi qui permet le "Fast Roaming" s'appelle : _______________________
```

**Question 1.2 — Problème 2 (qualité VoIP)**

```
La VoIP est sensible à : ☐ la bande passante seule ☐ le délai et la gigue

Dans une architecture sans QoS WiFi :
  Un paquet VoIP et un paquet de téléchargement vidéo HD sont traités :
  ☐ le paquet VoIP en priorité (prioritaire)
  ☐ les deux de façon identique (FIFO)

Le mécanisme de priorité WiFi s'appelle : ___________________________________
Il définit 4 files d'attente pour : Voice · Video · Best Effort · Background

Pendant le roaming (déplacement d'une chambre à l'autre), la VoIP se coupe car :
___________________________________________________________________________
```

**Question 1.3 — Problème 3 (200 capteurs IoT ralentissent le WiFi)**

```
200 capteurs IoT qui transmettent régulièrement sur le MÊME canal WiFi créent :
  ☐ plus de bande passante disponible
  ☐ des collisions et des retransmissions → ralentissement général

La technologie WiFi 6 qui résout ce problème s'appelle : ______________________
Elle permet de : ____________________________________________________________

Le fait que le réseau IoT est OUVERT (pas de sécurité) est un risque :
  ☐ Oui → un attaquant peut injecter de faux relevés de capteurs
  ☐ Non → les capteurs n'ont pas de données sensibles
```

**Question 1.4 — Problème 4 (routeur non autorisé)**

```
Ce routeur installé par un visiteur s'appelle un : _____________________________
Son danger principal : _______________________________________________________

Une architecture avec contrôleur centralisé peut détecter ce type d'appareil
grâce à un mode AP appelé : __________________________________________________

La protection WPA3 aurait-elle empêché ce problème ?
  ☐ Oui, complètement ☐ Non — WPA3 protège l'authentification, pas l'apparition d'APs non autorisés
```

---

## 📋 Document 2 — Architecture cible proposée

```
BÂTIMENT A                BÂTIMENT B               BÂTIMENT C
                                                     
[Salle serveurs]                                     
  │  ┌──────────────────────────────────────┐       
  │  │     WLC (Wireless LAN Controller)    │       
  │  │  - Gestion centralisée de tous les APs│       
  │  │  - Politiques SSID/QoS/Sécurité      │       
  │  │  - Détection des APs non autorisés   │       
  │  └──────────────────────────────────────┘       
  │          │ CAPWAP (UDP 5246/5247)                
[Switch Core]│                                       
  │    ┌─────┴──────────────────────────────┐       
  │    │  APs Lightweight (WiFi 6)           │       
  │    │  AP01 AP02 AP03 AP04 AP05 AP06 AP07 │       
  │    │  (pas de config locale)             │       
  │    └────────────────────────────────────┘       
  │                                                  
  └── SSID "Staff-WiFi6" → WPA3-Enterprise + WMM Voice
      SSID "IoT-Secure"  → WPA2-PSK isolé + OFDMA + débit limité
      SSID "Patient-WiFi"→ WPA3-Personal (SAE) + portail captif
```

---

## 🔍 PARTIE 2 — Comprendre l'architecture cible (12 min)

**Question 2.1** — Dans l'architecture cible, les APs n'ont plus de configuration locale. Qui les configure ?

```
Les APs reçoivent leur configuration depuis : _________________________________
Le protocole qui transporte cette configuration s'appelle : ___________________
Sur quels ports UDP ? ________________________________________________________
```

**Question 2.2** — Compare les deux architectures pour chaque problème :

| Problème | Architecture actuelle | Architecture cible |
|---|---|---|
| Roaming lent (10-15s) | APs autonomes → réauthentification complète | |
| VoIP de mauvaise qualité | Pas de QoS → FIFO | |
| IoT ralentit le WiFi | Même canal non géré | |
| AP non autorisé non détecté | Pas de surveillance | |

**Question 2.3** — WPA3 remplace WPA2 pour le SSID Staff. Donne un avantage concret dans le contexte hospitalier :

```
Avec WPA2-PSK "hospital2019" : si un employé part ou si le mot de passe fuit → ________________
Avec WPA3 (SAE) : ______________________________________________________________
Avec WPA3-Enterprise : chaque soignant a ses propres credentials → _______________
```

**Question 2.4** — WiFi 6 vs WiFi 5 (802.11ac) — à partir des informations du Document 2, déduis 2 avantages de WiFi 6 pour un hôpital dense (1 200 appareils) :

```
Avantage 1 : __________________________________________________________________
Avantage 2 : __________________________________________________________________
```

---

## 🏁 Bilan

```
Les 3 composants clés d'une architecture WLAN enterprise moderne :
1. ________________________ → centralise toute la gestion
2. ________________________ → protocole entre WLC et APs
3. ________________________ → WiFi de nouvelle génération

La différence entre un AP "standalone" et un AP "lightweight" :
  Standalone : ________________________________________________________________
  Lightweight : _______________________________________________________________

WPA3 améliore principalement :
  → ___________________________________________________________________________
```

> ✅ Tu as identifié tous les problèmes et leurs solutions — le cours va maintenant
> t'expliquer chaque technologie en détail.

---

## 📎 Pour l'enseignant — Réponses

**1.1** : Roaming · Les APs autonomes ne partagent pas les clés de session → réauthentification complète · < 50ms avec 802.11r · 802.11r (Fast BSS Transition)

**1.2** : Délai ET gigue · FIFO · WMM (Wi-Fi Multimedia) · VoIP nécessite < 150ms et < 30ms de gigue — le roaming interrompt les paquets pendant la reconnexion

**1.3** : Collisions et retransmissions · OFDMA (Orthogonal Frequency Division Multiple Access) · Subdivise le canal en Resource Units, plusieurs clients transmettent simultanément

**1.4** : Rogue AP · Connexion MITM involontaire · Mode Monitor ou Rogue Detector

**2.2** : Cible — Roaming : 802.11r < 50ms · VoIP : WMM Voice priority · IoT : OFDMA + SSID isolé + débit limité · AP non autorisé : AP en mode Monitor → alerte WLC

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S8*
*Compétences : S4.5 · S4.6 · S4.7 · S4.8 · S4.9*
