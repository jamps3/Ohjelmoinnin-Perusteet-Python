luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
komento = input("Komento: ").strip().lower()

if komento == "summa":
    print(f"{luku1} + {luku2} = {luku1 + luku2}")
elif komento == "tulo":
    print(f"{luku1} * {luku2} = {luku1 * luku2}")
elif komento == "erotus":
    print(f"{luku1} - {luku2} = {luku1 - luku2}")
