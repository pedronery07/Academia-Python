def distancia(x1, y1, x2, y2, p):
    d = (abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p)
    return d