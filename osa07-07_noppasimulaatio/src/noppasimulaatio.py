import random

# Funktio heita(noppa: str), joka heittää parametrinsa kertomaa noppaa.
def heita(noppa: str):
    tulos = ""
    if noppa == "A":
        numerot = [3, 3, 3, 3, 3, 6]
        tulos = random.choice(numerot)
    elif noppa == "B":
        numerot = [2, 2, 2, 5, 5, 5]
        tulos = random.choice(numerot)
    elif noppa == "C":
        numerot = [1, 4, 4, 4, 4, 4]
        tulos = random.choice(numerot)
    return tulos

# Funktio heittää kokonaisluvun kertoman määrän parametreina olevia noppia.
# Funktio palauttaa tuplen, joka kertoo nopan 1 voittojen lukumäärän, nopan 2 voittojen lukumäärän ja tasapelien lukumäärän.
def pelaa(noppa1: str, noppa2: str, kertaa: int):
    awins = 0
    bwins = 0
    tasapelit = 0
    for i in range(kertaa):
        a = heita(noppa1)
        b = heita(noppa2)
        if a > b:
            awins += 1
        elif b > a:
            bwins += 1
        else:
            tasapelit += 1
    return (awins, bwins, tasapelit)

if __name__ == "__main__":
    """
    for i in range(20):
        print(heita("A"), " ", end="")
    print()
    for i in range(20):
        print(heita("B"), " ", end="")
    print()
    for i in range(20):
        print(heita("C"), " ", end="")
    """
    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)