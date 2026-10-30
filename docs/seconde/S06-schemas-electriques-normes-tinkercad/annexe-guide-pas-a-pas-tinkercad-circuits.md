# 🖥️ GUIDE PAS À PAS — Tinkercad Circuits
## Créer, Simuler et Partager un Circuit Électronique

---

> **Document élève — À garder dans le portfolio numérique**
> BAC Pro CIEL | S6 Module E2 | MFR de Pontonx

---

## 📌 Accès et création de compte

### Étape 0 — Accéder à Tinkercad

```
1. Ouvrir Chrome ou Firefox
2. Aller sur : www.tinkercad.com
3. Cliquer sur "Se connecter" (haut droite)
4. Cliquer sur "Créer un compte personnel"
5. Renseigner : adresse email + mot de passe
6. Valider l'email de confirmation
7. → Vous êtes sur le tableau de bord Tinkercad
```

> 💡 **Si vous n'avez pas d'email** : Utiliser un compte de classe fourni par le formateur.

---

## PARTIE 1 — Créer un nouveau circuit

### Étape 1 — Accéder au module Circuits


```
Dans le tableau de bord :
  → Cliquer sur l'onglet "Circuits" dans le menu gauche ou en haut
  → Cliquer sur le bouton vert "+ Créer un nouveau circuit"
  → L'éditeur de circuit s'ouvre
```

### Étape 2 — Nommer le projet

```
  → Cliquer sur "Nouveau Circuit" en haut au centre
  → Taper le nom selon la convention : NOM_Prenom_S6_TP1
  → Appuyer sur Entrée pour valider
```

---

## PARTIE 2 — Ajouter des composants

### Étape 3 — Panneau Composants


Pour trouver un composant :
Option A → Taper son nom dans la barre de recherche
Option B → Dérouler la catégorie correspondante

Composants à connaître et leur emplacement :
| Composant | Catégorie |
|---|---|
| Résistance | Basiques |
| DEL (LED) | Basiques |
| Condensateur | Basiques |
| Pile (9V) | Basiques |
| Bouton-poussoir | Basiques |
| Multimètre | Instruments |
| Arduino Uno R3 | Microcontrôleurs |


### Étape 4 — Poser un composant sur le canvas

```
  1. Cliquer sur le composant voulu dans le panneau
  2. Il s'accroche au curseur de la souris
  3. Cliquer sur le canvas pour le déposer à l'endroit voulu
  4. Appuyer sur Échap pour désélectionner
```

### Étape 5 — Modifier la valeur d'un composant

1. Cliquer UNE FOIS sur le composant → il est sélectionné (bordure bleue)
2. Un encadré de propriétés apparaît (en haut ou en bas selon la version)
3. Modifier la valeur dans le champ "Résistance" ou "Tension" selon le composant
4. Valider en cliquant ailleurs

Exemples de valeurs à connaître :
| Composant | Champ | Valeur à taper |
|---|---|---|
| Résistance | Résistance | 390 (la valeur est en Ohms) |
| Pile | Tension | 9 (volts) |
| Condensateur | Capacitance | 100µ (microfarads) |
| DEL | Couleur | Choisir : rouge, vert, bleu… |


---

## PARTIE 3 — Connecter les composants

### Étape 6 — Tracer un fil de connexion


```
Pour tracer un fil :
  1. Positionner la souris sur une broche d'un composant
     → Un point VERT apparaît → c'est le signal de connexion disponible
  2. CLIQUER sur ce point vert
  3. Déplacer la souris vers la broche de destination
     → Le fil se trace automatiquement en angles droits (H/V)
  4. CLIQUER sur la broche de destination pour terminer le fil

Pour supprimer un fil :
  → Cliquer sur le fil pour le sélectionner → Touche Suppr
```

### Étape 7 — Changer la couleur d'un fil (optionnel mais recommandé)

```
  1. Cliquer sur le fil pour le sélectionner
  2. Choisir la couleur dans l'encadré de propriétés
  Convention recommandée :
    → Rouge = alimentation (+)
    → Noir = masse (GND, −)
    → Autres couleurs = liaisons signal
```

---

## PARTIE 4 — Simuler le circuit

### Étape 8 — Lancer la simulation


```
  → Cliquer sur le triangle vert "Démarrer la simulation"
  → Les composants s'animent : les LEDs s'allument, les multimètres affichent des valeurs
  → Si rien ne se passe : vérifier les connexions (fils complets ?)
  → Cliquer sur "Arrêter" pour modifier le circuit
  ATTENTION : on ne peut pas modifier le circuit pendant la simulation
```

### Étape 9 — Utiliser le multimètre virtuel

```
Pour mesurer une TENSION (voltmètre) :
  1. Poser un multimètre depuis le panneau Instruments
  2. Brancher la broche "+" du multimètre au point A (tension à mesurer)
  3. Brancher la broche "−" du multimètre au point B (référence, souvent GND)
  4. Sur le multimètre : sélectionner le mode Tension (V) et DCC (courant continu)
  5. Lancer la simulation → lire la valeur affichée

Pour mesurer un COURANT (ampèremètre) :
  1. Poser un multimètre
  2. L'insérer EN SÉRIE (interrompre un fil et insérer le multimètre dans la coupure)
  3. Sélectionner le mode Courant (A) et DCC
  4. Lancer la simulation → lire la valeur en A ou mA
```

---

## PARTIE 5 — Sauvegarder et partager

### Étape 10 — Sauvegarder

```
  → Tinkercad sauvegarde automatiquement dans le cloud
  → Forcer une sauvegarde : Ctrl + S
  → Vérifier que le nom du projet est correct (NOM_Prenom_S6_TP1)
```

### Étape 11 — Partager le circuit (pour remettre au formateur)


```
  → Cliquer sur l'icône "Partager" (flèche ou lien en haut à droite)
  → Dans la fenêtre qui s'ouvre : cliquer "Copier le lien"
  → Coller ce lien dans votre fiche portfolio ou l'envoyer au formateur
  → Vérifier que le projet est en "Public" ou "Partagé" (pas "Privé")
```

---

## 🔑 Raccourcis clavier utiles

| Raccourci | Action |
|---|---|
| **Ctrl + Z** | Annuler la dernière action |
| **Ctrl + S** | Sauvegarder manuellement |
| **Molette souris** | Zoom avant / arrière |
| **Clic droit + glisser** | Déplacer la vue |
| **Suppr** | Supprimer l'élément sélectionné |
| **Ctrl + D** | Dupliquer un composant |
| **Échap** | Désélectionner / annuler en cours |

---

## 🛠️ Problèmes fréquents et solutions

| Problème | Cause probable | Solution |
|---|---|---|
| La LED ne s'allume pas | Polarité inversée ou fil non connecté | Vérifier anode/cathode + vérifier les fils (point vert à chaque extrémité) |
| Le multimètre affiche "---" ou rien | Mode ou câblage incorrect | Vérifier le mode (V ou A) + vérifier le branchement parallèle/série |
| Je ne peux pas modifier le circuit | Simulation en cours | Cliquer "Arrêter la simulation" d'abord |
| Le fil ne se trace pas correctement | Mauvaise broche de départ | Vérifier qu'un point vert apparaît avant de cliquer |
| La valeur de résistance ne change pas | Mauvais composant sélectionné | Cliquer UNE FOIS sur la résistance (pas double-clic) |
| "Erreur de connexion" au chargement | Problème réseau | Recharger la page (F5) + vérifier connexion internet |

---

## 📏 Convention de nommage des projets S6

Tous vos projets Tinkercad de cette séance doivent être nommés selon cette convention :

```
  TP1 : NOM_Prenom_S6_TP1_LEDsimple
  TP2 : NOM_Prenom_S6_TP2_BoutonLED
  TP_Arduino (avancé) : NOM_Prenom_S6_Arduino_Blink
```

---

*Guide Tinkercad pas à pas — BAC Pro CIEL S6 Module E2 | MFR de Pontonx*
*Tinkercad est un produit Autodesk — tinkercad.com — Gratuit et sans installation*
