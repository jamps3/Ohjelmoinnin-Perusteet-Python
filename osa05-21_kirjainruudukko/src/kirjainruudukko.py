#Kirjainruudukko
kerrokset = int(input("Kerrokset: "))
    
if kerrokset < 1:
    print("Size must be at least 1")
    
size = 2 * kerrokset - 1
for i in range(size):
    for j in range(size):
        letter = chr(65 + max(abs(kerrokset - 1 - i), abs(kerrokset - 1 - j)))  # 'A' is 65 in ASCII
        print(letter, end="")
    print()