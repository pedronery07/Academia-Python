def classifica_trigo(l):
    saida = []
    if l == []:
        return saida
    for i in range(0, len(l)):
        if l[i] <= 2:
            saida.append('T1')
        elif l[i] > 2 and l[i] <= 3:
            saida.append('T2')
        elif l[i] > 3 and l[i] <= 7:
            saida.append('T3')
        else:
            saida.append('FT')
    return saida 