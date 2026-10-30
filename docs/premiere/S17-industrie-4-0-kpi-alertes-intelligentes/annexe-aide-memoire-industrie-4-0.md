# 🗂️ AIDE-MÉMOIRE INDUSTRIE 4.0 — À PLASTIFIER
## Dashboard · Alertes · Métrologie · BAC PRO CIEL · E2 · 2ᵉ année S17

---

> *Conserver pendant les TP et la rédaction du PV*

---

## 📊 KPI Industrie 4.0 — Indicateurs clés

```
OEE  = Disponibilité × Performance × Qualité (objectif > 85%)
TRS  = Taux de Rendement Synthétique (=OEE en français)
MTBF / MTTR : voir aide-mémoire S11
Uptime (%) = TO / (TO + TA) × 100
```

---

## 🔵 Requêtes InfluxDB Flux

```javascript
// Moyenne sur fenêtre glissante
from(bucket: "mon_bucket")
  |> range(start: -1h)
  |> filter(fn:(r)=>r._measurement=="table")
  |> filter(fn:(r)=>r._field=="temperature")
  |> mean()

// Agrégation par tranches de temps
  |> aggregateWindow(every: 10m, fn: mean, createEmpty: false)

// Écart-type
  |> stddev()

// Max et Min
  |> max()    ou    |> min()

Intervalle µ ± σ = 68% des mesures
Intervalle µ ± 2σ = 95% des mesures
Intervalle µ ± 3σ = 99,7% des mesures
```

---

## 🚦 Alertes multi-niveaux Node-RED

```javascript
// Ordre de vérification : CRITIQUE → ATTENTION → INFO
// (évite les doubles déclenchements)

if (valeur > CRIT_MAX || valeur < CRIT_MIN) {
    return [null, null, msg];  // Output 3 : CRITIQUE
}
if (valeur > ATTN_MAX || valeur < ATTN_MIN) {
    return [null, msg, null];  // Output 2 : ATTENTION
}
if (valeur > INFO_MAX || valeur < INFO_MIN) {
    return [msg, null, null];  // Output 1 : INFO
}
return [null, null, null];     // Normal → pas d'alerte
```

---

## 📏 PV Métrologie — Calculs

```
Biais (erreur systématique) :
  e̅ = Σei / n

Écart-type (fidélité) :
  σ = √[ Σ(ei²) / (n−1) ]

Incertitude type :
  u = σ / √n

Incertitude élargie (k=2 → 95%) :
  U = 2 × u

Résultat final :
  T = (valeur_moyenne ± U) °C

Conformité : |e̅| + U ≤ spécification constructeur ?
```

---

## 📋 Structure du PV

```
1. Page de garde (référence, dates, signataires, statut)
2. Objet et spécifications
3. Conditions de mesure (T°, H%, montage)
4. Tableau de mesures (≥ 10 mesures)
5. Calculs statistiques (biais, σ, u, U)
6. Analyse et décision (conforme / non conforme)
7. Recommandations
8. Signatures et archivage
Annexes : graphique des écarts, brouillon calculs
```

---

## 🎨 Feux tricolores dashboard

```javascript
// Dans nœud function → nœud text (Allow HTML)
var couleurs = {
    "OK"       : { bg:"#4CAF50", emoji:"🟢" },
    "INFO"     : { bg:"#FFEB3B", emoji:"🟡" },
    "ATTENTION": { bg:"#FF9800", emoji:"🟠" },
    "CRITIQUE" : { bg:"#F44336", emoji:"🔴" }
};
```

---

## ⚠️ Erreurs fréquentes PV

```
❌ Mesures prises sans stabilisation thermique
❌ Étalon et capteur trop éloignés (gradient T°)
❌ n−1 oublié dans σ (mettre n → surestimer la précision)
❌ Oublier de tracer le graphe des écarts
❌ Conclure "conforme" sans calculer |e̅| + U
```

---

*Aide-Mémoire Industrie 4.0 + Métrologie — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S17*
*Compétences S5.4 · S5.5 · S5.6 · C3.1 · C5.3*
