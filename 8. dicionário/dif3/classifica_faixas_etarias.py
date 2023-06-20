def agrupa_por_idade(pessoas):
    retorno = {}
    retorno['criança'] = []
    retorno['adolescente'] = []
    retorno['adulto'] = []
    retorno['idoso'] = []
    for nome, idade in pessoas.items():
        if idade <= 11:
            retorno['criança'].append(nome)
        elif idade >= 12 and idade <= 17:
            retorno['adolescente'].append(nome)
        elif idade >= 18 and idade <= 59:
            retorno['adulto'].append(nome)
        else:
            retorno['idoso'].append(nome)
    return retorno