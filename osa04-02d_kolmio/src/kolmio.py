def viiva(merkkia, mjono):
    if len(mjono) == 0:
        for i in range(merkkia):
            print("*", end="")
        return
    for i in range(merkkia):
        print(mjono[0], end="")
    print("")

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    for i in range(1, koko + 1):
        viiva(i, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
