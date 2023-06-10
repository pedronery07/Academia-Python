from math import sqrt, pi, e
def calcula_gaussiana(x, mi, sigma):
    valor = (1/(sigma*sqrt(2*pi)) * e**(-0.5*((x-mi)/sigma)**2))
    return valor