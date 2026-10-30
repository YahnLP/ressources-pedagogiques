"""Corrections de fond du contenu importé (erreurs factuelles / incohérences).
Usage : python3 corrections.py <racine>   — appelé par regenerer.sh après le nettoyage."""
import sys, pathlib

# (fichier relatif à docs/, ancien texte, nouveau texte)
CORR = [
    # HC-05 : le mode AT s'obtient avec KEY (EN) à l'état haut à la mise sous tension (cohérent avec S14)
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md",
     "| KEY | GND ou bouton vers GND | Maintenir à GND pour forcer le mode AT |",
     "| KEY (EN) | 3,3 V ou bouton vers 3,3 V | Maintenir à l'état haut (3,3 V) à la mise sous tension pour forcer le mode AT |"),
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md",
     "(broche KEY maintenue à GND ou niveau bas au démarrage)",
     "(broche KEY maintenue à l'état haut, 3,3 V, à la mise sous tension)"),
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md",
     "Vérifier que KEY est bien à GND et baud rate = 38400 en AT",
     "Vérifier que KEY est bien à l'état haut (3,3 V) à la mise sous tension et baud rate = 38400 en AT"),
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md",
     "Vérifier KEY=GND + baud rate = 38400",
     "Vérifier KEY à l'état haut (3,3 V) + baud rate = 38400"),
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md",
     "en mode AT, KEY à GND",
     "en mode AT, KEY à 3,3 V"),
    ("seconde/S13-communication-serie-uart-protocol/annexe-reference-sketches-commandes-at.md",
     "KEY  → GND (force le mode AT)", "KEY  → 3,3 V (force le mode AT)"),
    ("seconde/S13-communication-serie-uart-protocol/annexe-reference-sketches-commandes-at.md",
     "Vérifier : KEY du HC-05 est relié à GND", "Vérifier : KEY du HC-05 est relié au 3,3 V à la mise sous tension"),
    ("seconde/S13-communication-serie-uart-protocol/annexe-reference-sketches-commandes-at.md",
     "GND ────────────────────────────────── KEY  (mode AT)", "3,3V ──────────────────────────────── KEY  (mode AT)"),
    ("seconde/S13-communication-serie-uart-protocol/annexe-reference-sketches-commandes-at.md",
     "KEY doit être LIBRE (non câblé à GND)", "KEY doit être LIBRE (non relié au 3,3 V)"),
    # HC-05 : la vitesse se lit/règle avec AT+UART (AT+BAUD est une syntaxe de HC-06)
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md", "| `AT+BAUD?` | `+BAUD:4` | Lire le baud rate (4 = 9600) |", "| `AT+UART?` | `+UART:9600,0,0` | Lire le baud rate, le bit de stop et la parité |"),
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md", "| `AT+BAUD8` | `OK` | Passer le baud rate à 115200 (code 8) |", "| `AT+UART=115200,0,0` | `OK` | Passer le baud rate à 115200 (1 stop, sans parité) |"),
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md", "`AT+NAME?` · `AT+BAUD?` · `AT+RESET`", "`AT+NAME?` · `AT+UART?` · `AT+RESET`"),
    ("seconde/S13-communication-serie-uart-protocol/01-cours.md", "**Tableau des codes baud rate HC-05 :**\n\n| Code AT | Baud rate | Usage |\n|---|---|---|\n| 1 | 1200 | — |\n| 2 | 2400 | — |\n| 3 | 4800 | — |\n| **4** | **9600** | **Standard Arduino** |\n| 5 | 19200 | — |\n| 6 | 38400 | Mode AT |\n| 7 | 57600 | — |\n| **8** | **115200** | **Haut débit** |",
     "**Format de la commande de vitesse du HC-05 :** `AT+UART=<baud>,<stop>,<parité>`\n\n| Exemple | Effet |\n|---|---|\n| `AT+UART=9600,0,0` | 9600 bauds, 1 bit de stop, sans parité (**standard Arduino**) |\n| `AT+UART=38400,0,0` | 38400 bauds (vitesse du mode AT) |\n| `AT+UART=115200,0,0` | 115200 bauds (**haut débit**) |"),
    ("seconde/S13-communication-serie-uart-protocol/annexe-reference-sketches-commandes-at.md", "| `AT+BAUD?` | Requête | — | `+BAUD:4` |\n| `AT+BAUD<code>` | Config | Code 1-8 | `OK` |\n", ""),
    # Oscilloscope du lycée : Owon SDS5032E-V (30 MHz, 2 voies)
    ("terminale/S11-interpreter-document-mesures-carte/02-tp.md", "Rigol DS1054Z ou équivalent", "Owon SDS5032E-V ou équivalent"),
    ("terminale/S07-validation-conformite-pv-professionnel/01-cours.md", "Rigol DS1054Z  |  N°DS1054-2026-09", "Owon SDS5032E-V  |  N°SDS5032-2026-09"),
    ("terminale/S07-validation-conformite-pv-professionnel/03-exercices.md", "| TC-02 | Fréquence NE555 (Hz) | Rigol DS1054Z, Cl.0,1%", "| TC-02 | Fréquence NE555 (Hz) | Owon SDS5032E-V, Cl.0,1%"),
    ("terminale/S07-validation-conformite-pv-professionnel/03-exercices.md", "| TC-04 | Rapport cyclique (%) | Rigol DS1054Z, Cl.0,1%", "| TC-04 | Rapport cyclique (%) | Owon SDS5032E-V, Cl.0,1%"),
]


def main(root):
    docs = pathlib.Path(root) / "docs"
    manque = 0
    for f, ancien, nouveau in CORR:
        p = docs / f
        t = p.read_text(encoding="utf-8")
        if ancien not in t:
            print("introuvable :", f, "|", ancien[:50]); manque += 1; continue
        p.write_text(t.replace(ancien, nouveau), encoding="utf-8")
    print("corrections appliquées", len(CORR) - manque, "/", len(CORR))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
