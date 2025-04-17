def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x > len(lauta)-1 or y > len(lauta)-1 or x < 0 or y < 0:
        # Siirto on laudan ulkopuolella
        return False
    if lauta[y][x] == "":
        # Ruutu on tyhjä
        lauta[y][x] = nappula
        return True
    return False
        
if __name__ == "__main__":
    lauta = [["", "X", ""], ["O", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, -1, "X"))
    print(lauta)