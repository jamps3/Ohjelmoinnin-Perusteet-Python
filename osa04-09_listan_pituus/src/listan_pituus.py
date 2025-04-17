def pituus(lista: list):
    """
    Palauttaa listan pituuden.
    Args:
        lista: list, jolle pituus halutaan laskea
    Returns:
        int: listan pituus
    """
    pituus = 0
    for alkio in lista:
        pituus += 1
    return pituus

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = pituus(lista) 
    print(tulos)