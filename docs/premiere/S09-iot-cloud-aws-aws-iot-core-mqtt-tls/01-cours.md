# 📖 FICHE COURS – S9 ANNÉE 2 – E2

> [!NOTE] 🔶 Approfondissement
> Cette partie va **au-delà de l'essentiel** attendu pour l'épreuve E2. À faire **après** le parcours essentiel (voir l'onglet « L'essentiel en 1 an »), si tu as du temps ou si tu vises plus haut.

## IoT Cloud AWS : AWS IoT Core, MQTT TLS, Certificats X.509, CloudWatch

---

## 🎯 OBJECTIFS

- ✅ Décrire l'architecture d'AWS IoT Core et ses composants
- ✅ Expliquer le rôle des certificats X.509 dans la sécurité IoT
- ✅ Configurer un Thing AWS et connecter un ESP32 via MQTT TLS
- ✅ Créer une règle IoT pour router les données vers CloudWatch
- ✅ Lire un dashboard CloudWatch avec des métriques IoT

---

## 1️⃣ DU BROKER LOCAL AU CLOUD : POURQUOI ?

### Les limites de Mosquitto local (S7-A2)

> En S7-A2, votre broker Mosquitto ne fonctionnait que sur votre réseau local. Dans un projet IoT réel :

| **Besoin réel** | **Mosquitto local** | **AWS IoT Core** |
|---|---|---|
| Accessible depuis Internet | ❌ (IP privée, NAT) | ✅ (URL publique mondiale) |
| Haute disponibilité 24/7 | ❌ (si le PC s'éteint…) | ✅ (SLA 99,9%) |
| Sécurité de niveau production | ❌ (anonyme) | ✅ (TLS + X.509) |
| Milliers d'appareils | Difficile | ✅ (millions) |
| Stockage + règles d'automatisation | ❌ | ✅ (DynamoDB, S3, Lambda…) |

---

## 2️⃣ ARCHITECTURE AWS IOT CORE

### Vue d'ensemble

![Architecture AWS IoT Core](images/chaine-aws.png)

### Les 4 composants fondamentaux

| **Composant** | **Rôle** | **Analogie** |
|---|---|---|
| **Thing** | Représentation logique de l'équipement dans AWS | Fiche d'identité de l'ESP32 |
| **Certificat X.509** | Clé d'authentification cryptographique du device | Carte d'identité biométrique |
| **Policy** | Document JSON autorisant les actions (publish, subscribe…) | Carte d'accès avec permissions |
| **Endpoint** | URL unique de connexion MQTT du compte AWS | Adresse du broker cloud |

### L'Endpoint AWS IoT

> Chaque compte AWS a un endpoint unique, de la forme :

```
xxxxxxxxxxxxxxx-ats.iot.eu-west-1.amazonaws.com
       ↑                          ↑
  Identifiant unique du compte    Région AWS
```

> **Important :** L'endpoint contient la région. Toutes vos ressources (Thing, Policy, certificat) doivent être dans la **même région** que l'endpoint.

---

## 3️⃣ SÉCURITÉ : TLS ET CERTIFICATS X.509

### Pourquoi pas un simple mot de passe ?

> Un mot de passe peut être intercepté, deviné, ou partagé par erreur. Dans l'IoT, un appareil compromis pourrait empoisonner toute la plateforme cloud. Les **certificats X.509** offrent une sécurité cryptographique robuste :

| **Mot de passe** | **Certificat X.509** |
|---|---|
| Peut être lu si intercepté | Basé sur la cryptographie asymétrique (RSA/ECDSA) |
| Le serveur stocke une copie | Le serveur ne stocke que la clé publique |
| Partageable facilement | La clé privée ne quitte JAMAIS le device |
| Révocation difficile | Révocation immédiate côté AWS |

### Les 3 fichiers de certificats nécessaires

> [!NOTE] Fichier 1 : AmazonRootCA1.pem
> → Certificat de l'autorité de certification (CA) Amazon  
> → Permet à l'ESP32 de VÉRIFIER que le serveur AWS est légitime  
> → Même fichier pour tous les comptes AWS  
>
> Fichier 2 : device-certificate.pem.crt  
> → Certificat du device (clé publique signée par Amazon)  
> → Permet à AWS de VÉRIFIER que l'ESP32 est autorisé  
> → Spécifique à chaque Thing  
>
> Fichier 3 : private.pem.key  
> → Clé privée du device  
> → Utilisée pour signer la négociation TLS  
> → ⚠️ À NE JAMAIS PARTAGER ni stocker en clair dans un repo Git  

### Authentification mutuelle TLS (Mutual TLS / mTLS)

![TLS standard et mTLS : authentification du serveur seul ou des deux côtés](images/tls-mtls.png)

---

---

## 4️⃣ CRÉER UN THING DANS AWS IOT CORE

### Étapes dans la console AWS

```
Console AWS → IoT Core → Gérer → Objets → Créer un objet

Étape 1 : Nommer l'objet
  Nom : esp32-ciel-[votrenom]
  (pas d'espace, pas de caractère spécial)

Étape 2 : Configurer le certificat
  → "Génération automatique" (recommandé)
  → AWS génère : device cert + private key + public key

Étape 3 : Télécharger les fichiers
  ⚠️ TÉLÉCHARGER MAINTENANT — impossible de les récupérer après
  ✅ device-certificate.pem.crt
  ✅ private.pem.key
  ✅ public.pem.key (optionnel)
  ✅ AmazonRootCA1.pem (bouton séparé)

Étape 4 : Créer et attacher une Policy
  → Nouvelle policy : iot-ciel-lab-policy
  → JSON policy (voir ci-dessous)
  → Attacher au certificat
```

### Policy IoT pour le labo

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Connect",
        "iot:Publish",
        "iot:Subscribe",
        "iot:Receive"
      ],
      "Resource": "*"
    }
  ]
}
```

> **En production :** la Policy restrictive n'autorise que les topics et clientId spécifiques au device. En labo, `*` simplifie la configuration.

---

## 5️⃣ CODE ESP32 POUR AWS IOT CORE

### Bibliothèque recommandée

> **`PubSubClient`** + **`WiFiClientSecure`** (intégré à l'ESP32 Arduino SDK)

```cpp
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>

// ── Certificats (copier le contenu des fichiers téléchargés) ──────
// AmazonRootCA1.pem
const char* ca_cert = R"EOF(
-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
... (contenu complet)
-----END CERTIFICATE-----
)EOF";

// device-certificate.pem.crt
const char* device_cert = R"EOF(
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
)EOF";

// private.pem.key
const char* private_key = R"EOF(
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
)EOF";

// ── Configuration ──────────────────────────────────────────────────
const char* ssid        = "NOM_WIFI";
const char* password    = "MDP_WIFI";
const char* aws_endpoint = "xxxxxxx-ats.iot.eu-west-1.amazonaws.com";
const int   mqtt_port   = 8883;  // TLS obligatoire !
const char* client_id   = "esp32-ciel-alice";

const char* topic_pub  = "esp32/alice/data";
const char* topic_sub  = "esp32/alice/commande";

// ── Objets ─────────────────────────────────────────────────────────
WiFiClientSecure  tlsClient;
PubSubClient      mqtt(tlsClient);

// ── Callback ────────────────────────────────────────────────────────
void callback(char* topic, byte* payload, unsigned int length) {
  String msg = "";
  for (unsigned int i = 0; i < length; i++) msg += (char)payload[i];
  Serial.println("[" + String(topic) + "] " + msg);
}

// ── Connexion Wi-Fi ─────────────────────────────────────────────────
void connectWiFi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println("\nWi-Fi OK → " + WiFi.localIP().toString());
}

// ── Connexion AWS IoT ────────────────────────────────────────────────
void connectAWS() {
  tlsClient.setCACert(ca_cert);          // Vérifier le serveur AWS
  tlsClient.setCertificate(device_cert); // Authentifier ce device
  tlsClient.setPrivateKey(private_key);  // Signer la négociation TLS

  mqtt.setServer(aws_endpoint, mqtt_port);
  mqtt.setCallback(callback);

  while (!mqtt.connected()) {
    Serial.print("Connexion AWS IoT...");
    if (mqtt.connect(client_id)) {
      Serial.println("Connecté !");
      mqtt.subscribe(topic_sub);
    } else {
      Serial.print("Erreur : ");
      Serial.println(mqtt.state());
      delay(5000);
    }
  }
}

// ── Setup ────────────────────────────────────────────────────────────
void setup() {
  Serial.begin(115200);
  connectWiFi();
  connectAWS();
}

// ── Loop ─────────────────────────────────────────────────────────────
void loop() {
  if (!mqtt.connected()) connectAWS();
  mqtt.loop();

  static unsigned long last = 0;
  if (millis() - last > 5000) {
    last = millis();
    float temp = 20.0 + (float)random(0, 100) / 10.0;
    float hum  = 50.0 + (float)random(0, 30);
    String json = "{\"temp\":" + String(temp, 1) +
                  ",\"hum\":"  + String(hum, 0) +
                  ",\"device\":\"" + String(client_id) + "\"}";
    bool ok = mqtt.publish(topic_pub, json.c_str());
    Serial.println(ok ? "✓ " + json : "✗ Erreur publish");
  }
}
```

> **Différence clé avec S7-A2 :**
> - `WiFiClient` → `WiFiClientSecure` (TLS)
> - Port `1883` → Port `8883`
> - Pas de certificats → 3 fichiers PEM intégrés au code
> - Endpoint `localhost` → Endpoint AWS (URL longue)

---

## 6️⃣ IOT RULES : ROUTER LES DONNÉES

### Principe des Règles IoT

> AWS IoT Rules sont des règles SQL-like qui déclenchent des actions quand un message MQTT correspond à un critère. Elles permettent de router les données vers d'autres services AWS sans écrire de code serveur.

![AWS IoT : le Rule Engine distribue les messages (CloudWatch, DynamoDB, Lambda, S3)](images/aws-regles.png)

### Créer une règle IoT vers CloudWatch

```
Console AWS → IoT Core → Règles → Créer une règle

Étape 1 : Nom de la règle
  iot-ciel-temperature-rule

Étape 2 : Instruction SQL
  SELECT temp, hum, timestamp() as timestamp
  FROM 'esp32/+/data'

Étape 3 : Action
  → Envoyer les données du message à CloudWatch
  → Espace de noms : IoT/Capteurs/CIEL
  → Nom de la métrique : Temperature
  → Valeur : ${temp}
  → Unité : None (ou Celsius)
  → Rôle IAM : créer un rôle auto
```

---

## 7️⃣ CLOUDWATCH : DASHBOARD ET MÉTRIQUES

### CloudWatch dans l'architecture AWS

> **CloudWatch** est le service de monitoring d'AWS. Il collecte des métriques (valeurs numériques) et des logs depuis tous les services AWS, y compris les données IoT routées via des règles.

### Types de ressources CloudWatch utilisées en IoT

| **Ressource** | **Rôle** | **Exemple** |
|---|---|---|
| **Métrique** | Série temporelle d'une valeur numérique | Température ESP32 |
| **Dashboard** | Page de graphes personnalisée | "Dashboard Labo CIEL" |
| **Alarm** | Alerte si métrique dépasse un seuil | Temp > 30°C → email |
| **Log Group** | Journaux texte (erreurs, connexions) | Logs MQTT |

### Créer un Dashboard CloudWatch

```
Console AWS → CloudWatch → Dashboards → Créer un dashboard

Ajouter un widget :
  Type : Graphique en courbes (Line)
  Métrique : IoT/Capteurs/CIEL → Temperature
  Période : 1 minute
  Statistique : Moyenne

Ajouter un 2ème widget :
  Type : Jauge (Gauge)
  Métrique : IoT/Capteurs/CIEL → Temperature
  Min : 0, Max : 50
```

---

![Tableau de bord CloudWatch d'un projet IoT ESP32.](images/cloudwatch-dashboard.png)

---

## 8️⃣ COMPARATIF : MOSQUITTO LOCAL vs AWS IOT CORE

| **Critère** | **Mosquitto S7-A2** | **AWS IoT Core S9-A2** |
|---|---|---|
| **Localisation** | PC local | Cloud mondial |
| **Port** | 1883 | **8883 (TLS)** |
| **Sécurité** | Aucune (anonyme) | **X.509 + TLS** |
| **Authentification** | Optionnelle (user/pass) | **Certificats obligatoires** |
| **Scalabilité** | Limité au réseau local | Millions d'appareils |
| **Dashboard intégré** | Non | CloudWatch |
| **Règles de routage** | Non | IoT Rules Engine |
| **Device Shadow** | Non | ✅ Oui |
| **Coût** | Gratuit (open-source) | Pay-per-use (~0,08$/M messages) |
| **Code ESP32 différent ?** | Non (même PubSubClient) | Oui (WiFiClientSecure + certs) |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais décrire les 4 composants AWS IoT Core (Thing, Certificate, Policy, Endpoint)
- [ ] Je comprends pourquoi TLS + certificats X.509 sont nécessaires dans l'IoT cloud
- [ ] Je sais distinguer les 3 fichiers PEM et leur rôle respectif
- [ ] Je comprends l'authentification mutuelle TLS : le client ET le serveur s'authentifient
- [ ] Je sais configurer `WiFiClientSecure` avec les 3 certificats dans le code ESP32
- [ ] Je sais créer une règle IoT SQL pour router les données vers CloudWatch
- [ ] Je sais créer un widget graphique dans un dashboard CloudWatch

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **AWS IoT Core** | Broker MQTT managé cloud d'Amazon, hautement disponible, sécurisé |
| **Thing** | Représentation logique d'un équipement IoT dans le registre AWS |
| **Certificate X.509** | Certificat cryptographique pour l'authentification du device |
| **Private Key** | Clé privée RSA du device — ne quitte JAMAIS le matériel |
| **CA Certificate** | Certificat de l'autorité racine (Amazon Root CA 1) |
| **mTLS** | Mutual TLS — authentification bidirectionnelle client + serveur |
| **Policy IoT** | Document JSON autorisant les opérations MQTT (connect, pub, sub) |
| **Endpoint** | URL de connexion MQTT propre à chaque compte AWS |
| **Port 8883** | Port MQTT avec TLS (vs 1883 sans chiffrement) |
| **IoT Rule** | Règle SQL-like déclenchant des actions sur les messages MQTT |
| **CloudWatch** | Service AWS de monitoring, métriques, dashboards, alarmes |
| **Metric** | Série temporelle d'une valeur numérique dans CloudWatch |
| **Dashboard** | Page de visualisation personnalisée dans CloudWatch |
| **Device Shadow** | JSON représentant l'état désiré / réel d'un objet IoT |

---

## 📌 POINTS-CLÉS À RETENIR

1. AWS IoT Core = Mosquitto cloud + TLS + certificats + règles de routage
2. **3 fichiers obligatoires :** AmazonRootCA1 (vérifier serveur) + device cert (s'identifier) + private key (signer)
3. La **clé privée ne quitte jamais le device** — ne pas la committer dans Git
4. **mTLS** : le device vérifie AWS ET AWS vérifie le device (bidirectionnel)
5. Code ESP32 : `WiFiClient` → `WiFiClientSecure` ; port 1883 → **8883**
6. **IoT Rules** = pipeline sans serveur : MQTT → CloudWatch/DynamoDB/Lambda
7. CloudWatch : métriques = séries temporelles ; dashboards = visualisation ; alarms = alertes
8. Toutes les ressources AWS (Thing, cert, rule) doivent être dans la **même région**

---

**Document – BAC PRO CIEL – A2 – E2/U21 – Version 1.0 – 2026**
