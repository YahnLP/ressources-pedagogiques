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

## 📖 Le cours en bref

??? question "🤔 À ton avis ?"
    On te donne une carte inconnue avec un composant marqué « LM7805 ». Comment savoir comment le brancher sans rien griller ?

    **Réponse** : on lit sa **datasheet** et le **schéma**. Cette semaine, tu apprends à lire ces deux documents, qui sont ta « notice » en électronique.

### 1. Lire un schéma

Un schéma est un **plan** : il montre **comment les composants sont reliés**, pas où ils sont posés.

- Chaque composant a un **repère** : **R**1 (résistance), **C**1 (condensateur), **D**1 (diode), **Q**1 (transistor), **U**1 (circuit intégré), **J**1 (connecteur).
- Les **traits** sont des fils ; un **point plein** à un croisement veut dire « relié », **sans point** = pas relié.
- Le **+** est en **haut**, la **masse (GND)** en bas, le signal de **gauche à droite**.

> [!TIP] 💡 En clair
> Pour comprendre un schéma, **découpe-le en blocs** : alimentation → traitement → sortie. Puis lis bloc par bloc.

### 2. Lire une datasheet

Une datasheet contient toujours les mêmes parties : description, **brochage**, **limites absolues**, **caractéristiques électriques** (min / typ / max), courbes, boîtier.

| À chercher | Pourquoi |
|---|---|
| **Brochage** | brancher chaque broche au bon endroit |
| **Absolute maximum ratings** | limites à **ne jamais dépasser** |
| **Electrical characteristics** | valeurs **garanties** pour calculer |
| **Package** | choisir l'empreinte du PCB |

On calcule toujours avec le **cas le plus défavorable** (min ou max), jamais avec la valeur « typique ».

### 3. Exemple : le régulateur 7805

- **Brochage** (boîtier TO-220) : 1 = entrée, 2 = masse, 3 = sortie.
- **Sortie** : 5 V (garantie de 4,8 à 5,2 V).
- **Entrée** : de 7 V à 35 V maximum.
- **Montage type** : un condensateur de 100 nF côté entrée et de 10 µF côté sortie.

### 4. Exemple : le transistor BC547

- Limites : $V_{CE}$ max = 45 V ; $I_C$ max = 100 mA.
- Gain $h_{FE}$ de 110 à 800 (très dispersé).
- Saturé : $V_{CE(sat)} \approx 0{,}2\,\mathrm{V}$.

### 5. Exemple : le NE555 en astable

$$f = \frac{1{,}44}{(R_a + 2R_b) \times C} \qquad DC = \frac{R_a + R_b}{R_a + 2R_b}$$

Avec $R_a = 10\,\mathrm{k\Omega}$, $R_b = 68\,\mathrm{k\Omega}$, $C = 10\,\mathrm{\mu F}$ : $f \approx 0{,}99\,\mathrm{Hz}$ et $DC \approx 53\,\%$.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Utiliser une datasheet du **mauvais composant** (vérifie la référence exacte et le fabricant).
> - Confondre **limite absolue** et **valeur de fonctionnement**.
> - Lire le brochage **vu du dessous** au lieu de vu du dessus (le dessin précise le sens).

## 📚 Pour approfondir : les séances à consulter

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
