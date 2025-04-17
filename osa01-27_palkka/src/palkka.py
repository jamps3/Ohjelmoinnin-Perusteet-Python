# palkka.py

# Kysytään käyttäjältä tuntipalkka, työtunnit ja viikonpäivä
tuntipalkka = float(input("Tuntipalkka: "))
tyotunnit = float(input("Työtunnit: "))
viikonpaiva = input("Viikonpäivä: ").strip().lower()

# Lasketaan palkka
if viikonpaiva == "sunnuntai":
    palkka = tuntipalkka * tyotunnit * 2
else:
    palkka = tuntipalkka * tyotunnit

# Tulostetaan palkka
print(f"Palkka {palkka} euroa")