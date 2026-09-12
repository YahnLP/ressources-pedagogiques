# 🔬 TRAVAUX PRATIQUES — S6 · 2ᵉ ANNÉE · E31
## QoS : Priorisation VoIP vs Data — Configuration MQC sur Packet Tracer

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Packet Tracer**
> **Fichier .pkt** : `S6_E31_QoS_VoIP.pkt` (fourni par l'enseignant — QoS non configurée)
> **Épreuve ciblée** : **E31** – Infrastructure réseau · **E32** – Exploitation

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S3.2** | Identifier les marquages DSCP dans les flux réels |
| **S3.3** | Configurer LLQ (class-map, policy-map, service-policy) |
| **C2.2** | Appliquer une policy QoS sur une interface Cisco |
| **C2.3** | Vérifier et diagnostiquer la QoS avec `show policy-map interface` |
| **C3.1** | Documenter la configuration dans un compte rendu |

---

## 🗺️ Topologie du TP

```
  IP_Phone1 ──┐                                    ┌── IP_Phone2
  PC_Data1  ──┤                                    ├── PC_Serveur
              │                                    │
           SW_SIEGE          WAN                SW_AGENCE
           (LAN)         (1 Mbps simulé)          (LAN)
             │                 │                    │
             └──── Gi0/0 ─── R1 ─── Se0/0/0 ──── R2 ──── Gi0/0 ───┘

Adressage :
  LAN Siège    : 192.168.10.0/24   (R1 Gi0/0 : .1)
  WAN          : 10.0.12.0/30      (R1 Se0/0/0 : .1 · R2 Se0/0/0 : .2)
  LAN Agence   : 192.168.20.0/24   (R2 Gi0/0 : .1)

  IP_Phone1    : 192.168.10.11 (DHCP du CME)
  PC_Data1     : 192.168.10.101 (DHCP)
  IP_Phone2    : 192.168.20.11 (DHCP du CME)
  PC_Serveur   : 192.168.20.201

  VLAN Voix    : VLAN 10  (IP_Phones)
  VLAN Data    : VLAN 20  (PC)
  → Les téléphones marquent automatiquement leur trafic DSCP EF (46)
  → Les PC envoient en DSCP BE (0) par défaut
```

---

## 🟢 NIVEAU 1 — Observer le trafic sans QoS (10 min)

### Test initial sans QoS

**1.1** — Passe un appel entre IP_Phone1 et IP_Phone2.
Pendant l'appel, génère du trafic data intense : depuis PC_Data1, envoie un ping flood vers PC_Serveur.

```
Mode simulation Packet Tracer : Filters → voix (RTP) + ICMP
Observer les paquets qui circulent.
```

**1.2** — Affiche `show interface Serial0/0/0` sur R1. Note la charge du lien :

```
Load in  : _______   Load out : _______   Reliability : _______
La ligne "output queue" indique : _____ paquets en attente
```

**1.3** — Dans le mode simulation, observe les paquets voix (RTP). Sont-ils traités immédiatement ou font-ils la queue derrière les paquets ICMP ?

```
Ordre de traitement observé : ________________________________________________
Les paquets RTP sont : ☐ Traités immédiatement ☐ En attente derrière d'autres paquets
```

**1.4** — Affiche la table de routage de R1 avec `show ip route`. Le routage fonctionne-t-il ?

```
Route vers 192.168.20.0/24 : ________________________________________________
Communication de bout en bout : ☐ Fonctionnelle ☐ Non fonctionnelle
```

---

## 🟡 NIVEAU 2 — Classifier le trafic (class-map) (15 min)

> Tu vas maintenant configurer la QoS en 3 étapes. Commence par les class-maps.

**2.1** — Sur R1, configure les class-maps suivantes :

```cisco
R1> enable
R1# configure terminal

! Class-map pour le trafic voix (paquets RTP marqués EF par les téléphones IP)
R1(config)# class-map match-any _____________
R1(config-cmap)# match dscp _____________
R1(config-cmap)# exit

! Class-map pour la signalisation VoIP (SIP - marquée CS3)
R1(config)# class-map match-any _____________
R1(config-cmap)# match dscp _____________
R1(config-cmap)# exit

! Class-map pour les données critiques (marquées AF31)
R1(config)# class-map match-any _____________
R1(config-cmap)# match dscp _____________
R1(config-cmap)# exit
```

*(Compléter les blancs en t'aidant de la fiche de cours)*

**2.2** — Vérifie les class-maps créées :

```cisco
R1# show class-map
```

Note les class-maps affichées :

```
Class Map match-any __________________ (id __)
  Match: dscp ef (__)

Class Map match-any __________________ (id __)
  Match: dscp cs3 (__)

Class Map match-any __________________ (id __)
  Match: dscp af31 (__)
```

---

## 🟠 NIVEAU 3 — Définir les actions (policy-map) (15 min)

**3.1** — Configure la policy-map QOS-WAN avec les règles LLQ :

```cisco
R1(config)# policy-map _____________

! Voix : priorité stricte avec 256 kbps réservés
R1(config-pmap)# class _____________
R1(config-pmap-c)# priority _____________
R1(config-pmap-c)# exit

! Signalisation : bande passante garantie (32 kbps)
R1(config-pmap)# class _____________
R1(config-pmap-c)# bandwidth _____________
R1(config-pmap-c)# exit

! Données critiques : 30 % de la bande passante restante
R1(config-pmap)# class _____________
R1(config-pmap-c)# bandwidth percent _____________
R1(config-pmap-c)# exit

! Trafic par défaut : WFQ équitable
R1(config-pmap)# class class-default
R1(config-pmap-c)# fair-queue
R1(config-pmap-c)# exit

R1(config-pmap)# exit
```

**3.2** — Vérifie la policy-map :

```cisco
R1# show policy-map QOS-WAN
```

Recopie le résumé affiché :

```
Policy Map QOS-WAN
  Class _____________
    Priority : _____ kbps
  Class _____________
    Bandwidth : _____ kbps
  Class _____________
    Bandwidth : _____ %
  Class class-default
    Weighted Fair Queueing
```

---

## 🔵 NIVEAU 4 — Appliquer la QoS (service-policy) (20 min)

**4.1** — Déclare la bande passante réelle du lien WAN et applique la policy :

```cisco
R1(config)# interface _____________
R1(config-if)# bandwidth 1000
  ! ↑ Déclare 1 Mbps = référence pour les calculs QoS
R1(config-if)# service-policy output _____________
R1(config-if)# end
```

**4.2** — Vérifie que la policy est bien appliquée sur l'interface :

```cisco
R1# show policy-map interface Serial0/0/0
```

La sortie doit mentionner :

```
Serial0/0/0

 Service-policy output: _____________ ← nom de ta policy

   Class-map: _____________ (match-any)
     Match: dscp ef (46)
     Strict Priority
     ...

   Class-map: class-default (match-any)
     Weighted Fair Queueing
```

**4.3** — Reproduis la même configuration sur R2 (lien WAN sens inverse).

```
Sur R2 :
R2(config)# class-map match-any VOIX
R2(config-cmap)# match dscp ef
R2(config-cmap)# exit
R2(config)# class-map match-any SIGNALEMENT-VOIX
R2(config-cmap)# match dscp cs3
R2(config-cmap)# exit
R2(config)# policy-map QOS-WAN
R2(config-pmap)# class VOIX
R2(config-pmap-c)# priority 256
R2(config-pmap-c)# exit
R2(config-pmap)# class SIGNALEMENT-VOIX
R2(config-pmap-c)# bandwidth 32
R2(config-pmap-c)# exit
R2(config-pmap)# class class-default
R2(config-pmap-c)# fair-queue
R2(config-pmap-c)# exit
R2(config-pmap)# exit
R2(config)# interface Serial0/0/0
R2(config-if)# bandwidth 1000
R2(config-if)# service-policy output QOS-WAN
R2(config-if)# end
```

---

## 🔴 NIVEAU 5 — Vérifier et documenter (20 min)

### Tests de validation

**5.1** — Reproduis le test du Niveau 1 (appel VoIP + ping flood simultanés).
Le comportement a-t-il changé ?

```
Sans QoS : les paquets voix ________________________________________________
Avec QoS : les paquets voix ________________________________________________
Observation dans le mode simulation : ________________________________________
```

**5.2** — Affiche `show policy-map interface Serial0/0/0` sur R1 pendant un appel actif.
Note les statistiques de la classe VOIX :

```
Packets matched (classe VOIX) : _____________
Bytes matched : _____________
Drop rate : _____________ bps
→ drop rate = 0 bps signifie : ______________________________________________
```

**5.3** — Calcul de dimensionnement : combien d'appels VoIP simultanés G.711 peut supporter ce lien WAN de 1 Mbps avec la configuration actuelle ?

```
Bande passante réservée à la voix : _______ kbps (valeur dans priority)
Consommation par appel G.711 : ~80 kbps (codec 64 kbps + overhead IP/UDP/RTP)
Nombre max d'appels simultanés = _______ / 80 = _______ appels

Bande passante restante pour les données :
  1 000 kbps − _______ kbps (voix) − _______ kbps (signalisation) = _______ kbps
```

**5.4** — Rédige le compte rendu d'intervention :

```
┌─────────────────────────────────────────────────────────────────────────┐
│            COMPTE RENDU — Configuration QoS VoIP                       │
│            Réf. : S6-E31-CR-_______  Date : _______________            │
├─────────────────────────────────────────────────────────────────────────┤
│  Technicien : _______________________  Binôme : ______________________  │
├─────────────────────────────────────────────────────────────────────────┤
│  CONTEXTE                                                               │
│  Problème initial : ___________________________________________________  │
│  Cause identifiée : ___________________________________________________  │
├─────────────────────────────────────────────────────────────────────────┤
│  SOLUTION MISE EN ŒUVRE                                                 │
│  Mécanisme utilisé : ___________________________________________________  │
│  Équipement(s) configuré(s) : __________________________________________ │
│  Interface(s) concernée(s) : ___________________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  POLITIQUE QoS APPLIQUÉE                                                │
│  Classe VOIX : DSCP _____ → priorité _____ kbps (_____ appels max)    │
│  Classe SIGNALEMENT : DSCP _____ → bandwidth _____ kbps               │
│  Reste du trafic : _____________________________________________________  │
├─────────────────────────────────────────────────────────────────────────┤
│  VALIDATION                                                             │
│  Test appel VoIP + trafic data : ☐ OK — voix fluide sans dégradation  │
│  Commande de vérification : show policy-map interface _______________   │
│  drop rate classe VOIX : _____ bps ← doit être 0                      │
├─────────────────────────────────────────────────────────────────────────┤
│  RECOMMANDATIONS                                                        │
│  _____________________________________________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  Visa technicien : ___________________   Visa enseignant : ____________ │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Identifier DSCP EF=46 pour la VoIP | ☐ | ☐ | ☐ |
| Configurer une class-map avec match dscp | ☐ | ☐ | ☐ |
| Configurer une policy-map avec priority et bandwidth | ☐ | ☐ | ☐ |
| Appliquer une service-policy output sur une interface | ☐ | ☐ | ☐ |
| Lire et interpréter show policy-map interface | ☐ | ☐ | ☐ |
| Calculer le nombre d'appels VoIP possibles | ☐ | ☐ | ☐ |
| Rédiger un compte rendu d'intervention QoS | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niveaux 1-2 : observation + class-maps correctes | /5 |
| Niveau 3 : policy-map complète et cohérente | /5 |
| Niveau 4 : service-policy appliquée + R2 configuré | /5 |
| Niveau 5 : validation fonctionnelle + calcul dimensionnement | /5 |
| Compte rendu d'intervention complet | /5 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 2 — class-maps

```cisco
class-map match-any VOIX
 match dscp ef                ! DSCP 46

class-map match-any SIGNALEMENT-VOIX
 match dscp cs3               ! DSCP 24

class-map match-any DONNEES-CRITIQUES
 match dscp af31              ! DSCP 26
```

## Correction Niveau 3 — policy-map

```cisco
policy-map QOS-WAN
 class VOIX
  priority 256
 class SIGNALEMENT-VOIX
  bandwidth 32
 class DONNEES-CRITIQUES
  bandwidth percent 30
 class class-default
  fair-queue
```

## Correction Niveau 4 — service-policy

```cisco
interface Serial0/0/0
 bandwidth 1000
 service-policy output QOS-WAN
```

## Correction Niveau 5 — calculs

```
Appels max = 256 kbps / 80 kbps = 3,2 → 3 appels simultanés maximum

Bande passante restante pour données :
1 000 − 256 (voix) − 32 (signalisation) = 712 kbps disponibles
30 % pour données critiques = ~213 kbps garantis
Reste (fair-queue) ≈ 499 kbps pour best effort

show policy-map interface Serial0/0/0 :
→ drop rate classe VOIX = 0 bps → QoS fonctionne correctement
→ Si drop rate > 0 → lien saturé ou priority trop faible
```

## Recommandations pour le compte rendu

- Si > 3 appels simultanés nécessaires → augmenter `priority` OU upgrader le lien WAN
- Configurer la QoS de façon symétrique sur R1 ET R2 (les deux sens du lien)
- En production : implémenter aussi le marquage DSCP en entrée (trust boundary sur les switchs)
- Surveiller régulièrement avec `show policy-map interface` — drop rate > 0 = problème

---

*TP QoS VoIP + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S6*
*Document Portfolio E31/E32 — Compétences S3.2 · S3.3 · C2.2 · C2.3 · C3.1*
