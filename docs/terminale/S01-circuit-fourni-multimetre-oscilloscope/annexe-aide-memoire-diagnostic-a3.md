# 🗂️ AIDE-MÉMOIRE DIAGNOSTIC A3 — À PLASTIFIER
## Synthèse E2 Complète · Formules · Raccourcis · BAC PRO CIEL · E2 · 3ᵉ année S1

---

> *Conserver toute l'année · Mise à jour possible en A3*

---

## 🖥️ KiCad — Flux et règles

```
Schéma→ERC→Empreintes→PCB→Edge.Cuts→Placement→Routage→DRC→Gerber

F.Cu=rouge · B.Cu=bleu · Edge.Cuts=jaune · Via: 0,8mm/0,4mm
Clearance≥0,2mm · Signal 0,35mm · Alim 0,8mm
Découplage : 100nF + 10µF au plus proche du CI (<2mm)
```

---

## 📡 ESP32 Raccourcis

```cpp
// STA
WiFi.begin(ssid,pass);
while(WiFi.status()!=WL_CONNECTED){delay(500);}

// AP → IP = 192.168.4.1
WiFi.mode(WIFI_AP);  WiFi.softAP(ssid,pass);

// WebServer
server.on("/r",h);  server.handleClient();// loop() !

// MQTT
mqtt.connect("ID_UNIQUE");
mqtt.subscribe(t);  mqtt.publish(t,m);
mqtt.loop();  // loop() OBLIGATOIRE !
```

---

## 🔵 Node-RED

```javascript
// Extraire un champ JSON
msg.payload = msg.payload.temperature;

// Chart multi-séries → msg.topic = "NomSérie"

// InfluxDB format
msg.payload = [{
  measurement:"table",
  tags:{loc:"salle"},
  fields:{temp:parseFloat(val)}
}];

// Requête Flux
from(bucket:"b")|>range(start:-1h)
  |>filter(fn:(r)=>r._field=="temp")
  |>aggregateWindow(every:10m,fn:mean,createEmpty:false)
```

---

## 🔧 Fiabilité

```
λ = 1/MTBF    D = MTBF/(MTBF+MTTR)    R(t) = e^(−λt)
R(MTBF) = e⁻¹ = 0,368 = 36,8% ← JAMAIS 50% !
Série    : Rs = R1×R2×R3   (affaiblit)
Parallèle: Rs = 1−(1−R1)(1−R2)   (renforce)

e⁻⁰·¹=0,905  e⁻⁰·²=0,819  e⁻⁰·⁵=0,607  e⁻¹=0,368
1 an = 8760 h · 1 mois = 730 h
```

---

## 📻 CEM

```
Source→Couplage→Victime
4 couplages : Résistif · Capacitif · Inductif · Rayonné
Conduit < 30MHz · Rayonné > 30MHz
Fente max = λ/20  (λ=3×10⁸/f)
  Ex: 2,4GHz → λ=0,125m → fente<6,25mm
fc = 1/(2π×R×C)
Plan CONTINU → petite boucle → peu de rayonnement ✓
Plan FENDU   → grande boucle → fort rayonnement   ✗
```

---

## 📏 Métrologie

Biais = Σei/n  

$$σ = \sqrt(Σ\dfrac{ei^2}{n-1})$$

u = σ/√n  
U = 2u  (95% conf.)  
Conformité : |biais| + U ≤ spécif.  

---

## 🚨 Les 10 pièges E2

```
1.  R(MTBF) ≠ 50% → 36,8% (e⁻¹)
2.  Série Rs < Rmin (pas la moyenne)
3.  mqtt.loop() oublié → pas de réception
4.  handleClient() oublié → WebServer mort
5.  Client ID MQTT dupliqué → déconnexion
6.  delay() dans loop() → bloque mqtt.loop()
7.  Plan de masse fendu → antenne
8.  Condensateur découplage loin du CI
9.  while(status == WL_CONNECTED) → inversé !
10. |biais|+U pour conformité (pas biais seul)
```

---

## 📚 Ressources par thème A2

```
PCB/KiCad   → S1/S3/S4-2A_E2_03
ESP32/MQTT  → S6-2A_E2_03+04
Node-RED    → S8-2A_E2_02+03
Fiabilité   → S11-2A_E2_03+04
CEM         → S13-2A_E2_03+04
Métrologie  → S17-2A_E2_04+05
```

---

*Aide-Mémoire Diagnostique A3 — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S1*
