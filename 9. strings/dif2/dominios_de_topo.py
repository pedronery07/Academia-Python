def extrai_nome(email):
    name = ''
    for letra in email:
        if letra == "@":
            return name
        else:
            name += letra

def usuarios_por_pais(usuarios, significado):
    retorno = {}
    for u in usuarios:
        tam = len(u) - 1
        local = u[tam - 1::]
        nome = extrai_nome(u)
        pais = significado[local]
        if pais not in retorno.keys():
            retorno[pais] = [nome]
        else:
            retorno[pais].append(nome)
    return retorno