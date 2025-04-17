import random
from string import ascii_lowercase
import string

def luo_hyva_salasana(pituus: int, numerot: bool, erikoismerkit: bool):
    while True:
        salasana = ""
        for _ in range(pituus):
            if not numerot and not erikoismerkit:
                salasana += random.choice(ascii_lowercase)
            elif not numerot and erikoismerkit:
                salasana += random.choice(ascii_lowercase + "!?=+-()#")
            elif numerot and not erikoismerkit:
                salasana += random.choice(ascii_lowercase + string.digits)
            elif numerot and erikoismerkit:
                salasana += random.choice(ascii_lowercase + string.digits + "!?=+-()#")
        
        if (not numerot or any(char in string.digits for char in salasana)) and \
           (not erikoismerkit or any(char in "!?=+-()#" for char in salasana)):
            break
    
    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_hyva_salasana(8, True, True))