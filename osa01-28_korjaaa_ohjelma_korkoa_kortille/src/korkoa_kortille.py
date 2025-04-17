#korkoa_kortille.py

#Kysyy käyttäjältä pisteitä ja laskee niille bonuksen
#Tulostaa lopuksi pisteiden määrän
pisteet = int(input("Kuinka paljon pisteitä? "))
if pisteet < 100:
    pisteet *= 1.1
    print("Sait 10 % bonusta")

elif pisteet >= 100:
    pisteet *= 1.15
    print("Sait 15 % bonusta")

print("Pisteitä on nyt", pisteet)
