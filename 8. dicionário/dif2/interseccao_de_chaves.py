def interseccao_chaves(d1, d2):
    l = []
    for k in d1.keys():
        if k in d2.keys():
            l.append(k)
    return l