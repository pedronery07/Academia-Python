def porcento(v):
    final = v * 1.1
    return final

valor = float(input("Qual o valor da conta: "))
final = porcento(valor)
print("Valor da conta com 10%: R$ {0:.2f}".format(final))