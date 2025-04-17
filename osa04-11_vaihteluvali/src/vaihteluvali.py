def vaihteluvali(lista):
    # laske suurin ja pienin arvo listassa
    suurin = max(lista)
    pienin = min(lista)
    # laske vaihteluväli
    vaihteluväli = suurin - pienin
    return vaihteluväli

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)