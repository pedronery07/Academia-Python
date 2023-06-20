def apura_area(votos_por_secao, candidatos_por_partido):
    votos_por_area = {}
    resultados = {}
    # Manipulando dados por área e candidato num dicionário resultados
    for votos in votos_por_secao:
        area = votos['area']
        if area not in resultados.keys():
            resultados[area] = votos['candidatos']
        else:
            for cand, num in votos['candidatos'].items():
                if cand not in resultados[area].keys():
                    resultados[area][cand] = num
                else:
                    resultados[area][cand] += num
    # Votos brancos e nulos no dicionário de retorno
    for area, results in resultados.items():
        if area not in votos_por_area.keys():
            votos_por_area[area] = {}
        votos_por_area[area]['nulos'] = results['nulos']
        votos_por_area[area]['brancos'] = results['brancos']
        # Votos por partido no dicionário de retorno
        for candidato, votes in results.items():
            for partido, lista in candidatos_por_partido.items():
                if candidato in lista:
                    if partido not in votos_por_area[area].keys():
                        votos_por_area[area][partido] = votes
                    else:
                        votos_por_area[area][partido] += votes
    return votos_por_area