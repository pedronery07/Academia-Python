def conta_bigramas(string):
    saida = {}
    for i in range(len(string)-1):
        bigrama = string[i] + string[i+1]
        if bigrama not in saida.keys():
            saida[bigrama] = 1
        else:
            saida[bigrama] += 1
    return saida