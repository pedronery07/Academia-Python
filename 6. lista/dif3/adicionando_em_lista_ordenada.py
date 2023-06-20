def adiciona_em_ordem(pais, dist, lpaises):
    #Caso de lista vazia
    if lpaises == []:
        lpaises.append([pais, dist])
        return lpaises
    #Caso de país já estando na lista
    elif pais in lpaises:
        return lpaises
    #Caso de a distância do país ser maior que qualquer uma das distâncias dadas
    elif lpaises[len(lpaises)-1][1] < dist:
        lpaises.append([pais,dist])
        return lpaises
    #Caso de a distância do país ser menor que qualquer uma das distânias dadas
    elif lpaises[0][1] > dist:
        lpaises.insert(0, [pais, dist])
        return lpaises
    l_atualizada = []
    #Caso de o país ser inserido no meio da lista dada
    for i in range(len(lpaises)-1): 
        if lpaises[i][1] < dist and lpaises[i+1][1] > dist:
            l_atualizada.append(lpaises[i])
            l_atualizada.append([pais,dist])
        else:
            l_atualizada.append(lpaises[i])
    l_atualizada.append(lpaises[len(lpaises)-1])
    return l_atualizada