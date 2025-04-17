kenelle = input("Kenelle teos omistetaan: ")
mihin = input("Mihin kirjoitetaan: ")
with open(mihin, "w") as tiedosto:
    tiedosto.write(f"Hei {kenelle}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")