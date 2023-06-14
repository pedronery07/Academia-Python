# Aproximando o valor de pi
from math import sqrt
def aproxima(n):
    if n == 1:
        return sqrt(12)
    conta = 1
    termo = 3
    i = 2
    while i <= n:
        if i % 2 == 0:
            conta -= 1/(termo*(3**(i-1)))
        elif i % 2 != 0:
            conta += 1/(termo*(3**(i-1)))
        termo += 2
        i += 1
    return conta*(sqrt(12))