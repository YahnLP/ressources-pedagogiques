# 🎓 GUIDE ÉLÈVE : Création et Gestion de son Portfolio GitHub

Ce guide vous accompagne de la création de votre compte jusqu'à la maîtrise des commandes de rédaction. En BTS SIO, votre GitHub est votre **vitrine professionnelle**.

---

## 1. Création et Paramétrage du Compte

1. **Inscription :** Rendez-vous sur [github.com](https://github.com/).
2. **Identité :** Choisissez un pseudo professionnel (ex: `Jules-Dupont-SISR`).
3. **Nouveau Dépôt :** Cliquez sur **"+" > New repository**.
* Nom : `Mon-Portfolio-SISR`.
* Visibilité : **Public** (indispensable pour que vos professeurs voient votre travail sans licence payante).
* Initialisation : Cochez **"Add a README file"**.


4. **Connexion SSH :** Pour ne pas taper votre mot de passe à chaque fois :
* Générez une clé sur votre PC via le terminal : `ssh-keygen -t ed25519 -C "votre-email@exemple.com"`.
* Copiez le contenu du fichier `.pub` généré dans vos **Settings > SSH and GPG keys** sur GitHub.



---

## 2. Création de l'arborescence (En local)

Ouvrez votre terminal dans votre dossier de travail et créez la structure demandée pour le **Bloc 2** :

```bash
# Création des dossiers de phase
mkdir Phase1-Fondamentaux Phase2-Services-Reseau Phase3-Windows-Server

# Création des premières fiches de TP
touch Phase1-Fondamentaux/A1-bloc2-S1-Hardware.md
touch Phase1-Fondamentaux/A1-bloc2-S3-OS-NTFS.md

```

---

## 3. Le cycle Git : Enregistrer et Publier

Apprenez par cœur ces trois étapes. Si vous sautez une étape, votre travail ne sera pas en ligne.

* **ÉTAPE 1 : Indexer**
`git add .` (Le point signifie "tout ce qui a changé")
* **ÉTAPE 2 : Valider**
`git commit -m "Ajout du compte rendu S3 sur le NTFS"`
* **ÉTAPE 3 : Pousser**
`git push origin main`

---

## 4. Guide de rédaction : Les commandes Markdown

Le Markdown est le langage utilisé pour rédiger vos fiches de TP. Voici les commandes essentielles pour une mise en forme professionnelle :

### Structure du texte

| Résultat | Syntaxe à taper |
| --- | --- |
| **Titre Principal** | `# Titre du TP` |
| **Sous-titre** | `## Objectifs de la séance` |
| **Texte en gras** | `**Ce texte sera en gras**` |
| **Texte en italique** | `*Ce texte sera en italique*` |

### Listes et Liens

* **Liste à puces :** Utilisez une étoile `*` ou un tiret `-` au début de la ligne.
* **Liste numérotée :** Utilisez `1.`, `2.`, etc.
* **Insérer un lien :** `[Texte du lien](URL_du_site)`
* **Insérer une image :** `![Légende](chemin/vers/image.png)`

### Éléments Techniques (SISR)

* **Bloc de code (Commandes Cisco/Linux) :**
Encadrez vos commandes avec trois "backticks" (`) :
```bash
# Exemple de commande Linux
sudo apt update && sudo apt upgrade

```


* **Citation ou Note :**
`> Ce texte apparaîtra comme une citation encadrée.`
* **Tableau de configuration :**
```text
| Nom PC | Adresse IP | Masque |
| :--- | :--- | :--- |
| SRV-AD-01 | 192.168.1.10 | 255.255.255.0 |

```



---

### 🛠️ Aide-mémoire : Dépannage rapide

* **Le terminal affiche `Everything up-to-date` ?** Vous avez probablement oublié d'enregistrer votre fichier (`Ctrl+S`) avant de faire le `git add .`.
* **Erreur de permission ?** Tapez `ssh -T git@github.com` pour vérifier que GitHub vous reconnaît.
* **Le texte est tout attaché ?** Laissez toujours une **ligne vide** entre deux paragraphes en Markdown.

---

**Souhaitez-vous que je génère une version de cette fiche au format code brut (Markdown) pour que vous puissiez la copier-coller directement sur votre propre GitHub de classe ?**