def quantos_caminhoes(pesos):
    caminhoes = []
    for i in range(len(pesos)-1):
        if i == 0:
            peso = pesos[i]
        else:
            peso += pesos[i]
        if peso + pesos[i+1] > 2000:
            caminhoes.append(peso)
            peso = 0
    return len(caminhoes) + 1