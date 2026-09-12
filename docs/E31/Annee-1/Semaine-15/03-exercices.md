# 📝 EXERCICES - S15 E31
## Wireshark - Pratique

**Nom : ________________  Prénom : ________________**

---

## EXERCICE 1 : Filtres Display (6 pts)

**Écris les filtres Wireshark pour afficher :**

| **Objectif** | **Filtre** | **(1 pt)** |
|-------------|-----------|----------|
| Tout trafic HTTP | ________________ | |
| IP source 192.168.1.50 | ________________ | |
| Port TCP 443 (HTTPS) | ________________ | |
| Requêtes DNS | ________________ | |
| TCP SYN (flags) | ________________ | |
| HTTP ET IP 10.0.0.5 | ________________ | |

---

## EXERCICE 2 : TCP Handshake (4 pts)

**Complète la séquence :**

```
Établissement connexion TCP :

Client → Serveur : ________ (1)

Serveur → Client : ________ (2)

Client → Serveur : ________ (3)

Connexion établie ✅
```

**Barème :** 1 pt par étape, 1 pt nom complet

---

## EXERCICE 3 : Analyse Capture (5 pts)

**Capture HTTP suivante :**

```
No.  Time     Source        Dest          Protocol Info
142  12.5s    192.168.1.20  93.184.216.34 DNS      Query A example.com
143  12.52s   93.184.216.34 192.168.1.20  DNS      Response A 93.184.216.34
145  12.6s    192.168.1.20  93.184.216.34 TCP      SYN
146  12.65s   93.184.216.34 192.168.1.20  TCP      SYN-ACK
147  12.7s    192.168.1.20  93.184.216.34 TCP      ACK
150  12.8s    192.168.1.20  93.184.216.34 HTTP     GET /index.html
```

**Questions :**

**Q1** (1 pt) : IP client ?  
_______________

**Q2** (1 pt) : IP serveur ?  
_______________

**Q3** (1 pt) : Résolution DNS de ?  
_______________

**Q4** (1 pt) : Protocole couche 7 ?  
_______________

**Q5** (1 pt) : Port destination probable ?  
_______________

---

## EXERCICE 4 : Sécurité HTTP vs HTTPS (3 pts)

**Complète le tableau :**

| **Critère** | **HTTP** | **HTTPS** | **(0,5 pt)** |
|------------|---------|----------|----------|
| Chiffrement | Aucun | _________ | |
| Port par défaut | 80 | _________ | |
| MDP visible Wireshark | Oui | _________ | |
| Protocole chiffrement | - | _________ | |
| Cadenas navigateur | Non | _________ | |
| Recommandé 2026 | Non | _________ | |

---

## EXERCICE 5 : Cas Pratique (2 pts)

**Scénario :**

Admin réseau capture trafic utilisateur Alice.  
Wireshark révèle :

```
POST /login HTTP/1.1
Host: webmail.entreprise.com

user=alice&password=Alice2026!
```

**Questions :**

**Q1** (1 pt) : Quelle vulnérabilité ?

___________________________________________________

**Q2** (1 pt) : Solution recommandée ?

___________________________________________________

---

## 📊 BARÈME

| **Exercice** | **Points** | **Note** |
|-------------|-----------|----------|
| Filtres Display | /6 | |
| TCP Handshake | /4 | |
| Analyse Capture | /5 | |
| HTTP vs HTTPS | /3 | |
| Cas Pratique | /2 | |
| **TOTAL** | **/20** | |

---

**Document - Version 1.0 - Février 2026**
