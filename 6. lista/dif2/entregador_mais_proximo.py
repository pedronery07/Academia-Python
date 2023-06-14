from math import sqrt
def entregador_mais_proximo(restaurante, entregadores):
    x_r = restaurante[0] 
    y_r = restaurante[1]
    ind = 0
    for i in range(len(entregadores)):
        x_e = entregadores[i][0]
        y_e = entregadores[i][1]
        dist = sqrt((x_r - x_e)**2 + (y_r -y_e)**2)
        if i == 0:
            menor = dist
        elif dist < menor:
            menor = dist
            ind = i
    return ind