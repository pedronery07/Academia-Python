def alunos_impares(l_alunos):
    l_impar = []
    for i in range(len(l_alunos)):
        if i % 2 != 0:
            l_impar.append(l_alunos[i])
    return l_impar