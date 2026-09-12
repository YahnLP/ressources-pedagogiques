# 🔬 TRAVAUX PRATIQUES — S9 · 2ᵉ ANNÉE · E32
## WiFi Entreprise : Configurer et tester une architecture WLAN 802.1X / RADIUS

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Packet Tracer**
> **Fichier .pkt** : `S9_E32_WLAN_802.1X.pkt` (fourni par l'enseignant)
> **Épreuve ciblée** : **E32** – Cybersécurité et services réseau

---

## 📌 Compétences travaillées

| Code | Compétence | Niveau attendu |
|---|---|---|
| **S4.1** | Protocole 802.1X — 3 acteurs | Identifier les rôles sur la topologie PT |
| **S4.2** | RADIUS — flux AAA | Configurer le serveur et vérifier les logs |
| **S4.3** | EAP / PEAP | Configurer le client avec PEAP |
| **S4.5** | Architecture WLAN sécurisée | Compléter le schéma annoté |
| **C2.2** | Configurer les équipements | AP + serveur RADIUS + clients |
| **C2.3** | Diagnostiquer | Interpréter les refus d'authentification |

---

## 🗺️ Topologie du TP

```
                         VLAN 10 — Corp  (192.168.10.0/24)
  [Laptop_Alice]─────┐
  [Laptop_Bob]───────┤
                     │
               [AP_Corp] ─────────────── [SW_Core] ──────── [RADIUS_Server]
                     │    VLAN trunk           │             192.168.100.10
  [Laptop_Intrus]────┘                         │
                                               ├──────────── [DHCP_Server]
                         VLAN 20 — Guest        │             192.168.100.20
  [Laptop_Invité]────[AP_Guest]────────────────┤
                                               │
                                          [R_Gateway]
                                               │
                                          [Internet]

Serveur RADIUS :  192.168.100.10
AP Corp SSID :    "Corp-Secure"  → WPA2-Enterprise → VLAN 10
AP Guest SSID :   "Guest-Free"   → WPA2-PSK        → VLAN 20
```

---

## 🟢 NIVEAU 1 — Observer l'architecture (10 min)

> **Sans rien configurer**, explore la topologie Packet Tracer et réponds aux questions.

**Question 1.1** — Identifie chaque équipement de la topologie et son rôle 802.1X :

| Équipement | Rôle dans 802.1X | Adresse IP |
|---|---|---|
| Laptop_Alice | | |
| AP_Corp | | |
| RADIUS_Server | | |
| Laptop_Invité | | |
| AP_Guest | | |

**Question 1.2** — Ouvre le RADIUS_Server → onglet Services → AAA. Note les utilisateurs pré-configurés :

```
Utilisateur 1 : ________________  Mot de passe : ________________
Utilisateur 2 : ________________  Mot de passe : ________________
```

**Question 1.3** — Sans aucune configuration QoS ou 802.1X, Laptop_Alice peut-il pinguer le RADIUS_Server ?

```
Commande : ping _______________
Résultat : ☐ Succès !!!! ☐ Timeout ....
Explication : _______________________________________________________________
```

---

## 🟡 NIVEAU 2 — Configurer le serveur RADIUS (15 min)

> Le serveur RADIUS doit connaître les APs qui sont autorisés à lui envoyer des requêtes (clients NAS).

**2.1** — Sur le RADIUS_Server, onglet Services → AAA, configure les paramètres suivants :

```
Network Configuration (Clients RADIUS) :
  Client Name  : AP_Corp
  Client IP    : [adresse IP de AP_Corp dans la topologie]
  Secret Key   : CiscoRADIUS123

  ← Clique "Add" pour valider
```

Note l'adresse IP de AP_Corp : ___________________________

**2.2** — Vérifie que les comptes utilisateurs sont bien créés (onglet User Setup) :

```
☐ alice / Alice2024!  présent
☐ bob   / Bob2024!    présent
☐ intrus / ???        ☐ présent ☐ absent (normal — il ne doit pas exister)
```

**2.3** — Ajoute un 3ème utilisateur pour le test de refus :

```
Username : charlie
Password : Charlie2024!
← Clique "Add"
```

---

## 🟠 NIVEAU 3 — Configurer le point d'accès AP_Corp (20 min)

**3.1** — Clique sur AP_Corp → onglet Config → Interface → Port 1 (Gi1/0)

Configure le SSID WPA2-Enterprise :

```
SSID Name    : Corp-Secure
Authentication : WPA2-Enterprise (802.1X)
RADIUS Server IP      : 192.168.100.10
RADIUS Server Secret  : CiscoRADIUS123
RADIUS Server Port    : 1812
```

**3.2** — Vérifie l'association du SSID au VLAN 10 :

```
VLAN associé à Corp-Secure : VLAN _______
(Vérifier dans la config trunk du SW_Core)
```

**3.3** — Laisse l'AP_Guest configuré en WPA2-PSK (mot de passe : Guest1234) — c'est déjà fait dans le fichier.

---

## 🔵 NIVEAU 4 — Configurer les clients et tester (25 min)

### Connexion de Laptop_Alice (succès attendu)

**4.1** — Clique sur Laptop_Alice → onglet Desktop → PC Wireless :

```
Chercher le SSID "Corp-Secure"
Authentication : WPA2-Enterprise
EAP Method     : PEAP
Username       : alice
Password       : Alice2024!
← Connect
```

**4.2** — Note le résultat :

```
☐ Connexion réussie — Alice a obtenu l'adresse IP : ____________________
☐ Connexion échouée — message : _____________________________________
```

**4.3** — Teste la connectivité d'Alice :

```
PC Wireless → Command Prompt
ping 192.168.10.1 (gateway VLAN 10) → ☐ OK ☐ Échec
ping 192.168.100.10 (RADIUS) → ☐ OK ☐ Échec (accès VLAN 100 ?)
ping 8.8.8.8 (Internet) → ☐ OK ☐ Échec
```

### Connexion de Laptop_Bob (succès attendu)

**4.4** — Même procédure avec bob / Bob2024! → note le résultat :

```
Connexion : ☐ Réussie (IP : _______________) ☐ Échouée
Bob et Alice sont-ils dans le même VLAN ? ☐ Oui VLAN ______ ☐ Non
```

### Tentative de Laptop_Intrus (refus attendu)

**4.5** — Sur Laptop_Intrus, tente de te connecter à "Corp-Secure" avec :

```
Username : intrus
Password : n'importe quoi
```

Résultat :

```
☐ Connexion refusée ✗ — comme attendu
☐ Connexion réussie (problème de config — appeler l'enseignant)

Message d'erreur affiché : _________________________________________________
```

**4.6** — Sur le RADIUS_Server, vérifie les logs AAA (onglet Services → AAA → Log) :

```
Entrée pour alice  : ☐ Accept ☐ Reject
Entrée pour bob    : ☐ Accept ☐ Reject
Entrée pour intrus : ☐ Accept ☐ Reject
```

### Révocation de charlie

**4.7** — Connecte charlie (Charlie2024!) → vérifie qu'il accède au réseau → puis **supprime son compte du RADIUS** → réessaie de connecter charlie :

```
Avant suppression : charlie peut se connecter ? ☐ Oui ☐ Non
Après suppression du compte RADIUS : charlie peut se connecter ? ☐ Oui ☐ Non
Délai entre la suppression et le refus : ☐ Immédiat ☐ Quelques secondes
Conclusion sur la révocation individuelle : _____________________________________
```

---

## 🔴 NIVEAU 5 — Analyser et documenter l'architecture (10 min)

**5.1** — Complète le schéma d'architecture annoté :

```
Dans l'espace ci-dessous, dessine l'architecture complète avec :
  - Les 3 acteurs 802.1X légendés (supplicant, authenticator, serveur)
  - Le protocole utilisé entre chaque paire (EAPOL / RADIUS)
  - Les VLANs (10 Corp, 20 Guest, 100 Mgmt) avec leurs plages IP
  - Les flux de trafic autorisé (flèches vertes)
  - Le flux 802.1X (flèches pointillées)

┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**5.2** — Réponds aux questions de synthèse :

```
Pourquoi AP_Guest n'utilise-t-il pas 802.1X ?
______________________________________________________________________________

Quel protocole transporte EAP entre Laptop_Alice et AP_Corp ?
______________________________________________________________________________

Si le RADIUS_Server tombe en panne, que se passe-t-il pour les nouvelles connexions Corp ?
______________________________________________________________________________

Comment améliorer la résilience ? (solution en 1 ligne)
______________________________________________________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Identifier les 3 acteurs 802.1X | ☐ | ☐ | ☐ |
| Configurer le serveur RADIUS (clients NAS + comptes) | ☐ | ☐ | ☐ |
| Configurer un AP en WPA2-Enterprise | ☐ | ☐ | ☐ |
| Configurer un client PEAP | ☐ | ☐ | ☐ |
| Vérifier l'authentification dans les logs RADIUS | ☐ | ☐ | ☐ |
| Révoquer un utilisateur et observer l'effet immédiat | ☐ | ☐ | ☐ |
| Dessiner le schéma d'architecture annoté | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.1 — Architecture comprise, rôles identifiés | /4 |
| Niv.2 — RADIUS configuré (client NAS + comptes) | /4 |
| Niv.3 — AP configuré en WPA2-Enterprise | /4 |
| Niv.4 — Tests connexion/refus/révocation probants | /8 |
| Niv.5 — Schéma d'architecture annoté et réponses | /5 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 1

**1.1** :
- Laptop_Alice : supplicant
- AP_Corp : authenticator
- RADIUS_Server : serveur d'authentification
- Laptop_Invité : supplicant réseau guest
- AP_Guest : authenticator réseau guest (WPA2-PSK, pas 802.1X)

**1.3** : Avant config → Alice devrait pouvoir pinguer si le réseau L3 est configuré, mais elle n'a pas encore de profil WiFi → pas d'association

## Correction Niveau 4

**4.6 logs** :
- alice → Access-Accept (compte valide)
- bob → Access-Accept
- intrus → Access-Reject (compte inexistant)

**4.7 révocation** : La révocation est effective dès que le compte est supprimé → les nouvelles tentatives de connexion sont refusées immédiatement. Les sessions déjà établies peuvent rester jusqu'à l'expiration du bail (selon la config du reauthentication timer sur l'AP).

## Correction Niveau 5

**5.2** :
- AP_Guest n'utilise pas 802.1X car c'est un réseau invité : pas de serveur d'authentification pour les visiteurs, accès simple par PSK
- EAPOL (EAP over LAN) entre Laptop_Alice et AP_Corp
- Si RADIUS tombe → les nouvelles connexions sont refusées (AP ne peut plus vérifier) → Service interrompu
- Solution : RADIUS secondaire (RADIUS redondant / failover) ou Active-Standby RADIUS pair

---

*TP WLAN 802.1X + Correction — BAC PRO CIEL | E32 Cybersécurité | 2ᵉ année S9*
*Document Portfolio E32 — Compétences S4.1 · S4.2 · S4.3 · S4.5 · C2.2 · C2.3*
