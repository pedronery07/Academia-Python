maior = 0
contador = 0
n0 = n = numero = 2

while n0 < 1000:
    while True:
        if n % 2 == 0:
            n = n/2
        elif n % 2 != 0:
            n = 3*n + 1
        contador += 1
        if n == 1:
            break
    if contador > maior:
        maior = contador
        numero = n0
    n0 += 1
    n = n0
    contador = 0

print(numero)