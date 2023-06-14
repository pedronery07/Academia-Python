while True:
    inp = str(input('Digite algo: '))
    if inp == 'oi':
        print('Olá!')
    elif inp == 'bom dia':
        print('Bom dia')
    elif inp == 'site':
        print('Acesse https://insper.edu.br')
    elif inp == 'blackboard':
        print('Lá temos materiais, notas e muito mais!')
    elif inp == 'tchau' or inp == 'encerrar':
        print('Até logo')
        break
    else:
        print('Não sei como te ajudar!')
