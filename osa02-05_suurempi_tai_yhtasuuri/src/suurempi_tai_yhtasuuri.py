luku = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

if luku == luku2:
    print("Luvut ovat yhtä suuret!")
elif luku < luku2:
    print("Suurempi luku:", luku2)
elif luku2 < luku:
    print("Suurempi luku:", luku)