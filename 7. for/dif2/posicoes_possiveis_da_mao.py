def posicoes_possiveis(mesa, pecas):
    retorno = []
    if mesa == []:
        for i in range(0, len(pecas)):
            retorno.append(i)
        return retorno
    else:
        pontaesq = mesa[0][0]
        pontadir = mesa[len(mesa)-1][1]
        for i in range(0, len(pecas)):
            if pecas[i][0] == pontadir or pecas[i][1] == pontaesq:
                retorno.append(i)
            elif pecas[i][0] == pontaesq or pecas[i][1] == pontadir:
                retorno.append(i)
    return retorno