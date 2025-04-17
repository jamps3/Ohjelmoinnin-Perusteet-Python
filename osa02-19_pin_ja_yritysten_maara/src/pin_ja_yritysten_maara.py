correct_pin = "4321"
attempts = 0

while True:
    pin = input("PIN-koodi: ")
    attempts += 1
    if pin == correct_pin:
        if attempts == 1:
            print("Oikein, tarvitsit vain yhden yrityksen!")
        else:
            print(f"Oikein, tarvitsit {attempts} yritystä")
        break
    else:
        print("Väärin")
