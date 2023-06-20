from math import trunc
def calcula_troco(valor, compra, l):
    notas = l[0:6]
    moedas = l[6:]
    troco = []
    dif = compra - valor
    v1 = trunc(dif)
    v2 = dif - v1
    #Analisa notas
    for i in range(len(notas)):
        quant = 0
        if v1 - notas[i] >= 0:
            quant = int(v1 // notas[i])
            v1 = v1 - quant*notas[i]
            troco.append(f'{quant} nota(s) de R$ {notas[i]}')
    if v1 == 1:
        troco.append('1 moeda(s) de R$ 1')
    for j in range(len(moedas)):
        quant = 0
        if v2 - moedas[j] >= 0:
            quant = int(v2//moedas[j])
            v2 = v2 - quant*moedas[j]
            troco.append(f'{quant} moeda(s) de R$ {moedas[j]}')
    return troco