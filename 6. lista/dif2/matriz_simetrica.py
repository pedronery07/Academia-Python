def eh_simetrica(matriz):
    if len(matriz) != len(matriz[0]):
        return False
    transposta = []
    for i in range(len(matriz)):
        transposta.append([])
        transposta[i].append(matriz[0][i])
    for k in range(1, len(matriz)):
        for i in range(len(matriz)):
            transposta[i].append(matriz[k][i])
    if transposta == matriz:
        return True
    else:
        return False