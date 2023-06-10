from math import sqrt

def encontra_cateto(cat1, hip):
    cat2 = sqrt((hip)**2 - (cat1)**2)
    return cat2