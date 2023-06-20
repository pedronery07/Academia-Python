def mais_medalhas(lista_atletas):
    i = 0
    for atleta in lista_atletas:
        if i == 0:
            nac = atleta['nacionalidade']
            maior = atleta['ouro']
        elif atleta['ouro'] > maior:
            maior = atleta['ouro']
            nac = atleta['nacionalidade']
    return nac