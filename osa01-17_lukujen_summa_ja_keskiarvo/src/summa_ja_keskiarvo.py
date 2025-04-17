# Ohjelma, joka lukee käyttäjältä neljä lukua ja tulostaa niiden summan ja keskiarvon

# Kysytään käyttäjältä neljä lukua
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))
luku4 = int(input("Anna neljäs luku: "))

# Lasketaan lukujen summa
summa = luku1 + luku2 + luku3 + luku4

# Lasketaan lukujen keskiarvo
keskiarvo = summa / 4

# Tulostetaan summa ja keskiarvo
print(f"Lukujen summa on {summa} ja keskiarvo {keskiarvo}")