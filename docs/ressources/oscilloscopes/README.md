# 🔭 Fiches oscilloscopes

> Deux fiches d'utilisation illustrées pour **maîtriser** les oscilloscopes du laboratoire, et **un TP** qui fonctionne avec les deux.

## Quel oscilloscope as-tu devant toi ?

| | **OWON SDS5032E(V)** | **RIGOL DS1104Z (Plus)** |
|---|---|---|
| Voies | **2** | **4** |
| Bande passante | 30 MHz | 100 MHz |
| Fiche | [🔭 Fiche OWON](owon-sds5032e.md) | [🔭 Fiche RIGOL](rigol-ds1104z.md) |
| Réglage vertical | **2 jeux** de boutons (un par voie) | **1 jeu** de boutons, agit sur la **voie sélectionnée** |
| Réglage automatique | **Autoset** | **AUTO** |
| Choisir une option de menu | touches **H1 à H5** (sous l'écran) et **F1 à F5** (à droite) | touches à **droite de l'écran** + **bouton multifonction** |
| Mesures | **Measure** (8 mesures au plus) | **Measure** (5 mesures en même temps, **statistiques**) |
| Curseurs | **Cursor** | **Cursor** |
| Capture unique | **Single** | **SINGLE** |
| Sauvegarde d'image | **Save** → Image, en **BMP** sur clé USB (ou touche **Copy**) | touche **Quick Print** (clé USB en **FAT32**) ou **Storage** |

## Les mêmes gestes sur les deux appareils

| Je veux… | OWON SDS5032E | RIGOL DS1104Z |
|---|---|---|
| **Tout remettre à zéro** | Utility → Function → Adjust → *Default* | Storage → *Default* |
| **Régler la sonde** | interrupteur 10X **et** MENU CH1 → *Probe* X10 | interrupteur 10X **et** CHx → *Probe* 10X |
| **Afficher un signal automatiquement** | **Autoset** | **AUTO** |
| **Changer la sensibilité** | **VOLTS/DIV** de la voie | **SCALE** vertical (voie sélectionnée) |
| **Changer la base de temps** | **SEC/DIV** | **SCALE** horizontal |
| **Stabiliser l'image** | **TRIG LEVEL**, touche **50 %** | bouton **LEVEL** |
| **Passer en couplage AC** | MENU CH1 → *Coupling* → AC | CHx → *Coupling* → AC |
| **Figer l'écran** | **Run/Stop** | **RUN/STOP** |
| **Capturer une seule fois** | **Single** | **SINGLE** |
| **Mesurer automatiquement** | **Measure** → *Add* | **Measure** |
| **Mesurer avec des curseurs** | **Cursor** | **Cursor** |
| **Compenser la sonde** | sortie 5 V / 1 kHz + borne de masse | sortie de compensation + borne de masse (à côté) |

## Les cinq règles d'or (valables pour tous les oscilloscopes)

1. **Interrupteur de sonde et menu de la voie** : **même coefficient**.
2. **Compense** la sonde à chaque changement de sonde ou de voie.
3. **Une seule masse** : les pinces de masse sur le **même point** du circuit.
4. **Lis V/div et s/div** avant de lire le tracé.
5. **Stabilise** d'abord (déclenchement), **mesure** ensuite.

## Le TP qui accompagne les fiches

> [!TIP] 🧪 [TP « Passeport oscilloscope » : 13 missions](tp-passeport-oscilloscope.md)
> Un parcours de prise en main **progressif**, qui se fait avec l'un ou l'autre des deux oscilloscopes, avec un générateur de fonctions (GBF).

## Où ces fiches sont-elles utilisées ?

- **Seconde** : prise en main de l'oscilloscope (S12).
- **Première** : tests et mesures avancés (S05).
- **Terminale** : TP « circuit fourni » (S01).
- **Parcours « L'essentiel en 1 an »** : semaine 3 (GBF et oscilloscope), puis semaines 6, 7, 9 et 13.
