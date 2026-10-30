/* Rendu des formules (KaTeX hébergé sur le site : aucune requête vers un tiers). */
function renderMaths() {
  if (typeof renderMathInElement !== "function") return;
  renderMathInElement(document.body, {
    delimiters: [{ left: "\\[", right: "\\]", display: true }, { left: "\\(", right: "\\)", display: false }],
    throwOnError: false
  });
}
if (window.document$) document$.subscribe(renderMaths); else document.addEventListener("DOMContentLoaded", renderMaths);
