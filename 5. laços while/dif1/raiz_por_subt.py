def raiz_quadrada(n):
    sub = 1
    cont = 0
    while n > 0:
        n -= sub
        sub += 2
        cont += 1
    return cont