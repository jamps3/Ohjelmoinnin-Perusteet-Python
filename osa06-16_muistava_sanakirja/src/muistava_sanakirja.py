def lue_sanakirja(tiedosto):
    sanakirja = {}
    try:
        with open(tiedosto, "r", encoding="utf-8") as f:
            for rivi in f:
                suomi, englanti = rivi.strip().split(";")
                sanakirja[suomi] = englanti
    except FileNotFoundError:
        pass
    return sanakirja

def tallenna_sanakirja(tiedosto, sanakirja):
    with open(tiedosto, "a", encoding="utf-8") as f:
        for suomi, englanti in sanakirja.items():
            f.write(f"{suomi};{englanti}\n")

def lisaa_sana(sanakirja, tiedosto):
    suomi = input("Anna sana suomeksi: ")
    englanti = input("Anna sana englanniksi: ")
    sanakirja[suomi] = englanti
    tallenna_sanakirja(tiedosto, sanakirja)
    print("Sanapari lisätty")

def hae_sana(sanakirja):
    sana = input("Anna sana: ")
    loydetyt = [(suomi, englanti) for suomi, englanti in sanakirja.items() if sana in suomi or sana in englanti]
    if loydetyt:
        for suomi, englanti in loydetyt:
            print(f"{suomi} - {englanti}")
    else:
        print("Sanaa ei löytynyt")

tiedosto = "sanakirja.txt"
sanakirja = lue_sanakirja(tiedosto)

while True:
    print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
    valinta = input("Valinta: ")
    if valinta == "1":
        lisaa_sana(sanakirja, tiedosto)
    elif valinta == "2":
        hae_sana(sanakirja)
    elif valinta == "3":
        print("Moi!")
        break
    else:
        print("Virheellinen valinta, yritä uudelleen")
