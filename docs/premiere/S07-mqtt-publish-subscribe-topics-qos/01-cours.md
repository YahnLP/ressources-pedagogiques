# 📖 FICHE COURS – S7 ANNÉE 2 – E2
## MQTT : Publish/Subscribe, Topics, QoS, Mosquitto, ESP32

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Expliquer le modèle publish/subscribe et son avantage en IoT
- ✅ Utiliser correctement les topics et les wildcards
- ✅ Choisir le bon niveau de QoS selon le cas d'usage
- ✅ Configurer Mosquitto et tester avec la CLI
- ✅ Connecter un ESP32 à un broker MQTT

---

## 1️⃣ POURQUOI MQTT ? LE PROBLÈME DU HTTP EN IOT

### HTTP : adapté aux navigateurs, pas aux capteurs

> HTTP (le protocole du Web) fonctionne en **request/response** : le client demande, le serveur répond. Ce modèle a plusieurs inconvénients pour l'IoT :

| **Problème HTTP** | **Impact en IoT** |
|---|---|
| En-têtes verbeux (~500 octets minimum) | Trop lourd pour un microcontrôleur à 80 MHz / pile TCP limitée |
| Le client doit demander (polling) | Gaspille la batterie ; latence élevée |
| Connexion à chaque échange | Coûteux en temps et en énergie |
| N capteurs × M apps = N×M connexions | Non scalable |

### MQTT : conçu pour les contraintes de l'IoT

> **MQTT** (Message Queuing Telemetry Transport) a été créé en 1999 par IBM pour relier des capteurs pétroliers via des liaisons satellite très limitées. Il est maintenant le standard de l'IoT.

| **Avantage MQTT** | **Chiffre** |
|---|---|
| En-tête minimum | **2 octets** seulement |
| Maintien de connexion | Connexion TCP persistante |
| Consommation batterie | Très faible (push, pas polling) |
| Scalabilité | Un broker → des millions de clients |

---

## 2️⃣ LE MODÈLE PUBLISH / SUBSCRIBE

### Architecture

```
                    ┌──────────────────┐
  [Capteur Temp]    │                  │    [Dashboard]
  Publisher ───────►│    B R O K E R   │───►  Subscriber
                    │   (Mosquitto,    │
  [Capteur CO2]     │    HiveMQ...)    │    [Alarme SMS]
  Publisher ───────►│                  │───►  Subscriber
                    │                  │
                    └──────────────────┘
                                ▲
                         Seul point central
                         Les publishers et subscribers
                         ne se connaissent pas
```

### Les acteurs

| **Acteur** | **Rôle** | **Exemple** |
|---|---|---|
| **Broker** | Serveur central qui reçoit, filtre et redistribue | Mosquitto, HiveMQ, AWS IoT Core |
| **Publisher** | Client qui envoie un message sur un topic | ESP32 avec capteur DHT22 |
| **Subscriber** | Client abonné à un ou plusieurs topics | Application dashboard, Node-RED |
| **Topic** | Chemin hiérarchique identifiant le "canal" | `maison/salon/temperature` |
| **Message (Payload)** | Contenu du message (texte, JSON, binaire) | `{"temp":22.5,"hum":65}` |

---

## 3️⃣ LES TOPICS

### Structure hiérarchique

> Un topic est une chaîne UTF-8 avec des niveaux séparés par des `/`. Il n'y a pas de déclaration préalable — un topic existe dès qu'un message y est publié.

```
maison/salon/temperature          → température du salon
maison/salon/humidite             → humidité du salon
maison/cuisine/temperature        → température de la cuisine
usine/ligne1/machine3/vibration   → vibration machine 3, ligne 1
vehicule/bus42/GPS/latitude       → position GPS du bus 42
```

> **Bonnes pratiques de nommage :**
> - Tout en minuscules, sans espaces
> - Du général au spécifique (zone → pièce → grandeur)
> - Pas de `/` au début ou à la fin

### Wildcards (dans les souscriptions uniquement)

> Les wildcards permettent de s'abonner à plusieurs topics en une seule souscription. **Ils ne peuvent PAS être utilisés dans les publications.**

| **Wildcard** | **Signification** | **Exemple** | **Match** |
|---|---|---|---|
| `+` | Un niveau unique quelconque | `maison/+/temperature` | `maison/salon/temperature`, `maison/cuisine/temperature` — **pas** `maison/salon/haut/temperature` |
| `#` | Tout ce qui suit (doit être le dernier caractère) | `maison/#` | Tout ce qui commence par `maison/` |
| `#` seul | Tous les topics | `#` | **Tous** les messages du broker |

```
Souscription : maison/+/temperature
  ✅ maison/salon/temperature
  ✅ maison/cuisine/temperature
  ❌ maison/salon/haut/temperature    (+ couvre 1 seul niveau)

Souscription : maison/#
  ✅ maison/salon/temperature
  ✅ maison/cuisine/humidite
  ✅ maison/salon/haut/temperature    (# couvre tout ce qui suit)
  ❌ usine/ligne1/...                 (ne commence pas par maison/)
```

---

📷 **[ILLUSTRATION 1]**
*Schéma d'architecture MQTT. Au centre : un rectangle étiqueté "BROKER (Mosquitto)" avec une icône serveur. À gauche : 3 icônes ESP32/capteurs étiquetées "Publisher 1 → maison/salon/temp", "Publisher 2 → maison/cuisine/temp", "Publisher 3 → usine/ligne1/vib". À droite : 3 icônes étiquetées "Subscriber A (abonné à maison/#)", "Subscriber B (abonné à maison/salon/+)", "Subscriber C (abonné à usine/#)". Des flèches colorées montrent quel subscriber reçoit quels messages selon les topics. Style schéma IoT propre, fond blanc, couleurs distinctes par topic.*

> **Légende :** Architecture MQTT avec 3 publishers et 3 subscribers. Le broker est l'unique point de contact — publishers et subscribers ne communiquent jamais directement. Subscriber A (abonné à `maison/#`) reçoit tous les messages des publishers 1 et 2. Subscriber B (abonné à `maison/salon/+`) reçoit seulement les messages du publisher 1 (salon uniquement, toutes grandeurs). Subscriber C reçoit uniquement les données industrielles.

---

## 4️⃣ QoS — QUALITÉ DE SERVICE

### Les 3 niveaux

$$\boxed{QoS 0 < QoS 1 < QoS 2}$$

$$\text{fiabilité croissante, overhead croissant}$$

---

### QoS 0 — At Most Once (Fire and Forget)

```
Publisher → PUBLISH → Broker → PUBLISH → Subscriber
           (pas de confirmation)
```

> Le message est envoyé **une fois maximum**, sans confirmation. Si le réseau coupe, le message est perdu. Aucun stockage en mémoire.

**Quand l'utiliser :** données haute fréquence peu critiques (température toutes les secondes — si un point est perdu, le suivant arrivera dans 1s)

---

### QoS 1 — At Least Once

```
Publisher → PUBLISH → Broker → PUBACK → Publisher
                              (confirmation reçue)
           Si pas de PUBACK dans le délai → retransmission
           → Le message peut arriver 2× chez le subscriber
```

> Le message est envoyé **au moins une fois**. En cas de doute (timeout), le publisher retransmet. Cela peut créer des **doublons** chez le subscriber.

**Quand l'utiliser :** données importantes mais où les doublons sont acceptables (alertes, commandes simples). **Le plus utilisé en IoT pratique.**

---

### QoS 2 — Exactly Once

```
Publisher → PUBLISH → Broker → PUBREC → Publisher
           → PUBREL → Broker → PUBCOMP
           (4 échanges pour garantir exactement 1 livraison)
```

> Le message est livré **exactement une fois**, sans perte ni doublon. Nécessite 4 échanges TCP → latence et overhead élevés.

**Quand l'utiliser :** commandes critiques où le doublon est dangereux (actionner une vanne 2× = catastrophe). Peu utilisé sur microcontrôleurs (trop lourd).

### Tableau de choix QoS

| **Cas d'usage** | **QoS recommandé** | **Raison** |
|---|---|---|
| Télémétrie haute fréquence (temp toutes les secondes) | **0** | Pas critique, doublon gênant |
| Alerte seuil dépassé | **1** | On veut la garantie de livraison |
| Commande d'ouverture de vanne | **2** | Doublon = incident industriel |
| Message de statut périodique | **1** | Bon compromis |
| Streaming audio/vidéo | **0** | Latence faible > fiabilité |

---

## 5️⃣ FONCTIONNALITÉS AVANCÉES

### Retained Message (Message Retenu)

> Quand un publisher publie un message avec le flag **RETAIN = true**, le broker conserve **le dernier message** publié sur ce topic. Tout nouveau subscriber qui s'abonne reçoit immédiatement ce dernier message — même s'il n'était pas connecté lors de la publication originale.

```
Publish (RETAIN=true) : maison/salon/temperature → {"temp":22.5}
   ↓
[5 minutes plus tard, un nouvel abonné se connecte]
   ↓
Il reçoit immédiatement {"temp":22.5} sans attendre le prochain publish
```

**Cas d'usage :** état initial d'un actionneur (lampe ON/OFF), dernière valeur connue d'un capteur pour un dashboard qui vient de démarrer.

---

### Last Will and Testament (LWT)

> Quand un client se connecte au broker, il peut déclarer un **message de testament** : si la connexion est perdue brutalement (panne, coupure réseau), le broker publie automatiquement ce message.

```
ESP32 au démarrage : "Si je meurs, publie {'status':'offline'} sur esp32/status"
   ↓
[ESP32 perd le courant sans déconnexion propre]
   ↓
Broker publie automatiquement : esp32/status → {"status":"offline"}
```

**Cas d'usage :** supervision de la disponibilité des équipements IoT.

---

## 6️⃣ MOSQUITTO — BROKER LOCAL

### Installation (Linux)

```bash
sudo apt-get install mosquitto mosquitto-clients

# Fichier de configuration :
# /etc/mosquitto/mosquitto.conf
# ou /etc/mosquitto/conf.d/local.conf

# Configuration minimale pour le labo (accès anonyme local) :
listener 1883
allow_anonymous true

# Redémarrer :
sudo systemctl restart mosquitto

# Vérifier que le service tourne :
sudo systemctl status mosquitto
```

### Commandes CLI

```bash
# Publier un message
mosquitto_pub -h <IP_BROKER> -t <TOPIC> -m <MESSAGE> -q <QOS>

# Exemples :
mosquitto_pub -h localhost -t "maison/salon/temp" -m "22.5"
mosquitto_pub -h 192.168.1.50 -t "maison/salon/data" -m '{"temp":22.5,"hum":65}' -q 1

# S'abonner à un topic
mosquitto_sub -h <IP_BROKER> -t <TOPIC> -v

# Exemples :
mosquitto_sub -h localhost -t "maison/#" -v          # Tous les messages maison/
mosquitto_sub -h localhost -t "maison/+/temp" -v     # Toutes les températures

# Options utiles :
#  -r : retained message
#  -q 1 : QoS 1
#  -i <CLIENT_ID> : identifiant client personnalisé
```

---

## 7️⃣ ESP32 + PUBSUBCLIENT — CONNEXION MQTT

### Bibliothèque à installer

> Dans Arduino IDE : Outils → Gérer les bibliothèques → rechercher **PubSubClient** (by Nick O'Leary) → Installer

### Code complet ESP32

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

// ── Configuration ──────────────────────────────────────────────────
const char* ssid       = "NOM_WIFI";
const char* password   = "MOT_DE_PASSE_WIFI";
const char* mqtt_server = "192.168.1.X";  // IP du PC broker
const int   mqtt_port   = 1883;
const char* client_id   = "esp32-salon-001";

// Topics
const char* topic_pub = "maison/salon/data";     // où on publie
const char* topic_sub = "maison/salon/led";      // ce qu'on écoute

// ── Objets globaux ─────────────────────────────────────────────────
WiFiClient   wifiClient;
PubSubClient mqtt(wifiClient);

// ── Callback : appelée quand un message arrive ────────────────────
void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.print("Message reçu [");
  Serial.print(topic);
  Serial.print("] : ");
  Serial.println(message);

  if (message == "ON") {
    digitalWrite(2, HIGH);   // LED intégrée allumée
  } else if (message == "OFF") {
    digitalWrite(2, LOW);
  }
}

// ── Connexion Wi-Fi ────────────────────────────────────────────────
void connectWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("Connexion WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connecté ! IP : " + WiFi.localIP().toString());
}

// ── Connexion / Reconnexion MQTT ───────────────────────────────────
void connectMQTT() {
  while (!mqtt.connected()) {
    Serial.print("Connexion MQTT...");
    if (mqtt.connect(client_id)) {
      Serial.println("Connecté !");
      mqtt.subscribe(topic_sub);   // S'abonner au topic de commande
    } else {
      Serial.print("Échec, rc=");
      Serial.print(mqtt.state());
      Serial.println(" → nouvel essai dans 5s");
      delay(5000);
    }
  }
}

// ── Setup ──────────────────────────────────────────────────────────
void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);           // LED intégrée ESP32
  connectWiFi();
  mqtt.setServer(mqtt_server, mqtt_port);
  mqtt.setCallback(callback);
}

// ── Loop ──────────────────────────────────────────────────────────
void loop() {
  if (!mqtt.connected()) {
    connectMQTT();              // Reconnexion si nécessaire
  }
  mqtt.loop();                  // Traiter les messages entrants

  // Publier toutes les 5 secondes
  static unsigned long lastMsg = 0;
  if (millis() - lastMsg > 5000) {
    lastMsg = millis();
    String payload = "{\"temp\":" + String(random(20,25)) +
                     ",\"hum\":"  + String(random(50,70)) + "}";
    mqtt.publish(topic_pub, payload.c_str(), false);  // false = pas retained
    Serial.println("Publié : " + payload);
  }
}
```

---

📷 **[ILLUSTRATION 2]**
*Schéma de la chaîne IoT complète de cette séance. De gauche à droite : ESP32 avec capteur DHT22 (température et humidité) → connexion Wi-Fi (ondes) → PC Linux avec Mosquitto (broker, icône serveur) → deux clients : terminal CLI avec mosquitto_sub et Node-RED (icône) abonné. Annotations : "Topic : maison/salon/data", "JSON payload", "QoS 1". Style diagramme IoT moderne, fond blanc, flèches colorées, icônes hardware reconnaissables.*

> **Légende :** Chaîne IoT complète de la séance. L'ESP32 mesure température et humidité via DHT22, les formate en JSON et les publie sur le topic `maison/salon/data` vers le broker Mosquitto local. Deux subscribers écoutent simultanément : le terminal CLI (mosquitto_sub) pour le débogage et Node-RED pour l'affichage graphique. L'ESP32 s'abonne également au topic de commande `maison/salon/led` pour recevoir des ordres depuis le broker.

---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais expliquer le rôle du broker et pourquoi les publishers/subscribers ne se connaissent pas
- [ ] Je sais construire un topic hiérarchique adapté à un contexte IoT
- [ ] Je sais utiliser les wildcards `+` et `#` dans une souscription
- [ ] Je distingue QoS 0, 1 et 2 et sais choisir le bon niveau selon le cas
- [ ] Je sais lancer Mosquitto et tester avec mosquitto_pub / mosquitto_sub
- [ ] Je comprends le rôle du LWT (message publié si l'ESP32 se déconnecte brutalement)
- [ ] Je comprends le Retained message (dernier message conservé pour les nouveaux subscribers)
- [ ] Je sais configurer PubSubClient sur un ESP32 : setServer, setCallback, publish, subscribe

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **MQTT** | Message Queuing Telemetry Transport — protocole léger publish/subscribe pour l'IoT |
| **Broker** | Serveur central MQTT qui redistribue les messages |
| **Mosquitto** | Broker MQTT open-source léger, référence pour les labs et productions légères |
| **Topic** | Chemin hiérarchique identifiant le canal de message (`maison/salon/temp`) |
| **Publisher** | Client qui envoie des messages sur un topic |
| **Subscriber** | Client abonné à un ou plusieurs topics pour recevoir les messages |
| **Wildcard `+`** | Remplace un seul niveau dans un topic de souscription |
| **Wildcard `#`** | Remplace tout ce qui suit — doit être le dernier caractère |
| **QoS 0** | At most once — message envoyé sans confirmation |
| **QoS 1** | At least once — confirmé par PUBACK, peut se dupliquer |
| **QoS 2** | Exactly once — 4-way handshake, garanti sans doublon |
| **Retained** | Flag qui fait conserver le dernier message par le broker |
| **LWT** | Last Will and Testament — message publié si déconnexion brutale |
| **PubSubClient** | Bibliothèque Arduino/ESP32 pour MQTT |
| **Port 1883** | Port MQTT standard non chiffré |
| **Port 8883** | Port MQTT avec TLS (production sécurisée) |

---

## 📌 POINTS-CLÉS À RETENIR

1. MQTT = **2 octets** d'en-tête min. vs ~500 pour HTTP → protocole IoT
2. **Broker** = seul intermédiaire ; publishers et subscribers ne communiquent **jamais directement**
3. Topic = chemin hiérarchique `/` → du **général au spécifique**
4. `+` = 1 niveau, `#` = tout le reste (uniquement dans les **souscriptions**)
5. **QoS 0** = rapide, peut perdre ; **QoS 1** = garanti, peut dupliquer ; **QoS 2** = parfait, lent
6. **LWT** = supervision automatique de la disponibilité d'un équipement
7. **Retained** = nouveau subscriber reçoit immédiatement la dernière valeur connue
8. Dans PubSubClient : **`mqtt.loop()`** doit être appelé dans chaque `loop()` pour traiter les messages entrants

---

**Document – BAC PRO CIEL – A2 – E2/U21 – Version 1.0 – 2026**
