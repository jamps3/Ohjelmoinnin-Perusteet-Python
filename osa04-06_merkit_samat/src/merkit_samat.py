def samat(mjono, i, j):
    #i -= 1
    #j -= 1
    if i < 0 or j < 0 or i >= len(mjono) or j >= len(mjono):
        return False
    else:
        if mjono[i] == mjono[j]:
            return True
    return False

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 2))