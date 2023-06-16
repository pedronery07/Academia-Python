def conta_ocorrencias(palavras):
    contagens = {}
    for p in palavras:
        if p not in contagens.keys():
            contagens[p] = 1
        else:
            contagens[p] += 1
    return contagens