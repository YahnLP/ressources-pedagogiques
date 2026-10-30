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

---
