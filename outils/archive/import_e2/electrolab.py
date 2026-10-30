"""Intègre les TP virtuels ElectroLab dans les fiches de cours et de TP des 3 années :
« à faire AVANT le TP réel ». Les TP existants (menu TP ▾ d'ElectroLab, 39 TP à correction automatique)
sont proposés ; ElectroLab lui-même n'est jamais modifié.
Usage : python3 electrolab.py <racine>   — appelé par regenerer.sh après le nettoyage."""
import glob, json, re, sys
from pathlib import Path

URL = 'https://yahnlp.github.io/ElectroLab/'
CAT = json.load(open(Path(__file__).resolve().parents[1] / 'electrolab-sujets' / 'catalogue.json', encoding='utf-8'))

# (année, séance) -> TP ElectroLab (identifiants du catalogue)
TPS = {
 ('seconde', 'S01'): ['ohm', 'assoc', 'puissance'], ('seconde', 'S02'): ['led'], ('seconde', 'S03'): ['assoc'],
 ('seconde', 'S05'): ['test'], ('seconde', 'S06'): ['led'], ('seconde', 'S12'): ['test', 'ohm', 'osc_lect'],
 ('seconde', 'S13'): ['uart'], ('seconde', 'S15'): ['i2c'], ('seconde', 'S17'): ['dep2'],
 ('premiere', 'S04'): ['ne555'], ('premiere', 'S05'): ['osc_lect', 'signaux', 'osc_carre', 'la_intro', 'i2c', 'spi'],
 ('premiere', 'S12'): ['transistor', 'relais', 'portes', 'filtre'], ('premiere', 'S13'): ['filtre', 'rc'],
 ('premiere', 'S14'): ['dep1', 'dep2'], ('premiere', 'S11'): [],
 ('terminale', 'S01'): ['signaux', 'osc_lect', 'osc_ac'], ('terminale', 'S03'): ['transfo', 'redress', 'filtrage', 'regul'],
 ('terminale', 'S11'): ['ne555', 'regul'], ('terminale', 'S12'): ['diviseur', 'dep1', 'dep2'], ('terminale', 'S13'): ['dep1'],
 ('terminale', 'S14'): ['ne555', 'dep2'], ('terminale', 'S15'): ['dep3'], ('terminale', 'S17'): ['dep1', 'dep_log'],
}
MARQUE = '🖥️ TP virtuel ElectroLab'


def tp_ligne(i):
    t = CAT[i]
    return f"> - **{t['title']}** ({t['duration']}, {t['level'].strip('()')})"


def bloc(ids, tp_reel=True):
    titre = f"{MARQUE} : à faire avant le TP réel" if tp_reel else f"{MARQUE} : pour t'entraîner"
    lignes = [f"> [!TIP] {titre}",
              f"> Ouvre [ElectroLab]({URL}), menu **TP ▾**, puis choisis :"]
    lignes += [tp_ligne(i) for i in ids]
    lignes += ["> ", "> Le simulateur corrige automatiquement et ne risque pas d'abîmer le matériel : "
               "**réussis d'abord le TP virtuel, puis refais la manipulation sur le matériel réel.** "
               "Mode d'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md)."]
    return '\n'.join(lignes)


def main(root):
    docs = Path(root) / 'docs'
    n = 0
    for (y, s), ids in TPS.items():
        if not ids: continue
        for d in glob.glob(f'{docs}/{y}/{s}-*'):
            for fn, reel in (('01-cours.md', False), ('02-tp.md', True), ('02-tp-1.md', True)):
                f = Path(d) / fn
                if not f.exists(): continue
                t = f.read_text(encoding='utf-8')
                if MARQUE in t: continue
                lignes = t.split('\n')
                for i, l in enumerate(lignes):
                    if l.startswith('# '):
                        lignes[i + 1:i + 1] = ['', *bloc(ids, reel).split('\n'), '']
                        f.write_text('\n'.join(lignes), encoding='utf-8'); n += 1
                        break
    print('TP ElectroLab intégrés dans', n, 'fiches')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
