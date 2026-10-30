# Semaine 5 : Du cahier des charges au schéma (CAO)

> **Durée** : 4 h · **Compétences E2 travaillées** : C07

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Saisir un schéma dans KiCad (bibliothèques, alimentation, PWR_FLAG).
- Annoter, renseigner les valeurs, lancer et corriger l'ERC.
- Associer une empreinte à chaque composant.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Prise en main de KiCad : projet, bibliothèques |
| 2 h | Saisie d'un schéma LED + transistor, puis NE555 ; ERC à 0 erreur |
| 1 h | Empreintes et auto-test |

## 📚 Ressources à utiliser

- [Première S01 – interface et premiers schémas](../../premiere/S01-interface-bibliotheques-schemas/01-cours.md)
- [Première S02 – saisie de schéma](../../premiere/S02-kicad-saisie-de-schema-bibliotheques/01-cours.md)
- [Terminale S06 – flux KiCad complet](../S06-flux-kicad-complet-schema-erc-pcb-drc/01-cours.md)

## ✅ Auto-test

1. À quoi sert un PWR_FLAG ?
2. Que contrôle l'ERC ? Le DRC ?
3. Que se passe-t-il si une empreinte est mal choisie ?
4. Comment lever une erreur « pin not connected » voulue ?
5. Pourquoi corriger l'ERC avant le PCB ?

??? success "Réponses"
    1. À indiquer à KiCad qu'un rail d'alimentation est **bien alimenté** (évite l'erreur « power pin not driven »).
    2. L'ERC contrôle les **règles électriques du schéma** ; le DRC les **règles géométriques du PCB**.
    3. Le composant **ne rentre pas** sur la carte fabriquée.
    4. Poser un **No Connect** (touche Q).
    5. Une erreur de schéma se répercute sur **tout le PCB**.

## 📦 Livrable

Schéma complet NE555 + LED, ERC à 0 erreur, empreintes associées.
