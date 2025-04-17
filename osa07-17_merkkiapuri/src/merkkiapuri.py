def vaihda_koko(merkkijono: str):
    for i in range(len(merkkijono)):
        if merkkijono[i].isupper():
            merkkijono = merkkijono[:i] + merkkijono[i].lower() + merkkijono[i+1:]
        elif merkkijono[i].islower():
            merkkijono = merkkijono[:i] + merkkijono[i].upper() + merkkijono[i+1:]
    return merkkijono

def puolita(merkkijono: str):
    if len(merkkijono) % 2 == 0:
        return merkkijono[:len(merkkijono)//2], merkkijono[len(merkkijono)//2:]
    else:
        return merkkijono[:len(merkkijono)//2], merkkijono[len(merkkijono)//2:]

def poista_erikoismerkit(merkkijono: str):
    erikoismerkit = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '¤']
    for merkki in erikoismerkit:
        merkkijono = merkkijono.replace(merkki, '')
    return merkkijono

if __name__ == "__main__":
    merkkijono = input("Anna merkkijono: ")
    print("Vaihda koko:", vaihda_koko(merkkijono))
    print("Puolita:", puolita(merkkijono))
    print("Poista erikoismerkit:", poista_erikoismerkit(merkkijono))