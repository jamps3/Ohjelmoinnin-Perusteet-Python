def shakkilauta(x):
    for i in range(x):
        for j in range(x):
            if (i+j) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)
