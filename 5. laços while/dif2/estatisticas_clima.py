dias = int(input("Quantos dias quer analisar? "))
contach = 0
frio = 0
contagc = 0
contacas = 0
i = 1

while i <= dias:
    ch = str(input('Choveu? '))
    temp = int(input('Temperatua mínima: '))
    gc = str(input('Tinha guarda-chuva? '))
    cas = str(input('TInha casaco? ')) 
    if temp < 20:
        frio += 1
    if ch == 'S' or ch == 's':
        contach += 1
    if gc == 'S' and ch == 'S':
        contagc += 1
    if cas == 'S' and temp < 20:
        contacas += 1
    i += 1

print(f'Choveu em {contach} de {dias} dias')
print(f'Fez frio em {frio} de {dias} dias')
print(f'Usou guarda-chuva em {contagc} de {contach} dias de chuva')
print(f'Usou casaco em {contacas} de {frio} dias de frio')