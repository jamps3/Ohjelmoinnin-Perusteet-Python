def kaanna(sanakirja: dict):
    kaannetty_sanakirja = {}
    for avain, arvo in sanakirja.items():
        kaannetty_sanakirja[arvo] = avain
    sanakirja.clear()
    sanakirja.update(kaannetty_sanakirja)