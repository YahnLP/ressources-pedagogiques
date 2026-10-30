# 📘 FICHE DE COURS — S8 · 2ᵉ ANNÉE · E2
## Node-RED : Flows · Dashboard · Gauges · Graphes Temps Réel · InfluxDB

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences travaillées** : S5.4 · S5.5 · S5.6 · C5.3 · C3.1

---

## 🔑 Vocabulaire clé

| Terme | Définition |
|---|---|
| **Node-RED** | Outil de programmation visuelle par flux (flows) orienté IoT · développé par IBM |
| **Flow** | Programme visuel composé de nœuds connectés par des fils |
| **Nœud (Node)** | Bloc élémentaire d'un flow — reçoit un message, le traite, le transmet |
| **Wire** | Connexion entre deux nœuds (transporte les messages) |
| **msg** | Objet JavaScript passé de nœud en nœud — `msg.payload` = la donnée principale |
| **msg.payload** | Contenu principal du message (nombre, string, JSON, booléen...) |
| **msg.topic** | Sujet/source du message (souvent le topic MQTT) |
| **Node-RED Dashboard** | Module qui génère une interface web avec gauges, graphes, boutons... |
| **Gauge** | Jauge (compteur de vitesse) — affiche une valeur instantanée |
| **Chart** | Graphe temporel — affiche l'historique d'une valeur dans le temps |
| **Tab / Group** | Organisateurs du dashboard (onglets et groupes de widgets) |
| **InfluxDB** | Base de données de séries temporelles — optimisée pour les mesures IoT |
| **Measurement** | Table de données dans InfluxDB (équivalent d'une table SQL) |
| **Field** | Valeur numérique stockée dans InfluxDB (ex: temperature=23.5) |
| **Tag** | Métadonnée de filtrage dans InfluxDB (ex: location="salle12") |
| **Bucket** | Conteneur de données dans InfluxDB 2.x (équivalent d'une base de données) |
| **Flux (InfluxDB)** | Langage de requête d'InfluxDB 2.x (remplace InfluxQL) |

---

## 1️⃣ — Node-RED : la plateforme d'orchestration IoT

### Pourquoi Node-RED ?

```
SANS NODE-RED (programmation classique) :
  → Écrire un programme Python/JS qui :
    - Se connecte au broker MQTT
    - Parse le JSON
    - Met à jour une base de données
    - Génère une page HTML dynamique
    - Gère les reconnexions
  → Centaines de lignes de code pour chaque nouvelle intégration

AVEC NODE-RED :
  → Glisser-déposer des nœuds, connecter avec des fils
  → La même chose en 10 minutes sans presque aucun code
  → Modifier en temps réel (hot reload)
  → Bibliothèque de 4 000+ nœuds communautaires
```

### Interface Node-RED

```
URL : http://localhost:1880

┌─────────────────────────────────────────────────────────────┐
│  Palette  │         Zone de flow              │  Info/Debug │
│  (nœuds   │                                   │             │
│  disponib)│    [inject]──[function]──[debug]  │  Logs ici   │
│           │                                   │             │
│  inject   │    [mqtt in]──[json]──[gauge]      │             │
│  debug    │                                   │             │
│  function │                                   │             │
│  mqtt in  │                                   │             │
│  mqtt out │                                   │             │
│  http in  ├───────────────────────────────────┤             │
│  ...      │   [Deploy] ← Valider les flows    │             │
└─────────────────────────────────────────────────────────────┘

Dashboard : http://localhost:1880/ui
```

---

## 2️⃣ — Les nœuds essentiels

### Nœuds d'entrée (input nodes)

```
inject      → Envoie un message manuellement ou à intervalles réguliers
mqtt in     → Reçoit les messages d'un topic MQTT
http in     → Reçoit des requêtes HTTP
timestamp   → Injecte l'heure courante (via inject)
```

### Nœuds de traitement

```
function    → Code JavaScript personnalisé pour transformer msg
json        → Convertit string JSON ↔ objet JavaScript
change      → Modifie ou crée des propriétés de msg sans code
switch      → Routage conditionnel selon la valeur de msg
rbe         → Report-By-Exception : ne laisse passer que les changements
delay       → Retarde ou limite le débit des messages
```

### Nœuds de sortie

```
debug       → Affiche msg dans le panneau de débogage
mqtt out    → Publie un message sur un topic MQTT
http request → Envoie une requête HTTP vers une API
influxdb out → Écrit un point dans InfluxDB
```

### Nœuds Dashboard (module séparé)

```
gauge       → Jauge (speedometer) pour valeur instantanée
chart       → Graphe linéaire/barre pour historique
text        → Affiche du texte
button      → Bouton d'action
switch      → Interrupteur marche/arrêt
slider      → Curseur de valeur
```

---

**🖼️ ILLUSTRATION 1 — Interface Node-RED avec un flow simple**
> *Légende* : Capture de l'interface Node-RED avec un flow de 5 nœuds. De gauche à droite : nœud "inject" (bouton manuel), nœud "function" (boîte violette "Simuler données"), nœud "gauge" (jauge dashboard), nœud "chart" (graphe dashboard), nœud "debug" (icône bug). Les fils de connexion sont visibles. Le panneau de débogage à droite montre des messages JSON. En dessous, le bouton "Deploy" rouge.
>
> **Prompt illustration** : *"Node-RED editor interface screenshot in French. Flow canvas showing 5 connected nodes left-to-right: blue 'inject' node, purple 'function - Simuler données', teal 'gauge - Température', teal 'chart - Historique', green 'debug'. Orange wire connections between nodes. Right panel 'Débogage' showing JSON messages like '{payload: 23.4, topic: temperature}'. Red 'Deploy' button at top. Palette panel on left with node categories. French labels, dark Node-RED theme"*

---

## 3️⃣ — Le nœud function : transformer les données

### Syntaxe de base

```javascript
// Tout ce qui est dans un nœud function est du JavaScript
// msg = l'objet message entrant
// return msg = renvoyer le message (modifié ou non)

// Exemple 1 : extraire un champ JSON
var data = msg.payload;          // msg.payload = "{\"temp\":23.5}"
// Si msg.payload est un objet JSON déjà parsé (après nœud json) :
msg.payload = data.temperature;  // Extraire seulement la température
return msg;

// Exemple 2 : convertir des unités
msg.payload = (msg.payload * 9/5) + 32;  // Celsius → Fahrenheit
return msg;

// Exemple 3 : enrichir le message
msg.payload = {
    valeur: msg.payload,
    unite: "°C",
    alerte: msg.payload > 30,   // Booléen : true si > 30°C
    horodatage: new Date().toISOString()
};
return msg;

// Exemple 4 : filtrer (ne rien renvoyer si condition)
if (msg.payload < 0 || msg.payload > 100) {
    return null;   // null = ne pas envoyer le message suivant
}
return msg;

// Exemple 5 : envoyer vers plusieurs sorties
// (nœud function configuré avec 2 outputs)
if (msg.payload > 30) {
    return [msg, null];    // Vers output 1 seulement (alerte)
} else {
    return [null, msg];    // Vers output 2 seulement (normal)
}
```

---

## 4️⃣ — Node-RED Dashboard

### Configurer le dashboard

```
Avant d'utiliser les nœuds dashboard, configurer :
  1. Un TAB (onglet de la page web) → ex: "Salle E2"
  2. Des GROUPS (sections dans l'onglet) → ex: "Capteurs", "Historique"
  
  Dans chaque nœud dashboard (gauge, chart...) → assigner à un groupe

URL du dashboard : http://localhost:1880/ui
```

### Nœud Gauge (Jauge)

```
Propriétés importantes :
  Group  : groupe du dashboard où afficher
  Label  : titre de la jauge ("Température")
  Units  : unité affichée ("°C")
  Range  : min/max de l'aiguille (ex: 0 à 50)
  Sectors : zones de couleur (vert/orange/rouge par plage)
  
Format de msg.payload attendu :
  msg.payload = 23.5          ← Nombre simple
  (si c'est une string "23.5" → le gauge l'accepte)
```

### Nœud Chart (Graphe temporel)

```
Propriétés importantes :
  Type  : Line chart / Bar chart / Pie chart
  X-axis : Points à conserver (ex: "Last 60 points")
  Label : Légende de la série
  
Format de msg.payload :
  msg.payload = 23.5          ← Valeur ajoutée avec timestamp automatique
  
Pour plusieurs séries sur le même graphe :
  msg.topic = "Capteur 1"     ← Chaque topic = une série distincte
  msg.payload = 23.5
```

---

**🖼️ ILLUSTRATION 2 — Dashboard Node-RED avec gauge et graphe**
> *Légende* : Capture du dashboard Node-RED (http://localhost:1880/ui) avec un onglet "Salle E2". À gauche, une grande jauge type compteur de vitesse montrant 24.3°C, avec zones verte (0-25°C), orange (25-35°C), rouge (35-50°C). À droite, un graphe linéaire temporel montrant l'évolution de la température sur les 10 dernières minutes (courbe bleue oscillante entre 20 et 28°C). En bas, un texte "Dernière mise à jour : 14:35:22". Fond sombre du dashboard.
>
> **Prompt illustration** : *"Node-RED dashboard screenshot in French. Dark background 'node-red-dashboard' style. Tab labeled 'Salle E2'. Left widget: large speedometer gauge 'Température' showing 24.3°C, green sector 0-25°C, orange 25-35°C, red 35-50°C, needle pointing at 24.3. Right widget: line chart 'Historique Température' showing oscillating blue line between 20-28°C over last 10 minutes, x-axis time labels '14:25' to '14:35'. Bottom: text 'Dernière mise à jour: 14:35:22'. Mobile-responsive layout appearance"*

---

## 5️⃣ — InfluxDB : base de données temporelle

### Pourquoi une BDD temporelle ?

```
PROBLÈME avec SQL (MySQL, PostgreSQL) pour l'IoT :
  → Une table avec 1 000 000 de lignes (mesures toutes les secondes = 11 jours)
  → Requête "température moyenne des 5 dernières minutes" → lente et complexe
  → Pas optimisé pour les données horodatées

SOLUTION InfluxDB :
  → Optimisé pour les séries temporelles (time series)
  → Index sur le timestamp automatiquement
  → Compression des données similaires (ex: 1000 valeurs ~= 1°C)
  → Requêtes temporelles naturelles ("last 5m", "mean over 1h")
  → Rétention configurable (ex: effacer les données > 30 jours)
```

### Structure des données InfluxDB

```
MEASUREMENT (= "table")  : temperature_salle
  │
  ├── TAGS (= labels/index) :
  │     location = "salle_e2"
  │     capteur  = "esp32_01"
  │
  ├── FIELDS (= valeurs) :
  │     temp     = 23.5
  │     humidite = 65.2
  │
  └── TIMESTAMP (automatique) : 2024-05-10T14:35:22Z

Un "POINT" = 1 ligne dans InfluxDB = {tags} + {fields} + timestamp
```

### Langage Flux (InfluxDB 2.x)

```javascript
// Requête Flux — lire les données des 10 dernières minutes
from(bucket: "iot_salle")
  |> range(start: -10m)                           // Période
  |> filter(fn: (r) => r._measurement == "sonde") // Filtrer la table
  |> filter(fn: (r) => r._field == "temperature") // Filtrer le champ
  |> mean()                                        // Calcul optionnel

// Requête pour le graphe historique (dernière heure, une valeur par minute)
from(bucket: "iot_salle")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "sonde")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
```

---

## 6️⃣ — Intégration Node-RED + InfluxDB

### Écriture dans InfluxDB (nœud influxdb out)

```javascript
// Configuration du nœud influxdb out :
//   Server : http://localhost:8086
//   Token  : [token API InfluxDB]
//   Org    : CIEL
//   Bucket : iot_salle

// Le nœud influxdb out attend msg.payload au format :
// Option 1 — format simplifié (pour 1 measurement) :
msg.payload = [
    {
        measurement: "sonde",
        tags: {
            location: "salle_e2",
            capteur: "esp32_01"
        },
        fields: {
            temperature: 23.5,
            humidite: 65.2
        }
        // timestamp est ajouté automatiquement
    }
];
return msg;

// Option 2 — format compact (1 seule valeur) :
// Configurer measurement dans le nœud, envoyer juste la valeur :
msg.payload = 23.5;
return msg;
```

### Lecture depuis InfluxDB (nœud influxdb in)

```javascript
// Configuration nœud influxdb in :
//   Même server/token/org que influxdb out
//   Query : écrire la requête Flux

// La requête peut utiliser des variables Mustache {{topic}} :
msg.query = `
from(bucket: "iot_salle")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "sonde")
  |> filter(fn: (r) => r._field == "temperature")
`;
return msg;

// La sortie est un tableau de points :
// msg.payload = [
//   { _time: "2024-05-10T14:00:00Z", _value: 22.1 },
//   { _time: "2024-05-10T14:01:00Z", _value: 22.3 },
//   ...
// ]
```

---

**🖼️ ILLUSTRATION 3 — Flow complet IoT : ESP32 → MQTT → Node-RED → InfluxDB**
> *Légende* : Flow Node-RED complet en 3 lignes. Ligne 1 (acquisition temps réel) : mqtt-in → json → function "Parser JSON" → [gauge, chart, influxdb-out]. Ligne 2 (alertes) : function "Parser JSON" → switch "temp>30" → [debug "ALERTE", mqtt-out "alerte"]. Ligne 3 (historique) : inject "Toutes les 5min" → influxdb-in "Requête 1h" → chart "Historique InfluxDB". Les fils de connexion sont colorés par type (rouge=alerte, bleu=données, vert=historique).
>
> **Prompt illustration** : *"Node-RED flow diagram in French showing complete IoT pipeline. Three parallel rows: Row 1 'Temps réel': blue 'mqtt in - esp32/temp' → purple 'json' → purple 'function - Parser' → [teal 'gauge Température', teal 'chart Temps réel', orange 'influxdb out']. Row 2 'Alertes': from function output → yellow 'switch T>30°C' → [red 'debug ALERTE', red 'mqtt out - alertes']. Row 3 'Historique': gray 'inject 5min' → orange 'influxdb in - Query 1h' → teal 'chart Historique'. Colored wires. French node labels, Node-RED dark theme"*

---

## 7️⃣ — Architecture complète IoT

```
┌──────────────────────────────────────────────────────────────────┐
│                   STACK IOT COMPLÈTE                             │
│                                                                  │
│  [ESP32]────MQTT────[Broker]────[Node-RED]────[Dashboard Web]    │
│                               │     │                           │
│                               │     └──────[Email/Alerte]       │
│                               │                                  │
│                          [InfluxDB]────[Grafana]                 │
│                          (Stockage)    (Visualisation pro)       │
└──────────────────────────────────────────────────────────────────┘

Chaque brique :
  ESP32          : Acquisition + communication (S6)
  MQTT Broker    : Transport de messages (S6)
  Node-RED       : Orchestration + dashboard simple (S8 ← ICI)
  InfluxDB       : Stockage long terme (S8 ← ICI)
  Grafana        : Dashboard professionnel (bonus S8 / S10)
```

---

## 📌 Les essentiels à retenir

> ✅ **Node-RED** = programmation visuelle par flows · `msg.payload` = la donnée
> ✅ **Deploy** obligatoire pour valider les modifications du flow
> ✅ **Dashboard** : Tab → Group → Widget (gauge, chart, text...)
> ✅ **Gauge** = valeur instantanée · **Chart** = historique · `msg.topic` = nom de série
> ✅ **Function** : JavaScript · `return msg` ou `return null` pour bloquer
> ✅ **InfluxDB** = séries temporelles · measurement + tags + fields + timestamp
> ✅ **Bucket** = base de données InfluxDB 2.x
> ✅ **Flux** = langage de requête InfluxDB (`from → range → filter → mean`)
> ✅ `msg.payload` pour influxdb-out : tableau d'objets `{measurement, tags, fields}`
> ✅ Dashboard URL : **http://localhost:1880/ui**

---

*Fiche de Cours Node-RED + InfluxDB — BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S8*
*Compétences : S5.4 · S5.5 · S5.6 · C5.3 · C3.1*
