def total_centro_custo(dic_fun):
    total = {}
    for gasto in dic_fun.values():
        centro = gasto['centro de custo']
        valor = gasto['valor']
        if centro not in total.keys():
            total[centro] = valor
        else:
            total[centro] += valor
    return total