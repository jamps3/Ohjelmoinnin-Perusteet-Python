def kertaa_kymmenen(alku: int, loppu: int):
    sanakirja = {}
    for i in range(alku, loppu+1):
        sanakirja[i] = i*10
    return sanakirja

if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)