import math
import fractions

def jaa_palasiksi(maara: int):
    palaset = [fractions.Fraction(1, maara) for _ in range(maara)]
    return palaset

if __name__ == "__main__":
    print(jaa_palasiksi(3))