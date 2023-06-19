def calcula_premiacao(arrec_total, num_sorteados, apostas):
    premiacao = arrec_total*0.455
    # Monta dicionário de acertos para cada jogador
    pontos_jogadores = {}
    for jogador, numeros in apostas.items():
        for num in numeros:
            if num in num_sorteados:
                if jogador not in pontos_jogadores.keys():
                    pontos_jogadores[jogador] = 1
                else:
                    pontos_jogadores[jogador] += 1
    # Cria dicionários utilizados para construir o retorno
    retorno = {'6 acertos': 0,
    '5 acertos': 0,
    '4 acertos': 0}
    padrao = {
    'ganhadores': 0, 
    'premio por pessoa': 0
    }
    # Monta dicionário de retorno
    for i in range(4, 7):
        for acertos in pontos_jogadores.values():
            if acertos == i:
                padrao['ganhadores'] += 1
        # Exceção de ninguém acertar na aposta
        if padrao['ganhadores'] != 0:
            numero_venc = padrao['ganhadores']
            # Caso de 6 acertos
            if i == 6:
                padrao['premio por pessoa'] = 0.6*premiacao/numero_venc
            # Caso de 5 ou 4 acertos
            else:
                padrao['premio por pessoa'] = 0.2*premiacao/numero_venc
        indice = f'{i} acertos'
        # Adiciona no dicionário final a premiação de número de vencedores para cada número de acertos
        retorno[indice] = padrao
        # Reseta dicionário padrão
        padrao = {
            'ganhadores': 0, 
            'premio por pessoa': 0}
    return retorno