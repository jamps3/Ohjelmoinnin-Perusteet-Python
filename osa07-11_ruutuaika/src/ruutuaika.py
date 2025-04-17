import os
from datetime import date, datetime, timedelta
from time import strftime
import random

# Kovakoodatut tiedot
#tiedosto = os.path.join(os.path.dirname(__file__), 'kesakuun_loppu.txt')
#aloituspaiva = datetime.strptime("24.6.2020", "%d.%m.%Y")
#montako = 5
# Kysellään tiedot
tiedosto = input("Tiedosto: ")
aloituspaiva = datetime.strptime(input("Aloituspäivä: "), "%d.%m.%Y")
montako = int(input("Montako päivää: "))

# Kysy ruutuajat
print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")
ruutuajat = ""
for i in range(montako):  # Adjust the range as needed
    date_str = (aloituspaiva + timedelta(days=i)).strftime("%d.%m.%Y")  # Format the date
    user_input = input(f"Ruutuaika {date_str}: ")  # Prompt for user input
    ruutuajat += f"Ruutuaika {date_str}: {user_input}\n"  # Add to ruutuajat
# Random
#ruutuajat = ruutuajat + "Ruutuaika " + datetime.strftime(aloituspaiva + timedelta(days=i), "%d.%m.%Y") + " " + str(random.randint(1,60)) + " " + str(random.randint(1,60)) + " " + str(random.randint(1,60)) + "\n"

# Kirjoita tiedostoon
with open(tiedosto, "w") as file:
    file.write("Ajanjakso: " + datetime.strftime(aloituspaiva, "%d.%m.%Y") + "-" + datetime.strftime(aloituspaiva + timedelta(days=montako-1), "%d.%m.%Y") + "\n")
    ajat = ""
    yhteensa = 0
    for i in ruutuajat.splitlines():
        txt, date, ra1, ra2, ra3 = i.split(" ")
        yhteensa += int(ra1) + int(ra2) + int(ra3)
        
        ajat += date + " " + ra1 + "/" + ra2 + "/" + ra3 + "\n"
    # Yhteensä
    file.write("Yht. minuutteja: " + str(yhteensa) + "\n")
    file.write("Keskim. minuutteja: " + str(yhteensa / len(ruutuajat.splitlines())) + "\n")
    file.write(ajat)
print("Tiedot tallennettu tiedostoon " + tiedosto)