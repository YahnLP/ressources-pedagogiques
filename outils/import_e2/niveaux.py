"""Niveaux de difficulté : bandeaux « Approfondissement » (🔶) sur les contenus au-delà de l'essentiel E2,
version simplifiée des incertitudes (Terminale S02) et légende dans les README d'année.
Usage : python3 niveaux.py <racine>   — appelé par regenerer.sh après le nettoyage."""
import glob, re, sys
from pathlib import Path

BANDEAU = ("> [!NOTE] 🔶 Approfondissement\n"
           "> Cette partie va **au-delà de l'essentiel** attendu pour l'épreuve E2. À faire **après** le parcours essentiel "
           "(voir « L'essentiel en 1 an » en Terminale), si tu as du temps ou si tu vises plus haut.")

SIMPLIFIE = ("> [!NOTE] 🎚️ Deux niveaux pour cette partie\n"
             "> **Essentiel** : toute mesure a un doute. On l'estime avec la **précision donnée par le constructeur** de l'instrument, "
             "par exemple ±(0,5 % de la lecture + 2 chiffres) pour un multimètre. **Exemple** : lecture 5,02 V ; 0,5 % de 5,02 = 0,025 V ; "
             "2 chiffres de 0,01 V = 0,02 V ; marge ≈ 0,045 V, arrondie à 0,05 V → **(5,02 ± 0,05) V**. On conclut en comparant **toute la plage** "
             "« valeur ± marge » à la tolérance.\n"
             ">\n"
             "> **🔶 Approfondissement** : le calcul complet (type A, type B, incertitude combinée et élargie) qui suit.")

# (année, séance, fichier, titre de repère ou None pour le haut de fichier, texte)
CIBLES = [
    ('premiere', 'S09', '01-cours.md', None, BANDEAU), ('premiere', 'S09', '02-tp.md', None, BANDEAU),
    ('premiere', 'S11', '01-cours.md', None, BANDEAU), ('premiere', 'S11', '03-exercices.md', None, BANDEAU),
    ('premiere', 'S17', '01-cours.md', None, BANDEAU),
    ('premiere', 'S08', '03-exercices.md', '## 📐 EXERCICE 2', BANDEAU),
    ('terminale', 'S08', '01-cours.md', None, BANDEAU), ('terminale', 'S08', '02-tp.md', None, BANDEAU),
    ('terminale', 'S02', '01-cours.md', '## 4️⃣', SIMPLIFIE),
    ('terminale', 'S10', '03-exercices.md', '## 🟩 ATELIER B', BANDEAU),
    ('terminale', 'S10', '03-exercices.md', '## 🟨 ATELIER E', BANDEAU),
]
README_APPRO = {'premiere': ['S09', 'S11', 'S16', 'S17'], 'terminale': ['S08']}
LEGENDE = "> 🔶 = **approfondissement** : facultatif pour l'essentiel de l'épreuve E2 (à faire après le parcours essentiel)."


def inserer(texte, repere, bloc):
    lignes = texte.split('\n')
    for i, l in enumerate(lignes):
        if (repere is None and l.startswith('# ')) or (repere and l.startswith(repere)):
            return '\n'.join(lignes[:i + 1] + ['', *bloc.split('\n'), ''] + lignes[i + 1:])
    return None


def main(root):
    docs = Path(root) / 'docs'
    for y, s, fn, repere, bloc in CIBLES:
        d = glob.glob(f'{docs}/{y}/{s}-*')
        if not d: continue
        f = Path(d[0]) / fn
        if not f.exists(): continue
        t = f.read_text(encoding='utf-8')
        r = inserer(t, repere, bloc)
        if r is None: print('repère introuvable :', y, s, fn, repere); continue
        f.write_text(r, encoding='utf-8')
    for y, sess in README_APPRO.items():
        f = docs / y / 'README.md'
        t = f.read_text(encoding='utf-8')
        if LEGENDE in t: continue
        for s in sess:
            t = re.sub(rf'(\| \*\*{s}\*\* \| )', r'\1🔶 ', t)
        t = t.replace('## 📅 Progression\n', '## 📅 Progression\n\n' + LEGENDE + '\n', 1)
        f.write_text(t, encoding='utf-8')
    print('niveaux appliqués')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
