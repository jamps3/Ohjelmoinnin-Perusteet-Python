# Kysytään käyttäjältä kolme kirjainta
kirjain1 = input("Anna 1. kirjain: ")
kirjain2 = input("Anna 2. kirjain: ")
kirjain3 = input("Anna 3. kirjain: ")

# Laitetaan kirjaimet listaan ja järjestetään ne aakkosjärjestykseen
kirjaimet = [kirjain1, kirjain2, kirjain3]
kirjaimet.sort()

# Yksinkertainen tapa tulostaa keskimmäinen kirjain
if (kirjain1 <= kirjain2 <= kirjain3) or (kirjain3 <= kirjain2 <= kirjain1):
    keskimmainen = kirjain2
elif (kirjain2 <= kirjain1 <= kirjain3) or (kirjain3 <= kirjain1 <= kirjain2):
    keskimmainen = kirjain1
else:
    keskimmainen = kirjain3

# Tulostetaan keskimmäinen kirjain
print(f"Keskimmäinen kirjain on {kirjaimet[1]}")