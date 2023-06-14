from math import sqrt, trunc

def quadrados_no_intervalo(a, b):
    i = a
    conta = 0
    while i <= b:
        raiz = sqrt(i)
        inteiro = trunc(raiz)
        if inteiro**2 == i:
            conta += 1 
        i += 1
    return conta