import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## ÉTAPE 1", 'debut', apropos("À quelques semaines de l'épreuve, **où perds-tu le plus de points** ? Sais-tu vraiment ce que tu dois retravailler en priorité ?", "Cette séance t'aide à **cibler** tes lacunes (bilan personnel), à **comprendre** tes erreurs (erreurs types) puis à les **corriger** par des ateliers. Mieux vaut **travailler 2 points précis** que tout reprendre au hasard.")),
    ("## ÉTAPE 2", 'debut', clair("Une **erreur type** revient chez plusieurs élèves : oubli d'unité, arrondi trop tôt, mauvaise conversion, schéma sans PWR_FLAG… Repérer **tes** erreurs types t'évite de les refaire le jour de l'épreuve.") + "\n" + retenir("Noter ses erreurs types = ne plus les refaire.")),
]
