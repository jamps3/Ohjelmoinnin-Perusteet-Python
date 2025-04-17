def laske_alkiot(matriisi: list, alkio: int) -> int:
    lkm = 0
    for rivi in matriisi:
        for arvo in rivi:
            if arvo == alkio:
                lkm += 1
    return lkm

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))