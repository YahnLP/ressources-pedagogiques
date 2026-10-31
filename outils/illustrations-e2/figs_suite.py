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
    for idx, card in enumerate(cards):
        n, t, lines, full = card[:4]; ckw = card[4] if len(card) > 4 else kw
        col = PAL[idx % len(PAL)]
        h = 58 + max(len(lines), 1) * 25 + 16
        if full:
            y = max(y_left, y_right); x, w = LX, FW
            y_left = y_right = y + h + 18
        elif y_left <= y_right:
            y, x, w = y_left, LX, CW; y_left += h + 18
        else:
            y, x, w = y_right, RX, CW; y_right += h + 18
        placed.append((x, y, w, h, n, t, lines, col, ckw))
    total = max(y_left, y_right)
    o += f'<rect x="40" y="24" width="1120" height="{total-4}" rx="16" fill="#fff" stroke="#c7d0e2" stroke-width="3"/>'
    o += f'<rect x="40" y="24" width="1120" height="80" rx="16" fill="{INK}"/><rect x="40" y="70" width="1120" height="34" fill="{INK}"/>' + T(70, 76, title, 26, 800, "#fff", "start") + T(1130, 70, ref, 16, 700, "#cbd5ff", "end")
    for x, y, w, h, n, t, lines, col, ckw in placed:
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{col}" opacity=".06"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" stroke="{col}" stroke-width="2.5"/>'
        o += badge(x + 26, y + 28, n, col, 15) + T(x + 52, y + 34, t, 16, 800, col, "start")
        for k, (a, b) in enumerate(lines):
            yy = y + 66 + k * 25
            if b is None: o += T(x + 18, yy, a, 15, 600, INK, "start")
            else: o += T(x + 18, yy, a, 14, 700, MUTED, "start") + T(x + 18 + ckw, yy, b, 14, 700, INK, "start")
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


def _station(nv2, cname="C_dec"):
    o = f'<rect x="440" y="70" width="320" height="400" rx="14" fill="#fff" stroke="{RED}" stroke-width="4"/><rect x="440" y="70" width="320" height="40" rx="14" fill="{RED}"/>' + T(600, 98, "ESP32 DevKit v1", 18, 800, "#fff")
    pins_l = (("GPIO4", 170), ("3V3", 380)); pins_r = [("GPIO2", 170)] + ([("GPIO5", 260)] if nv2 else [])
    for n, y in pins_l: o += s_wire([(400, y), (440, y)]) + T(452, y + 6, n, 15, 800, INK, "start")
    for n, y in pins_r: o += s_wire([(760, y), (800, y)]) + T(748, y + 6, n, 15, 800, INK, "end")
    o += s_wire([(400, 170), (260, 170)]) + dot(300, 170) + s_wire([(300, 170), (300, 142)]) + sym("R", 300, 112, 90) + T(335, 118, "R_pullup", 14, 800, INK, "start") + s_wire([(300, 92), (300, 70)], RED) + f'<line x1="276" y1="70" x2="324" y2="70" stroke="{RED}" stroke-width="4"/>' + T(300, 58, "3V3", 14, 800, RED)
    o += s_wire([(300, 170), (300, 200)]) + block(230, 200, 140, 70, "DHT22", "capteur", BLUE) + s_wire([(300, 270), (300, 290)]) + gnd(300, 290)
    def led(y, rn, ln):
        return s_wire([(800, y), (850, y)]) + sym("R", 890, y) + T(890, y - 26, rn, 14, 800, INK) + s_wire([(930, y), (990, y)]) + sym("LED", 1030, y, s=1.1) + T(1030, y - 54, ln, 14, 800, INK) + s_wire([(1074, y), (1130, y), (1130, y + 20)]) + gnd(1130, y + 20)
    o += led(170, "R_LED", "LED")
    if nv2: o += led(260, "R_IR", "LED_IR")
    o += T(40, 386, "USB 5 V", 15, 800, RED, "start") + s_wire([(120, 380), (150, 380)], RED) + block(150, 345, 120, 70, "AMS1117", "régulateur", AMBER) + s_wire([(270, 380), (440, 380)])
    o += dot(320, 380) + s_wire([(320, 380), (320, 410)]) + sym("C", 320, 445, 90) + T(278, 450, cname, 14, 800, INK, "end") + s_wire([(320, 465), (320, 480)]) + gnd(320, 480)
    if nv2: o += dot(390, 380) + s_wire([(390, 380), (390, 410)]) + sym("R", 390, 445, 90) + T(390, 538, "R_charge", 14, 800, INK) + s_wire([(390, 465), (390, 480)]) + gnd(390, 480)
    return o


def f_station_final():
    o = _station(False)
    o += s_wire([(760, 250), (940, 250), (940, 308)]) + T(748, 256, "GPIO34", 15, 800, INK, "end") + T(960, 250, "curseur du potentiomètre", 14, 700, MUTED, "start")
    o += s_wire([(760, 340), (906, 340)]) + T(748, 346, "GPIO5", 15, 800, INK, "end") + sym("POT", 940, 340) + T(940, 400, "R_pot = potentiomètre 10 kΩ", 14, 800, INK) + s_wire([(974, 340), (1130, 340), (1130, 360)]) + gnd(1130, 360)
    o += dot(390, 380) + s_wire([(390, 380), (390, 410)]) + sym("R", 390, 445, 90) + T(390, 538, "R_charge", 14, 800, INK) + s_wire([(390, 465), (390, 480)]) + gnd(390, 480)
    return figure(W, 570, o)


def f_station_sonde(): return figure(W, 570, _station(False, "C1"))
def f_station_nv2(): return figure(W, 570, _station(True))


def f_mes_vierge():
    b = "_______"
    cards = [
        (1, "IDENTIFICATION", [("Client", "Coopérative AGROSMART"), ("Site", "Serre n°3 – TP Labo"), ("Date d'installation", "2026-___-___"), ("Intervenant(s)", "__________________")], False),
        (2, "MATÉRIELS INSTALLÉS", [("U1", "ESP32 DevKit v1 · n° série " + b + " · v____"), ("U2", "_____________ · n° série " + b), ("U3", "LED ×3 (V / O / R)")], False, 40),
        (3, "PARAMÈTRES CONFIGURÉS", [("Seuil WARNING, activation", "T > ____ °C"), ("Seuil WARNING, désactivation", "T < ____ °C (hystérésis)"), ("Seuil CRITICAL, activation", "T > ____ °C"), ("Seuil CRITICAL, désactivation", "T < ____ °C"), ("Anti-rebond", "____ secondes"), ("Moyenne mobile", "N = ____ points"), ("Fréquence de publication", "____ secondes")], False),
        (4, "TESTS DE VALIDATION", [("TC-001 · Lecture du capteur", "affiché ____ °C · réf. ____ °C · écart ____ °C  ☐ PASS (< 1 °C)  ☐ FAIL"), ("TC-002 · Alarme WARNING (T > 32 °C simulée)", "délai mesure → LED orange : ____ s  ☐ PASS  ☐ FAIL"), ("TC-003 · Retour à NORMAL", "LED verte à ____ °C  ☐ PASS  ☐ FAIL"), ("TC-004 · KPI moyenne mobile", "t_raw = ____ °C · t_moy = ____ °C · cohérent ?  ☐ Oui  ☐ Non"), ("TC-005 · Courbe de tendance", "☐ générée dans le tableur   ☐ tendance visible")], True, 400),
        (5, "OBSERVATIONS", [("______________________________________", None), ("______________________________________", None)], False),
        (6, "DÉCLARATION", [("☐  OPÉRATIONNEL : tous les tests validés", None), ("☐  OPÉRATIONNEL AVEC RÉSERVE : ____________", None), ("☐  NON OPÉRATIONNEL : défauts ____________", None)], False),
        (7, "SIGNATURES", [("Installateur", "______________   Date : ________"), ("Validateur", "______________   Date : ________")], False),
    ]
    return doc_figure("FICHE DE MISE EN SERVICE (à remplir)", "Réf. MES-2026-SERRE-___", cards, 270)


def f_page_garde():
    cards = [(1, "IDENTITÉ", [("Apprenti(e)", "_______________________"), ("Formation", "BAC PRO CIEL — CFA ______________"), ("Entreprise", "_______________________"), ("Tuteur", "_______________________"), ("Formateur E2", "_______________________")], False),
             (2, "DOSSIER", [("Module", "Systèmes embarqués, électronique"), ("Unités", "U21 systèmes embarqués · U22 qualité"), ("Période", "Sept. 2024 – Juin 2026 (A2 + A3)"), ("Version", "1.0 — Date : ________")], False, 90)]
    return doc_figure("DOSSIER DE COMPÉTENCES E2", "Page de garde", cards, 150)


def f_fiche_preuve():
    cards = [(1, "DOCUMENT / FICHIER", [("Document / fichier", "________________________________"), ("Séance d'origine", "___-A_ (ex. S6-A3)"), ("Date de production", "2026-___-___")], False),
             (2, "CE QUE ÇA PROUVE", [("Cette preuve démontre que je sais ____________________________", None), ("______________________________________ car", None), ("______________________________________.", None)], False),
             (3, "CE QUI ÉTAIT DIFFICILE ET COMMENT J'AI SURMONTÉ", [("______________________________________________________", None), ("______________________________________________________", None)], True),
             (4, "LIEN AVEC L'ENTREPRISE (si applicable)", [("J'ai utilisé / vu cette compétence en entreprise lors de ______________", None), ("______________________________________________________", None)], True)]
    return doc_figure("FICHE DE PREUVE", "Compétence : ______________________________", cards, 170)


def f_grr():
    b = "_______"
    cards = [(1, "RÉPÉTABILITÉ (EV)", [("σ_A", b + " °C"), ("σ_B", b + " °C"), ("σ_EV", b + " °C")], False),
             (2, "REPRODUCTIBILITÉ (AV)", [("x̄_A", b + " °C"), ("x̄_B", b + " °C"), ("AV", b + " °C"), ("σ_AV", b + " °C")], False),
             (3, "GRR TOTAL", [("σ_GRR", b + " °C"), ("%GRR", b + " %"), ("Verdict", "☐ EXCELLENT  ☐ ACCEPTABLE  ☐ INACCEPTABLE")], False, 80),
             (4, "LIMITE DE DÉTECTION", [("σ_bruit", b + " °C"), ("LD", b + " °C"), ("Apte à détecter ± 1 °C", "☐ OUI  ☐ NON")], False),
             (5, "CONCLUSION", [("Le DHT22 est  ☐ APTE  ☐ NON APTE  pour surveiller la salle technique", None)], True),
             (6, "SIGNATURE", [("Signature", "___________________   Date : _______________")], True)]
    return doc_figure("ÉTUDE GAUGE R&R — DHT22", "Opérateur A : ________ · B : ________", cards, 190)


FIGS = {"hc05_cablage_at": f_hc05_at, "hc05_cablage_normal": f_hc05_normal, "grille_oscillo_vierge": f_grille_oscillo, "rbd_pesee": f_rbd_pesee, "pv_validation": f_pv_validation, "config_dat": f_config_dat, "station_sonde": f_station_sonde, "station_nv2": f_station_nv2, "station_final": f_station_final, "mes_vierge": f_mes_vierge, "page_garde": f_page_garde, "fiche_preuve": f_fiche_preuve, "grr_synthese": f_grr}
