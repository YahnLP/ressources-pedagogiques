import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🗂️ Sommaire", 'fin', apropos("Ton casque sans fil reçoit la musique de ton téléphone sans aucun câble. Comment l'Arduino pourrait-il, lui aussi, **échanger avec un smartphone** ?", "Avec un **module Bluetooth** comme le **HC-05** : il se comporte comme un **câble série sans fil**. L'Arduino lui envoie des caractères par ses broches TX/RX, et le module les transmet par radio au téléphone.\n\nDans cette séance, tu apprends à **configurer** le HC-05 (commandes AT), à le **câbler** sans l'abîmer et à l'**appairer** avec ton smartphone.")),
    ("## 1.", 'fin', clair("Le **Bluetooth** est une liaison radio **courte portée** (une dizaine de mètres), qui consomme peu. Deux appareils doivent d'abord être **appairés** (ils se reconnaissent avec un code), puis ils peuvent échanger des données.") + "\n" + verifie(
        ("Que signifie « appairer » deux appareils ?", "Les faire **se reconnaître** (avec un code PIN) pour qu'ils puissent communiquer."),
        ("Quelle est la portée typique du Bluetooth ?", "Une **dizaine de mètres**.")) ),
    ("## 2.", 'fin', clair("Le HC-05 possède **6 broches** : **VCC**, **GND**, **TXD**, **RXD**, **STATE** et **EN/KEY**. Retiens surtout : **TXD** (il envoie) va vers **RX** de l'Arduino ; **RXD** (il reçoit) va vers **TX** de l'Arduino, **avec un diviseur de tension** car RXD ne supporte que **3,3 V**.") + "\n" + erreurs("Brancher RXD directement sur le 5 V de l'Arduino : le module peut être **endommagé**.") + "\n" + verifie(
        ("Où branche-t-on la broche TXD du HC-05 ?", "Sur la broche **RX** de l'Arduino."),
        ("Quelle broche demande un diviseur de tension ?", "**RXD**, car elle ne supporte que **3,3 V**.")) + "\n" + retenir("TXD → RX ; RXD → TX (avec diviseur).")),
    ("## 3.", 'fin', clair("Le HC-05 **transmet en radio** ce que tu lui envoies en série. Pour l'Arduino, **parler au HC-05 ou au PC, c'est la même chose** : on utilise `Serial` ou `SoftwareSerial`, avec les mêmes fonctions qu'en S13.") + "\n" + verifie(
        ("Pourquoi utilise-t-on `SoftwareSerial` avec le HC-05 ?", "Pour garder le port série matériel (USB) libre pour le **PC** pendant que le HC-05 utilise **deux autres broches**.")) ),
    ("## 4.", 'fin', clair("Les **commandes AT** servent à **configurer** le module (nom, code PIN, vitesse). On les envoie **en mode AT** : on met la broche **EN/KEY à l'état haut** au moment de l'alimentation, et la LED clignote **lentement** (environ toutes les 2 secondes). La vitesse du mode AT est de **38 400 bauds**. Chaque commande se termine par **retour à la ligne** : règle le moniteur sur « NL & CR ».") + "\n" + erreurs("Rester à 9600 bauds dans le moniteur : le module **ne répond pas**.", "Oublier « NL & CR » : la commande n'est pas validée.") + "\n" + verifie(
        ("Comment reconnaît-on que le HC-05 est en mode AT ?", "La LED clignote **lentement** (environ toutes les 2 s)."),
        ("À quelle vitesse communique-t-on avec le HC-05 en mode AT ?", "**38 400 bauds**."),
        ("Que répond le module à la commande `AT` ?", "`OK`.")) + "\n" + retenir("Mode AT : KEY à l'état haut, LED lente, 38 400 bauds, « NL & CR ».")),
    ("## 5.", 'fin', clair("Avant d'alimenter, **vérifie ton câblage** : alimentation, **masse commune**, TX/RX **croisés**, diviseur de tension sur RXD. Un câblage vérifié évite de détruire un module.") + "\n" + verifie(
        ("Quelles sont les trois vérifications avant d'alimenter ?", "**Alimentation correcte**, **masse commune**, **TX/RX croisés** (avec diviseur sur RXD).")) ),
    ("## 6.", 'fin', clair("Dans le sketch, on **lit** ce qui arrive du HC-05 pour **commander** quelque chose (par exemple une LED), et on **renvoie** une réponse au téléphone. Teste chaque partie **séparément** avant de les assembler.") + "\n" + verifie(
        ("Pourquoi teste-t-on le sketch par morceaux ?", "Pour **localiser** facilement l'erreur si ça ne marche pas.")) ),
    ("## 7.", 'fin', clair("Pour **appairer** : active le Bluetooth du téléphone, **cherche** « HC-05 », saisis le **code PIN** (par défaut **1234**), puis ouvre une **application de terminal Bluetooth**. Tu peux alors **envoyer et recevoir** des caractères.") + "\n" + verifie(
        ("Quel est le code PIN par défaut d'un HC-05 ?", "**1234**."),
        ("Que faut-il installer sur le smartphone pour échanger des caractères ?", "Une **application de terminal Bluetooth** (série).")) + "\n" + retenir("Appairage : chercher HC-05, PIN 1234, application de terminal.")),
]
