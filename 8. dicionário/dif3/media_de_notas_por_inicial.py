def medias_por_inicial(dici_alunos):
    analise = {}
    qtde = {}
    soma = {}
    for nome, nota in dici_alunos.items():
        if nome[0] not in analise.keys():
            analise[nome[0]] = nota
            qtde[nome[0]] = 1
            soma[nome[0]] = nota
        else:
            qtde[nome[0]] += 1
            soma[nome[0]] += nota
            analise[nome[0]] = soma[nome[0]]/qtde[nome[0]]
    return analise