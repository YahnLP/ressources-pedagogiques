# 📘 FICHE DE COURS — S6 · 2ᵉ ANNÉE · E2
## ESP32 WiFi : Modes Station & AP · WebServer Embarqué · MQTT Client Basique

---

> **Nom** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Date** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Compétences travaillées** : S5.1 · S5.2 · S5.3 · C5.1 · C5.2

---

## 🔑 Vocabulaire clé

| Terme | Définition |
|---|---|
| **ESP32** | Microcontrôleur Espressif avec WiFi + BT intégrés · cœur de l'IoT moderne |
| **Mode STA** | Station Mode — l'ESP32 se connecte à un réseau WiFi existant (comme un smartphone) |
| **Mode AP** | Access Point Mode — l'ESP32 crée son propre réseau WiFi (comme une box Internet) |
| **Mode STA+AP** | Les deux simultanément — connecté à une box ET diffuse son propre réseau |
| **WebServer** | Serveur HTTP embarqué dans l'ESP32 — répond à des requêtes de navigateurs |
| **HTTP GET** | Requête pour demander une ressource (une page, un état de capteur) |
| **HTTP POST** | Requête pour envoyer des données (formulaire, commande) |
| **MQTT** | Message Queuing Telemetry Transport — protocole léger pub/sub pour l'IoT |
| **Broker MQTT** | Serveur intermédiaire qui reçoit et redistribue les messages MQTT |
| **Publisher** | Client MQTT qui envoie des messages sur un topic |
| **Subscriber** | Client MQTT qui s'abonne à un topic pour recevoir ses messages |
| **Topic** | Chemin hiérarchique identifiant un flux de messages (ex: "maison/salon/temp") |
| **QoS** | Quality of Service — niveau de fiabilité de livraison d'un message MQTT (0, 1, 2) |
| **WiFi.begin()** | Fonction Arduino ESP32 pour se connecter à un réseau WiFi |
| **PubSubClient** | Bibliothèque Arduino pour le protocole MQTT |

---

## 1️⃣ — L'ESP32 : microcontrôleur IoT de référence

### Architecture et capacités

![Caractéristiques de l'ESP32 DevKit v1](images/esp32-caracteristiques.png)

```
Alimentation : 3,3 V (GPIO) — 5 V (USB)
⚠️ Les GPIO ESP32 sont en 3,3 V — incompatibles 5 V direct !
```

### Structure d'un programme Arduino ESP32

```cpp
// Inclure les bibliothèques nécessaires
#include <WiFi.h>
#include <WebServer.h>

// Variables globales
const char* ssid = "MonReseau";
const char* password = "MonMotDePasse";

void setup() {
  Serial.begin(115200);    // Moniteur série
  // Initialisation unique au démarrage
}

void loop() {
  // Répété en boucle indéfiniment
  // Gérer les requêtes, lire capteurs, publier MQTT...
}
```


> [!TIP] 💡 En clair
> Un **microcontrôleur** est un petit ordinateur sur une seule puce : il lit des capteurs, commande des sorties et exécute **un seul programme**, sans système d'exploitation. L'**ESP32** ajoute à cela le **Wi-Fi** et le **Bluetooth** déjà intégrés : il peut donc se connecter à un réseau sans carte supplémentaire.
>
> Le programme Arduino a toujours deux parties : `setup()` s'exécute **une seule fois** au démarrage (préparer) ; `loop()` se répète **sans fin** (agir).

> [!WARNING] ⚠️ Attention aux tensions
> Les broches (GPIO) de l'ESP32 fonctionnent en **3,3 V**. Brancher directement un signal **5 V** peut **détruire** la broche. Le port USB, lui, apporte 5 V à la carte, qui les convertit en 3,3 V.

### ✅ Vérifie que tu as compris

**Q1.** Combien de fois `setup()` est-elle exécutée ? Et `loop()` ?

??? success "Réponse"
    `setup()` : **une seule fois** au démarrage. `loop()` : **en boucle**, indéfiniment.

**Q2.** Peut-on brancher une sortie de capteur en 5 V sur un GPIO de l'ESP32 ?

??? success "Réponse"
    **Non**, pas directement : les GPIO sont en **3,3 V**. Il faut adapter le niveau (diviseur de tension ou adaptateur de niveau).

---

## 2️⃣ — Mode Station (STA) : se connecter au WiFi

### Connexion à un réseau existant

```cpp
#include <WiFi.h>

const char* ssid     = "NomDuReseau";
const char* password = "MotDePasse";

void setup() {
  Serial.begin(115200);
  
  // Démarrer la connexion WiFi en mode Station
  WiFi.begin(ssid, password);
  
  // Attendre la connexion (avec timeout)
  Serial.print("Connexion WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  // Connexion établie
  Serial.println("\n✓ Connecté !");
  Serial.print("Adresse IP : ");
  Serial.println(WiFi.localIP());   // Afficher l'IP obtenue par DHCP
}

void loop() {
  // Rien ici pour l'instant
}
```

### États WiFi courants

```
WiFi.status() peut retourner :
  WL_CONNECTED      = 3  ← Connecté ✓
  WL_IDLE_STATUS    = 0  ← En attente
  WL_NO_SSID_AVAIL  = 1  ← SSID introuvable
  WL_CONNECT_FAILED = 4  ← Mauvais mot de passe ou autre erreur
  WL_DISCONNECTED   = 6  ← Déconnecté

Informations utiles une fois connecté :
  WiFi.localIP()     → IP de l'ESP32 (ex: 192.168.1.42)
  WiFi.RSSI()        → Force du signal en dBm (ex: -65 dBm)
  WiFi.SSID()        → Nom du réseau connecté
  WiFi.macAddress()  → Adresse MAC de l'ESP32
```


> [!TIP] 💡 En clair : ce qui se passe quand l'ESP32 se connecte
> 1. `WiFi.begin(ssid, password)` : l'ESP32 cherche le réseau portant ce **nom** (SSID) et présente le **mot de passe**.
> 2. La **box** (le routeur) vérifie le mot de passe, puis lui attribue une **adresse IP** automatiquement : c'est le rôle du **DHCP**.
> 3. `WiFi.status() == WL_CONNECTED` devient vrai : l'ESP32 est **sur le réseau**, comme un téléphone.
>
> La boucle `while` **attend** que ce soit fini : sans elle, le programme continuerait avant d'être connecté. Si le SSID est faux ou le mot de passe incorrect, la boucle **ne se termine jamais** : on voit des points s'afficher à l'infini dans le moniteur série.

> [!NOTE] 🔎 Les mots à connaître
> **SSID** : nom du réseau Wi-Fi · **IP** : adresse de l'ESP32 sur ce réseau (`192.168.1.42`) · **DHCP** : service de la box qui distribue les adresses · **RSSI** : puissance du signal reçu en dBm (plus proche de 0 = meilleur : −50 dBm est très bon, −85 dBm est limite).

### ✅ Vérifie que tu as compris

**Q1.** Le moniteur série affiche des points sans fin. Cite deux causes.

??? success "Réponse"
    SSID ou **mot de passe incorrect** ; réseau **hors de portée** ; réseau en **5 GHz** (l'ESP32 ne gère que le **2,4 GHz**).

**Q2.** Qui attribue l'adresse IP à l'ESP32 ?

??? success "Réponse"
    Le **DHCP de la box** (routeur) du réseau.

**Q3.** Un RSSI de −80 dBm est-il meilleur qu'un RSSI de −50 dBm ?

??? success "Réponse"
    **Non** : −50 dBm est un signal **bien plus fort**.

---

![ESP32 en mode STA](images/wifi-sta.png)

---

## 3️⃣ — WebServer embarqué

> [!TIP] 💡 En clair : un serveur web sur un microcontrôleur
> Quand tu tapes une adresse dans ton navigateur, il envoie une **requête** à un serveur, qui renvoie une **réponse** (une page). L'ESP32 peut jouer le rôle du serveur : **tu tapes son adresse IP** dans ton navigateur, et il te répond.
>
> | Élément | Rôle |
> |---|---|
> | **URL** `http://192.168.1.42/led/on` | **Adresse** (l'IP) suivie du **chemin** demandé (`/led/on`) |
> | **Route** | Association chemin → fonction : `server.on("/led/on", handleLedOn)` |
> | **Handler** | La fonction qui s'exécute quand ce chemin est demandé |
> | **Code 200 / 404** | Réponse « tout va bien » / « page introuvable » |
> | **Port 80** | Le port standard du web (HTTP) |
>
> **Déroulé** : le navigateur demande `/led/on` → l'ESP32 appelle `handleLedOn()` → la LED s'allume → il répond « LED allumée » au navigateur.


### Créer un serveur HTTP sur l'ESP32

```cpp
#include <WiFi.h>
#include <WebServer.h>

const char* ssid     = "NomDuReseau";
const char* password = "MotDePasse";

WebServer server(80);   // Serveur HTTP sur le port 80

// ─── Handler : page d'accueil ──────────────────────────────────────────────
void handleRoot() {
  String html = "<!DOCTYPE html><html><head>";
  html += "<meta charset='UTF-8'>";
  html += "<title>ESP32 WebServer</title></head><body>";
  html += "<h1>🔌 ESP32 en ligne !</h1>";
  html += "<p>Température fictive : <b>23.5°C</b></p>";
  html += "</body></html>";
  
  server.send(200, "text/html", html);  // Code 200 = OK
}

// ─── Handler : LED on ──────────────────────────────────────────────────────
void handleLedOn() {
  digitalWrite(2, HIGH);               // Allumer LED GPIO 2
  server.send(200, "text/plain", "LED allumée");
}

// ─── Handler : LED off ─────────────────────────────────────────────────────
void handleLedOff() {
  digitalWrite(2, LOW);
  server.send(200, "text/plain", "LED éteinte");
}

// ─── Handler : 404 Not Found ───────────────────────────────────────────────
void handleNotFound() {
  server.send(404, "text/plain", "404 : Page introuvable");
}

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  
  // Connexion WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); Serial.print(".");
  }
  Serial.println("\nIP : " + WiFi.localIP().toString());
  
  // Enregistrer les routes (URL → fonction handler)
  server.on("/",        handleRoot);      // GET /
  server.on("/led/on",  handleLedOn);     // GET /led/on
  server.on("/led/off", handleLedOff);    // GET /led/off
  server.onNotFound(handleNotFound);      // Toute autre URL
  
  server.begin();   // Démarrer le serveur
  Serial.println("Serveur HTTP démarré !");
}

void loop() {
  server.handleClient();   // ← OBLIGATOIRE en loop() pour traiter les requêtes
}
```

### Utilisation depuis un navigateur

```
L'ESP32 a obtenu l'IP 192.168.1.42

URL                           Action
http://192.168.1.42/          → Page d'accueil HTML
http://192.168.1.42/led/on    → Allume la LED
http://192.168.1.42/led/off   → Éteint la LED

⚠️ server.handleClient() dans loop() est CRITIQUE
   Sans lui, le serveur ne répond à aucune requête
```


> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier `server.handleClient()` dans `loop()` : le serveur **ne répond jamais**.
> - Utiliser une adresse IP **différente** de celle affichée dans le moniteur série (la box peut en donner une autre à chaque démarrage).
> - Mettre un `delay()` de plusieurs secondes dans `loop()` : le navigateur **attend** la réponse.
> - Se connecter avec un téléphone sur **un autre réseau** (4G, autre Wi-Fi) : l'ESP32 n'est joignable que **sur son réseau**.

### ✅ Vérifie que tu as compris

**Q1.** Dans l'URL `http://192.168.1.42/led/off`, que représentent `192.168.1.42` et `/led/off` ?

??? success "Réponse"
    `192.168.1.42` est l'**adresse de l'ESP32** ; `/led/off` est le **chemin** (la route) qui déclenche `handleLedOff()`.

**Q2.** Que se passe-t-il si on demande `/led/clignote` qui n'a pas de route ?

??? success "Réponse"
    C'est `handleNotFound()` qui répond, avec le code **404**.

**Q3.** Pourquoi `server.handleClient()` doit-il être dans `loop()` ?

??? success "Réponse"
    Parce qu'il **vérifie à chaque tour** si une requête est arrivée et appelle le bon handler.

---

## 4️⃣ — Mode Access Point (AP)

> [!TIP] 💡 En clair : station ou point d'accès ?
> - **Mode STA (station)** : l'ESP32 est un **client**, comme ton téléphone qui rejoint le Wi-Fi de la maison. Il a besoin d'une box.
> - **Mode AP (point d'accès)** : l'ESP32 **crée son propre réseau**, comme une box. Ton téléphone s'y connecte. Aucune box nécessaire.
>
> | | STA | AP |
> |---|---|---|
> | Besoin d'une box existante | oui | **non** |
> | Accès à Internet / broker MQTT | oui | non (sauf mode STA+AP) |
> | IP de l'ESP32 | donnée par la box (DHCP) | **192.168.4.1** (fixe par défaut) |
> | Usage typique | capteur connecté | **configuration initiale**, démonstration sans réseau |
>
> Le cas classique : au premier démarrage l'ESP32 ne connaît pas le Wi-Fi de la maison. Il crée un réseau **AP** avec une page où l'utilisateur saisit le SSID et le mot de passe ; puis il redémarre en mode **STA**.


### L'ESP32 crée son propre réseau WiFi

```cpp
#include <WiFi.h>
#include <WebServer.h>

// Paramètres du réseau AP créé par l'ESP32
const char* ap_ssid     = "ESP32_Config";
const char* ap_password = "monmdp123";  // min 8 caractères, ou "" pour ouvert

WebServer server(80);

void setup() {
  Serial.begin(115200);
  
  // Démarrer en mode Access Point
  WiFi.mode(WIFI_AP);
  WiFi.softAP(ap_ssid, ap_password);
  
  // L'ESP32 a l'IP 192.168.4.1 par défaut en mode AP
  Serial.print("Réseau WiFi créé : ");
  Serial.println(ap_ssid);
  Serial.print("IP du portail : http://");
  Serial.println(WiFi.softAPIP());   // Affiche 192.168.4.1
  
  server.on("/", []() {
    server.send(200, "text/html",
      "<h1>Portail de configuration ESP32</h1>"
      "<p>Connecté au réseau ESP32_Config</p>");
  });
  
  server.begin();
}

void loop() {
  server.handleClient();
}
```

### Caractéristiques du mode AP

```
IP par défaut de l'ESP32 en mode AP : 192.168.4.1
DHCP intégré : attribue 192.168.4.2, 192.168.4.3... aux clients
Clients max simultanés : 4 (par défaut, configurable jusqu'à 10)
Portée : ~50-100m en espace ouvert

Mode STA + AP simultané :
  WiFi.mode(WIFI_AP_STA);   // Les deux modes en même temps
  WiFi.softAP(ap_ssid, ap_password);
  WiFi.begin(sta_ssid, sta_password);
  → L'ESP32 est connecté à Internet (STA) ET diffuse son propre réseau (AP)
  → Cas typique : portail de configuration initial
```


### ✅ Vérifie que tu as compris

**Q1.** Tu veux montrer ton ESP32 en classe sans accès au Wi-Fi du lycée. Quel mode choisis-tu ?

??? success "Réponse"
    Le mode **AP** : l'ESP32 crée son propre réseau et le téléphone s'y connecte.

**Q2.** En mode AP, à quelle adresse tape-t-on dans le navigateur ?

??? success "Réponse"
    `http://192.168.4.1` (adresse par défaut de l'ESP32 en AP).

**Q3.** Pourquoi utiliser STA+AP pour un portail de configuration ?

??? success "Réponse"
    L'ESP32 **diffuse un réseau** pour la configuration (AP) tout en pouvant **rejoindre** la box (STA).

---

![Modes Wi-Fi de l'ESP32 : STA, AP et STA + AP](images/wifi-modes.png)

---

## 5️⃣ — MQTT : messagerie IoT pub/sub

> [!TIP] 💡 En clair : MQTT en 30 secondes
> Avec le serveur web, **tu viens chercher** l'information. Avec MQTT, c'est l'ESP32 qui **envoie** sa mesure à un intermédiaire, le **broker**, qui la transmet à toutes les personnes **abonnées** au sujet (le **topic**). Le capteur et le tableau de bord ne se connaissent pas : ils ne parlent qu'au broker.
>
> Le détail (déroulé pas à pas, topics, QoS, retained, testament) est dans le cours suivant, **S07**. Ici, on retient surtout **comment l'ESP32 se connecte et publie**.


### Architecture MQTT

```
MQTT = Message Queuing Telemetry Transport
  → Protocole léger (quelques centaines d'octets)
  → Conçu pour les appareils IoT avec connexion instable
  → Port TCP 1883 (non chiffré) · 8883 (TLS)
  → Modèle Publish/Subscribe (pub/sub) via un Broker central

TROIS ACTEURS :
  Publisher  → Envoie un message sur un topic
  Subscriber → Reçoit les messages d'un topic (abonnement)
  Broker     → Intermédiaire central (Mosquitto, HiveMQ, EMQX...)
```

### Topics MQTT : convention de nommage

```
Format hiérarchique séparé par des /
  "bâtiment/salle/capteur/mesure"
  
Exemples :
  "ecole/labo_e2/esp32_1/temperature"
  "ecole/labo_e2/esp32_1/led/etat"
  "ecole/labo_e2/esp32_1/led/commande"

Wildcards :
  "ecole/+/esp32_1/temperature"  → "+" remplace UN niveau
  "ecole/#"                       → "#" remplace TOUT le reste
```

### QoS — Niveaux de qualité de service

```
QoS 0 → "Fire and forget" : message envoyé une fois, pas d'accusé de réception
         Le plus rapide, peut être perdu si déconnexion
         
QoS 1 → "At least once" : message envoyé jusqu'à réception d'un ACK
         Peut être reçu **plusieurs fois** (doublons possibles : à gérer côté application)
         
QoS 2 → "Exactly once" : garantit la réception exactement 1 fois
         Le plus fiable, mais plus lent (4 échanges)
         
Pour l'IoT basique : QoS 0 ou QoS 1 est suffisant
```

### Code ESP32 : client MQTT avec PubSubClient

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

// ─── Configuration ──────────────────────────────────────────────────────────
const char* ssid        = "NomDuReseau";
const char* password    = "MotDePasse";
const char* mqtt_server = "broker.hivemq.com";  // ou IP du Mosquitto local
const int   mqtt_port   = 1883;
const char* client_id   = "ESP32_CIEL_001";     // Unique par appareil !

// ─── Topics ─────────────────────────────────────────────────────────────────
const char* topic_pub   = "ecole/labo/esp32/temperature";
const char* topic_sub   = "ecole/labo/esp32/led/commande";

// ─── Objets globaux ─────────────────────────────────────────────────────────
WiFiClient   espClient;
PubSubClient mqtt(espClient);

// ─── Callback : appelée à la réception d'un message MQTT ───────────────────
void messageRecu(char* topic, byte* payload, unsigned int length) {
  // Convertir payload (bytes) en String
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  
  Serial.println("Message reçu sur [" + String(topic) + "] : " + message);
  
  // Réagir au message
  if (String(topic) == topic_sub) {
    if (message == "ON")  { digitalWrite(2, HIGH); }
    if (message == "OFF") { digitalWrite(2, LOW);  }
  }
}

// ─── Connexion WiFi ─────────────────────────────────────────────────────────
void connectWiFi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); Serial.print(".");
  }
  Serial.println("\n✓ WiFi connecté : " + WiFi.localIP().toString());
}

// ─── Connexion MQTT ─────────────────────────────────────────────────────────
void connectMQTT() {
  mqtt.setServer(mqtt_server, mqtt_port);
  mqtt.setCallback(messageRecu);
  
  while (!mqtt.connected()) {
    Serial.print("Connexion MQTT...");
    if (mqtt.connect(client_id)) {
      Serial.println(" ✓ Connecté au broker !");
      mqtt.subscribe(topic_sub);   // S'abonner au topic commande
      Serial.println("Abonné au topic : " + String(topic_sub));
    } else {
      Serial.print(" Échec (rc=");
      Serial.print(mqtt.state());
      Serial.println(") → Nouvelle tentative dans 5s");
      delay(5000);
    }
  }
}

// ─── Setup ──────────────────────────────────────────────────────────────────
void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  
  connectWiFi();
  connectMQTT();
}

// ─── Loop ───────────────────────────────────────────────────────────────────
void loop() {
  // Maintenir la connexion MQTT (reconnexion automatique si perdu)
  if (!mqtt.connected()) { connectMQTT(); }
  mqtt.loop();   // ← OBLIGATOIRE pour recevoir les messages
  
  // Publier la "température" toutes les 10 secondes
  static unsigned long lastMsg = 0;
  if (millis() - lastMsg > 10000) {
    lastMsg = millis();
    
    float temp = 23.5 + random(-10, 10) / 10.0;  // Valeur fictive
    String payload = String(temp, 1);             // "23.7"
    
    mqtt.publish(topic_pub, payload.c_str());
    Serial.println("Publié : " + String(topic_pub) + " → " + payload);
  }
}
```

---

![Architecture MQTT avec un ESP32](images/mqtt-esp32.png)

---

## 6️⃣ — Comparatif HTTP WebServer vs MQTT

```
                    HTTP WebServer              MQTT
Architecture        Client-Serveur              Pub/Sub via Broker
Initiation          Client (navigateur)         N'importe qui (pub ou sub)
Connexion           Stateless (une requête à la fois) Persistante (TCP keep-alive)
Complexité          Simple (URL → réponse)      Plus élaboré (broker nécessaire)
Adapté pour         Contrôle local, affichage   IoT, temps réel, multi-devices
Consommation        Moyenne (parse HTTP)        Faible (messages binaires légers)
Perte de connexion  La requête échoue           Broker conserve le dernier message (retain)
Sécurité            HTTPS (TLS sur 443)         MQTT over TLS (port 8883)
Cas d'usage E2      Page web de contrôle locale Multi-capteurs, tableau de bord
```


> [!TIP] 💡 En clair : lequel choisir ?
> - **Une seule personne**, qui veut **voir ou commander l'ESP32 depuis son navigateur**, sur le même réseau → **WebServer**.
> - **Plusieurs appareils ou applications** qui échangent des mesures, ou un **historique/supervision** → **MQTT**.
> - **Configuration initiale** sans réseau → **mode AP + WebServer**.

### ✅ Vérifie que tu as compris

**Q1.** Dix capteurs doivent envoyer leurs mesures à un dashboard. WebServer ou MQTT ?

??? success "Réponse"
    **MQTT** : chaque capteur publie vers le broker, le dashboard s'abonne ; en WebServer il faudrait interroger les dix capteurs un par un.

**Q2.** Tu veux allumer une LED depuis ton téléphone, sur le Wi-Fi de la classe, sans rien installer. Que choisis-tu ?

??? success "Réponse"
    Un **WebServer** : le navigateur du téléphone suffit.

---

## 📌 Les essentiels à retenir

> ✅ **Mode STA** : `WiFi.begin(ssid, pass)` → connecté au réseau → IP par DHCP
> ✅ **Mode AP** : `WiFi.softAP(ssid, pass)` → IP fixe **192.168.4.1**
> ✅ **WebServer** : `server.on("/route", handler)` → `server.handleClient()` dans **loop()**
> ✅ **MQTT** : 3 acteurs — **Publisher**, **Subscriber**, **Broker**
> ✅ **Topic** : chemin hiérarchique `"maison/salle/capteur"` · `+` = 1 niveau · `#` = tout
> ✅ **QoS 0** = "fire and forget" · **QoS 1** = au moins 1 fois · **QoS 2** = exactement 1 fois
> ✅ `mqtt.loop()` dans **loop()** est OBLIGATOIRE pour recevoir les messages
> ✅ Client ID MQTT = unique par appareil (sinon déconnexion en boucle !)
> ✅ PubSubClient : bibliothèque Arduino MQTT standard

---

*Fiche de Cours ESP32 WiFi — BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S6*
*Compétences : S5.1 · S5.2 · S5.3 · C5.1 · C5.2*
