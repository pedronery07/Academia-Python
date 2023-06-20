def agrupa_por_nacionalidade(dici_atletas):
    nac = {}
    for nome, info in dici_atletas.items():
        if info['nacionalidade'] not in nac.keys():
            nac[info['nacionalidade']] = [nome]
        else:
            nac[info['nacionalidade']].append(nome)
    return nac