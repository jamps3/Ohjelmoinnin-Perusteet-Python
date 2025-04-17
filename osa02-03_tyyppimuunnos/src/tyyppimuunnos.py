# Kysytään käyttäjältä desimaaliluku
desimaaliluku = float(input("Anna luku: "))

# Erotellaan kokonaisosa ja desimaaliosa
kokonaisosa = int(desimaaliluku)
desimaaliosa = desimaaliluku - kokonaisosa

# Tulostetaan kokonaisosa ja desimaaliosa
print("Kokonaisosa:", kokonaisosa)
print("Desimaaliosa:", desimaaliosa)