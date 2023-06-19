def lista_caracteres(string):
    l = []
    for letra in string:
        if letra not in l:
            l.append(letra)
    return l