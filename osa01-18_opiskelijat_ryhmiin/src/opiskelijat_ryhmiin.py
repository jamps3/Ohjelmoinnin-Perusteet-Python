opiskelijoiden_maara = int(input("Montako opiskelijaa? "))
ryhman_koko = int(input("Mikä on ryhmän koko? "))

ryhmien_maara = opiskelijoiden_maara // ryhman_koko
if opiskelijoiden_maara % ryhman_koko != 0:
    ryhmien_maara += 1

print(f"Ryhmien määrä: {ryhmien_maara}")