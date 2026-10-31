"""Suite des schémas « manuel » : HC-05 AT/normal, grille oscillo vierge, RBD pesée."""
from hl import *
from figs07 import block
from figs_prem import mk_rbd

W = 1200


def _hc05(mode_at):
    o = block(60, 50, 280, 490, "", None, BLUE) + block(860, 50, 280, 490, "", None, AMBER) + T(200, 90, "Arduino UNO", 22, 800, INK) + T(1000, 90, "HC-05", 22, 800, INK)
    for l, y in (("5V", 120), ("GND", 190), ("D11 (TX)", 270), ("D10 (RX)", 440), ("3,3V" if mode_at else "—", 490)): o += T(330, y + 6, l, 20, 800, INK, "end")
    for l, y in (("VCC", 120), ("GND", 190), ("RXD", 270), ("TXD", 440), ("KEY (EN)", 490)): o += T(870, y + 6, l, 20, 800, INK, "start")
    o += s_wire([(340, 120), (860, 120)], RED) + s_wire([(340, 190), (860, 190)], "#222")
    o += s_wire([(340, 270), (450, 270)]) + sym("R", 490, 270) + T(490, 242, "1 kΩ", 16, 800, INK) + s_wire([(530, 270), (860, 270)]) + dot(660, 270) + s_wire([(660, 270), (660, 300)]) + sym("R", 660, 340, 90) + T(700, 346, "2 kΩ", 16, 800, INK, "start") + s_wire([(660, 380), (660, 392)]) + gnd(660, 392)
    o += s_wire([(860, 440), (340, 440)], GREEN)
    if mode_at: o += s_wire([(340, 490), (860, 490)], AMBER) + T(600, 516, "KEY relié au 3,3 V : MODE AT (commandes)", 16, 800, AMBER)
    else: o += f'<line x1="780" y1="490" x2="860" y2="490" stroke="#9aa4b8" stroke-width="4" stroke-dasharray="6 6"/>' + T(600, 516, "KEY libre (non reliée) : mode communication normale", 16, 800, GREEN)
    o += T(600, 40, "diviseur 1 kΩ / 2 kΩ : 5 V → 3,3 V sur RXD", 16, 800, INK)
    return o


def f_hc05_at(): return figure(W, 570, _hc05(True))
def f_hc05_normal(): return figure(W, 570, _hc05(False))


def f_grille_oscillo():
    o = f'<rect x="70" y="40" width="880" height="340" rx="10" fill="#10151b"/>'
    for i in range(11): o += f'<line x1="{80+i*84}" y1="50" x2="{80+i*84}" y2="370" stroke="#26323e" stroke-width="{2 if i in (0,10) else 1}"/>'
    for j in range(9): o += f'<line x1="70" y1="{58+j*40}" x2="930" y2="{58+j*40}" stroke="#26323e" stroke-width="{2 if j in (0,8) else 1}"/>'
    o += f'<line x1="70" y1="218" x2="930" y2="218" stroke="#3c4d5e" stroke-width="2"/>'
    o += T(56, 66, "5 V", 15, 800, INK, "end") + T(56, 222, "2,5 V", 15, 800, INK, "end") + T(56, 362, "0 V", 15, 800, INK, "end") + T(500, 410, "temps →", 16, 800, MUTED)
    o += f'<rect x="980" y="40" width="190" height="340" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + T(1075, 74, "Échelles", 17, 800, INK) + T(1075, 118, "Vertical :", 14, 700, MUTED) + T(1075, 142, "1 V / division", 16, 800, INK) + T(1075, 190, "Horizontal :", 14, 700, MUTED) + T(1075, 214, "à compléter", 16, 800, INK) + T(1075, 262, "Dessine le signal", 14, 700, MUTED) + T(1075, 284, "observé en", 14, 700, MUTED) + T(1075, 306, "respectant", 14, 700, MUTED) + T(1075, 328, "les divisions", 14, 700, MUTED)
    return figure(W, 440, o)


def f_rbd_pesee():
    return mk_rbd([("Capteur A", "R = 0,88"), ("Capteur B", "R = 0,82")], [("IHM", "R = 0,97"), ("Réseau", "R = 0,99")])()


PAL = [BLUE, GREEN, AMBER, "#7c3aed", RED]


def doc_figure(title, ref, cards, kw=190):
    """Document « fiche » : bandeau + cartes numérotées sur deux colonnes (hauteur automatique).
    cards = [(numéro, titre, lignes, pleine_largeur)] ; ligne = (clé, valeur) ou (texte, None)."""
    LX, RX, CW, FW = 70, 620, 520, 1070
    o = ""
    y_left = y_right = 124
    placed = []
    for idx, (n, t, lines, full) in enumerate(cards):
        col = PAL[idx % len(PAL)]
        h = 58 + max(len(lines), 1) * 25 + 16
        if full:
            y = max(y_left, y_right); x, w = LX, FW
            y_left = y_right = y + h + 18
        elif y_left <= y_right:
            y, x, w = y_left, LX, CW; y_left += h + 18
        else:
            y, x, w = y_right, RX, CW; y_right += h + 18
        placed.append((x, y, w, h, n, t, lines, col))
    total = max(y_left, y_right)
    o += f'<rect x="40" y="24" width="1120" height="{total-4}" rx="16" fill="#fff" stroke="#c7d0e2" stroke-width="3"/>'
    o += f'<rect x="40" y="24" width="1120" height="80" rx="16" fill="{INK}"/><rect x="40" y="70" width="1120" height="34" fill="{INK}"/>' + T(70, 76, title, 26, 800, "#fff", "start") + T(1130, 70, ref, 16, 700, "#cbd5ff", "end")
    for x, y, w, h, n, t, lines, col in placed:
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{col}" opacity=".06"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" stroke="{col}" stroke-width="2.5"/>'
        o += badge(x + 26, y + 28, n, col, 15) + T(x + 52, y + 34, t, 16, 800, col, "start")
        for k, (a, b) in enumerate(lines):
            yy = y + 66 + k * 25
            if b is None: o += T(x + 18, yy, a, 15, 600, INK, "start")
            else: o += T(x + 18, yy, a, 14, 700, MUTED, "start") + T(x + 18 + kw, yy, b, 14, 700, INK, "start")
    return figure(W, total + 24, o)


def f_pv_validation():
    sig = [("Validateur", "________________   Date : ____________"), ("Responsable Q.", "________________   Date : ____________"), ("Client", "________________   Date : ____________")]
    cards = [
        (1, "IDENTIFICATION DU PRODUIT", [("Produit", "Carte minuterie LED NE555/7805"), ("Référence", "ASM-DEMO-001 / Rev.1"), ("N° lot", "LOT-20260322-003"), ("Client", "ELECTROPRO SAS")], False),
        (2, "RÉFÉRENTIELS APPLIQUÉS", [("Cahier des charges", "CdC-DEMO-001 Rev.A"), ("Norme assemblage", "IPC-A-610 Classe 2"), ("Norme conception", "IPC-2221 Classe B"), ("Norme essais", "Procédure interne PROC-TEST-001")], False),
        (3, "CONDITIONS D'ESSAI", [("Date", "2026-03-22"), ("Lieu", "Labo électronique CFA"), ("Température", "22 °C ± 2 °C"), ("Hygrométrie", "48 % HR ± 10 %")], False),
        (4, "INSTRUMENTS UTILISÉS", [("Multimètre", "Fluke 87V · n° 7435280 · classe 0,5 %"), ("Oscilloscope", "Owon SDS5032E-V · n° SDS5032-2026-09"), ("Alimentation", "PS305D · n° ALI-2026-05 · classe 1 %"), ("Tous les instruments sont dans leur période d'étalonnage valide.", None)], False),
        (5, "RÉSULTATS DE VALIDATION", [("Voir le tableau de la section suivante", None)], False),
        (6, "INSPECTION VISUELLE IPC-A-610", [("Voir la section dédiée", None)], False),
        (7, "CONCLUSION GLOBALE", [("☐  CONFORME au cahier des charges", None), ("☐  NON CONFORME — défauts : ______________", None), ("☐  CONFORME AVEC RÉSERVE", None)], False),
        (8, "SIGNATURES", sig, False),
    ]
    return doc_figure("PROCÈS-VERBAL DE VALIDATION FONCTIONNELLE", "Réf. PVF-2026-NE555-001", cards, 170)


def f_config_dat():
    cards = [
        (1, "8.1  RÉSEAU ET CONNECTIVITÉ", [("SSID Wi-Fi", "[NOM_RESEAU] (jamais le mot de passe)"), ("Fréquence", "2,4 GHz (IEEE 802.11 b/g/n)"), ("Adresse IP", "DHCP (assignée dynamiquement)"), ("Hostname", "industech-machine-01")], False),
        (2, "8.2  AWS IOT CORE", [("Endpoint", "xxxxxx-ats.iot.eu-west-1.amazonaws.com"), ("Port", "8883 (MQTT TLS)"), ("Client ID", "industech-machine-01"), ("Certificats", "dans le firmware (voir Annexe A)"), ("Région AWS", "eu-west-1")], False),
        (3, "8.3  TOPICS MQTT", [("Publication data", "industech/machine01/capteurs"), ("Publication status", "industech/machine01/status"), ("Subscription cmd", "industech/machine01/commande"), ("LWT", "…/status → {\"status\":\"offline\"}"), ("QoS publication", "1 (au moins une fois)")], False),
        (4, "8.4  SEUILS DE MAINTENANCE", [("Seuil d'alerte", "vibration > 2,5 g (RMS)"), ("Seuil critique", "vibration > 4,0 g (arrêt préventif)"), ("MTBF cible", "> 60 min (surveillance normale)"), ("Fréquence publication", "5 secondes")], False),
        (5, "8.5  CLOUDWATCH", [("Espace de noms", "Industrie40/CIEL"), ("Métriques", "Vibration, Temperature, MTBF_min, NbAlarmes"), ("Alarme", "Vibration > 2,5 pendant 2 périodes consécutives → SNS"), ("Dashboard", "Dashboard-IoT-CIEL-Machine01")], True),
    ]
    return doc_figure("SECTION 8 — CONFIGURATION", "DAT · exemple de table de configuration", cards, 190)


FIGS = {"hc05_cablage_at": f_hc05_at, "hc05_cablage_normal": f_hc05_normal, "grille_oscillo_vierge": f_grille_oscillo, "rbd_pesee": f_rbd_pesee, "pv_validation": f_pv_validation, "config_dat": f_config_dat}
