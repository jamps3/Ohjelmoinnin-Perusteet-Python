def ilman_vokaaleja(mjono:str):
    vokaaliton = mjono.replace("a", "")
    vokaaliton = vokaaliton.replace("e", "")
    vokaaliton = vokaaliton.replace("i", "")
    vokaaliton = vokaaliton.replace("o", "")
    vokaaliton = vokaaliton.replace("u", "")
    vokaaliton = vokaaliton.replace("y", "")
    vokaaliton = vokaaliton.replace("å", "")
    vokaaliton = vokaaliton.replace("ä", "")
    vokaaliton = vokaaliton.replace("ö", "")
    return vokaaliton

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))