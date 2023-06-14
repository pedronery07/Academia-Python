def soma_multiplos(a, b):
    soma = 0
    if a > b:
        maior = a*10
    else:
        maior = b*10
    i = 2
    while i <= maior:
        if i % a == 0 or i % b == 0:
            soma += i
        i += 1
    return soma