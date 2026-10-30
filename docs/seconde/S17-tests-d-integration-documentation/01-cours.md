# 📘 FICHE DE COURS ÉLÈVE — S17
## Tests d'intégration · Documentation technique (Schéma + BOM) · Résolution de pannes réelles

---

> **Compétences travaillées** : C1.2 – C3.2 – C4.1 – C4.2
> **Durée de lecture guidée** : ~45 minutes
> **Prérequis** : S14 (Bluetooth HC-05), S15-S16 (projet en cours)

---

## 🗂️ Sommaire

1. Les tests d'intégration — définition et méthode
2. Le protocole de tests — comment le construire
3. La documentation technique : le schéma annoté
4. La BOM (Bill of Materials) — nomenclature des composants
5. Méthodologie de résolution de pannes
6. Les outils du dépannage
7. Vocabulaire clé à maîtriser

---

## 1. Les tests d'intégration — définition et méthode

### 1.1 Qu'est-ce qu'un test d'intégration ?

Lorsque tu construis un système électronique (comme ton projet Arduino-Bluetooth), tu as d'abord testé chaque partie **séparément** :
- La communication Bluetooth seule (S14)
- Les DEL seules
- Le sketch Arduino seul

Un **test d'intégration** vérifie que **toutes ces parties fonctionnent correctement ensemble**, comme un seul système complet.

> 💡 **Analogie** : Imagine que tu construises une voiture. Tu testes d'abord le moteur seul, puis les freins seuls, puis les phares seuls. Le test d'intégration, c'est quand tu mets tout ensemble et que tu vérifies que la voiture démarre, freine ET éclaire **en même temps**, dans toutes les conditions.

### 1.2 Les niveaux de tests en électronique

```
[ILLUSTRATION 1]
Légende : Pyramide des niveaux de tests en électronique, de la base au sommet :
Base (large) = Tests unitaires (composant par composant),
Milieu = Tests d'intégration (sous-systèmes assemblés),
Sommet = Tests système (produit complet en conditions réelles).
Chaque niveau est coloré différemment (vert, orange, rouge) avec une icône représentative.
PROMPT ILLUSTRATION : "Clean infographic pyramid showing three levels of electronic testing:
Bottom (green, wide): 'Tests unitaires' with icon of single LED/resistor.
Middle (orange): 'Tests d'intégration' with icon of Arduino + HC-05 together.
Top (red, narrow): 'Tests système' with icon of complete device + smartphone.
White background, French labels, professional engineering style, flat design."
```

| Niveau | Quoi tester ? | Exemple pour notre projet |
|---|---|---|
| **Test unitaire** | Un seul composant à la fois | Vérifier que la DEL rouge s'allume avec 3,3V |
| **Test d'intégration** | Plusieurs composants ensemble | Vérifier que la commande BT allume bien la DEL |
| **Test système** | Le système complet en situation réelle | Contrôler les 3 DEL depuis 5 m, dans une autre pièce |

---

## 2. Le protocole de tests — comment le construire

### 2.1 Pourquoi un protocole ?

Un **protocole de tests** est un document qui décrit, **avant** de tester, exactement :
- **Ce que** l'on va tester (le cas de test)
- **Comment** on va le tester (la procédure)
- **Ce qu'on attend** comme résultat
- **Ce qu'on obtient** réellement

Sans protocole, les tests sont aléatoires et les résultats ne sont pas exploitables ni reproductibles.

### 2.2 Structure d'un cas de test

Chaque ligne du tableau de tests doit contenir :

| Champ | Description |
|---|---|
| **N° de test** | Identifiant unique (ex : T-01) |
| **Fonctionnalité testée** | Ce que le test vérifie |
| **Préconditions** | État du système avant le test |
| **Action** | Ce que l'opérateur fait |
| **Résultat attendu** | Ce qui doit se passer si tout est OK |
| **Résultat obtenu** | Ce qui s'est passé réellement |
| **Statut** | ✅ Conforme / ❌ Non-conforme / ⚠️ Partiel |

### 2.3 Exemple de protocole de tests pour le projet S14-S17

```
[ILLUSTRATION 2]
Légende : Extrait de tableau de protocole de tests rempli, montrant 3 lignes avec les colonnes :
N° test, Fonctionnalité testée, Action, Résultat attendu, Résultat obtenu, Statut (✅/❌).
La mise en forme est professionnelle, style document technique industriel.
PROMPT ILLUSTRATION : "Professional test protocol table screenshot showing 3 filled rows:
Row 1: T-01, Connexion Bluetooth, Tap Connect in app, LED HC-05 solid, LED solid, green checkmark.
Row 2: T-02, Allumage DEL rouge, Send 'R1', Red LED on + message, Red LED on, green checkmark.
Row 3: T-03, Commande ETAT, Send 'ETAT', 3 status lines shown, partial result, orange warning.
Clean spreadsheet style, French headers, professional formatting."
```

| N° | Fonctionnalité | Précondition | Action | Résultat attendu | Résultat obtenu | Statut |
|---|---|---|---|---|---|---|
| T-01 | Appairage BT | HC-05 alimenté, LED clignote vite | Connecter depuis app | LED HC-05 fixe | | |
| T-02 | Commande R1 | Connecté BT | Envoyer `R1` | DEL rouge allumée + `"DEL rouge allumee"` reçu | | |
| T-03 | Commande R0 | DEL rouge allumée | Envoyer `R0` | DEL rouge éteinte + message reçu | | |
| T-04 | Commande J1 | Connecté BT | Envoyer `J1` | DEL jaune allumée + message reçu | | |
| T-05 | Commande J0 | DEL jaune allumée | Envoyer `J0` | DEL jaune éteinte + message reçu | | |
| T-06 | Commande V1 | Connecté BT | Envoyer `V1` | DEL verte allumée + message reçu | | |
| T-07 | Commande V0 | DEL verte allumée | Envoyer `V0` | DEL verte éteinte + message reçu | | |
| T-08 | Commande ETAT | Au moins 1 DEL allumée | Envoyer `ETAT` | Affichage des 3 états | | |
| T-09 | Commande inconnue | Connecté BT | Envoyer `XYZ` | Message d'erreur reçu | | |
| T-10 | Test de portée 5 m | Connecté BT, 5 m de distance | Envoyer `R1` | Commande exécutée | | |
| T-11 | Test de portée 10 m | Connecté BT, 10 m | Envoyer `R1` | Commande exécutée ou déconnexion | | |

---

## 3. La documentation technique : le schéma annoté

### 3.1 Pourquoi un schéma annoté ?

Un schéma électrique permet à **n'importe quel technicien** de comprendre, reproduire ou dépanner un montage **sans avoir besoin d'expliquer verbalement**. C'est un langage universel dans le domaine de l'électronique et de l'électrotechnique.

**"Annoté"** signifie que le schéma contient :
- Les **valeurs** de tous les composants (ex : R1 = 220Ω)
- Les **références** des composants (ex : U1 = Arduino UNO, BT1 = HC-05)
- Les **tensions** aux points stratégiques (ex : +5V, +3,3V, GND)
- Un **cartouche** (cadre de titre) avec les informations du projet

### 3.2 Conventions à respecter

```
[ILLUSTRATION 3]
Légende : Exemples de symboles électroniques normalisés pour les composants du projet :
résistance (symbole rectangle ou zigzag selon norme), DEL avec flèches lumière, Arduino représenté
comme un bloc avec ses broches numérotées, module HC-05 comme un bloc rectangulaire avec VCC/GND/TX/RX.
Chaque symbole est accompagné de son nom et d'un exemple de référence (R1, D1, U1, BT1).
PROMPT ILLUSTRATION : "Technical electronic schematic symbols reference sheet showing:
Resistor (European rectangle style, labeled R1=220Ω), LED (triangle+bar with light arrows, labeled D1),
Arduino UNO (rectangular block with pin labels D4,D5,D6,D10,D11,5V,GND, labeled U1),
HC-05 module (rectangular block with VCC,GND,TXD,RXD labels, labeled BT1).
Clean engineering drawing style, black on white, IEC standard symbols."
```

| Élément | Convention |
|---|---|
| **Résistance** | Symbole rectangle (norme IEC/européenne) avec valeur en Ω |
| **DEL** | Triangle + barre avec flèches lumière, polarité (+/-) indiquée |
| **Fils** | Lignes droites horizontales/verticales uniquement |
| **Nœuds** | Point noir si deux fils se croisent et sont connectés |
| **Références** | R1, R2… pour résistances ; D1, D2… pour DEL ; U1 pour microcontrôleur ; BT1 pour module BT |
| **Valeurs** | Toujours indiquées à côté du symbole |
| **Alimentation** | Symbole +5V en haut, GND (triangle pointe en bas) en bas |

### 3.3 Le cartouche obligatoire

Le cartouche est le "badge d'identité" du schéma. Il se place en bas à droite de la feuille.

| Champ cartouche | Exemple |
|---|---|
| Titre du projet | Contrôle sans fil Bluetooth – 3 DEL |
| Auteur(s) | DUPONT Martin, MARTIN Sophie |
| Date | 01/03/2026 |
| Version | V1.0 |
| Établissement | LP [Nom de l'établissement] |
| Feuille | 1/1 |

---

## 4. La BOM (Bill of Materials) — Nomenclature des composants

### 4.1 Définition

La **BOM** (en français : *nomenclature des composants* ou *liste de matériel*) est un document qui recense **tous les composants** utilisés dans un projet, avec leurs caractéristiques et leur coût. C'est un document **indispensable** dans l'industrie pour :

- **Commander** les composants auprès des fournisseurs
- **Calculer** le coût de fabrication d'un produit
- **Reproduire** le montage à l'identique
- **Maintenir** le matériel en cas de panne (avoir les références pour commander les pièces de remplacement)

> 💡 **Analogie** : La BOM, c'est comme la **liste d'ingrédients d'une recette** — mais en version professionnelle, avec les fournisseurs, les quantités exactes et les prix unitaires.

### 4.2 Structure d'une BOM professionnelle

```
[ILLUSTRATION 4]
Légende : Extrait d'une BOM remplie dans un tableur, avec les colonnes : Référence projet (R1, R2…),
Désignation (Résistance 220Ω), Quantité, Valeur/Type, Référence fournisseur, Fournisseur,
Prix unitaire HT, Prix total HT. Deux lignes sont remplies à titre d'exemple. Style tableur professionnel.
PROMPT ILLUSTRATION : "Screenshot of a professional Bill of Materials spreadsheet with columns:
Ref Projet | Désignation | Quantité | Valeur/Type | Réf Fournisseur | Fournisseur | PU HT (€) | Total HT (€).
Rows filled: R1-R4: Résistance 220Ω, 4, 220Ω 1/4W, MRS25000C2200FRP00, Farnell, 0.10€, 0.40€.
BT1: Module Bluetooth HC-05, 1, HC-05 Maître/Esclave, HC-05-MODULE, Gotronic, 5.50€, 5.50€.
Professional Excel/LibreOffice style, French headers, color-coded header row."
```

### 4.3 Modèle de BOM à compléter pour le projet

| Réf Projet | Désignation | Qté | Valeur / Type | Réf Fournisseur | Fournisseur | PU HT (€) | Total HT (€) |
|---|---|---|---|---|---|---|---|
| U1 | Microcontrôleur | 1 | Arduino UNO R3 | | | | |
| BT1 | Module Bluetooth | 1 | HC-05 | | | | |
| R1 | Résistance pont diviseur | 1 | 1 kΩ – 1/4W | | | | |
| R2 | Résistance pont diviseur | 1 | 2 kΩ – 1/4W | | | | |
| R3 | Résistance limitation DEL rouge | 1 | 220 Ω – 1/4W | | | | |
| R4 | Résistance limitation DEL jaune | 1 | 220 Ω – 1/4W | | | | |
| R5 | Résistance limitation DEL verte | 1 | 220 Ω – 1/4W | | | | |
| D1 | Diode électroluminescente rouge | 1 | 5mm – rouge | | | | |
| D2 | Diode électroluminescente jaune | 1 | 5mm – jaune | | | | |
| D3 | Diode électroluminescente verte | 1 | 5mm – verte | | | | |
| BB1 | Breadboard | 1 | 830 points | | | | |
| CAB | Câbles de liaison Dupont | 20 | Mâle-Mâle/Femelle | | | | |
| ALI | Câble USB-B | 1 | USB-A vers USB-B | | | | |
| | **TOTAL PROJET** | | | | | | **€ HT** |

### 4.4 Calcul de la résistance de limitation DEL

Pour ne pas griller une DEL, il faut toujours calculer la résistance de limitation :

> **Formule :**
> ```
> R = (Vcc - V_DEL) / I_DEL
> ```
> Avec :
> - **Vcc** = tension d'alimentation = 5 V
> - **V_DEL** = tension de seuil de la DEL ≈ 2 V (rouge) / 2,1 V (jaune) / 2,2 V (verte)
> - **I_DEL** = courant nominal ≈ 20 mA = 0,02 A

**Exemple pour la DEL rouge :**
```
R = (5 - 2) / 0,02 = 3 / 0,02 = 150 Ω → on prend 220 Ω (valeur normalisée supérieure) ✅
```

**Calcule toi-même pour les DEL jaune et verte :**

| DEL | Vcc (V) | V_DEL (V) | I_DEL (A) | R calculée (Ω) | R choisie (Ω) |
|---|---|---|---|---|---|
| Rouge | 5 | 2,0 | 0,02 | | |
| Jaune | 5 | 2,1 | 0,02 | | |
| Verte | 5 | 2,2 | 0,02 | | |

---

## 5. Méthodologie de résolution de pannes

### 5.1 La méthode SVARC

Lorsqu'un système ne fonctionne pas, il existe une méthode structurée que tout technicien doit connaître :

```
[ILLUSTRATION 5]
Légende : Logigramme de la méthode SVARC représenté comme un organigramme à 5 étapes en cascade :
S = Symptôme (observer et décrire), V = Vérification (mesurer et tester),
A = Analyse (comparer attendu vs mesuré), R = Remède (apporter la correction),
C = Contrôle (vérifier que la correction a bien résolu le problème).
Chaque étape est une boîte colorée reliée par des flèches, avec une icône représentative.
PROMPT ILLUSTRATION : "Flowchart diagram showing 5-step SVARC troubleshooting method:
Step 1 (blue): S=Symptôme - magnifying glass icon - 'Observer et décrire le problème'.
Step 2 (orange): V=Vérification - multimeter icon - 'Mesurer et tester'.
Step 3 (yellow): A=Analyse - brain icon - 'Comparer attendu vs obtenu'.
Step 4 (red): R=Remède - wrench icon - 'Apporter la correction'.
Step 5 (green): C=Contrôle - checkmark icon - 'Vérifier la résolution'.
Connected by downward arrows, clean flat design, white background."
```

| Étape | Nom | Action concrète |
|---|---|---|
| **S** | **Symptôme** | Décrire précisément ce qui ne marche pas. *"La DEL jaune ne s'allume pas"* et non *"ça marche pas"* |
| **V** | **Vérification** | Mesurer les tensions, vérifier les connexions, tester en isolation |
| **A** | **Analyse** | Comparer ce qu'on mesure avec ce qu'on devrait mesurer |
| **R** | **Remède** | Apporter la correction identifiée |
| **C** | **Contrôle** | Retester le système complet après correction pour s'assurer que le problème est résolu ET qu'aucune nouvelle panne n'a été introduite |

### 5.2 Tableau des pannes fréquentes et leur diagnostic

| Symptôme observé | Cause probable | Vérification | Remède |
|---|---|---|---|
| Aucune communication BT possible | TX/RX inversés | Vérifier le câblage sur SoftwareSerial(rx, tx) | Inverser les broches dans le sketch ou le câblage |
| Caractères illisibles reçus | Baudrate différent entre HC-05 et sketch | En mode AT : `AT+UART?` puis vérifier `bluetooth.begin()` | Synchroniser les baudrates |
| DEL ne s'allume pas | Polarité DEL inversée | Mesurer la tension aux bornes de la DEL | Retourner la DEL |
| DEL ne s'allume pas | Mauvaise broche dans le sketch | `Serial.println(digitalRead(4))` après commande | Corriger le numéro de broche |
| DEL grillée / très chaude | Résistance de limitation absente ou trop faible | Vérifier la résistance en série avec la DEL | Ajouter/remplacer la résistance (220Ω minimum) |
| Module HC-05 ne répond pas aux AT | Pas en mode AT (EN/KEY non activé) | Vérifier que EN/KEY est bien à HIGH à la mise sous tension | Remettre EN/KEY à HIGH et redémarrer |
| La connexion BT s'établit puis se coupe | Alimentation insuffisante | Mesurer la tension VCC du HC-05 sous charge | Utiliser une alimentation plus stable ou condensateur de découplage |
| Le sketch ne se téléverse pas | Port COM occupé par moniteur série | Fermer le moniteur série avant de téléverser | Fermer moniteur série → téléverser → rouvrir |

---

## 6. Les outils du dépannage

### 6.1 Le multimètre

```
[ILLUSTRATION 6]
Légende : Schéma d'utilisation du multimètre en mode voltmètre pour mesurer la tension aux bornes
d'une DEL dans un circuit Arduino. La sonde rouge est sur l'anode, la sonde noire sur la cathode.
La valeur affichée est 2,0V (normal pour une DEL rouge allumée). Les points de mesure sont indiqués
par des croix rouges sur le schéma de câblage.
PROMPT ILLUSTRATION : "Technical diagram showing a digital multimeter in voltmeter mode connected
to measure voltage across an LED in an Arduino circuit. Red probe on LED anode, black probe on cathode.
Display shows 2.0V. Circuit shows Arduino pin → 220Ω resistor → LED → GND.
Measurement points marked with red X. Clean engineering illustration style, labeled in French."
```

| Mode | Mesure | Comment l'utiliser |
|---|---|---|
| **Voltmètre (V~~ ou V=)** | Tension | Sonde rouge sur + , sonde noire sur GND, mesure en **parallèle** |
| **Ohmmètre (Ω)** | Résistance | Circuit **hors tension**, mesure aux bornes de la résistance |
| **Continuité (🔊)** | Liaison électrique | Bip si connexion OK — utile pour vérifier un fil |
| **Ampèremètre (A)** | Courant | En **série** dans le circuit — rarement utilisé en dépannage |

> ⚠️ **Ne jamais mesurer une résistance dans un circuit sous tension** — risque de mesure fausse et de dommage au multimètre.

### 6.2 Le moniteur série comme outil de diagnostic

Le moniteur série de l'IDE Arduino est ton premier outil de diagnostic logiciel. Tu peux l'utiliser pour :

```cpp
// Ajouter des messages de debug dans ton sketch
Serial.print("Commande reçue : ");
Serial.println(commande);
Serial.print("État broche 4 : ");
Serial.println(digitalRead(4));   // Affiche 0 ou 1
Serial.print("Tension fictive : ");
Serial.println(analogRead(A0));   // Pour tester les entrées analogiques
```

---

## 7. Vocabulaire clé à maîtriser pour l'examen

| Terme | Définition |
|---|---|
| **Test d'intégration** | Test vérifiant le fonctionnement de plusieurs composants assemblés ensemble |
| **Protocole de tests** | Document décrivant les cas de tests, les actions, les résultats attendus et obtenus |
| **BOM (Bill of Materials)** | Liste exhaustive des composants d'un système avec références, quantités et coûts |
| **Schéma annoté** | Schéma électrique avec les valeurs, références et informations techniques complètes |
| **Cartouche** | Cadre de titre d'un schéma technique contenant les informations d'identification du document |
| **Symptôme** | Manifestation observable d'une panne (ce qu'on voit/entend/mesure) |
| **Cause** | Origine réelle du dysfonctionnement (ce qui provoque le symptôme) |
| **Méthode SVARC** | Méthode de diagnostic : Symptôme → Vérification → Analyse → Remède → Contrôle |
| **Résistance de limitation** | Résistance placée en série avec une DEL pour limiter le courant et protéger le composant |
| **Pont diviseur de tension** | Circuit de deux résistances en série permettant d'obtenir une tension intermédiaire |
| **Référence composant** | Identifiant unique d'un composant dans un schéma (R1, D1, U1, BT1…) |
| **Nomenclature** | Synonyme français de BOM — liste des matériaux et composants d'un projet |

---

> 📌 **Retiens l'essentiel en 4 points :**
> 1. Un test d'intégration ne remplace pas les tests unitaires — il vient **après**
> 2. La BOM est indispensable pour **commander** et **reproduire** un projet
> 3. En dépannage : **symptôme → hypothèse → mesure → remède → contrôle** — dans cet ordre !
> 4. Un schéma technique sans cartouche et sans valeurs n'est **pas exploitable** professionnellement

---

*Fiche Cours Élève — BAC PRO CIEL | Module E2 | S17*
*Compétences : C1.2 – C3.2 – C4.1 – C4.2*
