#!/bin/sh
# Régénère les cours E2 (Seconde, Première, Terminale) depuis l'import initial.
# Usage : outils/import_e2/regenerer.sh   (depuis la racine du dépôt)
set -e
BASE=5f7a72e
python3 -I outils/illustrations-e2/render.py /tmp/figs
[ -d /tmp/sym ] || python3 -I outils/illustrations-e2/render.py /tmp/sym >/dev/null
for f in $(git ls-tree -r --name-only $BASE docs | grep -E "^docs/(seconde|premiere|terminale)/.*\.md$" | grep -v "/images/" | grep -vE "/(README|04-simulateur)\.md$"); do git checkout $BASE -- "$f"; done
git reset -q
python3 outils/import_e2/enrichir.py . /tmp/figs /tmp/sym
python3 outils/import_e2/formules.py .
python3 outils/import_e2/nettoyage.py .
python3 outils/import_e2/espacement.py .
python3 - <<'PY'
import glob, re
for f in glob.glob('docs/*/*/*.md'):
    L = open(f, encoding='utf-8').read().split('\n'); o = []
    for i, l in enumerate(L):
        if re.match(r'^\$\$.+\$\$\s*$', l):
            if o and o[-1].strip(): o.append('')
            o.append(l)
            if i + 1 < len(L) and L[i + 1].strip(): o.append('')
        else: o.append(l)
    t = '\n'.join(o)
    if t != '\n'.join(L): open(f, 'w', encoding='utf-8').write(t)
PY
