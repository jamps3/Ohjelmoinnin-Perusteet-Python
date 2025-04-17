lahjan_suuruus = float(input("Lahjan suuruus? "))

if lahjan_suuruus < 5000:
    vero = 0
elif 5000 <= lahjan_suuruus < 25000:
    vero = 100 + (lahjan_suuruus - 5000) * 0.08
elif 25000 <= lahjan_suuruus < 55000:
    vero = 1700 + (lahjan_suuruus - 25000) * 0.10
elif 55000 <= lahjan_suuruus < 200000:
    vero = 4700 + (lahjan_suuruus - 55000) * 0.12
elif 200000 <= lahjan_suuruus < 1000000:
    vero = 22100 + (lahjan_suuruus - 200000) * 0.15
else:
    vero = 142100 + (lahjan_suuruus - 1000000) * 0.17

if vero == 0:
    print("Ei veroa!")
else:
    print(f"Vero: {vero:.1f} euroa")
