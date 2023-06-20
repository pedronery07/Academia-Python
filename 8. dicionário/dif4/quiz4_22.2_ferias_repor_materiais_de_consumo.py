def precisa_repor(materiais, salas):
    reposicoes = {}
    for sala, info in salas.items():
        reposicao = {'sala':'',
        'material':''}
        for material, qtde in info['materiais'].items():
            if material in materiais.keys():
                minimo = materiais[material]['nivel minimo']
                pessoa = materiais[material]['responsavel']
                if minimo > qtde:
                    reposicao['sala'] = sala
                    reposicao['material'] = material
                    if pessoa not in reposicoes.keys():
                        reposicoes[pessoa] = [reposicao]
                    else:
                        reposicoes[pessoa].append(reposicao)
                    reposicao = {'sala':'',
                                 'material':''}
    return reposicoes