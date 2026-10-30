"""Première S08 : réponses des exercices Node-RED / InfluxDB."""
F = '03-exercices.md'
E = lambda t, l: ('premiere', 'S08', F, t, l)
ENTREES = [
    E('## 📐 EXERCICE 1', [
        "**Q1.1** — `msg.payload = msg.payload.temp;`  ",
        "**Q1.2** — `celsius : Math.round(celsius * 10) / 10,` et `fahrenheit : Math.round((celsius * 9 / 5 + 32) * 10) / 10,` (par exemple 24,3 °C → 75,7 °F).  ",
        "**Q1.3** — `if (valeur < 0 || valeur > 100) { return null; }` : en renvoyant `null`, le message n'est pas transmis.  ",
        "**Q1.4** — `if (co2 > 1000) {`"]),
    E('## 📐 EXERCICE 2', [
        "**Q2.1** — Lire depuis le **bucket** (base) `iot_salle` ; période : les **30 dernières minutes** ; filtrer la table de mesure `sonde_salle_e2` ; filtrer le champ `temperature` ; calculer la **moyenne**. Résultat : un seul nombre = la **température moyenne des 30 dernières minutes**.  ",
        "**Q2.2** — `from(bucket: \"iot_salle\") |> range(start: -1h) |> filter(fn: (r) => r._measurement == \"salle_e2\") |> filter(fn: (r) => r._field == \"humidite\") |> max()`  ",
        "**Q2.3** — `range(start: -3h)` et `aggregateWindow(every: 5m, fn: mean, createEmpty: false)`.  ",
        "**Q2.4** — **Tag** : étiquette **indexée** (texte) qui décrit la source ; sert à **filtrer et regrouper** rapidement ; exemple : `site=salle_e2`. **Field** : valeur **mesurée** (non indexée) ; contient le nombre à analyser ; exemple : `temperature=24.3`."]),
    E('## 📐 EXERCICE 3', [
        "**Q3.1** — Topics acceptés : `serre/1/data`, `serre/nord/data`, `serre/est/data` (le `+` remplace **un seul niveau**). Non accepté : `serre/nord/zone2/data` (deux niveaux) ou `serre/data`.  ",
        "**Q3.2** — Sans nœud json : `msg.payload` est de type **chaîne de caractères (string)** ; avec le nœud json : c'est un **objet JavaScript**, donc `msg.payload.temperature` est accessible.  ",
        "**Q3.3** — Règle 1 (> 35) : **vrai** → routage vers **Output 1** → nœud `debug « ALERTE CHALEUR »`.  ",
        "**Q3.4** — Envoyer **aussi** les sorties 1 et 2 vers le nœud `influxdb out` (ou placer `influxdb out` en parallèle, juste après le nœud function, avant le switch). Ainsi toutes les données sont sauvegardées, et le switch ne sert plus qu'à déclencher les alertes."]),
]
