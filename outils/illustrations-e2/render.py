"""Génère les PNG (x2) des illustrations E2.

Usage :  python3 render.py [dossier_sortie] [nom_figure ...]
Prérequis : pip install playwright (+ chromium) ; police Inter installée.
"""
import importlib
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

MODULES = ["figs01", "figs02", "figs04", "figs07", "figs_sec", "figs_sec2", "figs_sym", "figs_sec3"]


def collect():
    figs = {}
    for m in MODULES:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError as e:
            if e.name == m:
                continue
            raise
        figs.update(mod.FIGS)
    return figs


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "sortie"
    only = set(sys.argv[2:])
    out.mkdir(parents=True, exist_ok=True)
    figs = collect()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(device_scale_factor=2)
        page = ctx.new_page()
        for name, fn in figs.items():
            if only and name not in only:
                continue
            svg = fn()
            page.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
            page.wait_for_timeout(60)
            page.locator("svg").first.screenshot(path=str(out / f"{name}.png"), omit_background=True)
            print("ok", name)
        browser.close()


if __name__ == "__main__":
    main()
