while True:
    mjono = input("Sana: ")
    if len(mjono) > 20:
        break
    if len(mjono) < 20:
        print ("*" * (20-len(mjono)) + mjono)
        break
    else:
        print(mjono)
        break