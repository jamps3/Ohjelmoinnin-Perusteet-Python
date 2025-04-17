def tuplaa_alkiot(luvut: list):
    tuplaluvut = []
    for luku in luvut:
        tuplaluvut.append(luku * 2)
    return tuplaluvut

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)