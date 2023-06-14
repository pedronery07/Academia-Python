def gera_direcoes(coordx, coordy):
    retorno = []
    for i in range(len(coordx)-1):
        x1 = coordx[i]
        x2 = coordx[i+1]
        y1 = coordy[i]
        y2 = coordy[i+1]
        #NORTE
        if x1 == x2 and y2 - 1 == y1:
            retorno.append('sul')
        #SUL
        elif x1 == x2 and y2 + 1 == y1:
            retorno.append('norte')
        #LESTE
        elif y1 == y2 and x2 - 1 == x1:
            retorno.append('leste')
        #OESTE
        elif y1 == y2 and x2 + 1 == x1:
            retorno.append('oeste')
        #SUDOESTE
        elif y1 + 1 == y2 and x2 + 1 == x1:
            retorno.append('sudoeste')
        #SUDESTE
        elif y1 + 1 == y2 and x2 - 1 == x1:
            retorno.append('sudeste')
        #NOROESTE
        elif y1 - 1 == y2 and x2 + 1 == x1:
            retorno.append('noroeste')
        #NORDESTE
        elif y1 - 1 == y2 and x2 - 1 == x1:
            retorno.append('nordeste')
    return retorno