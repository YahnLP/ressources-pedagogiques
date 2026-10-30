# 🔬 EXERCICES PRATIQUES — S4 · 2ᵉ ANNÉE · E2
## NE555 Astable · Calculs · Gerber · Sérigraphie · Métallisation

---

> **Nom** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Date** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Format** : Exercices complémentaires au TP · Fiche de cours autorisée

---

## 📐 EXERCICE 1 — Calculs NE555 Astable (15 min)

> Le NE555 en mode astable génère un signal carré dont la fréquence dépend de :
> **R1, R2 et C1**

### Formules

```
Période totale  : T = 0,693 × (R1 + 2×R2) × C1
Temps HIGH (Th) : Th = 0,693 × (R1 + R2) × C1
Temps LOW  (Tl) : Tl = 0,693 × R2 × C1
Fréquence       : f = 1 / T ≈ 1,44 / ((R1 + 2×R2) × C1)
Rapport cyclique: D = Th / T = (R1 + R2) / (R1 + 2×R2)
```

**Q1.1** — Calcule la fréquence avec R1=10kΩ, R2=47kΩ, C1=100µF :

$$T = 0{,}693 \times (10\,000 + 2 \times 47\,000) \times 100 \times 10^{-6}$$

$$T = 0{,}693 \times \underline{\hspace{2.5em}} \times 0{,}0001$$

$$T = \underline{\hspace{2.5em}} s$$

$$f = \dfrac{1}{T} = \underline{\hspace{2.5em}} \mathrm{Hz}$$

La LED clignote à \_\_\_\_\_\_\_\_\_\_ fois par seconde.  

**Q1.2** — Si on remplace C1 par 10µF (valeur ×10 plus petite), que devient la fréquence ?

$$
\begin{aligned}
T_{\mathrm{nouveau}} &= \dfrac{T_{\mathrm{ancien}}}{10} = \underline{\hspace{2.5em}} s \\
f_{\mathrm{nouvelle}} &= \underline{\hspace{2.5em}} \mathrm{Hz}
\end{aligned}
$$

**Q1.3** — Calcule le rapport cyclique pour R1=10kΩ, R2=47kΩ :

$$D = \dfrac{10 + 47}{10 + 2 \times 47} = \underline{\hspace{2.5em}} / \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %$$

Interprétation : le signal est HIGH pendant \_\_\_\_\_\_% du temps et LOW pendant \_\_\_\_\_\_%  
La LED est allumée pendant \_\_\_\_\_\_% de la période → elle semble ☐ plus ☐ moins lumineuse que 50%  

??? success "Réponses"
    **Q1.1** : $T = 0{,}693 \times 104\,000 \times 0{,}0001 \approx 7{,}2\,\mathrm{s}$ ; $f = \dfrac{1}{7{,}2} \approx 0{,}14\,\mathrm{Hz}$ : la LED clignote environ 0,14 fois par seconde (un clignotement toutes les 7,2 s).  
    **Q1.2** : $T_{nouveau} = \dfrac{7{,}2}{10} \approx 0{,}72\,\mathrm{s}$ ; $f_{nouvelle} \approx 1{,}4\,\mathrm{Hz}$.  
    **Q1.3** : $D = \dfrac{57}{104} \approx 0{,}548 = 54{,}8\,\%$ : le signal est HIGH 54,8 % du temps et LOW 45,2 % du temps. La LED est allumée 54,8 % de la période : elle semble un peu plus lumineuse qu'à 50 %.

---

## 📐 EXERCICE 2 — Identifier les calques Gerber (10 min)

> Voici les noms de fichiers Gerber générés par KiCad. Associe chaque fichier à son rôle.

| Fichier Gerber | Rôle (à compléter) |
|---|---|
| circuit-F_Cu.gbr | |
| circuit-B_Cu.gbr | |
| circuit-F_Mask.gbr | |
| circuit-B_Mask.gbr | |
| circuit-F_Silkscreen.gbr | |
| circuit-Edge_Cuts.gbr | |
| circuit-PTH.drl | |
| circuit-NPTH.drl | |

??? success "Réponses"
    | Fichier Gerber | Rôle |
    |---|---|
    | circuit-F_Cu.gbr | cuivre de la face avant (pistes et pastilles) |
    | circuit-B_Cu.gbr | cuivre de la face arrière |
    | circuit-F_Mask.gbr | masque de soudure face avant (ouvertures sur les pastilles) |
    | circuit-B_Mask.gbr | masque de soudure face arrière |
    | circuit-F_Silkscreen.gbr | sérigraphie face avant (références, contours, polarités) |
    | circuit-Edge_Cuts.gbr | contour de la carte (découpe) |
    | circuit-PTH.drl | perçages métallisés (pattes de composants, vias) |
    | circuit-NPTH.drl | perçages non métallisés (trous de fixation) |

---

## 📐 EXERCICE 3 — Analyse d'un PCB professionnel (15 min)

> Observe l'image d'un PCB Arduino Nano (ou la description suivante si pas d'image) :

```
DESCRIPTION DU PCBA ARDUINO NANO :
  - PCB vert, double face
  - Microcontrôleur ATmega328P en boîtier TQFP-32 (SMD 7×7mm, 32 pattes)
  - Résistances et condensateurs 0402 et 0603 (SMD, très petits)
  - Connecteur USB (SMD)
  - En-têtes de broches (THT, 2 rangées de 15 pins)
  - Un cristal oscillateur 16MHz (THT, 2 pattes)
  - Régulateur de tension en boîtier SOT-23 (SMD, 3 pattes)
  - Sérigraphie blanche : "ARDUINO NANO", étiquettes des broches (A0-A7, D2-D13...)
  - Vias visibles sur les deux faces
```

**Q3.1** — Identifie au moins 3 raisons pour lesquelles Arduino utilise des composants SMD plutôt que THT pour la majorité des composants :

```
Raison 1 : ____________________________________________________________________
Raison 2 : ____________________________________________________________________
Raison 3 : ____________________________________________________________________
```

**Q3.2** — Pourquoi les connecteurs en-têtes (les rangées de pins) sont-ils en THT et non SMD ?

```
_______________________________________________________________________________
_______________________________________________________________________________
```

**Q3.3** — Sur un Arduino Nano, comment reconnait-on les vias dans la sérigraphie ?

```
Les vias sont visibles comme des _________________ sur le PCB.
Leur rôle ici : _______________________________________________________________
```

??? success "Réponses"
    **Q3.1** : 1. composants beaucoup plus petits : carte compacte ; 2. montage automatique (machine pick and place), donc fabrication rapide et peu coûteuse ; 3. pas de perçage pour chaque patte et meilleures performances en haute fréquence (pistes courtes).  
    **Q3.2** : les en-têtes de broches subissent des efforts mécaniques (insertions et retraits répétés) ; la soudure traversante tient bien mieux qu'une soudure CMS, qui se décollerait.  
    **Q3.3** : les vias sont visibles comme de petits ronds (pastilles de cuivre percées) sur le PCB. Leur rôle ici : faire passer une piste d'une face à l'autre.

---

## 📐 EXERCICE 4 — Questions sur la métallisation (10 min)

**Q4.1** — Comment la métallisation des vias est-elle réalisée industriellement ?

```
Procédé : dépôt galvanique de cuivre (electroless plating + copper plating)
  Étape 1 : Perçage du trou → trou brut (pas de cuivre à l'intérieur)
  Étape 2 : Activation chimique → dépôt d'une couche conductrice de quelques µm
  Étape 3 : __________________ → épaississement du cuivre jusqu'à 25-35 µm

Pourquoi le trou doit-il être métallisé pour fonctionner ?
  Sans métallisation : le trou est un simple _________ → les deux faces ne sont pas connectées
  Avec métallisation : le cuivre du cylindre interne connecte _________ à _________
```

**Q4.2** — Quelle est la différence entre un **via PTH** et un **via NPTH** ?

```
PTH (Plated Through-Hole) : ___________________________________________________
NPTH (Non-Plated Through-Hole) : ______________________________________________
Exemple d'usage NPTH : ________________________________________________________
```

**Q4.3** — Quel est l'inconvénient d'un via avec un diamètre de perçage trop petit (ex: 0,1 mm) ?

```
☐ Le via ne peut pas être percé (limite de précision des machines ~0,2-0,3mm)
☐ Le via est trop résistant électriquement
☐ Le via n'est pas assez solide mécaniquement
☐ Toutes les réponses ci-dessus sont vraies
```

??? success "Réponses"
    **Q4.1** : étape 3 : dépôt électrolytique (galvanique) de cuivre. Sans métallisation, le trou est un simple trou isolant : les deux faces ne sont pas connectées. Avec métallisation, le cuivre du cylindre interne connecte la face avant à la face arrière.  
    **Q4.2** : PTH : trou dont la paroi est métallisée, il relie électriquement les couches et reçoit une patte soudée. NPTH : trou sans cuivre, uniquement mécanique. Exemple d'usage NPTH : trou de fixation (vis M3).  
    **Q4.3** : toutes les réponses sont vraies : un perçage de 0,1 mm est sous la limite des machines (environ 0,2 à 0,3 mm), et le cylindre de cuivre, très fin, serait plus résistif et plus fragile.

---

## 📐 EXERCICE 5 — Concevoir la sérigraphie (10 min)

> Voici les informations à placer en sérigraphie sur un PCB 70×55mm.

**Q5.1** — Classe ces éléments par priorité (du plus important au moins important) :

```
Éléments disponibles :
  A. Référence de chaque composant (R1, D1, IC1...)
  B. Valeur de chaque composant (10kΩ, 470Ω...)
  C. Logo de l'établissement scolaire
  D. Indication de polarité (+ de C1, pin 1 de IC1)
  E. Numéro de version du PCB (v1.0)
  F. Date de conception
  G. Flèche indiquant "Front" / "Back" de la carte
  H. Avertissement "ATTENTION : 9V"

Priorité 1 (indispensable) : _________________________________________________
Priorité 2 (fortement recommandé) : __________________________________________
Priorité 3 (optionnel si place) : ____________________________________________
```

**Q5.2** — La sérigraphie d'une résistance R1 se superpose partiellement sur son pad dans KiCad.
Quelle est la conséquence pratique et comment la corriger ?

```
Conséquence : lors du brasage, l'encre sérigraphie peut _______________________
              → connexion électrique médiocre ou court-circuit
DRC signale : ________________________________________________________________
Correction  : dans KiCad, sélectionner le texte → ____________________________
```

??? success "Réponses"
    **Q5.1** (proposition) : priorité 1 : A (références), D (polarités), H (avertissement 9 V) ; priorité 2 : B (valeurs), E (version du PCB) ; priorité 3 : C (logo), F (date), G (flèche Front / Back).  
    **Q5.2** : conséquence : lors du brasage, l'encre de sérigraphie peut recouvrir la pastille et empêcher la soudure (mouillage insuffisant). Le DRC signale un chevauchement de la sérigraphie avec une pastille (« silkscreen overlap »). Correction : dans KiCad, sélectionner le texte, puis le déplacer hors de la pastille ou réduire sa taille.

---
