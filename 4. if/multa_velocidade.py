v = float(input('Velocidade do carro: '))
if v > 80:
    excesso = v - 80
    multa = 5*excesso
    print('O carro foi multado no valor de {0:.2f}'.format(multa))
else:
    print('Não foi multado')