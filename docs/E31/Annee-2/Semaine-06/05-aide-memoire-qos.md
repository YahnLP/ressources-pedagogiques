# 🗂️ AIDE-MÉMOIRE QoS — À PLASTIFIER
## DSCP · Files d'attente · LLQ · MQC Cisco · BAC PRO CIEL · E31 · 2ᵉ année S6

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 🏷️ Classes DSCP à connaître

| Classe | Valeur | Usage |
|---|---|---|
| **EF** | **46** | 🎙️ VoIP (trafic voix RTP) |
| **CS3** | **24** | 📞 Signalisation SIP/H.323 |
| **AF41** | **34** | 📹 Vidéoconférence |
| **AF31** | **26** | 💼 Données critiques ERP |
| **AF21** | **18** | 📊 Données transactionnelles |
| **BE** | **0** | 🌐 Trafic ordinaire (défaut) |

---

## 📋 Contraintes VoIP

```
Latence max  : 150 ms (bout en bout)
Gigue max    : 30 ms
Perte max    : 1 %
BW / appel   : ~80 kbps (G.711)  ou  ~24 kbps (G.729)
Protocole    : UDP/RTP → pas de retransmission !
```

---

## ⚙️ MQC — 3 étapes dans l'ordre

### Étape 1 — class-map (classer)
```cisco
class-map match-any VOIX
 match dscp ef

class-map match-any SIGNALEMENT-VOIX
 match dscp cs3

class-map match-any DONNEES-CRITIQUES
 match dscp af31
```

### Étape 2 — policy-map (agir)
```cisco
policy-map QOS-WAN
 class VOIX
  priority 256        ← LLQ : kbps réservés, STRICTEMENT prioritaire
 class SIGNALEMENT-VOIX
  bandwidth 32        ← kbps garantis
 class DONNEES-CRITIQUES
  bandwidth percent 30 ← % de la BW restante
 class class-default
  fair-queue          ← WFQ pour le reste
```

### Étape 3 — service-policy (appliquer)
```cisco
interface Serial0/0/0      ← interface du lien congestionnable
 bandwidth 1000            ← bande passante réelle en kbps
 service-policy output QOS-WAN  ← TOUJOURS output !
```

---

## ✅ Commandes de vérification

```
show class-map              ← classes configurées
show policy-map             ← policy-maps configurées
show policy-map interface Serial0/0/0  ← stats en temps réel
  → drop rate VOIX = 0 bps  = QoS OK ✓
  → drop rate VOIX > 0 bps  = lien saturé ✗
```

---

## 📐 Calcul de dimensionnement VoIP

```
Appels max = Bande passante priority (kbps) / 80 kbps
Ex : priority 256 kbps → 256/80 = 3 appels G.711 max

Règle : réserver max 33 % du lien WAN à la voix
```

---

## ⚠️ Les 4 erreurs classiques

| ❌ Erreur | ✅ Correction |
|---|---|
| `match dscp 0` pour la voix | `match dscp ef` (EF = 46) |
| `priority` pour les données | `priority` réservé à la VOIX (LLQ) |
| `service-policy input` | Toujours **`output`** sur lien WAN |
| QoS sur Gi0/0 (LAN) | Sur l'interface WAN congestionnable |

---

## 🔑 Règle d'or

```
La QoS ne CRÉE PAS de bande passante.
Elle OPTIMISE l'utilisation de celle qui existe.
Si le lien est à 100 % → upgrader le lien !
```

---

*Aide-Mémoire QoS — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S6*
*Compétences S3.1 · S3.2 · S3.3 · C2.2 · C2.3*
