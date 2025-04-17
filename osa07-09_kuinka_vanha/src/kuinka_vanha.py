from datetime import datetime

vuosituhat = datetime(1999, 12, 31)
paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))

aika = datetime(vuosi, kuukausi, paiva)
erotus = vuosituhat - aika
if erotus.days < 0:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")
else:
    print("Olit " + str(erotus.days) + " päivää vanha, kun vuosituhat vaihtui.")