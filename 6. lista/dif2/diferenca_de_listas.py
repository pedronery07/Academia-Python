def subtracao_de_listas(l1,l2):
    subtracao = []
    for i in range(len(l1)):
        if l1[i] not in l2:
            subtracao.append(l1[i])
    return subtracao