# 🗂️ AIDE-MÉMOIRE CCF E2 — TOUTES LES FORMULES
## Révisions Complètes · À PLASTIFIER · BAC PRO CIEL · E2 · 2ᵉ année S15

---

## 🖥️ KiCad — Raccourcis essentiels

```
A = Ajouter symbole    P = Alimentation (+5V, GND, PWR_FLAG)
W = Fil                E = Éditer propriétés    R = Rotation
X = Tracer piste       V = Via (changer calque)
G = Déplacer avec fils F = Flip (retourner composant)
B = Remplir zones (plan de masse)   Alt+3 = Vue 3D
Deploy = valider flows Node-RED     Ctrl+S = Sauvegarder

Calques : F.Cu (rouge) · B.Cu (bleu) · Edge.Cuts (jaune/contour)
Règles  : Clearance ≥ 0,2mm · Signal 0,35mm · Alim 0,8mm
Via     : Ø ext 0,8mm · perçage 0,4mm
```

---

## 📡 ESP32 WiFi

```cpp
// Mode STA
WiFi.begin(ssid, pass);
while (WiFi.status() != WL_CONNECTED) { delay(500); }
Serial.println(WiFi.localIP());

// Mode AP
WiFi.mode(WIFI_AP);
WiFi.softAP(ssid, pass);  // IP = 192.168.4.1

// WebServer
server.on("/route", handler);
server.handleClient();  // ← dans loop() OBLIGATOIRE
```

---

## 📨 MQTT

```cpp
mqtt.setServer(broker, 1883);
mqtt.setCallback(onMessage);
mqtt.connect("CLIENT_ID_UNIQUE");  // ← UNIQUE !
mqtt.subscribe(topic);
mqtt.publish(topic, payload.c_str());
mqtt.loop();  // ← dans loop() OBLIGATOIRE

Topics : "projet/zone/appareil/mesure"
Wildcards : "salle/+/temp" (+= 1 niveau) · "salle/#" (#= tout)
QoS 0=fire&forget · 1=at least once · 2=exactly once
```

---

## 🔵 Node-RED

```javascript
// Nœud function — extraire un champ JSON :
msg.payload = msg.payload.temperature;
return msg;

// Chart multi-séries :
msg.topic = "NomDeLaSérie";
msg.payload = valeur;

// Format InfluxDB :
msg.payload = [{
  measurement: "nom_table",
  tags: { localisation: "salle" },
  fields: { temp: parseFloat(val) }
}];

Requête Flux :
from(bucket:"nom") |> range(start:-1h)
  |> filter(fn:(r)=>r._measurement=="table")
  |> filter(fn:(r)=>r._field=="temp")
  |> mean()
```

---

## 🔧 Fiabilité

```
λ = 1/MTBF         MTBF = TO/n      MTTR = TA/n
D = MTBF/(MTBF+MTTR)
R(t) = e^(−λt)     F(t) = 1−R(t)

À t=MTBF : R = e⁻¹ ≈ 0,368 (36,8%)

Série    : Rs = R1×R2×R3   λs = λ1+λ2+λ3
Parallèle: Rs = 1−(1−R1)(1−R2)

Valeurs e :
e⁻⁰·¹=0,905  e⁻⁰·²=0,819  e⁻⁰·³=0,741
e⁻⁰·⁵=0,607  e⁻¹=0,368    e⁻²=0,135

1 an = 8760 h · 1 mois = 730 h
```

---

## 📻 CEM

```
Source → Couplage → Victime
4 types : résistif · capacitif · inductif · rayonné

Conduit  < 30 MHz (câbles)
Rayonné  > 30 MHz (ondes)

Blindage : continu + masse · fente < λ/20
  λ = 3×10⁸/f  Ex: 2,4GHz → λ=12,5cm → fente < 6,25mm

Découplage : 100nF+10µF au plus proche du CI (<1mm)
Ferrite : absorbe énergie HF sur câbles

Plan de masse : CONTINU → petite boucle → peu de rayonnement
                FENDU → détour → grande boucle → fort rayonnement !

Filtre RC : fc = 1/(2π×R×C)
Séparer masse analogique et masse numérique → point de jonction unique
GND ≠ Terre (PE)
```

---

## ⚠️ Les 10 pièges fatals CCF E2

```
1.  DRC non lancé → violations cachées
2.  ERC non lancé → connexions fantômes
3.  mqtt.loop() oublié → pas de réception MQTT
4.  server.handleClient() oublié → WebServer muet
5.  Client ID MQTT identique → déconnexion en boucle
6.  MTBF ≠ durée de vie : R(MTBF) = 36,8% seulement !
7.  Série : Rs < Rmin (pas la moyenne !)
8.  Parallèle : Rs = 1−(1−R1)(1−R2) pas R1×R2
9.  Plan de masse fendu → antenne → interdit
10. Condensateur découplage loin → inductance piste → filtre inefficace
```

---

*Aide-Mémoire CCF E2 — À PLASTIFIER · Toutes formules*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S15*
