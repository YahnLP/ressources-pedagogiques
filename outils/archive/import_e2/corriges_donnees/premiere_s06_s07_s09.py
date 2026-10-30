"""Première S06, S07, S09 : éléments de réponse aux questions de compréhension et de diagnostic.
Les valeurs observées (IP, RSSI, etc.) dépendent du réseau de la salle."""
VA = "Éléments de réponse"
ENTREES = [
    ('premiere', 'S06', '02-tp.md', '## 🟢 NIVEAU 1', [
        "**1.1** — Adresse IP : donnée par le DHCP du réseau (par exemple `192.168.1.x`) ; RSSI : typiquement entre −40 dBm (très bon) et −80 dBm (faible) ; statut : **Connecté**.  ",
        "**1.2** — Les points s'affichent jusqu'à épuisement des 40 essais (20 s), puis le message « Échec connexion WiFi ». `WiFi.status()` ne vaut jamais `WL_CONNECTED` (3) : on obtient selon la version de la bibliothèque `WL_CONNECT_FAILED` (4) ou `WL_DISCONNECTED` (6)."], VA),
    ('premiere', 'S06', '02-tp.md', '## 🟡 NIVEAU 2', [
        "**2.1** — `/led/on` : LED **allumée** ; `/led/off` : LED **éteinte** ; `/status` : JSON de la forme `{\"led\":true,\"ip\":\"192.168.1.x\",\"rssi\":-55}`.  ",
        "**2.2** — Méthode **GET**, code de réponse **200**.  ",
        "**2.3** — **Oui** : l'ESP32 est accessible depuis tout appareil du même réseau local (même adresse IP, même sous-réseau)."], VA),
    ('premiere', 'S06', '02-tp.md', '## 🟠 NIVEAU 3', [
        "**3.1** — Réseau « ESP32_CIEL » visible : **oui** ; IP obtenue par le smartphone : de la forme `192.168.4.x` (souvent `192.168.4.2`).  ",
        "**3.2** — Page de configuration affichée : **oui** ; moniteur série : `SSID reçu : …` et `Pass reçu : …` après l'envoi du formulaire.  ",
        "**3.3** — Au premier démarrage, l'objet ne connaît pas encore le réseau WiFi du client. En mode AP, il crée **son propre réseau** : l'utilisateur s'y connecte avec son téléphone et lui indique le SSID et le mot de passe de son réseau. Aucun écran ni clavier n'est nécessaire."], VA),
    ('premiere', 'S06', '02-tp.md', '## 🔵 NIVEAU 4', [
        "**4.1** — WiFi et MQTT réussis : **oui** ; messages publiés toutes les 5 s (par exemple sur `ciel/…/temp`).  ",
        "**4.2** — Les messages arrivent toutes les 5 s sur le topic de publication, avec la valeur envoyée par l'ESP32.  ",
        "**4.3** — La LED réagit : **oui** ; moniteur série : `📩 [topic] → ON` puis `💡 LED allumée`."], VA),
    ('premiere', 'S07', '02-tp.md', '### 3.4', [
        "**Q11** — `online`. Le message est publié avec l'option **retained** : le broker le **conserve** et le renvoie à tout abonné qui se connecte plus tard.  ",
        "**Q12** — `offline` (le *Last Will*, publié automatiquement par le broker quand l'ESP32 disparaît sans se déconnecter proprement)."], VA),
    ('premiere', 'S07', '02-tp.md', '### Scénario', [
        "**Q13** — Causes possibles : adresse IP du broker incorrecte ; Mosquitto non démarré ; port 1883 bloqué par le pare-feu ; ESP32 et PC sur des réseaux différents ; identifiant client déjà utilisé.  ",
        "**Q14** — Par exemple depuis un autre appareil : `mosquitto_pub -h <IP_du_PC> -t test -m ok` ; ou sur le PC, vérifier que le port écoute : `netstat -an | findstr 1883` (Windows) / `ss -ltn | grep 1883` (Linux).  ",
        "**Q15** — **Non** : les topics MQTT sont **sensibles à la casse**, `Ciel/salon/temp` et `ciel/salon/temp` sont deux topics différents.  ",
        "**Q16** — `entrepot/esp32_[n]/capteur` : mesures publiées régulièrement ; `entrepot/esp32_[n]/status` : `online` (retained) à la connexion, `offline` en LWT. Une supervision s'abonne à `entrepot/+/status` : quand un ESP32 est coupé brutalement, le broker publie `offline` à sa place et la panne est détectée sans attendre."], VA),
    ('premiere', 'S09', '02-tp.md', '### Scénario', [
        "**Q12** —", "",
        "| Cause | Comment vérifier |", "|---|---|",
        "| Certificat ou clé mal collés dans le code | Comparer avec les fichiers téléchargés (lignes `BEGIN`/`END` complètes) |",
        "| Certificat non activé ou non attaché à la Policy | Console AWS : certificat actif, Policy attachée |",
        "| Endpoint, port ou horloge incorrects | Vérifier l'endpoint (port 8883) et que l'heure de l'ESP32 est synchronisée (NTP) |",
        "",
        "**Q13** — Vérifier que la **Policy est attachée au certificat** utilisé par l'ESP32, que ce certificat est **actif** et que le **client ID** et le topic utilisés correspondent bien aux ressources autorisées par la Policy.",
        "*(Remarque : le code `-7` n'existe pas dans PubSubClient, qui utilise `-4` à `5` ; il vient plutôt de la couche TLS. À vérifier par l'enseignant.)*"], VA),
]
