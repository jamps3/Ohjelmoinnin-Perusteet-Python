def pisin_naapurijono(lista):
    if not lista:
        return []

    longest = []
    current = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] == lista[i-1] + 1 or lista[i] == lista[i-1] - 1:
            current.append(lista[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [lista[i]]

    if len(current) > len(longest):
        longest = current

    return len(longest)

if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))