def sudoku_oikein(sudoku: list) -> bool:
    for i in range(0, len(sudoku)):
        if not rivi_oikein(sudoku, i):
            print("Rivi", i, "väärin")
            return False
    for i in range(0, len(sudoku[i])):
        if not sarake_oikein(sudoku, i):
            print("Sarake", i, "väärin")
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not nelio_oikein(sudoku, i, j):
                print("Nelio", i, j, "väärin")
                return False
    return True

def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int) -> bool:
    numbers = set()
    for i in range(rivi_nro, rivi_nro + 3):
        for j in range(sarake_nro, sarake_nro + 3):
            num = sudoku[i][j]
            print(num, end=" ")
            if num != 0:
                if num in numbers:
                    return False
                numbers.add(num)
    return True

def sarake_oikein(sudoku: list, sarake_nro: int) -> bool:
    sarake = sudoku[sarake_nro]
    for i in sudoku[sarake_nro]:
        numbers = set()
        for line in sudoku:
            if line[sarake_nro] != 0:
                if line[sarake_nro] in numbers:
                    return False
                numbers.add(line[sarake_nro])
        return True

def rivi_oikein(sudoku: list, rivi_nro: int) -> bool:
    rivi = sudoku[rivi_nro]
    for i in sudoku[rivi_nro]:
        numbers = set()
        for num in rivi:
            if num != 0:
                if num in numbers:
                    return False
                numbers.add(num)
        return True

if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))
    
    sudoku3 = [
        [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
        [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
        [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
        [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
        [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
        [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
        [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
        [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
        [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
    ]
    
    print(sudoku_oikein(sudoku3))