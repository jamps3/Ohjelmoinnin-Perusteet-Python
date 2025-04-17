sanat = []
while True:
    sana = input("sana: ")
    if sana in sanat:
        print("Annoit " + str(len(sanat)) + " eri sanaa")
        break
    else:
        sanat.append(sana)