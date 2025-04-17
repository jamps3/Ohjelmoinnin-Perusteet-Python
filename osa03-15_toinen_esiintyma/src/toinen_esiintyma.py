mjono = input("Anna merkkijono: ")
osa = input("Anna osajono: ")

kohta = mjono.find(osa)

if kohta == -1:
    print("Osajono ei esiinny merkkijonossa kahdesti.")
else:
    kohta2 = mjono.find(osa, kohta + len(osa))
    if kohta2 == -1:
        print("Osajono ei esiinny merkkijonossa kahdesti.")
    else:
        print("Osajonon toinen esiintymä on kohdassa " + str(kohta2) + ".")
