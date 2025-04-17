def viiva(merkkia, mjono):
    if len(mjono) == 0:
        for i in range(merkkia):
            print("*", end="")
        return
    for i in range(merkkia):
        print(mjono[0], end="")
    print("")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "")
