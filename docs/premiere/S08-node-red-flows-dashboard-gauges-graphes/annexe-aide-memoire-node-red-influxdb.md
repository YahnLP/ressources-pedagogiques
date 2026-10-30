# 🗂️ AIDE-MÉMOIRE NODE-RED · INFLUXDB — À PLASTIFIER
## Flows · Dashboard · Gauge · Chart · Séries Temporelles · BAC PRO CIEL · E2 · S8

---

> *Conserver à côté du clavier pendant les TP Node-RED*

---

## 🔵 Node-RED — Nœuds essentiels

```
inject     → Déclencheur (manuel ou intervalle)
mqtt in    → Réception MQTT
json       → String JSON ↔ Objet JavaScript
function   → Code JavaScript (transformation msg)
switch     → Routage conditionnel
debug      → Afficher dans le panneau debug
mqtt out   → Publication MQTT
influxdb out → Écriture InfluxDB

Dashboard :
  gauge  → Valeur instantanée (compteur)
  chart  → Historique (courbe)
  text   → Texte affiché
  button → Bouton d'action
```

---

## 🟣 Nœud function — syntaxe de base

```javascript
// Modifier le payload
msg.payload = msg.payload * 2;
return msg;

// Extraire un champ JSON (après nœud json)
msg.payload = msg.payload.temperature;
return msg;

// Bloquer le message
if (msg.payload > 100) { return null; }
return msg;

// 2 sorties
if (alerte) { return [msg, null]; }
else        { return [null, msg]; }

// Envoyer sans msg.topic pour chart
msg.topic = "Capteur 1";   // = nom de la série
msg.payload = 23.5;
return msg;
```

---

## 🟤 Dashboard — configuration

```
URL Dashboard : http://localhost:1880/ui

Ordre de création :
  1. Tab (onglet) → ex: "Salle E2"
  2. Group (section) → ex: "Capteurs"
  3. Widget (gauge, chart...) → assigné au Group

Gauge :
  msg.payload = nombre   (ex: 23.5)
  Range : min/max + couleurs secteurs

Chart (série unique) :
  msg.payload = nombre   (ajout automatique)
  
Chart (multi-séries) :
  msg.topic  = "Nom série"
  msg.payload = nombre
  → 1 courbe par topic distinct
```

---

## 🔴 InfluxDB — concepts

```
Bucket      = base de données
Measurement = table
Tag         = métadonnée (string, indexée)
Field       = valeur mesurée (nombre)
Point       = {measurement, tags, fields, timestamp}

Format msg.payload pour influxdb out :
msg.payload = [{
  measurement: "nom_table",
  tags:   { localisation: "salle" },
  fields: { temperature: 23.5, hum: 65 }
}];
```

---

## 🟢 Requête Flux (InfluxDB 2.x)

```javascript
from(bucket: "mon_bucket")
  |> range(start: -1h)           // Période
  |> filter(fn: (r) =>
       r._measurement == "sonde")
  |> filter(fn: (r) =>
       r._field == "temperature")
  |> mean()                      // Agrégation

// Autres agrégations : max() · min() · sum() · last()
// Par fenêtre :
|> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
```

---

## ⚠️ Erreurs fréquentes

```
❌ Oublier Deploy → les modifications ne s'appliquent pas
❌ Chart vide → msg.topic manquant ou mal configuré
❌ InfluxDB "unauthorized" → token invalide ou mal copié
❌ json oublié → msg.payload.temperature = undefined
❌ Gauge ne bouge pas → msg.payload est une string, pas un nombre
   Solution : msg.payload = parseFloat(msg.payload)
```

---

## 🏗️ Architecture IoT complète

```
ESP32 → MQTT → Node-RED ──→ Dashboard (temps réel)
                         ──→ InfluxDB (stockage)
                                  │
                     Node-RED ←── Requête Flux
                         │
                         ▼
                    Chart historique
```

---

*Aide-Mémoire Node-RED + InfluxDB — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S8*
*Compétences S5.4 · S5.5 · S5.6 · C5.3*
