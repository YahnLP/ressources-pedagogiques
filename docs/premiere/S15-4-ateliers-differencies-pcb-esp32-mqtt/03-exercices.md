# 🔬 ATELIERS DE REMÉDIATION CIBLÉE — S15 · 2ᵉ ANNÉE · E2
## 4 Ateliers Différenciés : PCB · ESP32/MQTT · Fiabilité · CEM

---

> **Nom** : ___________________________
> **Atelier(s) choisi(s) selon diagnostic** : ☐ A — PCB  ☐ B — ESP32/MQTT  ☐ C — Fiabilité  ☐ D — CEM

---

## 🟦 ATELIER A — PCB et KiCad (pour score < 4/5 en thème 1)

**Durée cible : 30 min · KiCad disponible**

### Rappel express (5 min)

```
FLUX KICAD en 30 secondes :
  Schéma (ERC=0) → Empreintes → Update PCB → Contour → Placement → Routage → DRC → Gerber

CALQUES ESSENTIELS :
  F.Cu = pistes avant (rouge)  ·  B.Cu = pistes arrière (bleu)
  Edge.Cuts = contour (jaune)  ·  F.Silkscreen = sérigraphie (blanc)

RÈGLES MINIMALES :
  Clearance ≥ 0,2 mm  ·  Piste signal : 0,35 mm  ·  Piste power : 0,8 mm
  Via : 0,8 mm ext / 0,4 mm perçage
```

### Exercice A1 — Identifier les erreurs dans ce schéma KiCad (10 min)

> Description d'un schéma KiCad avec des problèmes :

```
Schéma : LED + résistance + alimentation 5V

  [+5V] ─── [R1] ─── [D1 LED] ─── GND
  
Erreurs à trouver (il y en a 4) :

  1. La résistance R1 n'a pas de valeur saisie (champ Value vide)
     → Problème : ___________________________________________________________
     → Correction : __________________________________________________________

  2. Il n'y a pas de PWR_FLAG sur le net +5V
     → Problème visible : ____________________________________________________
     → Correction : __________________________________________________________

  3. La LED D1 est branchée avec la cathode vers le +5V (sens inversé)
     → Problème : ___________________________________________________________
     → Correction : __________________________________________________________

  4. ERC signale "Pin not connected" sur la broche "K" de la LED
     → Raison : ______________________________________________________________
     → Correction : __________________________________________________________
```

### Exercice A2 — Calculer la clearance (5 min)

```
Un PCB a :
  Piste A : largeur 0,35 mm
  Piste B : largeur 0,35 mm
  Distance bord à bord entre les deux pistes : 0,12 mm

La clearance configurée est 0,20 mm.

Y a-t-il une violation DRC ? ☐ Oui ☐ Non
De combien ? _______ mm (si violation)
Que fait le DRC dans ce cas : ________________________________________________
```

### Exercice A3 — Questions gerber (10 min)

```
Q.A.3a — Quels fichiers Gerber sont obligatoires pour commander un PCB chez JLCPCB ?
Citer au moins 5 :
  1. ___________________________  4. ___________________________
  2. ___________________________  5. ___________________________
  3. ___________________________

Q.A.3b — Après export, quelle étape de vérification est recommandée avant d'envoyer au fabricant ?
_______________________________________________________________________________

Q.A.3c — Dans GerbView, que signifient les zones NOIRES sur le calque F.Mask ?
_______________________________________________________________________________
```

---

## 🟩 ATELIER B — ESP32, WiFi, MQTT, Node-RED (pour score < 4/5 en thème 2)

**Durée cible : 30 min · Arduino IDE disponible**

### Rappel express (5 min)

```
ESP32 :
  Mode STA   : WiFi.begin(ssid, pass)  → IP par DHCP
  Mode AP    : WiFi.softAP(ssid, pass) → IP = 192.168.4.1
  WebServer  : server.on("/route", handler)  +  server.handleClient() dans loop()

MQTT :
  3 acteurs : Publisher · Subscriber · Broker
  mqtt.connect(client_id) · mqtt.subscribe(topic) · mqtt.publish(topic, msg)
  mqtt.loop() dans loop() = OBLIGATOIRE
  Client ID UNIQUE par ESP32 !

NODE-RED :
  msg.payload = la donnée  ·  msg.topic = nom de la série (chart)
  Deploy = valider les modifications
  Dashboard : http://localhost:1880/ui
```

### Exercice B1 — Corriger ce code Arduino (15 min)

> Ce code contient 4 erreurs. Identifie-les et corrige-les.

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid    = "MonWifi";
const char* pass    = "monpass";
const char* broker  = "broker.hivemq.com";
const char* topic   = "ecole/salle/temp";

WiFiClient   client;
PubSubClient mqtt(client);

void setup() {
  Serial.begin(9600);                // Erreur 1 : _________________________
  WiFi.begin(ssid, pass);
  while (WiFi.status() == WL_CONNECTED) { delay(500); }  // Erreur 2 : ____
  
  mqtt.setServer(broker, 1883);
  mqtt.connect("ESP32");             // Erreur 3 : _________________________
  mqtt.subscribe(topic);
}

void loop() {
  float temp = 23.5;
  mqtt.publish(topic, String(temp).c_str());
  delay(5000);                       // Erreur 4 : _________________________
}
```

```
Erreur 1 : _____________________ · Correction : ______________________________
Erreur 2 : _____________________ · Correction : ______________________________
Erreur 3 : _____________________ · Correction : ______________________________
Erreur 4 : _____________________ · Correction : ______________________________
```

### Exercice B2 — Node-RED (10 min)

```
Q.B.2a — Décris le flow minimum pour recevoir un message MQTT et afficher
          la valeur de "temperature" sur une gauge dashboard :
  
  Nœud 1 : ____________________ → Rôle : ______________________________________
  Nœud 2 : ____________________ → Rôle : ______________________________________
  Nœud 3 : ____________________ → Rôle : ______________________________________
  Nœud 4 : ____________________ → Rôle : ______________________________________

Q.B.2b — Un apprenant constate que sa gauge ne se met pas à jour.
          Le debug montre que msg.payload = '{"temperature":23.5}'.
          Que faut-il ajouter entre mqtt-in et la gauge ?

  → Problème : msg.payload est de type _____________ (pas un nombre)
  → Solution : ajouter le nœud __________________ puis un nœud function :
    msg.payload = __________________________________;
    return msg;

Q.B.2c — Pour afficher 3 courbes (température, humidité, CO₂) sur UN SEUL chart,
          que doit contenir msg.topic dans chaque flow ?

  Flow 1 (temp) → msg.topic = "_______________"
  Flow 2 (hum)  → msg.topic = "_______________"
  Flow 3 (CO₂)  → msg.topic = "_______________"
```

---

## 🟧 ATELIER C — Fiabilité : MTBF, MTTR, R(t) (pour score < 2/3 en thème 4)

**Durée cible : 30 min · Calculatrice obligatoire**

### Rappel express (3 min)

λ = 1/MTBF               MTBF = TO/n           MTTR = TA/n  
D = MTBF/(MTBF+MTTR)     R(t) = e^(−λt)        F(t) = 1 − R(t)  

À t = MTBF : R = e⁻¹ = 0,368 (36,8% encore OK)  

Série    : Rs = R1 × R2 × R3  
Parallèle: Rs = 1 − (1−R1)(1−R2)(1−R3)  

$$e⁻⁰ \cdot ¹=0{,}905 e⁻⁰ \cdot ^2=0{,}819 e⁻⁰ \cdot ^3=0{,}741 e⁻⁰ \cdot ⁵=0{,}607 e⁻¹=0{,}368$$

### Exercice C1 — MTBF/MTTR/D (10 min)

Un automate industriel a fonctionné 2 ans (24h/24) et a subi 5 pannes :  
Panne 1 : 2h00   Panne 2 : 30 min   Panne 3 : 45 min  
Panne 4 : 3h15   Panne 5 : 1h30  

a) TA total = _______ h  

$$b) TO = 2 \times 8760 - TA = \underline{\hspace{2.5em}} h$$

c) MTBF = TO / n = _______ h = _______ jours  
d) MTTR = TA / n = _______ h  
e) D = MTBF / (MTBF + MTTR) = _______  = _______ %  
f) Exigence D ≥ 99,9% : ☐ Conforme ☐ Non conforme  

### Exercice C2 — Loi exponentielle (10 min)

Capteur DHT22 : MTBF = 50 000 h  

$$a) λ = \dfrac{1}{50000} = \underline{\hspace{2.5em}} h⁻¹$$

b) R après 1 an (8760h) :  

$$λt = \underline{\hspace{2.5em}} \times 8760 = \underline{\hspace{2.5em}}$$

$$R(8760) = e^(\underline{\hspace{2.5em}}) = \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %$$

c) Sur 200 capteurs, après 1 an : _______ encore fonctionnels  

d) Pour R(t) ≥ 90% :  

$$e^(-λt) \geq 0{,}90 \to -λt \geq ln(0{,}90) \approx -0{,}105$$

t ≤ 0,105 / λ = _______ h = _______ mois  

### Exercice C3 — Système mixte (10 min)

![Système à étudier : capteurs A et B en parallèle, puis CPU et réseau en série](images/rbd-exercice.png)

```
a) R_capteurs (parallèle) = 1 − (1 − _______)(1 − _______) = _______

b) Rs global = _______ × _______ × _______ = _______ = _______ %

c) Quel est le maillon le plus faible ? _________ (R = _______)

d) Si on ajoute un C identique à B en parallèle :
   R_B-nouveau = 1 − (0,20)(0,20) = _______
   R_capteurs-nouveau = 1 − (0,15)(______) = _______
   Rs-nouveau = _______ × 0,95 × 0,98 = _______ %
   Gain : _______ points
```

---

## 🟥 ATELIER D — CEM (pour score < 3/4 en thème 5)

**Durée cible : 30 min · Calculatrice disponible**

### Rappel express (3 min)

```
3 acteurs : Source → Couplage → Victime
4 couplages : Résistif (masse commune) · Capacitif (pistes proches)
              Inductif (boucle courant) · Rayonné (ondes EM)

Conduit < 30 MHz (câbles) · Rayonné > 30 MHz (ondes)

Blindage : continu + mis à la masse · fente < λ/20
Découplage : 100nF + 10µF au plus près du CI (<1mm)
Ferrite : absorbe l'énergie HF sur les câbles
Plan de masse : continu → courant de retour direct → petite boucle → peu de rayonnement
Fente dans le plan → détour → grande boucle → fort rayonnement !

fc filtre RC = 1 / (2π × R × C)
```

### Exercice D1 — Couplages (10 min)

```
Pour chaque situation, identifie le type de couplage dominant et propose une solution :

Situation 1 : Une piste UART (transitions à 115200 baud) passe parallèle
              sur 8 cm à côté d'une piste de capteur analogique.
  Couplage : ________________   Solution : ______________________________________

Situation 2 : Un relais 12V commute un moteur. Le courant du moteur passe
              dans le même fil de masse que le microcontrôleur voisin.
  Couplage : ________________   Solution : ______________________________________

Situation 3 : Un téléphone 4G posé sur une table perturbe les données WiFi
              d'un ESP32 situé à 30 cm.
  Couplage : ________________   Solution : ______________________________________
```

### Exercice D2 — Calculs CEM (10 min)

a) Un boîtier doit bloquer les rayonnements WiFi (2,4 GHz).  
Quelle est la taille maximale des fentes d'aération ?  

$$λ = 3 \times 10⁸ / 2{,}4 \times 10⁹ = \underline{\hspace{2.5em}} m = \underline{\hspace{2.5em}} cm$$

Fente max = λ/20 = _______ cm = _______ mm  

b) Un filtre RC protège un ADC. Le signal utile est à 5 Hz maximum.  
On veut fc = 50 Hz. Avec R = 33 kΩ, calculer C :  

$$C = \dfrac{1}{2π \times fc \times R} = \dfrac{1}{2π \times \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}}}$$

C = _______ F = _______ nF (valeur commerciale : _______ nF)  

c) À partir de quelle fréquence une piste de 20 cm se comporte-t-elle comme une antenne ?  

$$L > λ/20 \to λ < 20 \times 0{,}20 = \underline{\hspace{2.5em}} m$$

$$f > c/λ = 3 \times 10⁸ / \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} MHz$$

### Exercice D3 — Règles PCB CEM (10 min)

```
Classe chaque affirmation comme VRAIE (V) ou FAUSSE (F) :

___ 1. Un plan de masse avec une fente améliore le blindage entre les deux zones.
___ 2. Le condensateur de découplage doit être au plus près du CI pour être efficace.
___ 3. Les émissions conduites se propagent par les ondes radio.
___ 4. Une ferrite absorbe l'énergie HF et la dissipe en chaleur.
___ 5. GND (masse logique) et Terre (PE) sont toujours le même conducteur.
___ 6. Plus une boucle de courant est grande, plus elle rayonne.
___ 7. Un filtre RC passe-bas laisse passer les fréquences inférieures à fc.
___ 8. En mode AP, l'ESP32 peut aussi être connecté à un réseau WiFi (STA) simultanément.

Pour chaque FAUSSE : corriger en une phrase :
  N°___ : ____________________________________________________________________
  N°___ : ____________________________________________________________________
```

---
