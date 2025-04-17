# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

# Kysytään käyttäjältä yhtälön kertoimet
a = float(input("Anna a: "))
b = float(input("Anna b: "))
c = float(input("Anna c: "))

# Lasketaan diskriminantti
d = b**2 - 4*a*c

# Lasketaan juuret
x1 = (-b + sqrt(d)) / (2*a)
x2 = (-b - sqrt(d)) / (2*a)

# Tulostetaan juuret
print(f"Juuret ovat {x1} ja {x2}")