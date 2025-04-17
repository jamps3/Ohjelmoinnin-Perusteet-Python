def lue_hedelmat():
    hedelmat = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            hinta = float(osat[1])
            hedelmat.update({osat[0]: hinta})
    return hedelmat

if __name__ == "__main__":
    print(lue_hedelmat())