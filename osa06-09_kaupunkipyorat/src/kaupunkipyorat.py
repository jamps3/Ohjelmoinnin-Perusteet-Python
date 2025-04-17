import os # Import os module for file path handling
# tämä rivi tarvitaan, jotta saadaan käyttöön metodi sqrt
import math

def hae_asematiedot(tiedosto: str):
    sanakirja = {}
    # Construct file path
    tiedosto = os.path.join(os.path.dirname(__file__), tiedosto)
    #tiedosto = tiedosto
    # Lue CSV-tiedosto ja tallenna tiedot sanakirjaan
    with open(tiedosto, encoding="utf-8") as csvfile:
        next(csvfile)  # Skip the first line
        for rivi in csvfile:
            # Jaa rivi osiin
            osat = rivi.strip().split(";")
            # Ota kolmas osa avaimena ja 0, 1 osat arvoina
            avain = osat[3]
            arvo = float(osat[0]), float(osat[1])
            # Tallenna avain-arvo-pari sanakirjaan
            sanakirja[avain] = arvo
    # Palauta sanakirja
    return sanakirja

def etaisyys(asemat: dict, asema1: str, asema2: str):
    # Laske etäisyys kahden aseman välillä
    # Ota aseman koordinaatit
    koordinaatti1 = asemat[asema1]
    koordinaatti2 = asemat[asema2]
    #print("koordinaatit: " + str(koordinaatti1[0]) + " " + str(koordinaatti1[1]))
    #print("koordinaatit: " + str(koordinaatti2[0]) + " " + str(koordinaatti2[1]))
    # Laske etäisyys
    x_kilometreina = (koordinaatti1[0] - koordinaatti2[0]) * 55.26
    y_kilometreina = (koordinaatti1[1] - koordinaatti2[1]) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    # Palauta etäisyys
    return etaisyys

def suurin_etaisyys(asemat: dict):
    # Selvittää mitkä kaksi asemaa ovat kauimpana toisistaan.
    # Funktio palauttaa tuplen, jonka ensimmäiset kaksi arvoa
    # kertovat asemien nimet ja kolmas arvo niiden välisen etäisyyden.
    max_etaisyys = 0
    kaukaisin_asema = ("", "", 0)
    asemat_nimet = list(asemat.keys())

    for i in range(len(asemat_nimet)):
        for j in range(i + 1, len(asemat_nimet)):
            asema1 = asemat_nimet[i]
            asema2 = asemat_nimet[j]
            etaisyys_vali = etaisyys(asemat, asema1, asema2)
            if etaisyys_vali > max_etaisyys:
                max_etaisyys = etaisyys_vali
                kaukaisin_asema = (asema1, asema2, max_etaisyys)

    return kaukaisin_asema

if __name__ == "__main__":
    result = hae_asematiedot("stations1.csv")
    print(result)
    result = etaisyys(result, "Viiskulma", "Sepankatu")
    print(result)
    asemat = hae_asematiedot("stations1.csv")
    result = suurin_etaisyys(asemat)
    result = f"{result[0]} {result[1]} {result[2]}"
    print(result)
