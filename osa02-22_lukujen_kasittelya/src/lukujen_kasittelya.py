#lukujen_kasittelya.py

lukumaara = 0
summa = 0
posit = 0
negat = 0

print("Syötä kokonaislukuja, 0 lopettaa:")
while True:
    luku = int(input("Luku: "))
    if luku == 0:
        break
    lukumaara += 1
    summa += luku
    if luku > 0:
        posit += 1
    else:
        negat += 1
print("Lukuja yhteensä", lukumaara)
print("Lukujen summa", summa)
print("Lukujen keskiarvo", summa / lukumaara)
print("Positiivisia", posit)
print("Negatiivisia", negat)