import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🗝️ Vocabulaire", 'fin', apropos("Quand ton PC et ton Arduino « se parlent » par le câble USB, comment savent-ils où commence et où finit chaque lettre envoyée ?", "Ils s'**accordent à l'avance** sur une vitesse (le **baud rate**) et sur une **forme de message** (la **trame**) : un bit de départ, les bits de la lettre, un bit d'arrêt. C'est comme une conversation où l'on **parle à la même vitesse** et où l'on **marque une pause** entre deux mots.\n\nDans cette séance, tu apprends à **lire une trame**, à **calculer sa durée** et à **dépanner** une liaison série.")),
    ("## 1.", 'fin', clair("Une liaison **UART** envoie les bits **un par un** sur un seul fil. Une trame **8N1** contient **10 bits** : 1 bit de **start** (0), **8 bits** de données, 1 bit de **stop** (1). Quand la ligne est au repos, elle reste à **1** : le passage à 0 signale « attention, ça commence ».\n\nLa durée d'un bit se calcule avec $T_{\\mathrm{bit}} = \\dfrac{1}{\\text{baud}}$. À 9600 bauds : $T_{\\mathrm{bit}} = \\dfrac{1}{9600} \\approx 104\\,\\mathrm{\\mu s}$.") + "\n" + verifie(
        ("Combien de bits contient une trame 8N1 ?", "**10 bits** : 1 start + 8 données + 1 stop."),
        ("Quelle est la durée d'un octet complet à 9600 bauds ?", "$10 \\times 104\\,\\mathrm{\\mu s} \\approx 1{,}04\\,\\mathrm{ms}$."),
        ("Pourquoi le bit de start vaut-il 0 alors que la ligne au repos est à 1 ?", "Pour créer un **front descendant** : le récepteur détecte ainsi le **début** de la trame.")) + "\n" + erreurs("Régler deux baud rates différents (émetteur et récepteur) : le récepteur lit des **caractères absurdes**.", "Oublier que la trame contient **10 bits** et pas 8 quand on calcule un débit.") + "\n" + retenir("8N1 = 10 bits par octet.", "$T_{\\mathrm{bit}} = \\dfrac{1}{\\text{baud}}$.")),
    ("## 2.", 'fin', clair("Pour **recevoir** des données, on vérifie d'abord qu'il y en a (`Serial.available()`), puis on les lit : `Serial.read()` lit **un seul caractère** ; `Serial.readString()` lit **toute la chaîne**. Sans test `available()`, on lit du « vide ».") + "\n" + verifie(
        ("À quoi sert `Serial.available()` ?", "À savoir **combien d'octets** sont arrivés et peuvent être lus."),
        ("Quelle fonction lit un seul caractère ?", "`Serial.read()`.")) ),
    ("## 3.", 'fin', clair("Le **Serial Monitor** est ton outil de test : tu y **vois** ce que l'Arduino envoie et tu peux lui **écrire**. Vérifie toujours que la **vitesse choisie en bas** de la fenêtre est la même que dans `Serial.begin()`.") + "\n" + verifie(
        ("Le Serial Monitor affiche des symboles bizarres. Première chose à vérifier ?", "Que le **baud rate** du moniteur est le même que celui de `Serial.begin()`.")) ),
    ("## 4.", 'fin', clair("Le **HC-05** fonctionne en **3,3 V** : sa broche **RXD** ne supporte pas les 5 V de l'Arduino. On place donc un **diviseur de tension** : avec 1 kΩ et 2 kΩ, $U_{\\mathrm{RXD}} = 5 \\times \\dfrac{2}{1+2} \\approx 3{,}33\\,\\mathrm{V}$.") + "\n" + verifie(
        ("Pourquoi un diviseur sur la broche RXD du HC-05 ?", "Parce que RXD ne supporte que **3,3 V** et que l'Arduino envoie **5 V**."),
        ("Calcule la tension obtenue avec R1 = 1 kΩ et R2 = 2 kΩ (entrée 5 V).", "$5 \\times \\dfrac{2}{3} \\approx 3{,}33\\,\\mathrm{V}$.")) + "\n" + retenir("HC-05 : logique 3,3 V ; diviseur 1 kΩ / 2 kΩ sur RXD.")),
    ("## 5.", 'fin', clair("Pour dépanner une liaison série, **va du plus simple au plus compliqué** : câblage (TX → RX, RX → TX), **masse commune**, **baud rate**, programme. Ne change qu'**une chose à la fois** et **teste après chaque modification**.") + "\n" + verifie(
        ("Pourquoi croise-t-on TX et RX ?", "Parce que **l'émission (TX) d'un appareil** doit arriver sur la **réception (RX)** de l'autre."),
        ("Pourquoi ne modifier qu'une seule chose à la fois ?", "Pour savoir **laquelle** a résolu (ou aggravé) le problème.")) + "\n" + retenir("Dépanner = câblage, masse, baud rate, programme ; une modification à la fois.")),
]
