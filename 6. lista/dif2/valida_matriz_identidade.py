def eh_identidade(matriz):
    if len(matriz[0]) != len(matriz):
        return False
    for i in range(len(matriz)):
        if matriz[i][i] == 1 and sum(matriz[i]) == 1:
            continue
        else:
            return False
    return True