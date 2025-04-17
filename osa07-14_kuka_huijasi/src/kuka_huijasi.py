import os
import csv
from datetime import datetime

def huijarit():
    aloitus = os.path.join(os.path.dirname(__file__), 'tentin_aloitus.csv')
    data = []
    with open(aloitus) as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            data.append(rivi)
        sanakirja = {key: value for key, value in data}
        palautus = os.path.join(os.path.dirname(__file__), 'palautus.csv')
        huijarit = []
        with open(palautus) as tiedosto2:
            for rivi in csv.reader(tiedosto2, delimiter=";"):
                tiedot = sanakirja.get(rivi[0])  # Haetaan opiskelijan tentin aloitusaika
                format = "%H:%M" # Aikamuoto
                tentinaloitus = datetime.strptime(tiedot, format) # Tentin aloitusaika
                tentinlopetus = datetime.strptime(rivi[3], format) # Tentin palautusaika
                difference = abs((tentinaloitus - tentinlopetus).total_seconds() / 3600) # Laske ero tunneissa
                result = difference <= 3 # Jos ero on yli 3 tuntia
                if not result: # Huijari!
                    #print(rivi[0] + " on huijari!")
                    if rivi[0] not in huijarit:
                        huijarit.append(rivi[0])
    return huijarit

if __name__ == "__main__":
    print(huijarit())