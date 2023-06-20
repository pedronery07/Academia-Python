def analisar_pilhas(dpilhas, lpilhas):
    status = []
    for pilha in lpilhas:
        m = pilha[0]
        t = pilha[1]
        v = pilha[2]
        if m not in dpilhas.keys():
            status.append('E')
            continue
        for marca, modelos in dpilhas.items():
            if marca == m:
                if t not in modelos.keys():
                    status.append('E')
                    continue
                else:
                    for tipo, info in modelos.items():
                        if tipo == t:
                            if v < info['volts']*(1-info['limite']):
                                if info['recarregavel'] == True:
                                    status.append('R')
                                else:
                                    status.append('D')
                            else:
                                status.append('N')
    return status