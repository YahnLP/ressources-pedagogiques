# Archive : ancienne chaîne de génération des cours

Les pages `docs/seconde`, `docs/premiere` et `docs/terminale` ont d'abord été produites par les scripts de `import_e2/`
(import, enrichissements, corrigés, explications, TP ElectroLab…).

**Depuis le gel des pages, ces scripts ne doivent plus être exécutés** : ils écraseraient les modifications faites à la main.
Les fichiers Markdown de `docs/` sont désormais la **seule source de référence** : on les corrige et on les enrichit directement.

Les scripts sont conservés uniquement pour l'historique (et pour retrouver comment une figure ou un corrigé a été produit).
Les générateurs de figures (`outils/illustrations-e2/`) et de sujets ElectroLab (`outils/electrolab-sujets/`) restent utilisables : ils produisent des images et des fichiers `.json`, pas des cours.
