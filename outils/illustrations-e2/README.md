# Illustrations E2

Sources Python des figures du dossier `BAC PRO CIEL/E2/images/` (SVG → PNG x2, police Inter).

```bash
pip install playwright && playwright install chromium
python3 render.py ../../sortie            # toutes les figures
python3 render.py ../../sortie multimetre # une seule
```

`lib.py` : composants réalistes et symboles normalisés ; `figs*.py` : une fonction par figure.
