# 🔬 ATELIERS DE REMÉDIATION CIBLÉE — S15 · 2ᵉ ANNÉE · E2
## 4 Ateliers Différenciés : PCB · ESP32/MQTT · Fiabilité · CEM

---

> **Nom** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Atelier(s) choisi(s) selon diagnostic** : ☐ A — PCB  ☐ B — ESP32/MQTT  ☐ C — Fiabilité  ☐ D — CEM

---

## 🟦 ATELIER A — PCB et KiCad (pour score < 4/5 en thème 1)

**Durée cible : 30 min · KiCad disponible**

### Rappel express (5 min)

> [!NOTE] Mémo KiCad en 30 secondes
>
> **Flux de travail** : Schéma (ERC = 0) → Empreintes → Update PCB → Contour → Placement → Routage → DRC → Gerber
>
> | Calque | Rôle | Couleur |
> |---|---|---|
> | F.Cu | pistes face avant | rouge |
> | B.Cu | pistes face arrière | bleu |
> | Edge.Cuts | contour de la carte | jaune |
> | F.Silkscreen | sérigraphie | blanc |
>
> **Règles minimales** : clearance $\geq 0{,}2$ mm · piste de signal $0{,}35$ mm · piste de puissance $0{,}8$ mm · via : $0{,}8$ mm extérieur / $0{,}4$ mm de perçage.

### Exercice A1 — Identifier les erreurs dans ce schéma KiCad (10 min)

> Description d'un schéma KiCad avec des problèmes :

![Schéma contenant quatre erreurs à trouver](images/schema-erreurs-erc.png)

**Erreurs à trouver (il y en a 4).** Pour chacune, indique le problème et la correction :

1. La résistance R1 n'a pas de valeur saisie (champ *Value* vide).  
   Problème : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
   Correction : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2. Il n'y a pas de PWR_FLAG sur le net +5V.  
   Problème visible : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
   Correction : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3. La LED D1 est branchée avec la cathode vers le +5V (sens inversé).  
   Problème : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
   Correction : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4. L'ERC signale « Pin not connected » sur la broche « K » de la LED.  
   Raison : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
   Correction : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"

    1. Valeur vide → impossible de lire ou commander le composant, BOM incomplète. Correction : renseigner le champ Value (par exemple 330 Ω).  
    2. Pas de PWR_FLAG → l'ERC signale « power pin not driven » : KiCad ne sait pas qu'une source alimente ce net. Correction : poser un PWR_FLAG sur +5V.  
    3. LED inversée → elle ne s'allume jamais. Correction : anode côté +5V (via la résistance), cathode vers GND.  
    4. Raison : la cathode (K) n'est reliée à rien. Correction : la relier à GND (ou poser un No Connect si la broche est volontairement libre).

### Exercice A2 — Calculer la clearance (5 min)

Un PCB comporte deux pistes :

| Piste A | Piste B | Distance bord à bord | Clearance configurée |
|---|---|---|---|
| largeur 0,35 mm | largeur 0,35 mm | **0,12 mm** | **0,20 mm** |

- Y a-t-il une violation DRC ? ☐ Oui ☐ Non
- De combien ? \_\_\_\_\_\_\_ mm (s'il y a violation)
- Que fait le DRC dans ce cas ? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **Oui**, il y a violation : $0{,}20 - 0{,}12 = 0{,}08\,\mathrm{mm}$ de moins que le minimum. Le DRC place un **marqueur d'erreur** sur le PCB à cet endroit ; il ne bloque pas la fabrication, mais la carte n'est pas conforme tant que l'erreur n'est pas corrigée (écarter les pistes).

### Exercice A3 — Questions gerber (10 min)

**Q.A.3a** — Quels fichiers Gerber sont obligatoires pour commander un PCB chez JLCPCB ? Citer au moins 5 :

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
3. \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
4. \_\_\_\_\_\_\_\_\_\_\_\_\_\_  
5. \_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Q.A.3b** — Après export, quelle étape de vérification est recommandée avant d'envoyer au fabricant ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Q.A.3c** — Dans GerbView, que signifient les zones NOIRES sur le calque F.Mask ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **Q.A.3a** — F.Cu, B.Cu, F.Mask, B.Mask, F.Silkscreen, Edge.Cuts, plus le fichier de perçage (.drl).  
    **Q.A.3b** — **Ouvrir les fichiers dans un visualiseur** (GerbView ou visualiseur en ligne) pour vérifier ce qui sera réellement fabriqué.  
    **Q.A.3c** — Les zones noires indiquent les **ouvertures du masque de soudure** : le cuivre y reste apparent (pastilles à souder).

---

## 🟩 ATELIER B — ESP32, WiFi, MQTT, Node-RED (pour score < 4/5 en thème 2)

**Durée cible : 30 min · Arduino IDE disponible**

### Rappel express (5 min)

> [!NOTE] Mémo ESP32 · MQTT · Node-RED
>
> **ESP32**
>
> | Mode / outil | Instruction | Résultat |
> |---|---|---|
> | Station (STA) | `WiFi.begin(ssid, pass)` | IP attribuée par DHCP |
> | Point d'accès (AP) | `WiFi.softAP(ssid, pass)` | IP = 192.168.4.1 |
> | WebServer | `server.on("/route", handler)` + `server.handleClient()` dans `loop()` | Page servie par l'ESP32 |
>
> **MQTT** : 3 acteurs (*Publisher*, *Subscriber*, *Broker*) · `mqtt.connect(client_id)` · `mqtt.subscribe(topic)` · `mqtt.publish(topic, msg)` · **`mqtt.loop()` dans `loop()` est OBLIGATOIRE** · **client ID UNIQUE** par ESP32.
>
> **Node-RED** : `msg.payload` = la donnée · `msg.topic` = nom de la série (chart) · *Deploy* = valider les modifications · tableau de bord : `http://localhost:1880/ui`

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

??? success "Réponses"
    1. `Serial.begin(9600)` : sur ESP32, utiliser **115200** (messages de démarrage lisibles).  
    2. `while (WiFi.status() == WL_CONNECTED)` : condition **inversée** ; il faut `!=`.  
    3. `mqtt.connect("ESP32")` : identifiant **non unique** et connexion **non testée** ; utiliser un ID unique et vérifier le retour de `connect`.  
    4. `delay(5000)` + absence de `mqtt.loop()` : le client MQTT n'est jamais entretenu ; appeler `mqtt.loop()` à chaque tour de `loop()` et remplacer `delay` par `millis()`.  
    *(Le repérage exact des 4 erreurs est une proposition à valider par l'enseignant.)*


| Erreur | Ce qui ne va pas | Correction |
|---|---|---|
| 1 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 2 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 3 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 4 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

### Exercice B2 — Node-RED (10 min)

**Q.B.2a** — Décris le flow minimum pour recevoir un message MQTT et afficher la valeur de « temperature » sur une gauge du dashboard :

| Nœud | Nom du nœud | Rôle |
|---|---|---|
| 1 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 2 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 3 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| 4 | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

**Q.B.2b** — Un apprenant constate que sa gauge ne se met pas à jour. Le debug montre que `msg.payload = '{"temperature":23.5}'`. Que faut-il ajouter entre *mqtt-in* et la gauge ?

- Problème : `msg.payload` est de type \_\_\_\_\_\_\_\_\_\_\_\_\_\_ (ce n'est pas un nombre).
- Solution : ajouter le nœud \_\_\_\_\_\_\_\_\_\_\_\_\_\_, puis un nœud *function* : `msg.payload = \_\_\_\_\_\_\_\_; return msg;`

**Q.B.2c** — Pour afficher 3 courbes (température, humidité, CO₂) sur **un seul** chart, que doit contenir `msg.topic` dans chaque flow ?

| Flow | Grandeur | `msg.topic` |
|---|---|---|
| 1 | température | « \_\_\_\_\_\_\_\_\_\_\_\_\_\_ » |
| 2 | humidité | « \_\_\_\_\_\_\_\_\_\_\_\_\_\_ » |
| 3 | CO₂ | « \_\_\_\_\_\_\_\_\_\_\_\_\_\_ » |

??? success "Réponses"
    **Q.B.2a** — Nœud 1 : `mqtt in` → reçoit le message ; nœud 2 : `json` → convertit la chaîne en objet ; nœud 3 : `function` → extrait `msg.payload.temperature` ; nœud 4 : `ui_gauge` → affiche la valeur.  
    **Q.B.2b** — `msg.payload` est de type **chaîne (string)** ; ajouter un nœud **json** puis un nœud function : `msg.payload = msg.payload.temperature;`.  
    **Q.B.2c** — `msg.topic = "temperature"`, `msg.topic = "humidite"`, `msg.topic = "co2"` : un topic **différent** par courbe.

---

## 🟧 ATELIER C — Fiabilité : MTBF, MTTR, R(t) (pour score < 2/3 en thème 4)

**Durée cible : 30 min · Calculatrice obligatoire**

### Rappel express (3 min)

| Grandeur | Formule |
|---|---|
| Taux de panne | $\lambda = \dfrac{1}{\mathrm{MTBF}}$ |
| MTBF (temps moyen entre pannes) | $\mathrm{MTBF} = \dfrac{TO}{n}$ |
| MTTR (temps moyen de réparation) | $\mathrm{MTTR} = \dfrac{TA}{n}$ |
| Disponibilité | $D = \dfrac{\mathrm{MTBF}}{\mathrm{MTBF} + \mathrm{MTTR}}$ |
| Fiabilité à l'instant $t$ | $R(t) = e^{-\lambda t}$ |
| Défiabilité | $F(t) = 1 - R(t)$ |
| À $t = \mathrm{MTBF}$ | $R = e^{-1} \approx 0{,}368$ (36,8 % encore en état de marche) |
| Système en **série** | $R_s = R_1 \times R_2 \times R_3$ |
| Système en **parallèle** | $R_s = 1 - (1 - R_1)(1 - R_2)(1 - R_3)$ |

**Valeurs utiles de $e^{-x}$ :**

| $x$ | 0,1 | 0,2 | 0,3 | 0,5 | 1 |
|---|---|---|---|---|---|
| $e^{-x}$ | 0,905 | 0,819 | 0,741 | 0,607 | 0,368 |

### Exercice C1 — MTBF/MTTR/D (10 min)

Un automate industriel a fonctionné 2 ans (24 h/24) et a subi 5 pannes :

| Panne 1 | Panne 2 | Panne 3 | Panne 4 | Panne 5 |
|---|---|---|---|---|
| 2 h 00 | 30 min | 45 min | 3 h 15 | 1 h 30 |

**a)** $TA_{\text{total}} =$ \_\_\_\_\_\_\_ h

**b)** $TO = 2 \times 8760 - TA =$ \_\_\_\_\_\_\_ h

**c)** $\mathrm{MTBF} = \dfrac{TO}{n} =$ \_\_\_\_\_\_\_ h $=$ \_\_\_\_\_\_\_ jours

**d)** $\mathrm{MTTR} = \dfrac{TA}{n} =$ \_\_\_\_\_\_\_ h

**e)** $D = \dfrac{\mathrm{MTBF}}{\mathrm{MTBF} + \mathrm{MTTR}} =$ \_\_\_\_\_\_\_ $=$ \_\_\_\_\_\_\_ %

**f)** Exigence $D \geq 99{,}9\ \%$ : ☐ Conforme ☐ Non conforme

??? success "Réponses"
    a) $TA = 2 + 0{,}5 + 0{,}75 + 3{,}25 + 1{,}5 = 8\,\mathrm{h}$.  
    b) $TO = 2 \times 8760 - 8 = 17\,512\,\mathrm{h}$.  
    c) $MTBF = \dfrac{17\,512}{5} = 3\,502{,}4\,\mathrm{h} \approx 146$ jours.  
    d) $MTTR = \dfrac{8}{5} = 1{,}6\,\mathrm{h}$.  
    e) $D = \dfrac{3\,502{,}4}{3\,502{,}4 + 1{,}6} \approx 0{,}9995 = 99{,}95\,\%$.  
    f) $99{,}95\,\% \geq 99{,}9\,\%$ : **conforme**.

### Exercice C2 — Loi exponentielle (10 min)

Capteur DHT22 : $\mathrm{MTBF} = 50\,000$ h

**a)** $\lambda = \dfrac{1}{50\,000} =$ \_\_\_\_\_\_\_ $\mathrm{h^{-1}}$

**b)** Fiabilité après 1 an (8760 h) :

- $\lambda t =$ \_\_\_\_\_\_\_ $\times\ 8760 =$ \_\_\_\_\_\_\_
- $R(8760) = e^{-\lambda t} = e^{-\ldots} =$ \_\_\_\_\_\_\_ $=$ \_\_\_\_\_\_\_ %

**c)** Sur 200 capteurs, après 1 an : \_\_\_\_\_\_\_ encore fonctionnels

**d)** Pour $R(t) \geq 90\ \%$ : $e^{-\lambda t} \geq 0{,}90 \Rightarrow \lambda t \leq -\ln(0{,}90) \approx 0{,}105$

$t \leq \dfrac{0{,}105}{\lambda} =$ \_\_\_\_\_\_\_ h $=$ \_\_\_\_\_\_\_ mois

??? success "Réponses"
    a) $\lambda = \dfrac{1}{50\,000} = 2 \times 10^{-5}\,\mathrm{h^{-1}}$.  
    b) $\lambda t = 2 \times 10^{-5} \times 8760 = 0{,}1752$ ; $R(8760) = e^{-0{,}1752} \approx 0{,}839 = 83{,}9\,\%$.  
    c) $200 \times 0{,}839 \approx 168$ capteurs encore fonctionnels.  
    d) $t \leq \dfrac{0{,}105}{2 \times 10^{-5}} \approx 5\,270\,\mathrm{h} \approx 7{,}2$ mois.

### Exercice C3 — Système mixte (10 min)

![Système à étudier : capteurs A et B en parallèle, puis CPU et réseau en série](images/rbd-exercice.png)

**a)** $R_{\text{capteurs}} = 1 - (1 - \ldots)(1 - \ldots) =$ \_\_\_\_\_\_\_ *(branches en parallèle)*

**b)** $R_s = \ldots \times \ldots \times \ldots =$ \_\_\_\_\_\_\_ $=$ \_\_\_\_\_\_\_ %

**c)** Quel est le maillon le plus faible ? \_\_\_\_\_\_\_\_\_ ($R =$ \_\_\_\_\_\_\_)

**d)** On ajoute un capteur C identique à B, en parallèle :

- $R_{B,\text{nouveau}} = 1 - (0{,}20)(0{,}20) =$ \_\_\_\_\_\_\_
- $R_{\text{capteurs,nouveau}} = 1 - (0{,}15)(\ldots) =$ \_\_\_\_\_\_\_
- $R_{s,\text{nouveau}} = \ldots \times 0{,}95 \times 0{,}98 =$ \_\_\_\_\_\_\_ %
- Gain : \_\_\_\_\_\_\_ points

??? success "Réponses"
    a) $R_{capteurs} = 1 - (1 - 0{,}85)(1 - 0{,}80) = 1 - 0{,}15 \times 0{,}20 = 0{,}97$.  
    b) $R_s = 0{,}97 \times 0{,}95 \times 0{,}98 \approx 0{,}903 = 90{,}3\,\%$.  
    c) Dans la chaîne en série, le maillon le plus faible est le **CPU** ($R = 0{,}95$) ; le composant individuellement le moins fiable est le capteur B ($R = 0{,}80$), mais la mise en parallèle le compense.  
    d) $R_{B,nouveau} = 1 - 0{,}2 \times 0{,}2 = 0{,}96$ ; $R_{capteurs,nouveau} = 1 - 0{,}15 \times 0{,}04 = 0{,}994$ ; $R_{s,nouveau} = 0{,}994 \times 0{,}95 \times 0{,}98 \approx 0{,}925 = 92{,}5\,\%$ ; gain : environ **+2,2 points**.

---

## 🟥 ATELIER D — CEM (pour score < 3/4 en thème 5)

**Durée cible : 30 min · Calculatrice disponible**

### Rappel express (3 min)

> [!NOTE] Mémo CEM
>
> - **3 acteurs** : Source → Couplage → Victime.
> - **4 couplages** : résistif (masse commune) · capacitif (pistes proches) · inductif (boucle de courant) · rayonné (ondes EM).
> - **Conduit** $< 30$ MHz (câbles) · **rayonné** $> 30$ MHz (ondes).
> - **Blindage** : continu et mis à la masse ; fente $< \lambda/20$.
> - **Découplage** : 100 nF + 10 µF au plus près du CI ($< 1$ mm).
> - **Ferrite** : absorbe l'énergie HF sur les câbles.
> - **Plan de masse** continu → courant de retour direct → petite boucle → peu de rayonnement ; **fente** dans le plan → détour → grande boucle → fort rayonnement.
> - **Filtre RC** : $f_c = \dfrac{1}{2\pi R C}$

### Exercice D1 — Couplages (10 min)

Pour chaque situation, identifie le type de couplage dominant et propose une solution :

**Situation 1.** Une piste UART (transitions à 115 200 baud) passe parallèle, sur 8 cm, à côté d'une piste de capteur analogique.

- Couplage : \_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Solution : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Situation 2.** Un relais 12 V commute un moteur. Le courant du moteur passe dans le même fil de masse que le microcontrôleur voisin.

- Couplage : \_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Solution : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Situation 3.** Un téléphone 4G posé sur une table perturbe les données WiFi d'un ESP32 situé à 30 cm.

- Couplage : \_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Solution : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"

    - **Situation 1** : couplage **capacitif** (pistes parallèles proches). Solution : éloigner les pistes ou intercaler une piste de garde à la masse.  
    - **Situation 2** : couplage **résistif** (impédance commune de la masse). Solution : masses séparées reliées en un seul point, diode de roue libre sur le relais.  
    - **Situation 3** : couplage **rayonné**. Solution : éloigner le téléphone, blinder le boîtier, filtrer.

### Exercice D2 — Calculs CEM (10 min)

a) Un boîtier doit bloquer les rayonnements WiFi (2,4 GHz).  
Quelle est la taille maximale des fentes d'aération ?  

$$\lambda  = 3 \times 10^{8} / 2{,}4 \times 10^{9} = \underline{\hspace{2.5em}} m = \underline{\hspace{2.5em}} cm$$

Fente max = λ/20 = \_\_\_\_\_\_\_ cm = \_\_\_\_\_\_\_ mm  

b) Un filtre RC protège un ADC. Le signal utile est à 5 Hz maximum.  
On veut fc = 50 Hz. Avec R = 33 kΩ, calculer C :  

$$C = \dfrac{1}{2\pi  \times fc \times R} = \dfrac{1}{2\pi  \times \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}}}$$

C = \_\_\_\_\_\_\_ F = \_\_\_\_\_\_\_ nF (valeur commerciale : \_\_\_\_\_\_\_ nF)  

c) À partir de quelle fréquence une piste de 20 cm se comporte-t-elle comme une antenne ?  

$$L > \lambda /20 \to \lambda  < 20 \times 0{,}20 = \underline{\hspace{2.5em}} m$$

$$f > c/\lambda  = 3 \times 10^{8} / \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} \mathrm{MHz}$$

??? success "Réponses"
    a) $\lambda = \dfrac{3 \times 10^{8}}{2{,}4 \times 10^{9}} = 0{,}125\,\mathrm{m} = 12{,}5\,\mathrm{cm}$ ; fente max $= \dfrac{\lambda}{20} = 0{,}625\,\mathrm{cm} = 6{,}25\,\mathrm{mm}$.  
    b) $C = \dfrac{1}{2\pi \times 50 \times 33\,000} \approx 9{,}6 \times 10^{-8}\,\mathrm{F} \approx 96\,\mathrm{nF}$ ; valeur commerciale : **100 nF**.  
    c) $\lambda < 20 \times 0{,}20 = 4\,\mathrm{m}$ ; $f > \dfrac{3 \times 10^{8}}{4} = 75\,\mathrm{MHz}$.

### Exercice D3 — Règles PCB CEM (10 min)

Classe chaque affirmation comme **VRAIE (V)** ou **FAUSSE (F)** :

| N° | Affirmation | V / F |
|---|---|---|
| 1 | Un plan de masse avec une fente améliore le blindage entre les deux zones. | \_\_\_ |
| 2 | Le condensateur de découplage doit être au plus près du CI pour être efficace. | \_\_\_ |
| 3 | Les émissions conduites se propagent par les ondes radio. | \_\_\_ |
| 4 | Une ferrite absorbe l'énergie HF et la dissipe en chaleur. | \_\_\_ |
| 5 | GND (masse logique) et Terre (PE) sont toujours le même conducteur. | \_\_\_ |
| 6 | Plus une boucle de courant est grande, plus elle rayonne. | \_\_\_ |
| 7 | Un filtre RC passe-bas laisse passer les fréquences inférieures à $f_c$. | \_\_\_ |
| 8 | En mode AP, l'ESP32 peut aussi être connecté à un réseau WiFi (STA) simultanément. | \_\_\_ |

Pour chaque affirmation FAUSSE, corrige-la en une phrase :

- N° \_\_\_ : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- N° \_\_\_ : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    1 **F** ; 2 **V** ; 3 **F** ; 4 **V** ; 5 **F** ; 6 **V** ; 7 **V** ; 8 **V**.  
    Corrections : 1 — une fente **dégrade** le blindage (le courant de retour fait un détour : grande boucle) ; 3 — les émissions conduites se propagent **par les câbles**, pas par ondes ; 5 — la masse logique et la terre (PE) sont **deux conducteurs distincts** (reliés en un point si nécessaire).

---
