"""Met en forme les formules restées en texte dans les pages élèves (hors blocs de code).

- dans les formules déjà en LaTeX : exposants Unicode, π, σ, λ… -> commandes LaTeX ;
- dans le texte : formules en gras (**I = U / R**), indices (U_sortie), carrés (U²), racines (√3).
Usage : python3 inline.py <racine_depot>
"""
import glob, json, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from formules import tex

SUPD = {'⁻': '-', '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}
SUPS = ''.join(SUPD)
GREEK = {'π': r'\pi ', 'σ': r'\sigma ', 'λ': r'\lambda ', 'Δ': r'\Delta ', 'µ': r'\mu ', 'τ': r'\tau ', 'η': r'\eta ', 'ρ': r'\rho ', 'ω': r'\omega ', 'θ': r'\theta '}


def fixmath_plain(s):
    s = re.sub('([' + SUPS + ']+)·([' + SUPS + ']+)', lambda x: '^{' + ''.join(SUPD[c] for c in x.group(1)) + '{,}' + ''.join(SUPD[c] for c in x.group(2)) + '}', s)
    s = re.sub(r'\^\(([^()]*)\)', r'^{\1}', s)
    s = re.sub('([' + SUPS + ']+)', lambda x: '^{' + ''.join(SUPD[c] for c in x.group(1)) + '}', s)
    for k, v in GREEK.items(): s = s.replace(k, v)
    def chain(m):
        body = m.group(2)
        return m.group(1) + '_{' + (body if len(body) == 1 else '\\mathrm{' + body.replace('_', '\\_') + '}') + '}'
    s = re.sub(r'(?<![\\\w{])([A-Za-zσλΔ])_([A-Za-z0-9]+(?:_[A-Za-z0-9]+)*)(?![\w{])', chain, s)
    s = re.sub(r'(?<![\\A-Za-z])(kHz|MHz|GHz|Hz)(?![A-Za-z])', r'\\mathrm{\1}', s)
    s = re.sub(r'(?<![\\A-Za-z])ln\(', r'\\ln(', s)
    return s


def fixmath(m):
    parts = re.split(r'(\\text\{(?:[^{}]|\{[^{}]*\})*\})', m)
    return ''.join(p if i % 2 else fixmath_plain(p) for i, p in enumerate(parts))


def split_protect(l):
    return re.split(r'(!\[[^\]]*\]\([^)]*\)|`[^`]*`|\]\([^)]*\)|\$[^$]*\$|<[^>]+>)', l)


def tokens(s):
    s = re.sub(r'(?<![\w./\-])([A-Za-zσλΔ])_([A-Za-z0-9]),([a-zé]{1,8})\b', lambda m: '$' + m.group(1) + '_{' + m.group(2) + ',\\mathrm{' + m.group(3) + '}}$', s)
    LB = r'(?<![\w./\-])'; LA = r'(?![\w]|\.[A-Za-z])'
    s = re.sub(LB + r'([A-Za-zσλΔ])_([A-Za-z]{2,8})' + LA, lambda m: '$' + m.group(1) + '_{\\mathrm{' + m.group(2) + '}}$', s)
    s = re.sub(LB + r'([A-Za-z])_([A-Za-z0-9])' + LA, lambda m: '$' + m.group(1) + '_{' + m.group(2) + '}$', s)
    s = re.sub(r'(?<![A-Za-zÀ-ÿ])([A-Za-z])([²³])(?![A-Za-zÀ-ÿ])', lambda m: '$' + m.group(1) + '^{' + SUPD[m.group(2)] + '}$', s)
    s = re.sub(r'√\s*(\d+(?:,\d+)?|\([^)]*\)|[A-Za-z]{1,3}\b(?!\())', lambda m: '$\\sqrt{' + m.group(1).strip('()') + '}$', s)
    return s


def process(text, boldmap):
    out = []; fence = False; math = False
    for l in text.split('\n'):
        if re.match(r'^\s*```', l): fence = not fence; out.append(l); continue
        if fence: out.append(l); continue
        if l.strip() == '$$': math = not math; out.append(l); continue
        if math or l.strip().startswith('$$'): out.append(fixmath(l)); continue
        if l.lstrip().startswith('|') and l.count('|') > 2 and '$' not in l:
            cells = l.split('|')
            for ci in range(1, len(cells) - 1):
                key = cells[ci].strip().strip('*').strip()
                if '=' in key and boldmap.get(key): cells[ci] = ' $' + boldmap[key] + '$ '
            l = '|'.join(cells)
        parts = split_protect(l)
        for k in range(len(parts)):
            if k % 2 == 1:
                if parts[k].startswith('$'): parts[k] = fixmath(parts[k])
                continue
            s = parts[k]
            s = re.sub(r'_{3,}', lambda m: '\\_' * len(m.group(0)), s)
            s = re.sub(r'\*\*([^*\n]+)\*\*', lambda m: ('$' + boldmap[m.group(1)] + '$') if boldmap.get(m.group(1)) else m.group(0), s)
            parts[k] = tokens(s) if '$' not in s or True else s
        out.append(''.join(parts))
    return '\n'.join(out)


BADKEY = re.compile(r'[*°̄]|[^\x00-\u024F\u0370-\u03FF\u2000-\u2BFF]')


def candidates(text):
    c = set(); fence = False
    for l in text.split('\n'):
        if re.match(r'^\s*```', l): fence = not fence; continue
        if fence or ('$' in l and not l.lstrip().startswith('|')): continue
        for m in re.finditer(r'\*\*([^*\n]+)\*\*', l):
            inner = m.group(1)
            if '=' in inner and not BADKEY.search(inner):
                t = tex(inner)
                if t: c.add((inner, t))
        if l.lstrip().startswith('|'):
            for cell in l.split('|')[1:-1]:
                key = cell.strip().strip('*').strip()
                if '=' in key and len(key) < 90 and not BADKEY.search(key):
                    t = tex(key)
                    if t: c.add((key, t))
    return c


def main(root):
    files = [f for f in glob.glob(root + '/docs/*/*/*.md') if not f.endswith(('README.md', '04-simulateur.md'))]
    texts = {f: Path(f).read_text(encoding='utf-8') for f in files}
    cands = {}
    for t in texts.values(): cands.update(dict(candidates(t)))
    node = r"""const k=require('/tmp/kt/package'); const L=JSON.parse(require('fs').readFileSync(0,'utf8')); const bad=[];
for(const s of L){try{k.renderToString(s,{throwOnError:true,strict:'ignore'})}catch(e){bad.push(s)}} console.log(JSON.stringify(bad))"""
    bad = set(json.loads(subprocess.run(['node', '-e', node], input=json.dumps(list(cands.values())), capture_output=True, text=True).stdout or '[]'))
    boldmap = {k: v for k, v in cands.items() if v not in bad}
    n = 0
    for f, t in texts.items():
        u = process(t, boldmap)
        if u != t: Path(f).write_text(u, encoding='utf-8'); n += 1
    print('formules en gras', len(boldmap), '| fichiers modifiés', n)


if __name__ == '__main__':
    main(sys.argv[1])
