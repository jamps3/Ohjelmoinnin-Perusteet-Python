def histogrammi(mjono: str):
    kirjaimet = {}
    for i in mjono:
        if i not in kirjaimet:
            kirjaimet[i] = 1
        else:
            kirjaimet[i] += 1
    #print(kirjaimet)
    for kirjain, maara in kirjaimet.items():
        print(f"{kirjain} {maara * '*'}")

if __name__ == "__main__":
    
    sana = "saippuakauppias"
    histogrammi(sana)