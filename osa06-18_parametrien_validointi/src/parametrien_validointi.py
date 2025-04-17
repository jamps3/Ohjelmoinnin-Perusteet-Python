def uusi_henkilo(nimi: str, ika: int):
    if nimi == "":
        raise ValueError("nimi on tyhjä")
    if len(nimi.split()) < 2:
        raise ValueError("nimi ei sisällä vähintään kahta sanaa")
    if len(nimi) > 40:
        raise ValueError("nimi liian pitkä")
    if ika < 0:
        raise ValueError("ikä on negatiivinen")
    if ika > 150:
        raise ValueError("ikä suurempi kuin 150")
    henkilo = (nimi, ika)
    return henkilo

if __name__ == "__main__":
    try:
        henkilo = uusi_henkilo("Pekka Puupää", 35)
        print(henkilo)
    except ValueError as e:
        print(e)