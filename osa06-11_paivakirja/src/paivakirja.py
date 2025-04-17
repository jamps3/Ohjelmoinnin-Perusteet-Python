def lue_paivakirja():
    try:
        with open("paivakirja.txt", "r") as tiedosto:
            return tiedosto.readlines()
    except FileNotFoundError:
        return []

def tallenna_paivakirja(merkinta):
    with open("paivakirja.txt", "a") as tiedosto:
        tiedosto.write(merkinta + "\n")
    print("Päiväkirja tallennettu")

while True:
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    valinta = input("Valinta: ")
    
    if valinta == "1":
        merkinta = input("Anna merkintä: ")
        tallenna_paivakirja(merkinta)
    elif valinta == "2":
        print("Merkinnät:")
        merkinnat = lue_paivakirja()
        for merkinta in merkinnat:
            print(merkinta.strip())
    elif valinta == "0":
        print("Heippa!")
        break
    else:
        print("Virheellinen valinta, yritä uudelleen.")
