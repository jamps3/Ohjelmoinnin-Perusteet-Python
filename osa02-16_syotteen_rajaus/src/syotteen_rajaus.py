from math import sqrt

while True:
    luku = int(input("Syötä luku: "))
    if luku < 0:
        print("Epäkelpo luku")
    elif luku == 0:
        print("Lopetetaan...")
        break
    else:
        print(sqrt(luku))
