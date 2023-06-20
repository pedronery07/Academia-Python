def dias_de_racao(estoque, info_pet):
    if estoque == []:
        return 0
    idade = info_pet['idade']
    porte = info_pet['porte']
    consumo = info_pet['gramas_dia']
    if idade <= 1:
        classif = 'filhote'
    elif idade > 1 and idade < 8:
        classif = 'adulto'
    else:
        classif = 'idoso'
    dias = 0
    total_racao_kg = 0
    for racoes in estoque:
        if racoes['porte'] == porte and racoes['indicado'] == classif:
            total_racao_kg += racoes['qtde']
    total_racao_g = total_racao_kg*1000
    dias = total_racao_g // consumo
    return dias