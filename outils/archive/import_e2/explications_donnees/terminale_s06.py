import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 1️⃣", 'debut', apropos("Tu dessines un schéma, tu routes une carte… et KiCad t'affiche **40 erreurs**. Comment éviter ça en travaillant **dans le bon ordre** ?", "Le flux KiCad est une **chaîne** : **schéma → ERC** (contrôle électrique) **→ empreintes → PCB → DRC** (contrôle géométrique) **→ fichiers Gerber → BOM**. Chaque étape **vérifie** la précédente : on ne passe pas à la suivante tant que la vérification n'est pas propre.")),
    ("## 1️⃣", 'fin', verifie(
        ("Que contrôle l'ERC ?", "Les **règles électriques** du schéma (broches non reliées, alimentations non pilotées, doublons de références)."),
        ("Que contrôle le DRC ?", "Les **règles géométriques** du circuit imprimé (distances, largeurs, perçages)."),
        ("Pourquoi corrige-t-on l'ERC avant de passer au PCB ?", "Une **erreur de schéma** se répercute sur tout le PCB : il est bien plus rapide de la corriger **avant**.")) + "\n" + retenir("ERC = schéma ; DRC = circuit imprimé ; on corrige chaque contrôle avant la suite.")),
    ("## 2️⃣", 'fin', clair("La plupart des erreurs ERC viennent de **cinq oublis** (voir le tableau). Le plus fréquent : l'absence de **PWR_FLAG**. KiCad doit savoir que **ton alimentation est bien une source** : on pose donc un symbole PWR_FLAG sur chaque rail (+VCC et GND).") + "\n" + verifie(
        ("L'ERC affiche `power_pin_not_driven`. Que faut-il vérifier ?", "La présence d'un **PWR_FLAG** sur le rail d'alimentation et sur la masse."),
        ("Une broche volontairement inutilisée génère `pin_not_connected`. Que faire ?", "Lui poser un **No Connect** (touche `Q`).")) + "\n" + retenir("PWR_FLAG sur +VCC et GND ; No Connect sur les broches inutilisées.")),
    ("## 3️⃣", 'fin', clair("Une **empreinte** est le dessin des pastilles sur le PCB. Un même composant peut exister en plusieurs boîtiers (traversant, CMS…) : **choisir la mauvaise empreinte** donne une carte où **le composant ne rentre pas**.") + "\n" + erreurs("Associer une empreinte sans **vérifier le datasheet** (écartement des broches, boîtier).") + "\n" + verifie(
        ("Pourquoi vérifie-t-on l'empreinte avec le datasheet ?", "Pour s'assurer que les **cotes des broches** correspondent au vrai composant.")) ),
    ("## 4️⃣", 'fin', clair("Avant de router, règle les **contraintes** : clearance minimale 0,25 mm, piste 0,25 mm, **pistes d'alimentation plus larges** (0,5 mm, car elles portent plus de courant). On place d'abord l'**alimentation**, puis le circuit principal, puis les passifs ; on **route l'alimentation en premier**, puis les signaux.") + "\n" + verifie(
        ("Pourquoi les pistes d'alimentation sont-elles plus larges ?", "Parce qu'elles transportent **plus de courant** : trop fines, elles chaufferaient."),
        ("Dans quel ordre route-t-on ?", "**Alimentation d'abord**, puis les signaux.")) + "\n" + retenir("Règles avant routage ; alimentation large et routée en premier.")),
    ("## 5️⃣", 'fin', clair("Les **fichiers Gerber** (un par couche) et le **fichier de perçage** sont ce que le fabricant reçoit. **Vérifie-les dans un visualiseur** avant de les envoyer : c'est ce qui sera réellement fabriqué.") + "\n" + verifie(
        ("Pourquoi ouvre-t-on les Gerber dans un visualiseur ?", "Pour **voir ce qui sera réellement fabriqué** et détecter une erreur avant commande.")) ),
    ("## 6️⃣", 'fin', clair("La **BOM** liste les composants **regroupés** par valeur et boîtier, avec leurs **repères** et la **quantité**. Elle sert à commander et à monter la carte.") + "\n" + verifie(
        ("Que contient une ligne de BOM ?", "Les **repères**, la **valeur**, l'**empreinte** et la **quantité**.")) ),
]
