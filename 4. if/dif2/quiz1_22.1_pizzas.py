t = str(input("Tamanho [P/M/G]? "))
if t == 'P':
    preco = 50
elif t == 'M':
    preco = 70
elif t == 'G':
    preco = 90
aumento1 = 0
aumento2 = 0
aumento3 = 0
aumento4 = 0

br = str(input("Borda recheada [S/N]? "))
if br == 'S' and t == 'P':
    aumento1 = 50*0.15
elif br == 'S' and t == 'M':
    aumento1 = 70*0.15
elif br == 'S' and t == 'G':
    aumento1 = 90*0.15

aq = str(input("Adicional de queijo [S/N]? "))
if aq == 'S' and t == 'P':
    aumento2 = 50*0.10
elif aq == 'S' and t == 'M':
    aumento2 = 70*0.10
elif aq == 'S' and t == 'G':
    aumento2 = 90*0.10

r = str(input("Refrigerante [S/N]? "))
if r == 'S':
    aumento3 = 12

s = str(input("Sobremesa [S/N]? "))
if s == 'S':
    aumento4 = 20

preco_total = preco + aumento1 + aumento2 + aumento3 + aumento4
if t == 'G' and s == 'S':
    desconto = 0.07*preco_total
    preco_total -= desconto

print('{0:.2f}'.format(preco_total))
