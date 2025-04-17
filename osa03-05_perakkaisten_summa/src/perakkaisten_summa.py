luku = int(input("Mihin asti: "))
summa = 3
laskuri = 3
laskettiin = "1 + 2"
while summa < luku:
    laskettiin += " + " + str(laskuri)
    summa = summa + laskuri
    laskuri += 1
print("Laskettiin " + laskettiin + " = " + str(summa))