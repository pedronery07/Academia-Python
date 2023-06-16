def melhor_valor(partes, inventario):
    l = []
    for serial in partes:
        menor = 0
        for pecas in inventario:
            if pecas['serial'] == serial or serial in pecas['equivalente']:
                if menor == 0:
                    menor = pecas['valor']
                elif pecas['valor'] < menor:
                    menor = pecas['valor']
        l.append(menor)
    return sum(l)