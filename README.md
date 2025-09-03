# Recon-Mini-Toolkit
Python Mini Projekte für Nachtatem - Whois, Portscanner, Subdomain Finder





Whois Mini-Projekt

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

Subdomain Scanner Mini-Projekt

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


Portscanner Mini-Projekt

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


