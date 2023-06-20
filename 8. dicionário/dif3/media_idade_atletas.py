def calcula_media(dici_atletas, pais):
    soma = 0
    n = 0
    for info in dici_atletas.values():
        if info['nacionalidade'] == pais:
            soma += info['idade'] 
            n += 1
    return soma/n