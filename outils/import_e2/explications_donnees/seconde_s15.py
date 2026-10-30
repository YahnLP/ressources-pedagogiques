import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🗂️ Sommaire", 'fin', apropos("Ton Arduino sait calculer une température, mais personne ne la voit… Comment **afficher** le résultat sur un petit écran **sans utiliser une dizaine de broches** ?", "Avec un écran LCD équipé d'un **module I2C** : il ne demande que **deux fils de données** (SDA et SCL) au lieu de plus de dix. Il suffit ensuite de **deux fils d'alimentation**.\n\nDans cette séance, tu apprends à **comprendre l'I2C**, à **afficher du texte** sur un LCD 16×2 et à y montrer la **température du LM35**.")),
    ("## 1.", 'fin', clair("L'**I2C** est un protocole à **deux fils** : **SDA** (les données) et **SCL** (l'horloge). Plusieurs appareils peuvent partager **les mêmes deux fils**, chacun étant repéré par une **adresse** (souvent `0x27` ou `0x3F` pour un écran LCD). Sur l'Arduino Uno : **SDA = A4**, **SCL = A5**.") + "\n" + verifie(
        ("Quels sont les deux fils de l'I2C ?", "**SDA** (données) et **SCL** (horloge)."),
        ("À quoi sert l'adresse I2C ?", "À **repérer** chaque appareil sur les mêmes deux fils."),
        ("Sur quelles broches de l'Arduino Uno trouve-t-on SDA et SCL ?", "**SDA = A4** et **SCL = A5**.")) + "\n" + erreurs("Se tromper d'adresse (`0x27` ou `0x3F`) : l'écran reste éteint ou vide.", "Intervertir SDA et SCL.") + "\n" + retenir("I2C = 2 fils (SDA, SCL) + une adresse par appareil.")),
    ("## 2.", 'fin', clair("L'écran **16×2** affiche **2 lignes de 16 caractères**. Sa position s'exprime avec **(colonne, ligne)** et la numérotation commence à **0** : `lcd.setCursor(0, 1)` place le curseur au **début de la deuxième ligne**.") + "\n" + verifie(
        ("Combien de caractères au maximum sur l'écran ?", "$16 \\times 2 = 32$ caractères."),
        ("Que fait `lcd.setCursor(0, 1)` ?", "Il place le curseur au **début de la 2ᵉ ligne** (numérotation à partir de 0).")) ),
    ("## 3.", 'fin', clair("Une **bibliothèque** est du code **déjà écrit** que tu réutilises. Avec `LiquidCrystal_I2C`, trois instructions suffisent : `lcd.init()` pour démarrer, `lcd.backlight()` pour allumer le rétro-éclairage, `lcd.print()` pour écrire.") + "\n" + verifie(
        ("À quoi sert une bibliothèque ?", "À **réutiliser du code déjà écrit** au lieu de tout reprogrammer."),
        ("Quelle instruction affiche du texte ?", "`lcd.print()`.")) + "\n" + retenir("`init()` démarre, `backlight()` allume, `print()` écrit.")),
    ("## 4.", 'fin', clair("Rappel de S09 : le LM35 donne **10 mV par °C**, et $T = \\text{valeur} \\times \\dfrac{5}{1023} \\times 100$.") ),
    ("## 5.", 'fin', clair("On **assemble** deux briques que tu connais : **mesurer** la température (S09) puis l'**afficher** (LCD). Pour éviter que d'anciens caractères restent à l'écran, on **efface** la ligne ou on réécrit des **espaces** avant d'afficher la nouvelle valeur.") + "\n" + verifie(
        ("Pourquoi efface-t-on l'écran avant d'écrire une nouvelle valeur ?", "Pour ne pas garder d'**anciens caractères** (par exemple « 100 » devenant « 99 » laisserait un « 0 »).")) ),
    ("## 6.", 'fin', clair("Quand on assemble **LM35 + LCD + HC-05**, la règle d'or est **d'ajouter un élément à la fois** et de **tester** à chaque étape : si tout est branché d'un coup et que ça ne marche pas, on ne sait plus où chercher.") + "\n" + verifie(
        ("Pourquoi ajoute-t-on les modules un par un ?", "Pour **localiser** facilement la cause d'un problème.")) + "\n" + retenir("Assembler = un module à la fois, test à chaque étape.")),
]
