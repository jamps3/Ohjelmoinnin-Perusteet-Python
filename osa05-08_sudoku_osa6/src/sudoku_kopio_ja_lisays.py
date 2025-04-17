def tulosta(sudoku):
    for i in range(0, len(sudoku)):
        for j in range(0, len(sudoku[i])):
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
            
            if (j + 1) % 3 == 0 and j != len(sudoku[i]) - 1:
                print(" ", end="")
        print("")
        if (i + 1) % 3 == 0 and i != len(sudoku) - 1:
            print("")

def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int):
    kopio = []
    for rivi in sudoku:
        kopio.append(rivi.copy())
    kopio[rivi_nro][sarake_nro] = luku
    return kopio

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)