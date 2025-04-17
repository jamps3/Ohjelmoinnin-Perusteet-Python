def palindromi(mjono):
    if mjono == mjono[::-1]:
        print(mjono + " on palindromi!")
        return True
    else:
        print("ei ollut palindromi")
        return False

while (True):
    vastaus = input("Anna palindromi: ")
    if (palindromi(vastaus)):
        break
