from math import sqrt
def classifica(gabarito, dimensoes):
    classif = ''
    i = 0
    for peixe, padroes in gabarito.items():
        for dim in padroes:
            d = sqrt((dim[0]-dimensoes[0])**2 + (dim[1]-dimensoes[1])**2)
            if i == 0:
                classif = peixe
                menor = d
                i = 1
            elif d < menor:
                classif = peixe
                menor = d
    return classif