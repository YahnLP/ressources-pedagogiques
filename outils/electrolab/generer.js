/* Génère les fichiers .json ElectroLab et les pages « Simulateur » des séances E2.
 * Usage : node generer.js <chemin_ElectroLab> <racine_du_depot>
 * ElectroLab n'est jamais modifié : on charge ses sources en lecture seule. */
const fs = require('fs'), path = require('path');
const EL = path.resolve(process.argv[2]), REPO = path.resolve(process.argv[3]);
const NS = require(path.join(EL, 'tests', 'load.js'))();

// séance du site → scénarios ElectroLab (id, nombre de variantes exportées)
const PLAN = {
  'seconde/1': [['ohm', 1]],
  'seconde/2': [['led', 3], ['assoc', 1]],
  'seconde/12': [['test', 1]],
  'premiere/4': [['ne555', 2]],
  'premiere/5': [['osc_lect', 2], ['la_intro', 1], ['i2c', 2], ['spi', 2]],
  'premiere/13': [['filtre', 2]],
  'premiere/14': [['dep1', 2], ['dep2', 2]],
  'terminale/1': [['signaux', 2]],
  'terminale/3': [['transfo', 1], ['redress', 1], ['filtrage', 1], ['regul', 1]],
  'terminale/12': [['diviseur', 1]],
};
const SEC = [
  ['Calculer R = (E − V<sub>F</sub>) / I<sub>F</sub> avec la loi des mailles', "Calculer R = (E − V<sub>F</sub>) / I<sub>F</sub> : la résistance reçoit la tension qui reste (E − V<sub>F</sub>), puis on applique la loi d'Ohm"],
  ['Calculez R avec la loi des mailles E = R·I + V<sub>F</sub>.', "Calculez R : la tension aux bornes de R est U<sub>R</sub> = E − V<sub>F</sub>, puis R = U<sub>R</sub> / I<sub>F</sub> (loi d'Ohm)."],
  ['Appliquer la loi des nœuds (I = I2 + I3)', 'Vérifier que le courant total est la somme des courants des branches (I = I2 + I3)'],
];
let CUR_YEAR = '';
const md = s => { let t = String(s || '').replace(/<br\s*\/?>/g, '  \n'); if (CUR_YEAR === 'seconde') SEC.forEach(([a, b]) => { t = t.split(a).join(b); }); return t.replace(/([A-Za-z])<sub>([^<]+)<\/sub>/g, (m, a, b) => `$${a}_{${b}}$`); };
const bySc = Object.fromEntries(NS.SCENARIOS.map(s => [s.id, s]));
let nfiles = 0;
for (const [key, list] of Object.entries(PLAN)) {
  const [year, n] = key.split('/'); CUR_YEAR = year;
  const ydir = path.join(REPO, 'docs', year);
  const sdir = fs.readdirSync(ydir).find(d => d.startsWith('S' + String(n).padStart(2, '0') + '-'));
  if (!sdir) { console.log('séance introuvable', key); continue; }
  const dir = path.join(ydir, sdir); const tp = path.join(dir, 'tp'); fs.mkdirSync(tp, { recursive: true });
  let page = ['# 🖥️ Exercices et TP sur le simulateur ElectroLab', '',
    '> [!NOTE]', '> **Comment faire ?** 1) Télécharge le fichier `.json` (clic droit → *Enregistrer le lien sous*). 2) Dans [ElectroLab](https://yahnlp.github.io/ElectroLab/), clique sur **Ouvrir** et choisis ce fichier. 3) Réponds aux questions sur ta feuille ou dans ton portfolio. Mode d\'emploi : [Utiliser ElectroLab](../../ressources/electrolab.md).', ''];
  const links = [];
  for (const [id, nv] of list) {
    const sc = bySc[id]; if (!sc) { console.log('scénario inconnu', id); continue; }
    page.push(`## ${sc.title}`, '', `*${sc.level || 'Bac Pro CIEL'} · durée indicative : ${sc.duration || '1 h'}*`, '', md(sc.desc), '');
    if (sc.objectives && sc.objectives.length) { page.push('### 🎯 Objectifs', '', ...sc.objectives.map(o => `- ${md(o)}`), ''); }
    if (sc.steps && sc.steps.length) { page.push('### 🛠️ Marche à suivre', '', ...sc.steps.map((s, i) => `${i + 1}. ${md(s)}`), ''); }
    if (sc.questions && sc.questions.length) {
      page.push('### ❓ Questions', '');
      sc.questions.forEach((q, i) => {
        let t = `${i + 1}. ${md(q.q)}`;
        if (q.type === 'choice' && q.options) t += '  \n' + q.options.map(o => `    - ☐ ${md(o)}`).join('  \n');
        page.push(t);
      });
      page.push('');
    }
    page.push('### 📥 Fichiers à ouvrir dans ElectroLab', '');
    const files = [];
    for (let v = 0; v < Math.min(nv, sc.variants || 1); v++) {
      const c = new NS.Circuit(); sc.build(c, { variant: v, rnd: NS.rng(1234 + v) });
      c.parts.forEach(p => { if (!p.dev) p.dev = NS.rng(c.seq * 31 + p.type.length + v * 7)() * 2 - 1; });
      const sim = new NS.Sim(c); sim.advance(0.05); // contrôle : le circuit se simule sans erreur
      const name = `${id}${(sc.variants || 1) > 1 ? '-v' + (v + 1) : ''}.json`;
      fs.writeFileSync(path.join(tp, name), JSON.stringify(NS.serialize(c)));
      files.push(name); nfiles++;
      page.push(`- [\`${name}\`](tp/${name})${(sc.variants || 1) > 1 ? ` — ${sc.variantLabel ? sc.variantLabel.replace('↻ ', '') + ' n° ' + (v + 1) : 'variante ' + (v + 1)}` : ''}`);
    }
    page.push('', `> **Version avec correction automatique :** dans ElectroLab, menu **TP ▾** → *${sc.title}*.`, '');
    files.forEach(f => links.push(f));
  }
  fs.writeFileSync(path.join(dir, '04-simulateur.md'), page.join('\n'));
  // .pages et README de la séance
  const pg = path.join(dir, '.pages'); let t = fs.readFileSync(pg, 'utf8').trimEnd() + '\n  - "🖥️ Simulateur ElectroLab": 04-simulateur.md\n'; fs.writeFileSync(pg, t);
  const rd = path.join(dir, 'README.md'); fs.writeFileSync(rd, fs.readFileSync(rd, 'utf8').trimEnd() + '\n| [🖥️ Simulateur ElectroLab](04-simulateur.md) | Exercices / TP simulés (fichiers `.json`) |\n');
  console.log(key, sdir, links.length, 'fichiers');
}
console.log('total fichiers :', nfiles);
