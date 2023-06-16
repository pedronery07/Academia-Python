def normaliza(mundo):
    dic_paises = {}
    for continente, paises in mundo.items():
        for nome, info in paises.items():
            info['continente'] = continente
            dic_paises[nome] = info
    return dic_paises