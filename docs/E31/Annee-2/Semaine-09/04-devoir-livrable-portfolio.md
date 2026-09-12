# 📝 DEVOIR & LIVRABLE PORTFOLIO — S9 · 2ᵉ ANNÉE · E32
## WiFi Entreprise : 802.1X · RADIUS · EAP-TLS · Architecture WLAN

---

> **Module** : E32 – Cybersécurité et services réseau
> **Épreuve visée** : **E32** – Cybersécurité · **E31** (architecture)
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)
> **Format du rendu** : Fiche complétée + schéma d'architecture dessiné

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S4.1** | 802.1X — acteurs, flux, protocoles | /25 |
| **S4.2** | RADIUS — AAA, messages, configuration | /20 |
| **S4.3** | EAP-TLS vs PEAP — différences et choix | /20 |
| **S4.4** | PKI — certificats, CA, révocation | /15 |
| **S4.5 + C3.2** | Architecture WLAN sécurisée annotée | /20 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation professionnelle

> **Tu es technicien E32** missionné pour **sécuriser l'infrastructure WiFi** d'un hôtel de 200 chambres.
>
> L'hôtel dispose actuellement d'un seul WiFi en WPA2-PSK partagé entre :
> - Le personnel (réception, housekeeping, restauration)
> - Les clients (chambre + espaces communs)
>
> Le responsable IT t'a listé les problèmes actuels :
> 1. Un ex-employé s'est reconnecté après son départ et a accédé au réseau interne
> 2. Impossible de savoir qui utilise la bande passante
> 3. Un client a réussi à pinguer les serveurs de facturation internes
>
> **Ta mission** : proposer et documenter la nouvelle architecture.

---

## 🅰️ PARTIE A — En classe (45 min)

### 🔐 Exercice 1 — Les 3 acteurs de 802.1X (/25)

**1.a** — Dans le contexte de l'hôtel, associe chaque composant à son rôle 802.1X : *(9 pts)*

| Composant hôtel | Rôle 802.1X | Terme technique |
|---|---|---|
| Smartphone d'un employé | ☐ Supplicant ☐ Authenticator ☐ Auth. Server | |
| Borne WiFi du hall | ☐ Supplicant ☐ Authenticator ☐ Auth. Server | |
| Serveur FreeRADIUS en salle serveur | ☐ Supplicant ☐ Authenticator ☐ Auth. Server | |

**1.b** — Décris en 4 étapes ce qui se passe quand un employé tente de se connecter au WiFi professionnel (SSID "HotelStaff") : *(8 pts)*

```
Étape 1 : _____________________________________________________________________
Étape 2 : _____________________________________________________________________
Étape 3 : _____________________________________________________________________
Étape 4 : _____________________________________________________________________
```

**1.c** — Le RADIUS répond "Access-Reject" pour l'employé Marie. Cite 3 raisons possibles : *(6 pts)*

```
Raison 1 : ____________________________________________________________________
Raison 2 : ____________________________________________________________________
Raison 3 : ____________________________________________________________________
```

**1.d** — Quel protocole est utilisé entre la borne WiFi et le serveur RADIUS ? Sur quel port UDP ? *(2 pts)*

```
Protocole : _____________    Port authentification : _______    Port accounting : _______
```

---

### 📡 Exercice 2 — RADIUS et messages AAA (/20)

> Voici la séquence de messages RADIUS lors d'une connexion réussie.
> Quelques messages ont été mélangés.

**2.a** — Remets les messages dans le bon ordre en les numérotant de 1 à 6 : *(12 pts)*

| Ordre | Message RADIUS | Direction |
|---|---|---|
| | Access-Accept + attributs VLAN=10 | RADIUS → AP |
| | Access-Request (EAP-Response / Credentials) | AP → RADIUS |
| | EAPOL-Start | Laptop → AP |
| | EAP-Request / Identity | AP → Laptop |
| | Access-Challenge (EAP-Request / Credentials) | RADIUS → AP |
| | EAP-Success | AP → Laptop |

**2.b** — Dans l'Access-Accept, le RADIUS inclut 3 attributs pour assigner le VLAN.
Complète le tableau : *(6 pts)*

| Attribut RADIUS | Valeur | Rôle |
|---|---|---|
| Tunnel-Type | | |
| Tunnel-Medium-Type | | |
| Tunnel-Private-Group-ID | | |

**2.c** — Le secret partagé AP↔RADIUS est `HotelSecret2024`. Où doit-il être configuré ? *(2 pts)*

```
Sur l'AP : ___________________________________________________________________
Sur le RADIUS : ______________________________________________________________
Si les secrets ne correspondent pas : ________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/55)

### 🔒 Exercice 3 — EAP-TLS vs PEAP (/20)

> Le responsable IT hésite entre EAP-TLS et PEAP pour le WiFi du personnel.

**3.a** — Pour chaque affirmation, indique si elle s'applique à EAP-TLS, PEAP, ou aux deux : *(10 pts)*

| Affirmation | EAP-TLS | PEAP | Les deux |
|---|---|---|---|
| Un certificat serveur est requis | ☐ | ☐ | ☐ |
| Un certificat client est requis | ☐ | ☐ | ☐ |
| Les credentials transitent dans un tunnel TLS | ☐ | ☐ | ☐ |
| Une PKI complète (CA + certificats clients) est nécessaire | ☐ | ☐ | ☐ |
| Vulnérable si l'utilisateur accepte un faux certificat serveur | ☐ | ☐ | ☐ |

**3.b** — Décris le handshake EAP-TLS en 5 étapes : *(5 pts)*

```
Étape 1 : _____________________________________________________________________
Étape 2 : _____________________________________________________________________
Étape 3 : _____________________________________________________________________
Étape 4 : _____________________________________________________________________
Étape 5 : _____________________________________________________________________
```

**3.c** — Le responsable IT dit : *"On a 200 employés. Gérer 200 certificats clients c'est trop complexe."*
Quelle méthode EAP recommandes-tu et pourquoi ? *(5 pts)*

```
Recommandation : _______________________________________________________________
Justification : ________________________________________________________________
______________________________________________________________________________
Avantage sécuritaire conservé par rapport au PSK : ______________________________
```

---

### 🏗️ Exercice 4 — PKI et certificats (/15)

**4.a** — Un certificat X.509 contient plusieurs champs. Indique le rôle de chacun : *(10 pts)*

| Champ | Valeur exemple | Rôle |
|---|---|---|
| Subject | CN=marie, O=Hotel Riviera | |
| Issuer | CN=Hotel-CA | |
| Valid From/To | 01/01/2025 - 01/01/2026 | |
| Public Key | RSA 2048 | |
| Signature | (données cryptographiques) | |

**4.b** — Marie quitte l'hôtel le 15 mars. Son certificat est valide jusqu'au 01/01/2026. Que doit faire l'administrateur pour l'empêcher de se connecter ? Décris le mécanisme. *(5 pts)*

```
Action immédiate : _____________________________________________________________
Mécanisme technique : __________________________________________________________
Nom de la liste consultée par le serveur RADIUS : _______________________________
Comment le serveur RADIUS utilise-t-il cette liste lors d'une connexion ? ________
______________________________________________________________________________
```

---

### 🏨 Exercice 5 — Architecture WLAN sécurisée de l'hôtel (/20)

> Conçois l'architecture WiFi complète pour l'hôtel en répondant d'abord aux questions,
> puis en dessinant le schéma.

**5.a** — Combien de SSID distincts préconises-tu ? Justifie chaque SSID et son VLAN associé : *(6 pts)*

```
SSID 1 : Nom = "______________"  Type auth = ____________  VLAN = ____
  Utilisateurs : _______________  Accès autorisé : ___________________________

SSID 2 : Nom = "______________"  Type auth = ____________  VLAN = ____
  Utilisateurs : _______________  Accès autorisé : ___________________________

SSID 3 (optionnel) : Nom = "_______________"  Type auth = _____  VLAN = ____
  Utilisateurs : _______________  Accès autorisé : ___________________________
```

**5.b** — Quels serveurs faut-il déployer pour cette architecture ? *(6 pts)*

```
Serveur 1 : ___________________  Rôle : ______________________________________
Serveur 2 : ___________________  Rôle : ______________________________________
Serveur 3 (si EAP-TLS) : ______  Rôle : ______________________________________
```

**5.c** — Dessine le schéma d'architecture complet de l'hôtel, annoté avec : *(8 pts)*
- Les équipements (AP, WLC, RADIUS, pare-feu)
- Les VLANs avec leurs plages IP
- Les protocoles sur chaque lien (EAPOL / RADIUS)
- Les zones d'accès (Internet seul vs réseau interne)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏅 Barème global et grille Qualiopi

| Exercice | Compétences RNCP | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Acteurs 802.1X, flux, protocoles | S4.1 | /25 | ≥ 14 |
| Ex. 2 — RADIUS messages et VLAN | S4.2 | /20 | ≥ 11 |
| Ex. 3 — EAP-TLS vs PEAP | S4.3 | /20 | ≥ 11 |
| Ex. 4 — PKI, certificats, révocation | S4.4 | /15 | ≥ 8 |
| Ex. 5 — Architecture WLAN annotée | S4.5 + C3.2 | /20 | ≥ 11 |
| **TOTAL** | | **/100** | **≥ 55** |

> 📌 **Note Qualiopi** : Ce devoir constitue une preuve d'acquisition des compétences **S4.1 à S4.5, C3.2** pour le dossier **E32**. Conserver avec signature enseignant et date.

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** :
- Smartphone employé → Supplicant
- Borne WiFi du hall → Authenticator
- Serveur FreeRADIUS → Authentication Server

**1.b** :
1. L'employé active le WiFi → son smartphone envoie EAPOL-Start à la borne
2. La borne demande l'identité (EAP-Request/Identity)
3. Le smartphone répond (marie@hotel.fr) → la borne relaie vers RADIUS (Access-Request)
4. RADIUS vérifie les credentials → Access-Accept → borne ouvre le port → EAP-Success

**1.c** :
1. Compte désactivé ou inexistant dans la base RADIUS
2. Mot de passe incorrect
3. Certificat expiré ou révoqué (si EAP-TLS)

**1.d** : RADIUS · port 1812 (auth) · port 1813 (accounting)

## Correction Exercice 2

**2.a** Ordre correct :
1. EAPOL-Start (Laptop → AP)
2. EAP-Request/Identity (AP → Laptop)
3. Access-Challenge (RADIUS → AP)
4. EAP-Request/Credentials (retransmis AP → Laptop)
5. Access-Request credentials (AP → RADIUS)
6. Access-Accept + VLAN (RADIUS → AP)
7. EAP-Success (AP → Laptop)

**2.b** :
- Tunnel-Type = VLAN → indique le type de tunnel (41 = VLAN)
- Tunnel-Medium-Type = 802 → medium Ethernet/IEEE 802
- Tunnel-Private-Group-ID = "10" → numéro du VLAN à assigner

**2.c** : Configuré sur l'AP (dans la config RADIUS client) ET sur le serveur RADIUS (dans la liste des NAS clients) → Si ne correspond pas : le serveur rejette silencieusement les Access-Request

## Correction Exercice 3

**3.a** :
- Certificat serveur requis : Les deux
- Certificat client requis : EAP-TLS uniquement
- Credentials dans tunnel TLS : Les deux
- PKI complète : EAP-TLS uniquement
- Vulnérable faux cert. serveur : PEAP (si validation désactivée côté client)

**3.b** Handshake EAP-TLS :
1. Client envoie ClientHello (version TLS, aléatoire)
2. Serveur envoie ServerHello + son certificat X.509
3. Client vérifie le certificat serveur auprès de la CA de confiance
4. Client envoie son propre certificat X.509
5. Serveur vérifie le certificat client (validité, CA, CRL) → authentification mutuelle réussie → session TLS établie

**3.c** : Recommander PEAP · Justification : seul le serveur RADIUS a besoin d'un certificat → 1 seul certificat à gérer au lieu de 200 · L'utilisateur s'authentifie avec login/mdp dans le tunnel TLS chiffré · Avantage vs PSK : traçabilité individuelle, révocation par compte, résistance aux attaques de capture réseau

## Correction Exercice 4

**4.a** :
- Subject : identité du titulaire
- Issuer : autorité qui a signé et délivré
- Valid From/To : période pendant laquelle le certificat est valide
- Public Key : clé publique du titulaire (utilisée pour chiffrement/vérification)
- Signature : preuve d'authenticité par la CA (impossible à falsifier sans la clé privée CA)

**4.b** : Ajouter le numéro de série du certificat de Marie à la **CRL** (Certificate Revocation List) · Le serveur RADIUS consulte la CRL à chaque Access-Request · Si le serial number est dans la CRL → Access-Reject, même si le certificat n'est pas encore expiré

## Correction Exercice 5

**5.a** Architecture 3 SSID recommandée :
- "HotelStaff" → WPA2-Enterprise (PEAP) → VLAN 10 (192.168.10.0/24) → accès réseau interne + Internet
- "HotelGuest" → WPA2-PSK ou portail captif → VLAN 20 (192.168.20.0/24) → Internet seulement, pas de réseau interne
- "HotelMgmt" (optionnel) → WPA2-Enterprise (EAP-TLS) → VLAN 100 (192.168.100.0/24) → IT/Admin seulement

**5.b** :
- RADIUS Server (ex: FreeRADIUS) : centralise l'authentification
- Active Directory / LDAP : base des comptes employés
- CA Server (si EAP-TLS) : délivre et gère les certificats

**Architecture schéma** : éléments attendus — pare-feu séparant Internet de l'interne · WLC gérant tous les APs · RADIUS dans VLAN 100 · Deux zones nettes (zone interne = VLAN 10+100 / zone isolée = VLAN 20) · Protocoles annotés

---

*Devoir & Livrable Portfolio + Correction — Ne pas distribuer avant le rendu*
*BAC PRO CIEL | E32 Cybersécurité | 2ᵉ année S9*
*Épreuve E32 | Compétences S4.1 · S4.2 · S4.3 · S4.4 · S4.5 · C3.2*
*Conforme référentiel Qualiopi*
