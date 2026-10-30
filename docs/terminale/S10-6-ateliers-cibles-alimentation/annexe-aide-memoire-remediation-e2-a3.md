# 🗂️ AIDE-MÉMOIRE REMÉDIATION E2 A3 — À PLASTIFIER
## Toutes les Formules Essentielles · BAC PRO CIEL · E2 · 3ᵉ année S10

---

## ⚡ Alimentation

Pdiss = (Vin−Vout) × Iout  
Tj = Tamb + Pdiss × Rθja  

$$Tj_max_exploitable = 105\,\mathrm{°C}$$

Autonomie = Capacité(mAh) / I_moy × 0,80  

$$I_{\mathrm{moy}} = \dfrac{I_{1} \times t1 + I_{2} \times t2}{t1+t2}$$

Linéaire : simple, bruit faible, Vdrop faible → OK  
Buck     : η=85-95%, sur batterie, Vin-Vout ≥ 2V → OK  

---

## 📐 Métrologie R&R

$$σ_EV = \dfrac{σ_A + σ_B}{2}$$

σ_AV ≈ |x̄_A − x̄_B| / √n  

$$σ_GRR = \sqrt{σ_EV^2 + σ_AV^2}$$

%GRR = 5,15 × σ_GRR / Tolérance × 100  

< 10% = EXCELLENT ✓✓  
10-30% = ACCEPTABLE ✓  
> 30% = INACCEPTABLE ✗  

LD ≈ 3 × σ_bruit  (signal détectable si > LD)  

---

## 🔧 Fiabilité

```
λ = 1/MTBF  ·  D = MTBF/(MTBF+MTTR)
R(t) = e^(−λt)
R(MTBF) = e⁻¹ = 0,368 = 36,8% ← JAMAIS 50% !
Série    : Rs = R1×R2×R3  (affaiblit)
Parallèle: Rs = 1−(1−R1)(1−R2)  (renforce)
1 an = 8760h
```

---

## 📻 CEM

```
Fente max = λ/20  (λ=3×10⁸/f)
  2,4GHz → λ=12,5cm → fente < 6,25mm
fc = 1/(2π×R×C)
Plan CONTINU : petite boucle → peu de rayonnement ✓
Plan FENDU   : grande boucle → fort rayonnement ✗
4 couplages : résistif/capacitif/inductif/rayonné
```

---

## 🖥️ KiCad & PCB

```
Découplage : 100nF au plus proche CI (<2mm)
Via : 0,8mm / 0,4mm
Clearance ≥ 0,2mm · Signal 0,35mm · Alim 0,8mm
ERC = erreurs schéma · DRC = erreurs PCB
B = remplir zones (plan de masse)
```

---

## 📡 ESP32 & IoT

```cpp
// AP : 192.168.4.1
// STA : WiFi.begin → while(!=WL_CONNECTED)
// server.handleClient()   // loop() !
// mqtt.loop()             // loop() !
// Client ID MQTT = UNIQUE
// delay() → bloque mqtt.loop() → utiliser millis()
// msg.topic = nom de la série chart Node-RED
// influxdb : [{measurement, tags, fields}]
```

---

## 🚨 Les 12 pièges E2 A3

```
1.  R(MTBF) = 36,8% (pas 50%)
2.  Série : Rs < Rmin
3.  %GRR > 30% → système inacceptable
4.  LD < variation → signal détectable
5.  |biais|+U ≤ spécif. pour conformité
6.  Tj > 105°C → radiateur !
7.  delay() dans loop() → bloque MQTT
8.  mqtt.loop() oublié → pas de réception
9.  Plan fendu → grande boucle → CEM
10. Découplage > 2mm du CI → inefficace
11. Client ID MQTT identique → déconnexion
12. Tolérance totale = 2× tolérance unilatérale
```

---

*Aide-Mémoire Remédiation E2 A3 — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S10*
