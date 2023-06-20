#UTILIZANDO SOMENTE LISTAS
def apurando_votos(cand, votos):
    k = 0
    resultados_validos = []
    while k < len(cand):
        resultados_validos.append(0)
        k += 1
    resultados_invalidos = [0]
    for i in range(len(votos)):
        if votos[i] not in cand:
            resultados_invalidos[0] += 1
    ind = 0
    for i in range(len(cand)):
        candidato = cand[i]
        if i != 0:
            ind += 1
        for j in range(len(votos)):
            if votos[j] == candidato:
                resultados_validos[ind] += 1
    maior_validos = max(resultados_validos)
    indice_vencedor = resultados_validos.index(maior_validos)
    vencedor_validos = cand[indice_vencedor]
    if resultados_invalidos[0] >= maior_validos:
        return 'CANCELADA'
    else:
        return vencedor_validos

#UTILIZANDO DICIONÁRIOS
def apurando_votos(cand, votos):
    resultados_validos = {}
    resultados_invalidos = {'inválidos' : 0}
    for i in range(len(votos)):
        if votos[i] not in cand:
            resultados_invalidos['inválidos'] += 1
        elif votos[i] not in resultados_validos.keys() and votos[i] in cand:
            resultados_validos[votos[i]] = 1
        else:
            resultados_validos[votos[i]] += 1
    maior1 = resultados_invalidos['inválidos']
    c = 0
    for k, v in resultados_validos.items():
        if c == 0:
            maior2 = v
            vencedor = k
            c = 1
        elif v > maior2:
            maior2 = v
            vencedor = k 
    if maior1 >= maior2:
        return 'CANCELADA'
    else:
        return vencedor