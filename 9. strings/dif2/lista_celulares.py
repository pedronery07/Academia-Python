def lista_celulares(lista):
    l = []
    for numero in lista:
        if len(numero) == 13 or len(numero) == 14:
            if numero[5] == '9':
                l.append(numero[5:])
        elif len(numero) == 10 or len(numero) == 11:
            if numero[2] == '9':
                l.append(numero[2:])
        else:
            if numero[0] == '9':
                l.append(numero)
    return l