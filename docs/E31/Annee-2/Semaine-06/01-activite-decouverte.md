# 🔍 ACTIVITÉ DE DÉCOUVERTE — S6 · 2ᵉ ANNÉE · E31
## « L'embouteillage réseau » — Comprendre la congestion et la priorisation

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche · Stylo · Calculatrice
> **Principe** : Avant tout cours sur la QoS, tu vas simuler une congestion réseau sur papier et inventer toi-même des règles de priorisation pour résoudre le problème.

---

## 🎯 Mise en situation

> Tu es **responsable réseau** d'une entreprise qui vient d'installer la **téléphonie IP** (VoIP).
>
> Depuis ce matin, les employés se plaignent :
> - Les appels téléphoniques sont **hachés, robotiques**, parfois coupés
> - Les transferts de fichiers et la navigation web fonctionnent **normalement**
>
> Le réseau utilise un seul lien WAN de **1 Mbps** entre le siège et l'agence.
> Tu observes les flux qui transitent sur ce lien à un instant T.

---

## 📊 PARTIE 1 — Analyser la situation (10 min)

**Les flux présents sur le lien WAN à cet instant :**

| Flux | Type | Débit demandé | Sensible à... |
|---|---|---|---|
| Appel téléphonique VoIP (Alice ↔ Bob) | Voix temps-réel | 80 kbps | Délai, coupures, irregularité |
| Téléchargement d'un fichier ZIP | Données bulk | 600 kbps | Débit global uniquement |
| Navigation web (5 employés) | HTTP/HTTPS | 400 kbps | Délai modéré acceptable |
| Mise à jour logicielle automatique | Données bulk | 300 kbps | Peut attendre, pas urgent |
| **TOTAL DEMANDÉ** | | **1 380 kbps** | |
| **Capacité du lien** | | **1 000 kbps** | |

**Question 1.1** — Le total demandé (1 380 kbps) dépasse la capacité (1 000 kbps). Quel est le déficit ?

```
Déficit = _______ − _______ = _______ kbps à "éliminer" ou "retarder"
```

**Question 1.2** — Sans aucune règle de priorisation, que se passe-t-il avec le trafic VoIP ?

```
Le routeur gère tous les flux de façon : ☐ Identique ☐ Prioritaire pour la voix
Conséquence pour la VoIP : _________________________________________________
Le fichier ZIP et la mise à jour reçoivent : ☐ Moins de bande passante ☐ La même chose
```

**Question 1.3** — Parmi les 4 flux, lequel peut le plus facilement être "mis en attente" sans que l'utilisateur s'en rende compte ? Lequel ne peut ABSOLUMENT PAS attendre ?

```
Peut attendre (sans impact perceptible) : ____________________________________
Ne peut PAS attendre : _______________________________________________________
Raison : ___________________________________________________________________
```

---

## 🚦 PARTIE 2 — Inventer des règles de priorité (10 min)

> Le routeur dispose de **files d'attente** (comme des couloirs de tri postal).
> Chaque paquet arrive et est placé dans une file selon son type.
> Le routeur envoie les paquets dans un ordre que TU vas définir.

**Question 2.1** — Propose une organisation en 3 files d'attente. Pour chaque file, indique quels flux y vont et pourquoi.

```
FILE 1 — Priorité : ☐ Haute ☐ Moyenne ☐ Basse
  Trafic concerné : _________________________________________________________
  Pourquoi cette priorité : _________________________________________________
  Bande passante maximum allouée : _______ kbps

FILE 2 — Priorité : ☐ Haute ☐ Moyenne ☐ Basse
  Trafic concerné : _________________________________________________________
  Pourquoi cette priorité : _________________________________________________
  Bande passante allouée : _______ kbps

FILE 3 — Priorité : ☐ Haute ☐ Moyenne ☐ Basse
  Trafic concerné : _________________________________________________________
  Pourquoi cette priorité : _________________________________________________
  Bande passante restante : _______ kbps
```

**Question 2.2** — Avec ton organisation, la somme des bandes passantes des files 1+2+3 dépasse-t-elle 1 000 kbps ?

```
File 1 : _______ kbps + File 2 : _______ kbps + File 3 : _______ kbps
= _______ kbps → ☐ ≤ 1 000 kbps (OK) ☐ > 1 000 kbps (problème !)
```

**Question 2.3** — Avec tes règles, l'appel VoIP d'Alice et Bob est-il préservé ?

```
VoIP est dans la file : _______
Cette file est traitée en : ☐ Premier ☐ Deuxième ☐ Troisième
L'appel sera : ☐ Préservé (fluide) ☐ Dégradé ☐ Coupé
```

---

## 🔬 PARTIE 3 — Les trois contraintes du trafic temps-réel (10 min)

> La VoIP est "capricieuse" — elle a des exigences très précises. Voici pourquoi.

**Question 3.1** — Un paquet VoIP contient 20 ms d'audio. Il doit arriver dans les **150 ms** maximum (recommandation ITU G.114). Qu'est-ce que cela signifie concrètement pour le réseau ?

```
Si le paquet arrive en 200 ms (trop tard) : ___________________________________
Ce paramètre s'appelle la : __________________________________ (latence / délai)
```

**Question 3.2** — Les paquets VoIP arrivent normalement toutes les 20 ms. Mais à cause de la congestion, certains arrivent après 15 ms, d'autres après 35 ms. Quel effet cela produit-il sur l'audio ?

```
L'irrégularité des temps d'arrivée s'appelle la : ____________________________
Effet sur l'audio : __________________________________________________________
Solution côté récepteur : ____________________________________________________
```

**Question 3.3** — Un paquet VoIP est perdu en route (congestion). Que se passe-t-il ?

```
Contrairement au HTTP, la VoIP : ☐ Redemande le paquet perdu ☐ N'attend pas
Raison : ___________________________________________________________________
Effet audible : ______________________________________________________________
Tolérance maximale de perte : environ _______ % pour une bonne qualité
```

**Question 3.4** — Complète le tableau des contraintes QoS :

| Trafic | Latence max | Gigue max | Perte max | Priorité réseau |
|---|---|---|---|---|
| **VoIP** | 150 ms | 30 ms | 1 % | |
| **Vidéoconférence** | 200 ms | 50 ms | 5 % | |
| **Navigation web** | ~2 000 ms | sans importance | ~10 % | |
| **Transfert de fichier** | sans limite | sans importance | ~5 % (retransmis) | |

---

## 🏁 Bilan de l'atelier

**Complète avec tes propres mots :**

```
La QoS (Quality of Service) est nécessaire quand : ____________________________
_____________________________________________________________________________

Les 3 paramètres critiques pour le trafic temps-réel sont :
1. _______________________________  (délai de bout en bout)
2. _______________________________  (variation des délais)
3. _______________________________  (proportion de paquets perdus)

La solution réseau consiste à : ______________________________________________
_____________________________________________________________________________

Le terme technique pour "mettre les paquets voix en premier" est : ____________
```

> ✅ Tu viens de réinventer le principe de la QoS par toi-même.
> Le cours va maintenant te donner le vocabulaire standardisé (DSCP, LLQ, MQC)
> et les commandes pour mettre en place ce que tu viens de concevoir sur un routeur Cisco.

---

## 📎 Pour l'enseignant — Réponses et points clés

**1.1** : Déficit = 1380 − 1000 = **380 kbps** à réguler

**2.1** : Réponse attendue proche de LLQ :
- File haute (priorité stricte) : VoIP, 80 kbps garantis — ne peut pas attendre
- File moyenne : Web + données critiques, ~600 kbps partagés équitablement
- File basse : Téléchargements + MAJ, reste disponible (~320 kbps en temps normal)

**3.3** : La VoIP n'attend pas la retransmission TCP — elle utilise UDP → paquet perdu = silence ou artefact · Tolérance : ~1 % de perte acceptable

**Transition naturelle** : *"Ce que vous venez d'inventer s'appelle LLQ (Low Latency Queuing). En IOS Cisco, cela se configure avec 3 blocs : class-map, policy-map, service-policy."*

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S6*
*Compétences : S3.1 · S3.2 · S3.3*
