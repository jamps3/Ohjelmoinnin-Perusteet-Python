def suorita(ohjelma):
    # Muuttujat A-Z
    muisti = {}
    muisti["A"] = 0
    muisti["B"] = 0
    muisti["C"] = 0
    muisti["D"] = 0
    muisti["E"] = 0
    muisti["F"] = 0
    muisti["G"] = 0
    muisti["H"] = 0
    muisti["I"] = 0
    muisti["J"] = 0
    muisti["K"] = 0
    muisti["L"] = 0
    muisti["M"] = 0
    muisti["N"] = 0
    muisti["O"] = 0
    muisti["P"] = 0
    muisti["Q"] = 0
    muisti["R"] = 0
    muisti["S"] = 0
    muisti["T"] = 0
    muisti["U"] = 0
    muisti["V"] = 0
    muisti["W"] = 0
    muisti["X"] = 0
    muisti["Y"] = 0
    muisti["Z"] = 0
    # muisti = {chr(c): 0 for c in range(ord("A"), ord("Z") + 1)}

    tulos = []

    # Program counter to step through instructions
    pc = 0

    while pc < len(ohjelma):
        rivi = ohjelma[pc]
        osat = rivi.split()
        komento = osat[0]

        if komento == "PRINT":
            if osat[1].isalpha():
                arvo = muisti[osat[1]]
            else:
                arvo = int(osat[1])
            tulos.append(arvo)
        elif komento == "MOV":
            if osat[2].isalpha():
                arvo = muisti[osat[2]]
            else:
                arvo = int(osat[2])
            muisti[osat[1]] = arvo
        elif komento == "ADD":
            if osat[2].isalpha():
                muisti[osat[1]] += muisti[osat[2]]
            else:
                arvo = int(osat[2])
                muisti[osat[1]] += arvo
        elif komento == "SUB":
            if osat[2].isalpha():
                muisti[osat[1]] -= muisti[osat[2]]
            else:
                arvo = int(osat[2])
                muisti[osat[1]] -= arvo
        elif komento == "MUL":
            if osat[2].isalpha():
                muisti[osat[1]] *= muisti[osat[2]]
            else:
                arvo = int(osat[2])
                muisti[osat[1]] *= arvo
        elif komento == "JUMP":
            kohta = osat[1]
            # Find the label and update the program counter
            for i, rivi in enumerate(ohjelma):
                if rivi.startswith(kohta + ":"):
                    pc = i
                    break
        elif komento == "IF":
            osa1 = osat[1]
            ehto = osat[2]
            osa2 = osat[3]
            kohta = osat[5]
            if osa2.isalpha():
                osa2 = muisti[osa2]
            if osa1.isalpha():
                osa1 = muisti[osa1]

            condition = False
            if ehto == ">":
                condition = osa1 > int(osa2)
            elif ehto == "<":
                condition = osa1 < int(osa2)
            elif ehto == "<=":
                condition = osa1 <= int(osa2)
            elif ehto == ">=":
                condition = osa1 >= int(osa2)
            elif ehto == "==":
                condition = osa1 == int(osa2)
            elif ehto == "!=":
                condition = osa1 != int(osa2)

            if condition:
                # Find the label and update the program counter
                for i, rivi in enumerate(ohjelma):
                    if rivi.startswith(kohta + ":"):
                        pc = i
                        break
        elif komento == "END":
            break

        pc += 1  # Increment the program counter

    return tulos


if __name__ == "__main__":
    """
    Ohjelma muodostuu riveistä, joista jokainen on yksi seuraavista:
    PRINT [arvo]: tulostaa annetun arvon
    MOV [muuttuja] [arvo]: asettaa muuttujaan annetun arvon
    ADD [muuttuja] [arvo]: lisää muuttujaan annetun arvon
    SUB [muuttuja] [arvo]: vähentää muuttujasta annetun arvon
    MUL [muuttuja] [arvo]: kertoo muuttujan annetulla arvolla
    [kohta]:: määrittelee kohdan, johon voidaan hypätä muualta
    JUMP [kohta]: hyppää annettuun kohtaan
    IF [ehto] JUMP [kohta]: jos ehto pätee, hyppää annettuun kohtaan
    END: lopettaa ohjelman
    """
    """ Esimerkki 1:
    ohjelma1 = []
    ohjelma1.append("MOV A 1")
    ohjelma1.append("MOV B 2")
    ohjelma1.append("PRINT A")
    ohjelma1.append("PRINT B")
    ohjelma1.append("ADD A B")
    ohjelma1.append("PRINT A")
    ohjelma1.append("END")
    tulos = suorita(ohjelma1)
    print(tulos)
    """
    """ Esimerkki 2:
    ohjelma2 = []
    ohjelma2.append("MOV A 1")
    ohjelma2.append("MOV B 10")
    ohjelma2.append("alku:")
    ohjelma2.append("IF A >= B JUMP loppu")
    ohjelma2.append("PRINT A")
    ohjelma2.append("PRINT B")
    ohjelma2.append("ADD A 1")
    ohjelma2.append("SUB B 1")
    ohjelma2.append("JUMP alku")
    ohjelma2.append("loppu:")
    ohjelma2.append("END")
    tulos = suorita(ohjelma2)
    print(tulos)
    """
    """ Esimerkki 3 (kertoma):
    ohjelma3 = []
    ohjelma3.append("MOV A 1")
    ohjelma3.append("MOV B 1")
    ohjelma3.append("alku:")
    ohjelma3.append("PRINT A")
    ohjelma3.append("ADD B 1")
    ohjelma3.append("MUL A B")
    ohjelma3.append("IF B <= 10 JUMP alku")
    ohjelma3.append("END")
    tulos = suorita(ohjelma3)
    print(tulos) # Odotettu tulos: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    """
    """ Esimerkki 4 (alkuluvut):
    ohjelma4 = []
    ohjelma4.append("MOV N 50")
    ohjelma4.append("PRINT 2")
    ohjelma4.append("MOV A 3")
    ohjelma4.append("alku:")
    ohjelma4.append("MOV B 2")
    ohjelma4.append("MOV Z 0")
    ohjelma4.append("testi:")
    ohjelma4.append("MOV C B")
    ohjelma4.append("uusi:")
    ohjelma4.append("IF C == A JUMP virhe")
    ohjelma4.append("IF C > A JUMP ohi")
    ohjelma4.append("ADD C B")
    ohjelma4.append("JUMP uusi")
    ohjelma4.append("virhe:")
    ohjelma4.append("MOV Z 1")
    ohjelma4.append("JUMP ohi2")
    ohjelma4.append("ohi:")
    ohjelma4.append("ADD B 1")
    ohjelma4.append("IF B < A JUMP testi")
    ohjelma4.append("ohi2:")
    ohjelma4.append("IF Z == 1 JUMP ohi3")
    ohjelma4.append("PRINT A")
    ohjelma4.append("ohi3:")
    ohjelma4.append("ADD A 1")
    ohjelma4.append("IF A <= N JUMP alku")
    tulos = suorita(ohjelma4)
    print(tulos)
    """
    """ Lisää esimerkkejä:
    ohjelma4 = []
    ohjelma4.append("MOV A 10")
    ohjelma4.append("alku:")
    ohjelma4.append("PRINT A")
    ohjelma4.append("SUB A 1")
    ohjelma4.append("IF A > 0 JUMP alku")
    ohjelma4.append("END")
    tulos = suorita(ohjelma4)
    print(tulos)  # odotettu tulos: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ohjelma5 = []
    ohjelma5.append("MOV A 1")
    ohjelma5.append("MOV B 1")
    ohjelma5.append("alku:")
    ohjelma5.append("MUL A 2")
    ohjelma5.append("ADD B 1")
    ohjelma5.append("IF B != 101 JUMP alku")
    ohjelma5.append("PRINT A")
    tulos = suorita(ohjelma5)
    print(tulos)  # odotettu tulos: [128]
    ohjelma6 = []
    ohjelma6.append("MOV A 1")
    ohjelma6.append("MOV B 999")
    ohjelma6.append("alku:")
    ohjelma6.append("ADD A 1")
    ohjelma6.append("SUB B 1")
    ohjelma6.append("ADD C 1")
    ohjelma6.append("IF A == B JUMP loppu")
    ohjelma6.append("JUMP alku")
    ohjelma6.append("loppu:")
    ohjelma6.append("PRINT C")
    tulos = suorita(ohjelma6)
    print(tulos)  # odotettu tulos: [999]
    """
    """
    ohjelma7 = []
    ohjelma7.append("MOV N 100")
    ohjelma7.append("PRINT 2")
    ohjelma7.append("MOV A 3")
    ohjelma7.append("alku:")
    ohjelma7.append("MOV B 2")
    ohjelma7.append("MOV Z 0")
    ohjelma7.append("testi:")
    ohjelma7.append("MOV C B")
    ohjelma7.append("uusi:")
    ohjelma7.append("IF C == A JUMP virhe")
    ohjelma7.append("IF C > A JUMP ohi")
    ohjelma7.append("ADD C B")
    ohjelma7.append("JUMP uusi")
    ohjelma7.append("virhe:")
    ohjelma7.append("MOV Z 1")
    ohjelma7.append("JUMP ohi2")
    ohjelma7.append("ohi:")
    ohjelma7.append("ADD B 1")
    ohjelma7.append("IF B < A JUMP testi")
    ohjelma7.append("ohi2:")
    ohjelma7.append("IF Z == 1 JUMP ohi3")
    ohjelma7.append("PRINT A")
    ohjelma7.append("ohi3:")
    ohjelma7.append("ADD A 1")
    ohjelma7.append("IF A <= N JUMP alku")
    ohjelma7.append("END")
    tulos = suorita(ohjelma7)
    print(tulos)  # odotettu tulos: [2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    """
    ohjelma8 = []
    ohjelma8.append("MOV N 100")
    ohjelma8.append("PRINT 2")
    ohjelma8.append("MOV A 3")
    ohjelma8.append("alku:")
    ohjelma8.append("MOV B 2")
    ohjelma8.append("MOV Z 0")
    ohjelma8.append("testi:")
    ohjelma8.append("MOV C B")
    ohjelma8.append("uusi:")
    ohjelma8.append("IF C == A JUMP virhe")
    ohjelma8.append("IF C > A JUMP ohi")
    ohjelma8.append("ADD C B")
    ohjelma8.append("JUMP uusi")
    ohjelma8.append("virhe:")
    ohjelma8.append("MOV Z 1")
    ohjelma8.append("JUMP ohi2")
    ohjelma8.append("ohi:")
    ohjelma8.append("ADD B 1")
    ohjelma8.append("IF B < A JUMP testi")
    ohjelma8.append("ohi2:")
    ohjelma8.append("IF Z == 1 JUMP ohi3")
    ohjelma8.append("PRINT A")
    ohjelma8.append("ohi3:")
    ohjelma8.append("ADD A 1")
    ohjelma8.append("IF A <= N JUMP alku")
    ohjelma8.append("END")
    tulos = suorita(ohjelma8)
    print(
        tulos
    )  # odotettu tulos: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
