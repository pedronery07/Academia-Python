def classifica_pedido(valor, dias, tam, avaria, capital):
    if valor <= 1000:
        if dias <= 1:
            if valor <= 150:
                if avaria == 'N' or avaria == 'n':
                    return 'normal'
                else:
                    return 'reclamacao'
            else:
                return 'reclamacao'
        else:
            return 'reclamacao'
    else:
        if dias <= 10:
            if avaria == 'N' or avaria == 'n':
                if valor <= 10000:
                    if valor <= 5000:
                        if capital == 'N' or capital == 'n':
                            return 'normal'
                        else:
                            if tam == 'P' or tam == 'p':
                                return 'reclamacao'
                            else:
                                return 'normal'
                    else:
                        return 'reclamacao'
                else:
                    return 'justica'
            else:
                return 'justica'
        else:
            return 'justica'