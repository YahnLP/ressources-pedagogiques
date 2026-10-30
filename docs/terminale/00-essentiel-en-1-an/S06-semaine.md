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

## 📚 Ressources à utiliser

- [Première S03 – PCB et routage](../../premiere/S03-kicad-pcb-editor-routage-pistes-vias/01-cours.md)
- [Première S04 – double face et Gerber](../../premiere/S04-pcb-double-face-metallisation/01-cours.md)
- [Terminale S06 – TP de bout en bout](../S06-flux-kicad-complet-schema-erc-pcb-drc/02-tp-de-bout-en-bout.md)
- [Seconde S04 – soudure et IPC](../../seconde/S04-soudure-a-l-etain-composants/01-cours.md)

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
