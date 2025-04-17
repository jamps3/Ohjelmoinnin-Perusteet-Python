pisteet = int(input("Anna pisteet [0-100]: "))

if pisteet < 0 or pisteet > 100:
    print("Arvosana: mahdotonta!")
elif pisteet < 50:
    print("Arvosana: hylätty")
elif pisteet < 60:
    print("Arvosana: 1")
elif pisteet < 70:
    print("Arvosana: 2")
elif pisteet < 80:
    print("Arvosana: 3")
elif pisteet < 90:
    print("Arvosana: 4")
else:
    print("Arvosana: 5")
