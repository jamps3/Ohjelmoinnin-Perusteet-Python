import os

if True:
    # tänne ei tulla
    opiskelijatiedot = input("opiskelijatiedot: ")
    tehtavatiedot = input("tehtävätiedot: ")
    koepistetiedot = input("koepisteet: ")
    kurssintiedot = input("kurssin tiedot: ")
else:
    # kovakoodatut syötteet
    # Construct file paths
    opiskelijatiedot = "opiskelijat2.csv"
    opiskelijatiedot = os.path.join(os.path.dirname(__file__), 'opiskelijat1.csv')
    tehtavatiedot = "tehtavat2.csv"
    tehtavatiedot = os.path.join(os.path.dirname(__file__), 'tehtavat1.csv')
    koepistetiedot = "koepisteet2.csv"
    koepistetiedot = os.path.join(os.path.dirname(__file__), 'koepisteet1.csv')
    kurssintiedot = "kurssi2.txt"
    kurssintiedot = os.path.join(os.path.dirname(__file__), 'kurssi1.txt')

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

with open(kurssintiedot) as tiedosto:
    kurssinnimi = ""
    laajuus = 0
    for rivi in tiedosto:
        if rivi.startswith("nimi: "):
            kurssinnimi = rivi.split("nimi: ")[1].strip()
        elif rivi.startswith("laajuus opintopisteina: "):
            laajuus = int(rivi.split("laajuus opintopisteina: ")[1].strip())
    #print(kurssinnimi + str(laajuus))
        
arvosanat = {}

#print(f"{'nimi':<30}{'teht_lkm':<10}{'teht_pist':<10}{'koe_pist':<10}{'yht_pist':<10}{'arvosana':<10}")

# Clear output files
with open("tulos.txt", "w") as ulos:
    string = kurssinnimi + ", " + str(laajuus) + " opintopistettä\n"
    ulos.write(string)
    ulos.write("=" * (len(string) - 1))
    ulos.write("\n")
    ulos.write(f"{'nimi':<30}{'teht_lkm':<10}{'teht_pist':<10}{'koe_pist':<10}{'yht_pist':<10}{'arvosana':<10}\n")

with open("tulos.csv", "w") as ulos:
    pass

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
        
        # Tulostus
        #print(f"{nimi:<30}{tehtavat[opnro]:<10}{int(prosenttiosuus / 10):<10}{koepisteet[opnro]:<10}{pisteet:<10}{arvosana:<10}")
        # Write to tulos.txt
        with open("tulos.txt", "a") as ulos:
            ulos.write(f"{nimi:<30}{tehtavat[opnro]:<10}{int(prosenttiosuus / 10):<10}{koepisteet[opnro]:<10}{pisteet:<10}{arvosana:<10}\n")
        # Write to tulos.csv
        with open("tulos.csv", "a") as ulos:
            ulos.write(opnro + ";" + nimi + ";" + str(arvosana) + "\n")