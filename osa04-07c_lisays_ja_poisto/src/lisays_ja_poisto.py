lista = []
luku = 1
while (True):
    print("Lista on nyt ", end="")
    print(lista)
    valinta = input("(l)isää, (p)oista vai e(x)it: ")
    if valinta == "l":
        lista.append(luku)
        luku += 1
    if valinta == "p":
        lista.pop()
        luku -= 1
    if valinta == "x":
        break
print("Moi!")