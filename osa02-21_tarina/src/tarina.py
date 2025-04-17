tarina = []
edellinen_sana = ""

while True:
    sana = input("Anna sana: ")
    if sana == "loppu" or sana == edellinen_sana:
        break
    tarina.append(sana)
    edellinen_sana = sana

print(" ".join(tarina))
