# Procédure de mise à jour du site

Le site est un projet **MkDocs Material** : le contenu est dans `docs/`, la configuration dans `mkdocs.yml`. Il est publié **automatiquement** sur GitHub Pages à chaque `push` sur `main` (`.github/workflows/mkdocs.yml`).

## 1. Prévisualiser en local

```bash
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build --strict # doit se terminer sans erreur avant de publier
```

## 2. Règle d'or : ce qui est publié

Le site est **public**.

| Type de document | Publié ? |
|---|---|
| Fiche de cours élève, fiche de TP, exercices sans corrigé | ✅ Oui |
| Annexes (aide-mémoire, fiches techniques, check-lists) | ✅ Oui |
| **Fiche enseignant, corrections, corrigés** | ❌ Non : jamais dans ce dépôt |

Avant d'ajouter un fichier, vérifier qu'il ne contient **aucune section « correction » ou « document enseignant »**.

## 3. Ajouter ou modifier une séance

Une séance = un dossier `docs/<année>/Sxx-titre/` avec `README.md`, `01-cours.md`, `02-tp.md`, éventuellement des annexes et un dossier `tp/` pour les fichiers ElectroLab. Le fichier `.pages` du dossier fixe l'ordre et les titres du menu. Ajouter la ligne de la séance dans le `README.md` de l'année.

## 4. Fichiers ElectroLab

Les exercices simulés sont générés par `outils/electrolab/generer.js` (ElectroLab n'est jamais modifié) :

```bash
node outils/electrolab/generer.js chemin/vers/ElectroLab .
```

## 5. Publier

```bash
git add docs/ mkdocs.yml
git commit -m "Message clair"
git push origin main
```

Le déploiement prend 1 à 3 minutes (onglet **Actions** du dépôt).
