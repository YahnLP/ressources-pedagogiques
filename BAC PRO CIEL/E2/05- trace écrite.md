---
title: "E2 - Pack 05 - Fiche de cours élève - Analyse et diagnostic des pannes"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Analyse et diagnostic des pannes

## I. Principes de l’analyse et du diagnostic des pannes

L’analyse et le diagnostic des pannes consistent à identifier et localiser les défauts ou dysfonctionnements dans un circuit électrique ou électronique. Ce processus repose sur une compréhension approfondie du circuit et sur l’utilisation d’outils et de méthodes structurées pour isoler la panne et en comprendre la cause.

✅ Complément utile :
- En atelier, diagnostiquer = **observer → tester → conclure**, sans “deviner”.
- Une bonne méthode évite d’abîmer le matériel (court-circuit, surchauffe).

● Compréhension du circuit : avant de diagnostiquer une panne, il est essentiel de bien connaître le schéma du circuit, ses composants, et son fonctionnement attendu.

✅ Complément utile :
- “Fonctionnement attendu” = ce qui devrait se passer quand tout va bien.
- Exemple : “LED doit s’allumer” / “sortie doit basculer de 0 à 5V”.

<p align="center">
  <img src="./images/diagnostic_schema_attendu.png" alt="Schéma + fonctionnement attendu" width="90%"><br>
  <em>Illustration attendue : schéma simple annoté (où doit-on trouver 5V ? où doit-on trouver 0V ?).</em>
</p>

● Utilisation de la logique et de la déduction : un diagnostic efficace passe par une analyse logique des symptômes observés, en vérifiant étape par étape chaque composant et chaque connexion.

✅ Complément utile :
- “Logique” = je teste ce qui est le plus probable et le plus simple en premier.
- On vérifie souvent : alimentation → connexions → polarités → composants.

● Méthode d’élimination : éliminer les causes potentielles les unes après les autres, en commençant par les vérifications les plus simples et les plus accessibles.

✅ Complément utile :
- C’est comme une enquête : je supprime des hypothèses avec des preuves (mesures).

● Utilisation d’outils de mesure : multimètres, oscilloscopes, et autres outils permettent de tester les composants et les points clés du circuit pour détecter les anomalies.

✅ Complément utile :
- Multimètre = tension, continuité, résistance, test diode
- Oscilloscope = “voir” un signal qui bouge dans le temps (forme, bruit, fréquence)

---

## II. Les symptômes de pannes courantes dans les circuits

Les pannes peuvent se manifester de plusieurs façons, et certains signes permettent de guider le diagnostic vers des causes probables.

● Absence de fonctionnement : le circuit ne s’allume pas ou ne réagit pas.  
○ Causes possibles : coupure d’alimentation, fusible grillé, court-circuit, composant défectueux.

✅ Complément utile :
- Premier réflexe : **U_alimentation** (ai-je bien 5V ?).
- Puis : continuité Vcc→circuit et GND→retour.

● Comportement anormal ou intermittent : le circuit fonctionne de façon instable ou intermittente.  
○ Causes possibles : soudures froides, connexions lâches, défauts dans les câbles, condensateur défectueux.

✅ Complément utile :
- “Intermittent” = très souvent un **faux contact** (fil, soudure, connecteur).
- Une soudure froide peut marcher “un jour sur deux”.

● Échauffement excessif : un composant chauffe anormalement.  
○ Causes possibles : court-circuit, résistance trop faible, surcharge de courant, dissipation thermique insuffisante.

✅ Complément utile :
- Si ça chauffe : **on coupe** et on cherche la cause.
- Un courant trop fort = danger (panne + casse).

● Bruits ou parasites : sons anormaux ou perturbations dans les signaux, particulièrement en audio ou en RF.  
○ Causes possibles : interférences électromagnétiques, composants mal blindés, alimentation instable.

✅ Complément utile :
- Un oscilloscope permet de voir si le signal est “sale” (bruit, distorsion).

<p align="center">
  <img src="./images/signal_propre_vs_bruit.png" alt="Signal propre vs bruité à l'oscilloscope" width="90%"><br>
  <em>Illustration attendue : deux oscillogrammes : (1) signal propre, (2) signal avec bruit/parasites.</em>
</p>

---

## III. Les étapes du diagnostic de pannes dans les circuits électroniques

Le processus de diagnostic suit des étapes structurées qui permettent de localiser la panne de manière méthodique.

● Étape 1 : Inspection visuelle  
○ Vérifier l’état physique des composants (déformations, traces de brûlure, soudures), les connexions, et la propreté de la carte.  
○ Exemple : une résistance noircie ou un condensateur bombé indiquent souvent une surchauffe ou une panne.

✅ Complément utile :
- On cherche : composant inversé, fil manquant, pont de soudure, patte cassée.

● Étape 2 : Vérification de l’alimentation  
○ Mesurer la tension de l’alimentation pour s’assurer qu’elle est stable et correspond aux spécifications du circuit.  
○ Exemple : si un circuit digital reçoit une alimentation en dessous de 5V au lieu de 5V, il peut ne pas fonctionner correctement.

✅ Complément utile :
- Vérifier aussi la présence de **GND** (le retour !).

● Étape 3 : Test de continuité  
○ Utiliser le multimètre pour tester la continuité des pistes et des connexions, afin de repérer les ruptures ou les court-circuits.  
○ Exemple : en cas de panne totale, vérifier que la continuité est assurée depuis la source d’alimentation jusqu’aux points clés du circuit.

✅ Complément utile :
- Continuité Vcc→entrée circuit, puis GND→retour.
- Chercher aussi un court-circuit Vcc↔GND.

● Étape 4 : Test des composants individuels  
○ Mesurer la résistance, la tension et le courant aux bornes de chaque composant pour vérifier leur comportement par rapport aux spécifications.  
○ Exemple : tester un transistor pour vérifier qu’il fonctionne en tant qu’interrupteur en mesurant la tension entre la base et l’émetteur.

✅ Complément utile :
- Résistance : Ω (hors tension)
- Diode/LED : mode “test diode” (doit conduire dans un sens)

● Étape 5 : Vérification des signaux avec un oscilloscope  
○ Pour des circuits plus complexes, l’oscilloscope permet d’observer la forme d’onde et la fréquence des signaux, ce qui aide à détecter les anomalies.  
○ Exemple : dans un circuit audio, vérifier la forme d’onde en sortie d’un amplificateur pour détecter les distorsions.

✅ Complément utile :
- Réglages essentiels : Volts/div et Temps/div.
- “Signal absent” = panne en amont ; “signal déformé” = composant/alim/bruit.

---

## IV. Les pannes courantes et leur identification

● Court-circuits : un court-circuit se produit lorsqu’un chemin non souhaité se crée entre deux points du circuit, souvent à cause d’une soudure mal réalisée ou d’un composant défectueux.  
○ Méthode de diagnostic : utiliser un multimètre en mode « test de continuité » pour localiser la connexion indésirable.

✅ Complément utile :
- Court-circuit typique : Vcc ↔ GND (danger).
- On coupe l’alimentation avant de chercher.

● Panne d’un composant spécifique :  
○ Résistances : si une résistance est endommagée, elle peut perdre sa valeur nominale.  
■ Méthode de diagnostic : mesurer la résistance et la comparer à sa valeur indiquée.

✅ Complément utile :
- Si la valeur est très différente : composant HS ou mesure faite dans un circuit qui influence.

○ Condensateurs : ils peuvent fuir, perdre leur capacité, ou se court-circuiter.  
■ Méthode de diagnostic : tester le condensateur avec un capacimètre, ou vérifier l’absence de court-circuit avec un multimètre.

✅ Complément utile :
- Un condensateur polarisé inversé peut s’abîmer.

○ Transistors : les transistors défectueux peuvent cesser de conduire ou conduire en permanence.  
■ Méthode de diagnostic : tester les jonctions entre base-émetteur et base-collecteur avec un multimètre.

○ Diodes : une diode défectueuse peut perdre sa propriété de conduction unidirectionnelle.  
■ Méthode de diagnostic : tester la diode dans les deux sens de polarisation pour vérifier qu’elle conduit dans un seul sens.

✅ Complément utile :
- Test diode : un sens “OK”, l’autre “bloqué”.

---

## V. Les outils et instruments de diagnostic

● Multimètre : outil de base pour mesurer les valeurs de tension, de courant et de résistance. Il permet de détecter les composants défectueux et de vérifier les connexions.

✅ Complément utile :
- Mode continuité + test diode = très utiles en diagnostic.

● Oscilloscope : utilisé pour visualiser les signaux variables en fonction du temps, il aide à identifier les problèmes de fréquence, de forme d’onde, et de stabilité.

● Capacimètre : mesure la capacité des condensateurs pour vérifier qu’ils conservent leur valeur nominale.

● Générateur de signal : permet d’injecter des signaux spécifiques dans le circuit pour tester sa réponse et détecter d’éventuelles dégradations ou pertes de signal.

✅ Complément utile :
- Injecter un signal et suivre sa trace à l’oscilloscope aide à localiser l’étage en panne.

---

## VI. Diagnostic de pannes spécifiques aux circuits numériques et analogiques

● Circuits numériques :  
○ Les circuits numériques utilisent des niveaux de tension discrets pour représenter des valeurs logiques.  
○ Exemple de panne : si une sortie reste bloquée sur un état haut ou bas, cela peut indiquer un composant logique (porte, compteur) défectueux.  
○ Diagnostic : vérifier les niveaux logiques et les changements d’état des signaux avec un oscilloscope ou un analyseur logique.

✅ Complément utile :
- On attend des niveaux proches de 0V ou 5V (selon le circuit).
- Une sortie “bloquée” peut venir d’un court-circuit, d’une entrée mal câblée ou d’un composant HS.

● Circuits analogiques :  
○ Les circuits analogiques manipulent des signaux continus qui varient en fonction du temps.  
○ Exemple de panne : une distorsion dans un amplificateur audio peut indiquer une panne dans un condensateur de couplage ou un transistor.  
○ Diagnostic : utiliser l’oscilloscope pour vérifier la linéarité du signal et localiser la source de la distorsion.

✅ Complément utile :
- “Distorsion” = signal déformé : souvent lié à alim, composant, saturation.

---

## VII. Les stratégies de réparation après le diagnostic

Une fois la panne identifiée, il est essentiel d’appliquer les bonnes techniques de réparation pour rétablir le bon fonctionnement du circuit.

● Remplacement de composants défectueux : dessouder le composant défaillant, vérifier la polarité et les valeurs avant d’installer le nouveau.

● Reprise des soudures froides ou mauvaises : refaire les soudures incorrectes ou endommagées, en s’assurant que la nouvelle soudure est propre et solide.

● Vérification des connexions et des pistes : après la réparation, s’assurer que les connexions sont correctes, que les pistes ne sont pas coupées ou en court-circuit.

● Test final du circuit : alimenter progressivement le circuit et surveiller les paramètres électriques (tension, courant) pour s’assurer que la panne a été résolue et qu’aucun autre problème ne persiste.

✅ Complément utile :
- Test final = on refait la checklist : alim, continuité, polarités, fonctionnement.

---

## VIII. Applications pratiques de l’analyse et du diagnostic de pannes

Dépannage d’une alimentation : en cas de panne, vérifier la tension de sortie, inspecter les diodes de redressement et les régulateurs, puis tester les condensateurs de filtrage.

Réparation d’un amplificateur audio : en cas de distorsion, vérifier les transistors de puissance, les condensateurs de couplage, et les résistances pour détecter toute anomalie dans le signal.

Maintenance de circuits de commande : dans les circuits de commande (par exemple, relais ou contacteurs), tester chaque interrupteur, bobine, et protection pour vérifier que chaque étape de commande est correctement réalisée.

---

# Tableau méthode (à apprendre pour E2)
| Étape | Je fais quoi ? | Outil | Exemple de conclusion |
|---|---|---|---|
| 1 Inspection | je cherche un défaut visible | yeux | “fil manquant / composant noirci” |
| 2 Alim | je mesure U et stabilité | multimètre | “alimentation trop basse” |
| 3 Continuité | je cherche coupure / court-circuit | multimètre | “Vcc↔GND en court-circuit” |
| 4 Composants | je teste R/diode/transistor… | multimètre/capacimètre | “diode conduit dans 2 sens → HS” |
| 5 Signaux | je vois forme/amplitude/fréquence | oscilloscope | “signal absent après l’étage 2” |
