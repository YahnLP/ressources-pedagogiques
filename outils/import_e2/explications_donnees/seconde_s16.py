import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🗂️ Sommaire", 'fin', apropos("Une maison « intelligente » **ouvre les volets** quand il fait chaud et **affiche l'humidité** dans le salon. Quel capteur mesure à la fois **température et humidité** ?", "Le **DHT11** : un petit capteur à **trois ou quatre broches** qui mesure la **température** et l'**humidité**, puis envoie les deux valeurs sous forme de **données numériques** sur **un seul fil**.\n\nDans ce projet, tu réalises un **système domotique complet** : **mesurer, afficher, communiquer**, puis tu rédiges le **schéma électrique** correspondant.")),
    ("## 1.", 'fin', clair("Le **DHT11** mesure la **température** (de 0 à 50 °C, précision environ ±2 °C) et l'**humidité** (de 20 à 80 %, précision environ ±5 %). Il est **lent** : **une mesure par seconde au maximum**. Contrairement au LM35, il envoie **directement des valeurs numériques**.") + "\n" + verifie(
        ("Quelles grandeurs mesure le DHT11 ?", "La **température** et l'**humidité**."),
        ("Peut-on lire le DHT11 100 fois par seconde ?", "**Non** : une mesure par seconde au maximum."),
        ("Quelle différence avec le LM35 ?", "Le DHT11 envoie des **données numériques** ; le LM35 une **tension analogique**.")) + "\n" + retenir("DHT11 : température + humidité, numérique, 1 mesure/s au maximum.")),
    ("## 2.", 'fin', clair("Le DHT11 envoie ses données sur **un seul fil** (bus « 1-Wire » simplifié). Le **microcontrôleur demande** la mesure, puis le capteur **répond** avec **40 bits** : l'humidité, la température et un **contrôle d'erreur**.") + "\n" + verifie(
        ("Combien de fils de données faut-il pour le DHT11 ?", "**Un seul**."),
        ("À quoi sert le contrôle d'erreur ?", "À **vérifier** que les données reçues sont correctes.")) ),
    ("## 3.", 'fin', clair("La bibliothèque **s'occupe du protocole** à ta place : toi, tu appelles simplement `dht.readTemperature()` et `dht.readHumidity()`. **Teste** toujours si le résultat est valide (`isnan`) avant de l'afficher.") + "\n" + verifie(
        ("Pourquoi teste-t-on avec `isnan` ?", "Pour **détecter une lecture ratée** et ne pas afficher une valeur absurde.")) ),
    ("## 4.", 'fin', clair("Le DHT11 se câble avec **trois fils** : **+5 V**, **GND** et la broche de **données**. Une **résistance de 10 kΩ** entre données et +5 V (appelée résistance de **pull-up**) **stabilise** la ligne.") + "\n" + erreurs("Inverser +5 V et GND : le capteur chauffe et se détruit.", "Oublier la résistance de pull-up : lectures erratiques.") + "\n" + verifie(
        ("À quoi sert la résistance de pull-up ?", "À **maintenir la ligne de données au niveau haut** quand personne ne parle."),
        ("Combien de fils faut-il brancher sur un DHT11 ?", "Trois : **+5 V**, **GND** et **données**.")) + "\n" + retenir("DHT11 : +5 V, GND, données, avec pull-up de 10 kΩ.")),
    ("## 5.", 'fin', clair("Pour afficher **deux grandeurs** sur un écran 16×2, on utilise **une ligne par grandeur** : la température sur la ligne 0, l'humidité sur la ligne 1.") ),
    ("## 6.", 'fin', clair("Un système domotique complet suit une **chaîne** : **capteur → Arduino → affichage / Bluetooth**. Découpe-le en **blocs** : tu programmes et tu testes **chaque bloc séparément**, puis tu les assembles.") + "\n" + verifie(
        ("Cite les trois blocs d'un système domotique simple.", "**Acquisition** (capteur), **traitement** (Arduino), **communication / affichage**.")) + "\n" + retenir("Un système = des blocs testés séparément, puis assemblés.")),
    ("## 7.", 'fin', clair("Un **schéma professionnel** doit se lire **sans explication** : **symboles normalisés**, fils **droits** (angles à 90°), croisements **sans point** si les fils ne sont pas reliés, **points de connexion** marqués, **composants repérés** (R1, C1…) et **valeurs indiquées**.") + "\n" + verifie(
        ("Deux fils se croisent sans point de connexion. Sont-ils reliés ?", "**Non** : seul un **point** indique une connexion."),
        ("Que doit-on indiquer à côté de chaque composant ?", "Son **repère** (R1, C1…) et sa **valeur**.")) + "\n" + retenir("Schéma pro : symboles normalisés, repères, valeurs, points de connexion.")),
]
