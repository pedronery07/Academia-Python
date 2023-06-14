dias = int(input('Dias a analisar: '))
i = 0
s = 0
while i != dias:
    p = float(input(f'Preço do dia {i}: '))
    s += p
    i += 1
media = s/i
print(f'O preço médio cobrado foi de {media:.2f}')