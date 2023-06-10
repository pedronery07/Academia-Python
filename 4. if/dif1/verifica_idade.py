def verifica_idade(idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    elif idade >= 18 and idade < 21:
        return 'Liberado BRASIL'
    elif idade < 18:
        return 'Não está liberado'