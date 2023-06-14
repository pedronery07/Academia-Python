# Acompanhamento surpresa 
tam = str(input('Tamanho do bolo: '))
if tam == 'XP':
    unidade = 5
elif tam == 'P':
    unidade = 7
elif tam == 'M':
    unidade = 20
elif tam == 'G':
    unidade = 31
else:
    unidade = 50
orcamento = int(input('Orçamento: '))
q_bolos = orcamento//unidade
sobra = orcamento - q_bolos*unidade
if sobra == 0:
    print('sem acompanhamento')
else:
    cheesecake = 0
    cupcake = 0
    if q_bolos > 4:
        while sobra > 1:
            sobra -= 2
            cupcake += 1
        if sobra != 0 and cupcake == 0:
            print('1 banoffee')
        elif sobra != 0 and cupcake != 0:
            print(f'{cupcake} cupcake')
            print('1 banoffee')
        else:
            print(f'{cupcake} cupcake')
    else:
        while sobra > 1:
            sobra -= 2
            cheesecake += 1
        if sobra != 0 and cheesecake == 0:
            print('1 brownie')
        elif sobra != 0 and cheesecake != 0:
            print(f'{cheesecake} cheesecake')
            print('1 brownie')
        else:
            print(f'{cheesecake} cheesecake')