import os

def tallenna_henkilo(henkilo: tuple):
    # Construct file path
    #tiedosto = os.path.join(os.path.dirname(__file__), 'henkilot.csv')
    tiedosto = 'henkilot.csv'
    with open(tiedosto, 'a') as henkilot_file:
        henkilot_file.write(henkilo[0] + ";" + str(henkilo[1]) + ";" + str(henkilo[2]) + "\n")

if __name__ == "__main__":
    henkilo = ("Kimmo Kimmonen", 37, 175.2)
    tallenna_henkilo(henkilo)