"""Met en notation mathématique les puissances restées en texte (2^10, e^(−λt), 10⁻⁵, h⁻¹)."""
import glob, re, sys

SUP = {'⁻': '-', '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}
SUPS = ''.join(SUP)


def sup(s): return ''.join(SUP[c] for c in s)


def inner(s): return s.replace('−', '-').replace('λ', r'\lambda ').replace('×', r'\times ').strip()


def conv(l):
    if '$' in l or l.lstrip().startswith(('![', '#!')): return l
    parts = re.split(r'(!\[[^\]]*\]\([^)]*\)|`[^`]*`|\]\([^)]*\))', l)
    for k in range(0, len(parts), 2):
        s = parts[k]
        s = re.sub(r'(\d+(?:,\d+)?)\s*[×x]\s*10([' + SUPS + r']+)', lambda m: '$' + m.group(1).replace(',', '{,}') + r'\times 10^{' + sup(m.group(2)) + '}$', s)
        s = re.sub(r'(?<![\w$])10([' + SUPS + r']+)', lambda m: '$10^{' + sup(m.group(1)) + '}$', s)
        s = re.sub(r'\b([a-zA-Zλ])([' + SUPS + r']+)', lambda m: '$\\mathrm{' + m.group(1) + '}^{' + sup(m.group(2)) + '}$' if m.group(1) in 'h' else m.group(0), s)
        s = re.sub(r'\be\^\(([^)]*)\)', lambda m: '$e^{' + inner(m.group(1)) + '}$', s)
        s = re.sub(r'\b(e|\d+)\^([A-Za-z0-9])\b', lambda m: '$' + m.group(1) + '^{' + m.group(2) + '}$', s)
        parts[k] = s
    return ''.join(parts)


def fix(text):
    L = text.split('\n'); fence = False; math = False; out = []
    for l in L:
        if re.match(r'^\s*```', l): fence = not fence; out.append(l); continue
        if l.strip() == '$$': math = not math; out.append(l); continue
        out.append(l if fence or math else conv(l))
    return '\n'.join(out)


if __name__ == '__main__':
    n = 0
    for f in glob.glob(sys.argv[1] + '/docs/*/*/*.md'):
        t = open(f, encoding='utf-8').read(); u = fix(t)
        if u != t: open(f, 'w', encoding='utf-8').write(u); n += 1
    print('fichiers avec puissances converties', n)
