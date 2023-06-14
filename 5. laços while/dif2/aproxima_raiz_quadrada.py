def aproxima_raiz(n):
    i = 1
    while i**2 < n:
        i += 1
    v1 = abs(n - (i-1)**2)
    v2 = abs(n - i**2)
    if v1 == 0:
        return i - 1
    elif v2 == 0:
        return i
    elif v1 < v2:
        return i - 1
    else:
        return i