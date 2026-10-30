"""Importe les fiches élèves E2 (cours, TP, exercices, annexes) dans docs/ au format du dépôt modèle.

Usage : python3 importer.py <dossier_source_E2> <racine_du_depot>
Seuls les fichiers élèves déjà filtrés dans le dossier source sont lus.
Les sections « correction / document enseignant » éventuellement incluses en fin de fichier sont retirées.
"""
import re
import shutil
import sys
import unicodedata
from pathlib import Path

SRC = Path(sys.argv[1])
REPO = Path(sys.argv[2])
DOCS = REPO / "docs"

YEARS = {"1": ("seconde", "Seconde", "🌱"), "2": ("premiere", "Première", "🌿"), "3": ("terminale", "Terminale", "🌳")}
OVERRIDE = {("1", 1): "Code couleurs des résistances et loi d'Ohm", ("1", 10): "Moteur DC, PWM et pont en H L293D",
            ("1", 12): "Tests au multimètre et contrôle qualité PCB", ("1", 9): "Capteur LM35 : analogRead et conversion ADC"}
ACRO = ["PCB", "IPC", "LCD", "HC-05", "DHT11", "DHT22", "IEC", "UART", "ESP32", "MQTT", "KiCad", "CEM", "MTBF", "BOM", "PV", "CCF", "DAT", "IoT",
        "NV2", "TP", "DC", "PWM", "I2C", "LED", "AT", "NE555", "E2", "A1", "A2", "A3", "I40", "CLIMASENS", "CdC", "R&R", "KPI", "MES", "LM35"]
ROLE_LABEL = {"cours": "📖 Cours", "tp": "🛠️ TP", "exo": "📝 Exercices et ateliers", "annexe": "📎"}
ROLE_DESC = {"cours": "Fiche de cours élève", "tp": "Fiche de TP", "exo": "Exercices / ateliers", "annexe": "Document de référence"}
EMOJI = re.compile(r"[\U0001F000-\U0001FFFF☀-➿️‍]+")
removed_illus = []
cut_log = []


def fold(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def clean_title(t):
    t = EMOJI.sub("", t).strip(" #*·—-")
    t = re.sub(r"\s+[—-]\s+À PLASTIFIER.*$", "", t)
    t = re.sub(r"\s+[—·-]\s+S\d+.*$", "", t) if re.search(r"[A-ZÉ]{4}", t) else t
    words = t.split()
    for i, w in enumerate(words):
        core = re.sub(r"[^\wÀ-ÿ]", "", w)
        if len(core) > 3 and core.isupper() and core not in ACRO:
            words[i] = w.capitalize() if i == 0 else w.lower()
    t = " ".join(words)
    for a in ACRO:
        t = re.sub(rf"(?i)(?<![\w]){re.escape(a)}(?![\w])", a, t)
    return t.strip()


def role_of(name):
    n = name.lower()
    if re.search(r"(^|_)(tp|td)(_|\.)", n):
        return "tp"
    if "cours" in n or "rappel" in n:
        return "cours"
    if any(k in n for k in ("exercices", "atelier", "parcours", "sprint", "revision")):
        return "exo"
    return "annexe"


def strip_illus(text, fname):
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("> **[ILLUSTRATION") or l.startswith("> **Prompt image IA"):
            j = i
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            # retire le bloc ``` IMAGE ... ``` qui précède
            title = ""
            k = len(out) - 1
            while k >= 0 and out[k].strip() == "":
                k -= 1
            if k >= 2 and out[k].strip() == "```" and out[k - 2].strip() == "```":
                title = out[k - 1].strip()
                del out[k - 2:]
            removed_illus.append((fname, title or "(figure)"))
            i = j
            continue
        out.append(l)
        i += 1
    return "\n".join(out)


CUT = re.compile(r"^(#{1,2}) ✅ (CORRECTION|CORRECTIONS|Corrections?)\b.*$|^## ✅ Retour enseignant.*$")


def strip_corrections(text, fname):
    lines = text.split("\n")
    for n, l in enumerate(lines):
        if CUT.match(l):
            cut_log.append((fname, n + 1, len(lines)))
            return "\n".join(lines[:n]).rstrip() + "\n"
    return text


def process(path):
    t = path.read_text(encoding="utf-8")
    t = strip_corrections(t, path.name)
    t = strip_illus(t, path.name)
    t = re.sub(r" ?:contentReference\[oaicite:\d+\]\{index=\d+\}", "", t)
    t = re.sub(r"\n{4,}", "\n\n\n", t)
    return t


def first_headings(text):
    h = [l for l in text.split("\n") if re.match(r"^#{1,2} ", l)]
    h1 = h[0].lstrip("# ") if h else ""
    h2 = h[1].lstrip("# ") if len(h) > 1 and h[1].startswith("## ") else ""
    return h1, h2


def write_pages(d, entries):
    nav = ["nav:", "  - README.md"] + [f'  - "{lab}": {fn}' for fn, lab in entries]
    return nav


def main():
    year_rows = {}
    for ydir in sorted(SRC.glob("Annee *")):
        y = ydir.name.split()[-1]
        ykey, yname, yemoji = YEARS[y]
        ydocs = DOCS / ykey
        ydocs.mkdir(parents=True, exist_ok=True)
        rows = []
        for sdir in sorted(ydir.glob("S*"), key=lambda p: int(p.name[1:])):
            n = int(sdir.name[1:])
            files = sorted(sdir.glob("*.md"))
            if not files:
                continue
            roles = {}
            for f in files:
                roles.setdefault(role_of(f.name), []).append(f)
            main_f = (roles.get("cours") or roles.get("tp") or roles.get("exo") or roles.get("annexe"))[0]
            h1, h2 = first_headings(main_f.read_text(encoding="utf-8"))
            title = OVERRIDE.get((y, n)) or clean_title(h2 or h1)
            slug = fold(title)
            if len(slug) > 40:
                slug = slug[:40].rsplit("-", 1)[0]
            sd = ydocs / f"S{n:02d}-{slug}"
            sd.mkdir(parents=True, exist_ok=True)
            entries, docrows = [], []
            counter = {"cours": 0, "tp": 0, "exo": 0, "annexe": 0}
            for role in ("cours", "tp", "exo", "annexe"):
                for f in roles.get(role, []):
                    counter[role] += 1
                    k = counter[role]
                    if role == "annexe":
                        a1, a2 = first_headings(f.read_text(encoding="utf-8"))
                        lab = ROLE_LABEL["annexe"] + " " + clean_title(a1 or f.stem)
                        sl = fold(clean_title(a1 or f.stem)); sl = sl if len(sl) <= 40 else sl[:40].rsplit('-', 1)[0]; fn = f"annexe-{sl}.md"
                    else:
                        suffix = "" if len(roles[role]) == 1 else f"-{k}"
                        base = {"cours": "01-cours", "tp": "02-tp", "exo": "03-exercices"}[role]
                        fn = base + suffix + ".md"
                        lab = ROLE_LABEL[role] + (f" ({k})" if len(roles[role]) > 1 else "")
                    (sd / fn).write_text(process(f), encoding="utf-8")
                    entries.append((fn, lab))
                    docrows.append((lab, fn, ROLE_DESC[role]))
            (sd / ".pages").write_text(f'title: "S{n:02d} · {title}"\n' + "\n".join(write_pages(sd, entries)) + "\n", encoding="utf-8")
            readme = [f"# S{n:02d} – {title}", "", "| Élément | Détail |", "|---|---|", f"| **Niveau** | {yname} Bac Pro CIEL |", f"| **Séance** | S{n:02d} |", "| **Module** | E2 – Électronique |", "",
                      "## 📚 Contenu", "", "| Document | Rôle |", "|---|---|"]
            for lab, fn, desc in docrows:
                readme.append(f"| [{lab}]({fn}) | {desc} |")
            (sd / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
            rows.append((n, title, sd.name))
        year_rows[ykey] = (yname, yemoji, rows)
        intro = {"seconde": "Découvrir l'électronique pas à pas : composants, loi d'Ohm, schémas, soudure, Arduino, capteurs et premier projet.",
                 "premiere": "Concevoir et mettre en réseau : CAO (KiCad), PCB, ESP32, MQTT, Node-RED, cloud, fiabilité, CEM et projet A2.",
                 "terminale": "Se préparer à l'épreuve E2 : mesures et procès-verbaux, alimentation, validation, métrologie, remédiation."}[ykey]
        readme = [f"# {yemoji} {yname} – Électronique (E2)", "", intro, "", "## 📅 Progression", "", "| Séance | Thème | Contenu |", "|---|---|---|"]
        for n, title, dn in rows:
            readme.append(f"| **S{n:02d}** | {title} | [📘 Ouvrir]({dn}/README.md) |")
        (ydocs / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
        (ydocs / ".pages").write_text(f"title: {yname}\n", encoding="utf-8")
    # journal pour le suivi des illustrations à créer
    log = ["# Emplacements d'illustration retirés lors de l'import", "", "À créer (figures vectorielles) dans un second temps.", "", "| Fichier source | Figure prévue |", "|---|---|"]
    log += [f"| {f} | {t} |" for f, t in removed_illus]
    (REPO / "outils" / "import_e2" / "illustrations-a-creer.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print("sessions:", {k: len(v[2]) for k, v in year_rows.items()})
    print("illustrations retirées:", len(removed_illus))
    print("sections correction retirées:", len(cut_log))
    for c in cut_log:
        print("  cut", c)


main()
