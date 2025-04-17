import math
while (True):
    luku = int(input("Anna luku: "))
    if luku < 1:
        break
    print("Luvun", luku, "kertoma on", math.factorial(luku))
print("Kiitos ja moi!")