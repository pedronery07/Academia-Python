from math import tan, radians

def area_pentagono(l):
    a = l/(2*tan(radians(36)))
    area = 5*(a*l)/2
    return area