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

if __name__ == "__main__":
    sudoku = [
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

    print(sarake_oikein(sudoku, 0))
    print(sarake_oikein(sudoku, 1))