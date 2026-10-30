"""Ajoute, sous les exercices, les réponses en zones déroulables.

Chaque entrée : (année, séance, fichier, début du titre de l'exercice, lignes de réponse).
Règle de maintenance : tout exercice à compléter doit avoir ses réponses dans une zone déroulable.
"""
import glob, sys
from pathlib import Path

ENTREES = [
    ('seconde', 'S01', '01-cours.md', '### 🧮 Exercice 1', ["1. 12 000 Ω = 12 kΩ  ", "2. 4 700 Ω = 4,7 kΩ  ", "3. 560 Ω = 0,56 kΩ"]),
    ('seconde', 'S01', '01-cours.md', '### 🧮 Exercice 2', ["1. $I = \\dfrac{U}{R} = \\dfrac{12}{600} = 0{,}02\\,\\mathrm{A} = 20\\,\\mathrm{mA}$  ", "2. $U = R \\times I = 200 \\times 0{,}05 = 10\\,\\mathrm{V}$  ", "3. $R = \\dfrac{U}{I} = \\dfrac{9}{0{,}003} = 3\\,000\\,\\Omega = 3\\,\\mathrm{k\\Omega}$"]),
    ('seconde', 'S01', '01-cours.md', '### 🧮 Exercice 3', ["1. 4 700 Ω = 4,7 kΩ  ", "2. 0,025 A = 25 mA  ", "3. 2,2 MΩ = 2 200 000 Ω  ", "4. 150 mA = 0,15 A"]),
]


def main(root):
    for y, s, fn, titre, rep in ENTREES:
        d = Path(glob.glob(f'{root}/docs/{y}/{s}-*')[0]); f = d / fn
        L = f.read_text(encoding='utf-8').split('\n')
        i = next((k for k, l in enumerate(L) if l.startswith(titre)), None)
        if i is None: print('introuvable', y, s, titre); continue
        j = next((k for k in range(i + 1, len(L)) if L[k].strip() == '---' or L[k].startswith('#')), len(L))
        if any(l.startswith('??? success') for l in L[i:j]): continue
        L[j:j] = ['??? success "Réponses"'] + ['    ' + x for x in rep] + ['']
        f.write_text('\n'.join(L), encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1])
