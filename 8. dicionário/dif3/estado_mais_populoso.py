def mais_populoso(pais):
    i = 0
    for estados, municipios in pais.items():
        pop_total = 0
        for pop in municipios.values():
            pop_total += pop
            if i == 0:
                maior = pop_total
                estado = estados
                i = 1
        if pop_total > maior:
            maior = pop_total
            estado = estados
    return estado