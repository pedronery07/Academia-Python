#USANDO WHILE
def numero_no_indice(l):
    saida = []
    i = 0
    while i < len(l) :
        if l[i] == i:
            saida.append(l[i])
        i += 1
    return saida

#USANDO FOR
#def numero_no_indice(l):
#    saida = []
#    for i in range(0, len(l)):
#        if l[i] == i:
#            saida.append(l[i])
#    return saida