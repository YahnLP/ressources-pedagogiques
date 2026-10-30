"""Génère le parcours « L'essentiel en 1 an » (Terminale) : 10 semaines de 4 h.
Usage : python3 essentiel.py <racine>"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from essentiel_cours import COURS
from essentiel_ateliers import ATELIER, EXOS

S = '../seconde/'
P = '../premiere/'
T = '../terminale/'

def L(titre, chemin): return f'[{titre}]({chemin})'

SEMAINES = [
 dict(n=1, titre="Les composants et les lois de base", comp="C07",
  obj=["Reconnaître les composants courants (résistance, condensateur, diode/LED, transistor, régulateur, circuit intégré).",
       "Appliquer la loi d'Ohm et calculer une puissance.", "Lire le code couleurs d'une résistance.", "Calculer la résistance en série d'une LED."],
  deroule=[("1 h","Découvrir les familles de composants et leurs symboles"),("1 h","Loi d'Ohm, puissance, code couleurs : exercices"),("1 h","LED : calcul de la résistance, câblage sur plaque d'essai"),("1 h","Auto-test et correction")],
  liens=[L("Seconde S01 – code couleurs et loi d'Ohm", S+"S01-code-couleurs-des-resistances-et-loi-d/01-cours.md"), L("Seconde S01 – familles de composants", S+"S01-code-couleurs-des-resistances-et-loi-d/02-familles-de-composants.md"), L("Seconde S02 – diodes et LED", S+"S02-diodes-led-circuits-serie-parallele-loi/01-cours.md")],
  tests=[("Une résistance marron – noir – orange – or vaut combien ?","**10 kΩ**, tolérance ± 5 %."),("Quel courant dans une résistance de 330 Ω sous 5 V ?","$I = \\dfrac{5}{330} \\approx 15{,}2\\,\\mathrm{mA}$."),("Quelle résistance en série avec une LED (2 V, 20 mA) sous 5 V ?","$R = \\dfrac{5 - 2}{0{,}020} = 150\\,\\Omega$."),("Quelle patte d'une LED est l'anode (+) ?","La **patte longue**."),("Quelle puissance dissipe une résistance traversée par 100 mA sous 5 V ?","$P = 5 \\times 0{,}1 = 0{,}5\\,\\mathrm{W}$.")],
  livrable="Fiche « mes composants » : symbole, rôle et une valeur typique pour 8 composants."),
 dict(n=2, titre="Mesurer : multimètre, alimentation, générateur et oscilloscope", comp="C07 · C11",
  obj=["Mesurer une tension, un courant, une résistance, une continuité.", "Régler une alimentation de labo (tension et limite de courant).", "Régler un générateur de fonctions (forme, fréquence, amplitude).", "Régler un oscilloscope (VOLT/DIV, SEC/DIV, déclenchement) et lire amplitude, période, fréquence.", "Choisir le bon instrument selon la grandeur."],
  deroule=[("1 h","Multimètre : tension, courant, résistance, continuité"),("1 h","Alimentation de labo et générateur de fonctions"),("1 h","Oscilloscope : signal de test, sonde ×10, PWM, LED qui clignote"),("1 h","Atelier chronométré et auto-test (passeport instruments)")],
  liens=[L("Seconde S12 – tests au multimètre", S+"S12-tests-au-multimetre-et-controle-qualite/01-cours.md"), L("Seconde S12 – prise en main de l'oscilloscope", S+"S12-tests-au-multimetre-et-controle-qualite/05-prise-en-main-oscilloscope.md"), L("Seconde S12 – alimentation de labo et générateur", S+"S12-tests-au-multimetre-et-controle-qualite/06-alimentation-labo-et-generateur.md"), L("Première S05 – TP instruments avancés", P+"S05-tests-mesures-avances-oscilloscope/05-tp-instruments-avances.md"), L("Terminale S01 – circuit fourni", T+"S01-circuit-fourni-multimetre-oscilloscope/README.md"), L("Passeport instruments", "passeport-instruments.md")],
  tests=[("Comment branche-t-on un ampèremètre ? Un voltmètre ?","L'ampèremètre en **série**, le voltmètre en **parallèle**."),("Une période occupe 4 carreaux à 5 ms/DIV. Quelle fréquence ?","$T = 20\\,\\mathrm{ms}$ ; $f = 50\\,\\mathrm{Hz}$."),("Dans quelles conditions mesure-t-on une résistance ?","**Hors tension** et, si possible, **hors circuit**."),("Que fait le couplage AC ?","Il supprime la **composante continue** pour voir la variation."),("Que vérifier avant de brancher la sonde ?","Qu'elle est déclarée en **×10** et que la masse est sur la **masse du circuit**."),("Que règle-t-on sur une alimentation de labo avant de brancher le montage ?","La **tension** et la **limite de courant**."),("Le voyant CC est allumé : que signifie-t-il ?","Le courant a atteint la **limite** : il y a une **anomalie** (court-circuit, consommation trop forte).")],
  livrable="Relevé de 5 mesures (valeur, unité, instrument, réglage utilisé)."),
 dict(n=3, titre="Lire un schéma et une datasheet", comp="C07",
  obj=["Lire un schéma normalisé et repérer les blocs fonctionnels.", "Trouver dans une datasheet : brochage, limites absolues, caractéristiques min / typ / max.", "Calculer les composants autour d'un circuit à partir de la datasheet."],
  deroule=[("1 h","Symboles normalisés et lecture d'un schéma"),("1 h","Anatomie d'une datasheet (7805)"),("1 h","Datasheet du BC547 et du NE555 : exercices"),("1 h","Auto-test et correction")],
  liens=[L("Seconde S03 – schémas normalisés", S+"S03-breadboard-schemas-electriques-normes/01-cours.md"), L("Seconde S06 – lecture de datasheet", S+"S06-schemas-electriques-normes-tinkercad/01-cours.md"), L("Première S01 – lire une datasheet", P+"S01-interface-bibliotheques-schemas/03-lire-une-datasheet.md")],
  tests=[("Que signifie « absolute maximum ratings » ?","Les limites à **ne jamais dépasser** : au-delà, le composant peut être détruit."),("Pour un calcul de sécurité, quelle colonne utilise-t-on : min, typ ou max ?","Le **cas le plus défavorable** (min ou max selon le calcul), pas le typique."),("Quelle est la tension d'entrée maximale d'un 7805 ?","**35 V**."),("Quelle formule donne la fréquence d'un NE555 en astable ?","$f = \\dfrac{1{,}44}{(R_a + 2R_b) \\times C}$."),("À quoi sert la section « pin configuration » ?","À **câbler sans erreur** (numéro et nom des broches).")],
  livrable="Fiche synthèse d'une datasheet au choix (brochage, limites, valeurs utiles)."),
 dict(n=4, titre="L'alimentation : bilan de puissance et thermique", comp="C07 · C11",
  obj=["Faire un bilan de puissance (courant de pointe et courant moyen).", "Calculer la puissance dissipée par un régulateur linéaire et sa température de jonction.", "Estimer l'autonomie d'une batterie."],
  deroule=[("1 h","Bilan de puissance : tableau et marge de 25 %"),("1 h","Régulateur linéaire : $P_{diss}$ et rendement"),("1 h","Température de jonction, radiateur, autonomie"),("1 h","Auto-test et correction")],
  liens=[L("Terminale S03 – dimensionnement d'alimentation", T+"S03-dimensionnement-d-alimentation-bilan-de/01-cours.md")],
  tests=[("Pic de 400 mA : quelle source minimale avec 25 % de marge ?","$400 \\times 1{,}25 = 500\\,\\mathrm{mA}$."),("Un 7805 passe de 9 V à 5 V pour 300 mA. Quelle puissance dissipe-t-il ?","$(9 - 5) \\times 0{,}3 = 1{,}2\\,\\mathrm{W}$."),("Avec $R_{\\theta ja} = 65\\,°\\mathrm{C/W}$ et 25 °C ambiants, quelle est $T_j$ ?","$25 + 1{,}2 \\times 65 = 103\\,°\\mathrm{C}$ : radiateur recommandé."),("Batterie 1000 mAh, 50 mA : autonomie réelle ?","$\\dfrac{1000}{50} \\times 0{,}8 = 16\\,\\mathrm{h}$."),("Pourquoi un régulateur linéaire chauffe-t-il ?","Il **dissipe en chaleur** la différence $V_{in} - V_{out}$.")],
  livrable="Bilan de puissance complet d'un petit montage (tableau + conclusion sur le régulateur)."),
 dict(n=5, titre="Du cahier des charges au schéma (CAO)", comp="C07",
  obj=["Saisir un schéma dans KiCad (bibliothèques, alimentation, PWR_FLAG).", "Annoter, renseigner les valeurs, lancer et corriger l'ERC.", "Associer une empreinte à chaque composant."],
  deroule=[("1 h","Prise en main de KiCad : projet, bibliothèques"),("2 h","Saisie d'un schéma LED + transistor, puis NE555 ; ERC à 0 erreur"),("1 h","Empreintes et auto-test")],
  liens=[L("Première S01 – interface et premiers schémas", P+"S01-interface-bibliotheques-schemas/01-cours.md"), L("Première S02 – saisie de schéma", P+"S02-kicad-saisie-de-schema-bibliotheques/01-cours.md"), L("Terminale S06 – flux KiCad complet", T+"S06-flux-kicad-complet-schema-erc-pcb-drc/01-cours.md")],
  tests=[("À quoi sert un PWR_FLAG ?","À indiquer à KiCad qu'un rail d'alimentation est **bien alimenté** (évite l'erreur « power pin not driven »)."),("Que contrôle l'ERC ? Le DRC ?","L'ERC contrôle les **règles électriques du schéma** ; le DRC les **règles géométriques du PCB**."),("Que se passe-t-il si une empreinte est mal choisie ?","Le composant **ne rentre pas** sur la carte fabriquée."),("Comment lever une erreur « pin not connected » voulue ?","Poser un **No Connect** (touche Q)."),("Pourquoi corriger l'ERC avant le PCB ?","Une erreur de schéma se répercute sur **tout le PCB**.")],
  livrable="Schéma complet NE555 + LED, ERC à 0 erreur, empreintes associées."),
 dict(n=6, titre="Du PCB aux fichiers de fabrication (Gerber)", comp="C07",
  obj=["Placer et router un PCB selon des règles (clearance, largeurs).", "Passer le DRC, exporter les Gerber, le perçage et la BOM.", "Contrôler une brasure selon IPC-A-610."],
  deroule=[("1 h","Contour, règles de conception, placement"),("1 h","Routage (alimentation d'abord) et DRC"),("1 h","Gerber, perçage, BOM, vérification dans un visualiseur"),("1 h","Soudure et contrôle IPC ; auto-test")],
  liens=[L("Première S03 – PCB et routage", P+"S03-kicad-pcb-editor-routage-pistes-vias/01-cours.md"), L("Première S04 – double face et Gerber", P+"S04-pcb-double-face-metallisation/01-cours.md"), L("Terminale S06 – TP de bout en bout", T+"S06-flux-kicad-complet-schema-erc-pcb-drc/02-tp-de-bout-en-bout.md"), L("Seconde S04 – soudure et IPC", S+"S04-soudure-a-l-etain-composants/01-cours.md")],
  tests=[("Quelle largeur pour une piste d'alimentation, quelle clearance ?","Piste d'alimentation **0,5 mm à 0,8 mm** ; clearance minimale **0,2 à 0,25 mm**."),("Quels fichiers envoie-t-on au fabricant ?","Les **Gerber** (cuivre, masque, sérigraphie, contour) et le fichier de **perçage**."),("Pourquoi ouvrir les Gerber dans un visualiseur ?","Pour voir **ce qui sera réellement fabriqué**."),("Une brasure avec un remplissage de 72 % est-elle conforme (classe 2) ?","**Non** : minimum 75 %."),("Dans quel ordre route-t-on ?","**Alimentation** d'abord, puis les signaux.")],
  livrable="Fichiers de fabrication (Gerber, perçage, BOM) de la carte de la semaine 5."),
 dict(n=7, titre="Commander une charge, amplifier, filtrer", comp="C07",
  obj=["Dimensionner la résistance de base d'un transistor en commutation.", "Choisir transistor, MOSFET ou relais, et protéger une charge inductive.", "Calculer le gain d'un AOP non inverseur et la fréquence de coupure d'un filtre RC.", "Lire une table de vérité."],
  deroule=[("1 h","Transistor en commutation : $R_b$"),("1 h","MOSFET et relais, diode de roue libre"),("1 h","AOP, filtre RC, portes logiques"),("1 h","Auto-test et correction")],
  liens=[L("Première S12 – transistor, MOSFET, relais", P+"S12-prototypes-avances-integration/03-transistor-mosfet-relais.md"), L("Première S12 – AOP, filtre RC, portes logiques", P+"S12-prototypes-avances-integration/04-aop-filtre-logique.md")],
  tests=[("Charge de 50 mA, commande à 5 V : valeur de $R_b$ ?","$I_B = 5\\,\\mathrm{mA}$ ; $R_b = \\dfrac{4{,}3}{0{,}005} = 860\\,\\Omega$ → **820 Ω**."),("Pourquoi une diode sur une bobine de relais ?","Elle absorbe le **pic de tension** à la coupure."),("AOP non inverseur, $R_f = 10\\,\\mathrm{k\\Omega}$, $R_g = 1\\,\\mathrm{k\\Omega}$ : gain ?","$1 + 10 = 11$."),("$R = 10\\,\\mathrm{k\\Omega}$, $C = 100\\,\\mathrm{nF}$ : $f_c$ ?","$\\dfrac{1}{2\\pi RC} \\approx 159\\,\\mathrm{Hz}$."),("Sortie d'une porte ET avec A = 1, B = 0 ?","**0**.")],
  livrable="Schéma commenté d'une commande de relais par transistor, avec calcul de $R_b$."),
 dict(n=8, titre="Tester et valider : protocole et procès-verbal", comp="C11 · C03",
  obj=["Suivre un protocole de test et noter attendu / mesuré / verdict.", "Comparer une mesure et sa marge à une tolérance.", "Rédiger un PV clair (identification, instruments, résultats, conclusion)."],
  deroule=[("1 h","Tolérance, marge de mesure (version essentielle) et conformité"),("1 h","Structure d'un PV, traçabilité des instruments"),("1 h","TP : carte NE555 / 7805 (mesures et PV)"),("1 h","Auto-test et correction")],
  liens=[L("Terminale S02 – rapport de mesures et PV", T+"S02-rapport-de-mesures-pv-professionnel/01-cours.md"), L("Terminale S07 – validation et conformité", T+"S07-validation-conformite-pv-professionnel/01-cours.md"), L("Terminale S11 – TP carte NE555 / 7805", T+"S11-interpreter-document-mesures-carte/02-tp.md")],
  tests=[("Sortie 5 V ± 5 % : quelle plage est acceptable ?","De **4,75 V à 5,25 V**."),("Mesure $(5{,}02 \\pm 0{,}05)\\,\\mathrm{V}$ : conforme ?","**Oui** : la plage 4,97 à 5,07 V est dans la tolérance."),("Mesure $(5{,}20 \\pm 0{,}08)\\,\\mathrm{V}$ : conforme ?","**Non garanti** : la plage dépasse 5,25 V."),("Pourquoi indiquer l'instrument et son étalonnage ?","Pour que la mesure soit **vérifiable** (traçabilité)."),("Un PV peut-il se terminer par « ça marche » ?","**Non** : la conclusion compare le résultat à un **critère chiffré**.")],
  livrable="PV complet d'une carte (tableau attendu / mesuré / verdict + conclusion)."),
 dict(n=9, titre="Dépanner un circuit simple", comp="C11",
  obj=["Appliquer la méthode : décrire, mesurer, comparer, isoler, réparer, tester.", "Construire un tableau de tensions attendues / mesurées.", "Remplir une fiche d'intervention et appliquer les règles de sécurité."],
  deroule=[("1 h","La méthode et la sécurité (TBT, ESD, EPI)"),("1 h","Cas pratique : LED pilotée par un transistor (4 pannes)"),("1 h","Dépannage sur maquette ESP32 (démarche DECA)"),("1 h","Fiche d'intervention et auto-test")],
  liens=[L("Terminale S12 – dépanner un circuit simple", T+"S12-reussir-un-tp-de-mesure-en-45-minutes/03-depannage-circuit-simple.md"), L("Première S14 – maintenance corrective", P+"S14-maintenance-corrective-diagnostic-de/01-cours.md"), L("Seconde S05 – sécurité et environnement", S+"S05-maintenance-n1-nettoyage-de-cartes/02-securite-et-environnement.md")],
  tests=[("Par quoi commence-t-on un dépannage ?","Par **décrire** le symptôme et **vérifier l'alimentation**, pas par changer des composants."),("Où se cache la panne dans un tableau de tensions ?","À la **première** valeur mesurée qui ne correspond pas à la valeur attendue."),("Pourquoi mesure-t-on une résistance hors tension ?","Sous tension, la mesure est **fausse** et peut endommager l'appareil."),("Combien de composants change-t-on à la fois ?","**Un seul**, puis on reteste."),("À partir de quelle tension faut-il une habilitation ?","Au-delà de **50 V alternatif ou 120 V continu**.")],
  livrable="Fiche d'intervention remplie pour une panne diagnostiquée."),
 dict(n=10, titre="Épreuve blanche et bilan", comp="C03 · C07 · C11",
  obj=["Réussir une épreuve complète en temps limité avec documents autorisés.", "Identifier ses dernières lacunes et les corriger.", "Constituer son dossier de compétences."],
  deroule=[("3 h","Épreuve blanche complète (mesures, calculs, PV)"),("1 h","Correction, bilan personnel et plan de révision")],
  liens=[L("Terminale S15 – examen complet 2 h", T+"S15-document-autorise-examen-complet-2h/README.md"), L("Terminale S13 – TP complet 2 h", T+"S13-documents-autorises-tp-complet-2h/README.md"), L("Terminale S17 – entraînement contrainte de temps", T+"S17-entrainement-contrainte-de-temps/README.md"), L("Terminale S16 – séance finale", T+"S16-seance-finale-cibler-comprendre-corriger/README.md"), L("Terminale S18 – dossier de compétences", T+"S18-finalisation-du-dossier-de-competences/README.md")],
  tests=[("Quels sont les trois temps d'un TP de mesure efficace ?","**Préparer** (calculs attendus), **mesurer** (noter attendu / mesuré), **conclure** (verdict et PV)."),("Qu'est-ce qui coûte le plus de points en épreuve ?","Les **oublis d'unité**, de tolérance et de conclusion."),("Que faire si une mesure est incohérente ?","Vérifier le **branchement**, le **calibre**, l'**instrument**, puis refaire la mesure."),("Quelles compétences sont évaluées à l'E2 ?","**C03** (participer à un projet), **C07** (réaliser des maquettes et prototypes), **C11** (maintenir un système électronique)."),("Que contient le dossier de compétences ?","Les **preuves** de tes activités : schémas, PV, fiches d'intervention, mesures.")],
  livrable="Copie corrigée de l'épreuve blanche et plan de révision personnel."),
]

PASSEPORT = """# 🎛️ Passeport instruments

> Chaque compétence se **valide** par une **manipulation observée** (l'enseignant ou un camarade coche). Les trois années préparent ces compétences ; en parcours court, tu les fais **toutes** pendant les semaines 2, 4, 8 et 9.

| Instrument | Je sais… | Où s'entraîner | Validé |
|---|---|---|---|
| **Multimètre** | mesurer une **tension** (en parallèle) | [Seconde S12](../seconde/S12-tests-au-multimetre-et-controle-qualite/01-cours.md) | ☐ |
| | mesurer un **courant** (en série) sans court-circuit | idem | ☐ |
| | mesurer une **résistance** hors tension | idem | ☐ |
| | tester une **continuité** et une **diode** | idem | ☐ |
| | choisir le bon **calibre** et lire la **précision** du constructeur | [Terminale S02](../terminale/S02-rapport-de-mesures-pv-professionnel/01-cours.md) | ☐ |
| **Alimentation de labo** | régler la **tension** et la **limite de courant** avant de brancher | [Seconde S12](../seconde/S12-tests-au-multimetre-et-controle-qualite/06-alimentation-labo-et-generateur.md) | ☐ |
| | interpréter le mode **CV / CC** | idem | ☐ |
| **Générateur de fonctions** | produire un sinus, un carré (fréquence, amplitude, offset) | idem | ☐ |
| **Oscilloscope** | installer et **compenser** une sonde ×10 | [Seconde S12](../seconde/S12-tests-au-multimetre-et-controle-qualite/05-prise-en-main-oscilloscope.md) | ☐ |
| | lire **amplitude, période, fréquence** | idem | ☐ |
| | régler le **déclenchement** | [Première S05](../premiere/S05-tests-mesures-avances-oscilloscope/05-tp-instruments-avances.md) | ☐ |
| | utiliser **mesures automatiques et curseurs** | idem | ☐ |
| | observer **deux voies** (entrée / sortie d'un montage) | idem | ☐ |
| | mesurer un **rapport cyclique** (PWM) | Seconde S12 et Première S05 | ☐ |
| **Analyseur logique** (si disponible) | décoder une liaison **UART** ou **I2C** | [Première S05](../premiere/S05-tests-mesures-avances-oscilloscope/01-cours.md) | ☐ |
| **Soudure** | souder et contrôler une brasure (IPC-A-610) | [Seconde S04](../seconde/S04-soudure-a-l-etain-composants/01-cours.md) | ☐ |

## ⏱️ Atelier chronométré (fin de semaine 2)

Objectif : **moins de 2 minutes** par manœuvre.

1. Mesurer une résistance hors tension et la comparer à sa tolérance.
2. Régler l'alimentation à 5 V, limite 50 mA, puis alimenter un montage LED.
3. Mesurer la tension aux bornes de la LED et le courant dans le circuit.
4. Régler le GBF (carré, 1 kHz, 3 V$_{pp}$) et lire sa période et son amplitude à l'oscilloscope.
5. Mesurer le rapport cyclique d'un signal PWM.

> [!SUCCESS] 🧠 À retenir
> - Avant toute mesure : **bon appareil**, **bon calibre**, **bon branchement**.
> - Avant de brancher un montage : **tension et limite de courant réglées**.
> - À l'oscilloscope : **sonde déclarée**, **masse au bon endroit**, **déclenchement réglé**.
"""

def page(w):
    n = w['n']
    o = [f"# Semaine {n} : {w['titre']}", "", f"> **Durée** : 4 h · **Compétences E2 travaillées** : {w['comp']}", "", "## 🎯 Objectifs : à la fin de la semaine, je sais…", ""]
    o += [f"- {x}" for x in w['obj']] + ["", "## 🗓️ Déroulé", "", "| Durée | Activité |", "|---|---|"]
    o += [f"| {d} | {a} |" for d, a in w['deroule']] + ["", "## 📖 Le cours en bref", "", COURS[n].strip(), "", "## 🛠️ Atelier guidé : on construit ensemble le clignoteur", "", ATELIER[n].strip(), "", "## ✍️ Exercices d'application", ""]
    for i, (q, _) in enumerate(EXOS[n], 1): o.append(f"{i}. {q}")
    o += ["", '??? success "Corrigés"']
    for i, (_, r) in enumerate(EXOS[n], 1): o.append(f"    {i}. {r}")
    o += ["", "## 📚 Pour approfondir : les séances à consulter", ""]
    o += [f"- {l}" for l in w['liens']] + ["", "## ✅ Auto-test", ""]
    for i, (q, _) in enumerate(w['tests'], 1): o.append(f"{i}. {q}")
    o += ["", '??? success "Réponses"']
    for i, (_, r) in enumerate(w['tests'], 1): o.append(f"    {i}. {r}")
    o += ["", "## 📦 Livrable", "", f"{w['livrable']}", ""]
    return "\n".join(o)

def readme():
    o = ["# ⚡ L'essentiel en 1 an : une formation express en 10 semaines", "",
         "Ce n'est **pas** une simple révision : c'est une **formation complète et accélérée**, qui part des bases et mène à l'épreuve E2 (« Réalisation et maintenance de produits électroniques », coefficient 5). **10 semaines de 4 heures** (40 h). Chaque semaine contient un **cours**, un **atelier guidé pas à pas**, des **exercices corrigés** et un **livrable**. On construit, on teste et on dépanne **une même carte** (un clignoteur à LED) du début à la fin : c'est le **fil rouge**. Utilisable en classe comme **seul(e)**, y compris pour rattraper avant le bac.", "",
         "## 🎯 Ce que tu sauras faire à la fin", "",
         "- **comprendre** un circuit électronique simple et **connaître** ses composants ;",
         "- **lire** une datasheet et en tirer les valeurs utiles ;",
         "- **tracer** un circuit (schéma, PCB) jusqu'aux **fichiers Gerber** ;",
         "- **mesurer, tester et valider** une carte (multimètre, oscilloscope, PV) ;",
         "- **dépanner** un circuit simple avec une méthode.", "",
         "Les compétences évaluées à l'E2 sont **C03** (participer à un projet), **C07** (réaliser des maquettes et prototypes) et **C11** (maintenir un système électronique).", "",
         "## 🗓️ Les 10 semaines", "", "| Semaine | Thème | Compétences |", "|---|---|---|"]
    o += [f"| [**{w['n']}**](S{w['n']:02d}-semaine.md) | {w['titre']} | {w['comp']} |" for w in SEMAINES]
    o += ["", "## 🧭 Comment travailler", "",
          "1. Lis les **objectifs** de la semaine, puis suis le **déroulé** (4 × 1 h).",
          "2. Lis le **cours en bref**, puis fais l'**atelier guidé** étape par étape (tu peux comparer à la correction).",
          "3. Fais les **exercices** et l'**auto-test** *sans regarder* les réponses, puis corrige-toi.",
          "4. Pour aller plus loin, les séances de Seconde, Première et Terminale sont indiquées en fin de page.",
          "5. Finis par le **livrable** : c'est une preuve de compétence pour ton dossier.", "",
          "> [!TIP] 🎛️ Passeport instruments",
          "> Savoir **manipuler les appareils de mesure** est une compétence clé de l'E2. Tout au long du parcours, fais valider ton [passeport instruments](passeport-instruments.md) : multimètre, alimentation, générateur, oscilloscope.", "",
          "> [!NOTE] 🔶 Et le reste ?",
          "> Les séances marquées 🔶 (approfondissement) ne sont **pas nécessaires** pour l'essentiel : Gauge R&R, calcul complet d'incertitudes, fiabilité MTBF, cloud AWS, requêtes Flux. Tu peux les faire **après** ce parcours.", ""]
    return "\n".join(o)

def main(root):
    d = Path(root) / 'docs' / 'essentiel-en-1-an'
    d.mkdir(parents=True, exist_ok=True)
    (d / 'README.md').write_text(readme(), encoding='utf-8')
    for w in SEMAINES: (d / f"S{w['n']:02d}-semaine.md").write_text(page(w), encoding='utf-8')
    nav = ['title: "⚡ L\'essentiel en 1 an"', 'nav:', '  - README.md']
    nav += ['  - "🎛️ Passeport instruments": passeport-instruments.md']
    nav += [f"  - \"Semaine {w['n']} · {w['titre']}\": S{w['n']:02d}-semaine.md" for w in SEMAINES]
    (d / 'passeport-instruments.md').write_text(PASSEPORT, encoding='utf-8')
    (d / '.pages').write_text("\n".join(nav) + "\n", encoding='utf-8')
    print('parcours essentiel généré')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
