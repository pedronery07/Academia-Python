def total_do_semestre_por_bairro(dic_gastos):
    dic_semestre = {}
    for nome, gastos in dic_gastos.items():
        soma = sum(gastos[6:])
        dic_semestre[nome] = soma
    return dic_semestre

def bairro_mais_custoso(dici_gastos):
    dici_semestre = total_do_semestre_por_bairro(dici_gastos)
    i = 0
    for k, v in dici_semestre.items():
        if i == 0:
            bairro = k
            maior = v
            i = 1
        elif v > maior:
            maior = v
            bairro = k
    return bairro