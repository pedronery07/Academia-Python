def define_vencedores(sorteados, cartelas):
    pontuações = {}
    for jogador, cartela in cartelas.items():
        pontuação = 0
        for num in cartela:
            if num in sorteados:
                pontuação += 1
        pontuações[jogador] = pontuação
    maior = max(pontuações.values())
    venc = []
    for jogador, points in pontuações.items():
        if points == maior:
            venc.append(jogador)
    return venc