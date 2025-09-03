import socket
import random

# 1️⃣ Domain abfragen
domain = input("Welche Domain wollen wir nach Subdomains absuchen? ")

# 2️⃣ Subdomain-Liste (später erweiterbar)
subdomains = ["www", "mail", "ftp", "test", "dev", "admin"]

# Drachen-Sprüche für gefundene Subdomains
dragon_quotes = [
    "🐉 Nachtatem: Ein verborgenes Tor wurde entdeckt…",
    "🐉 Nachtatem: Ahh, hier lauern Geheimnisse!",
    "🐉 Nachtatem: So leicht lassen sich Schatten durchschreiten…",
    "🐉 Nachtatem: Eine schwache Stelle in deiner Festung!",
    "🐉 Nachtatem: Menschlein, hier sind Risse im System!"
]

print(f"\n🐉 Nachtatem zischt: Ich durchforste die Schatten der Domain {domain}...\n")

# 3️⃣ Subdomain-Scan
found_subdomains = []

for sub in subdomains:
    full_domain = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        print(f"✅ Subdomain gefunden: {full_domain} -> {ip}")
        print(random.choice(dragon_quotes))  # Drache kommentiert
        found_subdomains.append(full_domain)
    except socket.gaierror:
        # Keine Auflösung möglich
        print(f"❌ {full_domain} existiert nicht oder ist nicht erreichbar.")

# 4️⃣ Ergebnis
print("\n🐉 Nachtatem brummt: Subdomain-Scan abgeschlossen.")
if found_subdomains:
    print(f"Gefundene Subdomains: {found_subdomains}")
else:
    print("Keine Subdomains gefunden… deine Festung ist still.")

