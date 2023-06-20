def detectar_acao(dicio, stopw):
    # Define lista de ações
    finais = ['ar', 'er', 'ir', 'or']
    retorno = {}
    i = 0
    for usuario, valor in dicio.items():
        # Cria para cada usuário um local no dicionário com uma lista vazia
        if usuario not in retorno.keys():
            retorno[usuario] = []
        for frase in valor.values():
            add = ''
            # Separa cada palavra dentro da frase
            f = frase.split()
            for palavra in f:
                # Percorre final de cada palavra para verificar se é uma ação
                final = palavra[len(palavra)-2::]
                # Se for o primeiro verbo a variável i muda pra 1
                if final in finais and i == 0:
                    add += palavra
                    i = 1
                # Se já existir o verbo e faltar a palavra seguinte entra na segunda condicional
                elif palavra not in stopw and i == 1:
                    add += " " + palavra
                    i = 2
            # Reseta variável i
            i = 0
            # Adiciona, se houver, a ação do usuário no dicionário
            if usuario not in retorno.keys() and add != '':
                retorno[usuario].append(add)
            elif usuario in retorno.keys() and add != "":
                retorno[usuario].append(add)
    return retorno