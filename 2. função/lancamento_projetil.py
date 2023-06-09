from math import sin,sqrt
g = 9.8
def calcula_distancia_do_projetil(v,theta,y0):
    p1 = (v**2)/(2*g)
    p2 = 1 + sqrt((1 + (2*g)*(y0)/((v**2)*(sin(theta))**2)))
    p3 = sin(2*theta)
    return p1*p2*p3