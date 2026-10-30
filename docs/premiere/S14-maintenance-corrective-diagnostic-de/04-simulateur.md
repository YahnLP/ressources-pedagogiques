# 🖥️ Exercices et TP sur le simulateur ElectroLab

> [!NOTE]
> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans ElectroLab, clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).

## Dépannage d'une alimentation 5 V (7 pannes)

*Bac Pro CIEL (terminale) · durée indicative : 2 h*

Une alimentation stabilisée 5 V / 110 mA (secteur → fusible → transformateur → pont → filtrage → régulateur 7805) ne fonctionne plus correctement. Le client décrit le symptôme. À vous de <b>localiser la panne</b>, de <b>proposer et réaliser le dépannage</b>, puis de <b>contrôler</b> le fonctionnement. La panne change à chaque « ↻ Autre panne ».

### 🎯 Objectifs

- Appliquer une démarche de dépannage structurée
- Mesurer en remontant la chaîne fonctionnelle (secteur → charge)
- Utiliser ohmmètre, testeur de diode, voltmètre et oscilloscope pour localiser le défaut
- Remplacer uniquement le composant défectueux et rechercher la cause
- Contrôler le résultat

### 🛠️ Marche à suivre

1. <b>Constat :</b> lisez le symptôme signalé (encadré jaune « Symptôme signalé » dans l’énoncé). Mesurez la tension de sortie sur RL.
2. <b>Hypothèses :</b> quels blocs peuvent expliquer ce symptôme ? Notez-les dans le carnet.
3. <b>Caméra thermique :</b> activez « 🌡 Thermographie » (barre du haut) : un composant anormalement chaud (court-circuit, surcharge, électrolytique qui chauffe) se repère tout de suite, comme à la caméra thermique en maintenance. Attention : un composant déjà détruit refroidit ensuite.
4. <b>Mesures :</b> avancez bloc par bloc : tension après F1, secondaire du transformateur (V∿), tension sur C1 (V⎓ + oscilloscope), entrée/sortie de U1. Les composants se testent hors tension à l'ohmmètre ou au testeur de diode.
5. <b>Localisation :</b> désignez le composant en cause dans la question ci-dessous.
6. <b>Réparation :</b> remplacez-le (inspecteur → « Remplacer le composant ») puis remettez sous tension. Pensez à chercher la <i>cause</i> de la panne (un fusible qui saute n'est jamais la cause ! Chaque remise sous tension sur un court-circuit échauffe le transformateur).
7. <b>Contrôle :</b> 5 V stables, ondulation faible, aucun échauffement anormal.

### ❓ Questions

1. Quelle est la tension de sortie constatée <b>avant</b> toute réparation ?  
    - ☐ 0 V  
    - ☐ ≈ 5 V mais avec une forte ondulation / un ronflement  
    - ☐ ≈ 15–17 V (tension trop élevée)  
    - ☐ 5 V stable (alimentation correcte)
2. Quel composant est défectueux ?
3. Nature de la panne  
    - ☐ Circuit ouvert / composant coupé  
    - ☐ Court-circuit  
    - ☐ Composant dégradé (dérive, vieillissement)
4. Décrivez votre démarche : mesures effectuées, conclusion, composant remplacé.

### 📥 Fichiers à ouvrir dans ElectroLab

- [`dep1-v1.json`](tp/dep1-v1.json) — Autre panne n° 1
- [`dep1-v2.json`](tp/dep1-v2.json) — Autre panne n° 2

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Dépannage d'une alimentation 5 V (7 pannes)*.

## Dépannage d'une platine transistor + LED (6 pannes)

*Bac Pro CIEL (première / terminale) · durée indicative : 1 h 30*

Une platine de signalisation commande une LED à l'aide d'un transistor : LED allumée quand l'interrupteur SW1 est fermé, éteinte quand il est ouvert. Elle ne fonctionne plus. Trouvez la panne par des mesures ($V_{BE}$, $V_{CE}$, tensions aux bornes de $R_{B}$ et $R_{C}$), réparez, puis contrôlez les deux états.

### 🎯 Objectifs

- Déduire un état du transistor (bloqué, saturé, court-circuité) des tensions mesurées
- Séparer commande ($R_{B}$, base) et puissance ($R_{C}$, LED, collecteur)
- Localiser un composant défectueux ou une connexion coupée
- Contrôler les deux états de fonctionnement après réparation

### 🛠️ Marche à suivre

1. <b>Constat</b> : testez SW1 ouvert / fermé et lisez le symptôme.
2. <b>Mesures</b> : $V_{BE}$ (≈ 0,7 V si la base est alimentée), $V_{CE}$ (≈ 0,1 V saturé, ≈ 5 V bloqué), tension sur $R_{B}$ et sur $R_{C}$.
3. <b>Localisation</b> : quelle partie est en cause, commande ou puissance ? Confirmez hors tension (ohmmètre, testeur de diode, continuité).
4. <b>Réparation</b> (remplacer le composant, ou rétablir la connexion avec un fil).
5. <b>Contrôle</b> : SW1 fermé → LED allumée ; SW1 ouvert → éteinte.

### ❓ Questions

1. Quel élément est défectueux ? (pour une connexion coupée, indiquer l'un des deux composants reliés)
2. Nature de la panne  
    - ☐ Composant ouvert / coupé  
    - ☐ Court-circuit  
    - ☐ Connexion coupée (fil, soudure)
3. Décrivez les mesures qui vous ont permis de conclure.

### 📥 Fichiers à ouvrir dans ElectroLab

- [`dep2-v1.json`](tp/dep2-v1.json) — Autre panne n° 1
- [`dep2-v2.json`](tp/dep2-v2.json) — Autre panne n° 2

> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *Dépannage d'une platine transistor + LED (6 pannes)*.
