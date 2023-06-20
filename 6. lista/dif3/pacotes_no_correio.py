def pacotes_correio(remessa):
    #Verifica se há pacote perdido
    if len(remessa) != remessa[0][0]:
        return 'pacote perdido'
    for i in range(len(remessa)):
        if i > 0:
            numeracao += 1
        if i == 0:
            numeracao = remessa[i][1]
            tam = remessa[i][2]
        #Verifica se há algum pacote com numeração errada
        if remessa[i][1] != numeracao:
            return 'ordem errada'
        #Verifica se há algum pacote com tamanho diferente
        if remessa[i][2] != tam:
            return 'tamanho errado'
    return 'tudo certo'