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

## 📖 Le cours en bref

??? question "🤔 À ton avis ?"
    Tu mesures 4,80 V sur une sortie censée être 5 V ± 5 %. Conforme ?

    **Réponse** : oui, **4,80 V est dans la plage [4,75 V ; 5,25 V]**. Mais si l'incertitude de ta mesure est de ± 0,1 V, la vraie valeur pourrait être 4,70 V : **hors tolérance**. On doit donc tenir compte de la **marge de mesure**.

### 1. La tolérance et la plage

« 5 V ± 5 % » signifie : **5 × 0,95 = 4,75 V** à **5 × 1,05 = 5,25 V**. Tout ce qui est dans cette plage est **conforme**.

### 2. La marge de mesure (version essentielle)

Aucun instrument n'est parfait. On estime la marge avec la **précision du constructeur**, par exemple « ± (0,5 % de la lecture + 2 chiffres) » pour un multimètre.

**Exemple** : lecture 5,02 V (résolution 0,01 V) : $0{,}5\,\% \times 5{,}02 = 0{,}025\,\mathrm{V}$ ; 2 chiffres = 0,02 V ; marge ≈ 0,05 V. Résultat : **(5,02 ± 0,05) V**.

> [!TIP] 💡 Règle de conclusion
> On compare **toute la plage** « valeur ± marge » à la tolérance :
> - toute la plage dedans → **conforme** ;
> - une partie dehors → **non garanti / à justifier** ;
> - toute la plage dehors → **non conforme**.

### 3. Le procès-verbal (PV)

Un PV est la **preuve écrite** d'un contrôle. Il contient :

1. **Identification** : carte, date, opérateur ;
2. **Instruments** utilisés (modèle, numéro de série, **étalonnage valide**) ;
3. **Méthode** (comment on a mesuré) ;
4. **Résultats** : attendu, mesuré, marge, verdict pour chaque test ;
5. **Conclusion** : conforme ou non, avec le critère ;
6. **Signature**.

### 4. La traçabilité

Un instrument est **comparé régulièrement** à une référence (étalonnage). Si son étalonnage est **périmé**, ses mesures ne sont plus valables dans un PV.

### Exercice guidé

Carte alimentée en 12 V : sortie 7805 mesurée à $(4{,}99 \pm 0{,}03)\,\mathrm{V}$, tolérance 5 V ± 5 %. Plage mesurée : 4,96 à 5,02 V, dans [4,75 ; 5,25] → **conforme**.

> [!WARNING] ⚠️ Erreurs fréquentes
> - Oublier l'**unité** ou la **tolérance** dans le PV.
> - Conclure « conforme » en comparant **seulement la valeur** et pas la plage avec sa marge.
> - Utiliser un instrument **hors étalonnage**.

## 📚 Pour approfondir : les séances à consulter

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
