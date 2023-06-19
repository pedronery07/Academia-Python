def fase_grupos(grupos, continentes):
    # Cria dicionário de retorno e padrao para montagem do retorno
    paises = {}
    padrao = {
        'continente': '',
        'grupo': '',
        'pontuacao': 0,
        'gols pro': 0,
        'gols contra': 0,
        'saldo de gols': 0}
    # Percorre cada grupo da copa e lista de jogos
    for grupo, jogos in grupos.items():
        # Captura informação de cada jogo
        for jogo in jogos.values():
            time1 = jogo[0]
            gols_time1 = jogo[1]
            gols_time2 = jogo[2]
            time2 = jogo[3]
            # Monta base de dados com base na informação de cada jogo de cada grupo
            for continente, nacoes in continentes.items():
                if time1 in nacoes:
                    if time1 not in paises.keys():
                        padrao['continente'] = continente
                        padrao['grupo'] = grupo
                        padrao['gols pro'] = gols_time1
                        padrao['gols contra'] = gols_time2
                        padrao['saldo de gols'] = gols_time1 - gols_time2
                        if gols_time1 > gols_time2:
                            padrao['pontuacao'] = 3
                        elif gols_time1 == gols_time2:
                            padrao['pontuacao'] = 1
                        else:
                            padrao['pontuacao'] = 0
                        paises[time1] = padrao
                    else:
                        paises[time1]['gols pro'] += gols_time1
                        paises[time1]['gols contra'] += gols_time2
                        paises[time1]['saldo de gols'] += gols_time1 - gols_time2
                        if gols_time1 > gols_time2:
                            paises[time1]['pontuacao'] += 3
                        elif gols_time1 == gols_time2:
                            paises[time1]['pontuacao'] += 1
                            # Reseta dicionário padrão
                padrao = {
                    'continente': '',
                    'grupo': '',
                    'pontuacao': 0,
                    'gols pro': 0,
                    'gols contra': 0,
                    'saldo de gols': 0}
                if time2 in nacoes:
                    if time2 not in paises.keys():
                        padrao['continente'] = continente
                        padrao['grupo'] = grupo
                        padrao['gols pro'] = gols_time2
                        padrao['gols contra'] = gols_time1
                        padrao['saldo de gols'] = gols_time2 - gols_time1
                        if gols_time2 > gols_time1:
                            padrao['pontuacao'] = 3
                        elif gols_time2 == gols_time1:
                            padrao['pontuacao'] = 1
                        else:
                            padrao['pontuacao'] = 0
                        paises[time2] = padrao
                    else:
                        paises[time2]['gols pro'] += gols_time2
                        paises[time2]['gols contra'] += gols_time1
                        paises[time2]['saldo de gols'] += gols_time2 - gols_time1
                        if gols_time2 > gols_time1:
                            paises[time2]['pontuacao'] += 3
                        elif gols_time2 == gols_time1:
                            paises[time2]['pontuacao'] += 1
                            # Reseta dicionário padrão
                padrao = {
                    'continente': '',
                    'grupo': '',
                    'pontuacao': 0,
                    'gols pro': 0,
                    'gols contra': 0,
                    'saldo de gols': 0}
    return paises
