def encontra_maximo(matriz):
    maiores = []
    for i in range(len(matriz)):
        l = [abs(matriz[i][0]),abs(matriz[i][1]),abs(matriz[i][2])]
        maiores.append(max(l))
    return max(maiores)
