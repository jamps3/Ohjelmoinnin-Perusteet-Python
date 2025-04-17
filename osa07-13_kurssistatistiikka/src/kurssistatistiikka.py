import os
import math
import urllib.request
import json


def hae_kaikki(url: str = "https://studies.cs.helsinki.fi/stats-mock/api/courses"):
    result = []  # Use a list to collect tuples
    # url = "../test/data/courses2.json"
    try:
        # Fetch data from the API
        if url.endswith(".json"):
            data_file_path = os.path.join(os.path.dirname(__file__), url)
            print(data_file_path)
            response = urllib.request.urlopen("file:///" + data_file_path)
        else:
            response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))  # Decode and parse JSON

        # Iterate through the data
        for element in data:
            if element.get("enabled"):  # Check if the course is enabled
                harjoitukset = element.get("exercises")
                pisteetyhteensa = 0
                for e in harjoitukset:
                    pisteetyhteensa += e
                # Extract required elements and append as tuples
                # print(element)
                result.append(
                    (
                        element.get("fullName"),
                        element.get("name"),
                        element.get("year"),
                        pisteetyhteensa,
                    )
                )
    except Exception as e:
        print(e)
        # print(f"Error fetching or processing data: {e}")

    return result


def hae_kurssi(kurssi: str):
    # Fetch all data first
    data = hae_kurssidata(kurssi)
    viikkoja = 0
    opiskelijoita = 0
    tunteja = 0
    harjoituksia = 0
    if data:
        for e in data:
            viikkoja += 1
            opiskelijoita += e[1]
            tunteja += e[2]
            harjoituksia += e[3]
    return {
        "viikkoja": viikkoja,
        "opiskelijoita": opiskelijoita,
        "tunteja": tunteja,
        "tunteja_keskimaarin": math.floor(tunteja / opiskelijoita),
        "tehtavia": harjoituksia,
        "tehtavia_keskimaarin": math.floor(harjoituksia / opiskelijoita),
    }


def hae_kurssidata(kurssi: str):
    """
    Hakee kurssin tiedot ja palauttaa ne sanakirjana.
    Sanakirja sisältää seuraavat avaimet:
    - viikkoja: Kurssin viikkojen määrä
    - opiskelijoita: Kurssilla olevien opiskelijoiden määrä
    - tunteja: Kurssin tuntimäärä
    - tunteja_keskimaarin: Keskimääräinen tuntimäärä opiskelijaa kohden
    - tehtavia: Kurssin tehtävien määrä
    - tehtavia_keskimaarin: Keskimääräinen tehtävämäärä opiskelijaa kohden
    """
    result = []  # Use a list to collect tuples
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + kurssi + "/stats"
    # print(url)
    try:
        # Fetch data from the API
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))  # Decode and parse JSON
        # Iterate through the data
        for week, info in data.items():
            # Extract required elements and append as tuples
            # print(data.items())
            result.append(
                (
                    week,
                    info.get("students"),
                    info.get("hour_total"),
                    info.get("exercise_total"),
                    info.get("hours"),
                )
            )
            # print(result)
    except Exception as e:
        # return None  # Return None if an error occurs
        print(f"Error fetching or processing data: {e}")
    return result


if __name__ == "__main__":
    """
    Sanakirjaan tallennetut arvot määrittyvät seuraavasti:
    viikkoja: kurssia vastaavan JSON-olioiden määrä
    opiskelijoita viikkojen opiskelijamäärien maksimi
    tunteja: kakkien viikkojen tuntimäärien (hour_total) summa
    tunteja_keskimaarin: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)
    tehtavia: kakkien viikkojen tehtävämäärien (exercise_total) summa
    tehtavia_keskimaarin: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)
    """
    print(hae_kaikki())
    print(hae_kurssi("docker2019"))
    print(hae_kurssi("CCFUN"))
