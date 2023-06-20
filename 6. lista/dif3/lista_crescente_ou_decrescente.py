def classifica_lista(l):
    if len(l) < 2:
        return 'nenhum'
    cresc = 0
    decr = 0
    igual = 0
    for i in range(len(l)-1):
        if l[i+1] > l[i]:
            cresc += 1
        elif l[i+1] < l[i]:
            decr += 1
        else:
            igual += 1
    if cresc > 0 and decr == 0 and igual == 0:
        return 'crescente'
    elif decr > 0 and cresc == 0 and igual == 0:
        return 'decrescente'
    else:
        return 'nenhum'