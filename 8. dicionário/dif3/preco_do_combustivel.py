def contabiliza_combustivel(combustiveis):
    saida = {}
    dic_custos = {}
    for info in combustiveis.values():
        tipo = info['tipo']
        lit = info['litros']
        custo = info['custo']
        if tipo not in saida.keys():
            saida[tipo] = {}
            saida[tipo]['total litros'] = lit
            saida[tipo]['custo por litro'] = 0
            dic_custos[tipo] = custo
        else:
            saida[tipo]['total litros'] += lit
            dic_custos[tipo] += custo
    for t in saida.keys():
        saida[t]['custo por litro'] = dic_custos[t]/saida[t]['total litros']
    return saida