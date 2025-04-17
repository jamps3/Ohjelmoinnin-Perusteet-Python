# Kysytään käyttäjän nimeä
nimi = input("Anna nimesi: ")

# Tarkistetaan nimi ja tulostetaan vastaus
if nimi in ["Tupu", "Hupu", "Lupu"]:
    print("Olet luultavasti Aku Ankan veljenpoika.")
elif nimi in ["Mortti", "Vertti"]:
    print("Olet luultavasti Mikki Hiiren veljenpoika.")
else:
    print("Et ole kenenkään tuntemani hahmon veljenpoika.")