def tamanho_minimo(string, n):
    pal = string.split()
    l = []
    for p in pal:
        if len(p) > n:
            l.append(p)
    return l