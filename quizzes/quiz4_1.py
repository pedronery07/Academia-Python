# Análise do índice de poluição

def total_por_pais(dic_poluicao):
    retorno = {}
    for paises in dic_poluicao.keys():
        retorno[paises] = 0
    for pais, cidades in dic_poluicao.items():
        soma = 0
        for pol in cidades.values():
            if pol < 0:
                soma += abs(pol)
            else:
                soma += pol
        retorno[pais] += soma
    return retorno