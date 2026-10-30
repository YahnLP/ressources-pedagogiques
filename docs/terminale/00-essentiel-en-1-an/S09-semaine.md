# Semaine 9 : Dépanner un circuit simple

> **Durée** : 4 h · **Compétences E2 travaillées** : C11

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Appliquer la méthode : décrire, mesurer, comparer, isoler, réparer, tester.
- Construire un tableau de tensions attendues / mesurées.
- Remplir une fiche d'intervention et appliquer les règles de sécurité.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | La méthode et la sécurité (TBT, ESD, EPI) |
| 1 h | Cas pratique : LED pilotée par un transistor (4 pannes) |
| 1 h | Dépannage sur maquette ESP32 (démarche DECA) |
| 1 h | Fiche d'intervention et auto-test |

## 📚 Ressources à utiliser

- [Terminale S12 – dépanner un circuit simple](../S12-reussir-un-tp-de-mesure-en-45-minutes/03-depannage-circuit-simple.md)
- [Première S14 – maintenance corrective](../../premiere/S14-maintenance-corrective-diagnostic-de/01-cours.md)
- [Seconde S05 – sécurité et environnement](../../seconde/S05-maintenance-n1-nettoyage-de-cartes/02-securite-et-environnement.md)

## ✅ Auto-test

1. Par quoi commence-t-on un dépannage ?
2. Où se cache la panne dans un tableau de tensions ?
3. Pourquoi mesure-t-on une résistance hors tension ?
4. Combien de composants change-t-on à la fois ?
5. À partir de quelle tension faut-il une habilitation ?

??? success "Réponses"
    1. Par **décrire** le symptôme et **vérifier l'alimentation**, pas par changer des composants.
    2. À la **première** valeur mesurée qui ne correspond pas à la valeur attendue.
    3. Sous tension, la mesure est **fausse** et peut endommager l'appareil.
    4. **Un seul**, puis on reteste.
    5. Au-delà de **50 V alternatif ou 120 V continu**.

## 📦 Livrable

Fiche d'intervention remplie pour une panne diagnostiquée.
