# 📘 Lire une datasheet (fiche technique)

## 🤔 À ton avis ?

Tu veux remplacer un régulateur grillé. Il est écrit « 7805 » dessus. Comment savoir **combien de courant** il supporte, **quelle tension d'entrée** maximale et **comment le brancher** ?

??? question "Réponse"
    On ouvre sa **datasheet** : la fiche technique du fabricant. Elle contient **toutes** les valeurs garanties. On la trouve en tapant la référence du composant suivie de « datasheet » dans un moteur de recherche (de préférence sur le site du fabricant).

## 1. Où trouver quoi dans une datasheet

| Section (en anglais) | Ce qu'on y trouve | À quoi ça sert |
|---|---|---|
| **Features / Description** | Résumé : à quoi sert le composant | Vérifier que c'est le bon |
| **Pin configuration** | Brochage (numéro et nom de chaque broche) | Le câbler sans erreur |
| **Absolute maximum ratings** | Limites à **ne jamais dépasser** | Ne pas le détruire |
| **Recommended operating conditions** | Plage de fonctionnement normal | Bien l'utiliser |
| **Electrical characteristics** | Valeurs **garanties** (min / typ / max) | Calculer les composants autour |
| **Typical characteristics (courbes)** | Comportement en fonction de la température, du courant… | Aller plus loin |
| **Package / mechanical data** | Dimensions du boîtier | Choisir l'empreinte KiCad |

> [!TIP] 💡 En clair
> « **Absolute maximum** » = au-delà, le composant **casse**. « **Recommended** » = ce qu'il faut viser **en fonctionnement normal**. On calcule toujours avec les valeurs **recommandées**, jamais avec les maximums.

## 2. Min, typ, max : comment lire une valeur

Pour chaque grandeur, la datasheet donne trois colonnes : **Min**, **Typ** (typique) et **Max**. Les valeurs **garanties** sont min et max ; la valeur « typique » est ce qu'on mesure **en général**, sans garantie.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Utiliser la valeur typique pour un calcul de sécurité : il faut prendre le **cas le plus défavorable**.
> - Confondre la tension **maximale absolue** avec la tension **de fonctionnement**.
> - Oublier que les valeurs sont données pour une **température précise** (souvent 25 °C).

## 3. Mini-lexique anglais

| Anglais | Français |
|---|---|
| Supply voltage ($V_{CC}$) | Tension d'alimentation |
| Input / Output voltage | Tension d'entrée / de sortie |
| Output current | Courant de sortie |
| Quiescent current | Courant consommé à vide |
| Dropout voltage | Chute de tension minimale (entrée − sortie) |
| Operating temperature | Température de fonctionnement |
| Thermal resistance | Résistance thermique |
| Forward voltage ($V_{F}$) | Tension directe (diode, LED) |
| Collector current ($I_{C}$) | Courant de collecteur |
| Current gain ($h_{FE}$) | Gain en courant |

## 4. Exercices : trois composants

Ouvre la datasheet de chaque composant (site du fabricant) et complète. Les valeurs peuvent légèrement varier selon le fabricant : note **lequel** tu as lu.

### Exercice 1 : le régulateur 7805
1. Quelle est la tension de sortie typique ? Entre quelles valeurs est-elle garantie ?
2. Quelle est la tension d'entrée maximale absolue ?
3. Quelle est la chute de tension minimale (dropout) ?
4. Avec $V_{in} = 9\,\mathrm{V}$ et un courant de 300 mA, calcule la puissance dissipée, puis $T_{j}$ si $R_{\theta ja} = 65\,°\mathrm{C/W}$ et $T_{amb} = 25\,°\mathrm{C}$.

??? success "Valeurs attendues"

    1. 5 V typique, garantie de **4,8 V à 5,2 V** (à 25 °C).
    2. **35 V**.
    3. Environ **2 V** : il faut au moins 7 V en entrée pour garder 5 V en sortie.
    4. $P = (9 - 5) \times 0{,}3 = 1{,}2\,\mathrm{W}$ ; $T_{j} = 25 + 1{,}2 \times 65 = 103\,°\mathrm{C}$, très proche de la limite de 105 °C exploitable : **radiateur recommandé**.

### Exercice 2 : le transistor BC547
1. Quelle est la tension $V_{CE}$ maximale ? Le courant de collecteur maximal ?
2. Entre quelles valeurs se situe le gain $h_{FE}$ ? Pourquoi une plage aussi grande ?
3. Quelle tension $V_{CE(sat)}$ obtient-on quand le transistor est saturé ?
4. Pour piloter une LED à 20 mA, quel courant de base minimal faut-il avec $h_{FE} = 110$ (cas le plus défavorable) ?

??? success "Valeurs attendues"

    1. $V_{CEO}$ = **45 V** ; $I_{C}$ max = **100 mA**.
    2. Environ **110 à 800** selon le groupe (A, B, C) : la fabrication ne contrôle pas ce gain précisément, d'où la plage large.
    3. Environ **0,2 V** (typique), au maximum environ 0,6 V.
    4. $I_{B} = \dfrac{20\,\mathrm{mA}}{110} \approx 0{,}18\,\mathrm{mA}$ ; en pratique, on prévoit 2 à 3 fois plus pour être sûr de saturer.

### Exercice 3 : le circuit intégré NE555
1. Quelle est la plage de la tension d'alimentation ?
2. Quel courant de sortie maximal peut-il fournir ?
3. Quelle formule donne la fréquence en mode astable ?
4. Avec $R_{a} = 10\,\mathrm{k\Omega}$, $R_{b} = 68\,\mathrm{k\Omega}$ et $C = 10\,\mathrm{\mu F}$, calcule $f$.

??? success "Valeurs attendues"

    1. Environ **4,5 V à 16 V** (selon le fabricant).
    2. Environ **200 mA** (il peut commander une LED directement).
    3. $f = \dfrac{1{,}44}{(R_{a} + 2R_b) \times C}$.
    4. $f = \dfrac{1{,}44}{146\,000 \times 10 \times 10^{-6}} \approx 0{,}99\,\mathrm{\mathrm{\mathrm{Hz}}}$.

> [!SUCCESS] 🧠 À retenir
> - La datasheet est **le document de référence** : pas de blog ni de forum à la place.
> - On lit toujours : **brochage**, **limites absolues**, **caractéristiques électriques** (cas le plus défavorable).
> - On vérifie que la **référence exacte** et le **fabricant** correspondent au composant dont on dispose.
