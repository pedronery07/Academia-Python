from random import choice
def sorteia_pais(dici_paises):
    l = []
    for pais in dici_paises.keys():
        l.append(pais)
    s = choice(l)
    return s
