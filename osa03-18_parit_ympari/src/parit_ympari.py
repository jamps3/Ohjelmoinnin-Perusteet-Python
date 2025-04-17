luku = int(input("Anna luku: "))
for i in range(1, luku + 1, 2):
    if i + 1 <= luku:
        print(i + 1)
    print(i)