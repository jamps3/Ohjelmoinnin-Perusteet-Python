def poista_pienin(lista: list):
    if len(lista) == 0:
        return
    pienin = min(lista)
    lista.remove(pienin)

if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)