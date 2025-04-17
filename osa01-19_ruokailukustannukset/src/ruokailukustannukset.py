unicafe_kerrat_viikossa = int(input("Montako kertaa viikossa syöt Unicafessa? "))
unicafe_lounas_hinta = float(input("Unicafe-lounaan hinta? "))
viikon_ruokaostokset = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

paivan_kustannukset = (unicafe_lounas_hinta * unicafe_kerrat_viikossa / 7) + (viikon_ruokaostokset / 7)
viikon_kustannukset = (unicafe_lounas_hinta * unicafe_kerrat_viikossa) + viikon_ruokaostokset

print("Kustannukset keskimäärin:")
print(f"Päivässä {paivan_kustannukset} euroa")
print(f"Viikossa {viikon_kustannukset} euroa")