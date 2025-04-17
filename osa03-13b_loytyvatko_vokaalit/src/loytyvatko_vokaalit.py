mjono = input("Anna merkkijono: ")
vokaalit = "aeo"
for vokaali in vokaalit:
    if vokaali in mjono:
        print(vokaali, "löytyy")
    else:
        print(vokaali, "ei löydy")
