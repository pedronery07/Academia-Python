# Altura do prédio
from math import radians, tan
def altura_do_predio(sombra, ang):
    ang_rad = radians(ang)
    cateto_oposto = tan(ang_rad)*sombra
    return cateto_oposto  