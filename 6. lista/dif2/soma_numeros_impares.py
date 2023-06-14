#USANDO WHILE
def soma_impares(lista):
    limp = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            limp.append(lista[i])
        i += 1
    return sum(limp)

#USANDO FOR
#def soma_impares(lista):
#    limp = []
#    for i in range(0,len(lista)):
#        if lista[i] % 2 != 0:
#            limp.append(lista[i])
#    somalimp = sum(limp)
#    return somalimp