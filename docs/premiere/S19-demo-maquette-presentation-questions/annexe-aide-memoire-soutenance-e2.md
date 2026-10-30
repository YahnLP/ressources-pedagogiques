# 🗂️ AIDE-MÉMOIRE SOUTENANCE E2 — À PLASTIFIER
## Structure · Démo · Questions · PV Recettage · BAC PRO CIEL · E2 · 2ᵉ année S19

---

> *Lire pendant la préparation · Conserver le jour J*

---

## ⏱️ Minutage de la soutenance (15 min)

```
0–5 min  → Présentation (schéma + architecture)
5–10 min → Démonstration LIVE
10–15 min→ Questions du jury
```

---

## 🎤 Structure de présentation (5 min)

```
30s : Intro (nom du projet + objectif)
90s : Architecture (schéma blocs + choix technologiques)
60s : PCB + composants (schéma KiCad + BOM)
120s: Démo live (dashboard + capteurs + alertes)
30s : Bilan + 1 amélioration
```

---

## 🖥️ Les 5 démos incontournables

```
1. Jauge T° se met à jour en temps réel
2. Alerte orange/rouge (doigt sur DHT22)
3. Historique InfluxDB (graphe ou interface)
4. Messages MQTT dans le terminal
5. PV métrologie → lire le résultat de conformité
```

---

## ❓ Réponses types

```
"Architecture ?" → ESP32 mesure → MQTT → Broker → Node-RED → Dashboard + InfluxDB

"Si WiFi coupé ?" → Reconnexion auto · données perdues pendant coupure

"Pourquoi MQTT vs HTTP ?" → Plus léger · connexion persistante · multi-clients

"MTBF ?" → DHT22 = 50 000h = 5,7 ans · Système série → MTBFs plus faible

"Conforme ?" → Biais +0,21°C · U=0,22°C · Pire cas 0,43°C < 0,5°C → OUI ✓

"Limite CEM ?" → Breadboard sans plan de masse → pistes longues = antennes
```

---

## 📋 Dossier à avoir sous la main

```
☐ Schéma KiCad (PDF)
☐ BOM (tableau complet)
☐ Code Arduino (commenté)
☐ PV métrologie signé
☐ Capture dashboard
☐ Schéma architecture
```

---

## 🚨 Checklist J−1

```
☐ ESP32 flashé avec version finale
☐ Node-RED démarré + flow Deploy
☐ Dashboard accessible : 1880/ui
☐ MQTT fonctionnel (messages dans debug)
☐ InfluxDB données récentes
☐ Dossier complet en PDF
☐ Backup sur clé USB
```

---

## 💡 La formule des 17/20

```
"J'ai fait X parce que Y, ce qui
 permet Z dans ce contexte."

Exemple :
"J'ai placé le condensateur 100nF
 à < 2mm du CI parce qu'au-delà
 l'inductance de piste l'annule."

≠ "J'ai mis un condensateur
    parce qu'il le faut."
```

---

*Aide-Mémoire Soutenance E2 — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S19*
