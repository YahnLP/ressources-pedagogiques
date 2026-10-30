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


def P(p, fn):
    d = D('premiere', p); g = sorted(glob.glob(str(d / (fn + '*'))))
    return d, (Path(g[0]) if g else None)


def q(src, dst):
    dst.parent.mkdir(exist_ok=True)
    Image.open(src).convert('RGBA').quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG).save(dst, optimize=True)


def replace_blocks(f, rules, d):
    t = f.read_text(encoding='utf-8'); n = 0
    for m in sorted(fences.finditer(t), key=lambda m: m.span()[0], reverse=True):
        b = m.body
        for rule in rules:
            pred, name, alt = rule[:3]; extra = rule[3] if len(rule) > 3 else ''
            if pred(b):
                if name is None: r = alt
                else:
                    q(FIG / f'{name}.png', d / 'images' / (name.replace('_', '-') + '.png'))
                    if '__REST__' in extra: extra = extra.replace('__REST__', '\n'.join(b.split('\n')[3:]).strip())
                    r = f'![{alt}](images/{name.replace("_", "-")}.png)' + ('\n\n' + extra if extra else '')
                a, e = m.span(); t = t[:a] + r + t[e:]; n += 1; break
    f.write_text(t, encoding='utf-8'); return n


has = lambda *s: (lambda b: all(x in b for x in s))
RE = re.compile(r'\s*\[ILLUSTRATION')


def is_table(b):
    rows = [l for l in b.split('\n') if l.strip().startswith('│')]
    seps = [l for l in b.split('\n') if re.match(r'^\s*├[─┼]+┤\s*$', l)]
    if not rows or not seps or '┼' not in b: return False
    counts = {l.count('│') for l in rows}
    return len(counts) == 1 and counts.pop() >= 3 and b.count('┌') == 1


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
        if is_table(b): r = box_to_table(b)
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


from premiere_rules import RULES


def premiere():
    n = 0
    for p, fn, rules in RULES:
        d, f = P(p, fn)
        if f: n += replace_blocks(f, rules, d)
    return n


def md_placeholder(prefix, fname, start, name, alt):
    d = D('seconde', prefix); f = d / fname; L = f.read_text(encoding='utf-8').split('\n')
    for i, l in enumerate(L):
        if l.startswith('![Illustration') and start in l:
            j = i + 1
            while j < len(L) and L[j].strip() == '': j += 1
            if j < len(L) and L[j].startswith('**Prompt image'): j += 1
            if name:
                q(FIG / f'{name}.png', d / 'images' / (name.replace('_', '-') + '.png')); rep = [f'![{alt}](images/{name.replace("_", "-")}.png)']
            else: rep = []
            L[i:j] = rep; f.write_text('\n'.join(L), encoding='utf-8'); return 1
    return 0


def s01_extra():
    n = md_placeholder('S01', '01-cours.md', 'Deux schémas côte à côte', None, '')
    n += md_placeholder('S01', '01-cours.md', "Schéma électrique d'un circuit LED", 'circuit_led_9v', 'Circuit LED : pile 9 V, résistance de protection 330 Ω et LED rouge')
    n += md_placeholder('S10', '01-cours.md', 'Deux schémas de moteur', 'moteur_sens', "Inversion du sens de rotation d'un moteur en inversant la pile")
    n += md_placeholder('S10', '01-cours.md', 'Schéma de câblage complet', 'cablage_l293d', 'Câblage du L293D : Arduino, moteur et pile 9 V externe')
    n += md_placeholder('S12', '01-cours.md', 'Multimètre en mode continuité', 'continuite_multimetre', 'Mode continuité : fil intact (bip) et fil coupé (pas de bip)')
    d = D('seconde', 'S01'); f = d / '01-cours.md'; t = f.read_text(encoding='utf-8')
    for old, k in (('──▭──', 'resistance'), ('──▷\\|── | Émettre', 'led'), ('──▷\\|── | Laisser', 'diode'), ('──\\|\\|──', 'condo'), ('─┤├─', 'npn'), ('─\\|+─', 'pile')):
        pass
    rows = {'🟤 **Résistance**': 'resistance', '🔴 **LED**': 'led', '⚫ **Diode**': 'diode', '🟡 **Condensateur**': 'condo', '🔵 **Transistor**': 'npn', '🔋 **Pile**': 'pile'}
    L = t.split('\n')
    for i, l in enumerate(L):
        for lab, k in rows.items():
            if l.startswith('| ' + lab):
                c = l.split(' | ')
                c[1] = f'![{lab.split("**")[1]}](images/sym-{k}.png){{ width="210" }}'; L[i] = ' | '.join(c); q(SYM / f'sym-{k}.png', d / 'images' / f'sym-{k}.png'); n += 1
    t = '\n'.join(L)
    for m in sorted(fences.finditer(t), key=lambda m: m.span()[0], reverse=True):
        if '← ← ←' in m.body or ('→ → →' in m.body and 'mA' in m.body):
            a, e_ = m.span(); r = "![Échelle des unités : multiplier ou diviser par 1 000](images/echelle-unites.png)" if '← ← ←' in m.body else ''
            t = t[:a] + r + t[e_:]
    q(FIG / 'echelle_unites.png', d / 'images' / 'echelle-unites.png')
    f.write_text(t, encoding='utf-8'); return n


HRULES = [  # (année, séance, fichier, n°, figure ou None = capture à réaliser, alt)
    ('premiere', 'S01', '01-cours', 1, 'kicad_editeur_schema', "Éditeur de schéma KiCad : zone de dessin et barre d'outils de droite"), ('premiere', 'S01', '01-cours', 2, 'kicad_schema_led', 'Schéma de la LED dans KiCad, broches annotées'),
    ('premiere', 'S03', '01-cours', 1, 'flux_schema_pcb', 'Du schéma au PCB en 8 étapes'), ('premiere', 'S03', '01-cours', 2, 'pistes_vias_clearance', 'Pistes, via et clearance'),
    ('premiere', 'S03', '01-cours', 3, 'kicad_drc', 'Fenêtre DRC et erreurs correspondantes sur le PCB'), ('premiere', 'S03', '01-cours', 4, 'kicad_vue_3d', 'Vue 3D KiCad du petit PCB'),
    ('premiere', 'S04', '01-cours', 1, 'coupe_pcb_double_face', "Coupe d'un PCB double face"), ('premiere', 'S04', '01-cours', 2, 'cms_traversant', 'Composant traversant (THT) et composant CMS (SMD)'),
    ('premiere', 'S04', '01-cours', 3, 'kicad_export_gerber', "Fenêtre d'export Gerber et fichiers générés"), ('premiere', 'S04', '01-cours', 4, 'gerber_couches', 'Des calques Gerber au PCB réel'),
    ('premiere', 'S06', '01-cours', 1, 'wifi_sta', 'ESP32 en mode STA'), ('premiere', 'S06', '01-cours', 2, 'wifi_modes', 'Modes Wi-Fi de l\'ESP32 : STA, AP et STA + AP'), ('premiere', 'S06', '01-cours', 3, 'mqtt_esp32', 'Architecture MQTT avec un ESP32'),
    ('premiere', 'S08', '01-cours', 1, 'nodered_flow_simple', 'Flow Node-RED simple à 5 nœuds'), ('premiere', 'S08', '01-cours', 2, 'nodered_dashboard', 'Dashboard Node-RED : jauge et graphe'), ('premiere', 'S08', '01-cours', 3, 'nodered_flow_complet', 'Flow IoT complet ESP32 → MQTT → Node-RED → InfluxDB'),
    ('premiere', 'S11', '01-cours', 1, 'chronologie_mtbf', 'Chronologie MTBF / MTTR'), ('premiere', 'S11', '01-cours', 2, 'courbe_fiabilite', 'Courbe de fiabilité R(t) = e^(−λt)'), ('premiere', 'S11', '01-cours', 3, 'serie_parallele_fiabilite', 'Fiabilité en série et en parallèle'),
    ('premiere', 'S13', '01-cours', 1, 'couplages_cem', 'Les quatre types de couplage CEM'), ('premiere', 'S13', '01-cours', 2, 'blindage_fente', 'Blindage efficace et effet de fente'), ('premiere', 'S13', '01-cours', 3, 'decouplage_pcb', 'Condensateurs de découplage sur un PCB'),
    ('premiere', 'S17', '01-cours', 1, 'hysteresis_alerte', "Hystérésis d'une alerte de température"), ('premiere', 'S17', '01-cours', 2, 'exactitude_fidelite', 'Exactitude et fidélité'),
    ('terminale', 'S03', '01-cours', 1, 'lineaire_decoupage', 'Régulateur linéaire et convertisseur à découpage'), ('terminale', 'S03', '01-cours', 2, 'modele_thermique', "Modèle thermique d'un régulateur"),
    ('terminale', 'S08', '01-cours', 1, 'cibles_repetabilite', 'Répétabilité et reproductibilité'), ('terminale', 'S08', '01-cours', 2, 'grr_interpretation', 'Interprétation graphique du %GRR')]


def heading_placeholders():
    n = 0; todo = []
    files = {}
    for y, s, fn, num, name, alt in HRULES:
        d = D(y, s); f = sorted(glob.glob(str(d / (fn + '*'))))[0]; f = Path(f)
        L = files.setdefault(f, (d, f.read_text(encoding='utf-8').split('\n')))[1]
        for i, l in enumerate(L):
            if l.startswith(f'**🖼️ ILLUSTRATION {num} '):
                j = i + 1
                while j < len(L) and L[j].startswith('>'): j += 1
                legend = next((x for x in L[i + 1:j] if 'Légende' in x), '')
                if name:
                    q(FIG / f'{name}.png', d / 'images' / (name.replace('_', '-') + '.png')); rep = [f'![{alt}](images/{name.replace("_", "-")}.png)']
                else:
                    rep = []; todo.append((f.parent.name, l.strip('*'), legend.replace('> *Légende* : ', '')[:300]))
                L[i:j] = rep; n += 1; break
    # filet de sécurité : tout placeholder restant est retiré et consigné
    for f in glob.glob(str(REPO / 'docs/*/*/*.md')):
        if '/annexes/' in f: continue
        f = Path(f); t = f.read_text(encoding='utf-8'); L = files[f][1] if f in files else t.split('\n'); ch = f in files
        i = 0
        while i < len(L):
            if re.match(r'^\*\*🖼️ ILLUSTRATION', L[i]):
                j = i + 1
                while j < len(L) and L[j].startswith('>'): j += 1
                legend = next((x for x in L[i + 1:j] if 'Légende' in x), '')
                todo.append((f.parent.name, L[i].strip('*'), legend.replace('> *Légende* : ', '')[:300])); del L[i:j]; ch = True; n += 1
            else: i += 1
        if ch: files[f] = (D('seconde', 'S01') if f not in files else files[f][0], L)
    for f, (d, L) in files.items(): f.write_text('\n'.join(L), encoding='utf-8')
    if todo:
        out = ['# Captures et figures à réaliser', '', 'Captures d\'écran de logiciels (KiCad, Node-RED…) à prendre depuis l\'application réelle, ou figures non encore créées.', '', '| Séance | Figure | Description |', '|---|---|---|']
        out += [f'| {a} | {b.replace("|", "/")} | {c.replace("|", "/")} |' for a, b, c in todo]
        (REPO / 'outils' / 'import_e2' / 'captures-a-realiser.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    return n, len(todo)


CAM = {  # figures réutilisées pour les placeholders 📷 : (année, séance, n°) -> (figure, légende)
    ('premiere', 'S05', 1): ('chrono_i2c', "Transaction I2C : condition START, adresse sur 7 bits, bit R/W et ACK."),
    ('premiere', 'S05', 2): ('chrono_spi', "Transaction SPI : CS bas, huit coups d'horloge SCLK, données sur MOSI et MISO."),
    ('premiere', 'S07', 1): ('mqtt_broker', "Architecture MQTT : le broker est l'unique point de contact entre publishers et subscribers."),
    ('premiere', 'S09', 1): ('tls_mtls', "Authentification TLS standard et mutuelle (mTLS) avec AWS IoT Core."),
    ('premiere', 'S14', 1): ('deca_entonnoir', "La démarche DECA : chaque étape réduit le champ des possibles jusqu'à l'action corrective."),
    ('premiere', 'S14', 2): ('logigramme_esp32', "Logigramme de diagnostic d'un ESP32 qui ne publie plus : le code mqtt.state() oriente la recherche."),
    ('premiere', 'S07', 2): ('chaine_iot_mqtt', "Chaîne IoT de la séance : ESP32 et DHT22, JSON, topic, broker Mosquitto, puis deux subscribers."),
    ('premiere', 'S18', 1): ('cablage_professionnel', "Schéma de câblage professionnel : fils repérés aux deux extrémités, couleurs CEI 60446, cartouche."),
    ('premiere', 'S18', 2): ('dat_amateur_pro', "Dossier technique amateur et professionnel."),
    ('premiere', 'S09', 2): ('cloudwatch_dashboard', "Tableau de bord CloudWatch d'un projet IoT ESP32."),
    ('premiere', 'S02', 1): ('eeschema_vue', "Schéma en cours de saisie : VCC et GND sont des nœuds globaux."),
    ('premiere', 'S02', 2): ('pwr_flag', "Le PWR_FLAG supprime les fausses alertes ERC sur les nœuds d'alimentation."),
    ('premiere', 'S12', 1): ('boitiers_quatre', "Quatre approches de boîtier pour un projet IoT ESP32."),
    ('premiere', 'S12', 2): ('plan_tests_exemple', "Plan de tests après exécution : TC-003 échoue, TC-005 est à la limite."),
    ('terminale', 'S04', 2): ('chaine_s4', "Chaîne complète de la séance : capteur, KPI, alarme, courbe, fiche de mise en service."),
    ('terminale', 'S07', 1): ('pv_validation', "Structure d'un PV de validation fonctionnelle professionnel."),
    ('terminale', 'S07', 2): ('dossier_livraison', "Dossier de livraison : DAT, PV de validation et fiche MES."),
    ('terminale', 'S02', 1): ('tracabilite_metrologique', "Chaîne de traçabilité métrologique du BIPM jusqu'au PV de mesure."),
    ('terminale', 'S02', 2): ('incertitude_composition', "Composition de l'incertitude : la classe de l'instrument domine."),
    ('terminale', 'S04', 1): ('hysteresis_alerte', "Alarme avec hystérésis : seuil haut 30 °C, seuil bas 28 °C, plus de clignotement autour du seuil.")}


def camera_placeholders():
    n = 0; todo = []
    for f in glob.glob(str(REPO / 'docs/*/*/*.md')):
        if '/annexes/' in f: continue
        f = Path(f); L = f.read_text(encoding='utf-8').split('\n'); i = 0; ch = False; k = 0
        y = f.parts[-3]; s = f.parent.name[:3]
        while i < len(L):
            if L[i].startswith('📷 **[ILLUSTRATION'):
                k += 1; j = i + 1
                while j < len(L) and (L[j].strip() == '' or L[j].startswith(('*', '>'))) and not L[j].startswith('---'):
                    if L[j].strip() == '' and j + 1 < len(L) and not L[j + 1].startswith(('*', '>')): break
                    j += 1
                block = L[i:j]; leg = next((x for x in block if x.startswith('> **Légende')), '').replace('> **Légende :** ', '')
                key = (y, s, k)
                if key in CAM:
                    name, cap = CAM[key]; d = f.parent
                    q(FIG / f'{name}.png', d / 'images' / (name.replace('_', '-') + '.png')); rep = [f'![{cap}](images/{name.replace("_", "-")}.png)']
                else:
                    rep = []; todo.append((f.parent.name, f'Figure {k}', leg[:300]))
                L[i:j] = rep; ch = True; n += 1
            else: i += 1
        if ch: f.write_text('\n'.join(L), encoding='utf-8')
    if todo:
        p = REPO / 'outils' / 'import_e2' / 'captures-a-realiser.md'
        old = p.read_text(encoding='utf-8') if p.exists() else ''
        p.write_text(old.rstrip('\n') + '\n' + '\n'.join(f'| {a} | {b} | {c.replace("|", "/")} |' for a, b, c in todo) + '\n', encoding='utf-8')
    return n, len(todo)


SMAN = {  # Seconde : figures des emplacements vides (séance -> [(début de titre, figure, texte alternatif)])
    'S02': [('### 1.2', 'diode_led', 'Symbole IEC et aspect réel d\'une LED'), ('### 2.2', 'loi_ohm_cercle', 'Cercle de la loi d\'Ohm : U en haut, R à gauche, I à droite'), ('### 3.1', 'circuit_led_9v', 'Circuit LED : pile 9 V, résistance et LED en série'), ('### 4.1', 'led_serie', 'Deux LED en série avec une résistance'), ('### 4.2', 'led_parallele', 'Deux LED en parallèle avec une résistance commune'), ('## 6.', 'multimetre', 'Multimètre numérique annoté')],
    'S03': [('### 1.1', 'breadboard', 'Structure interne d\'une breadboard'), ('### 1.3', 'cablage_ok_ko', 'Câblage correct et câblage incorrect sur breadboard'), ('### 2.2', 'symboles_de_base', 'Symboles IEC à maîtriser'), ('### 2.4', 'schema_parallele_iec', 'Schéma normé IEC : deux LED en parallèle'), ('### 3.2', 'schema_vs_montage', 'Du schéma au montage sur breadboard'), ('### 4.1', 'continuite_multimetre', 'Test de continuité : fil intact et fil coupé'), ('### 4.3', 'arbre_continuite', 'Arbre de diagnostic par test de continuité')],
    'S04': [('### 1.1', 'station_soudure', 'Station de soudure annotée'), ('### 1.2', 'materiaux_soudure', 'Fil d\'étain, flux et tresse à dessouder'), ('## 2.', 'etapes_soudure', 'Les 5 étapes de la soudure'), ('### 3.1', 'pyramide_ipc', 'Les trois classes IPC'), ('### 3.2', 'brasure_coupe', 'Brasure traversante IPC classe 2 acceptable'), ('### 3.3', 'defauts_brasures', 'Les 7 défauts de brasure les plus courants'), ('## 4.', 'sequence_insertion', 'Ordre d\'insertion des composants traversants')],
    'S05': [('### 1.1', 'pyramide_maintenance', 'Les niveaux de maintenance N1 à N4'), ('### 1.2', 'preventive_corrective', 'Maintenance préventive et corrective'), ('### 2.2', 'outils_nettoyage', 'Produits et outils de nettoyage'), ('### 3.1', 'grille_diagnostic_visuel', 'Les 9 critères du diagnostic visuel'), ('### 4.1', 'esd_phenomene', 'Le phénomène de décharge électrostatique'), ('### 4.2', 'esd_dommage', 'Dommage immédiat et dommage latent'), ('### 4.3', 'poste_esd', 'Poste de travail protégé contre les décharges'), ('### 5.1', 'outils_technicien', 'Outillage du technicien')],
    'S06': [('### 1.2', 'symboles_avances', 'Symboles IEC avancés'), ('### 1.3', 'schema_bp_led', 'Schéma normé : bouton-poussoir et LED'), ('### 2.1', 'tinkercad_interface', 'Interface de Tinkercad Circuits (maquette)'), ('### 2.4', 'tinkercad_multimetre', 'Multimètre virtuel : voltmètre en parallèle, ampèremètre en série'), ('### 3.1', 'datasheet_annotee', 'Première page d\'une datasheet annotée'), ('### 3.2', 'ratings_bc547', 'Absolute Maximum Ratings du BC547'), ('### 4.1', 'schema_transistor_led', 'LED commandée par un transistor BC547')],
    'S07': [('## 1.', 'arduino_uno_annote', 'Anatomie de la carte Arduino Uno'), ('### 2.1', 'arduino_ide', 'Interface de l\'IDE Arduino (maquette)'), ('### 3.1', 'setup_loop', 'Fonctionnement de setup() et loop()'), ('### 4.2', ['schema_led_d13', 'cablage_uno_breadboard'], ['Schéma normé : LED sur la broche D13', 'Câblage de la LED sur breadboard']), ('### 5.3', 'serial_monitor_ide', 'Moniteur série de l\'IDE Arduino (maquette)')],
    'S08': [('### 1.1', 'niveaux_logiques', 'Niveaux logiques d\'une entrée numérique Arduino'), ('### 1.3', 'flottant_pulldown', 'Entrée flottante et résistance pull-down'), ('### 2.1', 'pulldown_etats', 'Pull-down : bouton relâché et bouton appuyé'), ('### 3.2', 'pulldown_pullup', 'Pull-down externe et INPUT_PULLUP'), ('### 5.2', 'pyramide_debug', 'Les 4 niveaux de débogage série'), ('### 5.6', 'tableau_bugs', 'Les 5 bugs les plus fréquents')],
    'S11': [('### 1.1', 'pcb_coupe_couches', 'Coupe d\'un PCB simple face'), ('### 2.1', 'flux_fabrication_pcb', 'Les 8 étapes de fabrication d\'un PCB'), ('#### Réaction', 'gravure_mecanisme', 'Mécanisme de la gravure au perchlorure de fer'), ('#### Anomalies', 'gravure_defauts', 'Sous-gravure, gravure correcte et sur-gravure'), ('### 3.1', 'perceuse_colonne', 'Perceuse à colonne annotée'), ('### 4.2', 'criteres_ipc_a600', 'Critères visuels IPC-A-600'), ('#### Critère 3', 'anneau_cuivre', 'Mesure de l\'anneau de cuivre'), ('### 5.1', 'test_multimetre_pcb', 'Tests au multimètre sur un PCB')],
    'S13': [('### 1.1', 'uart_tx_rx', 'Liaison UART : TX et RX croisés'), ('### 1.2', 'trame_uart', 'Trame UART 8N1 : lettre A'), ('### 3.1', 'serial_monitor_params', 'Paramètres du moniteur série'), ('### 4.1', 'hc05_brochage', 'Module HC-05 et brochage'), ('### 4.2', 'diviseur_tension', 'Diviseur de tension 5 V vers 3,3 V'), ('### 4.5', 'cablage_arduino_hc05', 'Câblage complet Arduino et HC-05')],
}


def seconde_manquantes():
    n = 0
    for sess, rules in SMAN.items():
        d = D('seconde', sess); f = d / '01-cours.md'; L = f.read_text(encoding='utf-8').split('\n')
        for pref, fig, alt in rules:
            figs = fig if isinstance(fig, list) else [fig]; alts = alt if isinstance(alt, list) else [alt]
            idx = next((i for i, l in enumerate(L) if l.startswith(pref + ' ') or l.startswith(pref)), None)
            if idx is None: print('titre introuvable', sess, pref); continue
            j = idx + 1
            while j < len(L) and L[j].strip() == '': j += 1
            if j < len(L) and L[j].startswith('!['): continue
            ins = ['']
            for fg, al in zip(figs, alts):
                q(FIG / f'{fg}.png', d / 'images' / (fg.replace('_', '-') + '.png')); ins += [f'![{al}](images/{fg.replace("_", "-")}.png)', '']
            L[idx + 1:idx + 1] = ins; n += len(figs)
        f.write_text('\n'.join(L), encoding='utf-8')
    return n


ASCII = [  # (année, séance, marqueur dans le bloc, figure ou texte de remplacement, alt)
    ('seconde', 'S01', '╔═══', '=$$U = R \\times I$$', ''),
    ('seconde', 'S09', 'LM35DZ (TO-92)', 'lm35_brochage', 'Brochage du LM35 en boîtier TO-92, vu de face'),
    ('seconde', 'S09', '│ LM35│', '=', ''),
    ('seconde', 'S09', 'LM35                    Arduino Uno', 'cablage_lm35', 'Câblage du LM35 sur l\'Arduino Uno'),
    ('seconde', 'S09', '5V ─────────┬────── LM35 broche 1', '=| Arduino | LM35 |\n|---|---|\n| 5V | broche 1 (VCC) |\n| A0 | broche 2 (OUT) |\n| GND | broche 3 (GND) |', ''),
    ('seconde', 'S10', 'L293D (Vue de dessus)', 'brochage_l293d', 'Brochage du L293D vu de dessus'),
    ('seconde', 'S10', 'Arduino                 L293D', 'cablage_l293d', 'Câblage Arduino, L293D et moteur'),
    ('premiere', 'S01', 'Fenêtre principale de KiCad', 'kicad_fenetre_principale', 'Fenêtre principale de KiCad : gestionnaire de projet et outils'),
    ('premiere', 'S01', "Barre d'outils horizontale", 'kicad_editeur_schema', "Interface de l'éditeur de schéma KiCad"),
    ('premiere', 'S02', 'KiCad Project Manager', 'kicad_fenetre_principale', 'Gestionnaire de projet KiCad'),
    ('premiere', 'S02', 'BARRE DE MENUS', 'kicad_editeur_schema', "Interface d'Eeschema"),
    ('premiere', 'S09', 'AWS IoT Core', 'chaine_aws', 'Architecture AWS IoT Core'),
    ('premiere', 'S01', 'SCHÉMA ATTENDU', 'driver_transistor_s01', 'Schéma attendu : LED pilotée par un transistor', {'file': '02-tp.md', 'cut': 'CALCULS PRÉALABLES'}),
    ('premiere', 'S02', 'NE555 U1', 'ne555_astable_tp', 'Schéma du NE555 en montage astable', {'file': '02-tp.md', 'cut': 'Fréquence approximative'}),
    ('premiere', 'S03', 'Circuit à implémenter', 'driver_transistor_s03', 'Circuit à implémenter sur le PCB', {'file': '02-tp.md', 'cut': 'Composants et empreintes'}),
    ('premiere', 'S05', 'Bus I2C → Capteur MPU-6050', 'bus_arduino_i2c_spi', 'Bus I2C et bus SPI de l\'Arduino', {'file': '02-tp.md', 'cut': 'Alimentation : USB'}),
    ('premiere', 'S06', 'ESP32 DevKit v1 :', 'esp32_caracteristiques', 'Caractéristiques de l\'ESP32 DevKit v1', {'cut': 'Alimentation : 3,3 V'}),
    ('premiere', 'S07', 'Mosquitto 2.x', 'architecture_mqtt_tp', 'Architecture du TP : ESP32, Wi-Fi et broker Mosquitto', {'file': '02-tp.md', 'cut': 'Topics utilisés'}),
    ('premiere', 'S09', 'AWS IoT Core', 'chaine_aws', 'De l\'ESP32 à CloudWatch', {'file': '02-tp.md'}),
    ('premiere', 'S11', '┌── [C1] ──┐', 'rbd_parallele', 'Système parallèle', {'cut': 'Le système tombe'}),
    ('premiere', 'S12', 'Vue de dessus du boîtier', 'boitier_vue_dessus', 'Vue de dessus du boîtier', {}),
    ('premiere', 'S12', 'Développé à découper', 'developpe_boitier', 'Développé du boîtier en 6 faces', {'file': '02-tp.md'}),
    ('premiere', 'S13', 'L (inductance) en série', 'filtre_lc', 'Filtre LC', {'cut': 'Fréquence de coupure'}),
    ('premiere', 'S13', 'Signal bruité ──[R]──', 'filtre_rc', 'Filtre RC', {'file': '02-tp.md', 'cut': 'Fréquence de coupure'}),
    ('premiere', 'S13', 'PLAN CONTINU (recommandé)', 'plan_masse_continu_fendu', 'Plan de masse continu et plan de masse fendu', {'md': '{IMG}\n\n- **Plan continu** : le courant de retour emprunte le chemin de moindre impédance, juste sous la piste. La boucle est minimale, donc le rayonnement aussi.\n- **Plan fendu** : la fente force le courant de retour à faire un long détour. La boucle devient une grande antenne et les deux parties du plan se couplent.'}),
    ('premiere', 'S13', 'RÈGLE 1 — Point de masse unique', 'regles_masse', 'Les quatre règles de mise à la masse', {'md': '{IMG}\n\n1. **Point de masse unique (étoile)** : toutes les masses reviennent à un seul point, idéal pour l\'analogique basse fréquence.\n2. **Plan de masse (réseau)** : toutes les masses sont reliées à un plan continu, idéal pour le numérique et la haute fréquence.\n3. **Masses séparées** : les masses analogique et numérique se rejoignent en un point de jonction unique vers la terre.\n4. **Pas de boucle de masse** : deux chemins différents entre deux points de masse forment une antenne.'}),
    ('premiere', 'S15', 'Schéma : LED + résistance', 'schema_erreurs_erc', 'Schéma contenant quatre erreurs à trouver', {'file': '03-exercices.md', 'cut': 'Erreurs à trouver'}),
    ('terminale', 'S01', 'CARTE SONDE_E2_A3', 'carte_sonde', 'Carte sonde E2 A3', {'file': '02-tp.md', 'cut': 'Composants à mesurer'}),
    ('terminale', 'S03', 'Source (batterie LiPo', 'chaine_alimentation_decouplage', 'Chaîne d\'alimentation et découplage', {'cut': 'Protection optionnelle'}),
    ('terminale', 'S04', 'Architecture A3', 'architecture_a3', 'Architecture A3 : alarme locale et publication réseau', {'cut': 'Avantage'}),
    ('terminale', 'S06', '─┤  NE555', 'brochage_ne555', 'Brochage du NE555', {'cut': 'Mode astable'}),
    ('terminale', 'S06', '│ 7805│', 'brochage_7805', 'Brochage du régulateur 7805', {'cut': '(1) Input'}),
    ('terminale', 'S07', 'FAMILLE 1', 'familles_normes', 'Les trois familles de normes', {}),
    ('terminale', 'S11', 'pin7 (DISCHARGE)', 'ne555_astable_dossier', 'Schéma du dossier technique', {'file': 'annexe-dossier-technique-tp-s11-annee-3-e2.md'}),
    ('terminale', 'S11', 'CONTROL VOLTAGE', 'brochage_ne555', 'Brochage du NE555', {'file': 'annexe-dossier-technique-tp-s11-annee-3-e2.md'}),
    ('terminale', 'S11', '7805     │', 'brochage_7805', 'Brochage du 7805', {'file': 'annexe-dossier-technique-tp-s11-annee-3-e2.md'}),
]
LANGS = ('cpp', 'c', 'python', 'bash', 'javascript', 'json', 'arduino', 'ino', 'yaml', 'sql', 'js', 'sh', 'flux', 'csv')


def ascii_remplacements():
    n = 0
    for r in ASCII:
        y, sess, marker, rep, alt = r[:5]; ex = r[5] if len(r) > 5 else {}
        d = D(y, sess); f = d / ex.get('file', '01-cours.md'); L = f.read_text(encoding='utf-8').split('\n'); i = 0; done = False
        while i < len(L):
            m = re.match(r'^(\s*)```(\w*)\s*$', L[i])
            if m and m.group(2) not in LANGS:
                j = i + 1
                while j < len(L) and not re.match(r'^\s*```\s*$', L[j]): j += 1
                if any(marker in l for l in L[i + 1:j]):
                    if 'md' in ex or not rep.startswith('='):
                        q(FIG / f'{rep}.png', d / 'images' / (rep.replace('_', '-') + '.png')); img = f'![{alt}](images/{rep.replace("_", "-")}.png)'
                    if 'md' in ex: L[i:j + 1] = ex['md'].replace('{IMG}', img).split('\n')
                    elif rep.startswith('='): L[i:j + 1] = rep[1:].split('\n') if rep[1:] else []
                    elif 'cut' in ex:
                        k = next((x for x in range(i + 1, j) if L[x].strip().startswith(ex['cut'])), None)
                        if k is None: print('coupure introuvable', y, sess, ex['cut']); L[i:j + 1] = [img]
                        else: L[i:k] = [img, '', L[i]]
                    else: L[i:j + 1] = [img]
                    n += 1; done = True; break
                i = j
            i += 1
        if not done: print('bloc introuvable', y, sess, marker)
        f.write_text('\n'.join(L), encoding='utf-8')
    # Seconde S03, exercice 1 : schéma en texte non encadré
    f = D('seconde', 'S03') / '01-cours.md'; L = f.read_text(encoding='utf-8').split('\n')
    a = next((i for i, l in enumerate(L) if l.strip().startswith('+ 9V')), None)
    if a is not None:
        b = next(i for i in range(a, len(L)) if L[i].strip() == 'GND')
        if L[a - 1].strip().startswith('```') and b + 1 < len(L) and L[b + 1].strip() == '```': a -= 1; b += 1
        q(FIG / 'schema_exercice_lire.png', f.parent / 'images' / 'schema-exercice-lire.png')
        L[a:b + 1] = ['![Schéma de l\'exercice 1 : source 9 V, R1 = 470 Ω, deux LED en parallèle](images/schema-exercice-lire.png)']; n += 1
    f.write_text('\n'.join(L), encoding='utf-8')
    return n


def main():
    print('Placeholders (figures, captures)', heading_placeholders())
    print('Placeholders 📷', camera_placeholders())
    print('Seconde extra', s01_extra())
    print('Seconde manquantes', seconde_manquantes())
    print('Première', premiere())
    print('ASCII remplacés', ascii_remplacements())
    unfenced('S16', '01-cours.md', 5, 'schema_complet_domotique', 'Schéma électronique complet du système domotique A1')
    print('S01', s01(), '| symboles', symboles(), '| figures', seconde_figures())
    nb = 0
    for f in glob.glob(str(REPO / 'docs/*/*/*.md')):
        if '/annexes/' in f or f.endswith(('README.md', '04-simulateur.md')): continue
        nb += convert_boxes(Path(f))
    print('cadres convertis (callouts/tableaux)', nb)


main()
