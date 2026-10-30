# 🔬 EXERCICES PROGRESSIFS — S11 · 2ᵉ ANNÉE · E2
## Fiabilité : MTBF · MTTR · R(t) · Systèmes Série/Parallèle/Complexes

---

> **Nom** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Date** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Calculatrice obligatoire**

---

## 📌 Données utiles

$$e^{-0{,}1} = 0{,}905 \quad e^{-0{,}2} = 0{,}819 \quad e^{-0{,}3} = 0{,}741$$

$$e^{-0{,}4} = 0{,}670 \quad e^{-0{,}5} = 0{,}607 \quad e^{-1} = 0{,}368$$

$e^{-1{,}5}$ = 0,223    $e^{-2}$   = 0,135    $e^{-3}$   = 0,050  

1 an = 8 760 heures · 1 mois ≈ 730 heures · 1 semaine = 168 heures  

---

## 🟢 BLOC 1 — MTBF, MTTR, Disponibilité (30 min)

### Exercice 1.1 — Calculs fondamentaux

**Contexte** : Un serveur de supervision industrielle a fonctionné 3 ans en continu (24h/24).
Il a subi 4 arrêts pour maintenance corrective :

| Arrêt | Durée |
|---|---|
| 1 | 45 min |
| 2 | 3h 20 min |
| 3 | 1h 00 |
| 4 | 7h 15 min |

**Q1.1.a** — Convertis toutes les durées en heures décimales :

```
Arrêt 1 : 45 min = _______ h
Arrêt 2 : 3h 20 min = _______ h
Arrêt 3 : 1h 00 = _______ h
Arrêt 4 : 7h 15 min = _______ h
```

**Q1.1.b** — Calcule TA, TO, MTBF, MTTR et D :

```
TA (temps total arrêt) = _______ + _______ + _______ + _______ = _______ h
TO (temps de fonctionnement) = 3 × 8760 − TA = _______ − _______ = _______ h
MTBF = TO / n = _______ / _______ = _______ h
MTTR = TA / n = _______ / _______ = _______ h
D = MTBF / (MTBF + MTTR) = _______ / _______ = _______ = _______ %
```

**Q1.1.c** — Convertis le MTBF en mois :

```
MTBF = _______ heures / 730 h/mois ≈ _______ mois
Interprétation : une panne tous les _______ mois environ
```

**Q1.1.d** — La norme industrielle imposée est D ≥ 99,5%. Ce serveur la respecte-t-il ?

```
D calculé : _______ % · Norme : 99,5% · ☐ Conforme ☐ Non conforme
```

??? success "Réponses"
    **Q1.1.a** : 45 min = 0,75 h · 3 h 20 min ≈ 3,33 h · 1 h 00 = 1 h · 7 h 15 min = 7,25 h  
    **Q1.1.b** : TA = 0,75 + 3,33 + 1 + 7,25 ≈ 12,33 h · TO = 3 × 8 760 − 12,33 ≈ 26 267,67 h  
    MTBF = 26 267,67 / 4 ≈ 6 566,9 h · MTTR = 12,33 / 4 ≈ 3,08 h  
    $D = \dfrac{6\,566{,}9}{6\,566{,}9 + 3{,}08} \approx 0{,}99953 = 99{,}95\,\%$  
    **Q1.1.c** : 6 566,9 / 730 ≈ 9 mois : une panne tous les 9 mois environ  
    **Q1.1.d** : 99,95 % ≥ 99,5 % : conforme

---

### Exercice 1.2 — Améliorer la disponibilité

**Contexte** : L'ingénieur veut atteindre D = 99,9% avec le même MTBF calculé en 1.1.
Quel MTTR maximum peut-il se permettre ?

```
D = MTBF / (MTBF + MTTR) ≥ 0,999

Résoudre pour MTTR :
0,999 × (MTBF + MTTR) = MTBF
0,999 × MTBF + 0,999 × MTTR = MTBF
0,999 × MTTR = MTBF − 0,999 × MTBF
0,999 × MTTR = MTBF × (1 − 0,999) = MTBF × 0,001

MTTR ≤ MTBF × 0,001 / 0,999 = _______ × 0,001 / 0,999 ≈ _______ h

Le MTTR actuel est de _______ h.
Pour atteindre 99,9%, il faudrait le réduire de _______ h.
Piste d'amélioration : ________________________________________________________
```

??? success "Réponses"
    $MTTR \leq \dfrac{6\,566{,}9 \times 0{,}001}{0{,}999} \approx 6{,}57\,\mathrm{h}$  
    Le MTTR actuel est de 3,08 h : il est déjà inférieur à 6,57 h, donc l'objectif D ≥ 99,9 % est déjà atteint (D = 99,95 %). Aucune réduction n'est nécessaire ; pour garder cette marge, on peut tenir des pièces de rechange en stock.

---

### Exercice 1.3 — Comparaison de technologies

**Contexte** : Choisir entre 3 solutions de stockage :

| Technologie | MTBF | MTTR moyen |
|---|---|---|
| HDD 7200 tr/min | 300 000 h | 4 h |
| SSD SATA | 1 500 000 h | 1 h |
| SSD NVMe | 2 000 000 h | 0,5 h |

**Q1.3.a** — Calcule la disponibilité de chaque solution :

```
HDD  : D = _______ / (_______ + _______) = _______ = _______ %
SSD  : D = _______ / (_______ + _______) = _______ = _______ %
NVMe : D = _______ / (_______ + _______) = _______ = _______ %
```

**Q1.3.b** — Pour un datacenter qui exige 5 nines (99,999%), quelle solution atteint cet objectif ?

```
5 nines = 99,999% = 0,99999
Aucune des 3 ne l'atteint seule → ☐ Vrai ☐ Faux

La solution la plus proche est : _____________________________________________
Écart par rapport à l'objectif : _______ %
```

??? success "Réponses"
    **Q1.3.a** : HDD : $D = \dfrac{300\,000}{300\,004} \approx 99{,}9987\,\%$  
    SSD : $D = \dfrac{1\,500\,000}{1\,500\,001} \approx 99{,}99993\,\%$  
    NVMe : $D = \dfrac{2\,000\,000}{2\,000\,000{,}5} \approx 99{,}999975\,\%$  
    **Q1.3.b** : Faux : le HDD n'atteint pas 99,999 % mais le SSD et le NVMe l'atteignent. La solution la plus proche est le NVMe (99,999975 %), qui dépasse l'objectif d'environ 0,001 point.

---

## 🟡 BLOC 2 — Loi Exponentielle R(t) = $e^{-\lambda t}$ (30 min)

### Exercice 2.1 — Capteur DHT22

**Données** : DHT22 — MTBF = 50 000 h · fonctionnement 24h/24

**Q2.1.a** — Calcule le taux de panne λ :

```
λ = 1 / MTBF = 1 / _______ = _______ pannes/heure
En notation scientifique : λ = _______ × 10⁻⁵ pannes/heure
```

**Q2.1.b** — Calcule la fiabilité R(t) pour les durées suivantes :

| Durée t | Calcul λt | R(t) = $e^{-\lambda t}$ | En % |
|---|---|---|---|
| 1 an (8 760 h) | | | |
| 2 ans (17 520 h) | | | |
| 5 ans (43 800 h) | | | |
| MTBF (50 000 h) | | $e^{-1}$ = 0,368 | 36,8% |

**Q2.1.c** — Interprète le résultat à t = 1 an :

$$R(8760) = \underline{\hspace{2.5em}} %$$

Signification : sur 1000 capteurs DHT22 mis en service simultanément,  
après 1 an il en reste \_\_\_\_\_\_\_ encore fonctionnels.  
Et \_\_\_\_\_\_\_ sont tombés en panne.  

**Q2.1.d** — Quelle durée t garantit que R(t) ≥ 90% ?

```
R(t) ≥ 0,90
e^(−λt) ≥ 0,90

Pour trouver t : prendre le logarithme naturel ln des deux membres
−λt ≥ ln(0,90)   → Note : ln(0,90) ≈ −0,105

t ≤ −ln(0,90) / λ = 0,105 / (2×10⁻⁵) = _______ heures = _______ mois
```

??? success "Réponses"
    **Q2.1.a** : $\lambda = \dfrac{1}{50\,000} = 2 \times 10^{-5}$ panne/heure  
    **Q2.1.b** :  
    - 1 an : $\lambda t = 0{,}1752$ ; $R = e^{-0{,}1752} \approx 0{,}839$ soit 83,9 %  
    - 2 ans : $\lambda t = 0{,}3504$ ; $R \approx 0{,}704$ soit 70,4 %  
    - 5 ans : $\lambda t = 0{,}876$ ; $R \approx 0{,}416$ soit 41,6 %  
    - MTBF : $\lambda t = 1$ ; $R = 0{,}368$ soit 36,8 %  
    **Q2.1.c** : R(8 760) ≈ 83,9 % : sur 1 000 capteurs, environ 839 fonctionnent encore et 161 sont en panne.  
    **Q2.1.d** : $t \leq \dfrac{0{,}105}{2 \times 10^{-5}} \approx 5\,268\,\mathrm{h} \approx 7{,}2$ mois

---

### Exercice 2.2 — Comparer deux composants

**Données** :

- Composant A : MTBF = 10 000 h (composant économique)
- Composant B : MTBF = 100 000 h (composant premium, 5× plus cher)

**Q2.2.a** — Calcule les taux de panne :

$$
\begin{aligned}
\lambda A &= \dfrac{1}{10\,000} = \underline{\hspace{2.5em}} h^{-1} \\
\lambda B &= \dfrac{1}{100\,000} = \underline{\hspace{2.5em}} h^{-1}
\end{aligned}
$$

**Q2.2.b** — Complète le tableau de fiabilité et conclus :

| Durée | $R_{A}$(t) | $R_{B}$(t) | Δ fiabilité |
|---|---|---|---|
| 1 000 h | | | |
| 5 000 h | | | |
| 10 000 h | 36,8% | | |
| 50 000 h | | | |

**Q2.2.c** — Pour une application qui doit fonctionner 2 ans sans maintenance,
lequel des deux composants est indispensable ? Justifie avec les calculs :

Durée : 2 ans = \_\_\_\_\_\_\_ h  

$$R_{\mathrm{A}}(17520) = e^{-0{,}0001 \times 17520} = e^{\underline{\hspace{2.5em}}} = \underline{\hspace{2.5em}} \to \underline{\hspace{2.5em}} %$$

$$R_{\mathrm{B}}(17520) = e^{-0{,}00001 \times 17520} = e^{\underline{\hspace{2.5em}}} = \underline{\hspace{2.5em}} \to \underline{\hspace{2.5em}} %$$

Conclusion : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  

??? success "Réponses"
    **Q2.2.a** : $\lambda_A = 10^{-4}\,\mathrm{h^{-1}}$ ; $\lambda_B = 10^{-5}\,\mathrm{h^{-1}}$  
    **Q2.2.b** :  
    - 1 000 h : $R_A = 0{,}905$ ; $R_B = 0{,}990$ ; écart 0,085  
    - 5 000 h : $R_A = 0{,}607$ ; $R_B = 0{,}951$ ; écart 0,344  
    - 10 000 h : $R_A = 0{,}368$ ; $R_B = 0{,}905$ ; écart 0,537  
    - 50 000 h : $R_A = 0{,}0067$ ; $R_B = 0{,}607$ ; écart 0,600  
    **Q2.2.c** : 2 ans = 17 520 h. $R_A = e^{-1{,}752} \approx 0{,}173$ soit 17,3 % ; $R_B = e^{-0{,}1752} \approx 0{,}839$ soit 83,9 %.  
    Conclusion : le composant B (premium) est indispensable, car A n'a que 17 % de chances de tenir 2 ans sans panne.

---

## 🟠 BLOC 3 — Fiabilité des systèmes complexes (20 min)

### Exercice 3.1 — Système de contrôle industriel

**Architecture** :

```
Entrée → [Capteur (R=0,95)] → ┌─[CPU A (R=0,90)]─┐
                               └─[CPU B (R=0,90)]─┘ → [Sortie (R=0,99)] → Sortie
```

**Q3.1.a** — Calcule la fiabilité du bloc CPU (parallèle) :

$$
\begin{aligned}
R_{\mathrm{CPU}} &= 1 - (1 - \underline{\hspace{2.5em}}) \times (1 - \underline{\hspace{2.5em}}) \\
&= 1 - \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \\
&= \underline{\hspace{2.5em}}
\end{aligned}
$$

**Q3.1.b** — Calcule la fiabilité globale du système (série) :

$$
\begin{aligned}
Rs &= R_{\mathrm{capteur}} \times R_{\mathrm{CPU}} \times R_{\mathrm{sortie}} \\
&= \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \\
&= \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %
\end{aligned}
$$

**Q3.1.c** — Si les CPU n'étaient PAS redondants (1 seul CPU B, R=0,90), quelle serait la fiabilité ?

$$Rs_sans_redondance = \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %$$

Gain de la redondance CPU : \_\_\_\_\_\_\_ % − \_\_\_\_\_\_\_ % = \_\_\_\_\_\_\_ points  

??? success "Réponses"
    **Q3.1.a** : $R_{CPU} = 1 - (1 - 0{,}90)(1 - 0{,}90) = 1 - 0{,}10 \times 0{,}10 = 0{,}99$  
    **Q3.1.b** : $R_s = 0{,}95 \times 0{,}99 \times 0{,}99 \approx 0{,}931 = 93{,}1\,\%$  
    **Q3.1.c** : sans redondance : $0{,}95 \times 0{,}90 \times 0{,}99 \approx 0{,}846 = 84{,}6\,\%$ ; gain de la redondance : 93,1 − 84,6 ≈ 8,5 points

---

### Exercice 3.2 — Station IoT CLIMASENS (lien avec le projet)

**Architecture du système CLIMASENS** :

![Station IoT : DHT22 et MQ-2 en parallèle, puis ESP32, Wi-Fi/MQTT et Node-RED en série](images/rbd-station.png)

Note : les deux capteurs sont en **parallèle fonctionnel** (un seul suffit pour détecter une anomalie).

**Q3.2.a** — Calcule la fiabilité du bloc capteurs en parallèle :

$$
\begin{aligned}
R_{\mathrm{capteurs}} &= 1 - (1 - \underline{\hspace{2.5em}}) \times (1 - \underline{\hspace{2.5em}}) \\
&= 1 - \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \\
&= \underline{\hspace{2.5em}}
\end{aligned}
$$

**Q3.2.b** — Calcule la fiabilité globale :

$$
\begin{aligned}
Rs &= R_{\mathrm{capteurs}} \times R_{\mathrm{ESP32}} \times R_{\mathrm{WiFi}} \times R_{\mathrm{NodeRED}} \\
&= \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \times \underline{\hspace{2.5em}} \\
&= \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} %
\end{aligned}
$$

**Q3.2.c** — Le maillon le plus faible de la chaîne est le capteur MQ-2 (R=0,85). Comment améliorer le système sans changer les composants ?

```
Solution proposée : ___________________________________________________________
Calculer la nouvelle Rs avec votre amélioration : _______ %
```

??? success "Réponses"
    **Q3.2.a** : $R_{capteurs} = 1 - (1 - 0{,}88)(1 - 0{,}85) = 1 - 0{,}12 \times 0{,}15 = 0{,}982$  
    **Q3.2.b** : $R_s = 0{,}982 \times 0{,}92 \times 0{,}97 \times 0{,}99 \approx 0{,}868 = 86{,}8\,\%$  
    **Q3.2.c** : l'ESP32 (R = 0,92) est le maillon le plus faible de la chaîne en série : on le double en redondance (deux ESP32 en parallèle, $R = 1 - 0{,}08^2 = 0{,}9936$), d'où $R_s = 0{,}982 \times 0{,}9936 \times 0{,}97 \times 0{,}99 \approx 0{,}937 = 93{,}7\,\%$.

---

## ✍️ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Calcul MTBF, MTTR, D à partir d'un historique | ☐ | ☐ | ☐ |
| Conversion heures ↔ années ↔ mois | ☐ | ☐ | ☐ |
| Calcul λ = 1/MTBF | ☐ | ☐ | ☐ |
| Calcul R(t) = $e^{-\lambda t}$ avec calculatrice | ☐ | ☐ | ☐ |
| Fiabilité système série Rs = R1×R2×... | ☐ | ☐ | ☐ |
| Fiabilité système parallèle Rs = 1−(1−R1)(1−R2) | ☐ | ☐ | ☐ |
| Décomposer un système mixte série/parallèle | ☐ | ☐ | ☐ |

---
