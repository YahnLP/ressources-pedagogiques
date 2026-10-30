# 🛠️ GUIDE TECHNIQUE — PROJET A2
## Industrie 4.0 : Architecture, Code ESP32, MTBF, Dashboard CloudWatch

**Équipe : ________________  Sujet : ___**

---

> **Mode d'emploi :** Ce guide compile les références techniques dont vous avez besoin pour le projet. Vous êtes libres de l'adapter à votre sujet — il propose des points de départ, pas des solutions imposées.

---

## 1️⃣ ÉTAPE 1 — ARCHITECTURE (Phase 1, 30 min)

### Diagramme bloc à produire

> [!NOTE] VOTRE ARCHITECTURE
>
> [Capteur 1]  
> nom:_____  ─── I2C / GPIO ─── [ESP32]  ─── Wi-Fi ───► [AWS IoT]  
> grandeur:__                     │                          │  
>                             [LED]                    [IoT Rule]  
> [Capteur 2]                  [Relay/actuateur]             │  
> nom:_____  ─── GPIO ─────────                         [CloudWatch]  
> grandeur:__                                                │  
>                                                      [SNS/SMS]  

### Tableau de décisions techniques (à remplir au démarrage)

| **Décision** | **Option choisie** | **Justification** |
|---|---|---|
| Protocole capteur | I2C / SPI / GPIO analogique / UART | |
| Fréquence de publication | 5s / 10s / 30s | |
| QoS MQTT | 0 / 1 / 2 | |
| Format payload | JSON / CSV / binaire | |
| Indicateur MTBF | Vibration > X / Courant > Y / Niveau < Z | |
| Seuil d'alarme | Valeur choisie + justification | |

---

## 2️⃣ ÉTAPE 2 — CODE ESP32 BASE DE DÉPART

### Code complet commenté (à adapter à votre sujet)

```cpp
/**
 * PROJET A2 — Industrie 4.0
 * Sujet : _______________________
 * Équipe : _______________________
 * 
 * Architecture :
 *   ESP32 → AWS IoT Core (MQTT TLS) → CloudWatch → Alarme SNS
 */

#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
// Adapter selon votre capteur :
// #include <Wire.h>        // Pour I2C (ADXL345, BMP280...)
// #include <DHT.h>         // Pour DHT22
// #include <Adafruit_ADXL345.h>  // Pour accéléromètre

// ── Certificats AWS IoT Core ──────────────────────────────────────────
const char* CA_CERT = R"EOF(
-----BEGIN CERTIFICATE-----
[COLLER AmazonRootCA1.pem]
-----END CERTIFICATE-----
)EOF";

const char* DEVICE_CERT = R"EOF(
-----BEGIN CERTIFICATE-----
[COLLER device-certificate.pem.crt]
-----END CERTIFICATE-----
)EOF";

const char* PRIVATE_KEY = R"EOF(
-----BEGIN RSA PRIVATE KEY-----
[COLLER private.pem.key]
-----END RSA PRIVATE KEY-----
)EOF";

// ── Configuration réseau et AWS ───────────────────────────────────────
const char* SSID         = "NOM_WIFI";
const char* WIFI_PASS    = "MDP_WIFI";
const char* AWS_ENDPOINT = "XXXXX-ats.iot.eu-west-1.amazonaws.com";
const int   MQTT_PORT    = 8883;
const char* CLIENT_ID    = "industech-machine-01";    // Unique par équipe

// ── Topics ─────────────────────────────────────────────────────────────
const char* TOPIC_DATA    = "industech/machine01/capteurs";
const char* TOPIC_STATUS  = "industech/machine01/status";
const char* TOPIC_COMMAND = "industech/machine01/commande";  // Subscribe

// ── Seuils de maintenance prédictive ──────────────────────────────────
// À ADAPTER selon votre sujet :
const float SEUIL_ALERTE   = 2.5;   // Ex: 2.5g pour vibration, 2.0A pour courant
const float SEUIL_CRITIQUE = 4.0;   // Seuil critique → arrêt préventif

// ── Variables globales ─────────────────────────────────────────────────
WiFiClientSecure  tlsClient;
PubSubClient      mqtt(tlsClient);

// Compteur d'alarmes pour MTBF
unsigned int     nbAlarmes    = 0;
unsigned long    tempsDebutMs = 0;
unsigned long    derniereAlarmems = 0;
bool             alarmeActive = false;

// ── Callback : commandes reçues depuis le broker ──────────────────────
void onMessage(char* topic, byte* payload, unsigned int length) {
  String msg = "";
  for (unsigned int i = 0; i < length; i++) msg += (char)payload[i];
  Serial.printf("[%s] Commande reçue : %s\n", topic, msg.c_str());

  if (msg == "RESET_ALARME") {
    alarmeActive = false;
    Serial.println("Alarme réinitialisée par commande distante");
  }
}

// ── Connexion Wi-Fi ───────────────────────────────────────────────────
void connectWiFi() {
  WiFi.begin(SSID, WIFI_PASS);
  Serial.print("Connexion Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); Serial.print(".");
  }
  Serial.printf("\nWi-Fi OK → %s  RSSI: %d dBm\n",
                WiFi.localIP().toString().c_str(), WiFi.RSSI());
}

// ── Connexion AWS IoT ─────────────────────────────────────────────────
void connectAWS() {
  tlsClient.setCACert(CA_CERT);
  tlsClient.setCertificate(DEVICE_CERT);
  tlsClient.setPrivateKey(PRIVATE_KEY);
  mqtt.setServer(AWS_ENDPOINT, MQTT_PORT);
  mqtt.setCallback(onMessage);

  while (!mqtt.connected()) {
    Serial.print("Connexion AWS IoT...");
    // LWT : publier "offline" si déconnexion brutale
    if (mqtt.connect(CLIENT_ID, TOPIC_STATUS, 1, true, "offline")) {
      Serial.println("Connecté !");
      mqtt.publish(TOPIC_STATUS, "online", true);   // Retained
      mqtt.subscribe(TOPIC_COMMAND, 1);
      tempsDebutMs = millis();  // Démarrer le chrono MTBF
    } else {
      Serial.printf("Erreur MQTT %d — nouvel essai dans 5s\n", mqtt.state());
      delay(5000);
    }
  }
}

// ── Lecture capteur(s) — À ADAPTER ────────────────────────────────────
struct MesureCapteur {
  float valeur1;   // Ex: vibration (g), courant (A), niveau (cm)
  float valeur2;   // Ex: température (°C)
  bool  alarme;    // Seuil dépassé ?
};

MesureCapteur lireCapteurs() {
  MesureCapteur m;

  // ── ADAPTER ICI : lecture de votre capteur ──────────────────────────
  // Exemple DHT22 :
  // m.valeur2 = dht.readTemperature();
  //
  // Exemple ADXL345 :
  // sensors_event_t event;
  // accel.getEvent(&event);
  // m.valeur1 = sqrt(event.acceleration.x * event.acceleration.x +
  //                  event.acceleration.y * event.acceleration.y +
  //                  event.acceleration.z * event.acceleration.z);
  //
  // Exemple ADC (ACS712 courant) :
  // int raw = analogRead(34);
  // m.valeur1 = (raw - 2048) * (5.0 / 4096.0) / 0.185;  // ACS712-5A

  // Simulation si pas de capteur réel :
  m.valeur1 = 1.0 + (float)random(0, 30) / 10.0;  // Simulation 1.0–4.0
  m.valeur2 = 25.0 + (float)random(0, 50) / 10.0; // Simulation 25–30°C
  // ───────────────────────────────────────────────────────────────────

  m.alarme = (m.valeur1 > SEUIL_ALERTE);
  return m;
}

// ── Publication MQTT + mise à jour MTBF ──────────────────────────────
void publierMesure(const MesureCapteur& m) {
  // Comptabiliser les nouvelles alarmes pour le MTBF
  if (m.alarme && !alarmeActive) {
    alarmeActive = true;
    nbAlarmes++;
    unsigned long tempsDepuisDerniere = millis() - derniereAlarmems;
    derniereAlarmems = millis();
    Serial.printf("⚠ ALARME #%d — Intervalle depuis la précédente : %.1f min\n",
                  nbAlarmes, tempsDepuisDerniere / 60000.0);
  }
  if (!m.alarme) alarmeActive = false;

  // Calculer MTBF courant (en minutes)
  float mtbf_min = 0;
  if (nbAlarmes > 1) {
    float dureeObs_min = (millis() - tempsDebutMs) / 60000.0;
    mtbf_min = dureeObs_min / nbAlarmes;
  }

  // Construire le payload JSON
  String payload = "{";
  payload += "\"device_id\":\"" + String(CLIENT_ID) + "\",";
  payload += "\"ts\":" + String(millis() / 1000) + ",";
  payload += "\"mesure1\":" + String(m.valeur1, 2) + ",";
  payload += "\"mesure2\":" + String(m.valeur2, 1) + ",";
  payload += "\"alarme\":" + String(m.alarme ? "true" : "false") + ",";
  payload += "\"nb_alarmes\":" + String(nbAlarmes) + ",";
  payload += "\"mtbf_min\":" + String(mtbf_min, 1) + ",";
  payload += "\"heap\":" + String(ESP.getFreeHeap());
  payload += "}";

  bool ok = mqtt.publish(TOPIC_DATA, payload.c_str());
  Serial.printf("%s %s\n", ok ? "✓" : "✗ ERR", payload.c_str());
}

// ── Affichage diagnostic en continu ──────────────────────────────────
void afficherDiag() {
  Serial.println("─── DIAGNOSTIC ───────────────────────────────");
  Serial.printf("RSSI     : %d dBm\n", WiFi.RSSI());
  Serial.printf("MQTT     : %s (state=%d)\n",
                mqtt.connected() ? "Connecté" : "Déconnecté", mqtt.state());
  Serial.printf("Heap     : %d bytes\n", ESP.getFreeHeap());
  Serial.printf("Alarmes  : %d  |  MTBF estimé : %.1f min\n",
                nbAlarmes,
                nbAlarmes > 1 ? (millis() - tempsDebutMs) / 60000.0 / nbAlarmes : 0.0);
  Serial.println("──────────────────────────────────────────────");
}

// ── Setup ─────────────────────────────────────────────────────────────
void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);   // LED de statut

  // Initialiser le(s) capteur(s) ici :
  // dht.begin();
  // Wire.begin();
  // accel.begin();

  connectWiFi();
  connectAWS();
  Serial.println("Système démarré — publication toutes les 5s");
}

// ── Loop ──────────────────────────────────────────────────────────────
void loop() {
  if (!mqtt.connected()) connectAWS();
  mqtt.loop();

  static unsigned long dernierPublish = 0;
  static unsigned long dernierDiag    = 0;

  if (millis() - dernierPublish > 5000) {   // Toutes les 5 secondes
    dernierPublish = millis();
    MesureCapteur m = lireCapteurs();
    publierMesure(m);
    digitalWrite(2, m.alarme ? HIGH : LOW); // LED rouge si alarme
  }

  if (millis() - dernierDiag > 30000) {     // Toutes les 30 secondes
    dernierDiag = millis();
    afficherDiag();
  }
}
```

---

## 3️⃣ ÉTAPE 3 — RÈGLE IOT AWS ET CLOUDWATCH

### Règle IoT SQL recommandée

```sql
-- Dans la console AWS IoT Core → Rules → Create Rule :

SELECT mesure1, mesure2, alarme, nb_alarmes, mtbf_min,
       timestamp() as ts_aws,
       topic(2) as machine_id
FROM 'industech/+/capteurs'
WHERE mesure1 IS NOT NULL
```

### Actions à configurer sur la règle

```
Action 1 → CloudWatch Metrics
  Espace de noms   : Industrie40/CIEL
  Métrique 1       : Vibration  (ou Courant, Niveau selon sujet)
    Valeur         : ${mesure1}
    Dimension      : Machine = ${machine_id}
  Métrique 2       : Temperature
    Valeur         : ${mesure2}
  Métrique 3       : MTBF_min
    Valeur         : ${mtbf_min}

Action 2 → CloudWatch Logs (optionnel)
  Groupe de logs   : /industech/alarmes
  Condition        : WHERE alarme = true
```

### Dashboard CloudWatch recommandé

```
Widget 1 — Graphique courbes (Vibration/Courant dans le temps)
  Période : 1 minute, Statistique : Moyenne
  Annotation : ligne rouge sur le seuil d'alarme (ex: 2.5g)

Widget 2 — Chiffre instantané (dernière valeur)
  Métrique : Vibration, Statistique : Max, Période : 1 min

Widget 3 — Graphique courbes (MTBF_min dans le temps)
  Permet de voir si le MTBF se dégrade dans le temps

Widget 4 — Graphique courbes (Température)
  Corrélation temperature ↔ vibration

Alarme CloudWatch :
  Métrique     : Vibration
  Condition    : > SEUIL_ALERTE pendant 1 période consécutive
  Action       : SNS → envoyer SMS/email
```

---

## 4️⃣ CALCUL MTBF AVANCÉ

### Formule de base (vue dans le cahier des charges)

$$MTBF = \frac{T_{obs}}{N_{alarmes}}$$

### Formule avancée : intervalle de confiance

> En pratique, le MTBF calculé sur peu de données a une grande incertitude. On peut donner un **intervalle de confiance à 90%** :

$$MTBF_{min} = \frac{2 \times T_{obs}}{\chi^2_{2N+2,\ 0.95}} \quad \text{(borne basse)}$$

> **Approche simplifiée pour le projet :** Si vous avez N ≥ 5 alarmes, votre MTBF est fiable à ±30%. Si N < 5, précisez que la valeur est indicative.

### Interprétation pour la maintenance prédictive

```
Exemple avec MTBF = 30 min :

  "La machine génère en moyenne 1 alarme toutes les 30 minutes.
   Si on accepte au maximum 3 alarmes consécutives avant intervention :
   → Temps avant maintenance = 3 × 30 min = 90 minutes
   → Planifier l'intervention 1h30 avant le prochain dépassement critique"

  Niveau 1 : MTBF > 120 min → maintenance dans > 2h (surveillance normale)
  Niveau 2 : 60 < MTBF ≤ 120 min → surveillance renforcée
  Niveau 3 : 30 < MTBF ≤ 60 min → maintenance dans la journée
  Niveau 4 : MTBF ≤ 30 min → maintenance immédiate
```

### Tableau de suivi MTBF à alimenter en temps réel

> Copier dans un onglet de tableur ou document pendant la séance :

```
Heure    | Alarme# | Valeur  | ΔT depuis préc. | MTBF cumulé
---------|---------|---------|-----------------|------------
HH:MM:SS |    1    |  3.2g   | —               | —
HH:MM:SS |    2    |  2.8g   | 28 min          | 28 min
HH:MM:SS |    3    |  3.5g   | 32 min          | 30 min
HH:MM:SS |    4    |  2.6g   | 24 min          | 28 min
HH:MM:SS |    5    |  3.1g   | 35 min          | 29.8 min
         |         |         | MTBF final →    | 29.8 min
```

---

## 5️⃣ GUIDE CAPTEURS PAR SUJET

### SUJET A — ADXL345 (Accéléromètre I2C)

```cpp
#include <Wire.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

// Dans setup() :
Wire.begin(21, 22);  // SDA=21, SCL=22 sur ESP32
accel.begin();
accel.setRange(ADXL345_RANGE_16_G);

// Dans loop() : Calcul de l'accélération totale (module)
sensors_event_t event;
accel.getEvent(&event);
float g_total = sqrt(
  event.acceleration.x * event.acceleration.x +
  event.acceleration.y * event.acceleration.y +
  event.acceleration.z * event.acceleration.z
) / 9.81;  // Convertir m/s² en g

// g_total > 2.0 → alarme de vibration anormale
```

### SUJET B — ACS712 (Courant sur ADC)

```cpp
// ACS712-5A connecté sur GPIO 34 (ADC1 de l'ESP32)
const int ACS_PIN  = 34;
const float VREF   = 3.3;          // Référence ADC ESP32
const int   ADC_RES = 4096;
const float SENSI  = 0.185;        // V/A pour ACS712-5A

float lireCourant() {
  int raw = analogRead(ACS_PIN);
  float voltage = raw * VREF / ADC_RES;
  float courant = (voltage - VREF/2) / SENSI;  // Centré à VREF/2
  return abs(courant);  // Valeur absolue
}
// Courant > 2.0A → alarme de surcharge
```

### SUJET C — MQ135 (Qualité d'air)

```cpp
// MQ135 sur GPIO 35 (ADC1, entrée analogique)
const int MQ135_PIN = 35;

float lireQualiteAir() {
  int raw = analogRead(MQ135_PIN);
  // Calibration approximative : à adapter avec votre capteur
  float ppm = raw * (5000.0 / 4096.0);  // Linéaire grossier
  return ppm;
}
// CO2 > 1000 ppm → alarme qualité d'air dégradée
```

### SUJET D — HC-SR04 (Niveau ultrasons)

```cpp
const int TRIG_PIN = 5;
const int ECHO_PIN = 18;

float lireNiveauCm() {
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duree = pulseIn(ECHO_PIN, HIGH, 30000);  // timeout 30ms
  float distance_cm = duree * 0.034 / 2;
  return distance_cm;
}
// Niveau < 10 cm → cuve presque pleine → alarme
```

---

## 6️⃣ CHECKLIST DE VALIDATION PROGRESSIVE

> Remplir au fil de la séance — visa formateur à J1, J2, J3.

### Jalon J1 — Architecture validée (0h30)

```
☐ Diagramme bloc dessiné et commenté
☐ Tableau de décisions techniques rempli
☐ Seuil d'alarme justifié (pas juste un chiffre au hasard)
☐ Formule MTBF comprise par l'équipe

→ Visa formateur : ______________________
```

### Jalon J2 — Circuit opérationnel (1h30)

```
☐ Capteur(s) câblés sur l'ESP32
☐ Valeurs visibles dans le moniteur série (lecture cohérente)
☐ Schéma KiCad partiellement tracé (au moins les composants placés)
☐ Seuil testé manuellement (déclencher l'alarme en soufflant sur le capteur)

→ Visa formateur : ______________________
```

### Jalon J3 — AWS connecté (3h00)

```
☐ MQTT TLS connecté (log "Connecté !" dans série)
☐ Messages JSON visibles dans la console AWS MQTT Test
☐ Dashboard CloudWatch avec ≥ 1 métrique alimentée
☐ ≥ 1 alarme CloudWatch configurée (même si pas encore déclenchée)

→ Visa formateur : ______________________
```

---

**Document – BAC PRO CIEL – A2 – E2/U21 – Version 1.0 – 2026**
