import os
import random

def sanat(n: int, alku: str):
    sanat = []
    tiedosto = os.path.join(os.path.dirname(__file__), 'sanat.txt')
    
    with open(tiedosto, "r") as file:
        lines = [line.strip() for line in file]  # Stripping newline characters

    matches = [line for line in lines if line.startswith(alku)]
    
    if len(matches) < n:
        raise ValueError(f"Only {len(matches)} words found starting with '{alku}', but {n} were requested.")

    sanat = random.sample(matches, n)  # Randomly select `n` unique words
    return sanat

if __name__ == "__main__":
    try:
        lista = sanat(50, "cat")
        for sana in lista:
            print(sana)
        
        lista = sanat(500, "car")
        for sana in lista:
            print(sana)
        
        lista = sanat(45, "absol")
        for sana in lista:
            print(sana)
        
        lista = sanat(10, "superd")
        for sana in lista:
            print(sana)
    except:
        print("error!")
        pass