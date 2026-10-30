import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🎯 OBJECTIFS", 'fin', apropos("Deux fabricants livrent la même carte. Comment le client peut-il **vérifier** qu'elle est bien de bonne qualité, **sans se fier à leur parole** ?", "En s'appuyant sur des **normes** : des règles communes écrites et reconnues. Un PV de validation indique **quelle norme** et **quel critère** la carte respecte, avec **les mesures** qui le prouvent.\n\nDans cette séance, tu découvres les **normes IPC, CEI et ISO**, tu rédiges un **PV de validation avancé** et tu construis un **DAT** (dossier technique).")),
    ("## 1️⃣", 'fin', clair("Une **norme** garantit que **tout le monde parle le même langage** : mêmes essais, mêmes critères, mêmes unités. Elle protège le **client** (qualité), le **fabricant** (règles claires) et l'**utilisateur** (sécurité).") + "\n" + verifie(
        ("Pourquoi les normes sont-elles utiles à un client ?", "Elles permettent de **juger la qualité** avec des critères communs, sans dépendre de la parole du fabricant.")) ),
    ("## 2️⃣", 'fin', clair("Trois familles à ne pas confondre : **IPC** (conception et fabrication des cartes), **CEI** (essais d'environnement et sécurité électrique) et **ISO** (qualité et organisation). Nos cartes de bac pro relèvent de la **classe B** (industriel).\n\n**Exemple d'essai CEI :** humidité à **40 °C / 85 % HR pendant 96 h** pour vérifier qu'une carte résiste à un local humide.") + "\n" + verifie(
        ("Quelle famille de normes décrit les essais d'environnement (chaleur, froid, humidité) ?", "La **CEI** (par exemple la série 60068-2)."),
        ("À quelle classe IPC correspondent nos cartes ?", "À la **classe B** (industriel)."),
        ("Pourquoi teste-t-on une carte à la chaleur ou à l'humidité ?", "Pour vérifier qu'elle **tient dans son environnement réel** d'utilisation.")) + "\n" + retenir("IPC = cartes ; CEI = essais ; ISO = qualité ; bac pro = classe B.")),
    ("## 3️⃣", 'fin', clair("Un **PV de validation fonctionnelle** relie **chaque exigence** à **une mesure** : exigence (ex. « sortie = 5 V ± 5 % »), méthode, valeur mesurée avec son incertitude, **verdict**. Il doit permettre à un tiers de **rejouer** le test.") + "\n" + verifie(
        ("Quelle tension est acceptable si l'exigence est 5 V ± 5 % ?", "De $5 \\times 0{,}95 = 4{,}75\\,\\mathrm{V}$ à $5 \\times 1{,}05 = 5{,}25\\,\\mathrm{V}$."),
        ("Mesure : 5,30 V. Verdict ?", "**Non conforme** : 5,30 V dépasse 5,25 V.")) + "\n" + retenir("Exigence chiffrée → mesure → verdict.")),
    ("## 4️⃣", 'fin', clair("Le **DAT** (dossier technique) regroupe **tout ce qu'il faut pour comprendre, fabriquer, tester et maintenir** une carte : schéma, BOM, plan de test, PV, consignes de maintenance. Un bon DAT permet à **quelqu'un d'autre** de reprendre le travail.") + "\n" + verifie(
        ("Cite trois éléments d'un DAT.", "Par exemple : **schéma**, **BOM**, **plan de test**, **PV**, **consignes de maintenance**.")) ),
    ("## 5️⃣", 'fin', clair("Les **contraintes de fonctionnement** (température, humidité, alimentation, vibrations) fixent **dans quelles conditions** la carte reste conforme. Elles figurent dans le DAT pour que l'utilisateur **ne dépasse pas** les limites.") + "\n" + verifie(
        ("Pourquoi indique-t-on des contraintes de fonctionnement ?", "Pour que l'utilisateur sache **jusqu'où** il peut utiliser la carte sans risque de panne.")) ),
]
