"""Convertit les blocs de code « formule texte » des cours en formules LaTeX (KaTeX).
Usage : python3 formules.py <racine_depot> [--dry]
Chaque ligne est validée par KaTeX (node) ; une ligne non convertible reste en texte.
"""
import json, re, subprocess, sys, glob
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fences

REPO = Path(sys.argv[1]); DRY = '--dry' in sys.argv
UNITS = ['kΩ', 'MΩ', 'Ω', 'mV', 'kV', 'V', 'mA', 'µA', 'A', 'kHz', 'MHz', 'Hz', 'mW', 'kW', 'W', 'ms', 'µs', 'ns', 's', 'nF', 'µF', 'pF', 'F', 'mH', 'µH', 'H', '°C', '%', 'kbit/s', 'bit/s', 'Mo', 'Ko', 'ko', 'h', 'min', 'm', 'mm', 'cm', 'km']
UNITS.sort(key=len, reverse=True)
UN = '|'.join(re.escape(u) for u in UNITS)
NAMED = {'Vcc': r'V_{cc}', 'VCC': r'V_{cc}', 'Vdd': r'V_{dd}', 'Vin': r'V_{in}', 'Vout': r'V_{out}', 'Vref': r'V_{ref}', 'Vf': r'V_F', 'VF': r'V_F', 'IF': r'I_F', 'If': r'I_F',
         'Rled': r'R_{\mathrm{LED}}', 'Iled': r'I_{\mathrm{LED}}', 'Vled': r'V_{\mathrm{LED}}', 'Req': r'R_{eq}', 'Rth': r'R_{th}', 'Ptot': r'P_{tot}', 'Itot': r'I_{tot}', 'Utot': r'U_{tot}'}
SYM = [('−', '-'), ('–', '-'), ('×', r' \times '), ('÷', r' \div '), ('·', r' \cdot '), ('≈', r' \approx '), ('≠', r' \neq '), ('≤', r' \leq '), ('≥', r' \geq '), ('±', r' \pm '),
       ('→', r' \to '), ('²', '^2'), ('³', '^3'), ('√', r'\sqrt'), ('µ', r'\mu '), ('✓', r' \;\checkmark'), ('✔', r' \;\checkmark'), ('Ω', r'\Omega')]
NUM = r'\d+(?:[  ]\d{3})*(?:,\d+)?'
ATOM = rf'(?:\((?:[^()]|\([^()]*\))*\)|{NUM}(?:\s?(?:{UN}))?|[A-Za-z]+(?:_[A-Za-z0-9]+)?\d*(?:\^\d|[²³])?)'


def conv_atoms(s, store):
    # fractions a / b
    pat = re.compile(rf'({ATOM})\s*/\s*({ATOM})')
    while True:
        m = pat.search(s)
        if not m: break
        a, b = m.group(1), m.group(2)
        strip = lambda x: x[1:-1] if x.startswith('(') and x.endswith(')') else x
        store.append(r'\dfrac{' + basic(strip(a)) + '}{' + basic(strip(b)) + '}')
        s = s[:m.start()] + f'§{len(store)-1}§' + s[m.end():]
    return s


def basic(s):
    s = re.sub(r'√\s*\(((?:[^()]|\([^()]*\))*)\)', lambda m: '«R»' + m.group(1) + '«E»', s)
    s = re.sub(r'√\s*(\d[\d,\.]*)', lambda m: '«R»' + m.group(1) + '«E»', s)
    s = re.sub(r'\b([A-Za-z])_([A-Za-z]+),([A-Za-zÀ-ÿ]+)', r'\1_{\\mathrm{\2,\3}}', s)
    s = re.sub(r'_{3,}', '§B§', s)
    s = re.sub(rf'({NUM})\s*({UN})(?![A-Za-zΩµ])', lambda m: m.group(1).replace(' ', r'\,') + r'\,\mathrm{' + m.group(2).replace('Ω', r'\Omega ').replace('µ', r'\mu ').replace('%', r'\%') + '}', s)
    s = re.sub(r'(?<=\d) (?=\d{3}\b)', r'\\,', s)
    s = re.sub(r'(\d),(\d)', r'\1{,}\2', s)
    s = re.sub(r'\b([A-Za-z]+)\b', lambda m: NAMED.get(m.group(1), m.group(0)), s)
    s = re.sub(r'\b([A-Za-z])_([A-Za-z]+)\b', r'\1_{\\mathrm{\2}}', s)
    s = re.sub(r'\b([A-Za-z])_(\d+)\b', r'\1_{\2}', s)
    s = re.sub(r'\b([RCLIUVPQfT])(\d{1,2})\b', r'\1_{\2}', s)
    for a, b in SYM: s = s.replace(a, b)
    return s


def tex(line):
    s = line.strip()
    if not re.search(r'[=≈]', s): return None
    # trop de mots : c'est du texte
    words = re.findall(r'[A-Za-zÀ-ÿ]{4,}', re.sub(r'_[A-Za-z]+(,[A-Za-zÀ-ÿ]+)?', '', re.sub(rf'\b({"|".join(NAMED)})\b', '', s)))
    words = [w for w in words if w not in ('Vcc', 'VCC', 'Rled', 'Iled')]
    if len(words) > 0 or len(s) > 90 or ':' in s or '|' in s: return None
    store = []
    s2 = conv_atoms(s, store)
    s2 = basic(s2)
    s2 = re.sub(r'§(\d+)§', lambda m: store[int(m.group(1))], s2)
    s2 = s2.replace('«R»', r'\sqrt{').replace('«E»', '}')
    s2 = s2.replace('§B§', r'\underline{\hspace{2.5em}}')
    s2 = re.sub(r'\s+', ' ', s2).strip()
    return s2


def classify_block(b):
    if re.search(r'[┌╔│─]|→ →|←', b): return False
    ls = [l for l in b.split('\n') if l.strip()]
    return bool(ls) and any(re.search(r'[=≈]', l) for l in ls)


def main():
    cands = []  # (file, span, lines)
    for f in sorted(glob.glob(str(REPO / 'docs/*/*/*.md'))):
        if '/annexes/' in f: continue
        t = Path(f).read_text(encoding='utf-8')
        for m in fences.finditer(t):
            if classify_block(m.group(1)): cands.append((f, m.span(), m.group(1)))
    lines = sorted({tex(l) for _, _, b in cands for l in b.split('\n') if tex(l)})
    node = r"""const k=require('/tmp/kt/package'); const L=JSON.parse(require('fs').readFileSync(0,'utf8')); const bad=[];
for(const s of L){try{k.renderToString(s,{throwOnError:true,strict:'ignore'})}catch(e){bad.push(s)}} console.log(JSON.stringify(bad))"""
    bad = set(json.loads(subprocess.run(['node', '-e', node], input=json.dumps(lines), capture_output=True, text=True).stdout or '[]'))
    print('blocs candidats', len(cands), '| lignes formule', len(lines), '| invalides', len(bad))
    files = {}
    done = 0
    for f, span, b in cands:
        out = []; ok = False; kept_text = []
        ls = b.split('\n')
        conv = [(l, tex(l)) for l in ls]
        if not any(c and c not in bad for _, c in conv): continue
        # bloc 100 % formules -> aligned
        if all((not l.strip()) or (c and c not in bad) for l, c in conv):
            rows = [c.replace('=', '&=', 1) if '=' in c else c for _, c in conv if c]
            rep = '$$\n\\begin{aligned}\n' + ' \\\\\n'.join(rows) + '\n\\end{aligned}\n$$' if len(rows) > 1 else f'$${rows[0].replace("&=", "=")}$$'
        else:
            parts = []
            for l, c in conv:
                if not l.strip(): parts.append(''); continue
                parts.append(f'$${c}$$' if c and c not in bad else l.strip() + '  ')
            rep = '\n'.join(parts)
            # texte pur autour : garder un seul bloc compréhensible
        files.setdefault(f, []).append((span, rep)); done += 1
    for f, reps in files.items():
        t = Path(f).read_text(encoding='utf-8')
        for (a, b), r in sorted(reps, reverse=True): t = t[:a] + r + t[b:]
        if not DRY: Path(f).write_text(t, encoding='utf-8')
    print('blocs convertis', done, 'dans', len(files), 'fichiers')


main()
