mjono1 = input("Anna jono 1: ")
mjono2 = input("Anna jono 2: ")
if len(mjono1) > len(mjono2):
    print(mjono1 + " on pidempi")
elif len(mjono1) == len(mjono2):
    print("Jonot ovat yhtä pitkät")
else:
    print(mjono2 + " on pidempi")