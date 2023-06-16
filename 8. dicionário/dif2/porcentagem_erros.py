def calcula_porcentagens(erros):
    porc = {}
    total = 0
    total = sum(erros.values())
    for k, v in erros.items():
        porc[k] = (v/total)*100
    return porc
    