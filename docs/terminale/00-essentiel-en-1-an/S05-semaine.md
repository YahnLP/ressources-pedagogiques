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

## 📖 Le cours en bref

??? question "🤔 À ton avis ?"
    Pourquoi dessiner le schéma **dans un logiciel** plutôt que sur papier, alors qu'on va ensuite faire le circuit imprimé ?

    **Réponse** : parce que le logiciel (KiCad) **garde en mémoire les liaisons** : c'est ce qu'il transmet ensuite au circuit imprimé (**netlist**). Une erreur de schéma se répercute partout : on la contrôle donc avant.

### 1. Le flux de travail

**Schéma → ERC → empreintes → PCB → DRC → fichiers de fabrication.** Chaque étape se **vérifie** avant la suivante.

### 2. Saisir un schéma dans KiCad (Eeschema)

1. **A** : ajouter un composant (cherche par nom : `R`, `LED`, `NE555`, `BC547`).
2. **P** : ajouter une alimentation (+5 V, GND).
3. **W** : tracer les fils.
4. **L** : poser une étiquette de réseau (net label) pour relier sans tracer.
5. **Annoter** (R1, R2…) et **saisir les valeurs**.
6. **ERC** : contrôle électrique.

### 3. L'ERC et ses erreurs classiques

| Erreur | Cause | Solution |
|---|---|---|
| `power_pin_not_driven` | KiCad ne sait pas qu'une source alimente le rail | poser un **PWR_FLAG** |
| `pin_not_connected` | broche en l'air | la relier, ou poser un **No Connect** (Q) |
| `duplicate_reference` | deux composants avec le même repère | annoter à nouveau |

### 4. Les empreintes (footprints)

L'**empreinte** est le dessin des **pastilles** sur le circuit imprimé. Elle doit correspondre au **boîtier réel** :

- **THT** (traversant) : pattes qui traversent la carte ; facile à souder à la main.
- **CMS** (monté en surface) : composant posé sur les pistes ; plus petit.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Choisir une empreinte **sans vérifier la datasheet** : le composant ne rentre pas.
> - Oublier les **PWR_FLAG** ou la **valeur** des composants.
> - Passer au PCB avec des erreurs d'ERC.

### Exercice guidé

Dessine : un connecteur 2 broches (+12 V, GND), un 7805 avec condensateurs 100 nF et 10 µF, puis une LED avec sa résistance de 150 Ω. Ajoute 2 PWR_FLAG (sur +5 V et GND). L'ERC doit afficher **0 erreur**.

## 📚 Pour approfondir : les séances à consulter

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
