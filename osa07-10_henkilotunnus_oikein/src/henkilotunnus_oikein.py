from datetime import datetime
import math

def onko_validi(hetu: str):
    # Pituuden tarkistus
    if len(hetu) != 11:
        return False
    # Välimerkin tarkistus
    valimerkki = hetu[6]
    if valimerkki == "+":
        # Päivämäärän tarkistus
        try:
            day, month, year = int(hetu[:2]), int(hetu[2:4]), int(hetu[4:6])
            year = year + 1800
            if (1 <= day <= 31 and 1 <= month <= 12 and 1800 <= year <= 2100):
                datetime(year=year, month=month, day=day)
            else: return False
        except ValueError:
            return False
    elif valimerkki == "-":
        # Päivämäärän tarkistus
        try:
            day, month, year = int(hetu[:2]), int(hetu[2:4]), int(hetu[4:6])
            year = year + 1900
            if (1 <= day <= 31 and 1 <= month <= 12 and 1800 <= year <= 2100):
                datetime(year=year, month=month, day=day)
            else: return False
        except ValueError:
            return False
    elif valimerkki == "A":
        # Päivämäärän tarkistus
        try:
            day, month, year = int(hetu[:2]), int(hetu[2:4]), int(hetu[4:6])
            year = year + 2000
            if (1 <= day <= 31 and 1 <= month <= 12 and 1800 <= year <= 2100):
                datetime(year, month, day)
            else: return False
        except ValueError:
            return False
    else: # Not valid
        raise ValueError("Invalid delimiter")
    # Tarkistusmerkki
    indeksi = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    numerosarja = hetu[:6] + hetu[7:10]
    jakoj = int(numerosarja) % 31
    if indeksi[jakoj] != hetu[10]:
        return False    
    return True

if __name__ == "__main__":
    print(onko_validi("230827-906F")) #True
    print(onko_validi("120488+246L")) #True
    print(onko_validi("310823A9877")) #True
    print(onko_validi("230828-906F")) #False
    print(onko_validi("120488-246L")) #True
    print(onko_validi("310823A9876")) #False
    
    print(onko_validi("080842-720N")) #True
    
    print(onko_validi("100400A644E")) #True?
    print(onko_validi("081842-720N")) #True?
    print(onko_validi("230200+1234")) #True?