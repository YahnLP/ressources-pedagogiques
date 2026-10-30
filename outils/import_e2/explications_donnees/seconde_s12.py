import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🎯 OBJECTIFS", 'fin', apropos("Une carte vient d'être fabriquée. Comment savoir, **avant de l'alimenter**, qu'elle est sans défaut ?", "On la **teste méthodiquement avec un multimètre** : continuité des pistes, absence de court-circuit entre l'alimentation et la masse, et vérification des soudures. On **note** les résultats dans un **procès-verbal (PV)**.\n\nC'est ce que tu fais dans cette séance : **tester, contrôler, rédiger**.")),
    ("## 1️⃣", 'fin', clair("En **mode continuité**, le multimètre envoie un très petit courant entre ses deux pointes. **S'il passe**, il fait **BIP** : le chemin est fermé. **S'il ne passe pas**, silence : le chemin est coupé.\n\nOn teste **toujours hors tension**.") + "\n" + verifie(
        ("Que signifie un BIP en mode continuité ?", "Le chemin entre les deux pointes est **fermé** (continuité)."),
        ("Pourquoi teste-t-on hors tension ?", "Pour ne pas fausser la mesure et ne pas **endommager** le multimètre."),
        ("Quelle différence entre « pas de bip » et « BIP » sur un fil ?", "Pas de bip : le fil est **coupé** ; bip : il est **continu**.")) + "\n" + retenir("BIP = chemin fermé ; silence = chemin coupé ; toujours hors tension.")),
    ("## 2️⃣", 'fin', clair("Sur une carte, on enchaîne **trois tests** :\n\n1. **Continuité** de chaque piste importante (alimentation, masse, signaux) ;\n2. **Absence de court-circuit** entre le **+** et le **−** (en mode ohmmètre : une valeur **grande** est bon signe) ;\n3. **Vérification des soudures** (un bip peut disparaître si une soudure est froide).\n\nOn avance **dans l'ordre**, on **note** chaque résultat.") + "\n" + verifie(
        ("Le multimètre bipe entre le + et le − de l'alimentation. Que faut-il en conclure ?", "Il y a un **court-circuit** : il ne faut **pas** alimenter la carte avant de l'avoir cherché."),
        ("Quel test fait-on en premier ?", "La **continuité des pistes** d'alimentation et de masse, puis l'**absence de court-circuit**."),
        ("Pourquoi note-t-on chaque résultat ?", "Pour **garder une trace** et rédiger le PV, et pour repérer plus vite la cause d'un défaut.")) + "\n" + retenir("Continuité, court-circuit, soudures, dans cet ordre.")),
    ("## 3️⃣", 'fin', clair("Les défauts de fabrication **les plus fréquents** : **piste coupée** (pas de bip là où il en faut un), **court-circuit** entre pistes (bip là où il n'en faut pas), **soudure froide** (contact intermittent), **composant à l'envers** (polarité), **pastille décollée**.") + "\n" + verifie(
        ("Une piste ne bipe pas d'un bout à l'autre. Quel défaut ?", "Une **piste coupée**."),
        ("Une LED ne s'allume pas mais le circuit est complet. Que peut-on suspecter ?", "Une LED **à l'envers** ou une **soudure froide**.")) ),
    ("## 4️⃣", 'fin', clair("Une **procédure de contrôle** est une **liste d'étapes toujours identiques** : ainsi, **deux personnes différentes** trouvent les **mêmes défauts**. Elle va du **simple** (inspection visuelle) au **plus précis** (tests électriques).") + "\n" + verifie(
        ("Pourquoi suit-on toujours la même procédure ?", "Pour que le contrôle soit **reproductible** : le résultat ne dépend pas de la personne qui le fait.")) ),
    ("## 5️⃣", 'fin', clair("Le **procès-verbal (PV)** est la **preuve écrite** du contrôle. Il contient : la **référence** de la carte, la **date**, les **tests réalisés**, les **résultats mesurés**, la **conclusion** (conforme ou non) et la **signature**. Un PV doit être **clair** : quelqu'un d'autre doit comprendre ce que tu as fait.") + "\n" + verifie(
        ("Cite trois éléments d'un PV.", "Par exemple : la **référence de la carte**, la **date**, les **résultats des mesures**, la **conclusion**, la **signature**."),
        ("Pourquoi écrit-on la conclusion « conforme » ou « non conforme » ?", "Pour que la **décision** soit claire (la carte peut-elle être utilisée ?).")) + "\n" + retenir("Un PV = preuve écrite : tests, résultats, conclusion, signature.")),
]
