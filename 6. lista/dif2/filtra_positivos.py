def filtra_positivos(l):
    saida = []
    for i in range(0, len(l)):
        if l[i] > 0:
            saida.append(l[i])
    return saida