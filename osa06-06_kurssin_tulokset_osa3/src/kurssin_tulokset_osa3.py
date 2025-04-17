if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koepistetiedot = input("Koepisteet: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
    koepistetiedot = "koepisteet1.csv"

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
        
koepisteet = {}

with open(koepistetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(';')
        if osat[0] == "opnro":
            continue
        koepisteet[osat[0]] = sum(int(x) for x in osat[1:])

arvosanat = {}

print(f"{'nimi':<30}{'teht_lkm':<10}{'teht_pist':<10}{'koe_pist':<10}{'yht_pist':<10}{'arvosana':<10}")

for opnro, nimi in opiskelijat.items():
    if opnro in koepisteet:
        pisteet = 0
        # Koepisteet
        pisteet += koepisteet[opnro]
        # Tehtävät
        if opnro in tehtavat:
            max_tehtavat = 40  # Assuming the maximum number of tasks is 70
            prosenttiosuus = (tehtavat[opnro] / max_tehtavat) * 100
            pisteet += int(prosenttiosuus // 10)
        # Arvosanat
        if pisteet <= 14:
            arvosana = 0
        elif pisteet <= 17:
            arvosana = 1
        elif pisteet <= 20:
            arvosana = 2
        elif pisteet <= 23:
            arvosana = 3
        elif pisteet <= 27:
            arvosana = 4
        else:
            arvosana = 5
        arvosanat[opnro] = arvosana
        
        print(f"{nimi:<30}{tehtavat[opnro]:<10}{int(prosenttiosuus / 10):<10}{koepisteet[opnro]:<10}{pisteet:<10}{arvosana:<10}")