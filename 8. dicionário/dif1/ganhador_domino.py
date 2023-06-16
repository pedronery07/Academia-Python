def verifica_ganhador(dic):
    for k, v in dic.items():
        if v == []:
            return k
    return -1