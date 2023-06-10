def calcula_aumento(salario):
    print(salario)
    if salario > 1250:
        aumento = salario*0.10
    elif salario <= 1250:
        aumento = salario*0.15
    return aumento