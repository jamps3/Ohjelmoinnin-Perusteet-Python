luku = int(input("Anna luku: "))
for i in range(1, luku // 2 + 1):
    print(i)
    print(luku + 1 - i)
if luku % 2 != 0:
    print(luku // 2 + 1)
