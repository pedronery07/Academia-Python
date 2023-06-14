def intersecao_de_lista(l1, l2):
    retorno = []
    for elemento in l1:
        for e in l2:
            if e == elemento:
                if e not in retorno:
                    retorno.append(elemento)
    return retorno