import sys; sys.path.insert(0, __import__("pathlib").Path(__file__).resolve().parents[1].as_posix())
from explications import *

ENTREES = [
    ("## 🗂️ Sommaire", 'fin', apropos("Ton montage fonctionne **quand tu le regardes**. Mais comment **prouver** à quelqu'un d'autre qu'il fonctionne… et comment le réparer s'il tombe en panne ?", "Avec des **tests écrits**, une **documentation** (schéma, liste des composants) et une **méthode de dépannage**. Ce sont les **preuves** qu'un technicien laisse derrière lui.\n\nDans cette séance, tu apprends à **tester**, à **documenter** et à **dépanner** ton système.")),
    ("## 1.", 'fin', clair("Un **test d'intégration** vérifie que **plusieurs éléments assemblés** fonctionnent **ensemble**. Chaque élément peut marcher seul et pourtant **l'ensemble échouer** (mauvais câblage, conflit de broches, alimentation insuffisante).") + "\n" + verifie(
        ("Pourquoi un test d'intégration est-il utile si chaque module a déjà été testé seul ?", "Parce que les modules peuvent **mal fonctionner ensemble** (conflits, alimentation, câblage)."),
        ("Cite un exemple de problème visible seulement à l'assemblage.", "Deux modules qui utilisent la **même broche**, ou une **alimentation trop faible**.")) ),
    ("## 2.", 'fin', clair("Un **protocole de test** est un tableau avec : **ce qu'on teste**, **comment**, le **résultat attendu**, le **résultat obtenu** et **OK / NOK**. Écris le **résultat attendu AVANT** de faire le test, sinon tu risques de **trouver « normal »** ce que tu observes.") + "\n" + erreurs("Remplir « résultat attendu » après avoir fait la mesure.") + "\n" + verifie(
        ("Pourquoi écrit-on le résultat attendu avant le test ?", "Pour **comparer honnêtement** : sinon on ajuste l'attendu à ce qu'on observe."),
        ("Quelles colonnes contient un protocole de test ?", "Test, méthode, résultat **attendu**, résultat **obtenu**, **OK/NOK**.")) + "\n" + retenir("Protocole = attendu écrit avant, obtenu mesuré, verdict OK/NOK.")),
    ("## 3.", 'fin', clair("Le **schéma annoté** est la **carte** de ton système : symboles normalisés, **repères**, **valeurs**, **numéros de broches**. Quelqu'un d'autre doit pouvoir **reconstruire** ton montage avec ce seul document.") + "\n" + verifie(
        ("Quel est le critère d'un bon schéma annoté ?", "Quelqu'un d'autre peut **reconstruire le montage** à partir du seul schéma.")) ),
    ("## 4.", 'fin', clair("La **BOM** (nomenclature) est la **liste des composants** : **repère**, **désignation**, **valeur**, **quantité**. Elle sert à **commander**, à **vérifier** le montage et à **dépanner**.") + "\n" + verifie(
        ("À quoi sert une BOM ?", "À **lister tous les composants** (repère, valeur, quantité) pour commander, monter et dépanner."),
        ("Un schéma contient R1, R2, R3 de même valeur. Quelle quantité écris-tu pour cette valeur ?", "**3**.")) + "\n" + retenir("BOM = repère, désignation, valeur, quantité.")),
    ("## 5.", 'fin', clair("Dépanner, c'est **raisonner**, pas essayer au hasard : **1. observer** (qu'est-ce qui ne marche pas exactement ?), **2. supposer** (quelle cause possible ?), **3. mesurer** (vérifier avec le multimètre), **4. corriger**, **5. retester**.") + "\n" + verifie(
        ("Quelle est la première étape d'un dépannage ?", "**Observer** précisément le symptôme."),
        ("Pourquoi retester après la correction ?", "Pour vérifier que le défaut a **bien disparu** et qu'aucun autre n'est apparu.")) + "\n" + retenir("Observer, supposer, mesurer, corriger, retester.")),
    ("## 6.", 'fin', clair("Les **outils** du dépanneur : le **multimètre** (tension, continuité), le **moniteur série** (ce que dit le programme), l'**inspection visuelle** (soudures, composants à l'envers) et la **substitution** (essayer un composant sûr à la place).") + "\n" + verifie(
        ("Quel outil permet de voir ce que « pense » le programme ?", "Le **moniteur série**.")) ),
]
