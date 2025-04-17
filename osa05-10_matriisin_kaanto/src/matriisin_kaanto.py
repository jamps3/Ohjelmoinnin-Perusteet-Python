def transponoi(matriisi: list):
    for i in range(len(matriisi)):
        for j in range(i + 1, len(matriisi[0])):
            matriisi[i][j], matriisi[j][i] = matriisi[j][i], matriisi[i][j]
    #return matriisi

if __name__ == "__main__":
    matriisi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #kaannetty = transponoi(matriisi)
    #for rivi in kaannetty:
    #    print(rivi)