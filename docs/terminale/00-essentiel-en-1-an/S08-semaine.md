# Semaine 8 : Tester et valider : protocole et procès-verbal

> **Durée** : 4 h · **Compétences E2 travaillées** : C11 · C03

## 🎯 Objectifs : à la fin de la semaine, je sais…

- Suivre un protocole de test et noter attendu / mesuré / verdict.
- Comparer une mesure et sa marge à une tolérance.
- Rédiger un PV clair (identification, instruments, résultats, conclusion).

## 🗓️ Déroulé

| Durée | Activité |
|---|---|
| 1 h | Tolérance, marge de mesure (version essentielle) et conformité |
| 1 h | Structure d'un PV, traçabilité des instruments |
| 1 h | TP : carte NE555 / 7805 (mesures et PV) |
| 1 h | Auto-test et correction |

## 📚 Ressources à utiliser

- [Terminale S02 – rapport de mesures et PV](../S02-rapport-de-mesures-pv-professionnel/01-cours.md)
- [Terminale S07 – validation et conformité](../S07-validation-conformite-pv-professionnel/01-cours.md)
- [Terminale S11 – TP carte NE555 / 7805](../S11-interpreter-document-mesures-carte/02-tp.md)

## ✅ Auto-test

1. Sortie 5 V ± 5 % : quelle plage est acceptable ?
2. Mesure $(5{,}02 \pm 0{,}05)\,\mathrm{V}$ : conforme ?
3. Mesure $(5{,}20 \pm 0{,}08)\,\mathrm{V}$ : conforme ?
4. Pourquoi indiquer l'instrument et son étalonnage ?
5. Un PV peut-il se terminer par « ça marche » ?

??? success "Réponses"
    1. De **4,75 V à 5,25 V**.
    2. **Oui** : la plage 4,97 à 5,07 V est dans la tolérance.
    3. **Non garanti** : la plage dépasse 5,25 V.
    4. Pour que la mesure soit **vérifiable** (traçabilité).
    5. **Non** : la conclusion compare le résultat à un **critère chiffré**.

## 📦 Livrable

PV complet d'une carte (tableau attendu / mesuré / verdict + conclusion).
