# 🗂️ AIDE-MÉMOIRE ESP32 WiFi · WebServer · MQTT — À PLASTIFIER
## Modes STA/AP · HTTP · Pub/Sub · BAC PRO CIEL · E2 · 2ᵉ année S6

---

> *Conserver à côté du clavier pendant les TP Arduino ESP32*

---

## 📡 Modes WiFi

```cpp
// Mode STA (Station) — client du réseau
WiFi.begin("SSID", "password");
while (WiFi.status() != WL_CONNECTED) { delay(500); }
Serial.println(WiFi.localIP());   // IP obtenue par DHCP

// Mode AP (Access Point) — crée un réseau
WiFi.mode(WIFI_AP);
WiFi.softAP("ESP32_Config", "mdp8car");
// IP fixe : 192.168.4.1

// Mode STA + AP simultané
WiFi.mode(WIFI_AP_STA);
WiFi.softAP(ap_ssid, ap_pass);
WiFi.begin(sta_ssid, sta_pass);
```

---

## 🌐 WebServer embarqué

```cpp
#include <WebServer.h>
WebServer server(80);

// Enregistrer les routes
server.on("/",     handler);      // GET /
server.on("/data", handler2);     // GET /data
server.onNotFound(handler404);    // 404

server.begin();

// ⚠️ OBLIGATOIRE dans loop() :
server.handleClient();

// Envoyer une réponse :
server.send(200, "text/html", "<h1>OK</h1>");
server.send(302, "text/plain", "");  // Redirection

// Codes importants :
// 200 = OK  ·  302 = Redirect  ·  404 = Not Found
```

---

## 📨 MQTT (PubSubClient)

```cpp
#include <PubSubClient.h>
WiFiClient wClient;
PubSubClient mqtt(wClient);

// Setup
mqtt.setServer("broker.hivemq.com", 1883);
mqtt.setCallback(onMessage);
mqtt.connect("CLIENT_ID_UNIQUE");  // ← UNIQUE par ESP32 !
mqtt.subscribe("mon/topic");

// Publier
mqtt.publish("mon/topic", "valeur");

// Callback réception
void onMessage(char* topic, byte* payload, unsigned int len) {
  String msg = "";
  for (int i = 0; i < len; i++) msg += (char)payload[i];
  // Traiter msg...
}

// ⚠️ OBLIGATOIRE dans loop() :
if (!mqtt.connected()) reconnect();
mqtt.loop();
```

---

## 📌 Topics MQTT

```
Format : "projet/zone/appareil/mesure"
  "serre/bat1/esp01/temperature"
  "serre/bat1/esp01/led/commande"

Wildcards :
  "serre/+/esp01/temp"  → + = 1 niveau
  "serre/#"             → # = tout le reste
```

---

## ⚡ QoS MQTT

```
0 = Fire & forget (plus rapide, peut être perdu)
1 = At least once  (recommandé IoT standard)
2 = Exactly once   (critique, lent)
```

---

## ⚠️ Erreurs fréquentes

```
❌ Client ID identique → 2 ESP32 se déconnectent mutuellement
❌ mqtt.loop() oublié → aucun message reçu
❌ server.handleClient() oublié → WebServer ne répond plus
❌ delay() dans loop() → bloque mqtt.loop() → utiliser millis()
❌ while(status == WL_CONNECTED) → condition inversée !
                   doit être  != WL_CONNECTED
❌ GPIO 2 parfois en logique inversée selon la carte
```

---

## 🔧 Brokers MQTT disponibles

```
Public (test) :
  broker.hivemq.com  port 1883
  test.mosquitto.org port 1883

Local Mosquitto :
  sudo apt install mosquitto
  mosquitto_sub -h localhost -t "mon/topic" -v
  mosquitto_pub -h localhost -t "mon/topic" -m "ON"
```

---

*Aide-Mémoire ESP32 WiFi/MQTT — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S6*
*Compétences S5.1 · S5.2 · S5.3 · C5.1 · C5.2*
