# 🔄 FICHES DE REMÉDIATION EXPRESS — S1 · 3ᵉ ANNÉE · E2
## Synthèses Ciblées par Domaine · Rattrapage Rapide des Bases A2

---

> **Usage** : À lire en priorité selon les lacunes identifiées au diagnostic.
> Chaque fiche = 15-20 minutes de lecture + 1 exercice d'application rapide.

---

## 🟦 FICHE R1 — PCB KiCad (si score < 5/7)

### L'essentiel en 5 lignes

```
FLUX : Schéma (ERC=0) → Empreintes → Update PCB → Edge.Cuts → Placement → Routage → DRC → Gerber

CALQUES : F.Cu=pistes avant(rouge) · B.Cu=pistes arrière(bleu) · Edge.Cuts=contour(jaune)

RÈGLES : Clearance≥0,2mm · Signal 0,35mm · Alim 0,8mm · Via: Ø ext 0,8mm / perçage 0,4mm

DÉCOUPLAGE : 100nF au plus proche du CI (<2mm) · Via GND court · B=remplir le plan de masse

ERREURS : DRC "Clearance violation"=pistes trop proches · ERC "PWR_FLAG"=alimentation non déclarée
          "Silkscreen clipped"=sérigraphie sur pad · "Unconnected"=ratsnest non routé
```

### Exercice express R1 (10 min)

```
Un PCB a ces caractéristiques :
  - Clearance configurée : 0,20 mm
  - Distance entre piste A et piste B : 0,15 mm
  - Condensateur de découplage à 8 mm du CI
  - Plan de masse B.Cu fendu par une piste

Q1 : Y a-t-il une violation DRC ? ☐ Oui ☐ Non · De combien ? _______ mm
Q2 : Le condensateur est-il bien placé ? ☐ Oui ☐ Non · Règle : _______________
Q3 : Le plan fendu pose-t-il un problème CEM ? ☐ Oui ☐ Non · Raison : __________

```

??? success "Réponses"
    Q1=Oui +0,05mm · Q2=Non (8mm >> 2mm) · Q3=Oui (grande boucle = rayonnement)

---

## 🟩 FICHE R2 — ESP32, WiFi, MQTT (si score < 5/7)

### L'essentiel en 5 lignes

```
STA : WiFi.begin(ssid,pass) → while(status!=WL_CONNECTED){delay(500);} → WiFi.localIP()
AP  : WiFi.mode(WIFI_AP) · WiFi.softAP(ssid,pass) → IP=192.168.4.1

WEBSERVER : server.on("/route",handler) · server.handleClient() dans loop() [OBLIGATOIRE]
            Codes : 200=OK · 302=Redirect · 404=Not Found

MQTT : mqtt.setServer(broker,1883) · mqtt.connect("ID_UNIQUE") · mqtt.subscribe(topic)
       mqtt.publish(topic, payload.c_str()) · mqtt.loop() dans loop() [OBLIGATOIRE]
       
ERREURS : delay() dans loop() → bloque mqtt.loop() → utiliser millis()
          Client ID identique → 2 ESP32 se déconnectent mutuellement
          handleClient() oublié → WebServer muet
```

### Exercice express R2 (10 min)

```
Voici un extrait de code avec des erreurs. Trouve les 3 erreurs :

void setup() {
  Serial.begin(9600);                          // Erreur 1 : _______________
  WiFi.begin("ssid","pass");
  while (WiFi.status() == WL_CONNECTED) {}    // Erreur 2 : _______________
  mqtt.connect("ESP32");                       // Erreur 3 : _______________
}

void loop() {
  delay(10000);
  mqtt.publish("topic","hello");
}
// Bonus : quelle 4ème erreur critique dans loop() ?

```

??? success "Réponses"
    115200 · !=WL_CONNECTED · ID unique · mqtt.loop() absent

---

## 🟧 FICHE R3 — Fiabilité MTBF / R(t) (si score < 4/5)

### L'essentiel en 5 lignes

```
λ = 1/MTBF             MTBF=TO/n · MTTR=TA/n · D=MTBF/(MTBF+MTTR)
R(t) = e^(−λt)         A t=MTBF : R=e⁻¹=0,368=36,8% ← PAS 50% !

SÉRIE    : Rs = R1×R2×R3         → Rs < Rmin (s'affaiblit)
PARALLÈLE: Rs = 1−(1−R1)(1−R2) → Rs > Rmax (se renforce)

VALEURS e⁻ˣ : e⁻⁰·¹=0,905 · e⁻⁰·²=0,819 · e⁻⁰·⁵=0,607 · e⁻¹=0,368
1 an = 8 760 h · 1 mois = 730 h
```

### Exercice express R3 (10 min)

Capteur DHT22 : MTBF = 50 000 h  

$$a) \lambda  = \dfrac{1}{50000} = \underline{\hspace{2.5em}}h^{-1}$$

b) R après 1 an (8760h) :  

$$\lambda t = 2 \times 10^{-5} \times 8760 = \underline{\hspace{2.5em}}$$

$$R = e^{-\underline{\hspace{2.5em}}} = \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %$$

c) Système : [DHT22 (R=0,84)] en série avec [ESP32 (R=0,92)] :  

$$Rs = \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %$$

d) Même système mais DHT22 en double (2 capteurs parallèle) :  

$$R_{\mathrm{capt}}// = 1 - (1-0{,}84)^2 = 1 - \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}}$$

$$Rs_nouveau = \underline{\hspace{2.5em}} \times 0{,}92 = \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %$$

Gain : _______ points  

??? success "Réponses"
    a)$2\times 10^{-5}$ b)0,1752/0,839/83,9% c)0,773/77,3% d)0,0256/0,974 · 0,896 · 89,6% · +12,3pts

---

## 🟥 FICHE R4 — CEM (si score < 4/5)

### L'essentiel en 5 lignes

```
3 ACTEURS : Source → Couplage → Victime  [agir sur le couplage = plus simple]

4 COUPLAGES : Résistif(masse commune) · Capacitif(pistes proches) · Inductif(boucle courant) · Rayonné(ondes)

CONDUIT < 30MHz (câbles) · RAYONNÉ > 30MHz (ondes)

BLINDAGE : continu + masse · fente < λ/20 (λ=3×10⁸/f)  Ex: 2,4GHz → fente<6,25mm
DÉCOUPLAGE : 100nF+10µF au plus proche CI · Ferrite = absorbe HF (≠ filtre qui réfléchit)
PLAN MASSE : CONTINU=petite boucle=peu de rayonnement · FENDU=détour=grande boucle=fort rayonnement
```

### Exercice express R4 (10 min)

```
a) f=100MHz → λ = 3×10⁸/10⁸ = _______ m → fente max = λ/20 = _______ m = _______ cm

b) Filtre RC : R=22kΩ · C=100nF · fc = 1/(2π×22000×100×10⁻⁹) = _______ Hz

c) Quelle violation CEM : condensateur 100nF placé à 15mm de l'ESP32 ?
   ____________________________________________________________________________

d) Plan de masse fendu par une piste d'alimentation : quel problème CEM ?
   ____________________________________________________________________________

```

??? success "Réponses"
    a)3m/0,15m/15cm b)72Hz c)inductance piste → filtre inefficace à HF d)détour courant→grande boucle→rayonnement

---

## 🟪 FICHE R5 — Métrologie PV (si score < 2/3)

### L'essentiel en 5 lignes

```
BIAIS = Σei/n      (erreur systématique · le capteur surestime/sous-estime)
σ = √(Σei²/(n−1)) (écart-type · dispersion aléatoire des mesures)
u = σ/√n           (incertitude type · incertitude sur la moyenne)
U = k×u (k=2)      (incertitude élargie à 95%)

CONFORMITÉ : |Biais| + U ≤ spécification constructeur
             Ex: |0,21| + 0,22 = 0,43°C ≤ 0,5°C → CONFORME ✓
```

### Exercice express R5 (10 min)

5 mesures d'un capteur (référence = 25,0°C) :  
25,3 · 24,9 · 25,2 · 25,4 · 25,2  

ei (écarts) : _______ · _______ · _______ · _______ · _______  

$$Σei = \underline{\hspace{2.5em}} Σei^2 = \underline{\hspace{2.5em}}$$

Biais = _______ / 5 = _______ °C  

$$\sigma  = \sqrt{\underline{\hspace{2.5em}} / 4} = \underline{\hspace{2.5em}} °C$$

$$u = \underline{\hspace{2.5em}} / \sqrt{5} = \underline{\hspace{2.5em}} °C$$

$$U = 2 \times \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} °C$$

Spécification = ±0,5°C :  
|Biais| + U = _______ + _______ = _______ °C  
☐ CONFORME ☐ NON CONFORME  

??? success "Réponses"
    ei=+0,3/-0,1/+0,2/+0,4/+0,2 · Σei=+1,0 · Σei²=0,34  
    Biais=+0,20°C · σ=$\sqrt{0,34/4}$=$\sqrt{0,085}$=0,291°C · u=0,130°C · U=0,260°C  
    0,20+0,26=0,46°C ≤ 0,5°C → CONFORME (limite !)

---

## 🔄 Plan de remédiation selon votre groupe

```
GROUPE A (≥24/30) :
  → Relire uniquement les fiches des 1-2 questions ratées
  → Passer directement au programme A3 dès S2
  
GROUPE B (18-23/30) :
  → Travailler 2 fiches de remédiation ciblées (fiches R correspondantes)
  → Objectif : être à niveau avant S3-3A

GROUPE C (12-17/30) :
  → Travailler toutes les fiches en déficit avant S2
  → S2 = séance de remédiation collective
  → Refaire le QCM entier avant S3

GROUPE D (<12/30) :
  → Entretien individuel avec l'enseignant
  → Programme personnalisé de rattrapage intensif
  → Révision des fiches de cours A2 (docs _03_ de chaque séance)
```

---

*Fiches de Remédiation Express — BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S1*
*À utiliser en autonomie entre S1 et S3*
