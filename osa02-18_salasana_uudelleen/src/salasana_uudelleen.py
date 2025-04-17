password = input("Salasana: ")
while True:
    repeat_password = input("Toista salasana: ")
    if repeat_password == password:
        print("Käyttäjätunnus luotu!")
        break
    else:
        print("Ei ollut sama!")
