fahrenheit = float(input("Anna lämpötila (F): "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} fahrenheit-astetta on {celsius} celsius-astetta")
if celsius < 0:
    print("Paleltaa!")
