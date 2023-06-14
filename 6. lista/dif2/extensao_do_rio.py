from math import sqrt
def calcula_extensao(coordx, coordy):
    conta = 0
    for i in range(len(coordx)-1):
        x = coordx[i+1] - coordx[i]
        y = coordy[i+1] - coordy[i]
        conta += sqrt(x**2 + y**2)
    return conta