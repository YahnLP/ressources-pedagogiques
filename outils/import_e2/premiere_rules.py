"""Règles de remplacement des diagrammes en texte de la Première (utilisées par enrichir.py)."""
has = lambda *s: (lambda b: all(x in b for x in s))
M = lambda t: t  # lisibilité

MTBF = r"""$$\mathrm{MTBF} = \dfrac{T_O}{n}$$

avec $T_O$ le temps total de fonctionnement et $n$ le nombre de pannes.

**Exemple :** un disque dur fonctionne 87 600 heures (10 ans) et tombe en panne 3 fois.

$$\mathrm{MTBF} = \dfrac{87\,600}{3} = 29\,200\ \text{heures} \approx 3{,}3\ \text{ans entre deux pannes}$$

**Interprétation :**

- MTBF = 50 000 h → en fonctionnement 24 h/24, panne probable dans 5,7 ans
- MTBF = 500 000 h → panne probable dans 57 ans (quasi immortel !)

> [!WARNING] MTBF ≠ durée de vie garantie
> C'est un indicateur **statistique** : avec une loi exponentielle, environ **63 %** des composants ($1 - e^{-1}$) sont déjà en panne au bout d'un temps égal au MTBF, et seulement **37 %** ($e^{-1}$) le dépassent."""

MTTR = r"""$$\mathrm{MTTR} = \dfrac{T_A}{n}$$

avec $T_A$ le temps total d'arrêt et $n$ le nombre de pannes.

**Le MTTR inclut :**

- le temps de détection de la panne
- le temps d'attente de l'intervention
- le temps de diagnostic
- le temps de réparation proprement dit
- le temps de test et de remise en service

**Pour réduire le MTTR :**

- ✓ avoir des pièces de rechange en stock (gestion de stock)
- ✓ former les techniciens aux procédures
- ✓ utiliser des systèmes de diagnostic automatique (alertes, logs)
- ✓ prévoir des modules facilement remplaçables (hot-swap)"""

DISPO = r"""$$D = \dfrac{\mathrm{MTBF}}{\mathrm{MTBF} + \mathrm{MTTR}} = \dfrac{T_O}{T_O + T_A}$$

**Exemple numérique :** MTBF = 2 500 h et MTTR = 3,6 h.

$$D = \dfrac{2\,500}{2\,500 + 3{,}6} = \dfrac{2\,500}{2\,503{,}6} = 0{,}9986 = 99{,}86\ \%$$

**Classes de disponibilité industrielle :**

| Disponibilité | Arrêt par an | Usage |
|---|---|---|
| 99 % | 3,65 jours | industrie non critique |
| 99,9 % | 8,76 heures | « three nines » |
| 99,99 % | 52,6 minutes | « four nines » |
| 99,999 % | 5,26 minutes | « five nines » (datacenter Tier IV) |"""

LAMBDA = r"""$\lambda$ (lambda) est le **taux de panne** : le nombre de pannes par unité de temps.

$$\lambda = \dfrac{1}{\mathrm{MTBF}}$$

**Exemples :**

- DHT22 (MTBF = 50 000 h) → $\lambda = \dfrac{1}{50\,000} = 2 \times 10^{-5}$ panne/heure
- Disque dur (MTBF = 300 000 h) → $\lambda = \dfrac{1}{300\,000} = 3{,}3 \times 10^{-6}$ panne/heure
- LED (MTBF = 25 000 h) → $\lambda = \dfrac{1}{25\,000} = 4 \times 10^{-5}$ panne/heure

**Unité alternative :** le FIT (*Failure In Time*), nombre de pannes pour $10^9$ heures.

$$\mathrm{FIT} = \lambda \times 10^{9} \qquad \text{ex. : } \lambda = 2 \times 10^{-5}\ /\mathrm{h} \;\Rightarrow\; 20\,000\ \mathrm{FIT}$$"""

BAIGNOIRE = """**Phase 1 — Mortalité infantile** ($\\lambda$ décroissant) : pannes dues aux défauts de fabrication. Elles se manifestent lors du rodage ou des tests en usine, d'où le « burn-in » des constructeurs.

**Phase 2 — Vie utile** ($\\lambda$ constant) : pannes aléatoires, indépendantes du temps. La loi exponentielle s'applique ici : c'est la phase normale de fonctionnement, où le MTBF est valable.

**Phase 3 — Vieillissement** ($\\lambda$ croissant) : usure normale des matériaux. Les condensateurs électrolytiques vieillissent (l'ESR augmente), les LED perdent de la luminosité."""

SERIE = r"""$$R_s = R_1 \times R_2 \times R_3 \times \dots \times R_n$$

$$\lambda_s = \lambda_1 + \lambda_2 + \lambda_3 + \dots + \lambda_n \quad\Rightarrow\quad \mathrm{MTBF}_s = \dfrac{1}{\lambda_s}$$"""

EXEMPLE = r"""**Étape 1 : fiabilité des 2 capteurs en parallèle**

$$R_{\text{capteurs}} = 1 - (1 - 0{,}90)(1 - 0{,}90) = 1 - 0{,}10 \times 0{,}10 = 1 - 0{,}01 = 0{,}99$$

**Étape 2 : système réduit (tout en série)** : 0,99 → 0,95 → 0,98 → 0,99

**Étape 3 : fiabilité totale**

$$R_s = 0{,}99 \times 0{,}95 \times 0{,}98 \times 0{,}99 \approx 0{,}912 = 91{,}2\ \%$$"""

PARALLELE = r"""$$R_s = 1 - (1 - R_1)(1 - R_2)(1 - R_3)$$

$R_s > R_{max}$ : le système est plus fiable que le plus fiable de ses composants."""

RC = r"""$$f_c = \dfrac{1}{2\pi R C}$$

**Exemple :** $R = 10\,\mathrm{k\Omega}$ et $C = 330\,\mathrm{nF}$

$$f_c = \dfrac{1}{2\pi \times 10\,000 \times 330 \times 10^{-9}} \approx 48\ \mathrm{Hz}$$"""

STACK = """**Chaque brique :**

- **ESP32** : acquisition et communication (S6)
- **Broker MQTT** : transport de messages (S6)
- **Node-RED** : orchestration et dashboard simple (S8, *ici*)
- **InfluxDB** : stockage à long terme (S8, *ici*)
- **Grafana** : dashboard professionnel (bonus S8 / S10)"""

RULES = [
    ('S05', '01-cours', [(has('Analyseur logique USB', 'CH0'), 'analyseur_cablage', "Câblage de l'analyseur logique : voies CH0 à CH2 et GND"),
                         (has('Chronogramme', 'START'), 'chrono_i2c', 'Chronogramme I2C : START, adresse sur 7 bits, R/W et ACK'),
                         (has('CS LOW'), 'chrono_spi', 'Chronogramme SPI : CS, SCLK, MOSI et MISO'),
                         (has('CH1 (analogique'), 'oscillo_logique', 'Oscilloscope à signaux mixtes : voie analogique et voies logiques')]),
    ('S07', '01-cours', [(has('B R O K E R'), 'mqtt_broker', 'MQTT : publishers, broker et subscribers')]),
    ('S08', '01-cours', [(has('MEASUREMENT'), 'influx_point', "Un point InfluxDB : measurement, tags, fields et timestamp"), (has('STACK IOT COMPLÈTE'), 'stack_iot', 'Stack IoT complète : ESP32, broker, Node-RED, InfluxDB, Grafana', STACK)]),
    ('S08', 'annexe-ai', [(has('Requête Flux'), 'flux_nodered', 'Flux de données : MQTT, Node-RED, dashboard et InfluxDB')]),
    ('S09', '01-cours', [(has('mTLS'), 'tls_mtls', 'TLS standard et mTLS : authentification du serveur seul ou des deux côtés'), (has('Rule Engine'), 'aws_regles', 'AWS IoT : le Rule Engine distribue les messages (CloudWatch, DynamoDB, Lambda, S3)')]),
    ('S11', '01-cours', [(lambda b: b.startswith('MTBF = Temps total'), None, MTBF), (lambda b: b.startswith('MTTR = Temps total'), None, MTTR),
                         (has('MTBF + MTTR'), None, DISPO), (lambda b: b.startswith('λ (lambda)'), None, LAMBDA),
                         (has('Vie utile'), 'courbe_baignoire', 'Courbe en baignoire : mortalité infantile, vie utile, vieillissement', BAIGNOIRE),
                         (has('[C1] ──── [C2]'), 'rbd_serie', 'Système série : la panne d\'un seul composant arrête tout', SERIE), (has('Capteur 1 (R=0,90)'), 'rbd_capteurs', 'Exemple de système mixte : deux capteurs en parallèle puis CPU, réseau et serveur en série', EXEMPLE)]),
    ('S11', 'annexe-ai', [(has('Rs = 1 − (1−R1)'), 'rbd_parallele', 'Système parallèle : il suffit qu\'un composant fonctionne', PARALLELE)]),
    ('S11', '03-exerci', [(has('DHT22 (R=0,88)'), 'rbd_station', 'Station IoT : DHT22 et MQ-2 en parallèle, puis ESP32, Wi-Fi/MQTT et Node-RED en série')]),
    ('S13', 'annexe-ai', [(has('SOURCE ──→ COUPLAGE'), 'cem_couplage', 'CEM : source, couplage, victime'), (has('Sortie filtrée'), 'filtre_rc_cem', 'Filtre RC passe-bas', RC)]),
    ('S14', '01-cours', [(has('Chemin d\'un message MQTT'), 'chemin_message_mqtt', 'Chemin d\'un message MQTT et diagnostic par dichotomie')]),
    ('S15', '03-exerci', [(has('Système :  [A (R=0,85)]'), 'rbd_exercice', 'Système à étudier : capteurs A et B en parallèle, puis CPU et réseau en série', '```\n__REST__\n```')]),
    ('S16', 'annexe-ca', [(has('[Capteur(s)]'), 'chaine_aws', "Chaîne complète : capteurs, ESP32, AWS IoT Core, CloudWatch et notification SMS")]),
    ('S17', '01-cours', [(has('Décision', 'SCADA/MES'), 'niveaux_isa', 'Niveaux d\'une architecture industrielle : de la décision au terrain')]),
]
