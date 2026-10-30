# 🔬 EXERCICES PRATIQUES — S8 · 2ᵉ ANNÉE · E2
## Node-RED Function · InfluxDB Flux · Flows Avancés

---

> **Nom** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Date** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Format** : Exercices complémentaires · Fiche de cours autorisée

---

## 📐 EXERCICE 1 — Nœud function JavaScript (20 min)

> Le nœud function est le couteau suisse de Node-RED. Maîtriser les transformations basiques de `msg.payload` est essentiel.

**Q1.1** — Voici la sortie d'un ESP32 via MQTT (payload = string JSON) :

```
msg.payload = '{"temp": 24.3, "hum": 67, "co2": 512, "device": "esp32-01"}'
```

Écris le code du nœud function qui place **seulement la température** dans `msg.payload` :

```javascript
// Note : on suppose que le nœud [json] précédent a déjà parsé la string
// donc msg.payload est déjà un objet JavaScript

msg.payload = _______________________________________________________;
return msg;
```

**Q1.2** — Écris le code d'un nœud function qui :

- Convertit la température de Celsius en Fahrenheit (`F = C × 9/5 + 32`)
- Arrondit au dixième
- Crée un objet avec les deux valeurs

```javascript
var celsius = msg.payload;   // nombre en entrée

msg.payload = {
    celsius    : ______________________________,
    fahrenheit : ______________________________,
    source     : msg.topic
};
return msg;
```

**Q1.3** — Écris un nœud function qui **bloque le message** si la valeur est hors plage [0..100] :

```javascript
var valeur = msg.payload;

// Si hors plage, ne pas envoyer le message suivant
if (________________________________) {
    return _______;   // Bloquer
}

// Sinon, laisser passer
return msg;
```

**Q1.4** — Écris un nœud function avec **2 sorties** :

- Sortie 1 → Si CO₂ > 1000 ppm (qualité d'air mauvaise)
- Sortie 2 → Sinon (qualité normale)

```javascript
var co2 = msg.payload.co2;

if (____________) {
    msg.payload = "⚠️ CO₂ élevé : " + co2 + " ppm";
    return [msg, null];   // Sortie 1
} else {
    msg.payload = "✓ CO₂ normal : " + co2 + " ppm";
    return [null, msg];   // Sortie 2
}
```

---

## 📐 EXERCICE 2 — Requêtes InfluxDB Flux (20 min)

**Q2.1** — Identifie les éléments de cette requête Flux :

```javascript
from(bucket: "iot_salle")
  |> range(start: -30m)
  |> filter(fn: (r) => r._measurement == "sonde_salle_e2")
  |> filter(fn: (r) => r._field == "temperature")
  |> mean()
```

```
from(bucket: "iot_salle")      → Lire depuis : ________________________________
range(start: -30m)             → Période : ____________________________________
filter _measurement == ...     → Filtrer la table : ____________________________
filter _field == "temperature" → Filtrer le champ : ____________________________
mean()                         → Calculer : ____________________________________
Résultat : un seul nombre = ___________________________________________________
```

**Q2.2** — Écris une requête Flux pour obtenir **l'humidité maximale** sur la **dernière heure** dans la sonde "salle_e2" :

```javascript
from(bucket: "_____________")
  |> range(start: __________)
  |> filter(fn: (r) => r._measurement == "________________")
  |> filter(fn: (r) => r._field == "________________")
  |> ____________()
```

**Q2.3** — Écris une requête Flux pour obtenir la **moyenne de température par tranche de 5 minutes** sur les **3 dernières heures** :

```javascript
from(bucket: "iot_salle")
  |> range(start: ________)
  |> filter(fn: (r) => r._measurement == "sonde_salle_e2")
  |> filter(fn: (r) => r._field == "temperature")
  |> aggregateWindow(every: ________, fn: ________, createEmpty: false)
```

**Q2.4** — Quelle est la différence entre un **Tag** et un **Field** dans InfluxDB ?

```
Tag   : ________________________________________________________________________
       Peut être utilisé pour : __________________________________________________
       Exemple : _________________________________________________________________

Field : ________________________________________________________________________
       Contient : _______________________________________________________________
       Exemple : _________________________________________________________________
```

---

## 📐 EXERCICE 3 — Analyser un flow Node-RED (15 min)

> Voici la description d'un flow Node-RED. Réponds aux questions.

```
FLOW "SURVEILLANCE_SERRE" :
  Nœud 1 : [mqtt in] topic="serre/+/data" · broker=localhost
  Nœud 2 : [json] (parse le payload string → objet)
  Nœud 3 : [function "Extraire champs"] 
  Nœud 4 : [switch "Alerte T°"]  property=msg.payload.temperature
             Règle 1 : > 35 → Output 1
             Règle 2 : < 10 → Output 2
             Règle 3 : otherwise → Output 3
  Nœud 5 (Output 1) : [debug "ALERTE CHALEUR"]
  Nœud 6 (Output 2) : [debug "ALERTE FROID"]
  Nœud 7 (Output 3) : [influxdb out] measurement=serre_data
```

**Q3.1** — Le topic `"serre/+/data"` utilise le wildcard `+`. Quels topics serait-il possible de recevoir ?

```
Exemples de topics acceptés :
  ___________________________________________
  ___________________________________________
  ___________________________________________

Topic qui ne serait PAS accepté : ________________________________________
```

**Q3.2** — Pourquoi le nœud [json] est-il nécessaire avant le nœud [function] ?

```
Sans nœud json : msg.payload est de type _____________ → impossible d'accéder à msg.payload.temperature
Avec nœud json : msg.payload est de type _____________ → accès aux champs possible
```

**Q3.3** — Si un message arrive avec temperature=38.5, vers quel nœud de sortie est-il routé ? Justifie.

```
Température = 38.5
Règle 1 (> 35) : ☐ Vrai ☐ Faux → _____________
Routage vers Output : _______
Nœud de sortie : _______
```

**Q3.4** — Dans ce flow, les données normales (températures entre 10 et 35°C) sont envoyées vers InfluxDB.
Mais les données d'alerte **ne sont pas sauvegardées** dans InfluxDB. Propose une modification pour tout sauvegarder :

```
Solution : __________________________________________________________________
Modification du flow : ______________________________________________________
```

---

## 📐 EXERCICE 4 — Comparer les outils (10 min)

**Q4.1** — Pour chaque besoin, indique quel outil utiliser : ESP32, MQTT, Node-RED ou InfluxDB :

```
Mesurer la température toutes les 10 secondes : ____________________
Transporter le message de la serre vers le serveur : ____________________
Afficher la température en temps réel sur un écran : ____________________
Calculer la moyenne mensuelle de température : ____________________
Déclencher une alerte si T° > 35°C : ____________________
Stocker 6 mois d'historique de mesures : ____________________
Piloter un ventilateur via une commande distante : ____________________
```

**Q4.2** — Node-RED peut-il remplacer InfluxDB pour le stockage long terme ? Justifie.

```
☐ Oui ☐ Non
Justification : _________________________________________________________________
________________________________________________________________________________
```

**Q4.3** — Cite un avantage de la programmation visuelle (Node-RED) par rapport à un programme Python pour les mêmes tâches :

```
Avantage 1 : __________________________________________________________________
Avantage 2 : __________________________________________________________________
Limite de Node-RED vs Python : ________________________________________________
```

---
