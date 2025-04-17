def keskiarvo(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa / len(lista)
    
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)
