# Kysytään käyttäjältä kaksi sanaa
sana1 = input("Anna 1. sana: ")
sana2 = input("Anna 2. sana: ")

# Tarkistetaan, ovatko sanat samat
if sana1 == sana2:
    print("Annoit saman sanan kahdesti.")
# Verrataan sanoja ja tulostetaan aakkosjärjestyksessä jälkimmäinen
elif sana1 > sana2:
    print(f"{sana1} on aakkosjärjestyksessä viimeinen.")
else:
    print(f"{sana2} on aakkosjärjestyksessä viimeinen.")