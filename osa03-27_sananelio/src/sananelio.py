def nelio(sana, pituus):
    index = 0
    for row in range(pituus):
        for col in range(pituus):
            print(sana[index % len(sana)], end="")
            index += 1
        print()

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    #sana = input("Anna sana: ")
    sana = "abc"
    #pituus = int(input("Kuinka monta kertaa tulostetaan: "))
    pituus = 5
    nelio(sana, pituus)