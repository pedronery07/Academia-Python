def inverte_dicionario(pessoas):
    invertido = {}
    for pessoa, idade in pessoas.items():
        if idade not in invertido.keys():
            invertido[idade] = [pessoa]
        else:
            invertido[idade].append(pessoa)
    return invertido