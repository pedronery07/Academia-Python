num_dias = int(input("digite o número de dias "))
n = 0
soma = 0
while n < num_dias:
    preco = float(input(f'Preço do dia {n}: '))
    if n == 0:
        melhor = n + 1
        pior = n + 1
        menor = preco
        maior = preco   
    elif preco < menor:
        menor = preco
        melhor = n + 1
    elif preco > maior:
        maior = preco
        pior = n + 1   
    soma += preco
    n += 1

media = soma/n
print(f'O dia {melhor} foi o melhor dia para compra')
print(f'O dia {pior} foi o pior dia para compra')
print('O preço médio cobrado foi de {:.2f}'.format(media))