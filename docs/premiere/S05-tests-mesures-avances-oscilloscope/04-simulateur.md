# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans [ElectroLab](https://yahnlp.github.io/ElectroLab/), clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## Lire un signal à l'oscilloscope : régler, mesurer T, f, $U_{max}$, $U_{pp}$… (6 signaux)

*Bac Pro CIEL (seconde / première) · durée indicative : 1 h 15*

Un générateur délivre un signal <b>inconnu</b> (réglages masqués), de fréquence et d'amplitude très variables. L'oscilloscope est volontairement mal réglé : il faut choisir <b>sensibilité verticale</b> (V/div) et <b>base de temps</b> (s/div) pour obtenir une belle image, puis lire toutes les caractéristiques du signal.

### 🎯 Objectifs

- Régler V/div pour que le signal occupe au moins la moitié de l'écran sans sortir
- Régler s/div pour voir quelques périodes (2 à 10)
- Lire T, en déduire f = 1/T
- Lire $U_{max}$, $U_{min}$, $U_{pp}$, en déduire amplitude et valeur moyenne
- Distinguer valeur moyenne (V⎓) et efficace (V∿) et les comparer au calcul

### 🛠️ Marche à suivre

1. Câblez <b>CH1 → sortie du GBF</b> (R1 côté GBF) et <b>GND → masse</b>. Ouvrez l'oscilloscope.
2. Le signal est invisible ou écrasé : appuyez sur <b>Auto</b> puis affinez. <b>Règle</b> : ≈ 2 à 10 périodes à l'écran (s/div) ; signal sur 4 à 6 divisions de haut (V/div) sans sortir de l'écran.
3. Comptez les divisions : <b>T = nombre de divisions × s/div</b> ; <b>$U_{pp}$ = nombre de divisions × V/div</b>. Utilisez aussi les mesures affichées sous l'écran pour vérifier.
4. Câblez MM1 (V⎓) et MM2 (V∿) aux bornes de R1 : valeur moyenne et valeur efficace de la partie alternative.
5. Identifiez la forme et répondez aux questions.

### ❓ Questions

1. Forme du signal  
    - ☐ Sinusoïdale  
    - ☐ Carrée  
    - ☐ Triangulaire
2. Période T (en ms)
3. Fréquence f (en Hz)
4. Tension maximale $U_{max}$ (en V)
5. Tension minimale $U_{min}$ (en V)
6. Tension crête à crête $U_{pp}$ (en V)
7. Valeur moyenne (composante continue), lue en V⎓ (en V)
8. Valeur efficace de la partie alternative, lue en V∿ (en V)
9. Pour un signal alternatif <b>sinusoïdal</b> sans composante continue, la valeur efficace vaut…  
    - ☐ $U_{max}$ / √2 ≈ 0,707·$U_{max}$  
    - ☐ $U_{max}$ / 2  
    - ☐ $U_{pp}$  
    - ☐ $U_{max}$ × √2

### 📥 Fichiers à ouvrir dans ElectroLab

- [`osc_lect-v1.json`](tp/osc_lect-v1.json) — Autre signal n° 1
- [`osc_lect-v2.json`](tp/osc_lect-v2.json) — Autre signal n° 2

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Lire un signal à l'oscilloscope : régler, mesurer T, f, $U_{max}$, $U_{pp}$… (6 signaux)*.

## Prise en main de l'analyseur logique (chronogrammes d'un compteur)

*Bac Pro CIEL (première) · durée indicative : 45 min*

Avant d'analyser des liaisons série, apprenez à vous servir de l'<b>analyseur logique</b> sur un signal que vous connaissez : un compteur 4 bits piloté par un NE555. Vous allez le câbler, régler base de temps, déclenchement et seuil, puis mesurer des périodes avec les curseurs.

### 🎯 Objectifs

- Câbler plusieurs voies et la masse de l'analyseur
- Régler la base de temps pour voir plusieurs périodes
- Utiliser le déclenchement (voie, front) pour stabiliser l'affichage
- Mesurer une période avec les curseurs et en déduire une fréquence
- Lire un compteur sur un chronogramme

### 🛠️ Marche à suivre

1. Câblez <b>D0 → Q0</b>, <b>D1 → Q1</b>, <b>D2 → Q2</b>, <b>D3 → Q3</b> du compteur U2, et <b>GND → masse</b>. Double-clic sur LA pour ouvrir la fenêtre (le <b>❓ Guide d'utilisation</b> en bas de la fenêtre résume chaque réglage).
2. Appuyez sur <b>Auto</b> : la base de temps se règle toute seule. Réglez-la ensuite à la main pour voir <b>au moins une période complète de Q3</b> (la plus lente).
3. Déclenchement : choisissez la <b>voie D0, front montant</b> : l'image devient stable. Appuyez sur <b>STOP</b> pour figer la capture.
4. Avec les <b>curseurs</b> (glisser sur le chronogramme), mesurez la période de Q0 et celle de Q3. Comparez : Q3 est ___ fois plus lente.
5. Le seuil logique doit convenir à un signal 0 / 5 V : vérifiez qu'il vaut environ 1,65 V. Répondez aux questions.

### ❓ Questions

1. Période de l'horloge CK du NE555 (en µs)
2. Période de Q0 (en µs)
3. Période de Q3 (en ms)
4. Q3 est plus lente que Q0 d'un facteur…
5. Pourquoi faut-il relier la broche GND de l'analyseur à la masse du montage ?  
    - ☐ Pour alimenter l'analyseur  
    - ☐ Pour que les tensions soient mesurées par rapport à la même référence (sans masse commune, aucun niveau n'est lu)  
    - ☐ Pour augmenter la vitesse  
    - ☐ Ce n'est pas nécessaire
6. À quoi sert le déclenchement ?  
    - ☐ À amplifier le signal  
    - ☐ À démarrer l'affichage toujours au même événement (un front) pour obtenir une image stable  
    - ☐ À choisir la couleur des voies  
    - ☐ À éteindre l'instrument

### 📥 Fichiers à ouvrir dans ElectroLab

- [`la_intro-v1.json`](tp/la_intro-v1.json) — Autre horloge n° 1

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Prise en main de l'analyseur logique (chronogrammes d'un compteur)*.

## Analyse d'un bus I²C : adresse, ACK, résistances de rappel (4 cas)

*Bac Pro CIEL (terminale) · durée indicative : 1 h 45*

Un maître I²C communique avec un esclave sur deux lignes : <b>SCL</b> (horloge) et <b>SDA</b> (données). Capturez la transaction, décodez adresse et données et diagnostiquez : esclave présent (ACK) ou absent (NACK) ? Certains cas demandent de câbler les <b>résistances de rappel</b> (bus à drain ouvert).

### 🎯 Objectifs

- Câbler l'analyseur sur SCL et SDA
- Reconnaître START (SDA↓ pendant SCL = 1), STOP, ACK / NACK
- Décoder l'adresse 7 bits et le bit R/W, puis les données
- Comprendre pourquoi le bus I²C exige des résistances de rappel (pull-up)

### 🛠️ Marche à suivre

1. Câblez <b>D0 → SCL</b>, <b>D1 → SDA</b>, <b>GND → masse</b>. Si le bus est « à plat » (aucun signal haut), il manque des <b>résistances de rappel</b> : reliez SCL et SDA au +3,3 V par $R_{P1}$, $R_{P2}$ (4,7 kΩ).
2. Décodeur <b>I²C</b> : SCL = D0, SDA = D1. Seuil 1,65 V.
3. Lisez : adresse 7 bits, bit R/W, ACK de l'esclave, octets de données.
4. Mesurez la période de SCL pour en déduire la fréquence du bus.
5. Répondez aux questions.

### ❓ Questions

1. Adresse 7 bits de l'esclave (décimal)
2. Premier octet envoyé après le START (adresse + R/W), en décimal
3. Sens du transfert  
    - ☐ Écriture (le maître envoie des données)  
    - ☐ Lecture (le maître reçoit des données)
4. Réponse à l'adresse  
    - ☐ ACK : l'esclave répond  
    - ☐ NACK : personne ne répond à cette adresse
5. Nombre d'octets de données transférés après l'adresse
6. Valeur (décimale) du premier octet de données (0 s'il n'y en a pas)
7. Fréquence de l'horloge SCL (en kHz)
8. Pourquoi SCL et SDA ont-elles besoin de résistances de rappel ?  
    - ☐ Pour limiter le courant dans les LED  
    - ☐ Les sorties sont à drain ouvert : elles ne savent que tirer la ligne à 0, la résistance la ramène à 1  
    - ☐ Pour filtrer les parasites  
    - ☐ Pour adapter l'impédance

### 📥 Fichiers à ouvrir dans ElectroLab

- [`i2c-v1.json`](tp/i2c-v1.json) — Autre cas n° 1
- [`i2c-v2.json`](tp/i2c-v2.json) — Autre cas n° 2

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Analyse d'un bus I²C : adresse, ACK, résistances de rappel (4 cas)*.

## Analyse d'un bus SPI : retrouver le mode (CPOL / CPHA) (4 cas)

*Bac Pro CIEL (terminale) · durée indicative : 1 h 30*

Un maître SPI échange des octets avec un esclave. Le <b>mode SPI</b> (CPOL, CPHA) est inconnu : un mauvais mode donne des octets décalés ou faux. Observez le niveau de repos de SCK et le front d'échantillonnage, trouvez le mode et décodez les données.

### 🎯 Objectifs

- Câbler les 4 signaux SPI à l'analyseur (CS, SCK, MOSI, MISO)
- Déterminer CPOL (niveau de repos de SCK) et CPHA (front d'échantillonnage)
- Décoder les octets envoyés (MOSI) et reçus (MISO)
- Comprendre le rôle de CS (sélection de l'esclave)

### 🛠️ Marche à suivre

1. Câblez <b>D0 → CS</b>, <b>D1 → SCK</b>, <b>D2 → MOSI</b>, <b>D3 → MISO</b>, <b>GND → masse</b>.
2. Observez SCK quand CS est à 1 (repos) : niveau haut ou bas ? C'est <b>CPOL</b>.
3. Observez à quel front de SCK les données sont stables : au 1<sup>er</sup> front (CPHA = 0) ou au 2<sup>e</sup> (CPHA = 1) ? Mode = 2·CPOL + CPHA.
4. Choisissez le décodeur SPI et essayez les modes jusqu'à obtenir des octets cohérents (aucun bit incomplet).
5. Répondez aux questions.

### ❓ Questions

1. Niveau de repos de SCK (CPOL) : 0 si bas, 1 si haut
2. Phase d'échantillonnage CPHA : 0 (1<sup>er</sup> front) ou 1 (2<sup>e</sup> front)
3. Mode SPI (0 à 3)
4. Premier octet envoyé par le maître sur MOSI (en décimal)
5. Nombre d'octets échangés pendant que CS est actif
6. Dernier octet reçu sur MISO (en décimal)
7. Fréquence de l'horloge SCK (en kHz)
8. À quoi sert la ligne CS (chip select) ?  
    - ☐ À fournir l'horloge  
    - ☐ À sélectionner l'esclave : il ne communique que lorsque CS est à 0  
    - ☐ À transmettre les données du maître  
    - ☐ À alimenter l'esclave

### 📥 Fichiers à ouvrir dans ElectroLab

- [`spi-v1.json`](tp/spi-v1.json) — Autre mode n° 1
- [`spi-v2.json`](tp/spi-v2.json) — Autre mode n° 2

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Analyse d'un bus SPI : retrouver le mode (CPOL / CPHA) (4 cas)*.
