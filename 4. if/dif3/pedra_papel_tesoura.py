def pedra_papel_tesoura(j1, j2):
    l = ['pedra','papel','tesoura']
    if j1 not in l or j2 not in l:
        return 'Escolha pedra, papel ou tesoura para jogar'
    if j1 == j2:
        return 'empate'
    if j1 == 'pedra':
        if j2 == 'papel':
            return 'dois'
        else:
            return 'um'
    elif j1 == 'papel':
        if j2 == 'pedra':
            return 'um'
        else:
            return 'dois'
    elif j1 == 'tesoura':
        if j2 == 'papel':
            return 'um'
        else:
            return 'dois'