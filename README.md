Recon-Mini-Toolkit
Python Mini Projekte für Nachtatem - Whois, Portscanner, Subdomain Finder


# Nachtatem’s Vault of Tools 🐉🏜️

Willkommen, Wanderer, in den Ruinen des Ödlands!  
Hier in Nachtatem’s Vault of Tools findest du die geheimen Spielzeuge eines alten Drachen – gebaut, um menschliche Pfade zu erkunden und die Schatten der digitalen Welt zu durchforsten.  

---

## ⚔️ Warum diese Tools?

Die Ödnis ist voller Fallen, verlassener Maschinen und versteckter Geheimnisse.  
Nachtatem, uralter Wächter der Datenruinen, hat entschieden, dass du – ja, genau DU – ein bisschen Hilfe brauchst, um die Welt zu durchschauen:

- **Whois Abfrage**: Alte Domains haben Geschichten. Finde heraus, wann sie geboren wurden, wann sie sterben und welche Tore sie öffnen.  
- **Subdomain Finder**: Manche Bunker… äh, Subdomains, sind leicht zu übersehen. Nachtatem hilft dir, sie zu finden – bevor Mutanten oder Konkurrenten es tun.  
- **Portscanner**: Offene Türen und Terminaleingänge zeigen dir, wo Sicherheit schwach ist – oder wo du besser die Finger von lässt. Dein Pip-Boy 3000 für die digitale Ödnis.

„Jede Ruine hat ihre Geschichte. Jede Tür kann ein Schatz sein… oder ein tödlicher Fehler.“ – Nachtatem

---

## 🗂️ Projektübersicht

1. [Whois Mini-Projekt](whois/README.md) – Abfrage von Domaininformationen  
2. [Subdomain Finder Mini-Projekt](subdomain-finder/README.md) – Finden von versteckten Subdomains  
3. [Portscanner Mini-Projekt](port-scanner/README.md) – Überprüfen offener Ports auf Domain oder Subdomain  

---

## 🚀 Nutzung

Jedes Projekt hat ein eigenes Skript (`.py`) und eine kleine Anleitung im jeweiligen Ordner.  
Einfach das Skript ausführen, den Anweisungen folgen – und Nachtatem kommentiert alles direkt.  

---

## 🐉 Fun Fact

Alle Tools sind für **Lernzwecke & Ethical Hacking in sicheren Umgebungen** gedacht.  
Die Ödnis ist groß, aber sei vorsichtig – Nachtatem beobachtet immer. 🔥










## Whois Mini-Projekt


Willkommen in der Ödnis, Wanderer! 🏜️  
Nachtatem, der uralte Drache, streift durch die Ruinen alter Domains.  
Er hat sich entschieden, ein paar menschliche Spielzeuge zu benutzen – diese Whois-Abfrage –  
um die Geheimnisse der Welt vor dir aufzudecken.  

Warum? Nun ja… auch ein Drache muss seine Informationsversorgung sichern, bevor er  
die nächsten Vault-Türen aufreißt. 🔥

„Jede Domain hat ihre Geschichte, und jede Geschichte kann nützlich sein… oder tödlich.“ – Nachtatem


Beschreibung

Dieses Skript führt eine WHOIS-Abfrage für eine angegebene Domain durch und gibt relevante Informationen aus.
Zusätzlich kommentiert Nachtatem die Ergebnisse mit kleinen Hinweisen.

Nutzung
```bash
python whois.py

Anforderungen
- Python 3.x
- whois- Bilbiothek  ( Installation : pip install python-whois)

Beispiel:

Domain Name: example.com
Registrar: Example Registrar
🐉 Nachtatem: Eine alte Domain, voller Geschichte und Geheimnisse.

---

## Subdomain Scanner Mini-Projekt


Im Ödland lauern überall versteckte Bunker… äh, Subdomains! 🏚️  
Nachtatem hat beschlossen, dass du als menschliches Kleinstwesen ein Auge auf diese Schatten werfen sollst.  

Mit dem Subdomain Finder findest du die geheimen Tunnel, die sonst nur Mutanten kennen.  
Je mehr du findest, desto besser kannst du deine Vorräte planen… oder dir vielleicht ein kleines  
„Hackers Vault“ aufbauen. 💀

„Manchmal ist die kleinste Tür die gefährlichste.“ – Nachtatem

Beschreibung

Dieses Skript probiert eine Liste häufiger Subdomains aus und überprüft, welche existieren.
Nachtatem kommentiert jede gefundene Subdomain.

Nutzung
```bash
python subdomainscanner.py

Anforderungen
- Python 3.x
- socket ( in Python Standardbibliothek enthalten)

Beispiel:

✅ Subdomain gefunden: www.example.com -> 93.184.216.34
🐉 Nachtatem: Ein verborgenes Tor wurde entdeckt…
❌ mail.example.com existiert nicht oder ist nicht erreichbar.


---


## Portscanner Mini-Projekt

Die Ödnis ist voller verlassener Maschinen und Sicherungsterminals… 🛠️  
Bevor du unvorsichtig an einen Terminal gehst, will Nachtatem sicherstellen, dass du die richtigen Ports kennst.  

Der Portscanner ist dein Pip-Boy 3000: Er sagt dir, welche Eingänge offen sind,  
welche Fallen lauern und wo vielleicht ein Roboteraufseher noch patrouilliert.  

„Offene Türen sind verlockend, aber wehe, du trittst in die falsche…“ – Nachtatem


Beschreibung

Dieses Skript scannt Ports einer Domain oder IP-Adresse.
Es können bestimmte Ports oder ein Fullscan (1-1024) ausgewählt werden.
Nachtatem kommentiert offene Ports mit kleinen Sprüchen.

Nutzung
```bash
python portscanner.py

Anforderungen
- Python 3.x
- socket ( in Python Standartbibliothek enthalten)

Beispiel:

🔥 Port 80 ist offen!
🐉 Nachtatem: Ein verborgenes Tor wurde entdeckt…


