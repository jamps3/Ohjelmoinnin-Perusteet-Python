sana = input("Sana: ")
leveys = 30
reuna = '*' * leveys
padding = (leveys - len(sana) - 2) // 2
rivi = '*' + ' ' * padding + sana + ' ' * (leveys - len(sana) - padding - 2) + '*'

print(reuna)
print(rivi)
print(reuna)