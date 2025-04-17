def pisimman_pituus(lista):
    pisin = 0
    for i in lista:
        if len(i) > pisin:
            pisin = len(i)
    return pisin