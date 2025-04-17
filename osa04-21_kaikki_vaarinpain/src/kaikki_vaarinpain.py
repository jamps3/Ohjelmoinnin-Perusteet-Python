def kaikki_vaarinpain(lista):
    uusi = []
    uusi.append(lista[::-1])
    reversed = []
    for i in range(len(uusi[0])):
        reversed.append(uusi[0][i][::-1])
    uusi = reversed
    return uusi

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)