# Calculadora simplificada
conta = 0
valor = 0
i = 0
while True:
    if i == 0:
        num1 = int(input('número: '))
    op = str(input('operador: '))
    while op not in '+-*=/':
        print("Deveria ser um dos seguintes operadores: + - / * ou o =")
        op = str(input('operador: '))
    if op == '=':
        break
    num2 = int(input('número: '))
    if op == '+':
        if i == 0:
            conta = num1 + num2 
        else:
            valor += num2
    elif op == '*':
        if i == 0:
            conta = num1 * num2 
        else:
            valor *= num2
    elif op == '-':
        if i == 0:
            conta = num1 - num2
        else:
            valor -= num2
    elif op == '/':
        if i == 0:
            conta = num1/num2
        else:
            valor /= num2
    verifica = 0
    if i == 0:
        valor += conta
    i = 1
print(valor)