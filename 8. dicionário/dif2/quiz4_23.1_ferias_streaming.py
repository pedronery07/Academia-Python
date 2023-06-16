def series_por_streaming(plat, atores, titulos):
    dici = {}
    ator_filme = {}
    for p in plat:
        if p not in dici.keys():
            dici[p] = []
    for i in range(len(atores)):
        ator_filme['performer'] = atores[i]
        ator_filme['title'] = titulos[i]
        dici[plat[i]].append(ator_filme)
        ator_filme = {}
    return dici