import socket
import random

# 1️⃣ Ziel-IP Adresse eingeben
target_ip = input("Geben Sie die Ziel-IP-Adresse oder Domain ein: ")

# Hostname auflösen zu IP-Adresse
target_ip = socket.gethostbyname(target_ip)

# Nachtatems Einsatz
print("\n🐉 Nachtatem spricht:")
print("1. Bestimmte Ports scannen?")
print("2. Automatischer Fullscan (1-1024)?")
choice = input("Wähle weise... 1 oder 2: ")
print(f"So sei es, Menschlein... Starte Port-Scan für {target_ip}...\n")

# Liste offener Ports
open_ports = []

# Drachen-Sprüche für offene Ports
dragon_quotes = [
    "Ein Tor in deine schwache Festung offenbart sich...",
    "So leicht dringen Schatten durch diese Öffnung...",
    "Menschlein, hier hast du geschlampt...",
    "Ahh, ein Eingang – zu verlockend, um ihn ungenutzt zu lassen.",
    "Eine klaffende Wunde in deinem System..."
]

# 2️⃣ Port-Auswahl
if choice == "1":
    ports_input = input("Gib die Ports ein (z.B. 22,80,443 oder 20-25): ")
    ports_to_scan = []

    for part in ports_input.split(","):
        part = part.strip()
        if "-" in part:  # Bereich
            start, end = map(int, part.split("-"))
            ports_to_scan.extend(range(start, end + 1))
        else:  # Einzelport
            try:
                ports_to_scan.append(int(part))
            except ValueError:
                print(f"Ungültiger Port: {part}. Überspringe...")

else:
    ports_to_scan = range(1, 1025)  # Fullscan Standardbereich

print(f"\n🐲 Nachtatem zischt: 'Ich durchforste nun Ports {ports_to_scan if choice=='1' else '1-1024'}...'\n")

# 3️⃣ Port-Scan
for port in ports_to_scan:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"🔥 Port {port} ist offen!")
        print("   🐉 Nachtatem: " + random.choice(dragon_quotes))
        open_ports.append(port)

        # Banner-Grabbing
        try:
            sock.send(b"Hello\r\n")
            banner = sock.recv(1024).decode().strip()
            if banner:
                print(f"   -> Banner: {banner}")
        except:
            pass
    sock.close()

# 4️⃣ Statistik
print(f"\n🐉 Nachtatem brummt: 'Der Scan ist vollendet. {len(open_ports)} offene Tore habe ich erspäht.'")
print(f"⚔️ Offene Ports: {open_ports if open_ports else 'Keine... deine Festung ist vorerst sicher.'}")
