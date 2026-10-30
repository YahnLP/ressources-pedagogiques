"""Blocs de code « simples » (``` sans langage), repérés ligne par ligne (robuste aux blocs ```cpp voisins)."""


class Block:
    def __init__(self, a, b, body): self._s = (a, b); self.body = body
    def span(self): return self._s
    def group(self, i=1): return self.body if i == 1 else None


def finditer(text):
    out = []; pos = 0; opened = None
    for line in text.split("\n"):
        ln = len(line) + 1
        if line.startswith("```"):
            if opened is None:
                opened = (pos, line[3:].strip(), pos + ln)
            else:
                a, lang, bstart = opened
                if lang == "":
                    out.append(Block(a, pos + len(line), text[bstart:pos - 1] if pos - 1 >= bstart else ""))
                opened = None
        pos += ln
    return out
