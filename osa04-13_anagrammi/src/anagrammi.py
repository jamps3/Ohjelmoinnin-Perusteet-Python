def anagrammi(str1, str2):
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
    return sorted1 == sorted2

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(anagrammi("talo", "tola")) # True
    print(anagrammi("talo", "lato")) # True
    print(anagrammi("talo", "olat")) # True
    print(anagrammi("tammi", "mitta")) # False
    print(anagrammi("python", "java")) # False