from random import choice
def distribuir(n, l):
    saida = []
    while n > 0:
        num = choice(l)
        if num not in saida:
            saida.append(num)
            n -= 1
    return saida