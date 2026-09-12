# 📘 FICHE DE COURS — S6 · 2ᵉ ANNÉE · E31
## QoS : Marquage DSCP · Files d'attente · Priorisation VoIP · Configuration MQC

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences travaillées** : S3.1 · S3.2 · S3.3 · C2.2 · C2.3

---

## 🔑 Vocabulaire clé à maîtriser

| Terme | Définition |
|---|---|
| **QoS** | Quality of Service — ensemble de mécanismes permettant de garantir des niveaux de service différenciés selon le type de trafic |
| **Congestion** | Situation où le débit demandé dépasse la capacité du lien — file d'attente se remplit |
| **Latence** | Délai de bout en bout d'un paquet — critique pour la VoIP (< 150 ms) |
| **Gigue (Jitter)** | Variation des délais d'arrivée entre paquets consécutifs — cause de robotisation VoIP |
| **ToS / DSCP** | Type of Service / Differentiated Services Code Point — champ de l'en-tête IP pour marquer la priorité |
| **DSCP EF** | Expedited Forwarding — DSCP 46 — réservé au trafic voix temps-réel |
| **DSCP AF** | Assured Forwarding — garantie de transmission selon la classe (AF11 à AF43) |
| **DSCP BE** | Best Effort — DSCP 0 — trafic ordinaire, aucune garantie |
| **File d'attente** | Buffer où les paquets attendent d'être transmis — l'ordre de traitement détermine la priorité |
| **LLQ** | Low Latency Queuing — file d'attente à priorité stricte pour la voix, garantie absolue |
| **WFQ** | Weighted Fair Queuing — partage équitable pondéré de la bande passante restante |
| **CBWFQ** | Class-Based WFQ — WFQ avec des classes définies par l'administrateur |
| **MQC** | Modular QoS CLI — framework Cisco pour configurer la QoS en 3 étapes : class-map → policy-map → service-policy |
| **Marking** | Marquage — action de modifier le champ DSCP d'un paquet à l'entrée du réseau |
| **Policing** | Limiter le débit d'un flux au-delà d'un seuil (les paquets excédentaires sont droppés) |
| **Shaping** | Retarder (mettre en file) les paquets excédentaires au lieu de les supprimer |

---

## 1️⃣ — Pourquoi la QoS est nécessaire : les trafics n'ont pas les mêmes besoins

### Le réseau convergent : tout sur le même câble

Les réseaux modernes transportent **voix, vidéo et données** sur la même infrastructure IP.
Ces trafics ont des exigences très différentes :

| Type de trafic | Protocole | Latence | Gigue | Perte | Bande passante | Caractère |
|---|---|---|---|---|---|---|
| **VoIP** | RTP/UDP | < 150 ms ⚠️ | < 30 ms ⚠️ | < 1 % ⚠️ | ~80 kbps/appel | **Temps-réel, inélastique** |
| **Vidéoconférence** | RTP/UDP | < 200 ms | < 50 ms | < 5 % | 384 kbps–2 Mbps | Temps-réel |
| **Navigation web** | TCP/HTTP | < 2 000 ms | Sans importance | < 10 % | Variable | **Élastique** (TCP s'adapte) |
| **Transfert de fichiers** | TCP/FTP | Sans limite | Sans importance | ~5 % (retransmis) | Maximum disponible | **Élastique, tolère l'attente** |
| **E-mail / backup** | TCP | Sans limite | Sans importance | ~5 % | Minimum | **Best effort, peut attendre** |

> **Trafic inélastique** : doit arriver maintenant, ne peut pas être retransmis (UDP) → nécessite une priorité garantie.
> **Trafic élastique** : TCP gère la retransmission, s'adapte à la bande passante disponible → peut attendre.

### Le problème de la congestion

```
Sans QoS, tous les paquets attendent dans la MÊME file (FIFO) :

  [VoIP] [ZIP] [VoIP] [WEB] [UPDATE] [VoIP] [VoIP] [ZIP] [ZIP]
  ─────────────────────────────────────────────────────► Sortie (1 Mbps)

  Un paquet VoIP peut attendre derrière 5 paquets ZIP → latence excessive → appel haché
```

---

**🖼️ ILLUSTRATION 1**
> *Légende* : Schéma côte à côte. Gauche "Sans QoS (FIFO)" : une seule file unique mélangeant paquets VoIP (téléphone), ZIP (archive), Web (globe), update (flèche). Le routeur envoie dans l'ordre d'arrivée. Indicateurs rouges : latence VoIP 300 ms, gigue élevée, appel dégradé. Droite "Avec QoS (LLQ)" : trois files séparées. File rouge VoIP traitée en priorité stricte. File orange données critiques avec WFQ. File bleue trafic ordinaire. Paquets VoIP passent immédiatement. Indicateurs verts : latence 45 ms, gigue faible, appel fluide.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 2️⃣ — Le marquage DSCP : étiqueter les paquets

### Où se trouve le champ DSCP ?

Le champ DSCP est dans l'**en-tête IP** (couche 3), dans le byte ToS (Type of Service).
Il occupe **6 bits** → 64 valeurs possibles (0 à 63).

```
En-tête IP :
┌─────────┬──────────┬────────────────────────────────┐
│ Version │  ToS/DS  │  ... reste de l'en-tête ...    │
│  4 bits │  8 bits  │                                 │
└─────────┴──────────┴────────────────────────────────┘
              │
              └── DSCP : 6 premiers bits
                  CU   : 2 bits réservés
```

### Classes DSCP à connaître

| Classe | Nom | Valeur DSCP | Binaire | Usage typique |
|---|---|---|---|---|
| **EF** | Expedited Forwarding | **46** | 101110 | VoIP, trafic voix temps-réel |
| **AF41** | Assured Forwarding 4.1 | **34** | 100010 | Vidéoconférence |
| **AF31** | Assured Forwarding 3.1 | **26** | 011010 | Données critiques d'entreprise |
| **AF21** | Assured Forwarding 2.1 | **18** | 010010 | Données transactionnelles |
| **AF11** | Assured Forwarding 1.1 | **10** | 001010 | Streaming non-critique |
| **CS3** | Class Selector 3 | **24** | 011000 | Signalement VoIP (SIP, H.323) |
| **CS1** | Class Selector 1 | **8** | 001000 | Trafic scavenger (indésirable) |
| **BE** | Best Effort | **0** | 000000 | Trafic ordinaire, par défaut |

> 💡 **À retenir absolument** : **EF = 46** pour la voix · **BE = 0** pour le trafic ordinaire
> Le signalement VoIP (SIP) utilise **CS3 = 24** (séparé du trafic RTP voix)

### Qui marque les paquets ?

```
TÉLÉPHONE IP → marque lui-même ses paquets RTP en DSCP EF (46)
            → marque la signalisation SIP en DSCP CS3 (24)

ROUTEUR EN ENTRÉE DE RÉSEAU → peut re-marquer les paquets venant des PC
            → "trust" : faire confiance au marquage du téléphone
            → "set" : forcer un marquage quel que soit le marquage d'origine

RÈGLE DE CONFIANCE (trust boundary) :
  ✓ Faire confiance aux téléphones IP Cisco (ils marquent correctement)
  ✗ Ne PAS faire confiance aux PC (un utilisateur peut modifier son DSCP)
  → Le routeur/switch re-marque le trafic PC en BE au point d'entrée
```

---

**🖼️ ILLUSTRATION 2**
> *Légende* : Schéma réseau avec Trust Boundary. À gauche : téléphone IP envoyant des paquets avec label DSCP EF=46, flèche verte "Confiance accordée" passant le trust boundary. PC envoyant des paquets avec label DSCP EF=46 malicieux, flèche rouge "Re-marqué en BE=0" à la trust boundary. Le switch ou routeur en entrée constitue la trust boundary (ligne pointillée). Les valeurs DSCP dans l'en-tête IP sont représentées comme des étiquettes colorées sur les paquets.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 3️⃣ — Les files d'attente : traiter les paquets dans le bon ordre

### Le problème sans files intelligentes

Sans QoS, le routeur utilise **FIFO** (First In, First Out) — premier arrivé, premier servi.
Un gros paquet TCP peut bloquer des dizaines de petits paquets VoIP → **head-of-line blocking**.

### Les mécanismes de files d'attente

#### FIFO — First In First Out
```
Tous les paquets dans une seule file, traités dans l'ordre d'arrivée.
→ Simple, aucune garantie, non recommandé sur les liens congestionnables.
```

#### PQ — Priority Queuing
```
4 files (High / Medium / Normal / Low) — traite toute la file High avant Medium.
→ Risque de "famine" : les files basses ne sont jamais traitées si High est saturée.
```

#### WFQ — Weighted Fair Queuing
```
Partage équitable pondéré de la bande passante entre tous les flux.
→ Bon pour l'équité, mais ne garantit pas la latence pour la voix.
```

#### CBWFQ — Class-Based WFQ
```
WFQ avec des classes définies par l'admin → garanties de bande passante par classe.
→ Bien pour les données, mais toujours pas de garantie stricte de latence.
```

#### LLQ — Low Latency Queuing ⭐ (recommandé VoIP)
```
CBWFQ + une file strictement prioritaire (priority queue) pour la voix.
→ Les paquets VoIP sont traités EN PREMIER, avant tout autre trafic.
→ Bande passante garantie + latence garantie + gigue minimale.
→ Standard de facto pour les réseaux convergents voix+données.
```

---

**🖼️ ILLUSTRATION 3**
> *Légende* : Diagramme comparatif vertical de 5 mécanismes de files d'attente. Pour chaque mécanisme, une représentation visuelle des files (rectangle) avec des paquets de couleurs différentes (rouge=VoIP, bleu=web, gris=bulk) et une flèche de sortie. LLQ est mis en avant (encadré vert, étoile). Les avantages et inconvénients sont notés en vert/rouge sous chaque mécanisme. La progression de FIFO à LLQ illustre l'évolution de la sophistication.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 4️⃣ — Configuration QoS sous IOS Cisco : le framework MQC

### Qu'est-ce que MQC ?

**MQC** (Modular QoS CLI) est le framework Cisco standard pour configurer la QoS.
Il se décompose en **3 étapes obligatoires dans cet ordre** :

```
ÉTAPE 1 : class-map     → "Qui est ce trafic ?" (classification)
ÉTAPE 2 : policy-map    → "Que faire de ce trafic ?" (action)
ÉTAPE 3 : service-policy → "Sur quelle interface appliquer ?" (application)
```

---

### Étape 1 — class-map : classifier le trafic

```cisco
! Classer le trafic voix (paquets déjà marqués EF par le téléphone IP)
class-map match-any VOIX
 match dscp ef

! Classer la signalisation VoIP (SIP)
class-map match-any SIGNALEMENT-VOIX
 match dscp cs3

! Classer les données critiques
class-map match-any DONNEES-CRITIQUES
 match dscp af31

! Le reste sera traité par "class-default" (automatique)
```

> **match-any** : le paquet correspond si AU MOINS UNE condition est vraie
> **match-all** : le paquet doit correspondre à TOUTES les conditions (ET logique)

### Étape 2 — policy-map : définir les actions

```cisco
policy-map QOS-WAN
 !
 class VOIX
  priority 256
  ! → LLQ : 256 kbps réservés en priorité stricte pour la voix
  ! → Les paquets voix ne peuvent JAMAIS dépasser 256 kbps (police implicite)
 !
 class SIGNALEMENT-VOIX
  bandwidth 32
  ! → 32 kbps garantis pour la signalisation SIP (pas de priorité stricte)
 !
 class DONNEES-CRITIQUES
  bandwidth percent 30
  ! → 30 % de la bande passante restante garantis
 !
 class class-default
  fair-queue
  ! → WFQ équitable pour tout le reste (best effort)
```

> ⚠️ **Règle importante** : La somme des `bandwidth` ne doit pas dépasser 75 % de la bande passante du lien (les 25 % restants sont réservés au overhead réseau).

### Étape 3 — service-policy : appliquer sur l'interface

```cisco
interface Serial0/0/0
 bandwidth 1000
  ! → Déclarer la bande passante réelle du lien (1 Mbps = 1000 kbps)
  ! → OSPF et QoS utilisent cette valeur comme référence
 service-policy output QOS-WAN
  ! → Appliquer la policy en SORTIE (direction vers le WAN)
  ! → "output" = paquets qui quittent cette interface
```

> ℹ️ La QoS s'applique toujours **en sortie** sur l'interface de congestion (le lien le plus lent).

---

**🖼️ ILLUSTRATION 4**
> *Légende* : Schéma en 3 blocs verticaux représentant les 3 étapes MQC. Bloc 1 "class-map" (bleu) : entonnoir triant les paquets par couleur (DSCP). Bloc 2 "policy-map" (orange) : boîte avec des règles d'action pour chaque classe (priorité, bande passante garantie, fair-queue). Bloc 3 "service-policy" (vert) : interface réseau avec la flèche de sortie. Des flèches relient les 3 blocs. Le code IOS correspondant est affiché sous chaque bloc en police monospace sombre.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 5️⃣ — Vérifier la QoS : les commandes show

### show policy-map interface

```cisco
R1# show policy-map interface Serial0/0/0

Serial0/0/0

  Service-policy output: QOS-WAN

    Class-map: VOIX (match-any)
      192800 packets, 5976000 bytes
      30 second offered rate 256000 bps, drop rate 0 bps
      Match: dscp ef (46)
      Queueing
        Strict Priority
        Output Queue: Conversation 264/1000000
        (pkts matched/bytes matched) 192800/5976000

    Class-map: DONNEES-CRITIQUES (match-any)
      45200 packets, 32544000 bytes
      30 second offered rate 300000 bps, drop rate 0 bps
      Match: dscp af31 (26)
      Queueing
        bandwidth 30% (300 kbps)

    Class-map: class-default (match-any)
      12500 packets, 9000000 bytes
      30 second offered rate 100000 bps, drop rate 0 bps
      Match: any
        Weighted Fair Queueing
```

**Lecture de cette sortie :**
- La classe VOIX traite 256 kbps en priorité stricte → `drop rate 0 bps` = aucune perte ✓
- Les données critiques reçoivent 300 kbps garantis
- Le reste utilise WFQ

---

**🖼️ ILLUSTRATION 5**
> *Légende* : Diagramme de topologie réseau complet VoIP + Data avec les marquages DSCP annotés sur chaque flux. Téléphone IP → paquets RTP marqués EF=46 (rouge). PC → paquets HTTP marqués BE=0 (gris). Les deux convergent vers le routeur R1 qui applique la policy-map QOS-WAN. Sur le lien WAN (lien le plus étroit), les 3 files d'attente LLQ sont visibles avec les paquets priorisés. R2 reçoit les paquets et les délivre. Côté droit : phone IP2 et PC_Serveur. Les labels de bande passante (256 kbps VoIP, 300 kbps data, reste WFQ) sont indiqués sur les files.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 6️⃣ — Limites et bonnes pratiques de la QoS

### Ce que la QoS peut faire

```
✓ Garantir la priorité de la voix pendant les périodes de CONGESTION
✓ Réduire la latence et la gigue pour les flux temps-réel
✓ Garantir un minimum de bande passante pour les applications critiques
✓ Limiter les trafics indésirables (peer-to-peer, streaming non-autorisé)
```

### Ce que la QoS NE peut PAS faire

```
✗ Créer de la bande passante qui n'existe pas
  → Si le lien est saturé à 100 %, LLQ ne peut donner que ce qui est alloué
  → Solution réelle : augmenter la capacité du lien (upgrade)

✗ Fonctionner sans cohérence de bout en bout
  → La QoS doit être configurée sur TOUS les équipements du chemin
  → Un seul routeur sans QoS entre les deux extrémités annule l'effet

✗ Corriger une mauvaise conception réseau
  → La QoS est un outil d'optimisation, pas de réparation
```

> 🔑 **Calcul de dimensionnement VoIP** :
> Codec G.711 : **64 kbps** par appel + overhead IP/UDP/RTP ≈ **80 kbps** par appel
> Sur un lien WAN 1 Mbps : max ~**12 appels simultanés** recommandés (en laissant 40 % pour les données)

---

## 📌 Les essentiels à retenir pour l'examen

> ✅ La QoS est nécessaire car **voix et données n'ont pas les mêmes contraintes**
> ✅ VoIP : latence < 150 ms · gigue < 30 ms · perte < 1 % · ~80 kbps/appel
> ✅ **DSCP EF = 46** (voix RTP) · **DSCP CS3 = 24** (signalisation SIP) · **DSCP BE = 0** (trafic ordinaire)
> ✅ **LLQ** = file à priorité stricte pour la voix + WFQ pour le reste = mécanisme recommandé VoIP
> ✅ MQC en 3 étapes : `class-map` (classer) → `policy-map` (agir) → `service-policy output` (appliquer)
> ✅ La QoS s'applique en **sortie** (`output`) sur l'interface de congestion (lien le plus lent)
> ✅ La QoS ne crée pas de bande passante — elle **optimise l'utilisation** de celle qui existe

---

*Fiche de Cours — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S6*
*Compétences : S3.1 · S3.2 · S3.3 · C2.2 · C2.3*
