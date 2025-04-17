def pisimmat(lista):
    pisin = 0
    items = []
    for i in lista:
        if len(i) > pisin:
            pisin = len(i)
            items = [i]
        elif len(i) == pisin:
            items.append(i)
    return items