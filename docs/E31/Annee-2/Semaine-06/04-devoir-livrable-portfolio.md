# 📝 DEVOIR & LIVRABLE PORTFOLIO — S6 · 2ᵉ ANNÉE · E31
## QoS : DSCP · Files d'attente · Priorisation VoIP · Configuration MQC

---

> **Module** : E31 – Infrastructure Réseau · QoS
> **Épreuve visée** : **E31** – Infrastructure réseau · **E32** – Exploitation
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)
> **Format du rendu** : Fiche complétée, commandes IOS écrites avec soin

---

## 📌 Compétences du référentiel évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S3.1** | Comprendre la nécessité de la QoS, contraintes VoIP | /20 |
| **S3.2** | DSCP : valeurs, marquage, trust boundary | /20 |
| **S3.3** | Files d'attente, LLQ, configuration MQC | /35 |
| **C2.3** | Analyser une policy-map, diagnostiquer | /15 |
| **C3.1** | Rédiger une recommandation technique | /10 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation professionnelle

> Tu es **technicien CIEL** en charge du réseau d'une entreprise de 50 personnes.
>
> L'entreprise vient de déployer la **téléphonie IP (VoIP)** sur son infrastructure existante.
> Le DSI reçoit des plaintes : les appels téléphoniques sont de mauvaise qualité aux heures de pointe.
>
> **Ta mission** :
> 1. Analyser les contraintes et identifier le problème
> 2. Proposer et configurer une politique QoS
> 3. Valider et documenter la solution

---

## 🅰️ PARTIE A — En classe (45 min)

### 📡 Exercice 1 — Contraintes du trafic temps-réel (/20)

> L'infrastructure réseau dispose d'un lien WAN de **2 Mbps** entre le siège et l'agence.
> Pendant les heures de pointe, les flux suivants coexistent :

| Flux | Protocole | Débit mesuré |
|---|---|---|
| 4 appels VoIP G.711 | RTP/UDP, DSCP EF | 4 × 80 kbps = 320 kbps |
| Visioconférence RH | RTP/UDP, DSCP AF41 | 1 500 kbps |
| Navigation web | TCP/HTTP, DSCP BE | 300 kbps |
| Backup nocturne lancé manuellement | TCP/FTP, DSCP BE | 600 kbps |
| **TOTAL** | | **2 720 kbps** |

**1.a** — Le lien WAN est-il en congestion ? Calcule le déficit. *(3 pts)*

```
Capacité du lien : _______ kbps
Total demandé : _______ kbps
Déficit : _______ − _______ = _______ kbps → congestion : ☐ Oui ☐ Non
```

**1.b** — Parmi les 4 flux, classe-les par ordre de priorité décroissante et justifie. *(8 pts)*

```
Priorité 1 : _____________________________ car _______________________________
Priorité 2 : _____________________________ car _______________________________
Priorité 3 : _____________________________ car _______________________________
Priorité 4 : _____________________________ car _______________________________
```

**1.c** — La VoIP G.711 a une tolérance de latence de 150 ms maximum. Si un paquet VoIP doit attendre derrière le backup FTP (600 kbps) avant d'être envoyé sur le lien 2 Mbps, quelle latence d'attente maximale peut-il subir ? *(5 pts)*

```
Taille d'un paquet FTP typique : ~1 500 octets = 12 000 bits
Temps de transmission sur 2 Mbps : 12 000 / 2 000 000 = _______ ms
Ce délai est-il acceptable pour la VoIP ? ☐ Oui (< 150 ms) ☐ Non
Cela explique pourquoi les paquets voix ne doivent PAS attendre derrière : ______
```

**1.d** — Explique en 3 lignes la différence entre la gigue (jitter) et la latence. Donne un exemple concret de l'effet de chacun sur une conversation téléphonique. *(4 pts)*

```
Latence = __________________________________________________________________
Effet : ____________________________________________________________________
Gigue = ____________________________________________________________________
Effet : ____________________________________________________________________
```

---

### 🏷️ Exercice 2 — DSCP et marquage (/20)

**2.a** — Pour chaque trafic du tableau, indique la classe DSCP appropriée et sa valeur décimale. *(10 pts)*

| Trafic | Classe DSCP recommandée | Valeur décimale |
|---|---|---|
| Voix RTP (appel téléphonique) | | |
| Signalisation SIP | | |
| Vidéoconférence | | |
| Données transactionnelles critiques (ERP) | | |
| Navigation web standard | | |

**2.b** — Un PC d'un employé malveillant envoie du trafic HTTP en marquant ses paquets DSCP EF (46) pour obtenir la priorité voix. Comment le réseau doit-il gérer cette situation ? *(5 pts)*

```
Mécanisme de protection : ___________________________________________________
Rôle du concept "Trust Boundary" : _________________________________________
Emplacement typique de la Trust Boundary : __________________________________
Action sur les paquets du PC : ______________________________________________
```

**2.c** — Dans quel champ de l'en-tête IP se trouve le marquage DSCP ? Combien de valeurs possibles ce champ offre-t-il ? *(5 pts)*

```
Champ IP concerné : _______________________
Taille en bits : _______ bits → _______ valeurs possibles (0 à _______)
Valeur 0 = classe _______ = trafic _______________
Valeur 46 = classe _______ = trafic _______________
```

---

## 🅱️ PARTIE B — En autonomie (/45)

### ⌨️ Exercice 3 — Lire et corriger une policy-map existante (/20)

> Le technicien précédent a configuré la policy-map suivante. Elle contient **3 erreurs**.

```cisco
! Configuration existante sur R_WAN :

class-map match-any VOIX
 match dscp 0
  
class-map match-any DONNEES
 match dscp af31

policy-map QOS_SITE
 class VOIX
  bandwidth 256
 class DONNEES
  priority percent 40
 class class-default
  fair-queue

interface GigabitEthernet0/0
 service-policy input QOS_SITE
```

**3.a** — Identifie et explique les 3 erreurs : *(12 pts — 4 pts par erreur)*

```
ERREUR 1 :
  Localisation : ______________________________________________________________
  Nature : ___________________________________________________________________
  Impact : ___________________________________________________________________
  Correction : _______________________________________________________________

ERREUR 2 :
  Localisation : ______________________________________________________________
  Nature : ___________________________________________________________________
  Impact : ___________________________________________________________________
  Correction : _______________________________________________________________

ERREUR 3 :
  Localisation : ______________________________________________________________
  Nature : ___________________________________________________________________
  Impact : ___________________________________________________________________
  Correction : _______________________________________________________________
```

**3.b** — Réécris la configuration complète et corrigée : *(8 pts)*

```cisco
class-map match-any VOIX
 match dscp _____________

class-map match-any DONNEES
 match dscp _____________

policy-map QOS_SITE
 class VOIX
  _____________ 256
 class DONNEES
  bandwidth _____________
 class class-default
  fair-queue

interface Serial0/0/0
 service-policy _____________ QOS_SITE
```

---

### 📐 Exercice 4 — Dimensionnement VoIP (/15)

> L'entreprise prévoit d'ouvrir **2 nouvelles agences** reliées au siège par des liens WAN.
> Tu dois dimensionner la bande passante voix pour chaque lien.

**Données :**
- Codec VoIP utilisé : G.729 (8 kbps) + overhead IP/UDP/RTP ≈ **24 kbps par appel**
- Codec de secours : G.711 (64 kbps) + overhead ≈ **80 kbps par appel**
- Règle de déploiement : réserver **max 33 %** du lien WAN à la voix (laisser 67 % aux données)

**4.a** — Agence Nord : lien WAN 512 kbps · 8 appels simultanés prévus avec G.729 *(5 pts)*

```
Bande passante voix nécessaire (G.729) : 8 × _______ = _______ kbps
33 % du lien 512 kbps = _______ kbps
_______ kbps ≤ _______ kbps → la voix tient sur ce lien ? ☐ Oui ☐ Non
Commande IOS : policy-map QOS-AGENCE-NORD → class VOIX → priority _______
```

**4.b** — Agence Sud : lien WAN 1 Mbps · 15 appels simultanés prévus avec G.711 *(5 pts)*

```
Bande passante voix nécessaire (G.711) : 15 × _______ = _______ kbps
33 % du lien 1 000 kbps = _______ kbps
_______ kbps ≤ _______ kbps → la voix tient sur ce lien ? ☐ Oui ☐ Non
Si non : nombre maximum d'appels G.711 sur ce lien = _______ / 80 = _______ appels
Recommandation : _____________________________________________________________
```

**4.c** — Pour l'Agence Sud avec trop d'appels, proposes 2 solutions techniques : *(5 pts)*

```
Solution 1 : ________________________________________________________________
  Avantage : __________________________________________________________________
  Inconvénient : ______________________________________________________________

Solution 2 : ________________________________________________________________
  Avantage : __________________________________________________________________
  Inconvénient : ______________________________________________________________
```

---

### 📝 Exercice 5 — Note de recommandation (/10)

> Le DSI te demande une note technique concise pour justifier la mise en place de la QoS.
> Elle doit répondre en 10-12 lignes à :
> *"Pourquoi la QoS est-elle indispensable pour notre déploiement VoIP ? Quelle architecture technique recommandez-vous et quelles sont ses limites ?"*

```
Note technique :

___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

---

## 🏅 Barème global et grille Qualiopi

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Contraintes temps-réel, congestion | S3.1 | /20 | ≥ 11/20 |
| Ex. 2 — DSCP, marquage, trust boundary | S3.2 | /20 | ≥ 11/20 |
| Ex. 3 — Analyser et corriger une policy-map | S3.3 · C2.3 | /20 | ≥ 11/20 |
| Ex. 4 — Dimensionnement VoIP | S3.3 · C2.2 | /15 | ≥ 8/15 |
| Ex. 5 — Note de recommandation DSI | C3.1 | /10 | ≥ 5/10 |
| Forme et présentation | | /15 | |
| **TOTAL** | | **/100** | **≥ 55/100** |

> 📌 **Note Qualiopi** : Ce devoir constitue une preuve d'acquisition QoS pour **E31/E32**. Conserver avec signature enseignant et date.

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

---

## Correction Exercice 1

**1.a** : 2 720 − 2 000 = **720 kbps** de déficit → congestion

**1.b** :
1. VoIP G.711 — temps-réel, inélastique, ne peut pas attendre
2. Visioconférence — temps-réel, important mais peut tolérer plus de perte
3. Navigation web — élastique, TCP s'adapte, utilisateur attend quelques ms
4. Backup FTP — bulk, peut être planifié de nuit, aucune contrainte temps-réel

**1.c** : 12 000 / 2 000 000 = **6 ms** → acceptable (< 150 ms) MAIS si plusieurs gros paquets FTP s'accumulent : 10 paquets × 6 ms = 60 ms — les paquets voix ne doivent pas attendre derrière une file de paquets FTP

**1.d** : Latence = délai total de bout en bout → effet : écho gênant si > 300 ms, sensation de délai dans la conversation. Gigue = variation de ce délai → effet : robotisation, saccades, artefacts sonores

---

## Correction Exercice 2

**2.a** :

| Trafic | Classe DSCP | Valeur |
|---|---|---|
| Voix RTP | EF (Expedited Forwarding) | **46** |
| Signalisation SIP | CS3 | **24** |
| Vidéoconférence | AF41 | **34** |
| Données ERP | AF31 | **26** |
| Navigation web | BE (Best Effort) | **0** |

**2.b** : Trust Boundary = frontière de confiance sur les switchs d'accès. Les téléphones IP sont en mode "trust dscp", les ports des PC sont en mode "set dscp 0" (tout PC = BE, quelle que soit la demande). Cela empêche un utilisateur de forger des marquages DSCP EF.

**2.c** : Champ ToS/DS dans l'en-tête IP · 6 bits DSCP → 64 valeurs (0 à 63) · 0=BE · 46=EF

---

## Correction Exercice 3

**3 erreurs :**

1. `match dscp 0` dans class-map VOIX → **ERREUR : 0 = BE (Best Effort)** → la VoIP se retrouve dans la file ordinaire. Correction : `match dscp ef`

2. `priority percent 40` dans class DONNEES → **ERREUR : `priority` est réservé à LLQ (voix)**. `priority percent` n'existe pas de façon standard; de plus priority doit être la voix, pas les données. Correction : `bandwidth percent 40`

3. `service-policy input` → **ERREUR : la QoS s'applique en `output`** sur l'interface de congestion. De plus, GigabitEthernet est le LAN (pas le lien congestionnable). Correction : `interface Serial0/0/0` + `service-policy output`

**Configuration corrigée :**
```cisco
class-map match-any VOIX
 match dscp ef          ! EF = 46
class-map match-any DONNEES
 match dscp af31
policy-map QOS_SITE
 class VOIX
  priority 256          ! LLQ pour la voix
 class DONNEES
  bandwidth percent 40  ! 40 % de la BW restante
 class class-default
  fair-queue
interface Serial0/0/0
 service-policy output QOS_SITE   ! output sur lien WAN
```

---

## Correction Exercice 4

**4.a** : 8 × 24 = **192 kbps** · 33 % × 512 = **169 kbps** · 192 > 169 → **Non, ne tient pas** → Réduire à 7 appels max (7 × 24 = 168 kbps ≤ 169) ou upgrader le lien

**4.b** : 15 × 80 = **1 200 kbps** · 33 % × 1 000 = **330 kbps** · 1 200 > 330 → **Non** · Appels max = 330 / 80 = **4 appels** seulement

**4.c** :
1. Passer au codec G.729 (24 kbps) → 330 / 24 = 13 appels possibles (mieux) · Avantage : pas de coût d'infrastructure · Inconvénient : légère dégradation qualité audio vs G.711
2. Upgrader le lien à 2 Mbps → 33 % × 2000 = 660 kbps → 8 appels G.711 · Avantage : qualité maximale · Inconvénient : coût mensuel lien WAN

---

## Éléments attendus Note de recommandation

- VoIP = trafic temps-réel, inélastique (UDP, pas de retransmission) → sensible à latence, gigue, perte
- Sur réseau convergent sans QoS : la voix et les données se battent pour la même bande passante → dégradation aux heures de pointe
- Architecture recommandée : LLQ (Low Latency Queuing) + MQC Cisco — class-map → policy-map → service-policy output sur lien WAN
- Classes : EF=46 voix, CS3=24 signalisation, AF31 données critiques, BE=0 reste
- Trust boundary sur switchs d'accès : les PC ne peuvent pas forger du DSCP EF
- Limite : la QoS ne crée pas de bande passante — si lien saturé à 100 %, il faut upgrader. Nombre d'appels G.711 simultanés = BW_priority / 80 kbps

---

*Devoir & Livrable Portfolio + Correction — Ne pas distribuer avant le rendu*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S6*
*Épreuves E31 · E32 | Compétences S3.1 · S3.2 · S3.3 · C2.2 · C2.3 · C3.1*
*Conforme référentiel Qualiopi*
