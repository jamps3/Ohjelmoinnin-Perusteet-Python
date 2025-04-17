def lyhin(lista):
    lyhin = len(lista[0])
    item = lista[0]
    for i in lista:
        if len(i) < lyhin:
            lyhin = len(i)
            item = i
    return item