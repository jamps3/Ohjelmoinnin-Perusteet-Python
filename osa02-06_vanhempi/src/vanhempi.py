# Kysytään ensimmäisen henkilön nimi ja ikä
nimi1 = input("Henkilö 1:\nNimi: ")
ika1 = int(input("Ikä: "))

# Kysytään toisen henkilön nimi ja ikä
nimi2 = input("Henkilö 2:\nNimi: ")
ika2 = int(input("Ikä: "))

# Verrataan ikää ja tulostetaan vanhemman henkilön nimi
if ika1 > ika2:
    print(f"Vanhempi on {nimi1}")
elif ika2 > ika1:
    print(f"Vanhempi on {nimi2}")
else:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")