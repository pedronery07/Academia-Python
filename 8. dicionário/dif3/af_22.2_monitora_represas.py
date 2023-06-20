def monitora_represas(estado0, var):
    #Ajusta volumes iniciais de cada represa para litros
    for represa, vol in estado0.items():
        estado0[represa]['v0_litros'] = estado0[represa]['capacidade']*(estado0[represa]['volume']/100)
    vol_finais = {}
    #Percorre variações e devolve dicionário com volumes finais de cada represa em litros
    for rep, dias in var.items():
        vol_final = estado0[rep]['v0_litros']
        for variacoes in dias.values():
            vol_final += variacoes[0]
            vol_final -= variacoes[1]
        vol_finais[rep] = vol_final
    retorno = {}
    #Percorre dicionário com volumes finais de cada represa e devolve o dicionario com a classificação da cada represa
    for r, v in vol_finais.items():
        porcentagem_final = (vol_finais[r]/estado0[r]['capacidade'])*100
        if porcentagem_final <= 20:
            if 'emergencia' not in retorno.keys():
                retorno['emergencia'] = []
            retorno['emergencia'].append(r)
        elif porcentagem_final > 20 and porcentagem_final <= 50:
            if 'critico' not in retorno.keys():
                retorno['critico'] = []
            retorno['critico'].append(r)
        elif porcentagem_final > 50 and porcentagem_final <= 70:
            if 'atencao' not in retorno.keys():
                retorno['atencao'] = []
            retorno['atencao'].append(r)
        elif porcentagem_final > 70 and porcentagem_final <= 100:
            if 'normal' not in retorno.keys():
                retorno['normal'] = []
            retorno['normal'].append(r)
        else:
            if 'escoar' not in retorno.keys():
                retorno['escoar'] = []
            retorno['escoar'].append(r)
    return retorno