---
title: "E2 - Pack 05 - Fiche de cours élève - Analyse et diagnostic des pannes"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Analyse et diagnostic des pannes

## 🎯 Objectifs (niveau E2)
À la fin de cette fiche, je suis capable de :

| Je sais… | Exemple attendu en E2 |
|---|---|
| **Observer** un symptôme et le décrire | “La LED ne s’allume pas / le signal est bruité / ça chauffe.” |
| **Appliquer une méthode** de diagnostic | “Je fais : inspection → alim → continuité → composants → signaux.” |
| **Mesurer au bon endroit** avec le bon outil | “U_alimentation, test diode, continuité Vcc↔GND…” |
| **Conclure sans deviner** | “J’ai une preuve : mesure / test → donc panne localisée.” |
| **Proposer une réparation** et vérifier | “Je remplace / ressoude / corrige câblage, puis test final.” |

---

## 🔑 Idée essentielle avant de commencer
Diagnostiquer une panne, ce n’est pas “deviner”.  
En atelier, diagnostiquer = **observer → tester → conclure**.

➡️ Une bonne méthode :
- fait gagner du temps,
- évite d’abîmer le matériel (court-circuit, surchauffe),
- permet d’expliquer clairement ce qu’on a trouvé (attendu E2).

---

## I. Principes de l’analyse et du diagnostic des pannes

L’analyse et le diagnostic des pannes consistent à identifier et localiser les défauts ou dysfonctionnements dans un circuit électrique ou électronique. Ce processus repose sur une compréhension approfondie du circuit et sur l’utilisation d’outils et de méthodes structurées pour isoler la panne et en comprendre la cause.

### ● Compréhension du circuit
Avant de diagnostiquer une panne, il est essentiel de bien connaître le schéma du circuit, ses composants, et son fonctionnement attendu.

Le **fonctionnement attendu**, c’est : *ce qui devrait se passer quand tout va bien*.  
Exemples très concrets :
- “La LED doit s’allumer.”
- “La sortie doit basculer de 0 à 5V.”
- “Le capteur doit faire varier une tension.”
- “Le moteur doit tourner quand la commande est à 1.”

<p align="center">
  <img src="./images/diagnostic_schema_attendu.png" alt="Schéma simple annoté : où doit-on trouver 5V, où doit-on trouver 0V (GND)" width="90%"><br>
  <em>Illustration attendue : schéma simple annoté (où doit-on trouver 5V ? où doit-on trouver 0V ?).</em>
</p>

### ● Utilisation de la logique et de la déduction
Un diagnostic efficace passe par une analyse logique des symptômes observés, en vérifiant étape par étape chaque composant et chaque connexion.

Une logique simple et très efficace (souvent vraie) :
1) **alimentation** (ai-je bien la bonne tension ?)  
2) **connexions** (continuité, GND, court-circuit Vcc↔GND)  
3) **polarités** (LED, diode, condensateur polarisé)  
4) **composants** (valeur/état)  

L’idée est de tester **le plus probable et le plus simple en premier**.

### ● Méthode d’élimination
Éliminer les causes potentielles les unes après les autres, en commençant par les vérifications les plus simples et les plus accessibles.

C’est comme une enquête :  
- j’émets une hypothèse (“alim absente”, “faux contact”…),  
- je fais un test,  
- si le test prouve que ce n’est pas ça, j’élimine et je passe à la suite.

### ● Utilisation d’outils de mesure
Multimètres, oscilloscopes, et autres outils permettent de tester les composants et les points clés du circuit pour détecter les anomalies.

- **Multimètre** : tension, continuité, résistance, **test diode**.
- **Oscilloscope** : “voir” un signal qui bouge dans le temps (forme, bruit, fréquence).

---

## II. Les symptômes de pannes courantes dans les circuits

Les pannes peuvent se manifester de plusieurs façons. Certains signes orientent immédiatement vers des causes probables.

### ● Absence de fonctionnement
Le circuit ne s’allume pas ou ne réagit pas.  
Causes possibles : coupure d’alimentation, fusible grillé, court-circuit, composant défectueux.

Premier réflexe : **U_alimentation**  
➡️ “Ai-je bien 5V ? 3,3V ? 12V ?”  
Ensuite : continuité **Vcc → entrée circuit** et **GND → retour** (car un GND manquant = circuit qui ne se ferme pas).

### ● Comportement anormal ou intermittent
Le circuit fonctionne de façon instable ou intermittente.  
Causes possibles : soudures froides, connexions lâches, défauts dans les câbles, condensateur défectueux.

À retenir : “intermittent” = très souvent un **faux contact** (fil, soudure, connecteur).  
Une soudure froide peut fonctionner “un jour sur deux” : dès qu’on bouge, la panne apparaît.

### ● Échauffement excessif
Un composant chauffe anormalement.  
Causes possibles : court-circuit, résistance trop faible, surcharge de courant, dissipation thermique insuffisante.

Réflexe sécurité : si ça chauffe, **on coupe** et on cherche la cause.  
Un courant trop fort = danger (panne + casse). Il ne faut pas “laisser pour voir”.

### ● Bruits ou parasites
Sons anormaux ou perturbations dans les signaux, particulièrement en audio ou en RF.  
Causes possibles : interférences électromagnétiques, composants mal blindés, alimentation instable.

Un oscilloscope permet de vérifier si le signal est “sale” (bruit, distorsion).

<p align="center">
  <img src="./images/signal_propre_vs_bruit.png" alt="À l'oscilloscope : signal propre comparé à un signal bruité (parasites)" width="90%"><br>
  <em>Illustration attendue : deux oscillogrammes : (1) signal propre, (2) signal avec bruit/parasites.</em>
</p>

---

## III. Les étapes du diagnostic de pannes dans les circuits électroniques

Le processus de diagnostic suit des étapes structurées qui permettent de localiser la panne de manière méthodique.

### ✅ La méthode “pro” (à appliquer dans cet ordre)
| Étape | Ce que je cherche | Pourquoi c’est efficace |
|---|---|---|
| 1. Inspection visuelle | erreur évidente (sens, fil, pont) | rapide, sans risque |
| 2. Alimentation | U correcte et stable + GND présent | panne fréquente |
| 3. Continuité | coupure / court-circuit | preuve simple |
| 4. Composants | valeur / état / test diode | cible précise |
| 5. Signaux | signal absent / déformé / bruité | utile sur circuits complexes |

### ● Étape 1 : Inspection visuelle
Vérifier l’état physique des composants (déformations, traces de brûlure, soudures), les connexions, et la propreté de la carte.  
Exemple : une résistance noircie ou un condensateur bombé indiquent souvent une surchauffe ou une panne.

On cherche notamment :
- composant inversé (LED, diode, condensateur polarisé),
- fil manquant,
- pont de soudure,
- patte cassée / piste arrachée.

### ● Étape 2 : Vérification de l’alimentation
Mesurer la tension de l’alimentation pour s’assurer qu’elle est stable et correspond aux spécifications du circuit.  
Exemple : si un circuit digital reçoit une alimentation en dessous de 5V au lieu de 5V, il peut ne pas fonctionner correctement.

Très important : vérifier aussi la présence de **GND** (le retour).  
Sans GND, la boucle n’est pas fermée → le circuit peut rester “mort”.

### ● Étape 3 : Test de continuité
Utiliser le multimètre pour tester la continuité des pistes et des connexions, afin de repérer les ruptures ou les court-circuits.  
Exemple : en cas de panne totale, vérifier que la continuité est assurée depuis la source d’alimentation jusqu’aux points clés du circuit.

Deux vérifications très utiles :
- continuité **Vcc → entrée circuit**, puis **GND → retour**,
- recherche d’un court-circuit **Vcc ↔ GND** (danger).

### ● Étape 4 : Test des composants individuels
Mesurer la résistance, la tension et le courant aux bornes de chaque composant pour vérifier leur comportement par rapport aux spécifications.  
Exemple : tester un transistor pour vérifier qu’il fonctionne en tant qu’interrupteur en mesurant la tension entre la base et l’émetteur.

Rappels pratiques :
- résistance : mesure en **Ω** (hors tension),
- diode/LED : mode **test diode** (doit conduire dans un sens).

### ● Étape 5 : Vérification des signaux avec un oscilloscope
Pour des circuits plus complexes, l’oscilloscope permet d’observer la forme d’onde et la fréquence des signaux, ce qui aide à détecter les anomalies.  
Exemple : dans un circuit audio, vérifier la forme d’onde en sortie d’un amplificateur pour détecter les distorsions.

Réglages essentiels :
- **Volts/div** et **Temps/div**.

Lecture rapide :
- “signal absent” = panne en amont,
- “signal déformé” = composant / alim / bruit / saturation.

---

## IV. Les pannes courantes et leur identification

### ● Court-circuits
Un court-circuit se produit lorsqu’un chemin non souhaité se crée entre deux points du circuit, souvent à cause d’une soudure mal réalisée ou d’un composant défectueux.  
Méthode de diagnostic : utiliser un multimètre en mode « test de continuité » pour localiser la connexion indésirable.

Court-circuit typique : **Vcc ↔ GND** (danger).  
➡️ On coupe l’alimentation avant de chercher.

### ● Panne d’un composant spécifique

#### ○ Résistances
Si une résistance est endommagée, elle peut perdre sa valeur nominale.  
Méthode de diagnostic : mesurer la résistance et la comparer à sa valeur indiquée.

Attention : si tu mesures une résistance “dans un circuit”, la valeur peut être fausse car le reste du circuit influence la mesure.

#### ○ Condensateurs
Ils peuvent fuir, perdre leur capacité, ou se court-circuiter.  
Méthode de diagnostic : tester le condensateur avec un capacimètre, ou vérifier l’absence de court-circuit avec un multimètre.

Un condensateur polarisé inversé peut s’abîmer : c’est une cause classique de panne après montage.

#### ○ Transistors
Les transistors défectueux peuvent cesser de conduire ou conduire en permanence.  
Méthode de diagnostic : tester les jonctions entre base-émetteur et base-collecteur avec un multimètre.

#### ○ Diodes
Une diode défectueuse peut perdre sa propriété de conduction unidirectionnelle.  
Méthode de diagnostic : tester la diode dans les deux sens de polarisation pour vérifier qu’elle conduit dans un seul sens.

Test diode attendu :
- un sens “OK”,
- l’autre “bloqué”.

---

## V. Les outils et instruments de diagnostic

| Outil | À quoi il sert | Ce que je peux conclure |
|---|---|---|
| Multimètre | U / Ω / continuité / test diode | alim OK ? coupure ? court-circuit ? diode HS ? |
| Oscilloscope | voir un signal dans le temps | signal absent ? bruité ? déformé ? |
| Capacimètre | capacité des condensateurs | condensateur conforme ou dégradé |
| Générateur de signal | injecter un signal | localiser l’étage où le signal disparaît |

Injecter un signal et suivre sa trace à l’oscilloscope est très efficace pour localiser “où ça s’arrête”.

---

## VI. Diagnostic de pannes spécifiques aux circuits numériques et analogiques

### ● Circuits numériques
Les circuits numériques utilisent des niveaux de tension discrets pour représenter des valeurs logiques.  
Exemple de panne : si une sortie reste bloquée sur un état haut ou bas, cela peut indiquer un composant logique (porte, compteur) défectueux.  
Diagnostic : vérifier les niveaux logiques et les changements d’état des signaux avec un oscilloscope ou un analyseur logique.

En pratique, on attend souvent des niveaux proches de :
- 0V (état bas),
- 5V (état haut), selon le circuit.

Une sortie “bloquée” peut aussi venir :
- d’un court-circuit,
- d’une entrée mal câblée,
- d’un composant HS.

### ● Circuits analogiques
Les circuits analogiques manipulent des signaux continus qui varient en fonction du temps.  
Exemple de panne : une distorsion dans un amplificateur audio peut indiquer une panne dans un condensateur de couplage ou un transistor.  
Diagnostic : utiliser l’oscilloscope pour vérifier la linéarité du signal et localiser la source de la distorsion.

À retenir : “distorsion” = signal déformé, souvent lié à :
- alim instable,
- composant dégradé,
- saturation (signal trop fort).

---

## VII. Les stratégies de réparation après le diagnostic

Une fois la panne identifiée, il est essentiel d’appliquer les bonnes techniques de réparation pour rétablir le bon fonctionnement du circuit.

- **Remplacement de composants défectueux** : dessouder le composant défaillant, vérifier la polarité et les valeurs avant d’installer le nouveau.
- **Reprise des soudures froides ou mauvaises** : refaire les soudures incorrectes ou endommagées, en s’assurant que la nouvelle soudure est propre et solide.
- **Vérification des connexions et des pistes** : après la réparation, s’assurer que les connexions sont correctes, que les pistes ne sont pas coupées ou en court-circuit.
- **Test final du circuit** : alimenter progressivement le circuit et surveiller les paramètres électriques (tension, courant) pour s’assurer que la panne a été résolue et qu’aucun autre problème ne persiste.

En fin de réparation, on refait la checklist :
**alim → continuité → polarités → fonctionnement**.

---

## VIII. Applications pratiques de l’analyse et du diagnostic de pannes

- **Dépannage d’une alimentation** : vérifier la tension de sortie, inspecter les diodes de redressement et les régulateurs, puis tester les condensateurs de filtrage.
- **Réparation d’un amplificateur audio** : en cas de distorsion, vérifier les transistors de puissance, les condensateurs de couplage, et les résistances pour détecter toute anomalie dans le signal.
- **Maintenance de circuits de commande** : dans les circuits de commande (par exemple, relais ou contacteurs), tester chaque interrupteur, bobine, et protection pour vérifier que chaque étape de commande est correctement réalisée.

---

# Tableau méthode (à apprendre pour E2)

| Étape | Je fais quoi ? | Outil | Exemple de conclusion |
|---|---|---|---|
| 1 Inspection | je cherche un défaut visible | yeux | “fil manquant / composant noirci” |
| 2 Alim | je mesure U et stabilité | multimètre | “alimentation trop basse” |
| 3 Continuité | je cherche coupure / court-circuit | multimètre | “Vcc↔GND en court-circuit” |
| 4 Composants | je teste R/diode/transistor… | multimètre/capacimètre | “diode conduit dans 2 sens → HS” |
| 5 Signaux | je vois forme/amplitude/fréquence | oscilloscope | “signal absent après l’étage 2” |
