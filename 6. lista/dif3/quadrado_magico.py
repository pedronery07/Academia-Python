def quadrado_magico(l):
    #Verifica soma das linhas
    for i in range(len(l)):
        if i == 0:
            soma_linhas = sum(l[i])
        elif sum(l[i]) != soma_linhas:
            return False
    #Verifica soma das colunas
    i = len(l[i]) - 1
    while i >= 0:
        n = 0
        for j in range(len(l)):
            n += l[j][i]
        if n != soma_linhas:
            return False
        i -= 1
    #Verifica soma das diagonais
    s = 0
    for k in range(1, len(l)+1):
        s += l[k-1][k-1]
    if s == soma_linhas:
        return True
    else:
        return False