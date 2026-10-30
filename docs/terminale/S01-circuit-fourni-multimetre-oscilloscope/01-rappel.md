# 📖 Rappel essentiel : mesurer, comparer, conclure

> Cette page te remet en mémoire, **avant le TP**, ce qu'il faut savoir pour mesurer une carte et conclure. Elle se suffit à elle-même.

## 🤔 À ton avis ?

Tu mesures une résistance marquée 10 kΩ et tu lis 9,7 kΩ. La carte est-elle bonne ?

??? question "Voir une réponse possible"
    On ne peut pas répondre sans **tolérance**. Si la tolérance est ± 5 %, la plage est de 9,5 à 10,5 kΩ : **9,7 kΩ est conforme**. Si elle est ± 1 %, la plage est de 9,9 à 10,1 kΩ : **non conforme**.

## 1. La méthode en trois temps

**Plage → mesure → verdict.** On **calcule d'abord** la plage acceptable, on **mesure** ensuite, puis on **compare** et on écrit le verdict avec les chiffres.

$$\text{plage} = \text{nominal} \pm \text{tolérance}\,\% \qquad \text{écart}\,\% = \frac{|\text{mesure} - \text{nominal}|}{\text{nominal}} \times 100$$

**Exemple** (autre valeur que le TP) : 4,7 kΩ ± 5 %, mesure 4,52 kΩ → plage de 4,465 à 4,935 kΩ ; écart = 3,8 % ; le verdict est **conforme**.

## 2. Les gestes qui évitent les erreurs

| Mesure | Geste | Piège classique |
|---|---|---|
| **Résistance** | Circuit **éteint**, composant **isolé** si possible | Mesure sous tension ou en parallèle d'autres composants : valeur fausse |
| **Tension** | Voltmètre **en parallèle**, rouge sur +, noir sur la masse | Mauvais calibre ou sonde sur la mauvaise broche |
| **Diode** | Mode **test diode** | Se tromper de sens : on attend **0,5 à 0,7 V** dans un sens et **OL** dans l'autre |
| **Signal** | Oscilloscope : sonde compensée, masse **sur la masse**, bon déclenchement | Couplage AC/DC oublié |

## 3. Capteur et incertitude : ce qu'il faut savoir

Un capteur comme le DHT22 a une **précision** annoncée (par exemple ± 0,5 °C). Tes mesures peuvent être **décalées** (le **biais**) et **dispersées** (l'**écart-type**). On évite de toucher le capteur avec les doigts : sa température change vite.

## 4. Lire un signal à l'oscilloscope

Période *T* (en s) → fréquence $f = \dfrac{1}{T}$. Rapport cyclique = durée à l'état haut / période. Un signal logique d'un ESP32 passe de **0 V à environ 3,3 V**.

## 5. Le mini-PV

> [!TIP] 💡 Les 5 éléments d'un PV
> **1** Identification (date, opérateur, conditions) · **2** Tableau de résultats (attendu, mesuré, verdict) · **3** Décision (conforme, sous réserve, refusée) · **4** Motif en deux lignes **chiffrées** · **5** **Signature**.

??? tip "💡 Aide : ordres de grandeur pour vérifier ta réponse"
    - **Résistance** : si ton écart est **supérieur à 10 %**, refais la mesure (sondes mal posées ?) avant de conclure « non conforme ».
    - **Tension 3,3 V** : la mesure sur une carte alimentée par USB est généralement **entre 3,2 et 3,4 V**.
    - **Courant dans la LED** : $I = \dfrac{V_{CC} - V_{LED}}{R}$ donne souvent **quelques mA** ; il doit rester **sous 20 mA**.
    - **Bruit d'alimentation** : quelques **dizaines de mV** crête-à-crête sont courants ; plusieurs **centaines** indiquent un problème de découplage.

## ✅ Vérifie que tu as compris

**Q1.** Pourquoi calcule-t-on la plage avant de mesurer ?

??? success "Réponse"
    Pour que le verdict soit **objectif** : on ne choisit pas la tolérance en fonction de ce qu'on a mesuré.

**Q2.** Tu mesures une résistance en laissant le circuit alimenté. Que risque-t-il d'arriver ?

??? success "Réponse"
    La valeur sera **fausse** (courants parasites des autres composants) et l'instrument peut être **endommagé**.

**Q3.** Un signal carré a une période de 20 ms. Quelle est sa fréquence ?

??? success "Réponse"
    $f = \dfrac{1}{0{,}020} = 50\,\mathrm{Hz}$.
