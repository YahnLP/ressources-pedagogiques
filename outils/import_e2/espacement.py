"""Ajoute les lignes vides exigées par Markdown : avant les listes et autour des blocs $$ ... $$."""
import glob, re, sys

LIST = re.compile(r'^(\s*)([-*+]|\d+[.)])\s+')


def fix(text):
    L = text.split('\n'); out = []; fence = False; math = False
    for i, l in enumerate(L):
        if re.match(r'^\s*(```|~~~)', l):
            fence = not fence; out.append(l); continue
        if fence: out.append(l); continue
        prev = out[-1] if out else ''
        if l.strip() == '$$':
            if not math:
                if prev.strip(): out.append('')
                math = True
            else:
                math = False
            out.append(l)
            if not math and i + 1 < len(L) and L[i + 1].strip(): out.append('')
            continue
        if math: out.append(l); continue
        m = LIST.match(l)
        if m and prev.strip() and not LIST.match(prev) and not prev.startswith((' ', '\t', '>', '|', '#', '<', '!', '---', '```')):
            out.append('')
        out.append(l)
    return '\n'.join(out)


if __name__ == '__main__':
    n = 0
    for f in glob.glob(sys.argv[1] + '/docs/*/*/*.md'):
        t = open(f, encoding='utf-8').read(); u = fix(t)
        if u != t: open(f, 'w', encoding='utf-8').write(u); n += 1
    print('fichiers ajustés', n)
