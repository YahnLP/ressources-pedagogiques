# Semaine 6 : Du PCB aux fichiers de fabrication (Gerber)

> **Durée** : 4 h · **Compétences E2 travaillées** : C07

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Placer et router un PCB selon des règles (clearance, largeurs).
- Passer le DRC, exporter les Gerber, le perçage et la BOM.
- Contrôler une brasure selon IPC-A-610.

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Contour, règles de conception, placement |
| 1 h | Routage (alimentation d'abord) et DRC |
| 1 h | Gerber, perçage, BOM, vérification dans un visualiseur |
| 1 h | Soudure et contrôle IPC ; auto-test |

## 📖 Le cours en bref

??? question "🤔 À ton avis ?"
    Pourquoi les pistes d'alimentation sont-elles plus larges que les pistes de signal ?

    **Réponse** : une piste est un **fil de cuivre** : trop fine pour le courant, elle **chauffe**. On la dimensionne en fonction du courant qu'elle transporte.

### 1. Les règles de conception

| Règle | Valeur courante | Pourquoi |
|---|---|---|
| **Clearance** (espace entre deux pistes) | 0,2 à 0,25 mm | éviter les courts-circuits |
| Piste de **signal** | 0,25 à 0,35 mm | faible courant |
| Piste d'**alimentation** | 0,5 à 0,8 mm | plus de courant |
| **Via** | Ø 0,8 mm, perçage 0,4 mm | passer d'une face à l'autre |

### 2. Placement et routage

1. **Contour** de la carte (Edge.Cuts).
2. Placer les **connecteurs au bord**, puis l'**alimentation**, puis le circuit principal, puis les passifs **près des circuits** qu'ils servent.
3. Le **condensateur de découplage** (100 nF) se place **au plus près** des broches d'alimentation du circuit intégré.
4. **Router l'alimentation en premier**, puis les signaux. Une masse **continue** (pas coupée par une piste) limite les perturbations.

### 3. Contrôler : le DRC

Le DRC vérifie que **rien ne viole les règles** (pistes trop proches, trop fines, pastilles qui se touchent). Objectif : **0 erreur**.

### 4. Les fichiers de fabrication

Le fabricant reçoit :

- les **Gerber** : un fichier par couche (cuivre, masque de soudure, sérigraphie, contour) ;
- le fichier de **perçage** (.drl) ;
- la **BOM** (liste des composants) pour l'assemblage.

> [!TIP] 💡 En clair
> Un fichier Gerber est une **image vectorielle** d'une couche. On l'ouvre dans un **visualiseur** pour voir **exactement** ce qui sera fabriqué.

### 5. Souder et contrôler (IPC-A-610)

Pour un composant traversant (classe 2) : soudure **brillante**, forme de **cône**, trou **rempli à 75 % au moins**. Défauts : **pont de soudure** (court-circuit), soudure **froide** (terne, craquelée), **manque de soudure**.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Ne pas ouvrir les Gerber avant l'envoi.
> - Router une piste de signal **sous** un composant sans y penser (risque de court-circuit).
> - Oublier le **perçage** (fichier .drl) dans l'envoi.

## 🛠️ Atelier guidé : on construit ensemble le clignoteur

**Fil rouge** : tu transformes le schéma en **carte fabricable**, puis tu la **soudes**.

1. Importe le schéma dans le PCB. Trace le **contour 60 × 40 mm**.
2. **Règles** : clearance 0,25 mm ; pistes 0,25 mm ; alimentation 0,5 mm ; via 0,8 / 0,4 mm.
3. **Place** : J1 au bord, 7805 et ses condensateurs, NE555, passifs près du NE555, LED près du bord.
4. **Route** l'alimentation, puis les signaux. Lance le **DRC** : 0 erreur.
5. **Exporte** Gerber (cuivre, masque, sérigraphie, contour), perçage, BOM. **Ouvre-les** dans un visualiseur.
6. **Soude** dans l'ordre : résistances, support DIP-8, condensateurs, régulateur, connecteur, LED. **Contrôle** les brasures.

??? success "Résultats attendus"
    - DRC : **0 erreur** ; pistes d'alimentation visiblement plus larges.
    - Fichiers : F.Cu (ou B.Cu), masque, sérigraphie, Edge.Cuts, `.drl`, `.csv` de la BOM.
    - Brasures : brillantes, en cône, trou rempli à **75 % au moins** ; aucun pont ni soudure froide.

## ✍️ Exercices d'application

1. Deux pistes sont à 0,18 mm l'une de l'autre, règle 0,25 mm. Violation de combien ?
2. Une pastille de 1,8 mm est percée à 1,0 mm. Largeur de l'anneau de cuivre ?
3. Où place-t-on le condensateur de découplage du NE555 ?
4. Remplissage d'un trou traversant de 70 % : conforme en classe 2 ?

??? success "Corrigés"
    1. $0{,}25 - 0{,}18 = 0{,}07\,\mathrm{mm}$ : le DRC signale une erreur.
    2. $\dfrac{1{,}8 - 1{,}0}{2} = 0{,}4\,\mathrm{mm}$.
    3. **Au plus près** des broches 8 (VCC) et 1 (GND).
    4. **Non** : il faut au moins 75 %.

## 📚 Pour approfondir : les séances à consulter

- [Première S03 – PCB et routage](../premiere/S03-kicad-pcb-editor-routage-pistes-vias/01-cours.md)
- [Première S04 – double face et Gerber](../premiere/S04-pcb-double-face-metallisation/01-cours.md)
- [Terminale S06 – TP de bout en bout](../terminale/S06-flux-kicad-complet-schema-erc-pcb-drc/02-tp-de-bout-en-bout.md)
- [Seconde S04 – soudure et IPC](../seconde/S04-soudure-a-l-etain-composants/01-cours.md)

## ✅ Auto-test

1. Quelle largeur pour une piste d'alimentation, quelle clearance ?
2. Quels fichiers envoie-t-on au fabricant ?
3. Pourquoi ouvrir les Gerber dans un visualiseur ?
4. Une brasure avec un remplissage de 72 % est-elle conforme (classe 2) ?
5. Dans quel ordre route-t-on ?

??? success "Réponses"
    1. Piste d'alimentation **0,5 mm à 0,8 mm** ; clearance minimale **0,2 à 0,25 mm**.
    2. Les **Gerber** (cuivre, masque, sérigraphie, contour) et le fichier de **perçage**.
    3. Pour voir **ce qui sera réellement fabriqué**.
    4. **Non** : minimum 75 %.
    5. **Alimentation** d'abord, puis les signaux.

## 📦 Livrable

Fichiers de fabrication (Gerber, perçage, BOM) de la carte de la semaine 5.
