def poista_isot(mjonot):
    jonot = []
    for i in mjonot:
        if not i.isupper():
            jonot.append(i)
    return jonot

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)