import random
d = 100

while d != 0:
    print(d)
    a = float(input('Aposta: '))
    if a == 0:
        break
    perg = str(input('Número ou paridade?' ))
    if perg == 'n':
        num = random.randint(0,36)
        tentativa = int(input('Digite o número: '))
        if num == tentativa:
            d += 35*a
        else:
            d -= a
    elif perg == 'p':
        escolha = str(input('Par ou ímpar: '))
        num = random.randint(0,36)
        if num % 2 == 0 and escolha == 'p':
            d += a
        elif num % 2 != 0 and escolha == 'i':
            d += a
        else:
            d -= a