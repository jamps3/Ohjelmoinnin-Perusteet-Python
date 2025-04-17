def suurin():
    suurin = 0
    with open("luvut.txt") as tiedosto:
        for rivi in tiedosto:
            luku = int(rivi)
            if luku > suurin:
                suurin = luku
    return suurin

if __name__ == "__main__":
    print("Suurin: " + str(suurin()))