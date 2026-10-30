"""Terminale S01 : valeurs attendues du TP de mesure (comparer avec ses propres mesures)."""
VA = "Valeurs attendues"
ENTREES = [
    ('terminale', 'S01', '02-tp.md', '### 1.1 Mesure de résistances', ["R1 : plage acceptable de 9 500 Ω à 10 500 Ω (10 000 Ω ± 5 %). Écart % = |mesure − 10 000| / 10 000 × 100 ; dans la tolérance si l'écart est inférieur ou égal à 5 %.  ", "R2 : plage acceptable de 209 Ω à 231 Ω (220 Ω ± 5 %)."], VA),
    ('terminale', 'S01', '02-tp.md', '### 1.2 Mesure de tension', ["Tension 3V3 : plage de 3,135 V à 3,465 V (3,3 V ± 5 %).  ", "Exemple de calcul avec $V_{led} = 2{,}0\\,\\mathrm{V}$ : $I = \\dfrac{3{,}3 - 2{,}0}{220} \\approx 5{,}9\\,\\mathrm{mA}$ (à refaire avec ta mesure)."], VA),
    ('terminale', 'S01', '02-tp.md', '### 1.3 Test de la diode', ["Sens passant : environ 0,5 V à 0,7 V (diode fonctionnelle). Sens bloqué : « OL » ou « 1. » (pas de court-circuit)."], VA),
    ('terminale', 'S01', '02-tp.md', '### 1.4 Potentiomètre', ["Position min : ≈ 0 V ; position milieu : ≈ 1,65 V ; position max : ≈ 3,3 V. La tension varie bien entre 0 et 3,3 V : oui."], VA),
    ('terminale', 'S01', '02-tp.md', '### 2.3 Observer', ["Avec le doigt, la température augmente de quelques degrés ; elle revient à sa valeur initiale en quelques dizaines de secondes. Commentaire : le DHT22 a un temps de réponse lent (quelques secondes à plusieurs dizaines de secondes) : il ne suit pas les variations rapides."], VA),
    ('terminale', 'S01', '02-tp.md', '### 3.1 Observer', ["Fréquence : 50 Hz ; période : 20 ms ; amplitude haute ≈ 3,3 V ; amplitude basse ≈ 0 V ; rapport cyclique : 50 % (10 ms HIGH, 10 ms LOW)."], VA),
    ('terminale', 'S01', '02-tp.md', '### 3.2 Observer', ["Le bruit augmente quand la LED commute. Explication : la commutation de la LED fait varier le courant tiré sur l'alimentation 3V3 ; à cause de l'impédance de l'alimentation et des pistes, la tension 3V3 est perturbée (couplage par impédance commune). Un condensateur de découplage réduit ce bruit."], VA),
]
