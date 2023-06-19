def atualiza_telefone(telefone):
    if "-" in telefone:
        if len(telefone) == 9:
            digitos = telefone.split()
            digitos.insert(0, '9')
            telefone = ''.join(digitos)
    else:
        if len(telefone) == 8:
            digitos = telefone.split()
            digitos.insert(0, '9')
            telefone = ''.join(digitos)
    return telefone