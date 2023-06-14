def PiWallis(n):
    i = 1
    num = 2
    nom = 2
    den = 3
    while i < n:
        if i == 1:
            num *= nom/den
        elif i % 2 == 0:
            nom += 2
        else:
            den += 2
        if i != 1:
            num *= nom/den
        i += 1
    return num*2
    