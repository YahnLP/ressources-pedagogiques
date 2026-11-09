# 🧮 Utiliser LogicLab

> [!NOTE] 🧪 Voir aussi : [tous les Labs](labs.md) · [🖥️ ElectroLab](electrolab.md) pour câbler des circuits électroniques · [🔬 OscilloLab](oscillolab.md) pour régler les oscilloscopes.

**LogicLab** est un simulateur de **circuits logiques** qui fonctionne **hors ligne** dans un navigateur (un seul fichier HTML). On dessine un schéma avec des **symboles européens (CEI 60617-12)** et on voit en direct le **0 ou le 1** derrière chaque porte : fil vert épais pour 1, fil gris pour 0, fil orange pointillé pour « ? » (entrée en l'air ou conflit de sorties).

▶️ **Ouvrir le simulateur : [LogicLab — Simulateur de circuits logiques](https://yahnlp.github.io/LogicLab/)**

📥 Pour travailler hors ligne, le fichier unique `dist/logiclab.html` est disponible dans le [dépôt LogicLab](https://github.com/YahnLP/LogicLab).

## Ce qu'on y trouve

| Élément | Détail |
|---|---|
| **Portes** | NON, tampon, ET, OU, NON-ET, NON-OU, OU exclusif, NON-OU exclusif (2 à 8 entrées), **boîte noire** à fonction cachée |
| **Entrées** | interrupteur, bouton poussoir, niveaux 0 / 1 fixes, **horloge** (fréquence, rapport cyclique), **séquence binaire**, **générateur de combinaisons** (compteur 2 à 4 bits) |
| **Sorties** | LED, sonde logique, afficheur 7 segments, actionneur (moteur, pompe, lampe, sirène, électrovanne) |
| **Onglets d'analyse** | **Chronogramme** · **Table de vérité** (en direct) · **Équations** (lues sur le schéma, formes canoniques, forme simplifiée) · **Karnaugh** (remplissage, groupements corrigés) · **Concepteur** (table → équation → schéma) |

## Commencer

1. Ouvre le menu **TP ▾** et choisis une séance.
2. Lis le **sujet** et les **objectifs** dans le panneau de droite.
3. Dessine le schéma : outil **Fil** pour relier deux broches, **Pivoter** et **Supprimer** pour corriger.
4. Teste les combinaisons avec les interrupteurs, observe l'onglet **Table de vérité**, puis réponds aux questions : la validation est **automatique**.

> [!TIP] 🎓 TD ou TP ?
> Un **TD** est **guidé étape par étape** : *À comprendre*, *À faire*, coup de pouce, validation de chaque étape. Un **TP** ne donne que le **cahier des charges** : à toi de câbler, avec validation automatique du schéma et des réponses. Chaque TP renvoie vers le TD correspondant : **fais le TD si tu hésites**.

> [!WARNING] ⚠️ Comme dans un vrai montage
> Une **entrée laissée en l'air** donne un état **indéterminé** (« ? ») et deux **sorties reliées entre elles** créent un conflit. C'est l'erreur n° 1 sur une platine réelle (voir la semaine 9 de l'[Essentiel en 1 an](../essentiel-en-1-an/S09-semaine.md)).

## Quels TD / TP pour quelle séance ?

| Thème | TD / TP LogicLab | Séances |
|---|---|---|
| **Portes et tables de vérité** | TD *Découvrir les niveaux logiques et la porte ET* · TD *ET et OU* · TD *NON, NON-ET, NON-OU et OU exclusif* · TP *Premier circuit* · *ET contre OU* · *NON, NON-ET, NON-OU et OU exclusif* · *Porte inconnue* | Essentiel S9 · Première S12 |
| **Lire et écrire une équation** | TD / TP *Lire un schéma : table de vérité et équation* · TD / TP *Dessiner le schéma d'une équation* · *Que se passe-t-il derrière chaque porte ?* · TD *Σ, Π, mintermes et maxtermes* · *Formes canoniques d'un schéma* | Première S12 *(pour aller plus loin)* |
| **Dépanner une platine logique** | TP *Dépannage : trouver la porte défectueuse* · *Que se passe-t-il derrière chaque porte ?* | Essentiel S13 · Terminale S17 |
| **Algèbre de Boole et Karnaugh** | TD *Lois de De Morgan* · TD *Simplifier avec un tableau de Karnaugh (3 variables)* · TP *Tout avec des NON-ET* · *Simplifier un schéma* · *Karnaugh à 3 variables* · *Karnaugh à 4 variables* · *États indifférents : afficheur BCD* | Première S12 *(pour aller plus loin)* |
| **Concevoir un circuit** | TD *Méthode de conception : une alarme* · TP *Alarme d'une maison* · *Commande d'une pompe de cuve* · *Vote à la majorité* · *Va-et-vient* · *Demi-additionneur* · *Additionneur complet* | Première S12 *(pour aller plus loin)* |
| **Problèmes complets** | TD *Du cahier des charges au circuit* · *Portail automatique* · *Distributeur de boissons* · *Monte-charge sécurisé* · *Comparateur de deux nombres de 2 bits* | Terminale S17 *(entraînement)* |
| **Signaux et bascules** | TD *Signaux carrés : période, fréquence, rapport cyclique* · TP *Générateur de signaux* · *Deux horloges, trois portes* · *Détecter une combinaison avec un compteur* · TD *La bascule D* · *Diviseur par 2* · *Compteur asynchrone 2 bits* | Première S05 *(chronogrammes)* |

Le simulateur propose **12 TD** et **30 TP** (la plupart avec plusieurs variantes de tirage). Les durées indicatives vont de 30 min à 1 h 45.

> [!TIP] 🏁 Comment l'utiliser avec ElectroLab
> **LogicLab** pour **raisonner** (table de vérité, équation, simplification, chronogramme) ; **ElectroLab** pour **câbler la vraie platine** (alimentation, CMOS / TTL, LED, mesures). Réussis d'abord le TP virtuel, puis refais la manipulation sur le **matériel réel**.

## 📄 Droits

LogicLab est diffusé sous licence **EUPL 1.2** (voir le [dépôt LogicLab](https://github.com/YahnLP/LogicLab)). © 2026 Yahn LE PRETTRE.
