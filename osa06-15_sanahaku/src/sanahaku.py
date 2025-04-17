import os
import re

def hae_sanat(hakusana: str):
    """
    Palauttaa listana annetun hakusanan mukaiset sanat tiedostosta.
    - '.' represents any single character
    - '*' represents zero or more characters
    """
    # Construct file paths
    tiedosto = "sanat.txt"
    tiedosto = os.path.join(os.path.dirname(__file__), 'sanat.txt')
    
    # Replace '*' with '.*' to adapt to regex syntax
    regex_pattern = hakusana.replace('*', '.*')
    
    # Use '^' and '$' to match the entire line (exact matches)
    regex_pattern = f"^{regex_pattern}$"
    
    result = []

    with open(tiedosto, "r", encoding="utf-8") as file:
        for rivi in file:
            if re.fullmatch(regex_pattern, rivi.strip()):
                #print(rivi, end="")
                result.append(rivi.strip())
    
    return result

#hakusana = input("Anna hakusana: ")
#print(hae_sanat(hakusana))