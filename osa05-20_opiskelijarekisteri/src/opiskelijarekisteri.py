def lisaa_suoritus(opiskelijat: dict, nimi: str, kurssi: tuple):
    if nimi not in opiskelijat:
        opiskelijat[nimi] = []
    for i, existing_kurssi in enumerate(opiskelijat[nimi]):
        if existing_kurssi[0] == kurssi[0]:
            if existing_kurssi[1] < kurssi[1]:
                opiskelijat[nimi][i] = kurssi
            return
    if kurssi[1] > 0:
        opiskelijat[nimi].append(kurssi)
    
def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []
    
def tulosta(opiskelijat: dict, nimi: str):
    if nimi not in opiskelijat:
        print("ei löytynyt ketään nimellä " + nimi)
    elif len(opiskelijat[nimi]) > 0:
        print(nimi + ":")
        suorituksia = len([suoritus for suoritus in opiskelijat[nimi] if suoritus[1] != 0])
        if suorituksia > 0:
            print(" suorituksia " + str(suorituksia) + " kurssilta:")
        else:
            print(" ei suorituksia")
        for suoritus in opiskelijat[nimi]:
            if suoritus[1] != 0:
                suorituksia = True
                print("  " + suoritus[0] + " " + str(suoritus[1]))
        if suorituksia:
            suoritukset = [suoritus[1] for suoritus in opiskelijat[nimi] if suoritus[1] != 0]
            if suoritukset:
                print(" keskiarvo " + str(sum(suoritukset) / len(suoritukset)))
    else:
        print(nimi + ":")
        print(" ei suorituksia")

def kooste(opiskelijat: dict):
    eniten = 0
    print("opiskelijoita " + str(len(opiskelijat)))
    for nimi in opiskelijat:
        if eniten < len(opiskelijat[nimi]):
            eniten = len(opiskelijat[nimi])
    print("eniten suorituksia " + str(eniten), end=" ")
    for nimi in opiskelijat:
        if len(opiskelijat[nimi]) == eniten:
            print(nimi)
    paras_opiskelija = max(opiskelijat, key=lambda nimi: sum([suoritus[1] for suoritus in opiskelijat[nimi] if suoritus[1] != 0]) / len([suoritus[1] for suoritus in opiskelijat[nimi] if suoritus[1] != 0]) if len([suoritus[1] for suoritus in opiskelijat[nimi] if suoritus[1] != 0]) > 0 else 0)
    paras_keskiarvo = sum([suoritus[1] for suoritus in opiskelijat[paras_opiskelija] if suoritus[1] != 0]) / len([suoritus[1] for suoritus in opiskelijat[paras_opiskelija] if suoritus[1] != 0])
    print("paras keskiarvo " + str(paras_keskiarvo) + " " + paras_opiskelija)
        

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)