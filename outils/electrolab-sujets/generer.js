// Génère les sujets ElectroLab (.json) du parcours à partir de circuits existants.
// Usage : ELECTROLAB_DIR=/chemin/vers/ElectroLab node outils/electrolab-sujets/generer.js <racine du dépôt>
// ElectroLab n'est jamais modifié : on n'utilise que son moteur, en lecture, pour VALIDER les sujets.
const fs = require('fs'), path = require('path');
const EL = process.env.ELECTROLAB_DIR || '/home/claude/yahnlp/ElectroLab';
const ROOT = process.argv[2] || '.';
const NS = require(path.join(EL, 'tests', 'load.js'))(); const { Sim } = NS;
const rd = f => JSON.parse(fs.readFileSync(path.join(ROOT, 'docs', f), 'utf8'));
const wr = (f, o) => { fs.mkdirSync(path.dirname(path.join(ROOT, 'docs', f)), { recursive: true }); fs.writeFileSync(path.join(ROOT, 'docs', f), JSON.stringify(o)); };
const SECONDE = 'seconde/S12-tests-au-multimetre-et-controle-qualite/tp/', ESS = 'essentiel-en-1-an/tp/';

/* 1) Alimentation de labo : mode CV puis mode CC (à partir de ohm.json) */
function alim(R, Ilim, V) {
  const o = rd('seconde/S01-code-couleurs-des-resistances-et-loi-d/tp/ohm.json');
  for (const p of o.parts) { if (p.type === 'psu') p.p = { V, Ilim, on: true }; if (p.type === 'resistor') p.p = { R, tol: 5, W: 0.5 }; }
  return o;
}
/* 2) Clignoteur NE555 (fil rouge) : 5 V -> fusible -> NE555 astable -> R3 -> LED, oscilloscope sur la sortie */
function clign(fault) {
  const c = NS.deserialize(rd('premiere/S04-pcb-double-face-metallisation/tp/ne555-v1.json'));
  const al = c.byRef('AL1'), ra = c.byRef('R1'), rb = c.byRef('R2'), cc = c.byRef('C1');
  al.p = { V: 5, Ilim: 0.2, on: true }; ra.p = { R: 10000, tol: 1, W: 0.25 }; rb.p = { R: 68000, tol: 1, W: 0.25 }; cc.p = Object.assign({}, cc.p, { C: 1e-5, tol: 1 }); ra.dev = rb.dev = cc.dev = 0;
  const f1 = c.add('fuse', 240, 100, { I: 0.5, R: 0.1, fast: true }, 'F1');
  const r3 = c.add('resistor', 660, 180, { R: 150, tol: 5, W: 0.25 }, 'R3');
  const d1 = c.add('led', 780, 280, { model: 'LED rouge' }, 'D1'); d1.rot = 90;
  // le +5 V passe maintenant par le fusible : on déplace les fils qui partaient de l'alimentation
  for (const w of c.wires) for (const e of [w.a, w.b]) if (e.c === al.id && e.p === 0) { e.c = f1.id; e.p = 1; }
  c.link('AL1', '+', 'F1', 'A', [[160, 100]]);
  c.link('U1', 'OUT', 'R3', 'A'); c.link('R3', 'B', 'D1', 'A', [[780, 180]]); c.link('D1', 'K', 'GND1', 'G', [[780, 420], [100, 420]]);
  if (fault === 'A') f1.fault = 'blown'; if (fault === 'B') rb.fault = 'open'; if (fault === 'C') ra.fault = 'open';
  return c;
}
/* mesure : tension de sortie du 7805, durée à l'état haut / bas de la sortie du 555, courant LED */
function mesure(c) {
  const s = new Sim(c); s.settle(0.2); const dt = 0.002, N = 6000; const out = [];
  for (let i = 0; i < N; i++) { s.advance(dt); out.push(s.vPin('U1', 'OUT')); }
  const up = []; for (let i = 1; i < out.length; i++) if (out[i - 1] < 2 && out[i] >= 2) up.push(i * dt);
  const per = up.length > 2 ? (up[up.length - 1] - up[1]) / (up.length - 2) : 0; const hi = out.filter(v => v >= 2).length / out.length;
  const vi = s.vPin('R3', 'A') - s.vPin('R3', 'B');
  return { Vcc: +s.vPin('U1', 'VCC').toFixed(2), T_s: +per.toFixed(3), f_Hz: per ? +(1 / per).toFixed(3) : 0, duty_pct: +(hi * 100).toFixed(0), Vout_haut: +Math.max(...out).toFixed(2), THR_now: +s.vPin('U1', 'THR').toFixed(2) };
}
if (require.main === module) {
  wr(SECONDE + 'alim-cv.json', alim(220, 0.05, 5)); wr(SECONDE + 'alim-cc.json', alim(100, 0.03, 5));
  for (const f of ['', 'A', 'B', 'C']) { const c = clign(f); wr(ESS + 'clignoteur' + (f ? '-panne-' + f : '') + '.json', NS.serialize(c)); console.log('clignoteur' + (f ? ' panne ' + f : ''), JSON.stringify(mesure(clign(f)))); }
}
module.exports = { alim, clign, mesure, NS };
