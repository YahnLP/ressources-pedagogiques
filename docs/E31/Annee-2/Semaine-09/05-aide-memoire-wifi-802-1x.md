# 🗂️ AIDE-MÉMOIRE WiFi ENTREPRISE 802.1X — À PLASTIFIER
## RADIUS · EAP-TLS · PEAP · Architecture WLAN · BAC PRO CIEL · E32 · 2ᵉ année S9

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 👥 Les 3 acteurs de 802.1X

```
SUPPLICANT       → Appareil client (laptop, smartphone)
                   Prouve son identité

AUTHENTICATOR    → Borne WiFi ou switch
                   Filtre le trafic, relaie les messages
                   N'accorde PAS lui-même l'accès

SERVEUR RADIUS   → Décide : OUI (Access-Accept) / NON (Access-Reject)
                   Port UDP 1812 (auth) · UDP 1813 (accounting)
```

---

## 📨 Messages RADIUS dans l'ordre

```
1. EAPOL-Start         (Laptop → AP)
2. EAP-Request/Identity (AP → Laptop)
3. EAP-Response        (Laptop → AP → RADIUS : Access-Request)
4. Access-Challenge     (RADIUS → AP → Laptop)
5. EAP-Response/Creds  (Laptop → AP → RADIUS : Access-Request)
6. Access-Accept + VLAN (RADIUS → AP)
7. EAP-Success         (AP → Laptop)
   ✓ Trafic autorisé sur VLAN assigné
```

---

## 🔒 EAP-TLS vs PEAP

```
              EAP-TLS        PEAP
Cert. Client    ✅ OUI        ❌ NON
Cert. Serveur   ✅ OUI        ✅ OUI
Authentif.      Mutuelle      Serveur seulement
Sécurité        ⭐⭐⭐          ⭐⭐
PKI requise     Complète      RADIUS seul suffit
Usage           Banque/armée  Entreprise standard
```

---

## 📜 Certificat X.509 — champs clés

```
Subject    → identité du titulaire (CN=alice)
Issuer     → qui a signé (CN=Corp-CA)
Valid To   → date d'expiration
Public Key → clé publique RSA/ECC
Signature  → preuve CA (impossible à forger)
```

**Révocation** → ajouter le serial à la **CRL** (Certificate Revocation List)
→ RADIUS consulte la CRL → refus immédiat même si certif pas expiré

---

## 🏗️ Architecture WLAN minimale sécurisée

```
Internet
   │
[Pare-feu]
   │
[WLC] ←→ [AP1][AP2][AP3]
   │
[Serveur RADIUS] ←→ [Active Directory]
[CA/PKI] (si EAP-TLS)

VLAN 10 : Staff WiFi     → 802.1X + accès interne
VLAN 20 : Guest WiFi     → PSK / captif + Internet seul
VLAN 100 : Serveurs/Mgmt → accès restreint
```

---

## ⌨️ Configuration Packet Tracer

```
RADIUS Server → Services → AAA :
  Network (clients) : ajouter l'AP
    · IP AP, secret partagé
  Users : ajouter les comptes

AP → Config → Interface :
  SSID : Corp-Secure
  Auth  : WPA2-Enterprise
  RADIUS IP / Secret / Port 1812

Laptop → Desktop → PC Wireless :
  SSID : Corp-Secure
  Auth  : WPA2-Enterprise / PEAP
  Username / Password
```

---

## ✅ Commandes de vérification

```
RADIUS Server → AAA → Log    ← Accept/Reject par utilisateur
AP → Config → Interface      ← vérifier SSID et auth
Laptop → Desktop → Wireless  ← statut de connexion + IP obtenue
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| Secret AP≠RADIUS | Configurer le MÊME secret des deux côtés |
| AP non déclaré comme client RADIUS | Ajouter l'IP de l'AP dans "Network" du RADIUS |
| Mauvais port (1645 au lieu de 1812) | UDP 1812 (standard moderne) |
| EAP-TLS sans PKI | Déployer CA + émettre certif. clients |
| VLAN guest non isolé | Mettre règle de filtrage inter-VLAN sur le pare-feu |

---

## 🔑 Différence PSK vs Enterprise

```
WPA2-PSK :
  → 1 mot de passe pour tous
  → Employé part → changer pour TOUT LE MONDE

WPA2-Enterprise (802.1X) :
  → 1 identité par personne
  → Employé part → désactiver SON compte/certificat
  → Traçabilité complète dans les logs RADIUS
```

---

*Aide-Mémoire WiFi 802.1X — À plastifier*
*BAC PRO CIEL | E32 Cybersécurité | 2ᵉ année S9*
*Compétences S4.1 · S4.2 · S4.3 · S4.4 · S4.5 · C2.2*
