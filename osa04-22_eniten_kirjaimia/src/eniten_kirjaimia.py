def eniten_kirjainta(mjono:str):
    eniten = 0
    merkki = ""
    for i in mjono:
        if mjono.count(i) > eniten:
            merkki = i
            eniten = mjono.count(i)
    return merkki

if __name__ == "__main__":
    print(eniten_kirjainta("lollerskates"))