def mais_lancamentos(series, ano):
    dic_series = {}
    for serie in series:
        plat = serie['plataforma']
        year = serie['ano_estreia']
        if year == ano:
            if plat not in dic_series.keys():
                dic_series[plat] = 1
            else:
                dic_series[plat] += 1
    retorno = []
    if dic_series == {}:
        return retorno
    n = max(dic_series.values())
    for p, num in dic_series.items():
        if num == n:
            retorno.append(p)
    return retorno