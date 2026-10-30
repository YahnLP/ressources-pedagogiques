"""Terminale S11 : valeurs attendues de la partie 0 (calculs préalables) et des mesures A2/B2 — d'après le schéma du dossier."""
F = '02-tp.md'
VA = "Valeurs attendues"
E = lambda t, l: ('terminale', 'S11', F, t, l, VA)
ENTREES = [
    E('### 0.1', [
        "| Bloc | Nom | Fonction | Composant principal |", "|---|---|---|---|",
        "| 1 | Alimentation | Transformer 12 V en 5 V régulés | Régulateur 7805 |",
        "| 2 | Oscillateur | Générer un signal carré de 1 Hz environ (astable) | NE555 |",
        "| 3 | Indicateur | Visualiser le clignotement | LED1 + R3 |"]),
    E('### 0.2', [
        "Valeurs lues sur le schéma : $R_a = 10\\,\\mathrm{k\\Omega}$, $R_b = 68\\,\\mathrm{k\\Omega}$, $C_3 = 10\\,\\mathrm{\\mu F}$.  ",
        "**Q0.2.1** — $f = \\dfrac{1{,}44}{(10\\,000 + 2 \\times 68\\,000) \\times 10 \\times 10^{-6}} = \\dfrac{1{,}44}{1{,}46} \\approx 0{,}986\\,\\mathrm{Hz}$.  ",
        "**Q0.2.2** — $t_{High} = 0{,}693 \\times 78\\,000 \\times 10 \\times 10^{-6} \\approx 0{,}541\\,\\mathrm{s}$ ; $t_{Low} = 0{,}693 \\times 68\\,000 \\times 10 \\times 10^{-6} \\approx 0{,}471\\,\\mathrm{s}$ ; $T \\approx 1{,}012\\,\\mathrm{s}$ ; $f = \\dfrac{1}{T} \\approx 0{,}988\\,\\mathrm{Hz}$ (le léger écart avec 0,986 Hz vient de l'arrondi de la constante 1,44).  ",
        "**Q0.2.3** — $DC = \\dfrac{10 + 68}{10 + 2 \\times 68} = \\dfrac{78}{146} \\approx 0{,}534 = 53{,}4\\,\\%$. La LED est allumée environ **53 %** du temps."]),
    E('### 0.3', [
        "**Q0.3.1** — $R_3 = 150\\,\\Omega$ ; $I_F = \\dfrac{5 - 2}{150} = 20\\,\\mathrm{mA}$. Courant max absolu : **30 mA** ; nominal cible : **20 mA**. Le courant calculé est égal à la cible : **dans la tolérance**.  ",
        "**Q0.3.2** — Oui : 12 V est dans la plage [7 V ; 35 V].  ",
        "**Q0.3.3** — $P = (12 - 5) \\times 0{,}035 = 0{,}245\\,\\mathrm{W}$. **Non**, pas de radiateur nécessaire : avec $R_{\\theta ja} \\approx 65\\,°\\mathrm{C/W}$, l'échauffement est d'environ 16 °C."]),
    E('### Mesure A2', [
        "$V_{out}$ reste très proche de 5 V (écart de quelques mV seulement) pour $V_{in}$ de 8 V à 14 V : cette propriété s'appelle la **régulation de ligne** (réjection des variations de l'entrée).  ",
        "À $V_{in} = 8\\,\\mathrm{V}$ : marge $= 8 - 5 = 3\\,\\mathrm{V} \\geq 2\\,\\mathrm{V}$ → **suffisante**."]),
    E('### Mesure B2', [
        "Forme : **dents de scie arrondies** (charge et décharge exponentielles).  ",
        "Avec $V_{cc} = 5\\,\\mathrm{V}$ : $V_{min} = \\dfrac{5}{3} \\approx 1{,}67\\,\\mathrm{V}$ ; $V_{max} = \\dfrac{2 \\times 5}{3} \\approx 3{,}33\\,\\mathrm{V}$. Les mesures doivent être proches (écart de quelques dizaines de mV)."]),
]
