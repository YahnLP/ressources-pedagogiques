# Semaine 3 : Lire un schéma et une datasheet

> **Durée** : 4 h · **Compétences E2 travaillées** : C07

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Lire un schéma normalisé et repérer les blocs fonctionnels.
- Trouver dans une datasheet : brochage, limites absolues, caractéristiques min / typ / max.
- Calculer les composants autour d'un circuit à partir de la datasheet.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Symboles normalisés et lecture d'un schéma |
| 1 h | Anatomie d'une datasheet (7805) |
| 1 h | Datasheet du BC547 et du NE555 : exercices |
| 1 h | Auto-test et correction |

## 📚 Ressources à utiliser

- [Seconde S03 – schémas normalisés](../../seconde/S03-breadboard-schemas-electriques-normes/01-cours.md)
- [Seconde S06 – lecture de datasheet](../../seconde/S06-schemas-electriques-normes-tinkercad/01-cours.md)
- [Première S01 – lire une datasheet](../../premiere/S01-interface-bibliotheques-schemas/03-lire-une-datasheet.md)

## ✅ Auto-test

1. Que signifie « absolute maximum ratings » ?
2. Pour un calcul de sécurité, quelle colonne utilise-t-on : min, typ ou max ?
3. Quelle est la tension d'entrée maximale d'un 7805 ?
4. Quelle formule donne la fréquence d'un NE555 en astable ?
5. À quoi sert la section « pin configuration » ?

??? success "Réponses"
    1. Les limites à **ne jamais dépasser** : au-delà, le composant peut être détruit.
    2. Le **cas le plus défavorable** (min ou max selon le calcul), pas le typique.
    3. **35 V**.
    4. $f = \dfrac{1{,}44}{(R_a + 2R_b) \times C}$.
    5. À **câbler sans erreur** (numéro et nom des broches).

## 📦 Livrable

Fiche synthèse d'une datasheet au choix (brochage, limites, valeurs utiles).
