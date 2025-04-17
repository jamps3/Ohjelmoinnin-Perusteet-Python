sana = input("Sana: ")
merkki = input("Merkki: ")
kohta = sana.find(merkki)
while kohta < len(sana) - 2:
    if (sana[kohta] == merkki):
        print (sana[kohta:kohta+3])
    sana = sana[1:]