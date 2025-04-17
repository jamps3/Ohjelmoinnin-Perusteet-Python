def kumpi_voitti(pelilauta: list):
    pelaaja1 = 0
    pelaaja2 = 0
    for rivi in pelilauta:
        for alkio in range(len(rivi)):
            if rivi[alkio] == 1:
                pelaaja1 += 1
            elif rivi[alkio] == 2:
                pelaaja2 += 1
    if pelaaja1 > pelaaja2:
        return 1
    elif pelaaja2 > pelaaja1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    pelilauta = [0, 1, 0], [0, 2, 1], [0, 1, 2]
    print(kumpi_voitti(pelilauta))