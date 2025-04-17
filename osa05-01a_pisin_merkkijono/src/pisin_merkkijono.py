def pisin(jonot: list):
    pisin = ""
    for jono in jonot:
        if len(jono) > len(pisin):
            pisin = jono
    return pisin

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))