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

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int):
    sudoku[rivi_nro][sarake_nro] = luku

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

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)