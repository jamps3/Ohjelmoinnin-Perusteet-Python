def viiva(merkkia, mjono):
    if len(mjono) == 0:
        for i in range(merkkia):
            print("*", end="")
        return
    for i in range(merkkia):
        print(mjono[0], end="")
    print("")

def kuvio(korkeus1, merkki1, korkeus2, merkki2):
    for i in range(korkeus1 + 1):
        viiva(i, merkki1)
    for i in range(korkeus2):
        viiva(korkeus1, merkki2)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
