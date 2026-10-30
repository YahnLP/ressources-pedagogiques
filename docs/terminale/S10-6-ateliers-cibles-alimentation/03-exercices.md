# 🔬 ATELIERS DE REMÉDIATION — S10 · 3ᵉ ANNÉE · E2
## 6 Ateliers Ciblés : Alimentation · Métrologie · PCB · IoT · Fiabilité · CEM

---

> **Utiliser selon votre fiche de lacunes personnalisée**
> **Durée par atelier : 80-90 minutes**
> **Calculatrice + fiche de cours autorisées**

---

## 🟦 ATELIER A — Alimentation & Calcul Thermique

> Pour les apprenants ayant < 12/20 en alimentation au S9.

### Rappel express (5 min)

```
Pdiss = (Vin − Vout) × Iout        (régulateur linéaire)
η = Pout / Pin = Vout/Vin           (rendement approché)
Tj = Tamb + Pdiss × Rθja            (sans radiateur)
Tj max exploitable = 105°C (125−20)
I_moy cycle = (I_actif×t1 + I_veille×t2) / (t1+t2)
Autonomie = Capacité(mAh) / I_moy × 0,80
```

### Exercice A1 — Bilan complet (40 min)

Système : traceur GPS IoT outdoor, batterie LiPo 3,7V/2000mAh  

Composants :  
ESP32 actif GPS     : 200 mA @ 3,3V (30s toutes les 10 min)  
ESP32 deep sleep    : 0,02 mA @ 3,3V (reste du temps)  
GPS NEO-6M          : 50 mA @ 3,3V (actif en même temps que l'ESP32)  
LED statut          : 5 mA @ 3,3V (50% duty, toujours)  
Régulateur LDO      : Vin=3,7V, Vout=3,3V, Rθja=44°C/W, Tamb=30°C  

a) Calcule I_moy ESP32 sur un cycle de 10 min (600s) :  

$$I_{\mathrm{moy}} = \dfrac{200 \times 30 + 0{,}02 \times 570}{600} = \underline{\hspace{2.5em}} mA$$

b) Calcule I_moy total @ 3,3V :  
I_moy total = I_ESP32_moy + I_GPS_moy + I_LED_moy  

$$I_GPS_moy = 50 \times \dfrac{30}{600} = \underline{\hspace{2.5em}} mA$$

$$I_LED_moy = 5 \times 0{,}5 = \underline{\hspace{2.5em}} mA$$

I_moy total = _______ mA  

c) Calcule Pdiss LDO et Tj :  
Pdiss = (3,7−3,3) × _______ = _______ W  

$$Tj = 30 + \underline{\hspace{2.5em}} \times 44 = \underline{\hspace{2.5em}} °C$$

☐ OK ☐ Radiateur nécessaire  

d) Autonomie batterie :  
t = 2000 / _______ × 0,80 = _______ h = _______ jours  

### Exercice A2 — Choisir le bon régulateur (20 min)

```
Pour chaque application, justifie le choix et calcule η ou Pdiss :

Application 1 : Véhicule 12V → Raspberry Pi 5V, 3A
  Type choisi : ________________ · η attendu : _______ %
  Pdiss si linéaire : _______ W · Problème : _______________________

Application 2 : Capteur sur Li-ion 3,7V → MCU 3,3V, 30mA
  Type choisi : ________________ · Vdrop = _______ V
  Pdiss = _______ W · Tj = _______ °C

Application 3 : Amplificateur audio précision ±15V → ±12V, 100mA
  Type choisi : ________________ · Raison (lien CEM) : _____________________
```

### Mini-quiz A (10 min)

```
1. Quelle est la formule de Pdiss pour un régulateur linéaire ?
2. Si Tj calculé = 110°C (sans radiateur), que faire ?
3. Avantage principal du convertisseur à découpage sur une batterie ?
4. Formula de l'autonomie avec facteur pratique inclus ?
5. LDO vs LM78xx : quelle est la différence principale ?
```

---

## 🟩 ATELIER B — Métrologie R&R & Limite de Détection

> Pour les apprenants ayant < 12/20 en métrologie au S9.

### Rappel express (5 min)

σ_EV = (σ_A + σ_B) / 2          (répétabilité)  
σ_AV ≈ |x̄_A − x̄_B| / √n        (reproductibilité)  

$$σ_GRR = \sqrt(σ_EV^2 + σ_AV^2)$$

%GRR = 5,15 × σ_GRR / Tolérance × 100  
< 10% = excellent · 10-30% = acceptable · > 30% = inacceptable  
LD ≈ 3 × σ_bruit  

### Exercice B1 — R&R complet (50 min)

> Deux opérateurs mesurent la pression d'un compresseur (consigne 4,0 bar ±0,3 bar).

Capteur 1 (bar) | Capteur 2 (bar)  
Mesure 1 :    3,98       |    4,05  
Mesure 2 :    4,02       |    4,08  
Mesure 3 :    3,97       |    4,03  
Mesure 4 :    4,01       |    4,07  
Mesure 5 :    4,00       |    4,06  
Mesure 6 :    3,99       |    4,04  

Référence : 4,00 bar · Tolérance totale : 0,6 bar  

a) Calcule x̄ et σ de chaque capteur :  

$$x̄_1 = \underline{\hspace{2.5em}} bar \cdot σ_1 = \underline{\hspace{2.5em}} bar$$

$$x̄_2 = \underline{\hspace{2.5em}} bar \cdot σ_2 = \underline{\hspace{2.5em}} bar$$

b) Biais de chaque capteur :  
Biais_1 = _______ · Biais_2 = _______  

c) σ_EV, σ_AV, σ_GRR, %GRR :  

$$σ_EV = \underline{\hspace{2.5em}} \cdot σ_AV = \underline{\hspace{2.5em}} \cdot σ_GRR = \underline{\hspace{2.5em}} \cdot %GRR = \underline{\hspace{2.5em}} %$$

d) Verdict et recommandation :  
☐ Excellent ☐ Acceptable ☐ Inacceptable  
Recommandation : _______________________________________________  

e) LD du capteur 1 :  

$$LD \approx 3 \times σ_1 = \underline{\hspace{2.5em}} bar$$

Peut-il détecter une variation de 0,02 bar ? ☐ Oui ☐ Non  

### Mini-quiz B (10 min)

```
1. Répétabilité = variabilité due à _______ (même/différents opérateurs ?)
2. %GRR > 30% → que faire ?
3. LD ≈ _______ × σ_bruit (règle 3-sigma)
4. Si LD=0,5 bar et variation à détecter=0,2 bar → capteur apte ? ☐ Oui ☐ Non
5. NDC ≥ _______ → instrument distingue les pièces
```

---

## 🟧 ATELIER C — PCB et KiCad

> Pour les apprenants ayant < 9/15 en PCB au S9.

### Rappel express (3 min)

```
Flux : Schéma→ERC→Empreintes→PCB→Edge.Cuts→Placement→Routage→DRC→Gerber
Plan de masse CONTINU → petit boucle → peu de rayonnement ✓
Condensateur découplage : 100nF + 10µF, au plus proche du CI (<2mm)
Clearance ≥ 0,2mm · Signal 0,35mm · Alim 0,8mm
```

### Exercice C1 — Identifier 5 violations dans ce PCB (30 min)

```
Description d'un PCB défaillant pour un ESP32 + DHT22 + LED :

  • Condensateur de découplage 100nF placé à 12mm des pins VCC/GND de l'ESP32
  • Plan de masse B.Cu fendu par une piste d'alimentation 5V
  • Piste de signal DHT22 de 18cm (straight run)
  • Sérigraphie "R1" superposée sur le pad de la résistance
  • Clearance entre piste GND et piste VCC : 0,15mm (règle = 0,20mm)
  • Résistance pull-up DHT22 sans valeur saisie (champ Value vide)

Remplir :

Violation 1 : _______________ · Problème CEM : _______________ · Correction : _______________
Violation 2 : _______________ · Problème : _______________ · Correction : _______________
Violation 3 : _______________ · Problème : _______________ · Correction : _______________
Violation 4 : _______________ · Problème : _______________ · Correction : _______________
Violation 5 : _______________ · Problème : _______________ · Correction : _______________
```

### Exercice C2 — Calcul fréquence antenne (15 min)

a) Piste de 18cm : à partir de quelle fréquence se comporte-t-elle comme une antenne ?  

$$L=0{,}18\,\mathrm{m} \cdot L > λ/20 \to λ < 20 \times 0{,}18=3{,}6\,\mathrm{m} \cdot f > 3 \times 10⁸/3{,}6 = \underline{\hspace{2.5em}} MHz$$

b) Pour le WiFi ESP32 (2,4GHz), λ/20 = _______ mm  
Toute piste > _______ mm peut rayonner → règle : pistes courtes !  

c) Fente dans un boîtier blindant à 2,4GHz : taille max ?  

$$λ=0{,}125\,\mathrm{m} \to λ/20 = \underline{\hspace{2.5em}} mm$$

### Mini-quiz C (10 min)

```
1. ERC = vérification _______ · DRC = vérification _______
2. F.Mask : les zones NOIRES représentent quoi ?
3. Via standard : Ø ext = _______ mm / perçage = _______ mm
4. Condensateur découplage : distance max au CI = _______ mm
5. Commande KiCad : X=piste · V=via · B=_______ · Alt+3=_______
```

---

## 🟥 ATELIER D — ESP32, MQTT, Node-RED, InfluxDB

> Pour les apprenants ayant < 12/20 en IoT au S9.

### Rappel express (3 min)

```cpp
// STA : WiFi.begin(ssid,pass) · while(status!=WL_CONNECTED){delay(500);}
// AP  : WiFi.mode(WIFI_AP) · WiFi.softAP(ssid,pass) · IP=192.168.4.1
// WebServer : server.on("/r",h) · server.handleClient() // loop() !
// MQTT : mqtt.connect("ID_UNIQUE") · mqtt.subscribe(t) · mqtt.publish(t,msg)
//        mqtt.loop() // loop() OBLIGATOIRE
// delay() dans loop() → bloque mqtt.loop() → utiliser millis() !
```

### Exercice D1 — Corriger ce code (25 min)

```cpp
// Ce code a 5 erreurs. Trouve-les et corrige-les.

#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Labo"; const char* pass = "pass";
WiFiClient w; PubSubClient mqtt(w);

void onMessage(char* t, byte* p, unsigned int l) {
  String msg = String((char*)p);
  if (msg == "ON") digitalWrite(2, HIGH);
}

void setup() {
  Serial.begin(9600);                           // Erreur 1 : _______________
  WiFi.begin(ssid, pass);
  while (WiFi.status() == WL_CONNECTED) {}     // Erreur 2 : _______________
  
  mqtt.setServer("broker.hivemq.com", 1883);
  mqtt.connect("ESP32");                        // Erreur 3 : _______________
  mqtt.setCallback(onMessage);                  // Erreur 4 : _______________
  mqtt.subscribe("salle/led");
}

void loop() {
  delay(5000);                                  // Erreur 5 : _______________
  mqtt.publish("salle/temp", "23.5");
}
```

### Exercice D2 — Node-RED flow (30 min)

```
Décrire ou dessiner le flow Node-RED qui :
1. Reçoit les données MQTT du topic "salle/+/data" (JSON {temp, hum})
2. Parse le JSON
3. Affiche la température sur une gauge (0-50°C, zones couleur)
4. Affiche un graphe historique température (30 derniers points)
5. Déclenche une alerte si temp > 35°C → notification + mqtt-out
6. Stocke tout dans InfluxDB (measurement="salle_data", tags={site})

Nœuds utilisés (dans l'ordre) :
  ___________________________________________________________________________
  
Code function "Parser" (2 outputs : gauge/chart en sortie 1, InfluxDB en sortie 2) :
```
```javascript
var data = msg.payload;
if (!data || data.temp === undefined) { return null; }

var msgVisu = { ______________________________________ };
var msgDB   = { ______________________________________ };

return [msgVisu, msgDB];
```

### Mini-quiz D (10 min)

```
1. IP ESP32 en mode AP = _______
2. handleClient() dans loop() : ☐ obligatoire ☐ optionnel
3. msg.topic dans un chart Node-RED = _______ de la courbe
4. Format influxdb-out : msg.payload = [{_______________, tags{}, fields{}}]
5. delay(5000) dans loop() est problématique car : _______________________
```

---

## 🟨 ATELIER E — Fiabilité MTBF / R(t)

> Pour les apprenants ayant < 9/15 en fiabilité au S9.

### Rappel express (3 min)

```
λ=1/MTBF · MTBF=TO/n · MTTR=TA/n · D=MTBF/(MTBF+MTTR)
R(t)=e^(−λt) · R(MTBF)=e⁻¹=0,368 ← jamais 50% !
Série    : Rs=R1×R2×R3     (affaiblit)
Parallèle: Rs=1−(1−R1)(1−R2)  (renforce)
e⁻⁰·¹=0,905 · e⁻⁰·²=0,819 · e⁻⁰·⁵=0,607 · e⁻¹=0,368
```

### Exercice E1 — Système IoT industriel (50 min)

```
Architecture d'un système de pesée industrielle :
  [Capteur A (R=0,88)] ─┐
                         ├──→ [IHM (R=0,97)] ──→ [Réseau (R=0,99)]
  [Capteur B (R=0,82)] ─┘

Données : Capteur A MTBF=60000h · Capteur B MTBF=40000h · Tamb=25°C

a) Fiabilité bloc capteurs en parallèle :
   R_capt = 1−(1−0,88)(1−0,82) = _______ = _______%

b) Rs global :
   Rs = _______ × 0,97 × 0,99 = _______ = _______%

c) R après 1 an (8760h) si on utilise uniquement Capteur A (MTBF=60000h) :
   λA = 1/60000 = _______ h⁻¹
   λA × t = _______ × 8760 = _______
   R_A(8760) = e^(_______) = _______ = _______%

d) Sur 200 capteurs A mis en service simultanément, combien fonctionnent encore après 1 an ?
   _______ × 200 = _______ capteurs

e) Système de pesée MTBF=10000h, MTTR=4h :
   D = 10000 / (10000+4) = _______ = _______%
```

### Mini-quiz E (10 min)

```
1. R(MTBF) = _______ % (pas 50 !)
2. Rs série : Rs ☐ < ☐ > ☐ = Rmin
3. Rs parallèle 2 composants R=0,9 : Rs = 1−(0,1)² = _______%
4. λ = _______ / MTBF
5. D = MTBF / (_______ + _______)
```

---

## 🟪 ATELIER F — CEM

> Pour les apprenants ayant < 6/10 en CEM au S9.

### Rappel express (3 min)

```
Source → Couplage → Victime  (4 couplages : résistif/capacitif/inductif/rayonné)
Conduit < 30MHz · Rayonné > 30MHz
Blindage : continu + masse · fente < λ/20 (λ=3×10⁸/f)
Découplage : 100nF au plus proche CI (<2mm)
Ferrite : absorbe HF sur câbles
Plan CONTINU → petite boucle ✓ · Plan FENDU → grande boucle ✗
fc = 1/(2π×R×C)
```

### Exercice F1 — Identifier couplages et solutions (30 min)

```
Décrire le type de couplage ET proposer une solution pour chaque scénario :

Scénario 1 : Un relais 24V commute un moteur. La masse de ce circuit est partagée avec
  le microcontrôleur ESP32. Quand le relais commute, l'ESP32 redémarre.
  Couplage : _______ · Explication : _______________________
  Solution 1 : __________________ · Solution 2 : __________________

Scénario 2 : Deux pistes PCB parallèles sur 12cm :
  Piste 1 = signal PWM 20kHz · Piste 2 = signal ADC capteur analogique
  Couplage : _______ · Solution PCB : _______________________

Scénario 3 : Câble d'alimentation 5V (2A) cheminant sur 30cm à côté d'un câble
  de données UART. Les données sont corrompues lors de fortes charges.
  Couplage : _______ · Solution câblage : _______________________
```

### Exercice F2 — Calculs (25 min)

a) Boîtier blindant un ESP32 WiFi (2,4GHz) : taille max des fentes ?  

$$λ = 3 \times 10⁸/2{,}4 \times 10⁹ = \underline{\hspace{2.5em}} m \cdot λ/20 = \underline{\hspace{2.5em}} mm$$

b) Filtre RC pour ADC (signal utile max 20Hz, fc cible 100Hz, R=22kΩ) :  

$$C = \dfrac{1}{2π \times 100 \times 22000} = \underline{\hspace{2.5em}} F = \underline{\hspace{2.5em}} nF$$

c) Piste PCB de 22cm : fréquence à partir de laquelle elle devient une antenne ?  

$$λ < 20 \times 0{,}22 = \underline{\hspace{2.5em}} m \cdot f > 3 \times 10⁸/\underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} MHz$$

d) 8 affirmations : VRAI ou FAUX  
___ Plan de masse continu : courant de retour direct sous la piste  
___ Ferrite : réfléchit les signaux HF (≠ les absorbe)  
___ Condensateur découplage à 15mm du CI : efficacité optimale  
___ Conduites < 30MHz : se propagent par l'air  
___ Plan fendu : grande boucle → fort rayonnement  
___ Blindage relié à la masse en 2 points : recommandé  
___ LDO : génère moins de bruit HF qu'un buck → meilleur pour CEM signal  
___ fc = 1/(2πRC) : formule filtre passe-bas  

### Mini-quiz F (10 min)

1. 4 types de couplage : _______ · _______ · _______ · _______  
2. Conduites = < _______ MHz · Rayonnées = > _______ MHz  
3. Fente dans blindage WiFi (2,4GHz) < _______ mm  
4. Plan fendu → courant de retour _______ → grande _______ → fort _______  

$$5. fc = \dfrac{1}{2π \times \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}}}$$

---
