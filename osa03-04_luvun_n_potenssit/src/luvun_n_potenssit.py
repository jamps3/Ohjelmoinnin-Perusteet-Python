luku = int(input("Mihin asti: "))
kerroin = int(input("Mikä kerroin: "))
i = 0
while kerroin**i <= luku:
    print(kerroin**i)
    i += 1