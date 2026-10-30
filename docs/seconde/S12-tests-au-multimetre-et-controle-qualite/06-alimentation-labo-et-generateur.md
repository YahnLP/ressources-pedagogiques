# ⚡ L'alimentation de laboratoire et le générateur de fonctions

## 🤔 À ton avis ?

Tu veux alimenter un montage en 5 V pour la première fois. Tu règles l'alimentation de labo, tu branches… et une LED grille. Comment **éviter** ça ?

??? question "Réponse"
    En réglant **avant de brancher** la **tension** ET la **limite de courant** : l'alimentation de labo protège alors le montage en cas d'erreur.

## 1. L'alimentation de laboratoire

Une alimentation réglable a deux réglages :

| Réglage | Rôle | Exemple |
|---|---|---|
| **Tension** (V) | la tension de sortie voulue | 5,0 V |
| **Limite de courant** (A) | le courant **maximal** qu'elle acceptera de fournir | 50 mA |

Elle fonctionne en deux modes :

- **CV** (tension constante) : fonctionnement normal, la tension reste à la valeur réglée ;
- **CC** (courant constant) : le courant a **atteint la limite** ; l'alimentation **baisse la tension** pour protéger le montage. Si le voyant CC s'allume, **il y a un problème** (court-circuit ou consommation trop forte).

> [!TIP] 💡 En clair
> La limite de courant est un **fusible réglable**. On la règle un peu **au-dessus** de ce qu'on attend (par exemple 50 mA pour un montage qui consomme 20 mA).

### Procédure de mise sous tension

1. Sortie **coupée** (OFF).
2. Régler la **tension** voulue.
3. **Court-circuiter** les deux bornes de sortie avec un fil et régler la **limite de courant**, puis retirer le fil.
4. Brancher le montage, mettre la sortie ON, **observer** le courant affiché.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Brancher le montage **avant** de régler la tension.
> - Laisser la limite de courant **au maximum**.
> - Inverser le **+** et le **−**.

### Vérifie

1. Une LED avec sa résistance consomme 15 mA. Quelle limite de courant règles-tu ?
2. Le voyant CC s'allume dès que tu branches : que penses-tu ?

??? success "Réponses"

    1. Environ **30 mA** (le double de la consommation attendue).
    2. La consommation **dépasse la limite** : probable **court-circuit** ou composant monté à l'envers. On coupe et on cherche l'erreur.

## 2. Le générateur de fonctions (GBF)

Le GBF **produit un signal** de forme choisie, que l'on envoie dans un montage et que l'on observe à l'oscilloscope.

| Réglage | Signification |
|---|---|
| **Forme** | sinusoïdale, carrée, triangulaire |
| **Fréquence** | nombre de périodes par seconde (Hz) |
| **Amplitude** | taille du signal (souvent en $U_{pp}$) |
| **Offset** (décalage) | tension continue ajoutée |
| **Rapport cyclique** | pour un signal carré, part du temps à l'état haut |

> [!WARNING] ⚠️ Attention
> La sortie du GBF a une **résistance de sortie** (50 Ω en général) : ne jamais la brancher directement sur une alimentation ou sur une tension.

### Manipulation guidée

1. Règle le GBF : **sinus, 1 kHz, 2 V crête à crête**.
2. Branche-le sur l'oscilloscope (voie 1, sonde ×1 ou ×10 déclarée).
3. Relève : période $T$ = \_\_\_\_\_\_ ms ; amplitude $U_{pp}$ = \_\_\_\_\_\_ V.
4. Passe en **signal carré** à 500 Hz : relève $T$ et le rapport cyclique.

??? success "Valeurs attendues"

    1. $T = \dfrac{1}{1000} = 1\,\mathrm{ms}$ ; $U_{pp} = 2\,\mathrm{V}$ (par exemple 1 V/DIV sur 2 carreaux).
    2. Signal carré à 500 Hz : $T = 2\,\mathrm{ms}$ ; rapport cyclique de 50 % par défaut.

> [!SUCCESS] 🧠 À retenir
> - Alimentation de labo : **tension et limite de courant réglées avant de brancher**.
> - Voyant CC allumé = **anomalie**.
> - GBF : forme, fréquence, amplitude, offset ; ne jamais le brancher sur une tension.
