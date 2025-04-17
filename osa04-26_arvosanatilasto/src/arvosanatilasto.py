def arvosanatilastot():
    koepisteet = []
    harjoitustehtavat = []

    while True:
        rivi = input("Koepisteet ja harjoitusten määrä: ")
        if rivi == "":
            break
        koe, harjoitus = map(int, rivi.split())
        koepisteet.append(koe)
        harjoitustehtavat.append(harjoitus)

    if not koepisteet:
        print("Ei syötettyjä tietoja.")
        return

    # Lasketaan harjoituspisteet
    harjoituspisteet = [ht // 10 for ht in harjoitustehtavat]

    # Lasketaan kokonaispisteet
    kokonaispisteet = [kp + hp for kp, hp in zip(koepisteet, harjoituspisteet)]

    # Lasketaan arvosanat
    arvosanat = []
    for kp, kp_total in zip(koepisteet, kokonaispisteet):
        if kp < 10:
            arvosanat.append(0)
        elif kp_total <= 14:
            arvosanat.append(0)
        elif kp_total <= 17:
            arvosanat.append(1)
        elif kp_total <= 20:
            arvosanat.append(2)
        elif kp_total <= 23:
            arvosanat.append(3)
        elif kp_total <= 27:
            arvosanat.append(4)
        else:
            arvosanat.append(5)

    # Tulostetaan tilastot
    print("Tilasto:")
    print(f"Pisteiden keskiarvo: {sum(kokonaispisteet) / len(kokonaispisteet):.1f}")
    hyvaksytyt = sum(1 for arvosana in arvosanat if arvosana > 0)
    print(f"Hyväksymisprosentti: {100 * hyvaksytyt / len(arvosanat):.1f}")
    print("Arvosanajakauma:")
    for i in range(5, -1, -1):
        print(f"  {i}: {'*' * arvosanat.count(i)}")

# Kutsutaan funktiota
arvosanatilastot()