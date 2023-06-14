def zera_negativos(l):
    l_saida = []
    for i in range(len(l)):
        if l[i] < 0:
            l_saida.append(0)
        else:
            l_saida.append(l[i])
    return l_saida