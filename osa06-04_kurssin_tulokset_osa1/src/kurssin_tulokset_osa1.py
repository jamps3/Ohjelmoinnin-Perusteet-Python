if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"

opiskelijat = {}

with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(';')
        if osat[0] == "opnro":
            continue
        opiskelijat[osat[0]] = f"{osat[1]} {osat[2]}"

tehtavat = {}

with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(';')
        if osat[0] == "opnro":
            continue
        tehtavat[osat[0]] = sum(int(x) for x in osat[1:])

for opnro, nimi in opiskelijat.items():
    if opnro in tehtavat:
        tehtava = tehtavat[opnro]
        print(f"{nimi} {tehtava}")
    else:
        print(f"{nimi}")
