from math import sin
import math

def haversine(r, phi1, lam1, phi2, lam2):
    rp1 = math.radians(phi1)
    rp2 = math.radians(phi2)
    rl1 = math.radians(lam1)
    rl2 = math.radians(lam2)
    p1 = (rp2 - rp1) / 2
    p2 = (rl2 - rl1) / 2
    soma = (math.sin(p2)**2 ) * math.cos(rp2) * math.cos(rp1)
    raiz = (math.sin(p1)**2) + soma
    d = 2*r * math.asin(math.sqrt(raiz))
    return d