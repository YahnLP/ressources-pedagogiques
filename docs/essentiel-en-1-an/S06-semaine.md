# Semaine 6 : Le système communicant : UART, I²C, WiFi, MQTT et supervision

> **Durée** : 4 h · **Compétences E2 travaillées** : C07 · C11

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Expliquer la chaîne capteur → microcontrôleur → réseau → supervision.
- Lire une trame UART et calculer sa durée.
- Reconnaître un bus I²C et son adresse.
- Décrire un échange MQTT (broker, topic, JSON).
- Diagnostiquer une liaison qui ne fonctionne pas.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | TP virtuels ElectroLab : analyseur logique, UART, I²C |
| 1 h | Cours : protocoles et MQTT |
| 1 h | Atelier : trames, topics, supervision |
| 1 h | Diagnostic d'une liaison ; auto-test |

## 🖥️ TP virtuel dans ElectroLab : à faire avant le TP réel

Ouvre [ElectroLab](https://yahnlp.github.io/ElectroLab/), menu **TP ▾**, puis fais ces TP **avant** de toucher au matériel :

- **Prise en main de l'analyseur logique (chronogrammes d'un compteur)** (45 min, niveau première)
- **Analyse d'une liaison série UART / RS-232 (5 variantes)** (1 h 30, niveau première / terminale)
- **Analyse d'un bus I²C : adresse, ACK, résistances de rappel (4 cas)** (1 h 45, niveau terminale)

> [!TIP] 🖥️ Pourquoi d'abord le simulateur ?
> On peut se tromper sans rien casser, répéter autant de fois que nécessaire et obtenir une correction automatique. Le TP réel sert ensuite à **confirmer** et à manipuler le vrai matériel.

## 📖 Le cours en bref

**🤔 À ton avis ?** Ton capteur de température est dans une salle, ton écran de contrôle dans un bureau. Comment la valeur voyage-t-elle jusqu'à lui ?

??? question "Réponse"
    Par une **liaison** (série, I²C, WiFi) qui suit un **protocole** : des règles communes de format et de vitesse. On étudie les plus courantes.

### 1. Pourquoi et comment communiquer

Un système communicant suit une **chaîne** : **capteur → microcontrôleur → réseau → supervision** (écran, tableau de bord, alarme). Chaque maillon doit **parler la même langue** que le suivant : c'est le rôle des **protocoles**.

### 2. La liaison série UART

Les bits partent **un par un** sur un fil, à une vitesse commune (**baud rate**, par exemple 9600). Une trame **8N1** contient **10 bits** : 1 bit de départ (0), 8 bits de données (le moins significatif d'abord), 1 bit d'arrêt (1).

$$T_{bit} = \frac{1}{\text{baud}} \qquad \text{à 9600 bauds : } T_{bit} \approx 104\,\mathrm{\mu s}\ ;\ \text{un octet} \approx 1{,}04\,\mathrm{ms}$$

**Câblage** : TX d'un côté vers **RX** de l'autre (et inversement) + **masse commune**. Même vitesse des deux côtés, sinon : caractères absurdes.

### 3. Le bus I²C

Deux fils seulement : **SDA** (données) et **SCL** (horloge), partagés par plusieurs appareils. Chaque appareil a une **adresse** (par exemple `0x27` pour un écran LCD). Les deux lignes ont des **résistances de rappel** (≈ 4,7 kΩ) vers le +V. Sur l'Arduino Uno : SDA = A4, SCL = A5.

### 4. WiFi et MQTT avec l'ESP32

L'**ESP32** se connecte au WiFi (mode **station**) ou crée son propre réseau (mode **point d'accès**, adresse 192.168.4.1). Ses broches fonctionnent en **3,3 V** : ne jamais y appliquer 5 V.

**MQTT** : un **broker** (serveur) reçoit les messages d'un **publisher** et les redistribue aux **subscribers** abonnés au même **topic** (par exemple `salle1/temperature`). Port **1883** (8883 avec TLS). Les topics sont **sensibles à la casse**. Caractères joker : `+` (un niveau) et `#` (tous les niveaux suivants). Le contenu est souvent un texte **JSON** : `{"temp": 23.5}`.

### 5. Superviser : moyenne, seuil, hystérésis

Pour fiabiliser une mesure, on calcule des **indicateurs** (KPI) :

- **Moyenne mobile** des N dernières mesures : elle lisse le bruit (20, 22, 21, 25 → 22).
- **Seuil avec hystérésis** : l'alarme se **déclenche** à 30 °C mais ne se **coupe** qu'en dessous de 28 °C : on évite le battement autour d'un seul seuil.
- **Trois niveaux** : normal, avertissement, critique.

### 6. Diagnostiquer une liaison

Dans l'ordre : **alimentation** ; **câblage** (TX ↔ RX croisés, masse commune) ; **vitesse** identique ; **niveaux** de tension compatibles (3,3 V / 5 V) ; **adresse** I²C correcte ; **IP du broker** et **topic** (casse !) pour MQTT. Un outil précieux : le **moniteur série** et l'**analyseur logique**.


## 🛠️ Atelier guidé : on construit, on mesure, on valide

**Fil rouge 2 : la station de mesure communicante.**

1. **Trame UART** : écris la trame de la lettre `A` (code `0x41`) en 8N1 (bit de départ, 8 bits de données le moins significatif d'abord, bit d'arrêt).
2. **Durées** : durée d'un octet à 9600 bauds, puis à 115200 bauds.
3. **Topics MQTT** : propose les topics pour 3 salles (température) et le topic qui permet de s'abonner aux 3 salles.
4. **Hystérésis** : seuils 30 °C (déclenchement) et 28 °C (retour) ; suite de mesures : 29,5 ; 30,5 ; 29,5 ; 28,5 ; 27,9. Donne l'état de l'alarme pour chaque mesure.
5. **Niveaux** : un signal de 5 V doit entrer dans l'ESP32 : propose un diviseur 1 kΩ / 2 kΩ et calcule la tension.

??? success "Résultats attendus"
    1. `0x41` = 01000001 ; bits envoyés dans l'ordre : **0** (départ), **1 0 0 0 0 0 1 0**, **1** (arrêt).
    2. 9600 bauds : environ **1,04 ms** ; 115200 bauds : environ **87 µs**.
    3. `salle1/temperature`, `salle2/temperature`, `salle3/temperature` ; abonnement `salle/+/temperature` si les topics sont `salle/1/temperature`… (ou `+/temperature`).
    4. OK, **ALARME**, ALARME, ALARME, **OK**.
    5. $5 \times \dfrac{2}{1+2} \approx 3{,}33\,\mathrm{V}$.

## ✍️ Exercices d'application

1. Quelle différence entre UART et I²C ?
2. À quoi sert l'adresse I²C ?
3. Moyenne mobile de 18, 20, 22, 24 ?
4. Pourquoi une hystérésis ?

??? success "Corrigés"
    1. L'**UART** relie **deux** appareils (TX/RX, vitesse commune) ; l'**I²C** relie **plusieurs** appareils sur 2 fils (SDA, SCL) grâce aux **adresses**.
    2. À **repérer** chaque appareil sur le bus.
    3. $\dfrac{84}{4} = 21$.
    4. Pour éviter que l'alarme **bat** (s'allume et s'éteigne sans arrêt) autour d'un seul seuil.

## 📚 Pour approfondir : les séances à consulter

- [Seconde S13 – liaison série UART](../seconde/S13-communication-serie-uart-protocol/01-cours.md)
- [Seconde S15 – LCD I²C](../seconde/S15-lcd-i2c-bibliotheque-affichage/01-cours.md)
- [Première S06 – ESP32 WiFi](../premiere/S06-esp32-wifi-modes-station-ap-webserver/01-cours.md)
- [Première S07 – MQTT](../premiere/S07-mqtt-publish-subscribe-topics-qos/01-cours.md)
- [Terminale S04 – KPI et alarme embarquée](../terminale/S04-acquisition-capteur-courbe-kpi-alarme/01-cours.md)

## ✅ Auto-test

1. Combien de bits dans une trame 8N1 ?
2. Durée d'un octet à 9600 bauds ?
3. Un ESP32 reçoit un signal de 5 V sur une broche : problème ?
4. `Salle1/temp` et `salle1/temp` : même topic ?
5. Quel port utilise MQTT sans chiffrement ?

??? success "Réponses"
    1. **10 bits** (1 départ + 8 données + 1 arrêt).
    2. $10 \times 104\,\mathrm{\mu s} \approx 1{,}04\,\mathrm{ms}$.
    3. Oui : ses broches sont en **3,3 V** ; il faut un diviseur de tension ou un convertisseur de niveau.
    4. **Non** : les topics sont **sensibles à la casse**.
    5. **1883**.

## 📦 Livrable

Schéma de la chaîne de ta station de mesure (capteur, microcontrôleur, protocole, topic MQTT) avec les valeurs choisies.
