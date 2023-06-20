def inverte_lista(l):
    saida = []
    i = len(l) - 1
    while i >= 0:
        saida.append(l[i])
        i -= 1
    return saida