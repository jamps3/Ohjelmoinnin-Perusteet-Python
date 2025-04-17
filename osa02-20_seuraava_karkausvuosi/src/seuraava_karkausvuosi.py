def on_karkausvuosi(vuosi):
    if vuosi % 4 == 0:
        if vuosi % 100 == 0:
            if vuosi % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

annettuvuosi = int(input("Vuosi: "))
vuosi = annettuvuosi + 1  # Start checking from the next year

while not on_karkausvuosi(vuosi):
    vuosi += 1

print(f"Vuotta {annettuvuosi} seuraava karkausvuosi on {vuosi}")