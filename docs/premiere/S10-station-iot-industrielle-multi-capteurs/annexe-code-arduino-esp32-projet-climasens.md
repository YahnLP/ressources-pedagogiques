# 💻 CODE ARDUINO ESP32 — PROJET CLIMASENS
## Station Multi-Capteurs · WiFi · MQTT · S10 · 2ᵉ ANNÉE · E2

---

> **Fichier** : `climasens_esp32.ino`
> **Auteur** : ___________________________
> **Date** : ___________________________
> **Groupe** : ___________________________
> **Bibliothèques requises** : WiFi · PubSubClient · DHTesp · ArduinoJson

---

## 📋 Instructions d'installation des bibliothèques

```
Dans Arduino IDE : Tools → Manage Libraries → Install :
  ✓ PubSubClient       by Nick O'Leary      (MQTT)
  ✓ DHTesp             by beegee-tokyo      (DHT22 sur ESP32)
  ✓ ArduinoJson        by Benoit Blanchon   (JSON)
  
Optionnel (si capteur BMP280) :
  ✓ Adafruit BMP280    by Adafruit          (BMP280 I2C)
  ✓ Adafruit Unified Sensor by Adafruit
```

---

## 🟢 CODE COMPLET — `climasens_esp32.ino`

```cpp
/*
 * CLIMASENS - Station IoT Industrielle Multi-Capteurs
 * =====================================================
 * Auteur  : ___________________________
 * Groupe  : ___________________________
 * Date    : ___________________________
 * Version : 1.0
 *
 * Capteurs :
 *   DHT22  → GPIO 4  (Température + Humidité)
 *   MQ-2   → GPIO 34 (Qualité air / Fumée, ADC)
 *   LDR    → GPIO 35 (Luminosité, ADC) [optionnel]
 *   LED    → GPIO 2  (Indicateur statut)
 *
 * Communication :
 *   WiFi 802.11 b/g/n
 *   MQTT → topic "climasens/grpXX/data"
 */

// ═══════════════════════════════════════════════════════
// INCLUSIONS DES BIBLIOTHÈQUES
// ═══════════════════════════════════════════════════════
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHTesp.h>
#include <ArduinoJson.h>

// ═══════════════════════════════════════════════════════
// CONFIGURATION RÉSEAU — À MODIFIER
// ═══════════════════════════════════════════════════════
const char* WIFI_SSID     = "TON_SSID";          // ← Modifier
const char* WIFI_PASSWORD = "TON_PASSWORD";       // ← Modifier
const char* MQTT_BROKER   = "192.168.1.100";      // ← IP du broker
const int   MQTT_PORT     = 1883;
const char* CLIENT_ID     = "CLIMASENS_GRP_XX";  // ← Modifier XX

// ═══════════════════════════════════════════════════════
// TOPICS MQTT
// ═══════════════════════════════════════════════════════
const char* TOPIC_DATA    = "climasens/grpXX/data";     // ← Modifier XX
const char* TOPIC_STATUS  = "climasens/grpXX/status";
const char* TOPIC_ALERTE  = "climasens/grpXX/alerte";

// ═══════════════════════════════════════════════════════
// BROCHES GPIO
// ═══════════════════════════════════════════════════════
const int PIN_DHT    = 4;    // DHT22 — DATA
const int PIN_MQ2    = 34;   // MQ-2  — Sortie analogique (ADC)
const int PIN_LDR    = 35;   // LDR   — Pont diviseur (ADC)
const int PIN_LED    = 2;    // LED de statut

// ═══════════════════════════════════════════════════════
// SEUILS D'ALERTE
// ═══════════════════════════════════════════════════════
const float TEMP_MIN  = 5.0;    // °C — alerte froid
const float TEMP_MAX  = 40.0;   // °C — alerte chaleur
const float HUM_MAX   = 80.0;   // % — alerte humidité élevée
const float HUM_MIN   = 20.0;   // % — alerte humidité faible
const int   AIR_SEUIL = 60;     // % — alerte fumée/gaz

// ═══════════════════════════════════════════════════════
// INTERVALLE DE PUBLICATION
// ═══════════════════════════════════════════════════════
const unsigned long INTERVALLE_PUB = 10000;  // ms (10 secondes)

// ═══════════════════════════════════════════════════════
// OBJETS GLOBAUX
// ═══════════════════════════════════════════════════════
DHTesp          dht;
WiFiClient      wifiClient;
PubSubClient    mqtt(wifiClient);
unsigned long   dernierePub = 0;

// ═══════════════════════════════════════════════════════
// STRUCTURES DE DONNÉES
// ═══════════════════════════════════════════════════════
struct Mesures {
  float temperature;
  float humidite;
  int   air;        // 0-100% (valeur relative)
  int   luminosite; // 0-100%
  bool  valide;     // true si lecture OK
};

// ═══════════════════════════════════════════════════════
// FONCTIONS DE LECTURE DES CAPTEURS
// ═══════════════════════════════════════════════════════

/**
 * Lire le DHT22 (Température + Humidité)
 * Retourne les valeurs dans la structure mesures
 */
void lireDHT22(Mesures &m) {
  TempAndHumidity data = dht.getTempAndHumidity();
  
  if (dht.getStatus() == DHTesp::ERROR_NONE) {
    m.temperature = data.temperature;
    m.humidite    = data.humidity;
    m.valide      = true;
    Serial.printf("DHT22 → Temp: %.1f°C · Hum: %.0f%%\n",
                  m.temperature, m.humidite);
  } else {
    Serial.println("⚠️ DHT22 : Erreur de lecture !");
    m.temperature = NAN;
    m.humidite    = NAN;
    m.valide      = false;
  }
}

/**
 * Lire le MQ-2 (Qualité Air / Fumée)
 * Conversion ADC 12 bits (0-4095) → pourcentage (0-100%)
 */
void lireMQ2(Mesures &m) {
  int rawADC = analogRead(PIN_MQ2);
  m.air      = map(rawADC, 0, 4095, 0, 100);  // Conversion en %
  Serial.printf("MQ-2   → Air: %d%% (ADC: %d)\n", m.air, rawADC);
}

/**
 * Lire la LDR (Luminosité)
 * Pont diviseur : LDR en série avec 10kΩ
 * Plus la luminosité est forte → résistance LDR baisse → tension monte
 */
void lireLDR(Mesures &m) {
  int rawADC   = analogRead(PIN_LDR);
  m.luminosite = map(rawADC, 0, 4095, 0, 100);
  Serial.printf("LDR    → Luminosité: %d%%\n", m.luminosite);
}

// ═══════════════════════════════════════════════════════
// VÉRIFICATION DES ALERTES
// ═══════════════════════════════════════════════════════

/**
 * Vérifier si les mesures déclenchent des alertes
 * Publie sur TOPIC_ALERTE si nécessaire
 */
void verifierAlertes(const Mesures &m) {
  String alerte = "";
  
  if (m.valide) {
    if (m.temperature <= TEMP_MIN)
      alerte = "❄️ ALERTE FROID : " + String(m.temperature, 1) + "°C";
    else if (m.temperature >= TEMP_MAX)
      alerte = "🔥 ALERTE CHALEUR : " + String(m.temperature, 1) + "°C";
    else if (m.humidite >= HUM_MAX)
      alerte = "💧 ALERTE HUMIDITÉ ÉLEVÉE : " + String(m.humidite, 0) + "%";
    else if (m.humidite <= HUM_MIN)
      alerte = "🏜️ ALERTE HUMIDITÉ FAIBLE : " + String(m.humidite, 0) + "%";
  }
  
  if (m.air >= AIR_SEUIL)
    alerte = "⚠️ ALERTE FUMÉE/GAZ : " + String(m.air) + "%";
  
  if (alerte != "") {
    mqtt.publish(TOPIC_ALERTE, alerte.c_str());
    Serial.println("🚨 " + alerte);
    // Faire clignoter la LED d'alerte
    for (int i = 0; i < 3; i++) {
      digitalWrite(PIN_LED, HIGH); delay(200);
      digitalWrite(PIN_LED, LOW);  delay(200);
    }
  }
}

// ═══════════════════════════════════════════════════════
// PUBLICATION MQTT
// ═══════════════════════════════════════════════════════

/**
 * Construire et publier le payload JSON sur TOPIC_DATA
 * Format : {"temperature":23.5,"humidite":65,"air":12,"luminosite":75,"alerte":false}
 */
void publierDonnees(const Mesures &m) {
  // Créer le document JSON (capacité 200 octets)
  StaticJsonDocument<200> doc;
  
  // Remplir les champs
  if (m.valide) {
    doc["temperature"] = serialized(String(m.temperature, 1));
    doc["humidite"]    = m.humidite;
  } else {
    doc["temperature"] = nullptr;
    doc["humidite"]    = nullptr;
  }
  doc["air"]        = m.air;
  doc["luminosite"] = m.luminosite;
  doc["alerte"]     = (m.air >= AIR_SEUIL ||
                       (m.valide && (m.temperature >= TEMP_MAX ||
                                     m.temperature <= TEMP_MIN ||
                                     m.humidite >= HUM_MAX ||
                                     m.humidite <= HUM_MIN)));
  doc["uptime"]     = millis() / 1000;  // Secondes depuis démarrage
  
  // Sérialiser en string
  char jsonBuffer[256];
  serializeJson(doc, jsonBuffer);
  
  // Publier
  if (mqtt.publish(TOPIC_DATA, jsonBuffer)) {
    Serial.println("📤 Publié : " + String(jsonBuffer));
  } else {
    Serial.println("✗ Erreur publication MQTT");
  }
}

// ═══════════════════════════════════════════════════════
// CONNEXION WiFi
// ═══════════════════════════════════════════════════════
void connecterWiFi() {
  Serial.print("Connexion WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  
  int tentatives = 0;
  while (WiFi.status() != WL_CONNECTED && tentatives < 30) {
    delay(500); Serial.print(".");
    tentatives++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\n✓ WiFi connecté : " + WiFi.localIP().toString());
    digitalWrite(PIN_LED, HIGH);  // LED allumée = connecté
  } else {
    Serial.println("\n✗ Échec WiFi — redémarrage dans 5s");
    delay(5000);
    ESP.restart();
  }
}

// ═══════════════════════════════════════════════════════
// CONNEXION MQTT
// ═══════════════════════════════════════════════════════
void connecterMQTT() {
  mqtt.setServer(MQTT_BROKER, MQTT_PORT);
  
  while (!mqtt.connected()) {
    Serial.print("Connexion MQTT → ");
    
    // LWT (Last Will Testament) : publié si l'ESP32 se déconnecte brutalement
    if (mqtt.connect(CLIENT_ID,
                     TOPIC_STATUS, 0,  // LWT topic, QoS
                     true,             // LWT retain
                     "offline")) {
      Serial.println("✓ Connecté au broker !");
      mqtt.publish(TOPIC_STATUS, "online", true);  // Annonce en ligne
    } else {
      Serial.print("Échec rc=");
      Serial.print(mqtt.state());
      Serial.println(" → 5s");
      delay(5000);
    }
  }
}

// ═══════════════════════════════════════════════════════
// SETUP — Initialisation
// ═══════════════════════════════════════════════════════
void setup() {
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("=================================");
  Serial.println("  CLIMASENS v1.0 — Démarrage");
  Serial.println("=================================");
  
  // Broches
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);
  
  // DHT22
  dht.setup(PIN_DHT, DHTesp::DHT22);
  Serial.println("DHT22 initialisé sur GPIO " + String(PIN_DHT));
  
  // Analogique ESP32 — atténuation 11 dB pour full range 0-3.3V
  analogSetAttenuation(ADC_11db);
  
  // Connexions
  connecterWiFi();
  connecterMQTT();
  
  Serial.println("✓ Système prêt !");
}

// ═══════════════════════════════════════════════════════
// LOOP — Boucle principale
// ═══════════════════════════════════════════════════════
void loop() {
  // Maintenir la connexion MQTT
  if (!mqtt.connected()) {
    if (WiFi.status() != WL_CONNECTED) connecterWiFi();
    connecterMQTT();
  }
  mqtt.loop();
  
  // Publication périodique
  unsigned long maintenant = millis();
  if (maintenant - dernierePub >= INTERVALLE_PUB) {
    dernierePub = maintenant;
    
    // Lire tous les capteurs
    Mesures m;
    lireDHT22(m);
    lireMQ2(m);
    lireLDR(m);
    
    // Vérifier les alertes
    verifierAlertes(m);
    
    // Publier les données
    publierDonnees(m);
    
    Serial.println("───────────────────────────────");
  }
}
```

---

## 🔌 Schéma de câblage (description textuelle)

```
ESP32 DevKit v1 — Connexions :

GPIO 4  → DATA DHT22 (+ résistance 10kΩ entre DATA et 3V3)
GPIO 34 → AO du MQ-2  (lecture analogique 0-3.3V)
GPIO 35 → Point milieu pont diviseur LDR (LDR + 10kΩ vers GND)
GPIO 2  → LED avec résistance 220Ω vers GND

Alimentation :
  3V3 → VCC DHT22 · VCC LDR
  5V  → VCC MQ-2 (chauffage interne nécessite 5V)
  GND → GND de tous les composants

⚠️ Le MQ-2 consomme ~150mA — ne pas alimenter directement depuis GPIO !
   Utiliser la broche 5V (USB) de la carte ESP32.
⚠️ Les GPIO 34, 35 sont INPUT ONLY (pas de sortie possible).
```

---

## 🧩 Variante simulateur (sans matériel)

```cpp
// Remplacer les fonctions lireDHT22(), lireMQ2(), lireLDR()
// par ce simulateur pour tester sans capteurs :

void simulerMesures(Mesures &m) {
  static float baseTemp = 22.0;
  static float baseHum  = 60.0;
  
  // Drift lent + bruit gaussien
  baseTemp += (random(-5, 5)) / 10.0;
  baseTemp  = constrain(baseTemp, 15.0, 35.0);
  
  baseHum  += (random(-3, 3)) / 10.0;
  baseHum   = constrain(baseHum, 30.0, 90.0);
  
  m.temperature = baseTemp;
  m.humidite    = baseHum;
  m.air         = random(5, 30);      // Valeur normale
  m.luminosite  = random(40, 90);
  m.valide      = true;
  
  // Simuler une alerte MQ-2 toutes les 50 cycles
  static int cycles = 0;
  if (++cycles % 50 == 0) m.air = 75;  // Dépasser le seuil
}
```

---

*Code Arduino CLIMASENS — BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S10*
*À déposer dans le dossier technique du portfolio*
