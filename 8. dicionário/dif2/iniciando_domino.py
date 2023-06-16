def inicia_jogo(jogadores,pecas):
    dic = {}
    j = {}
    m = []
    n = 0
    while n < jogadores:
        l = []
        for i in range(0, 7):
            l.append(pecas[i])
        for i in range(0, 7):
            del pecas[0]
        j[n] = l
        n += 1
    dic['jogadores'] = j
    dic['monte'] = pecas
    dic['mesa'] = []
    return dic