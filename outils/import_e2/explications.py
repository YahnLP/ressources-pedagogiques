"""Enrichit les cours (Seconde, Terminale) avec des explications, des questions de vérification et des synthèses.

Les contenus sont dans explications_donnees/<annee>_<seance>.py : ENTREES = [(titre, position, texte), ...]
  - titre    : début du titre de la section (ex. '## 2️⃣')
  - position : 'debut' (juste sous le titre) ou 'fin' (fin de la section, avant le séparateur)
Les aides qa(), apropos(), clair(), retenir(), erreurs() construisent les blocs.
"""
import glob, importlib.util, sys
from pathlib import Path


def qa(n, question, reponse):
    r = reponse.strip().split('\n')
    return f"**Q{n}.** {question}\n\n??? success \"Réponse\"\n" + '\n'.join('    ' + x for x in r) + "\n"


def verifie(*paires):
    """Bloc « Vérifie que tu as compris » : paires = (question, réponse)."""
    return "### ✅ Vérifie que tu as compris\n\n" + '\n'.join(qa(i + 1, q, r) for i, (q, r) in enumerate(paires))


def apropos(question, reponse):
    r = reponse.strip().split('\n')
    return f"### 🤔 À ton avis ?\n\n{question}\n\n??? question \"Voir une réponse possible\"\n" + '\n'.join('    ' + x for x in r) + "\n"


def clair(texte, titre="💡 En clair"):
    return f"> [!TIP] {titre}\n" + '\n'.join('> ' + x if x.strip() else '>' for x in texte.strip().split('\n')) + "\n"


def retenir(*points):
    return "> [!SUCCESS] 🧠 À retenir\n" + '\n'.join(f'> - {p}' for p in points) + "\n"


def erreurs(*points):
    return "> [!WARNING] ⚠️ Erreurs fréquentes\n" + '\n'.join(f'> - {p}' for p in points) + "\n"


def charger(root):
    res = []
    for f in sorted((Path(__file__).parent / 'explications_donnees').glob('*.py')):
        spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        res.append((f.stem, m.ENTREES))
    return res


def appliquer(root, nom, entrees):
    annee, seance = nom.split('_')[0], nom.split('_')[1].upper()
    d = Path(glob.glob(f'{root}/docs/{annee}/{seance}-*')[0]); f = d / '01-cours.md'
    L = f.read_text(encoding='utf-8').split('\n'); n = 0
    for titre, pos, texte in entrees:
        i = next((k for k, l in enumerate(L) if l.startswith(titre)), None)
        if i is None: print('titre introuvable', nom, titre); continue
        niv = len(titre) - len(titre.lstrip('#'))
        if pos == 'debut': j = i + 1
        else: j = next((k for k in range(i + 1, len(L)) if L[k].strip() == '---' or (L[k].startswith('#') and len(L[k]) - len(L[k].lstrip('#')) <= niv)), len(L))
        L[j:j] = [''] + texte.rstrip('\n').split('\n') + ['']; n += 1
    f.write_text('\n'.join(L), encoding='utf-8'); return n


def main(root):
    for nom, entrees in charger(root): print(nom, appliquer(root, nom, entrees))


if __name__ == '__main__':
    main(sys.argv[1])
