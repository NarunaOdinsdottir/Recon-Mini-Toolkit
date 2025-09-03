#import whois

#1.Domain Abfrage
#domain = input(" Welche Domain darf es sein?  (z.B. example.com): ")

#2. Whois Abfrage
#domain_info = whois.whois(domain)

#3. Ausgabe der Whois Informationen
#print("\n🔍 Whois Informationen für", domain    )   
#print("===================================")
#print("f""Domain Name: {domain_info.domain_name}")
#print(f"Registrar: {domain_info.registrar}")
#print(f"Whois Server: {domain_info.whois_server}")
#print(f"Referrer: {domain_info.referrer}")
#print(f"Updated Date: {domain_info.updated_date}")
#print(f"Creation Date: {domain_info.creation_date}")
#print(f"Expiration Date: {domain_info.expiration_date}")
#print(f"Name Servers: {domain_info.name_servers}")

import whois
from datetime import datetime

# 1️⃣ Domain Abfrage
domain = input("Welche Domain darf es sein? (z.B. example.com): ")

# 2️⃣ Whois Abfrage
domain_info = whois.whois(domain)

# 3️⃣ Ausgabe der Whois Informationen
print("\n🔍 Whois Informationen für", domain)
print("===================================")

# Nachtatem kommentiert
def dragon_comment(field, value):
    if not value:
        return ""
    if field == "creation_date":
        if isinstance(value, list):
            value = value[0]
        age = (datetime.now() - value).days
        if age < 365:
            return "🐉 Nachtatem: Frisch geschlüpft… noch jung und unerfahren."
        else:
            return "🐉 Nachtatem: Eine alte Domain, voller Geschichte und Geheimnisse."
    if field == "expiration_date":
        if isinstance(value, list):
            value = value[0]
        days_left = (value - datetime.now()).days
        if days_left < 30:
            return "🐉 Nachtatem: Bald wird die Zeit knapp, Menschlein…"
        else:
            return ""
    if field == "name_servers":
        return "🐉 Nachtatem: Hier liegen deine geheimen Tore…"
    return ""

# Felder ausgeben
fields = [
    ("Domain Name", domain_info.domain_name),
    ("Registrar", domain_info.registrar),
    ("Whois Server", domain_info.whois_server),
    ("Referrer", domain_info.referrer),
    ("Updated Date", domain_info.updated_date),
    ("Creation Date", domain_info.creation_date),
    ("Expiration Date", domain_info.expiration_date),
    ("Name Servers", domain_info.name_servers)
]

for name, value in fields:
    print(f"{name}: {value}")
    comment = dragon_comment(name.lower().replace(" ", "_"), value)
    if comment:
        print(comment)
