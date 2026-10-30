"""Remplace diagrammes en texte, cadres et placeholders des cours par des figures/encadrés propres.
Usage : python3 enrichir.py <racine_depot> <dossier_png_figures> <dossier_png_symboles>
(idempotent sur un dossier restauré depuis l'import ; utilise fences.py)"""
import glob, re, sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fences

REPO = Path(sys.argv[1]); FIG = Path(sys.argv[2]); SYM = Path(sys.argv[3])
BOX = re.compile(r'[┌┐└┘├┤┬┴┼]')


def D(year, p): return Path(glob.glob(str(REPO / f'docs/{year}/{p}-*'))[0])


def q(src, dst):
    dst.parent.mkdir(exist_ok=True)
    Image.open(src).convert('RGBA').quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG).save(dst, optimize=True)


def replace_blocks(f, rules, d):
    t = f.read_text(encoding='utf-8'); n = 0
    for m in sorted(fences.finditer(t), key=lambda m: m.span()[0], reverse=True):
        b = m.body
        for pred, name, alt in rules:
            if pred(b):
                if name is None: r = alt
                else:
                    q(FIG / f'{name}.png', d / 'images' / (name.replace('_', '-') + '.png')); r = f'![{alt}](images/{name.replace("_", "-")}.png)'
                a, e = m.span(); t = t[:a] + r + t[e:]; n += 1; break
    f.write_text(t, encoding='utf-8'); return n


has = lambda *s: (lambda b: all(x in b for x in s))
RE = re.compile(r'\s*\[ILLUSTRATION')


def box_to_table(b):
    out = []; rows = []
    def flush():
        nonlocal rows
        if rows:
            out.append('| ' + ' | '.join(rows[0]) + ' |'); out.append('|' + '---|' * len(rows[0]))
            for r in rows[1:]: out.append('| ' + ' | '.join(r) + ' |')
            out.append(''); rows = []
    for l in b.split('\n'):
        if re.match(r'^\s*[┌├└][─┬┼┴┐┤┘]+\s*$', l): continue
        if l.strip().startswith('│') and l.count('│') >= 3:
            rows.append([c.strip() for c in l.strip().strip('│').split('│')])
        else:
            flush(); out.append(l.strip())
    flush(); return '\n'.join(out)


def box_to_callout(b):
    L = b.split('\n'); inner = []
    for l in L[1:-1]:
        c = l.strip()
        c = c[1:] if c.startswith('│') else c
        c = c[:-1] if c.endswith('│') else c
        inner.append(c.rstrip())
    inner = [re.sub(r'^ {1,3}', '', x) for x in inner]
    while inner and not inner[0].strip(): inner.pop(0)
    while inner and not inner[-1].strip(): inner.pop()
    if not inner: return None
    title = inner[0].strip(); body = inner[1:]
    out = [f'> [!NOTE] {title}']
    for x in body:
        out.append('>' if not x.strip() else '> ' + x + '  ')
    return '\n'.join(out)


def convert_boxes(f):
    t = f.read_text(encoding='utf-8'); n = 0
    for m in sorted(fences.finditer(t), key=lambda m: m.span()[0], reverse=True):
        b = m.body; r = None
        if re.search(r'[┬┼]', b) and '│' in b: r = box_to_table(b)
        elif b.lstrip().startswith('┌') and not re.search(r'[├┬┼┴]', b) and b.count('┌') == 1 and b.rstrip().endswith('┘'):
            r = box_to_callout(b)
        if r: a, e = m.span(); t = t[:a] + r + t[e:]; n += 1
    f.write_text(t, encoding='utf-8'); return n


F = 'Formule de la loi d\'Ohm'
def s01():
    d = D('seconde', 'S01'); f = d / '01-cours.md'
    form = "$$U = R \\times I \\qquad I = \\dfrac{U}{R} \\qquad R = \\dfrac{U}{I}$$"
    for n in ('loi_ohm_cercle', 'analogie_eau'): q(FIG / f'{n}.png', d / 'images' / (n.replace('_', '-') + '.png'))
    q(REPO / 'docs/annexes/rappels-e2/images/resistance_code_couleurs.png', d / 'images/resistance-code-couleurs.png') if False else None
    rules = [(has("CHÂTEAU D'EAU"), None, "![Analogie de l'eau : château d'eau, pompe, tuyau étroit et turbine face à pile, résistance et lampe](images/analogie-eau.png)"),
             (lambda b: b.strip().startswith('U') and '───' in b and 'U = R' not in b, None, "![Cercle de la loi d'Ohm : U en haut, R à gauche, I à droite ; on cache la grandeur cherchée](images/loi-ohm-cercle.png)\n\n" + form),
             (has('RÉSISTANCE 4 BAGUES'), None, "![Lecture du code couleurs d'une résistance à 4 bagues](images/resistance-code-couleurs.png)"),
             (lambda b: 'Rled' in b and '───' in b, None, "$$R_{\\text{LED}} = \\dfrac{V_{cc} - V_F}{I_{\\text{LED}}}$$"),
             (lambda b: 'U = R × I' in b and '───' in b, None, "![Cercle de la loi d'Ohm](images/loi-ohm-cercle.png)\n\n" + form)]
    return replace_blocks(f, rules, d)


def symboles():
    MAP = {'source de tension continue': 'source-continue', 'pile': 'pile', 'résistance': 'resistance', 'diode': 'diode', 'led': 'led', 'condensateur non polarisé': 'condo', 'condensateur polarisé': 'condo-polarise',
           'interrupteur no': 'inter-no', 'interrupteur nf': 'inter-nf', 'poussoir no': 'poussoir-no', 'fil conducteur': 'fil', 'jonction': 'jonction', 'croisement': 'croisement', 'masse': 'masse', 'lampe': 'lampe',
           'transistor npn': 'npn', 'transistor pnp': 'pnp', 'circuit intégré': 'ci', 'connecteur': 'connecteur', 'capteur générique': 'capteur', 'moteur dc': 'moteur', 'fusible': 'fusible',
           'régulateur': 'regulateur', 'relais': 'relais', 'optocoupleur': 'optocoupleur', 'interrupteur (nf ouvert)': 'inter-no', 'condensateur': 'condo'}
    def key(name):
        n = re.sub(r'\*|\(.*?\)', '', name).strip().lower(); n0 = name.replace('*', '').strip().lower()
        if n0 in MAP: return MAP[n0]
        for k in sorted(MAP, key=len, reverse=True):
            if n.startswith(k): return MAP[k]
    used = set()
    def img(k, alt): used.add(k); return f'![{alt}](images/sym-{k}.png){{ width="210" }}'
    s3, s6 = D('seconde', 'S03'), D('seconde', 'S06'); total = 0
    for f, ci in ((s3 / 'annexe-fiche-memo-symboles-iec-normes.md', 2), (s3 / '01-cours.md', 1)):
        L = f.read_text(encoding='utf-8').split('\n'); out = []; inT = False
        for l in L:
            if l.startswith('|') and 'Symbole IEC' in l and 'Composant' in l:
                inT = True; l = re.sub(r'Symbole IEC \((?:description textuelle|description)\)', 'Symbole IEC', l)
            elif inT and l.startswith('|---'): pass
            elif inT and l.startswith('|'):
                c = [x.strip() for x in l.strip().strip('|').split('|')]; k = key(c[1 if ci == 2 else 0])
                if k and not c[ci].startswith('!['): c[ci] = img(k, c[ci].replace('[', '(').replace(']', ')')[:140]); l = '| ' + ' | '.join(c) + ' |'; total += 1
            else: inT = False
            out.append(l)
        f.write_text('\n'.join(out), encoding='utf-8')
    f = s6 / '01-cours.md'; L = f.read_text(encoding='utf-8').split('\n'); out = []; inT = False; used6 = set()
    for l in L:
        if l.startswith('| Symbole | Repère | Usage typique |'): inT = True; l = '| Composant | Symbole IEC | Repère | Usage typique |'
        elif inT and l.startswith('|---'): l = '|---|---|---|---|'
        elif inT and l.startswith('|'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]; k = key(c[0])
            if k and len(c) == 3: l = f'| {c[0]} | {img(k, c[0].replace("*", ""))} | {c[1]} | {c[2]} |'; used6.add(k); total += 1
        else: inT = False
        out.append(l)
    f.write_text('\n'.join(out), encoding='utf-8')
    for k in used: q(SYM / f'sym-{k}.png', s3 / 'images' / f'sym-{k}.png')
    for k in used6: q(SYM / f'sym-{k}.png', s6 / 'images' / f'sym-{k}.png')
    return total


def seconde_figures():
    n = 0
    ZONE = "> [!NOTE] ✏️ À toi de dessiner\n> Dessine ton schéma sur ta feuille ou dans ton dossier (zone prévue pour le schéma)."
    spec = [('S03', '01-cours.md', [(has('Votre schéma IEC'), None, ZONE)]),
            ('S09', '01-cours.md', [(has('Variation CONTINUE'), 'signal_analogique', 'Signal analogique : variation continue de la tension'), (has('États DISCRETS'), 'signal_numerique', 'Signal numérique : deux états, 0 ou 1'),
                                    (lambda b: 'ADC' in b and '1023' in b and '──>' in b, 'adc_conversion', 'Conversion ADC 10 bits : 0 V → 0, 5 V → 1023')]),
            ('S10', '01-cours.md', [(lambda b: b.strip() == '──M──', 'symbole_moteur', 'Symbole du moteur DC et moteur réel'), (has('PWM 25%'), 'pwm_rapport_cyclique', 'PWM : rapport cyclique de 0 % à 100 % et vitesse du moteur')]),
            ('S12', '01-cours.md', [(has('Diode + Son'), 'continuite_buzzer', 'Test de continuité : symbole diode et bip sonore')]),
            ('S14', '01-cours.md', [(has('[ILLUSTRATION 1]'), 'portees_sans_fil', 'Portées comparées : Bluetooth, Wi-Fi et NFC'), (has('[ILLUSTRATION 2]'), 'hc05_brochage', "Module HC-05 : brochage et LED d'état"),
                                    (has('[ILLUSTRATION 3]'), 'chaine_bluetooth', 'Chaîne de communication : smartphone, HC-05, Arduino, actionneur'), (has('[ILLUSTRATION 4]'), 'moniteur_serie_at', 'Moniteur série : échange de commandes AT'),
                                    (has('[ILLUSTRATION 5]'), 'cablage_arduino_hc05', 'Câblage Arduino – HC-05 avec pont diviseur 1 kΩ / 2 kΩ')]),
            ('S14', '01-cours.md', [(has('[ILLUSTRATION 6]'), 'pairing_bluetooth', 'Appairage Bluetooth en 4 étapes sur smartphone')]),
            ('S15', '01-cours.md', [(has('[ILLUSTRATION 4]'), 'lcd_curseur', 'LCD 16×2 : coordonnées de setCursor'), (has('[ILLUSTRATION 5]'), 'lm35_brochage', 'LM35 : brochage et conversion tension → température'), (has('[ILLUSTRATION 6]'), 'cablage_lm35_lcd', 'Câblage : LM35 sur A0 et LCD I2C sur A4 / A5'), (has('[ILLUSTRATION 7]'), 'architecture_proto', 'Architecture du proto maquette final')]),
            ('S15', '01-cours.md', [(has('[ILLUSTRATION 1]'), 'lcd_classique_vs_i2c', 'LCD classique (10 fils) et LCD I2C (4 fils)'), (has('[ILLUSTRATION 2]'), 'bus_i2c', 'Bus I2C : un maître et trois esclaves'),
                                    (has('[ILLUSTRATION 3]'), 'lcd_i2c_annote', 'LCD 16×2 : positions des caractères et module I2C')]),
            ('S16', '01-cours.md', [(has('[ILLUSTRATION 3]'), 'dht11_cablage', 'Câblage du DHT11 nu sur Arduino avec résistance pull-up de 10 kΩ'), (has('[ILLUSTRATION 4]'), 'architecture_domotique', 'Architecture du système domotique'), (has('[ILLUSTRATION 5]'), 'schema_complet_domotique', 'Schéma électronique complet du système domotique A1')]),
            ('S16', '01-cours.md', [(has('[ILLUSTRATION 1]'), 'dht11_brochage', 'Capteur DHT11 : version nue (4 broches) et module (3 broches)'), (has('[ILLUSTRATION 2]'), 'dht11_chronogramme', 'Protocole du DHT11 : démarrage, réponse, 40 bits')]),
            ('S16', 'annexe-fiche-technique-capteur-dht11.md', [(lambda b: 'DHT11' in b and '┬' in b, 'dht11_brochage', 'DHT11 : face avant et numérotation des broches'), (has('pull-up', 'Arduino 5V'), 'dht11_cablage', 'Câblage du DHT11 avec résistance pull-up de 10 kΩ')]),
            ('S16', 'annexe-fiche-gabarit-schema-electronique-du.md', [(has('ZONE DE SCHÉMA'), None, ZONE)]),
            ('S17', '01-cours.md', [(has('[ILLUSTRATION 5]'), 'svarc_logigramme', 'Méthode SVARC : symptôme, vérification, analyse, remède, contrôle'), (has('[ILLUSTRATION 6]'), 'voltmetre_led', 'Mesure de la tension aux bornes d\'une LED avec le multimètre')]),
            ('S17', '01-cours.md', [(has('[ILLUSTRATION 1]'), 'pyramide_tests', 'Pyramide des tests : unitaires, intégration, système'), (has('[ILLUSTRATION 2]'), 'protocole_tests', 'Extrait de protocole de tests'),
                                    (has('[ILLUSTRATION 3]'), 'symboles_projet', 'Symboles normalisés des composants du projet'), (has('[ILLUSTRATION 4]'), 'bom_extrait', "Extrait d'une BOM (nomenclature)")]),
            ('S18', '01-cours.md', [(has('[ILLUSTRATION 1]'), 'soutenance_zones', "Ce qu'évalue une soutenance : savoir, savoir-faire, savoir-être"), (has('[ILLUSTRATION 2]'), 'soutenance_frise', 'Frise de la présentation : contexte, solution, résultats'),
                                    (has('[ILLUSTRATION 3]'), 'jury_organigramme', 'Répondre à une question du jury en 3 étapes'), (has('[ILLUSTRATION 4]'), 'grille_criteriee', "Extrait de grille critériée : trois niveaux de maîtrise")])]
    for p, fn, rules in spec:
        d = D('seconde', p); f = d / fn
        if f.exists(): n += replace_blocks(f, rules, d)
    return n


def unfenced(prefix, fname, n, name, alt):
    d = D('seconde', prefix); f = d / fname; L = f.read_text(encoding='utf-8').split('\n')
    for i, l in enumerate(L):
        if l.startswith(f'[ILLUSTRATION {n}]'):
            j = i
            while j < len(L) and not (L[j].startswith('PROMPT') or any(x.startswith('PROMPT') for x in L[i:j + 1]) and L[j].rstrip().endswith('"')): j += 1
            q(FIG / f'{name}.png', d / 'images' / (name.replace('_', '-') + '.png'))
            L[i:j + 1] = [f'![{alt}](images/{name.replace("_", "-")}.png)']; f.write_text('\n'.join(L), encoding='utf-8'); return 1
    return 0


def main():
    unfenced('S16', '01-cours.md', 5, 'schema_complet_domotique', 'Schéma électronique complet du système domotique A1')
    print('S01', s01(), '| symboles', symboles(), '| figures', seconde_figures())
    nb = 0
    for f in glob.glob(str(REPO / 'docs/*/*/*.md')):
        if '/annexes/' in f or f.endswith(('README.md', '04-simulateur.md')): continue
        nb += convert_boxes(Path(f))
    print('cadres convertis (callouts/tableaux)', nb)


main()
