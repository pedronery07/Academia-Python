#MODO 1
def total_do_semestre_por_bairro(dic_gastos):
    dic_semestre = {}
    for nome, gastos in dic_gastos.items():
        soma = sum(gastos[6:])
        dic_semestre[nome] = soma
    return dic_semestre

#MODO2
#def total_do_semestre_por_bairro(dic_gastos):
#    dic_semestre = {}
#    for nome, gastos in dic_gastos.items():
#        soma = 0
#        for i in range(6, 12):
#            soma += gastos[i]
#        dic_semestre[nome] = soma
#    return dic_semestre