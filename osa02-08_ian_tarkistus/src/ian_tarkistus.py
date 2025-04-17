# Kysytään käyttäjän ikää
ika = int(input("Kerro ikäsi? "))

# Tarkistetaan ikä ja annetaan sopiva vastaus
if ika < 0:
    print("Taitaa olla virhe")
elif ika < 5:
    print("En usko, että osaat kirjoittaa...")
else:
    print(f"Ok, olet siis {ika}-vuotias")