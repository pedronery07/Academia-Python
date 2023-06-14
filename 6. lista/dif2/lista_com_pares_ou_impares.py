def verifica_lista(l):
    contapar = 0
    contaimpar = 0
    if l == []:
        return 'misturado'
    for i in range(len(l)):
        if l[i] % 2 == 0:
            contapar += 1
        elif l[i] % 2 != 0:
            contaimpar += 1
    if contapar > 0 and contaimpar > 0:
        return 'misturado'
    elif contaimpar > 0 and contapar == 0:
        return 'ímpar'
    else:
        return 'par'