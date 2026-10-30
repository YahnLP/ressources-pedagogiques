"""Structure finale des 10 semaines de « L'essentiel en 1 an » : une formation complète pour un élève qui
arrive directement en Terminale (composants, mesures, prototypage, microcontrôleur, communication, CAO jusqu'au
Gerber, test, dépannage, épreuve). Deux fils rouges : la carte CLIGNOTEUR NE555 et une STATION DE MESURE communicante.
Les TP virtuels ElectroLab sont proposés AVANT chaque TP réel."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import essentiel as OLD            # anciennes semaines (briques réutilisées)
from essentiel_cours import COURS as OC
from essentiel_ateliers import ATELIER as OA, EXOS as OE
import json

CAT = json.load(open(Path(__file__).resolve().parents[1] / 'electrolab-sujets' / 'catalogue.json', encoding='utf-8'))
S, P, T = '../seconde/', '../premiere/', '../terminale/'
URL = 'https://yahnlp.github.io/ElectroLab/'
old = {w['n']: w for w in OLD.SEMAINES}

def L(titre, chemin): return f'[{titre}]({chemin})'

def decoupe(txt):
    """-> (intro, [(titre, corps)]) selon les titres ###"""
    parts = re.split(r'(?m)^(?=### )', txt.strip() + '\n')
    intro = parts[0].strip(); secs = []
    for p in parts[1:]:
        t, _, b = p.partition('\n'); secs.append((t[4:].strip(), b.strip()))
    return intro, secs

def compose(intro_src, picks, extra=None):
    """intro_src : texte dont on garde l'accroche ; picks : [(texte source, indices ou None)] ; extra : sections nouvelles"""
    intro = decoupe(intro_src)[0]
    out = []
    for txt, idx in picks:
        secs = decoupe(txt)[1]
        out += [secs[i] for i in (idx if idx is not None else range(len(secs))) if not secs[i][0].startswith('Exercice guidé')]
    out += (extra or [])
    n = 0; res = [intro]
    for t, b in out:
        t = re.sub(r'^\d+\.\s*', '', t); n += 1
        res.append(f'### {n}. {t}\n\n{b}')
    return '\n\n'.join(res) + '\n'

def tpvirt(ids, nouveaux=None, intro=None):
    o = [f"Ouvre [ElectroLab]({URL}), menu **TP ▾**, puis fais ces TP **avant** de toucher au matériel :", ""]
    for i in ids:
        c = CAT[i]; o.append(f"- **{c['title']}** ({c['duration']}, niveau {c['level'].strip('()')})")
    if nouveaux:
        o += ["", "**Sujets à ouvrir dans ElectroLab** (bouton **Ouvrir**, puis choisis le fichier `.json`) :", ""]
        o += [f"- [`{f}`]({chemin}) : {desc}" for f, chemin, desc in nouveaux]
    o += ["", "> [!TIP] 🖥️ Pourquoi d'abord le simulateur ?",
          "> On peut se tromper sans rien casser, répéter autant de fois que nécessaire et obtenir une correction automatique. Le TP réel sert ensuite à **confirmer** et à manipuler le vrai matériel."]
    return '\n'.join(o)

# ----------------------------------------------------------------- nouvelles sections de cours
SECURITE = ("Sécurité et bons réflexes", r"""
- **Très basse tension** (jusqu'à 50 V alternatif / 120 V continu) : pas de risque d'électrisation. Au-delà, **habilitation électrique** (BR) obligatoire.
- **Électricité statique (ESD)** : touche les cartes par les bords, range les circuits intégrés dans leurs sachets antistatiques.
- **Fer à souder** : toujours sur son support ; aspiration des fumées ; étain **sans plomb** (RoHS).
- **Déchets** : une carte ou une batterie hors service est un **déchet électronique (DEEE)**, jamais à la poubelle ordinaire.""".strip())

PROTO = ("Monter un circuit : plaque d'essai puis soudure", r"""
**Plaque d'essai (breadboard)** : les trous d'une **même colonne** (5 trous) sont reliés ; les **rails** (lignes + et −) courent sur toute la longueur. On y monte un circuit **sans souder**, pour le tester.

> [!TIP] 💡 Méthode
> 1. Relier les rails +5 V et GND. 2. Poser les composants **dans l'ordre du schéma**. 3. Vérifier **avant** d'alimenter (sens des LED, polarité des condensateurs, absence de court-circuit entre + et −).

**Souder à l'étain (5 étapes)** : 1) fer chaud (≈ 350 °C) et panne propre ; 2) chauffer **en même temps** la patte et la pastille ; 3) amener l'étain **sur la pastille** (pas sur le fer) ; 4) retirer l'étain, puis le fer ; 5) laisser refroidir **sans bouger**.

**Brasure correcte** (IPC-A-610, classe 2) : brillante, en **cône**, trou rempli à **75 % au moins**. Défauts : **pont** de soudure (court-circuit), soudure **froide** (terne, craquelée), **manque** de soudure.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Alimenter avant de vérifier le montage.
> - Souder un composant polarisé (LED, condensateur chimique, diode) **à l'envers**.
> - Oublier que le fer **brûle** : jamais de la main.""".strip())

MICRO = ("Programmer un microcontrôleur : Arduino / ESP32", r"""
Un **microcontrôleur** est un petit ordinateur sur une puce : il lit des **entrées**, exécute un **programme** et pilote des **sorties**. Un programme Arduino (« sketch ») a deux parties :

```cpp
void setup() {            // exécuté UNE fois au démarrage
  pinMode(13, OUTPUT);    // broche 13 = sortie
  Serial.begin(9600);     // moniteur série à 9600 bauds
}
void loop() {             // répété en boucle
  digitalWrite(13, HIGH); // sortie à 5 V
  delay(500);             // attendre 500 ms
  digitalWrite(13, LOW);
  delay(500);
}
```

| Instruction | Rôle |
|---|---|
| `pinMode(p, OUTPUT / INPUT / INPUT_PULLUP)` | choisir le rôle d'une broche |
| `digitalWrite(p, HIGH / LOW)` | mettre une sortie à 5 V / 0 V |
| `digitalRead(p)` | lire une entrée (HIGH ou LOW) |
| `analogRead(A0)` | lire une tension de 0 à 5 V : nombre de **0 à 1023** |
| `analogWrite(p, 0…255)` | signal **PWM** (rapport cyclique) |
| `Serial.println(x)` | afficher x sur le moniteur série |

> [!TIP] 💡 Bouton poussoir
> Avec `INPUT_PULLUP`, une résistance interne tire l'entrée à 5 V : le bouton relié à la masse donne **LOW quand on appuie**.""".strip())

CAPTEURS = ("Lire un capteur : conversion analogique-numérique", r"""
Le convertisseur **ADC** de l'Arduino a **10 bits** : $2^{10} = 1\,024$ valeurs (0 à 1023) pour 0 à 5 V. Un pas vaut $\dfrac{5}{1023} \approx 4{,}9\,\mathrm{mV}$.

$$U = \text{valeur} \times \frac{5}{1023}$$

**Capteur de température LM35** : **10 mV par °C**, donc $T = U \times 100$.

```cpp
void loop() {
  int brut = analogRead(A0);
  float tension = brut * 5.0 / 1023.0;
  float temperature = tension * 100.0;
  Serial.println(temperature);
  delay(1000);
}
```

**Exemple** : `brut = 51` → $U \approx 0{,}249\,\mathrm{V}$ → $T \approx 24{,}9\,°\mathrm{C}$. Un pas de l'ADC (4,9 mV) correspond à environ 0,5 °C : c'est la **résolution** de la mesure.

**PWM** : `analogWrite(9, 64)` donne un rapport cyclique de $\dfrac{64}{255} \approx 25\,\%$ à environ 490 Hz.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier `Serial.begin(9600)` ou régler le moniteur sur une autre vitesse : texte illisible.
> - Diviser des entiers (`brut / 1023`) : le résultat est tronqué. Écrire `1023.0`.
> - Brancher le capteur sur une broche **numérique** au lieu d'une entrée **analogique** (A0…).""".strip())

COM1 = ("Pourquoi et comment communiquer", r"""
Un système communicant suit une **chaîne** : **capteur → microcontrôleur → réseau → supervision** (écran, tableau de bord, alarme). Chaque maillon doit **parler la même langue** que le suivant : c'est le rôle des **protocoles**.""".strip())
COM2 = ("La liaison série UART", r"""
Les bits partent **un par un** sur un fil, à une vitesse commune (**baud rate**, par exemple 9600). Une trame **8N1** contient **10 bits** : 1 bit de départ (0), 8 bits de données (le moins significatif d'abord), 1 bit d'arrêt (1).

$$T_{bit} = \frac{1}{\text{baud}} \qquad \text{à 9600 bauds : } T_{bit} \approx 104\,\mathrm{\mu s}\ ;\ \text{un octet} \approx 1{,}04\,\mathrm{ms}$$

**Câblage** : TX d'un côté vers **RX** de l'autre (et inversement) + **masse commune**. Même vitesse des deux côtés, sinon : caractères absurdes.""".strip())
COM3 = ("Le bus I²C", r"""
Deux fils seulement : **SDA** (données) et **SCL** (horloge), partagés par plusieurs appareils. Chaque appareil a une **adresse** (par exemple `0x27` pour un écran LCD). Les deux lignes ont des **résistances de rappel** (≈ 4,7 kΩ) vers le +V. Sur l'Arduino Uno : SDA = A4, SCL = A5.""".strip())
COM4 = ("WiFi et MQTT avec l'ESP32", r"""
L'**ESP32** se connecte au WiFi (mode **station**) ou crée son propre réseau (mode **point d'accès**, adresse 192.168.4.1). Ses broches fonctionnent en **3,3 V** : ne jamais y appliquer 5 V.

**MQTT** : un **broker** (serveur) reçoit les messages d'un **publisher** et les redistribue aux **subscribers** abonnés au même **topic** (par exemple `salle1/temperature`). Port **1883** (8883 avec TLS). Les topics sont **sensibles à la casse**. Caractères joker : `+` (un niveau) et `#` (tous les niveaux suivants). Le contenu est souvent un texte **JSON** : `{"temp": 23.5}`.""".strip())
COM5 = ("Superviser : moyenne, seuil, hystérésis", r"""
Pour fiabiliser une mesure, on calcule des **indicateurs** (KPI) :

- **Moyenne mobile** des N dernières mesures : elle lisse le bruit (20, 22, 21, 25 → 22).
- **Seuil avec hystérésis** : l'alarme se **déclenche** à 30 °C mais ne se **coupe** qu'en dessous de 28 °C : on évite le battement autour d'un seul seuil.
- **Trois niveaux** : normal, avertissement, critique.""".strip())
COM6 = ("Diagnostiquer une liaison", r"""
Dans l'ordre : **alimentation** ; **câblage** (TX ↔ RX croisés, masse commune) ; **vitesse** identique ; **niveaux** de tension compatibles (3,3 V / 5 V) ; **adresse** I²C correcte ; **IP du broker** et **topic** (casse !) pour MQTT. Un outil précieux : le **moniteur série** et l'**analyseur logique**.""".strip())

# ----------------------------------------------------------------- semaines
def sem(n, titre, comp, obj, deroule, liens, tests, livrable, cours, atelier, exos, tpv):
    return dict(n=n, titre=titre, comp=comp, obj=obj, deroule=deroule, liens=liens, tests=tests, livrable=livrable, cours=cours, atelier=atelier, exos=exos, tpvirtuel=tpv)

SEM = []
# --- 1
SEM.append(sem(1, "Les composants, les lois de base et la sécurité", "C07", old[1]['obj'] + ["Connaître les règles de sécurité de base."],
  [("1 h", "TP virtuel ElectroLab : loi d'Ohm, associations, LED"), ("1 h", "Cours : composants, code couleurs, puissance"), ("1 h", "Atelier réel : LED + résistance sur plaque d'essai"), ("1 h", "Exercices, sécurité, auto-test")],
  old[1]['liens'] + [L("Seconde S05 – sécurité et environnement", S + "S05-maintenance-n1-nettoyage-de-cartes/02-securite-et-environnement.md")],
  old[1]['tests'] + [("À partir de quelle tension faut-il une habilitation électrique ?", "Au-delà de **50 V alternatif** ou **120 V continu**.")], old[1]['livrable'],
  compose(OC[1], [(OC[1], None)], [SECURITE]), OA[1], OE[1],
  tpvirt(['ohm', 'assoc', 'puissance', 'led'])))
# --- 2
SEM.append(sem(2, "Mesurer : multimètre, alimentation, générateur et oscilloscope", "C07 · C11", old[2]['obj'],
  [("1 h", "TP virtuels ElectroLab : multimètre et oscilloscope"), ("1 h", "Multimètre, alimentation de labo, générateur : réel"), ("1 h", "Oscilloscope : réel (signal de test, PWM)"), ("1 h", "Atelier chronométré, passeport instruments, auto-test")],
  old[2]['liens'], old[2]['tests'], old[2]['livrable'], OC[2], OA[2], OE[2],
  tpvirt(['test', 'osc_lect', 'signaux', 'osc_carre', 'osc_ac'], [
    ('alim-cv.json', S + 'S12-tests-au-multimetre-et-controle-qualite/tp/alim-cv.json', "alimentation 5 V sur une résistance de 220 Ω : mode CV ; relève U et I (attendu : environ 5,0 V et 22,7 mA)"),
    ('alim-cc.json', S + 'S12-tests-au-multimetre-et-controle-qualite/tp/alim-cc.json', "même montage avec une résistance de 100 Ω et une limite de 30 mA : l'alimentation passe en mode CC (attendu : environ 30 mA et 3,0 V)")])))
# --- 3
SEM.append(sem(3, "Lire un schéma et une datasheet, monter et souder", "C07", old[3]['obj'] + ["Monter un circuit sur plaque d'essai puis le souder."],
  [("1 h", "Schéma normalisé et datasheet (7805, BC547, NE555)"), ("1 h", "TP virtuel ElectroLab : NE555 en astable"), ("1 h", "Montage sur plaque d'essai"), ("1 h", "Soudure et contrôle IPC ; auto-test")],
  old[3]['liens'] + [L("Seconde S04 – soudure et IPC", S + "S04-soudure-a-l-etain-composants/01-cours.md")],
  old[3]['tests'] + [("Combien de trous sont reliés dans une même colonne d'une plaque d'essai ?", "**5 trous**.")], old[3]['livrable'],
  compose(OC[3], [(OC[3], None)], [PROTO]), OA[3], OE[3], tpvirt(['ne555'])))
# --- 4
SEM.append(sem(4, "Alimentation et commande de charges", "C07 · C11", old[4]['obj'] + ["Commander une charge avec un transistor, un MOSFET ou un relais."],
  [("1 h", "TP virtuels ElectroLab : régulation 7805, transistor"), ("1 h", "Bilan de puissance et thermique"), ("1 h", "Transistor, MOSFET, relais, diode de roue libre"), ("1 h", "Atelier réel et auto-test")],
  old[4]['liens'] + old[7]['liens'][:1], old[4]['tests'][:3] + old[7]['tests'][:2], old[4]['livrable'],
  compose(OC[4], [(OC[4], None), (OC[7], [0, 1])]), OA[4] + "\n" + OA[7].split("2.")[0] if False else OA[4], OE[4][:3] + OE[7][:1], tpvirt(['regul', 'transistor', 'relais', 'mosfet'])))
# --- 5 (nouvelle) : microcontrôleur, capteurs, signaux
SEM.append(sem(5, "Microcontrôleur, capteurs et traitement du signal", "C07 · C11",
  ["Écrire et lire un programme Arduino simple (entrées, sorties, moniteur série).", "Lire un capteur analogique (LM35) et convertir en grandeur physique.", "Produire un signal PWM.", "Filtrer un signal (filtre RC), amplifier (AOP) et lire une table de vérité."],
  [("1 h", "Programme Arduino : sorties, entrées, bouton"), ("1 h", "Capteur LM35 : lecture et conversion"), ("1 h", "TP virtuels ElectroLab : AOP, filtre RC, portes ; conditionnement du signal"), ("1 h", "Exercices et auto-test")],
  [L("Seconde S07 – structure d'un sketch", S + "S07-arduino-ide-structure-du-sketch-led/01-cours.md"), L("Seconde S08 – entrées numériques", S + "S08-e-s-numeriques-bouton-led-pull-up-pull/01-cours.md"), L("Seconde S09 – capteur LM35", S + "S09-capteur-lm35-analogread-et-conversion/01-cours.md"), L("Première S12 – AOP, filtre RC, portes logiques", P + "S12-prototypes-avances-integration/04-aop-filtre-logique.md")],
  [("Que fait `analogRead(A0)` ? Quelle plage de valeurs ?", "Il lit une tension de 0 à 5 V et renvoie un nombre de **0 à 1023**."), ("`analogRead` renvoie 102 pour un LM35 : quelle température ?", "$U = 102 \\times \\dfrac{5}{1023} \\approx 0{,}50\\,\\mathrm{V}$ ; $T \\approx 49{,}9\\,°\\mathrm{C}$."), ("Quel rapport cyclique donne `analogWrite(9, 128)` ?", "$\\dfrac{128}{255} \\approx 50\\,\\%$."), ("Avec `INPUT_PULLUP`, que lit-on quand on appuie sur le bouton relié à la masse ?", "**LOW** (0)."), ("Fréquence de coupure d'un filtre RC (10 kΩ, 100 nF) ?", "$\\dfrac{1}{2\\pi RC} \\approx 159\\,\\mathrm{Hz}$.")],
  "Programme commenté qui lit un capteur de température et affiche la valeur en °C sur le moniteur série.",
  compose("""
??? question "🤔 À ton avis ?"
    Un capteur délivre une tension de 0,25 V. Comment l'Arduino peut-il en faire « 25 °C » sur un écran ?

    **Réponse** : il **convertit** la tension en nombre (ADC), puis le programme applique une **formule**. On va apprendre chaque étape.
""", [], [MICRO, CAPTEURS, ("Traiter le signal : filtre, amplificateur, logique", decoupe(OC[7])[1][2][1] + "\n\n" + decoupe(OC[7])[1][3][1] + "\n\n" + decoupe(OC[7])[1][4][1])]),
  r"""
**Fil rouge 2 : la station de mesure.** Matériel : Arduino (ou ESP32), capteur LM35, LED, bouton.

1. Câble la **LED** sur la broche 13 avec une résistance de 220 Ω. Téléverse le programme de clignotement (500 ms).
2. Câble le **bouton** entre la broche 2 et la masse (`INPUT_PULLUP`) : la LED s'allume tant qu'on appuie.
3. Câble le **LM35** (+5 V, A0, GND). Écris le programme de lecture et affiche la température sur le moniteur série (9600 bauds).
4. Change la fréquence de clignotement : combien de clignotements par seconde pour `delay(250)` ?
5. Pose la LED sur une broche PWM (9) et fais varier l'intensité avec `analogWrite`.

??? success "Résultats attendus"
    1. La LED clignote à **1 Hz** (500 ms allumée + 500 ms éteinte).
    2. LED allumée **quand on appuie** (le bouton relié à la masse donne LOW).
    3. Environ la **température ambiante** (par exemple 22 à 25 °C) ; elle monte si on touche le capteur.
    4. Période 500 ms → **2 clignotements par seconde**.
    5. Intensité proportionnelle au rapport cyclique ($64/255 \approx 25\,\%$ : faible ; 255 : maximale).
""",
  [("Combien de valeurs distinctes peut renvoyer `analogRead` ?", "$2^{10} = 1\\,024$ valeurs (0 à 1023)."), ("`brut = 307` sur un LM35 : température ?", "$U = 307 \\times \\dfrac{5}{1023} \\approx 1{,}50\\,\\mathrm{V}$ ; $T \\approx 150\\,°\\mathrm{C}$ : valeur impossible pour un LM35 (de −55 à 150 °C) à 5 V : à vérifier."), ("Pourquoi écrire `1023.0` plutôt que `1023` ?", "Pour forcer un calcul **décimal** ; avec des entiers le résultat est tronqué."), ("Un AOP non inverseur a $R_f = 10\\,\\mathrm{k\\Omega}$, $R_g = 1\\,\\mathrm{k\\Omega}$ : gain ?", "$G = 1 + 10 = 11$.")],
  tpvirt(['inverseur', 'filtre', 'portes', 'diviseur'])))
SEM[-1]['exos'] = SEM[-1]['exos'][:1] + [("`brut = 102` sur un LM35 : température ?", "$U \\approx 0{,}50\\,\\mathrm{V}$ ; $T \\approx 49{,}9\\,°\\mathrm{C}$.")] + SEM[-1]['exos'][2:]
# --- 6 (nouvelle) : système communicant
SEM.append(sem(6, "Le système communicant : UART, I²C, WiFi, MQTT et supervision", "C07 · C11",
  ["Expliquer la chaîne capteur → microcontrôleur → réseau → supervision.", "Lire une trame UART et calculer sa durée.", "Reconnaître un bus I²C et son adresse.", "Décrire un échange MQTT (broker, topic, JSON).", "Diagnostiquer une liaison qui ne fonctionne pas."],
  [("1 h", "TP virtuels ElectroLab : analyseur logique, UART, I²C"), ("1 h", "Cours : protocoles et MQTT"), ("1 h", "Atelier : trames, topics, supervision"), ("1 h", "Diagnostic d'une liaison ; auto-test")],
  [L("Seconde S13 – liaison série UART", S + "S13-communication-serie-uart-protocol/01-cours.md"), L("Seconde S15 – LCD I²C", S + "S15-lcd-i2c-bibliotheque-affichage/01-cours.md"), L("Première S06 – ESP32 WiFi", P + "S06-esp32-wifi-modes-station-ap-webserver/01-cours.md"), L("Première S07 – MQTT", P + "S07-mqtt-publish-subscribe-topics-qos/01-cours.md"), L("Terminale S04 – KPI et alarme embarquée", T + "S04-acquisition-capteur-courbe-kpi-alarme/01-cours.md")],
  [("Combien de bits dans une trame 8N1 ?", "**10 bits** (1 départ + 8 données + 1 arrêt)."), ("Durée d'un octet à 9600 bauds ?", "$10 \\times 104\\,\\mathrm{\\mu s} \\approx 1{,}04\\,\\mathrm{ms}$."), ("Un ESP32 reçoit un signal de 5 V sur une broche : problème ?", "Oui : ses broches sont en **3,3 V** ; il faut un diviseur de tension ou un convertisseur de niveau."), ("`Salle1/temp` et `salle1/temp` : même topic ?", "**Non** : les topics sont **sensibles à la casse**."), ("Quel port utilise MQTT sans chiffrement ?", "**1883**.")],
  "Schéma de la chaîne de ta station de mesure (capteur, microcontrôleur, protocole, topic MQTT) avec les valeurs choisies.",
  compose("""
??? question "🤔 À ton avis ?"
    Ton capteur de température est dans une salle, ton écran de contrôle dans un bureau. Comment la valeur voyage-t-elle jusqu'à lui ?

    **Réponse** : par une **liaison** (série, I²C, WiFi) qui suit un **protocole** : des règles communes de format et de vitesse. On étudie les plus courantes.
""", [], [COM1, COM2, COM3, COM4, COM5, COM6]),
  r"""
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
""",
  [("Quelle différence entre UART et I²C ?", "L'**UART** relie **deux** appareils (TX/RX, vitesse commune) ; l'**I²C** relie **plusieurs** appareils sur 2 fils (SDA, SCL) grâce aux **adresses**."), ("À quoi sert l'adresse I²C ?", "À **repérer** chaque appareil sur le bus."), ("Moyenne mobile de 18, 20, 22, 24 ?", "$\\dfrac{84}{4} = 21$."), ("Pourquoi une hystérésis ?", "Pour éviter que l'alarme **bat** (s'allume et s'éteigne sans arrêt) autour d'un seul seuil.")],
  tpvirt(['la_intro', 'uart', 'i2c'])))
# --- 7
SEM.append(sem(7, "Du cahier des charges au schéma et au PCB", "C07", old[5]['obj'] + ["Placer et router un PCB selon des règles."],
  [("1 h", "TP virtuel ElectroLab : valider le clignoteur avant de le dessiner"), ("1 h", "Schéma KiCad, ERC, empreintes"), ("1 h", "Contour, règles, placement"), ("1 h", "Routage et auto-test")],
  old[5]['liens'], old[5]['tests'] + old[6]['tests'][:1], old[5]['livrable'],
  compose(OC[5], [(OC[5], None), (OC[6], [0, 1])]), OA[5], OE[5][:3] + OE[6][2:3],
  tpvirt(['ne555'], [('clignoteur.json', 'tp/clignoteur.json', "le clignoteur NE555 complet (alimentation 5 V, fusible, NE555, LED, oscilloscope) ; relève la période T (attendu environ 1,01 s), la fréquence (environ 0,99 Hz), le rapport cyclique (environ 55 %) et la tension de sortie à l'état haut (environ 3,1 V)")])))
# --- 8
SEM.append(sem(8, "Du PCB aux fichiers de fabrication, à la carte soudée", "C07", old[6]['obj'],
  [("1 h", "DRC, corrections, fichiers de fabrication (Gerber, perçage, BOM)"), ("1 h", "Vérification dans un visualiseur ; TP de bout en bout (étapes 3 à 5)"), ("1 h", "Soudure de la carte et contrôle IPC"), ("1 h", "Mise sous tension et auto-test")],
  old[6]['liens'], old[6]['tests'], old[6]['livrable'],
  compose(OC[6], [(OC[6], [2, 3, 4])]), OA[6], OE[6],
  tpvirt(['test'])))
# --- 9
SEM.append(sem(9, "Tester, valider et dépanner", "C11 · C03", old[8]['obj'] + old[9]['obj'][:2],
  [("1 h", "Tolérance, marge de mesure et PV (carte clignoteur)"), ("1 h", "Méthode de dépannage : tableau de tensions"), ("1 h", "TP virtuels ElectroLab : dépannage (alimentation, transistor, clignoteur)"), ("1 h", "Dépannage réel, fiche d'intervention, auto-test")],
  old[8]['liens'] + old[9]['liens'][:1], old[8]['tests'][:3] + old[9]['tests'][:3], "PV de la carte clignoteur et fiche d'intervention d'une panne diagnostiquée.",
  compose(OC[8], [(OC[8], [0, 1, 2, 3]), (OC[9], [0, 1, 2, 3])]),
  r"""
**Fil rouge 1 : valider puis dépanner la carte clignoteur.**

1. **Valide** la carte : tension d'alimentation (5 V ± 5 %), fréquence (1 Hz ± 10 %), rapport cyclique, courant dans la LED. Rédige le PV (attendu / mesuré / marge / verdict).
2. Dans **ElectroLab**, ouvre `clignoteur.json` puis les sujets de panne `clignoteur-panne-A.json`, `-B.json`, `-C.json`. Pour chacun : **décris** le symptôme, **mesure** (tensions, puis résistances hors tension), **conclus**.
3. Remplis une **fiche d'intervention** pour chaque panne.

??? success "Résultats attendus"
    - **Carte saine** : $V_{CC} \approx 5\,\mathrm{V}$ ; période ≈ 1,01 s ($f \approx 0{,}99\,\mathrm{Hz}$, conforme à 0,9–1,1 Hz) ; rapport cyclique ≈ 55 % ; sortie à l'état haut ≈ 3,1 V, donc courant LED ≈ 9 mA avec 150 Ω (inférieur au calcul simplifié : le NE555 bipolaire « perd » environ 1,9 V en sortie).
    - **Panne A** : aucune tension sur la carte : le **fusible F1** est grillé (mesure de la tension avant et après le fusible).
    - **Pannes B et C** : LED **toujours allumée**, broches 2 et 6 à environ 0 V : le condensateur **ne peut plus se charger**. Même symptôme, deux causes : on **départage hors tension** en mesurant la résistance. **B** : $R_b$ coupée ; **C** : $R_a$ coupée.
""", old[8]['tests'] and (OE[8][:2] + OE[9][:2]),
  tpvirt(['dep1', 'dep2', 'dep3', 'dep_log'], [
    ('clignoteur.json', 'tp/clignoteur.json', "la carte saine de référence"),
    ('clignoteur-panne-A.json', 'tp/clignoteur-panne-A.json', "panne A : rien ne s'allume"),
    ('clignoteur-panne-B.json', 'tp/clignoteur-panne-B.json', "panne B : LED toujours allumée"),
    ('clignoteur-panne-C.json', 'tp/clignoteur-panne-C.json', "panne C : même symptôme que B, autre cause")])))
# --- 10
SEM.append(sem(10, "Épreuve blanche et bilan", "C03 · C07 · C11", old[10]['obj'],
  old[10]['deroule'], old[10]['liens'], old[10]['tests'], old[10]['livrable'], OC[10], OA[10], OE[10],
  tpvirt(['dep1', 'signaux'])))
