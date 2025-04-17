def tulosta_monesti(merkkijono, kertaa):
    for i in range(kertaa):
        print(merkkijono)
        
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)