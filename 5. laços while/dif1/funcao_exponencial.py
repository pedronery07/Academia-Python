from math import factorial

def calcula_euler(x, n):
    e = 1
    cont = 1
    while cont != n:
        e += x**cont/factorial(cont)
        cont += 1
    return e