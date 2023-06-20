def estritamente_crescente(l):
    saida = []
    if l == []:
        return []
    for i in range(len(l)):
        if i == 0:
            saida.append(l[i])
        elif l[i] > saida[len(saida)-1]:
            saida.append(l[i])
        else:
            continue
    return saida