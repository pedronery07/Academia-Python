def calcula_serie(a, b, n):
    soma = 1
    i = 1
    while i <= n-1:
        e = a**(i*b)
        soma += 1/(a**(i*b))
        i += 1
    return soma