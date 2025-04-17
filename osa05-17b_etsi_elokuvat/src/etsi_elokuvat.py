def etsi_elokuvat(rekisteri: list, hakusana: str):
    hakusana = hakusana.lower()
    loydetyt = []
    for elokuva in rekisteri:
        if hakusana in elokuva["nimi"].lower():
            loydetyt.append(elokuva)
    return loydetyt

if __name__ == "__main__":
    rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
    {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
    {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

    lista = etsi_elokuvat(rekisteri, "python")
    print(lista)