"""Première S18 : réponses aux questions de méthode de l'atelier DAT (le contenu du DAT dépend du projet de l'élève)."""
F = '03-exercices.md'
E = lambda t, l: ('premiere', 'S18', F, t, l, "Éléments de réponse")
ENTREES = [
    E('## Créer votre fichier DAT', [
        "**Q1** — Un DAT complet à 13 sections fait en général **15 à 25 pages** (une à deux pages par section, plus le schéma et la BOM) ; l'important est que **chaque section soit présente et renseignée**."]),
    E('### Tableau de repérage des fils', [
        "**Q2** — Deux fils qui se croisent **sans point plein** ne sont **pas reliés** (simple croisement). Une **jonction** se reconnaît au **point plein** à l'intersection. Il vaut mieux éviter les croisements en utilisant des étiquettes de net."]),
    E('### À remplir (ajouter toutes les lignes nécessaires)', [
        "**Q3** — Sites de recherche : **Mouser**, **Farnell**, **RS Components**, **Digi-Key**, **LCSC** (recherche par référence fabricant ou par désignation).  ",
        "**Q4** — La **référence fabricant (le modèle exact)** : elle permet de chercher un composant équivalent chez un autre fournisseur."]),
    E('## Échange de DAT entre binômes', [
        "**Q5** — Exemples d'améliorations prioritaires : schéma plus lisible (légende, repères), BOM complète (références fournisseur, quantités), section configuration sans mot de passe en clair, procédures numérotées et testables."]),
]
