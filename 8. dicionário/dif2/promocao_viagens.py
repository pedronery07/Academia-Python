def promocao_viagens(dic_destinos):
    dic_final = {}
    for destino, l in dic_destinos.items():
        ranking = l[0]
        preco = l[1]
        preco_final = preco - (preco*ranking*0.1)
        dic_final[destino] = preco_final
    return dic_final