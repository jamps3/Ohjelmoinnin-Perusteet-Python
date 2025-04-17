import random
from string import ascii_lowercase

#Funktio, jonka avulla on mahdollista luoda halutun pituisia satunnaisista pienistä kirjaimista (väliltä a-z) muodostettuja salasanoja.
def luo_salasana(pituus: int):
    salasana = ""
    for _ in range(pituus):
        salasana += random.choice(ascii_lowercase)
    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))