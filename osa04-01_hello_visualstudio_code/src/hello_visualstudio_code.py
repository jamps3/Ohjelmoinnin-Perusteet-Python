while (True):
    mjono = input("Editori: ")
    if "visual studio code" == mjono.lower():
        print("loistava valinta!")
        break
    elif mjono.lower() == "word" or mjono.lower() == "notepad":
        print("surkea")
    else:
        print("ei ole hyvä")
