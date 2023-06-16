def compras_da_semana(receitas, lpratos):
    compras = {}
    for p in lpratos:
        ing = receitas[p]
        for i, n in ing.items():
            if i not in compras.keys():
                compras[i] = n
            else:
                compras[i] += n
    return compras