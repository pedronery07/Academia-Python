def encontra_servico(email):
    servico = ''
    ind = email.index('@')
    email = email[ind+1::]
    ponto = email.index('.')
    servico += email[:ponto] 
    return servico

def perfis_profissionais(censo):
    dados = {}
    auxiliar = {'média salarial': [],
    'tempo médio de serviço': [],
    'servidores': []}
    for info in censo.values():
        ramo = info['ramo']
        sal = info['salário']
        anos = info['anos de serviço']
        email = info['e-mail']
        if ramo not in dados.keys():
            auxiliar['média salarial'].append(sal)
            auxiliar['tempo médio de serviço'].append(anos)
            serv = encontra_servico(email)
            auxiliar['servidores'].append(serv)
            dados[ramo] = auxiliar
        else:
            dados[ramo]['média salarial'].append(sal)
            dados[ramo]['tempo médio de serviço'].append(anos)
            serv = encontra_servico(email)
            if serv not in dados[ramo]['servidores']:
                dados[ramo]['servidores'].append(serv)
        auxiliar = {'média salarial': [],
                    'tempo médio de serviço': [],
                    'servidores': []}
    # Transforma dados
    for ramo, info in dados.items():
        soma = sum(info['média salarial'])
        tam = len(info['média salarial'])
        dados[ramo]['média salarial'] = soma/tam
        soma = sum(info['tempo médio de serviço'])
        tam = len(info['tempo médio de serviço'])
        dados[ramo]['tempo médio de serviço'] = soma/tam
    return dados