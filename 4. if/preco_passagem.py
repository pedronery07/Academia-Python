d = int(input('Distância: '))
if d <= 200:
    preco = 0.5*d
elif d > 200:
    diferenca = d - 200
    preco = 100 + diferenca*0.45
print('{0:.2f}'.format(preco))