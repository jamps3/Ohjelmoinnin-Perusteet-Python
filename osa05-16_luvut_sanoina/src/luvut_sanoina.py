def lukukirja():
    ykköset = ['nolla', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi', 'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän']
    kymmenet = ['kymmenen', 'toista', 'kymmentä']
    sanakirja = {}
    for i in range(100):
        if i < 10:
            sanakirja[i] = ykköset[i]
        elif i == 10:
            sanakirja[i] = kymmenet[0]
        elif i < 20:
            sanakirja[i] = ykköset[i-10] + kymmenet[1]
        elif i > 19:
            if i % 10 == 0:
                sanakirja[i] = ykköset[i//10] + kymmenet[2]
            else:
                sanakirja[i] = ykköset[i//10] + kymmenet[2] + ykköset[i%10]
    return sanakirja