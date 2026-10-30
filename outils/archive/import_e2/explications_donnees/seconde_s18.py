import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🗂️ Sommaire", 'fin', apropos("Tu as terminé ton projet. Mais **qui le sait** ? Comment convaincre un jury en 10 minutes que ton système fonctionne et que tu l'as compris ?", "Avec une **soutenance** bien préparée : **4 minutes de présentation**, **3 minutes de démonstration**, **3 minutes de questions**. Le jury ne veut pas t'entendre réciter : il veut voir que tu **comprends ce que tu as fait**.\n\nDans cette séance, tu apprends à **structurer**, à **démontrer** et à **répondre aux questions**, puis à **t'évaluer** avec la grille du jury.")),
    ("## 1.", 'fin', clair("Une soutenance évalue **trois choses** : ce que tu **sais** (savoir), ce que tu sais **faire** (savoir-faire) et la façon dont tu **communiques** (savoir-être).") + "\n" + verifie(
        ("Une soutenance est-elle une récitation de cours ?", "**Non** : on évalue ta capacité à **expliquer, démontrer et analyser** ton projet.")) ),
    ("## 2.", 'fin', clair("Le format dure **10 minutes** en tout : $4 + 3 + 3 = 10$ (présentation, démonstration, questions). **Tu ne peux pas lire** un texte écrit mot pour mot, mais tu peux avoir des **notes** comme guide.") + "\n" + verifie(
        ("Combien de temps dure la démonstration ?", "**3 minutes**."),
        ("Peut-on lire un texte rédigé à l'avance ?", "**Non** : seules des notes servant de guide sont autorisées.")) + "\n" + retenir("4 min présentation + 3 min démonstration + 3 min questions = 10 min.")),
    ("## 3.", 'fin', clair("Une présentation claire suit **toujours le même fil** : **contexte** (à quoi sert le projet), **solution** (ce que tu as choisi), **résultats** (ce que ça donne), **bilan** (ce qui a marché ou non).") + "\n" + verifie(
        ("Cite les quatre parties d'une présentation.", "**Contexte**, **solution**, **résultats**, **bilan**.")) ),
    ("## 4.", 'fin', clair("La démonstration est la partie **la plus risquée** : prépare **avant** tout le matériel, **teste** une dernière fois, et **prévois un plan B** (une vidéo ou des photos) si le montage plante.") + "\n" + erreurs("Brancher le montage **pendant** la soutenance.", "Dire « ça marche » sans le **montrer**.") + "\n" + verifie(
        ("Que faire si la démonstration échoue en direct ?", "**Rester calme**, expliquer ce qu'on suspecte, et utiliser le **plan B** (vidéo, photos).")) + "\n" + retenir("Préparer, tester, prévoir un plan B.")),
    ("## 5.", 'fin', clair("Face à une question du jury : **écoute jusqu'au bout**, **reformule** si besoin, puis **réponds simplement**. Si tu ne sais pas, **dis-le honnêtement** et explique **comment tu chercherais** la réponse.") + "\n" + verifie(
        ("Tu ne connais pas la réponse. Que fais-tu ?", "Tu le **dis honnêtement** et tu expliques **comment tu chercherais**.")) ),
    ("## 6.", 'fin', clair("Le jury évalue avec une **grille critériée** : pour chaque **compétence**, il choisit un **niveau** de maîtrise. Connaître la grille te permet de **savoir exactement ce qu'on attend** de toi.") + "\n" + verifie(
        ("À quoi sert une grille critériée ?", "À **évaluer chaque compétence** selon des critères clairs et connus à l'avance.")) ),
    ("## 7.", 'fin', clair("L'**auto-évaluation** consiste à te **situer toi-même** par rapport à la grille. Elle t'aide à voir **ce qu'il te reste à travailler** : être honnête avec soi-même est une qualité professionnelle.") + "\n" + retenir("S'auto-évaluer honnêtement = savoir quoi améliorer.")),
]
