# 🗂️ FICHE DE RÉFÉRENCE — AIDE-MÉMOIRE LCD I2C
## Commandes essentielles & guide de dépannage rapide

---

> **À conserver dans ton classeur et ton portfolio**
> *BAC PRO CIEL | Module E2 | S15*

---

## 📐 Câblage en un coup d'œil

| LCD I2C | Arduino UNO | Couleur conseillée |
|---|---|---|
| VCC | 5V | 🔴 Rouge |
| GND | GND | ⚫ Noir |
| SDA | A4 | 🔵 Bleu |
| SCL | A5 | 🟡 Jaune |

---

## 💻 Structure minimale d'un sketch LCD I2C

```cpp
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);   // Remplacer 0x27 par ton adresse

void setup() {
  lcd.init();
  lcd.backlight();
  // --- Écris ici ce que tu veux afficher au démarrage ---
}

void loop() {
  // --- Écris ici ce que tu veux afficher en boucle ---
}
```

---

## 🔧 Fonctions LCD — tableau récapitulatif

| Fonction | Syntaxe complète | Ce qu'elle fait |
|---|---|---|
| Initialiser | `lcd.init();` | Démarre le LCD — obligatoire dans setup() |
| Rétroéclairage ON | `lcd.backlight();` | Allume le rétroéclairage |
| Rétroéclairage OFF | `lcd.noBacklight();` | Éteint le rétroéclairage |
| Positionner curseur | `lcd.setCursor(col, ligne);` | Place le curseur avant d'écrire |
| Afficher texte | `lcd.print("Bonjour");` | Affiche une chaîne de caractères |
| Afficher nombre entier | `lcd.print(42);` | Affiche un entier |
| Afficher nombre décimal | `lcd.print(23.4, 1);` | Affiche avec 1 décimale |
| Effacer l'écran | `lcd.clear();` | Efface tout + curseur en (0,0) |
| Retour origine | `lcd.home();` | Curseur en (0,0) sans effacer |
| Caractère spécial | `lcd.print((char)223);` | Affiche le symbole ° |

---

## 📍 Carte des positions du LCD 16×2

```
Ligne 0 (haut)  →  Col : 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
Ligne 1 (bas)   →  Col : 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
```

**Exemples de setCursor :**

| Appel | Résultat |
|---|---|
| `lcd.setCursor(0, 0)` | Début de la ligne du haut |
| `lcd.setCursor(0, 1)` | Début de la ligne du bas |
| `lcd.setCursor(8, 0)` | Milieu de la ligne du haut |
| `lcd.setCursor(5, 1)` | 6ème caractère de la ligne du bas |

---

## 🐛 Guide de dépannage rapide

| Problème observé | Cause probable | Solution |
|---|---|---|
| Écran allumé mais rien ne s'affiche | Adresse I2C incorrecte | Lancer le sketch de scan I2C et corriger l'adresse |
| Écran allumé, carrés noirs sur ligne 1 | Contraste trop fort ou pas de code envoyé | Tourner le potentiomètre bleu, vérifier que `lcd.init()` est dans `setup()` |
| Écran éteint, pas de rétroéclairage | VCC ou GND non connecté | Vérifier le câblage alimentation |
| Caractères parasites ou décalés | `clear()` non appelé entre deux affichages | Appeler `lcd.clear()` ou compléter avec des espaces |
| Adresse 0x27 ne fonctionne pas | Certains modules ont l'adresse 0x3F | Remplacer `0x27` par `0x3F` dans la déclaration |
| Bibliothèque introuvable | Non installée | Outils → Gérer les bibliothèques → LiquidCrystal I2C (Frank de Brabander) |

---

## 🌡️ Rappel — Formule LM35

```
Valeur brute = analogRead(A0)           → 0 à 1023
Tension (V)  = valeurBrute × 5.0 / 1023.0
Température  = tension × 100.0          → en °C
```

---

## 🔗 Caractères spéciaux utiles

| Caractère | Code ASCII | Syntaxe Arduino |
|---|---|---|
| ° (degré) | 223 | `lcd.print((char)223);` |
| → (flèche droite) | 126 | `lcd.print((char)126);` |
| ← (flèche gauche) | 127 | `lcd.print((char)127);` |

---

*Aide-mémoire LCD I2C — BAC PRO CIEL | Module E2 | S15*
*À plastifier et afficher en atelier*
