name = input("Mikä on nimesi: ")
if name != "Jerry":
    annokset = int(input("Kuinka monta annosta keittoa: "))
    hinta = annokset * 5.90
    print(f"Kokonaishinta on {hinta:.2f}")
print("Seuraava!")