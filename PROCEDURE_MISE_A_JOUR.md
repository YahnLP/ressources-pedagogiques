# Procédure de mise à jour — Site BAC PRO CIEL (ressources-pedagogiques)

Ce document explique comment ajouter du contenu, prévisualiser le site en local, et le publier sur GitHub Pages.
Il s'applique au site MkDocs situé à la racine du dépôt `ressources-pedagogiques` (dossier `docs/`, `mkdocs.yml`, `.github/workflows/mkdocs.yml`).

---

## 0. Installation initiale (une seule fois par PC)

Vous avez déjà fait cette étape pour le site BTS — c'est exactement la même chose.

```bash
# Se placer dans le dossier local du dépôt ressources-pedagogiques
cd chemin/vers/ressources-pedagogiques

# Créer un environnement Python dédié (recommandé)
python -m venv .venv
# Windows :
.venv\Scripts\activate
# macOS/Linux :
source .venv/bin/activate

# Installer les dépendances du site
pip install -r requirements.txt
```

---

## 1. Prévisualiser le site en local

Avant de pousser sur GitHub, prévisualisez toujours vos changements :

```bash
mkdocs serve
```

Puis ouvrez `http://127.0.0.1:8000/` dans un navigateur. La page se recharge automatiquement à chaque modification d'un fichier.

Pour vérifier qu'il n'y a pas d'erreur de configuration ou de lien cassé avant de publier :

```bash
mkdocs build --strict
```

Si cette commande échoue, ne poussez pas — corrigez d'abord l'erreur indiquée.

---

## 2. Règle d'or : ce qui est publié, ce qui ne l'est pas

Le site est **public**. Avant d'ajouter un fichier dans `docs/`, vérifiez :

| Type de document | Publié sur le site ? |
|---|---|
| Fiche de cours élève | ✅ Oui |
| Activité découverte / exercices (sans corrigé) | ✅ Oui |
| Fiche de TP | ✅ Oui |
| Grille d'évaluation | ✅ Oui |
| QCM (énoncé) | ✅ Oui |
| **Fiche enseignant** | ❌ Non — reste uniquement dans votre dossier source |
| **Corrections / corrigés / aide formateur** | ❌ Non — reste uniquement dans votre dossier source |

**En pratique :** tout fichier dont le nom contient `Enseignant`, `Correction`, `Corrige`, `Aide_Formateur` ne doit **pas** être copié dans `docs/`.

---

## 3. Ajouter une nouvelle semaine à un bloc existant (ex. E31 Année 1, S3)

1. Créer le dossier :
   ```
   docs/E31/Annee-1/Semaine-03/
   ```
2. Créer un fichier `.pages` dedans pour fixer l'ordre d'affichage, par exemple :
   ```yaml
   arrange:
       - README.md
       - 01-fiche-cours-eleve.md
       - 02-fiche-tp.md
   ```
3. Créer un `README.md` de présentation de la semaine (objectifs, compétences, durée) — copiez le modèle d'une semaine existante (`docs/E31/Annee-1/Semaine-01/README.md`) et adaptez-le.
4. Copier les fichiers élèves depuis votre dossier source (`BAC PRO Ciel/plan de formation/.../E31/Année 1/S3/`), **en excluant** les fiches enseignant et corrections (voir règle ci-dessus), et les renommer avec un préfixe numérique clair (`01-...`, `02-...`) pour contrôler l'ordre si vous n'utilisez pas `.pages`.
5. Mettre à jour `docs/E31/Annee-1/.pages` pour ajouter `Semaine-03` à la liste `arrange`.
6. Prévisualiser (`mkdocs serve`), vérifier, puis publier (étape 5 ci-dessous).

---

## 4. Ajouter un nouveau bloc (ex. E32, E2, E12)

1. Créer le dossier `docs/E32/Annee-1/` (même logique que E31).
2. Créer `docs/E32/.pages` avec un titre, par exemple :
   ```yaml
   title: "E32 - <intitulé du bloc>"
   arrange:
       - Annee-1
   ```
3. Ajouter `E32` à la liste `arrange` de `docs/.pages` (à la racine).
4. Reproduire la structure Semaine-XX comme au point 3.
5. Mettre à jour le tableau d'état dans `docs/index.md` (passer E32 de ⏳ à 🟢 dès qu'il y a du contenu en ligne).

---

## 5. Publier (envoyer les changements sur GitHub)

Le site se reconstruit et se publie **automatiquement** via GitHub Actions à chaque `push` sur la branche `main` (voir `.github/workflows/mkdocs.yml`). Il n'y a rien à faire côté GitHub Pages une fois que c'est activé (voir étape 6).

```bash
git add docs/ mkdocs.yml requirements.txt
git commit -m "Ajout S3 E31 Année 1"
git push origin main
```

Le déploiement prend 1 à 3 minutes. Vous pouvez suivre son avancement dans l'onglet **Actions** du dépôt GitHub :
`https://github.com/YahnLP/ressources-pedagogiques/actions`

Le site est visible à l'adresse :
`https://yahnlp.github.io/ressources-pedagogiques/`

---

## 6. Activer GitHub Pages (à faire une seule fois, lors de la mise en place initiale)

1. Aller sur `https://github.com/YahnLP/ressources-pedagogiques/settings/pages`
2. Dans **Build and deployment > Source**, choisir **GitHub Actions** (pas « Deploy from a branch »).
3. Pousser (`git push`) une première fois : le workflow `.github/workflows/mkdocs.yml` se déclenche et publie le site.

---

## 7. Checklist rapide avant chaque publication

- [ ] `mkdocs build --strict` ne renvoie aucune erreur
- [ ] Aucun fichier `Fiche_Enseignant` / `Correction` / `Corrige` dans `docs/`
- [ ] Le `.pages` du dossier parent liste bien la nouvelle semaine/le nouveau bloc
- [ ] `mkdocs serve` : la page s'affiche correctement, les liens internes fonctionnent
- [ ] Message de commit clair (ex. « Ajout S3 E31 Année 1 »)
