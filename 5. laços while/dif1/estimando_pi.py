from math import sqrt
def calcula_pi(n):
    i = 1
    s = 0
    while i <= n:
        s += 6/i**2
        i += 1
    return sqrt(s)