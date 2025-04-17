def lue(kysymys, luku1, luku2):
    while True:
        try:
            syote = input(kysymys)
            luku = int(syote)
            if luku2 >= luku >= luku1:
                return luku
        except ValueError:
            pass # tämä komento ei tee mitään

        print(f"Syötteen on oltava kokonaisluku väliltä {luku1}...{luku2}")

if __name__ == "__main__":
    luku = lue()
    print(luku)