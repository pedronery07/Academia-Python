casa = float(input('Valor da casa: '))
salario = float(input('Salario: '))
anos = int(input('Anos: '))

meses = anos*12
prestacao = casa/meses

if prestacao > 0.30*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')