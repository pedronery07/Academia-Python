def quantia_de_raizes(a, b, c):
    delta = b - 4*a*c
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0