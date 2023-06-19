pergunta = True
vogais = 'aeiou'

while pergunta:
    palavra = str(input('Palavra: '))
    if palavra == 'fim':
        print('Até a próxima')
        pergunta = False
    else:
        n = ''
        for p in palavra:
            if p not in vogais:
                n += p
        print(n)