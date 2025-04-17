import os
import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto, "r") as file:
        data = file.read()
    tiedot = json.loads(data)
    for i in tiedot:
        print(i["nimi"] + " " + str(i["ika"]) + " vuotta (", end="")
        #if i["harrastukset"]:
        laskuri = 0
        for harrastus in i["harrastukset"]:
            if laskuri == 0:
                #print("(", end="")
                laskuri += 1
                print(harrastus, end="")
            else:
                print(", " + harrastus, end="")
        print(")")
        #else:
            #print("\n")

if __name__ == "__main__":
    # Kovakoodatut tiedot
    tiedosto = os.path.join(os.path.dirname(__file__), 'tiedosto4.json')
    # Kysellään tiedot
    tiedosto = input("Tiedosto: ")
    tulosta_henkilot(tiedosto)