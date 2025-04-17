#import math
import random

# arpoo annetun määrän satunnaislukuja väliltä alaraja...ylaraja,
# tallentaa ne listaan ja palauttaa listan.
# Lukujen tulee olla palautetussa listassa suuruusjärjestyksessä.
# Koska kyseessä ovat lottonumerot, sama numero ei saa esiintyä listassa kahta kertaa
def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    numerot = []
    while len(numerot) < maara:
        numero = random.randint(alaraja, ylaraja)
        if numero not in numerot:
            numerot.append(numero)

    numerot.sort()
    return numerot

if __name__ == "__main__":
    print(lottonumerot(7, 1, 53))
    for numero in lottonumerot(7, 1, 40):
        print(numero)