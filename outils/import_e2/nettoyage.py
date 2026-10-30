"""Nettoyage éditorial des pages élèves.

- retire l'en-tête d'identité (niveau, établissement, Nom/Prénom/Date/Binôme) ;
- retire le pied de fiche (date, auteur, contact, prochaine mise à jour) ;
- place les réponses dans des zones déroulables (pymdownx.details).
"""
import glob, re, sys

META = re.compile(r'^\s*\*\*(📅|✍️|📧|🔄)[^*]*\*\*')
IDENT = re.compile(r'^\s*(>\s*)?(\*\*)?\s*(Nom|Classe|Binôme)\s*:.*$')
MFR = re.compile(r'^\s*>.*(BAC Pro CIEL|Bac Pro CIEL).*(1ère année|MFR de Pontonx)')
REP = re.compile(r'^\s*(\*{1,2})?\s*(R[ée]ponses?)( attendues?)?\s*:?\s*(\*{1,2})?\s*:?\s*(.*)$')


def collapse_rules(L):
    out = []; i = 0; fence = False
    for l in L:
        if re.match(r'^\s*```', l): fence = not fence
        out.append(l)
    res = []
    fence = False
    for l in out:
        if re.match(r'^\s*```', l): fence = not fence
        if not fence and l.strip() == '---':
            j = len(res) - 1
            while j >= 0 and not res[j].strip(): j -= 1
            if j >= 0 and res[j].strip() == '---':
                del res[j + 1:]; continue
        res.append(l)
    return res


def header_footer(L):
    out = []; fence = False
    for i, l in enumerate(L):
        if re.match(r'^\s*```', l): fence = not fence
        if not fence and (META.match(l) or (i < 25 and (IDENT.match(l) or MFR.match(l)))): continue
        out.append(l)
    return out


def details(body, title):
    return ['', f'??? success "{title}"'] + ['    ' + x.rstrip() + ('  ' if k < len(body) - 1 else '') for k, x in enumerate(body)] + ['']


def reponses(L):
    out = []; i = 0; fence = False
    while i < len(L):
        l = L[i]
        if re.match(r'^\s*```', l):
            fence = not fence; out.append(l); i += 1; continue
        m = REP.match(l) if not l.startswith(('\t', '>', '|')) else None
        if m and (fence or not l.startswith(' ')):
            label = m.group(2) + (m.group(3) or '')
            body = [m.group(5)] if m.group(5).strip() else []
            j = i + 1
            if not body:
                while j < len(L) and not L[j].strip(): j += 1
            while j < len(L) and L[j].strip() and not L[j].startswith(('#', '---', '```', '|', '>', '![', '**R', '*R')): body.append(L[j]); j += 1
            if body and not any('___' in b for b in body) and sum(len(b) for b in body) < 900:
                title = 'Réponses' if label.lower().startswith('réponses') else 'Réponse'
                if fence:
                    k = j
                    while k < len(L) and not re.match(r'^\s*```', L[k]): k += 1
                    rest = [x for x in L[j:k]]
                    out.append('```'); out += details(body, title)
                    if any(x.strip() for x in rest): out.append('```'); out += rest + ['```']
                    fence = False; i = k + 1; continue
                if out and out[-1].strip(): out.append('')
                out += details(body, title)[1:]; i = j; continue
        out.append(l); i += 1
    return out


def fix(text):
    L = text.split('\n')
    L = header_footer(L); L = collapse_rules(L); L = reponses(L)
    t = re.sub(r'\n{3,}', '\n\n', '\n'.join(L))
    return t


if __name__ == '__main__':
    n = 0
    for f in glob.glob(sys.argv[1] + '/docs/*/*/*.md'):
        if f.endswith(('README.md', '04-simulateur.md')): continue
        t = open(f, encoding='utf-8').read(); u = fix(t)
        if u != t: open(f, 'w', encoding='utf-8').write(u); n += 1
    print('fichiers nettoyés', n)
