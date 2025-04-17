def summa():
    with open("matriisi.txt") as tiedosto:
        summa = 0
        for rivi in tiedosto:
            osat = rivi.strip().split(",")
            summa = summa + sum([float(osa) for osa in osat])
        return int(summa)

def maksimi():
    with open("matriisi.txt") as tiedosto:
        maksimi = 0
        for rivi in tiedosto:
            osat = rivi.strip().split(",")
            for osa in osat:
                if float(osa) > maksimi:
                    maksimi = float(osa)
        return int(maksimi)

def rivisummat():
    with open("matriisi.txt") as tiedosto:
        rivisummat = []
        for rivi in tiedosto:
            osat = rivi.strip().split(",")
            rivisummat.append(sum([float(osa) for osa in osat]))
        return rivisummat

if __name__ == "__main__":
    print(summa())
    print(maksimi())
    print(rivisummat())