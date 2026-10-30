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

## 📖 Le cours en bref

??? question "🤔 À ton avis ?"
    Un circuit ne marche plus. Tu as un fer à souder et un multimètre. Que fais-tu **en premier** ?

    **Réponse** : tu **observes** et tu **mesures l'alimentation**. Remplacer des composants au hasard fait perdre du temps et risque d'abîmer le circuit.

### 1. La méthode en 6 étapes

1. **Décrire** le symptôme (qu'est-ce qui marche ? qu'est-ce qui ne marche pas ?).
2. **Sécuriser** (tension, chaleur, odeur de brûlé).
3. **Vérifier l'alimentation** sur la carte.
4. **Dresser un tableau de tensions** : point de mesure, valeur attendue, valeur mesurée, verdict.
5. **Isoler** : couper le circuit en deux pour savoir de quel côté est la panne (dichotomie).
6. **Réparer** (un seul changement), **retester**, **tracer** (fiche d'intervention).

### 2. Trouver la panne avec les tensions

La panne est à la **première valeur** qui ne correspond pas à l'attendu, en partant de l'alimentation.

**Exemple** (LED pilotée par un transistor, 5 V) : base ≈ 0,7 V, collecteur ≈ 0,2 V quand tout va bien.

| Symptôme mesuré | Cause probable |
|---|---|
| signal d'entrée 5 V, base à 0 V | résistance de base coupée |
| signal d'entrée 0 V | problème **en amont** du circuit |
| collecteur à 0 V même sans commande | transistor en court-circuit |
| base normale mais collecteur à 1,8 V | transistor qui ne sature pas (résistance de base trop grande) |

### 3. Les mesures hors tension

- **Résistance** : retirée du circuit.
- **Transistor / diode** : test diode (≈ 0,6 V dans un sens, rien dans l'autre).
- **Continuité** : pistes et fils (bip).

### 4. Sécurité

- **Très basse tension** (≤ 50 V AC / 120 V DC) : pas de risque d'électrisation, mais attention à la chaleur et aux courts-circuits.
- Au-delà : **habilitation** (BR) obligatoire.
- **ESD** : bracelet, tapis, sachets antistatiques.

### 5. La fiche d'intervention

Équipement, date, intervenant · symptôme · mesures (attendu / mesuré) · cause · action · test après réparation · préconisation.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Mesurer une résistance **sous tension**.
> - Changer **plusieurs** composants à la fois.
> - Oublier de **retester** (la panne a-t-elle disparu ? autre chose est-il en panne ?).

## 📚 Pour approfondir : les séances à consulter

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
